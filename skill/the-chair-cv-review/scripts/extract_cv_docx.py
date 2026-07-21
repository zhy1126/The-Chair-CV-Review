Exit code: 0
Wall time: 1.9 seconds
Output:
#!/usr/bin/env python3
"""Extract CV text and review risks from a DOCX without external dependencies."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
CP = "{http://schemas.openxmlformats.org/package/2006/metadata/core-properties}"
DC = "{http://purl.org/dc/elements/1.1/}"
DCTERMS = "{http://purl.org/dc/terms/}"
EP = "{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}"

PLACEHOLDER_PATTERNS = {
    "blank contact field": re.compile(r"E-?mail:\s*(?:[｜|]\s*)?Tel:\s*(?:$|\n)", re.I | re.M),
    "question-mark date": re.compile(r"(?:^|\s)0?\?\.20\d\?|\b20\?\?\b", re.I),
    "generic XX placeholder": re.compile(r"\bX{2,}\b"),
    "generic course placeholder": re.compile(r"\bCourse\s+[A-Z](?:\s*\(\d+\))?", re.I),
    "draft marker": re.compile(r"\b(?:TBD|TBC|TODO|PLACEHOLDER|INSERT)\b", re.I),
}


def read_xml(zf: zipfile.ZipFile, name: str):
    try:
        return ET.fromstring(zf.read(name))
    except KeyError:
        return None


def visible_paragraph_text(p: ET.Element) -> str:
    parts: list[str] = []
    for node in p.iter():
        if node.tag == f"{W}del":
            continue
        if node.tag == f"{W}t" and node.text:
            deleted_ancestor = False
            # ElementTree has no parent pointer; deleted text normally uses w:delText,
            # while visible and inserted content uses w:t.
            if not deleted_ancestor:
                parts.append(node.text)
        elif node.tag == f"{W}tab":
            parts.append("\t")
        elif node.tag in {f"{W}br", f"{W}cr"}:
            parts.append("\n")
    return "".join(parts).strip()


def extract_part_paragraphs(root: ET.Element | None) -> list[str]:
    if root is None:
        return []
    result = []
    for p in root.iter(f"{W}p"):
        text = visible_paragraph_text(p)
        if text:
            result.append(text)
    return result


def text_of(root: ET.Element | None, tag: str) -> str:
    if root is None:
        return ""
    node = root.find(tag)
    return node.text.strip() if node is not None and node.text else ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()

    path = args.docx.resolve()
    if not path.is_file():
        parser.error(f"file not found: {path}")
    if path.suffix.lower() != ".docx":
        parser.error("input must be a .docx file")

    with zipfile.ZipFile(path) as zf:
        document_root = read_xml(zf, "word/document.xml")
        paragraphs = extract_part_paragraphs(document_root)

        comments_root = read_xml(zf, "word/comments.xml")
        comments = []
        if comments_root is not None:
            for comment in comments_root.findall(f"{W}comment"):
                comments.append(
                    {
                        "id": comment.attrib.get(f"{W}id", ""),
                        "author": comment.attrib.get(f"{W}author", ""),
                        "date": comment.attrib.get(f"{W}date", ""),
                        "text": " ".join(extract_part_paragraphs(comment)),
                    }
                )

        headers_footers = {}
        for name in zf.namelist():
            if re.fullmatch(r"word/(?:header|footer)\d+\.xml", name):
                headers_footers[name] = extract_part_paragraphs(read_xml(zf, name))

        insertions = sum(1 for _ in document_root.iter(f"{W}ins")) if document_root is not None else 0
        deletions = sum(1 for _ in document_root.iter(f"{W}del")) if document_root is not None else 0
        table_count = sum(1 for _ in document_root.iter(f"{W}tbl")) if document_root is not None else 0

        core = read_xml(zf, "docProps/core.xml")
        app = read_xml(zf, "docProps/app.xml")
        metadata = {
            "title": text_of(core, f"{DC}title"),
            "author": text_of(core, f"{DC}creator"),
            "last_modified_by": text_of(core, f"{CP}lastModifiedBy"),
            "created": text_of(core, f"{DCTERMS}created"),
            "modified": text_of(core, f"{DCTERMS}modified"),
            "reported_pages": text_of(app, f"{EP}Pages"),
        }

    full_text = "\n".join(paragraphs)
    placeholder_risks = []
    for label, pattern in PLACEHOLDER_PATTERNS.items():
        matches = sorted(set(m.group(0).strip() for m in pattern.finditer(full_text)))
        if matches:
            placeholder_risks.append({"type": label, "matches": matches[:10]})

    section_terms = {
        "education",
        "publications",
        "publications and conferences",
        "publications/conferences",
        "conference presentations",
        "research experience",
        "research experiences",
        "internship",
        "internships",
        "professional experience",
        "work experience",
        "honors",
        "honours",
        "awards",
        "scholarships",
        "scholarships and honors",
        "scholarships & honors",
        "skills",
        "activities",
        "activity",
    }
    detected_sections = []
    for paragraph in paragraphs:
        normalized = paragraph.lower().strip(" :&/")
        if len(paragraph) <= 60 and normalized in section_terms:
            detected_sections.append(paragraph)

    result = {
        "path": str(path),
        "paragraph_count_including_table_cells": len(paragraphs),
        "word_count": len(re.findall(r"\b[\w'-]+\b", full_text)),
        "table_count": table_count,
        "insertions": insertions,
        "deletions": deletions,
        "comments": comments,
        "headers_and_footers": headers_footers,
        "metadata": metadata,
        "detected_section_candidates": detected_sections,
        "placeholder_risks": placeholder_risks,
        "text": full_text,
    }
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


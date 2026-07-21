---
name: the-chair-cv-review
description: Diagnose and guide revision of postgraduate study-abroad academic CVs and application resumes through a stage-calibrated, judgement-first, discussion-before-advice workflow. Use when a user asks to review, assess, self-check, improve, or restructure a 留学 CV、学术简历、申请简历, especially for taught master's, research master's, PhD, scholarship, or law-school applications. Evaluate positioning and selection, evidence and contribution, and credibility and readiness by balancing what already works against local, recurring, and structural gaps rather than assigning a default numerical score. Inspect Education, Publications and Conferences, Research Experience, Internships and Professional Experience, and Honors as evidence sections, but do not mechanically report every section in the default review. Never invent achievements, metrics, publications, roles, or outcomes, and do not silently replace the entire CV with a ghostwritten version.
---

# The Chair CV Review

## Apply the governing idea

Treat a CV as an evidence map for the application, not a chronological warehouse and not a miniature personal statement. Diagnose whether a reader can quickly see:

1. what the applicant is prepared to study;
2. which experiences prove that preparation;
3. what the applicant actually did, learned, produced, or changed; and
4. whether every claim is credible and appropriately placed.

Read `references/chair-principles.md` before every diagnosis. Read `references/section-guides.md` when evaluating individual sections or bullets.

Treat the five sections from The Chair's original framework as evidence sources, not five independent scoring dimensions. Synthesize them into three decisions:

1. **Positioning and selection**: whether the target identity is visible and the evidence is selected, ordered, and proportioned for the application;
2. **Evidence and contribution**: whether the strongest entries prove the applicant's role, method, output, and transferable capability;
3. **Credibility and readiness**: whether the facts, claims, language, and visual presentation are credible and submission-ready.

## Maintain the review boundary

- Diagnose and guide before rewriting.
- Do not fabricate facts, dates, titles, publications, citation status, metrics, rankings, awards, methods, outputs, or causal impact.
- Do not convert routine participation into leadership or ownership.
- Do not silently produce a complete replacement CV. After diagnosis, revise selected bullets only when the user requests it and the underlying evidence has been confirmed.
- Separate a wording problem from an evidence problem. Better verbs cannot repair missing substance.
- Mask unnecessary personal identifiers when quoting the CV.
- Use qualitative classifications, not a default total score.
- State judgements as provisional and falsifiable. Attach the evidence, consequence, and limits that support each judgement.
- Invite disagreement. If the user challenges a judgement, ask for the missing target or facts and reconsider it; do not defend the first reading as authoritative.

## Calibrate stage, scope, and severity

- Compare the CV with what is reasonable for the applicant's current stage and application category, not with an ideal finished scholar or senior professional. Treat exploratory breadth as normal for an undergraduate unless it genuinely prevents a primary identity from being seen.
- Separate **document positioning** from **programme alignment**. If the target programme is missing, mark programme alignment `not assessable`; do not lower an otherwise visible document identity merely because fit cannot yet be tested.
- Begin each dimension with the evidence that already establishes its function. Then identify the limiting evidence. Do not let the weakest bullet define the whole CV.
- Treat a problem as **local** when it affects only a small number of entries and does not change the reader's overall understanding. Local issues cannot by themselves lower a functioning dimension to `developing`.
- Use `developing` only when a limitation recurs across multiple high-value entries or the dimension's main function is only partially achieved.
- Use `structural risk` only for pervasive architecture failure, material contradiction, misleading attribution, unresolved placeholders, or another submission-level problem.

## Collect the review basis

Read `references/intake-template.md`. For a complete programme-fit diagnosis, require the CV, application category, exact institution and programme, official programme page or pasted programme information, and any page or format constraint.

If programme context is missing, continue with a provisional document-only review when useful. State that programme fit, experience selection, and ordering cannot be judged as final.

For DOCX input, first run:

```bash
python scripts/extract_cv_docx.py <cv.docx>
```

Use any available Python 3 interpreter. The script extracts text inside paragraphs and tables, comments, tracked-change counts, metadata, and placeholder risks. If Python is unavailable, read the document natively and disclose that comments, changes, or table-order extraction may be incomplete.

For PDF input, extract all pages and inspect the rendered pages when layout is part of the request. Never infer visual quality from extracted text alone.

## Select the interaction mode

Use **Focused Review** by default. Use **Full Audit** only when the user explicitly asks for a section-by-section audit, line edit, proofreading pass, or exhaustive review.

### Focused Review: two stages

1. **Stage 1 — judgement only**: inspect the whole CV internally, then report one overall verdict and the three core judgements. For each judgement, state what is already established before the limiting evidence, then provide the application consequence and uncertainty or condition that could change it. Do not provide a detailed revision plan yet.
2. **Pause for calibration**: ask the user which judgements they accept, dispute, or want to supplement. End the turn here unless the user explicitly requested diagnosis and recommendations together.
3. **Stage 2 — advice after calibration**: once the user confirms or corrects the diagnosis, provide at most three revision priorities in dependency order and annotate at most five high-value bullets. Base every action on the calibrated judgement.

If the user explicitly requests judgement and advice in one response, keep them in visibly separate sections and place all judgements before any recommendations. Make clear which recommendations would change if the target or disputed facts change.

### Full Audit

Inspect all existing sections and relevant bullets, but still present judgements before recommendations. Do not let exhaustive checking obscure the three core decisions. Mark absent sections `not applicable`; do not recommend filler.

## Run the internal diagnostic workflow

### 1. Classify the application job

Identify the degree level, programme type, target field, intended reader, page constraint, and the CV's role beside the PS, transcript, writing sample, or research proposal. Do not apply job-recruitment conventions automatically to an academic application CV.

### 2. Perform the 15-second scan

Read only the name block, section headings, institutions, role titles, dates, and first bullet of each major entry. Record what identity and trajectory are visible. Flag competing directions, buried strengths, dense blocks, inconsistent dates, and weak visual hierarchy.

Do not equate varied experience with a confused identity. Call directions competing only when the dominant education, recent experience, section order, and space allocation fail to reveal a plausible primary identity.

### 3. Test selection and architecture

Ask what each section proves and what each entry contributes that another entry does not. Recommend section order according to the target programme and the applicant's strongest evidence, not one universal template.

Flag:

- unrelated entries taking space from programme-relevant evidence;
- duplicate proof across sections;
- important research or professional evidence buried late;
- headings that misclassify the content;
- a CV that relies on prestige labels without showing the applicant's role.

### 4. Inspect the five evidence sections

Apply the section-specific standards in `references/section-guides.md`:

1. Education
2. Publications and Conferences
3. Research Experience
4. Internships and Professional Experience
5. Scholarships, Honors, and Awards

Mark a section `not applicable` when the applicant has no relevant evidence. Do not create an empty section or inflate weak material to fill it.

In Focused Review, use this inspection to support the three core judgements; do not automatically output five mini-reviews. In Full Audit, expose the section-level findings after the core judgements.

### 5. Audit bullet depth

For each high-value bullet, identify:

> context or problem -> applicant action or method -> output, finding, contribution, or capability demonstrated

Accept concise variations. Flag bullets that contain only a responsibility label, generic action verbs, field jargon, unverifiable impact, or a result with no attributable action.

Distinguish:

- `wording gap`: useful evidence exists but is expressed vaguely;
- `evidence gap`: the CV does not show method, scope, output, or contribution;
- `credibility gap`: the wording exceeds the confirmed facts;
- `selection gap`: the entry does not help this application;
- `placement gap`: useful evidence appears in the wrong section or order.

### 6. Check credibility and consistency

Cross-check dates, institution names, degree titles, role titles, publication status, citation format, tense, location, capitalization, and claimed outputs. Compare with the transcript, PS, research proposal, or supporting documents when provided.

Treat placeholders, unexplained or impossible date gaps, overlapping full-time roles, future-dated achievements, inconsistent titles, ambiguous publication status, unclear authorship, and claims that exceed the stated individual role as verification risks. Ask a question instead of repairing the fact by assumption.

Do not treat the absence of uploaded certificates, transcripts, acceptance letters, or other proof as evidence that an otherwise plausible CV claim is untrustworthy. Distinguish:

- `verification question`: useful detail or supporting material has not been supplied;
- `credibility gap`: the wording is internally inconsistent, implausible, contradicted by supplied material, or attributes a team result to the applicant without support.

An unnamed conference, incomplete award description, expected-graduation label, or third-party Word metadata is normally a local completeness issue unless it creates a material identity, status, privacy, or authorship conflict.

### 7. Check programme alignment

Build an internal evidence map:

> programme demand -> applicant evidence -> missing preparation or unexplained gap

Judge alignment through field-relevant preparation, methods, outputs, and progression. Do not reward keyword repetition, generic course lists, or superficial mirroring of the programme webpage.

### 8. Form the three core judgements only after diagnosing

Classify each of the three core dimensions with one of:

- `convincing`
- `convincing with local gaps`
- `developing`
- `structural risk`
- `not assessable from supplied context`

Use the labels consistently:

- `convincing`: the dimension's main function is achieved without a material limitation;
- `convincing with local gaps`: the main function is achieved, with a small number of bounded and fixable issues;
- `developing`: recurring limitations materially weaken the dimension across multiple important entries;
- `structural risk`: the problem is pervasive, misleading, contradictory, or submission-breaking;
- `not assessable`: the necessary context is missing and no responsible inference is available.

If the user requests a score, provide the evidence-based classification first and explain that a weighted total cannot substitute for programme-specific judgement.

For each judgement, state:

- the evidence that already establishes the dimension;
- the limiting evidence and whether it is local, recurring, or structural;
- the calibrated judgement in plain language;
- why it matters to the application reader;
- the limitation, missing context, or fact that could change the judgement.

Do not disguise a recommendation as a judgement. For example, first judge that the research identity is split across competing themes; only after calibration recommend a new order or deletion.

### 9. Calibrate before prioritizing revision

In Stage 1, stop after the user calibration prompt. Do not append a revision route, bullet rewrites, or a long self-check list.

In Stage 2, update any judgement affected by the user's response, then order recommendations by dependency:

1. Structural: positioning, selection, section order, or missing evidence.
2. Major: reconstruct an entry or bullet evidence chain.
3. Local: compress, clarify, standardize, or proofread.

Do not spend most of the response correcting punctuation when the CV's evidence architecture is weak.

## Produce the diagnosis

Read `references/output-schema.md` and follow it. Match the user's language and preserve quoted CV text in its original language.

In Stage 1, end with the calibration prompt. In Stage 2 or Full Audit, end with only the evidence questions needed for the proposed changes. Do not append a fully rewritten CV.


# The Chair｜CV 申请竞争力诊断

一套面向留学申请 CV 的定性诊断 Skill。它不把 CV 简化成分数，也不直接替申请者重写整份简历，而是先判断一份 CV 已经证明了什么、真正受限于什么，再与使用者确认判断，最后提出修改建议。

## 核心理念

CV 不是经历仓库，而是申请证据地图。它需要让招生者快速看见：

- 申请者准备学习什么；
- 哪些经历能够证明这种准备；
- 申请者本人做了什么、如何做、形成了什么产出；
- 信息是否清楚、可信并适合当前申请。

Skill 会检查五类常见材料：

1. Education
2. Publications and Conferences
3. Research Experience
4. Internships and Professional Experience
5. Scholarships, Honors, and Awards

但默认不会逐栏打分，而是将证据整合为三个核心判断：

1. **定位与取舍**
2. **证据与贡献**
3. **可信度与完成度**

## 1.2 的判断校准

- 按申请者当前阶段判断，不用成熟研究者的标准压低本科申请者；
- 先说明已经成立的证据，再指出限制；
- 本科阶段经历多样不自动等于定位混乱；
- 缺少目标项目只意味着项目契合暂不可判断；
- 未上传证书或录用函不自动构成可信度问题；
- 区分局部缺口、反复出现的维度问题和真正的结构性风险。

定性标签包括：

- `convincing`
- `convincing with local gaps`
- `developing`
- `structural risk`
- `not assessable`

## 两阶段使用方式

### 第一阶段：先判断

Skill 先输出三个核心判断，并分别说明：

- 已成立的证据；
- 限制点及其严重程度；
- 综合判断；
- 对招生者阅读的影响；
- 什么信息可能改变判断。

随后暂停，让使用者确认、反驳或补充。

### 第二阶段：再建议

确认诊断后，Skill 最多给出三个修改优先级，并可标注最多五条高价值 bullet。未经确认，不虚构方法、数字、成果、角色或影响。

## 建议输入

```text
【申请类别】授课型硕士 / 研究型硕士 / PhD / 奖学金 / 其他
【学校与项目】
【项目官网或项目介绍】
【目标入学年份】
【CV 文件】DOCX / PDF / 粘贴全文
【页数或格式要求】
【申请方向或希望突出的人设】
【同时使用的材料】PS / Research Proposal / Transcript / 其他（可选）
【已知担忧】结构 / 内容选择 / research / internship / 英文 / 排版 / 事实一致性 / 其他
```

只有 CV 时也可以进行文档内部诊断，但项目契合、最终取舍和排序会被标为暂定或 `not assessable`。

## 调用示例

```text
使用 $the-chair-cv-review 平衡诊断这份留学申请 CV。第一轮先说明已经成立的证据，再区分局部缺口、维度问题和无法判断的项目契合；等我确认后再提出修改建议。
```

## 安装

将仓库中的 `skill/the-chair-cv-review` 文件夹完整复制到：

```text
~/.codex/skills/the-chair-cv-review
```

也可以把本仓库链接交给 Codex，要求安装其中的 `skill/the-chair-cv-review`。

## 仓库结构

```text
The-Chair-CV-Review/
├── README.md
└── skill/
    └── the-chair-cv-review/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        │   ├── chair-principles.md
        │   ├── intake-template.md
        │   ├── output-schema.md
        │   └── section-guides.md
        └── scripts/
            └── extract_cv_docx.py
```

仓库不包含任何申请者的真实 CV、联系方式或未脱敏案例。



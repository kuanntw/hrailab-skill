---
name: hrxai-research-handoff
description: Use this skill when HRxAI lab members need to generate, validate, or repair standardized research handoff documentation after completing a study or project. It creates AI-readable project overview, protocol, data inventory, RAW data guide, variable dictionary, measurement toolkit, technical resources, reports index, privacy/access notes, next-user guide, and completeness checks so future members can quickly locate, understand, and safely use research materials through AI.
---

# HRxAI Research Handoff

## Purpose

Use this skill to help HRxAI lab members turn completed research folders into standardized, AI-readable handoff packages. A complete handoff package lets future members use AI to quickly find past reports, RAW data, questionnaires, AI feature outputs, expert ratings, system resources, and administrative records without misusing sensitive data.

## Non-negotiable rules

- Never overwrite, rename, move, delete, or transform RAW data unless the user explicitly asks and a derived copy is created.
- Treat participant rosters, consent files, questionnaire responses, video data, expert ratings, incentive/gift-card records, administrative signatures, credentials, active invite codes, API keys, and backend access notes as sensitive or restricted.
- Do not reproduce direct identifiers, live credentials, active invitation codes, passwords, or API keys in generated handoff documents.
- Mark uncertain information as `TODO` or `Needs verification`; do not infer final status, variable roles, consent scope, or RAW data lineage from filenames alone.
- Every substantive summary must preserve source traceability with file/folder paths.
- Reports, slides, theses, and oral-defense files are secondary sources; verify empirical claims against data files when possible.

## Modes

### Generate mode

Use when a lab member needs new handoff documentation from a project folder.

1. Confirm project name, root folder, owner, time range, and intended audience if missing.
2. Inspect or ask for the folder structure.
3. Classify materials as protocol, consent/IRB, raw data, cleaned data, derived data, AI output, expert rating, questionnaire, report/output, technical resource, administrative record, or unknown.
4. Generate the standard 00-09 handoff documents using the templates in `assets/templates/`.
5. Use `TODO` for missing paths, dates, owners, versions, and uncertain interpretations.
6. Recommend running Validate mode before declaring the package ready.

### Validate mode

Use when a handoff package already exists and the user asks whether it is complete.

1. Read `references/completeness-checklist.md`.
2. Check that required documents exist and required fields are filled.
3. Check traceability among reports, RAW data, cleaned data, analysis files, variables, questionnaires, expert ratings, and technical systems.
4. Check privacy, access, and credential risks.
5. Check AI search readiness: can a future AI answer the core lookup questions?
6. Generate or update `10_HANDOFF_COMPLETENESS_CHECK.md`.
7. Assign one overall status: `Not ready for handoff`, `Ready with warnings`, or `Ready for handoff`.

### Repair mode

Use when validation finds gaps and the user wants help fixing them.

1. Start from `10_HANDOFF_COMPLETENESS_CHECK.md` if available.
2. Fix safe documentation gaps directly when the evidence is available.
3. For unknown items, insert focused `TODO` placeholders with owner/action guidance.
4. Never invent missing paths, versions, final-report status, consent scope, variable roles, or reliability statistics.
5. Re-run Validate mode after repairs.

## Standard handoff package

Create or validate these documents for each project:

```text
ProjectName_Handoff/
├── 00_README_PROJECT_OVERVIEW.md
├── 01_RESEARCH_PROTOCOL.md
├── 02_DATA_INVENTORY.md
├── 03_RAW_DATA_GUIDE.md
├── 04_VARIABLE_DICTIONARY.md
├── 05_MEASUREMENT_TOOLKIT.md
├── 06_TECHNICAL_RESOURCES.md
├── 07_REPORTS_AND_OUTPUTS_INDEX.md
├── 08_PRIVACY_AND_ACCESS_NOTES.md
├── 09_NEXT_USER_GUIDE.md
└── 10_HANDOFF_COMPLETENESS_CHECK.md
```

Use `10_HANDOFF_COMPLETENESS_CHECK.md` for validation results; it is not required before the first Generate-mode draft.

## HRxAI source folder map

Use this map as the initial search guide; update project-specific paths in each handoff package.

- `00 與HRDA共用`: shared HRDA materials.
- `01 職能`: competency models and related materials.
- `02 會議記錄`: meeting records and decisions.
- `03 Kairos AI 介紹影片`: Kairos AI introduction videos.
- `04 同意文件`: consent and ethics/IRB-related files.
- `05 資料蒐集`: data collection plans, forms, and procedures.
- `06 實驗名單`: experiment rosters and participant lists.
- `07 日間碩評分享區`: day-program graduate evaluation/share materials.
- `08 在職碩評分享區`: in-service graduate evaluation/share materials.
- `09 系統操作影片`: system operation tutorials.
- `10 產品Demo影片`: product demo videos.
- `11 實驗數據`: experiment data, RAW data, cleaned data, and derived datasets.
- `0. 畢業學長姐資料`: prior graduates' materials.
- `1. 表達技巧影片`: communication/presentation training videos.
- `2. 小組論文共享資料`: group thesis/reference sharing materials.
- `3. 口試資料`: oral defense materials.
- `4. 實驗問卷`: experiment questionnaires and versions.
- `5. Echo系統`: Echo system resources.
- `6. 實驗禮券發放明細`: incentive/gift-card administrative records.
- `7. 小論繳交`: short paper submissions.
- `師大AI實驗室_2025畢業小組進度.xlsx`: graduation group progress tracker.

## Search order by task

- Research design/protocol: `05 資料蒐集` → `04 同意文件` → `02 會議記錄` → `4. 實驗問卷` → related reports/theses.
- RAW data: `11 實驗數據` → `5. Echo系統` → `06 實驗名單` → `05 資料蒐集` → `4. 實驗問卷` → related reports/theses.
- Measurement tools: `4. 實驗問卷` → `05 資料蒐集` → `2. 小組論文共享資料` → related theses/reports.
- Technical resources: `09 系統操作影片` → `10 產品Demo影片` → `03 Kairos AI 介紹影片` → `5. Echo系統` → Git/model repository references if available.
- Knowledge/admin archive: `0. 畢業學長姐資料` → `2. 小組論文共享資料` → `3. 口試資料` → `7. 小論繳交` → `6. 實驗禮券發放明細` → `02 會議記錄`.

## Reference files

- Read `references/handoff-document-spec.md` when generating or repairing standard documents.
- Read `references/completeness-checklist.md` when validating completeness or producing fix lists.
- Prefer running `scripts/validate_handoff.py <ProjectName_Handoff>` for deterministic first-pass validation, then review its output against the full checklist.
- Read `references/data-classification.md` when classifying files as raw, cleaned, derived, report, internal, sensitive, or restricted.
- Read `references/privacy-and-ethics.md` before summarizing or exposing sensitive research/administrative data.
- Read `references/ai-query-patterns.md` when writing `09_NEXT_USER_GUIDE.md` or evaluating AI search readiness.

## Output requirements

When producing handoff documents:

- Prefer Markdown tables for inventories, variable dictionaries, resources, reports, and issue lists.
- Use `Not applicable` only with a short reason.
- Use `TODO: ...` for missing information that must be supplied by a human.
- Include `Sources consulted` sections whenever evidence was reviewed.
- End validation with prioritized fixes grouped by `Critical`, `High`, `Medium`, and `Low`.

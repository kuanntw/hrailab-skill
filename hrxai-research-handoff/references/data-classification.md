# Data Classification

Use this reference to classify HRxAI research materials consistently.

## Data lifecycle classes

| Class | Definition | Examples | Handling |
|---|---|---|---|
| RAW | Original exported, recorded, uploaded, or collected data before cleaning or transformation | participant videos, raw questionnaire exports, original Echo outputs, original expert rating sheets | Never overwrite; analyze a copied/derived file |
| Cleaned | Data after cleaning, de-identification, filtering, recoding, or formatting | cleaned CSV/XLSX, coded survey data | Document source raw files and transformation steps |
| Derived | Data generated from raw/cleaned sources by computation or aggregation | AI features, scale scores, summary statistics, inter-rater reliability outputs | Document inputs, model/script/version, and calculation |
| Report | Human interpretation or presentation of findings | thesis, oral defense slides, conference paper, technical report | Use for context; verify against data when possible |
| Administrative | Operational or compliance files | roster, consent tracker, gift-card records, signatures, committee list | Treat as sensitive or highly sensitive |
| Technical | System or tooling resources | operation videos, backend export instructions, Git repos, model docs | Separate public instructions from restricted access details |
| Unknown | Files whose role is unclear | ambiguous filenames or unlabeled folders | Mark `Needs verification` and request owner clarification |

## Sensitivity classes

| Level | Data type | Examples | Default output rule |
|---|---|---|---|
| Low | Public/demo material | product demo videos, public slides | Can summarize with source path |
| Internal | Lab work material | meeting notes, progress trackers, draft reports | Summarize with source path; avoid unnecessary personal details |
| Sensitive | Research data | questionnaire responses, videos, AI features, expert ratings | De-identify; aggregate where possible |
| Highly sensitive | Direct identifiers or administrative proof | participant names, email, phone, student ID, consent forms, gift-card records, signatures | Do not expose identifiers in normal outputs |
| Restricted | Credentials or live access controls | passwords, API keys, backend credentials, active invite codes | Do not store in Skill or handoff docs; point to approved secure location |

## Classification rules

- If a file contains both research data and identifiers, classify by the highest sensitivity.
- If a folder contains mixed files, mark the folder sensitivity as the highest known child sensitivity and explain mixed contents.
- If the same dataset exists in multiple versions, classify each version separately and document lineage.
- If a file's role is unclear, do not choose `RAW` or `final`; mark it `Unknown - needs verification`.

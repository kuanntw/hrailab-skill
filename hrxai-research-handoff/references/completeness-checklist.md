# Handoff Completeness Checklist

Use this checklist in Validate mode and Repair mode.

## Overall status rules

### Not ready for handoff

Assign this status if any condition is true:

- Any unresolved `Critical` issue exists.
- Required documents `00`, `02`, `03`, `08`, or `09` are missing without a justified `Not applicable` explanation.
- RAW data paths are missing and the project uses empirical data.
- Sensitive/restricted files are unmarked.
- Direct identifiers, live credentials, active invite codes, passwords, or API keys appear in handoff documents.
- Future AI cannot answer where the data are or which files are sensitive.

### Ready with warnings

Assign this status if:

- No `Critical` issues remain.
- Some `High` or `Medium` issues remain.
- Future AI can answer core lookup questions, but some details require owner verification.

### Ready for handoff

Assign this status if:

- No unresolved `Critical` or `High` issues remain.
- All required documents exist or are explicitly `Not applicable` with reasons.
- Data files have paths, lifecycle classes, sensitivity classes, and notes.
- Future AI can answer the AI search readiness questions without guessing.

## Severity levels

| Severity | Meaning | Examples |
|---|---|---|
| Critical | Blocks safe or useful handoff | missing data inventory, missing privacy notes, RAW data location missing, credentials exposed, variables undefined for main dataset |
| High | Seriously impairs reuse or interpretation | missing experimental conditions, missing raw-cleaned lineage, missing final-report status, missing questionnaire version |
| Medium | Reduces clarity or traceability | missing keywords, known issues, recommended reading order, model version, operation video index |
| Low | Formatting or optional detail | inconsistent headings, optional citation gaps, historical changelog missing |

## Required documents check

| Document | Required | Critical if missing | Purpose |
|---|---:|---:|---|
| `00_README_PROJECT_OVERVIEW.md` | Yes | Yes | Entry point for project meaning and paths |
| `01_RESEARCH_PROTOCOL.md` | Yes | High/Critical | Study design and procedure |
| `02_DATA_INVENTORY.md` | Yes | Yes | Master file/folder inventory |
| `03_RAW_DATA_GUIDE.md` | Yes if empirical data exists | Yes | RAW data location and handling |
| `04_VARIABLE_DICTIONARY.md` | Yes if variables/datasets exist | High/Critical | Variable meaning and roles |
| `05_MEASUREMENT_TOOLKIT.md` | Yes if questionnaires/scales exist | High | Instruments and scoring |
| `06_TECHNICAL_RESOURCES.md` | Yes if systems/models/tools exist | Medium/High | Systems and tooling context |
| `07_REPORTS_AND_OUTPUTS_INDEX.md` | Yes | High | Final/non-final outputs |
| `08_PRIVACY_AND_ACCESS_NOTES.md` | Yes | Yes | Sensitive data and access rules |
| `09_NEXT_USER_GUIDE.md` | Yes | High | Future user navigation |
| `10_HANDOFF_COMPLETENESS_CHECK.md` | Validation output | No | Readiness result and fix list |

## Required fields by document

### 00_README_PROJECT_OVERVIEW.md

Required:

- Project / Study Name
- Owner / Lab Member
- Advisor / PI or `Not applicable`
- Time Range
- Research Topic
- Short Abstract
- Related Folders
- Recommended Reading Order
- Handoff Package Last Updated

### 01_RESEARCH_PROTOCOL.md

Required:

- Study Purpose
- Participants or population description
- Recruitment Channels or `Not applicable`
- Experimental Design
- Conditions / Groups
- Procedure Timeline
- Consent and Ethics
- Protocol Version History

Critical/High checks:

- If GUI/CUI, AI roles, or manipulation conditions appear in the project, they must be defined.
- If N/N+7, pretest/posttest, or delayed testing is used, the timeline must identify participant and system actions.

### 02_DATA_INVENTORY.md

Required:

- Path for every listed file/folder
- Format
- Lifecycle class: Raw, Cleaned, Derived, Report, Administrative, Technical, or Unknown
- Contains PII
- Sensitivity
- Notes or `Needs verification`

Critical checks:

- RAW data exists but is not listed.
- Sensitive files are listed without sensitivity/access notes.
- Data category is `Unknown` for core analysis files and no owner/action is identified.

### 03_RAW_DATA_GUIDE.md

Required if empirical data exists:

- RAW data definition
- RAW data locations
- Do-not-modify rule
- Known missing data or `None known`
- Relationship between raw, cleaned, analysis, and report files

### 04_VARIABLE_DICTIONARY.md

Required if datasets contain variables:

- Variable name
- Role or `Unknown - needs verification`
- Construct
- Source
- Data type
- Scale/unit
- Calculation
- Missing rule

Critical/High checks:

- Main outcome variables missing.
- AI feature variables lack source/system explanation.
- Expert-rating variables lack rubric or scoring context.

### 05_MEASUREMENT_TOOLKIT.md

Required if questionnaires/scales exist:

- Instrument name
- Construct
- Item count or item list location
- Scale
- Version/file location
- Scoring rules
- Reliability/validity evidence or `TODO: verify`

### 06_TECHNICAL_RESOURCES.md

Required if systems/models/tools exist:

- System purpose and location
- Access requirement
- Data export procedure or location of instructions
- Model/module version if AI outputs are used
- Credential policy statement

Critical check: live credentials, API keys, passwords, or active invite codes are included.

### 07_REPORTS_AND_OUTPUTS_INDEX.md

Required:

- Output type
- Title
- Author/group or `Unknown`
- Date or `Unknown`
- Status
- Location
- Related data if known

High check: no final or best-current report is identified and no `Needs verification` owner/action is provided.

### 08_PRIVACY_AND_ACCESS_NOTES.md

Required:

- Data sensitivity summary
- PII statement
- Consent scope or `TODO: verify with PI/IRB owner`
- Restricted files
- De-identification rules
- External tool restrictions
- Contact for access

Critical check: sensitive data exists but privacy/access notes are missing.

### 09_NEXT_USER_GUIDE.md

Required:

- Reading path for understanding the study
- Reading path for reanalyzing data
- Reading path for questionnaire reuse if applicable
- Reading path for system use if applicable
- Known issues
- Recommended next steps
- Common AI queries

## Data traceability checks

Create issues if any are missing:

- Final reports point to related data files or state `Unknown - needs verification`.
- RAW files point to cleaned/derived/analysis files when those exist.
- Cleaned files identify raw source and transformation notes.
- AI feature outputs identify source system/model/version if known.
- Variable dictionary covers columns in main datasets.
- Questionnaire files identify versions, scales, and scoring rules.
- Expert ratings identify rubric, rater count, and reliability report if known.

## Privacy and access risk checks

Create `Critical` issues for:

- Direct identifiers copied into ordinary handoff documents.
- Live credentials, API keys, passwords, backend access tokens, or active invite codes.
- Consent or incentive records without restricted handling notes.
- Recommendation to upload identifiable/sensitive raw data to external tools without explicit authorization.

## Repair output format

Each issue should use this structure:

```markdown
## Issue NNN

- Severity:
- Location:
- Missing item / Risk:
- Why it matters:
- Evidence:
- Recommended action:
- Suggested text / template:
- Owner:
- Due date:
```

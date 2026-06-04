# Handoff Document Specification

Use this reference to generate or repair the standard HRxAI project handoff package. Each document should be concise, source-traceable, and safe for future AI-assisted search.

## 00_README_PROJECT_OVERVIEW.md

Purpose: the entry point for humans and AI.

Required sections:

- Project / Study Name
- Owner / Lab Member
- Advisor / PI
- Time Range
- Research Topic
- Short Abstract
- Related Folders
- Recommended Reading Order
- Handoff Package Last Updated
- Sources Consulted

Recommended sections:

- Research Questions
- Keywords
- Contact / Maintainer
- Known Gaps

## 01_RESEARCH_PROTOCOL.md

Purpose: document how the study was designed and executed.

Required sections:

- Study Purpose
- Participants
- Recruitment Channels
- Experimental Design
- Conditions / Groups
- Procedure Timeline
- Consent and Ethics
- Protocol Version History

Recommended sections:

- GUI / CUI Definition
- AI Role Definitions: Coach, Partner, Assistant Coach, or project-specific roles
- Manipulation SOP and related prompts/dialogue style notes
- Inclusion / Exclusion Criteria
- N, N+7, pretest, posttest, delayed-test timing
- IRB / Consent File Locations

## 02_DATA_INVENTORY.md

Purpose: the master list of available project data and outputs.

Required columns:

| Data Category | File / Folder | Path | Format | Raw / Cleaned / Derived / Report | Contains PII | Sensitivity | Notes |
|---|---|---|---|---|---|---|---|

Required categories to check:

- Consent / IRB files
- Participant rosters
- Recruitment records
- Video raw files
- Questionnaire raw exports
- AI feature outputs
- Expert ratings
- Cleaned datasets
- Analysis scripts
- Reports / slides / theses
- Administrative records

Use `Not applicable` with a reason if a category does not exist.

## 03_RAW_DATA_GUIDE.md

Purpose: explain what counts as RAW data and how to avoid corrupting it.

Required sections:

- Definition of RAW Data in This Project
- RAW Data Locations
- Video Raw Data
- Questionnaire Raw Data
- System Log / AI Output Raw Data
- Expert Rating Raw Data
- Relationship Between Raw, Cleaned, and Analysis Files
- Do Not Modify Rules
- Known Data Issues
- Missing Data Notes
- Recommended First Files to Inspect

Required relationship table:

| Raw File | Cleaned File | Analysis File | Report Output | Notes |
|---|---|---|---|---|

## 04_VARIABLE_DICTIONARY.md

Purpose: prevent future users and AI from guessing variable meaning or role.

Required columns:

| Variable Name | Role | Construct | Source | Data Type | Scale / Unit | Calculation | Missing Rule | Notes |
|---|---|---|---|---|---|---|---|---|

Allowed role values:

- `X`
- `M`
- `Y`
- `Moderator`
- `Control`
- `Covariate`
- `Metadata`
- `Administrative`
- `Unknown - needs verification`

Do not infer role from filename alone. Confirm with protocol, analysis plan, thesis, report, or project owner.

## 05_MEASUREMENT_TOOLKIT.md

Purpose: preserve questionnaires, scales, scoring, and psychometric evidence.

Required sections:

- Instruments Used
- Questionnaire Versions
- Scoring Rules
- Reliability / Validity Evidence
- References / Citations
- Related Files

Required tables:

| Instrument | Construct | Items | Scale | Source / Citation | Used For | File Location |
|---|---|---:|---|---|---|---|

| Instrument | Subscale | Item Numbers | Reverse-coded Items | Score Calculation | Notes |
|---|---|---|---|---|---|

| Instrument | Sample / Study | Cronbach's Alpha | CFA / EFA Result | Report Location | Notes |
|---|---|---:|---|---|---|

Use `TODO: verify` for missing reliability or validity values; do not fabricate statistics.

## 06_TECHNICAL_RESOURCES.md

Purpose: preserve system, model, data export, and tool usage context.

Required sections:

- Systems Used
- System Operation Materials
- Admin Backend
- Invitation Code Management
- Data Export Procedure
- Git Repositories
- Models / Analysis Modules
- Recommended Research Tools
- Access and Credential Policy

Do not include live passwords, API keys, active invitation codes, or backend credentials. Point to the approved internal credential manager or protected access sheet instead.

## 07_REPORTS_AND_OUTPUTS_INDEX.md

Purpose: identify final and non-final knowledge outputs.

Required columns:

| Output Type | Title | Author / Group | Date | Status | Location | Related Data | Notes |
|---|---|---|---|---|---|---|---|

Recommended status values:

- `proposal`
- `midterm`
- `draft`
- `conference`
- `oral-defense`
- `post-defense-final`
- `submitted`
- `published`
- `archived`
- `unknown - needs verification`

## 08_PRIVACY_AND_ACCESS_NOTES.md

Purpose: make sensitive data and access limits explicit.

Required sections:

- Data Sensitivity Summary
- Personally Identifiable Information
- Consent Scope
- IRB Notes
- Restricted Files
- De-identification Rules
- External Tool Restrictions
- Do Not Use / Do Not Share List
- Contact for Access

Required table:

| Data Type | Sensitivity | Access Requirement | Output Rule | Notes |
|---|---|---|---|---|

## 09_NEXT_USER_GUIDE.md

Purpose: tell future users and AI where to start.

Required sections:

- If You Want To Understand the Study
- If You Want To Reanalyze the Data
- If You Want To Reuse the Questionnaire
- If You Want To Use the System
- If You Need Administrative or Access Information
- Known Issues
- Recommended Next Steps
- Common AI Queries

## 10_HANDOFF_COMPLETENESS_CHECK.md

Purpose: validation output, not source documentation.

Required sections:

- Overall Status
- Summary by Severity
- Required Documents Check
- Required Fields Check
- Data Traceability Check
- Privacy and Access Risk Check
- AI Search Readiness
- Prioritized Fix List
- Final Recommendation

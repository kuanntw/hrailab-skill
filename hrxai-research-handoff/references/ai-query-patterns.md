# AI Query Patterns

Use these prompts in `09_NEXT_USER_GUIDE.md` and validation. The goal is to make future AI-assisted search reliable and safe.

## Common future-user prompts

- Summarize this project and list the files I should read first.
- Find the RAW data and explain which files should not be modified.
- Build a data inventory from the handoff documents.
- Explain the experimental conditions and variables.
- List all questionnaires used in this study and their scoring rules.
- Identify which files contain sensitive information.
- Find the final thesis/report and related data files.
- Explain how raw, cleaned, derived, and report files relate to each other.
- Find Echo/system AI feature outputs and explain the variable dictionary.
- Tell me what is missing before I reuse this dataset.

## AI search readiness questions

A valid handoff package should let a future AI answer these without guessing:

1. What is this project about?
2. Who maintained it and what period does it cover?
3. Where are the RAW data?
4. Which files are raw, cleaned, derived, report, administrative, or technical?
5. Which files are sensitive or restricted?
6. What was the experimental design?
7. What are the conditions/groups and manipulations?
8. What variables exist and what are their roles?
9. What questionnaires or scales were used?
10. Where are expert ratings and reliability reports?
11. Which report/thesis/output is final?
12. What should a future user read first?
13. What requires PI, IRB, or access-owner confirmation?

## Validation rule

If a readiness question is `No` or `Partial`, create a completeness issue with severity, evidence, missing pieces, and a suggested repair template.

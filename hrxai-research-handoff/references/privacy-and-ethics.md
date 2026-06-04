# Privacy and Ethics Rules

Use these rules before generating, validating, or repairing handoff documents that mention participants, students, administrators, experts, or system access.

## Default stance

Assume HRxAI research folders may contain personal data, student data, research-subject data, consent records, compensation records, and system access information. Prefer de-identified summaries and source-path references over copying sensitive content.

## Do not include in handoff documents

- Participant names, phone numbers, emails, student IDs, national IDs, addresses, signatures, or raw contact lists.
- Live passwords, API keys, backend credentials, active invitation codes, or private tokens.
- Full consent forms with identifiable participant entries.
- Gift-card or incentive details tied to named individuals.
- Raw questionnaire rows or video-level details that identify individuals, unless explicitly authorized and necessary.

## Safe documentation patterns

Use this pattern for restricted access:

```markdown
Access details are stored in the approved internal credential/access-control location. Contact: TODO: owner/role. Do not duplicate live credentials or active invitation codes in this handoff package.
```

Use this pattern for sensitive research data:

```markdown
This folder contains sensitive research data. Future outputs should use de-identified participant IDs and aggregate summaries unless direct identifiers are explicitly required and authorized.
```

Use this pattern for uncertain consent scope:

```markdown
TODO: verify consent scope with PI/IRB owner before reusing, sharing, or uploading these data to external tools.
```

## External AI/tool restrictions

Before recommending external tools, check whether the material contains sensitive or highly sensitive data. Do not recommend uploading identifiable or raw sensitive data to external systems unless the lab has explicit approval and the user confirms authorization.

## Consent and IRB versioning

Do not call any consent document "latest" unless the document has a verification date and owner. Prefer:

```markdown
Current known consent template: TODO: version/path. Verified on: TODO: date. Before reuse, confirm with PI/IRB owner.
```

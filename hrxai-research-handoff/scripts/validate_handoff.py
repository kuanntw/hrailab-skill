#!/usr/bin/env python3
"""Validate an HRxAI research handoff package and write a Markdown completeness check."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

DOCS = {
    "00_README_PROJECT_OVERVIEW.md": [
        "Project / Study Name", "Owner / Lab Member", "Advisor / PI", "Time Range",
        "Research Topic", "Short Abstract", "Related Folders", "Recommended Reading Order",
        "Handoff Package Last Updated",
    ],
    "01_RESEARCH_PROTOCOL.md": [
        "Study Purpose", "Participants", "Recruitment Channels", "Experimental Design",
        "Conditions / Groups", "Procedure Timeline", "Consent and Ethics", "Protocol Version History",
    ],
    "02_DATA_INVENTORY.md": ["Inventory Table", "Categories Checked"],
    "03_RAW_DATA_GUIDE.md": [
        "Definition of RAW Data in This Project", "RAW Data Locations", "Do Not Modify Rules",
        "Known Data Issues", "Missing Data Notes",
    ],
    "04_VARIABLE_DICTIONARY.md": ["Variables", "Role Definitions"],
    "05_MEASUREMENT_TOOLKIT.md": [
        "Instruments Used", "Questionnaire Versions", "Scoring Rules", "Reliability / Validity Evidence",
    ],
    "06_TECHNICAL_RESOURCES.md": [
        "Systems Used", "System Operation Materials", "Data Export Procedure", "Access and Credential Policy",
    ],
    "07_REPORTS_AND_OUTPUTS_INDEX.md": ["Outputs", "Best Current / Final Output"],
    "08_PRIVACY_AND_ACCESS_NOTES.md": [
        "Data Sensitivity Summary", "Personally Identifiable Information", "Consent Scope",
        "Restricted Files", "De-identification Rules", "External Tool Restrictions", "Contact for Access",
    ],
    "09_NEXT_USER_GUIDE.md": [
        "If You Want To Understand the Study", "If You Want To Reanalyze the Data",
        "Known Issues", "Recommended Next Steps", "Common AI Queries",
    ],
}

CRITICAL_DOCS = {
    "00_README_PROJECT_OVERVIEW.md",
    "02_DATA_INVENTORY.md",
    "03_RAW_DATA_GUIDE.md",
    "08_PRIVACY_AND_ACCESS_NOTES.md",
}

CREDENTIAL_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|password|passwd|token)\s*[:=]\s*[^\s`]+"),
    re.compile(r"(?i)(bearer\s+[a-z0-9._\-]{20,})"),
]


def has_heading(text: str, heading: str) -> bool:
    pattern = re.compile(rf"^#+\s+{re.escape(heading)}\s*$", re.MULTILINE)
    return bool(pattern.search(text))


def has_unresolved_placeholder(text: str) -> bool:
    return "TODO" in text or "needs verification" in text.lower() or "unknown - needs verification" in text.lower()


def validate(root: Path) -> tuple[list[dict[str, str]], dict[str, int]]:
    issues: list[dict[str, str]] = []
    for doc, headings in DOCS.items():
        path = root / doc
        if not path.exists():
            severity = "Critical" if doc in CRITICAL_DOCS else "High"
            issues.append({
                "severity": severity,
                "location": doc,
                "issue": "Required handoff document is missing.",
                "action": f"Create `{doc}` from the HRxAI handoff template.",
            })
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for heading in headings:
            if not has_heading(text, heading):
                issues.append({
                    "severity": "High" if doc in CRITICAL_DOCS else "Medium",
                    "location": doc,
                    "issue": f"Missing required heading: {heading}.",
                    "action": f"Add a `{heading}` section and fill it or mark `Not applicable` with a reason.",
                })
        if has_unresolved_placeholder(text):
            issues.append({
                "severity": "Medium",
                "location": doc,
                "issue": "Contains unresolved TODO / needs-verification placeholders.",
                "action": "Resolve the placeholders or assign owner/date for follow-up.",
            })
        for pattern in CREDENTIAL_PATTERNS:
            if pattern.search(text):
                issues.append({
                    "severity": "Critical",
                    "location": doc,
                    "issue": "Possible credential, token, API key, or password found.",
                    "action": "Remove the secret and point to the approved protected credential/access-control location.",
                })
    counts = {level: 0 for level in ["Critical", "High", "Medium", "Low"]}
    for issue in issues:
        counts[issue["severity"]] += 1
    return issues, counts


def status_from_counts(counts: dict[str, int]) -> str:
    if counts["Critical"]:
        return "Not ready for handoff"
    if counts["High"] or counts["Medium"]:
        return "Ready with warnings"
    return "Ready for handoff"


def render(root: Path, issues: list[dict[str, str]], counts: dict[str, int]) -> str:
    status = status_from_counts(counts)
    lines = [
        "# Handoff Completeness Check",
        "",
        "## Overall Status",
        "",
        f"Status: {status}",
        "",
        "## Summary by Severity",
        "",
        "| Severity | Count |",
        "|---|---:|",
    ]
    for level in ["Critical", "High", "Medium", "Low"]:
        lines.append(f"| {level} | {counts[level]} |")
    lines += ["", "## Prioritized Fix List", ""]
    for level in ["Critical", "High", "Medium", "Low"]:
        lines += [f"### {level}", ""]
        selected = [i for i in issues if i["severity"] == level]
        if not selected:
            lines.append("- None")
        else:
            for issue in selected:
                lines.append(f"- `{issue['location']}`: {issue['issue']} Recommended action: {issue['action']}")
        lines.append("")
    lines += [
        "## Required Documents Check",
        "",
        "| Document | Status |",
        "|---|---|",
    ]
    for doc in DOCS:
        lines.append(f"| `{doc}` | {'Present' if (root / doc).exists() else 'Missing'} |")
    lines += [
        "",
        "## Final Recommendation",
        "",
        "Resolve all Critical issues before handoff. Resolve or explicitly assign all High/Medium issues before declaring the package final.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Path to a ProjectName_Handoff folder")
    parser.add_argument("--output", type=Path, help="Output Markdown path; defaults to ROOT/10_HANDOFF_COMPLETENESS_CHECK.md")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Handoff root does not exist or is not a directory: {root}")
    issues, counts = validate(root)
    output = args.output or root / "10_HANDOFF_COMPLETENESS_CHECK.md"
    output.write_text(render(root, issues, counts), encoding="utf-8")
    print(f"Wrote {output}")
    print(f"Status: {status_from_counts(counts)}")
    return 0 if not counts["Critical"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

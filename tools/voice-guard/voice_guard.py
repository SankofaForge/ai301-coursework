#!/usr/bin/env python3
"""voice_guard.py: Gating outgoing open-source comments against contributor voice standards.

Validates candidate issue comments, claims, reproduction reports, and PR descriptions
against the rules defined in voice-guide.md. Appends all check results to voice-guard.log.
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

# Banned patterns that indicate ownership demands, speculative timelines, or empty fluff
RULES = [
    {
        "id": "NO_ASSIGNMENT_DEMAND",
        "description": "Never demand assignment or ticket reservation ('assign this to me', 'please assign me')",
        "pattern": re.compile(r"\b(please\s+assign(\s+this)?(\s+to)?\s+me|assign\s+me|reserve\s+this\s+issue|assign\s+to\s+me)\b", re.IGNORECASE),
        "guidance": "State your intention to investigate and share local reproduction findings instead of requesting formal assignment.",
    },
    {
        "id": "NO_SPECULATIVE_TIMELINES",
        "description": "Never promise fixed delivery dates or speculative timelines ('by tomorrow', 'in 48 hours', 'ETA')",
        "pattern": re.compile(r"\b(by\s+tomorrow|in\s+\d+\s+(days?|hours?)|eta\b|guarantee|promise\s+to\s+deliver)\b", re.IGNORECASE),
        "guidance": "Commit only to the immediate next technical step without promising unverified completion dates.",
    },
    {
        "id": "NO_OVERCONFIDENT_GUARANTEES",
        "description": "Never make overconfident outcome guarantees ('100% fixed', 'easy fix', 'quick fix')",
        "pattern": re.compile(r"\b(100%\s+fixed|guaranteed\s+reproducible|easy\s+fix|quick\s+fix|trivial\s+to\s+fix)\b", re.IGNORECASE),
        "guidance": "Report observations plainly and state what you plan to test rather than asserting triviality.",
    },
    {
        "id": "AVOID_GENERIC_BOILERPLATE",
        "description": "Avoid boilerplate compliments without technical engagement ('great project! I would love to work on this')",
        "pattern": re.compile(r"\b(great\s+project|amazing\s+repo|love\s+this\s+project)\b.*?\b(would\s+love\s+to\s+contribute|want\s+to\s+work\s+on\s+this)\b", re.IGNORECASE),
        "guidance": "Engage directly with the technical defect or deliverable rather than relying on generic compliments.",
    },
]

ANCHOR_PATTERN = re.compile(r"(#\d+|scripts?/[\w\.\-]+|\b[a-zA-Z0-9_\-]+\.(py|md|yml|yaml|ts|js)\b|reproduc|check_all|CONTRIBUTING)", re.IGNORECASE)


def evaluate_text(text: str):
    violations = []
    for rule in RULES:
        if rule["pattern"].search(text):
            violations.append(rule)

    has_technical_anchor = bool(ANCHOR_PATTERN.search(text))
    if not has_technical_anchor:
        violations.append({
            "id": "MISSING_TECHNICAL_ANCHOR",
            "description": "Must reference specific technical components, issue numbers (#...), files, or deliverables",
            "guidance": "Name the specific error, behavior, files, or deliverables involved.",
        })

    return violations


def log_result(log_path: Path, text: str, violations: list):
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    status = "PASS" if not violations else "FAIL"
    log_entry = [
        f"--- [{timestamp}] {status} ---",
        f"Text Preview: {text.strip()[:160]}...",
    ]
    if violations:
        log_entry.append("Violations:")
        for v in violations:
            log_entry.append(f"  - [{v['id']}] {v['description']}")
    else:
        log_entry.append("Result: Passed all voice-guard rules.")
    log_entry.append("")

    with open(log_path, "a", encoding="utf-8") as f:
        f.write("\n".join(log_entry) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Voice Guard: Gate outgoing contributor communications.")
    parser.add_argument("file", nargs="?", help="Path to markdown/text draft file. Reads stdin if omitted.")
    parser.add_argument("--log", default="voice-guard.log", help="Path to audit log file (default: voice-guard.log)")
    args = parser.parse_args()

    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"Error: file not found: {args.file}", file=sys.stderr)
            sys.exit(2)
        text = file_path.read_text(encoding="utf-8")
    else:
        if sys.stdin.isatty():
            print("Enter text to guard (end with EOF / Ctrl+D):", file=sys.stderr)
        text = sys.stdin.read()

    violations = evaluate_text(text)
    log_file = Path(args.log)
    if not log_file.is_absolute():
        log_file = Path(__file__).resolve().parent / args.log

    log_result(log_file, text, violations)

    if violations:
        print("[FAIL] Voice guard caught violations:", file=sys.stderr)
        for v in violations:
            print(f"  - [{v['id']}]: {v['description']}", file=sys.stderr)
            print(f"    Guidance: {v['guidance']}", file=sys.stderr)
        sys.exit(1)
    else:
        print("[PASS] Voice guard verified: comment adheres to contributor voice standards.")
        sys.exit(0)


if __name__ == "__main__":
    main()

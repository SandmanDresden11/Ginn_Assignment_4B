#!/usr/bin/env python3
"""Validate BD meeting memo outputs produced by batch_process.py.

Checks, per meeting (memo .md + audit .json pair in --out-dir):
  1. Required memo sections are present (schema Shape 1 for live/ok memos,
     Shape 2 for insufficient-input status reports). Dry-run prompt packets
     are recorded but not held to the memo schema.
  2. Every row in the "Recommended Follow-Ups" table has a non-empty Owner
     and Timeline (either a real value or an explicit "TBD" marker).
  3. Every source the audit record marks eligible (relevance score 3) has a
     URL on file.

Writes a CSV summary across all meetings to --csv.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Optional

SHAPE1_SECTIONS = [
    "1. Meeting Summary",
    "2. Key Issues Raised",
    "3. Market & Competitive Evidence",
    "4. Inferences",
    "5. Recommended Follow-Ups",
    "6. Human Review Required",
    "7. Excluded Evidence",
    "8. Scope Note",
]

SHAPE2_SECTIONS = [
    "What was checked",
    "What is missing",
    "What a human needs to supply or fix",
]


def find_pairs(out_dir: Path) -> list[dict]:
    audits = {p.stem[: -len("_audit")]: p for p in out_dir.glob("*_audit.json") if p.stem.endswith("_audit")}
    memos = {p.stem[: -len("_memo")]: p for p in out_dir.glob("*_memo.md") if p.stem.endswith("_memo")}
    keys = sorted(set(audits) | set(memos))
    return [{"key": k, "audit_path": audits.get(k), "memo_path": memos.get(k)} for k in keys]


def extract_section(memo_text: str, header_substring: str) -> Optional[str]:
    lines = memo_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## ") and header_substring in line:
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start, len(lines)):
        if lines[j].strip().startswith("## "):
            end = j
            break
    return "\n".join(lines[start:end])


def check_required_sections(memo_text: str, required: list[str]) -> list[str]:
    missing = []
    for header in required:
        if extract_section(memo_text, header) is None:
            missing.append(header)
    return missing


def parse_followup_table(section_text: str) -> list[dict]:
    rows = []
    lines = [l for l in section_text.splitlines() if l.strip().startswith("|")]
    data_lines = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells:
            continue
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
            continue  # markdown separator row
        data_lines.append(cells)

    if not data_lines:
        return rows

    header_cells = [c.lower() for c in data_lines[0]]
    body = data_lines[1:] if "action" in header_cells[0] else data_lines

    for cells in body:
        row = {
            "action": cells[0] if len(cells) > 0 else "",
            "owner": cells[1] if len(cells) > 1 else "",
            "timeline": cells[2] if len(cells) > 2 else "",
            "rationale": cells[3] if len(cells) > 3 else "",
            "confidence": cells[4] if len(cells) > 4 else "",
        }
        rows.append(row)
    return rows


def validate_meeting(pair: dict) -> dict:
    key = pair["key"]
    audit_path: Optional[Path] = pair["audit_path"]
    memo_path: Optional[Path] = pair["memo_path"]

    row = {
        "meeting_key": key,
        "meeting_number": "",
        "meeting_file": "",
        "mode": "",
        "status": "",
        "sections_missing": "",
        "actions_total": 0,
        "actions_missing_owner_or_timeline": 0,
        "sources_total": 0,
        "sources_eligible": 0,
        "sources_eligible_missing_url": 0,
        "human_review_flags": "",
        "validation_passed": False,
        "notes": "",
    }

    notes = []

    if audit_path is None or not audit_path.exists():
        notes.append("audit JSON missing")
        row["notes"] = "; ".join(notes)
        return row
    if memo_path is None or not memo_path.exists():
        notes.append("memo .md missing")
        row["notes"] = "; ".join(notes)
        return row

    try:
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        notes.append(f"audit JSON malformed: {exc}")
        row["notes"] = "; ".join(notes)
        return row

    memo_text = memo_path.read_text(encoding="utf-8")

    row["meeting_number"] = audit.get("meeting_number", "")
    row["meeting_file"] = audit.get("meeting_file", "")
    row["mode"] = audit.get("mode", "")
    row["status"] = audit.get("status", "")
    row["human_review_flags"] = ";".join(audit.get("human_review_flags", []) or [])

    sources = audit.get("sources", []) or []
    row["sources_total"] = len(sources)
    eligible = [s for s in sources if s.get("eligible")]
    row["sources_eligible"] = len(eligible)
    missing_url = [s for s in eligible if not s.get("url")]
    row["sources_eligible_missing_url"] = len(missing_url)
    non_score3_eligible = [s for s in eligible if s.get("relevance_score") != 3]
    if non_score3_eligible:
        notes.append(
            f"{len(non_score3_eligible)} source(s) marked eligible without relevance score 3"
        )

    passed = True

    if audit.get("status") == "error":
        notes.append(f"meeting processing error: {audit.get('error')}")
        row["validation_passed"] = False
        row["notes"] = "; ".join(notes)
        return row

    if audit.get("status") == "insufficient_input":
        # Shape 2 (status report) is rendered identically in dry-run and live
        # mode, since eligibility is checked before any API call is made.
        missing_sections = check_required_sections(memo_text, SHAPE2_SECTIONS)
        row["sections_missing"] = ";".join(missing_sections)
        if missing_sections:
            passed = False
            notes.append(f"missing Shape-2 sections: {', '.join(missing_sections)}")
        row["validation_passed"] = passed
        row["notes"] = "; ".join(notes) if notes else "ok (insufficient-input report)"
        return row

    if audit.get("status") == "ok" and audit.get("mode") == "dry_run":
        if "Prompt Packet" not in memo_text:
            notes.append("dry-run memo missing 'Prompt Packet' marker")
            passed = False
        row["validation_passed"] = passed
        row["notes"] = "; ".join(notes) if notes else "dry-run: schema checks not applicable"
        return row

    # status == "ok", mode == "live": full Shape 1 validation
    missing_sections = check_required_sections(memo_text, SHAPE1_SECTIONS)
    row["sections_missing"] = ";".join(missing_sections)
    if missing_sections:
        passed = False
        notes.append(f"missing sections: {', '.join(missing_sections)}")

    followups_section = extract_section(memo_text, "5. Recommended Follow-Ups") or ""
    followup_rows = parse_followup_table(followups_section)
    row["actions_total"] = len(followup_rows)
    bad_rows = 0
    for fr in followup_rows:
        if not fr["owner"].strip() or not fr["timeline"].strip():
            bad_rows += 1
    row["actions_missing_owner_or_timeline"] = bad_rows
    if followup_rows and bad_rows:
        passed = False
        notes.append(f"{bad_rows} follow-up row(s) missing owner/timeline (and no TBD marker)")
    if not followup_rows:
        notes.append("no follow-up rows found")

    if missing_url:
        passed = False
        notes.append(
            f"{len(missing_url)} relevance-3 source(s) missing a URL: "
            + ", ".join(s.get("title", "?") for s in missing_url)
        )
    if non_score3_eligible:
        passed = False

    if row["sources_eligible"] == 0:
        passed = False
        notes.append("no eligible (relevance-3) sources recorded in audit data")

    row["validation_passed"] = passed
    row["notes"] = "; ".join(notes) if notes else "ok"
    return row


def write_csv(rows: list[dict], csv_path: Path) -> None:
    fieldnames = [
        "meeting_key",
        "meeting_number",
        "meeting_file",
        "mode",
        "status",
        "sections_missing",
        "actions_total",
        "actions_missing_owner_or_timeline",
        "sources_total",
        "sources_eligible",
        "sources_eligible_missing_url",
        "human_review_flags",
        "validation_passed",
        "notes",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", required=True, type=Path, help="Directory containing *_memo.md / *_audit.json pairs")
    parser.add_argument("--csv", type=Path, default=None, help="Path to write the CSV summary (default: <out-dir>/validation_summary.csv)")
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    out_dir: Path = args.out_dir
    csv_path: Path = args.csv or (out_dir / "validation_summary.csv")

    if not out_dir.is_dir():
        print(f"ERROR: --out-dir does not exist or is not a directory: {out_dir}", file=sys.stderr)
        return 2

    pairs = find_pairs(out_dir)
    if not pairs:
        print(f"No *_memo.md / *_audit.json pairs found in {out_dir}", file=sys.stderr)
        return 2

    rows = [validate_meeting(pair) for pair in pairs]
    write_csv(rows, csv_path)

    total = len(rows)
    passed = sum(1 for r in rows if r["validation_passed"])
    failed = total - passed

    print(f"Validated {total} meeting(s): {passed} passed, {failed} failed.")
    print(f"CSV summary written to {csv_path}")
    for r in rows:
        status_str = "PASS" if r["validation_passed"] else "FAIL"
        print(f"  [{status_str}] {r['meeting_key']}: {r['notes']}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

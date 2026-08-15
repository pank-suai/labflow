#!/usr/bin/env python3
"""Validate the machine-checkable contract of SELF_REVIEW.md."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = (
    "## Scope",
    "## Requirement Coverage",
    "## Checks Executed",
    "## Code Review",
    "## Mathematics and Artifacts",
    "## Visual Report Review",
    "## Visual Evidence",
    "## Changes Requested",
    "## Blockers",
    "## Final Status",
)
STATUS_RE = re.compile(r"^Final Status:\s*(passed|changes_requested|blocked)\s*$", re.MULTILINE)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("review", type=Path)
    parser.add_argument("--require-passed", action="store_true")
    args = parser.parse_args()

    if not args.review.is_file():
        print(f"ERROR: review file does not exist: {args.review}", file=sys.stderr)
        return 1

    text = args.review.read_text(encoding="utf-8")
    missing = [heading for heading in REQUIRED_HEADINGS if heading not in text]
    if missing:
        print("ERROR: missing headings: " + ", ".join(missing), file=sys.stderr)
        return 1

    statuses = STATUS_RE.findall(text)
    if len(statuses) != 1:
        print("ERROR: expected exactly one literal 'Final Status: ...' line", file=sys.stderr)
        return 1

    status = statuses[0]
    if args.require_passed and status != "passed":
        print(f"ERROR: final status is {status}, expected passed", file=sys.stderr)
        return 2

    print(f"SELF_REVIEW_VALID status={status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

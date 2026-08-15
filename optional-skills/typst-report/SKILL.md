---
name: typst-report
description: Create and compile neutral GOST-based Typst reports.
version: 0.1.0
author: Vasilii Pankov (pank-su), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [typst, reports, gost, assignments]
    related_skills: [assignment-report, assignment-self-review]
---

# Typst Report

Optional report adapter for labflow. It creates a small, neutral GOST-based
Typst skeleton and compiles it when the Typst CLI is available. The adapter is
not tied to a university, faculty, course, logo, or assignment template.

## When to Use

- The assignment requests a Typst report.
- A project needs a basic GOST-style report skeleton before a local adapter is added.

Do not use it when the source requires a different format or an institution-specific template.

## Prerequisites

- Python 3.10+ for the initializer script.
- Typst CLI only for compilation; initialization works without Typst installed.

## How to Run

From the repository root, run through the `terminal` tool:

```bash
python optional-skills/typst-report/scripts/init_typst.py \
  --output-dir . \
  --kind lab \
  --title "Work title" \
  --subject "Subject" \
  --author "Student Name" \
  --group "Group"
```

Compile after filling the report:

```bash
typst compile docs/index.typ docs/report.pdf
```

## Quick Reference

- `--kind lab` — laboratory work.
- `--kind coursework` — course project.
- `--kind practical` — practical or calculation work.
- `--force` — replace generated files; never use it on a filled report without a backup.
- `--university`, `--faculty`, `--department`, `--city` — optional metadata.

## Procedure

1. Run `init_typst.py` with metadata known from the assignment.
2. Read `docs/index.typ` and replace the generated section placeholders with real content.
3. Keep calculations, code, figures, and raw outputs in their logical artifact directories.
4. Compile with Typst.
5. Pass the output to `assignment-self-review`.

Completion criterion: `docs/index.typ` exists, all referenced files exist, and
compilation succeeds when a Typst installation is available.

## Rules

- Do not invent student, university, or assignment metadata.
- The template is a starting point, not a substitute for source requirements.
- Keep GOST conventions in the adapter; keep workflow logic in core skills.
- Do not claim a PDF was created if Typst was unavailable or compilation failed.

## Self-Review Handoff

Run `typst compile docs/index.typ docs/report.pdf`, then confirm that the PDF is
non-empty and that required sections, figures, tables, and formulas are present.

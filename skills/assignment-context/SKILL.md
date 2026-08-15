---
name: assignment-context
description: Extract requirements and constraints from an assignment.
version: 0.1.0
author: Vasilii Pankov (pank-su), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [assignments, requirements, planning, context]
    related_skills: [assignment-workflow, assignment-self-review]
---

# Assignment Context

Convert an assignment brief, methodology, or course-project specification into a
structured, source-grounded context. This skill discovers what must be done; it
does not implement the solution or write the final report.

## When to Use

- Before coding or mathematical work on a lab, practical, or course project.
- When the assignment is spread across PDFs, images, source files, and user notes.

## Procedure

1. Inventory every input file and record its path and type.
2. Extract readable text from the methodology; use an OCR skill for scanned pages.
3. Identify the objective, tasks, variant, inputs, constraints, algorithms, and deliverables.
4. Separate explicit requirements from assumptions and unresolved questions.
5. Write `context/TASK.md` in human-readable form.
6. Write `context/context.yaml` using `references/context-schema.md`.
7. Write `context/open_questions.md`; use an empty list when nothing is missing.
8. Create a requirement checklist mapping each requirement to a planned artifact.

## Rules

- Never select a variant or input value by guessing.
- Preserve exact formulas, file extensions, and required section names.
- Mark contradictions between sources instead of silently resolving them.
- Do not add university-specific defaults unless the source explicitly provides them.
- Do not modify the methodology or user-provided data.

## Output Contract

```text
context/TASK.md
context/context.yaml
context/open_questions.md
context/requirements-checklist.md
```

Completion means each explicit requirement has an identifier and a planned
review method. Unknown values must appear in `open_questions.md`.

## Self-Review Handoff

Compare the checklist against the original source. Confirm that every required
input, output, restriction, and report section appears in the generated context.

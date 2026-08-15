---
name: labflow-guap
description: Apply GUAP-specific study and submission rules.
version: 0.1.0
author: Vasilii Pankov (pank-su), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [GUAP, labs, coursework, teachers, defense]
    related_skills: [labflow, labflow-typst, labflow-guap-mcp]
---

# Labflow GUAP

Apply university-specific context on top of the generic `labflow` workflow. This
skill contains only GUAP rules, teacher and subject patterns, defense preparation,
and report conventions observed in the supplied archive. It does not replace the
university-agnostic workflow and does not access Moodle.

## When to Use

- The task belongs to GUAP or mentions `pro.guap.ru`.
- The report needs GUAP-specific title-page or defense preparation.
- A teacher or subject pattern from `references/` may affect the plan.

Do not use this skill as evidence for a current deadline or task description. Read
live task details through `labflow-guap-mcp` first when the cabinet is available.

## Source Policy

Apply evidence in this order:

1. Current task details from the GUAP cabinet.
2. The methodology or files attached to the task.
3. Explicit user-provided notes.
4. A reference marked `confirmed` from the archive.
5. A reference marked `observed` as a planning hint only.

Never turn an `observed` pattern into a hard requirement without checking the
current task. If sources conflict, preserve the conflict and ask the user when it
can change the deliverable.

## Procedure

1. Load `references/guap-rules.md`.
2. Identify the discipline and teacher from the live task or user context.
3. Load the matching teacher and subject references before planning.
4. Copy only confirmed requirements into `context/context.yaml`.
5. Add teacher-specific preparation items to `context/open_questions.md` or a
   separate defense checklist; do not hide them in the report.
6. Run the generic `labflow` phases.
7. If a report is required, run `labflow-typst` only after the context is complete.
8. Before submission, produce a defense checklist and confirm the current task,
   allowed extension, deadline, and submission format from the cabinet.

## GUAP Rules

- A task marked `ожидает проверки` is already submitted; do not redo it by default.
- A missing deadline is not permission to invent one.
- The current task description controls the required file format and submission path.
- A title page is generated only from known context metadata.
- If the task mentions a defense, prepare the student for an oral explanation of
  the method, inputs, intermediate results, and conclusions.
- Teacher advice is guidance for preparation, not a guarantee of grading behavior.

## Output Contract

The skill adds only GUAP-specific context to the generic workspace:

```text
context/guap-context.yaml
context/defense-checklist.md       # when defense is required or expected
```

The generic report, source code, mathematics, and self-review artifacts remain
owned by the corresponding `labflow-*` skills.

## Verification Handoff

Before claiming readiness, confirm that every GUAP-specific rule in the plan has a
source label (`confirmed`, `user_note`, or `observed`) and that no current deadline
or submission format was inferred from an old archive.

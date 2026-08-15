---
name: assignment-workflow
description: Run a reproducible workflow for academic assignments.
version: 0.1.0
author: Vasilii Pankov (pank-su), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [assignments, labs, coursework, workflow, reproducibility]
    related_skills: [assignment-context, assignment-coding, assignment-math, assignment-report, assignment-self-review]
---

# Assignment Workflow

Run a university-agnostic workflow for labs, practical assignments, calculation
works, and course projects. This skill owns phase ordering, artifact contracts,
blocking questions, and completion gates; specialist skills own their domains.
It does not prescribe a university, language, report format, or project template.

## When to Use

- A user provides a methodology, assignment, course-project brief, or dataset.
- A task needs a traceable path from requirements to code, calculations, and report.
- Existing specialist skills should be reused when available.

Do not use it for a one-line calculation or an isolated code fix with no assignment context.

## Prerequisites

- The assignment source and all available input files are present in the workspace.
- The workspace is writable.
- If a required input is missing, record it in `context/open_questions.md` instead of guessing.

## Phase Selection

1. Always run `assignment-context` first.
2. Run `assignment-coding` when the context requires software or simulations.
3. Run `assignment-math` when formulas, numerical methods, statistics, or data analysis are required.
4. Run `assignment-report` when a report is requested or required.
5. Always launch a fresh subagent with `assignment-self-review` before claiming completion.

Use matching external skills for PDF extraction, a programming language, testing,
Jupyter, Typst, LaTeX, DOCX, or PDF when they are available. Treat them as
capabilities, not hard dependencies. If one is unavailable, use the fallback
procedure and record the limitation.

## Procedure

### 1. Establish the workspace

Inspect the available files and create only neutral directories: `context/`,
`src/`, `tests/`, `math/`, `artifacts/`, `report/`, and `evidence/` as needed.
Completion criterion: every input file has a known path and no source file was modified.

### 2. Build the context

Run `assignment-context`. It must produce `context/TASK.md`,
`context/context.yaml`, and `context/open_questions.md`.
Completion criterion: requirements, constraints, inputs, outputs, and unresolved questions are explicit.

### 3. Resolve blockers

Ask the user only for information that blocks a correct result: missing variant,
missing dataset, ambiguous output requirement, or inaccessible source.
Completion criterion: every blocking question is answered or explicitly accepted as a blocker.

### 4. Produce domain artifacts

Run coding and/or mathematics specialists. Keep code, calculations, logs, figures,
and tables outside the report source.
Completion criterion: every required domain result has a reproducible command or notebook and a saved output.

### 5. Assemble the report

Run `assignment-report`. Choose the requested format through an adapter; do not
assume Typst, GOST, a title page, or a fixed directory layout.
Completion criterion: the report references only existing artifacts and contains no invented results.

### 6. Run the self-review

Use `delegate_task` to launch a fresh subagent with the `assignment-self-review`
skill. Give it the workspace path, the assignment context, and permission to run
read-only checks, tests, builds, and report rendering. The subagent must write
`SELF_REVIEW.md` with findings and a final status.

Fix every `changes_requested` finding in the responsible phase, then launch a
new review subagent. Do not reuse the previous review as proof after changes.
Completion criterion: `SELF_REVIEW.md` records the review scope, executed checks,
visual inspection results, requirement coverage, and final status `passed`.

## Rules

- Do not invent missing values, variants, execution results, or citations.
- Prefer the assignment source and user-provided data over general knowledge.
- Keep planning, implementation, mathematics, writing, and self-review separate.
- Preserve raw outputs so important claims can be checked.
- Do not call an assignment complete without real execution and self-review output.
- Never overwrite user files without an explicit reason and a recoverable copy.
- If a specialist skill has stronger domain rules, follow those rules inside its phase.

## Failure Recovery

If a phase fails, preserve its logs, state the failing phase, and retry only after
identifying the cause. Do not silently skip a failed compile, test, or calculation.

## Completion

The workflow is complete only when:

- `context/TASK.md` exists;
- All required code and mathematics artifacts exist;
- Required commands or notebooks were executed;
- The report format was compiled or rendered when applicable;
- `SELF_REVIEW.md` has final status `passed` and no unresolved blocking finding.

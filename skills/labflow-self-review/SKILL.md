---
name: labflow-self-review
description: Review code, report appearance, and requirement coverage.
version: 0.1.0
author: Vasilii Pankov (pank-su), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [tasks, self-review, code-quality, visual-review, requirements]
    related_skills: [labflow, labflow-context, labflow-coding, labflow-math, labflow-report]
---

# Labflow Self-Review

Review an academic task as an independent fresh-agent pass. Check whether
the requirements are fulfilled, the code is readable and usable, and the report
looks correct after rendering. This skill produces findings and a decision; it
does not silently repair the work it reviews.

## When to Use

- At the end of every `labflow` run.
- After changing code, calculations, report structure, or report formatting.
- Before presenting a lab, practical task, or course project as finished.

## Review Model

The workflow should launch this skill in a fresh subagent through `delegate_task`.
The parent agent supplies the workspace path and asks the reviewer to inspect the
current state. The reviewer must not rely on the parent agent's claim that a step
was completed.

Recommended delegation prompt:

```text
Review the task in <workspace> using labflow-self-review.
Read context/TASK.md, context/context.yaml, the requirements checklist, source
files, execution artifacts, and the report. Explicitly review all four dimensions:
(1) requirement coverage, (2) code quality and behavior, (3) mathematics and
artifacts, and (4) visual report appearance. Run checks, tests, builds, notebooks,
and report compilation/rendering when available. Inspect rendered report pages
and representative code files. Do not rewrite tracked source files.
Write SELF_REVIEW.md in <workspace> using the required headings, checks table,
visual evidence section, severity labels, and a literal final line such as
"Final Status: passed".
```

If `delegate_task` is unavailable, run the same procedure directly and state that
no fresh subagent was available. This is a fallback, not equivalent evidence.

## Procedure

### 1. Establish review scope

Read the original task source, `context/TASK.md`, `context/context.yaml`,
and `context/requirements-checklist.md`. List every explicit requirement and its
expected evidence.

Completion criterion: the review scope is based on source material, not on the
implementation's self-description.

### 2. Check requirement coverage

For each requirement, locate the implementation, calculation, report section,
and verification evidence. Mark each item `passed`, `changes_requested`, or
`blocked`. A file's existence is not evidence that its behavior is correct.

Check especially:

- objective and all task items;
- variant and input data;
- required algorithms and formulas;
- required output files;
- tests, tables, figures, screenshots, and report sections;
- restrictions on language, libraries, file formats, and tools.

### 3. Review the code

Inspect representative and central source files. Run the build, tests, formatter,
and a representative execution when available. Review:

- readability and naming;
- structure and separation of responsibilities;
- correctness at boundaries and failure cases;
- dead code, placeholders, duplicated logic, and hardcoded data;
- error handling and user-visible output;
- consistency with the task and language conventions.

Record exact file paths and line numbers for findings. Do not rewrite source files.

### 4. Review the mathematics and artifacts

Run the notebook or calculation script when possible. Check formulas, units,
intermediate values, rounding, tolerances, tables, and figures. Confirm that
reported values match the generated artifacts and that plots have readable labels,
legends, axes, and units.

### 5. Review the report visually

Compile or render the report with the selected adapter, writing generated output
to a temporary directory or `artifacts/self-review/`. Inspect representative
pages, including the title page, a dense content page, a page with code or a
formula, a page with tables or figures, and the final page. Use `vision_analyze`
when available; otherwise inspect the rendered output with an available viewer or
record visual review as blocked.

Check:

- no clipped or overflowing text;
- no blank or nearly blank accidental pages;
- readable font sizes and line spacing;
- consistent headings, numbering, margins, and page breaks;
- figures and tables fit the page and have captions;
- code listings are readable;
- formulas render correctly;
- references and cross-references resolve;
- title-page metadata is correct;
- conclusions match the actual results.

### 6. Write the review

Create `SELF_REVIEW.md` with this structure:

```markdown
# Self-Review

## Scope

## Requirement Coverage

| ID | Requirement | Evidence | Status | Finding |
|---|---|---|---|---|

## Checks Executed

| Check | Command or tool | Exit status | Evidence | Status |
|---|---|---:|---|---|

## Code Review

## Mathematics and Artifacts

## Visual Report Review

## Visual Evidence

## Changes Requested

## Blockers

## Final Status

`Final Status: passed` | `Final Status: changes_requested` | `Final Status: blocked`
```

Every finding must include a severity (`blocker`, `major`, or `minor`), a file or
artifact path, and a concrete recommended change. A review with no findings must
still list the checks that were actually performed and the visual evidence that
was inspected.

## Rules

- Do not rewrite tracked solution files, source data, notebooks, or report sources
  during the review.
- Generated outputs may be written only to a temporary directory or
  `artifacts/self-review/`.
- Do not call a check passed when it was not executed.
- Do not infer visual correctness from source code alone.
- Do not approve a report that has not been rendered when visual review is required.
- Do not ignore a requirement because it is difficult to test.
- Distinguish `blocked` from `changes_requested`.
- Prefer concrete findings over general advice.

## Final Status

Use `passed` only when all requirements are covered, code and calculations have
been reviewed, and the report has passed visual inspection. Use
`changes_requested` when the parent agent can fix findings. Use `blocked` when a
missing input, unavailable tool, or inaccessible source prevents a meaningful review.

The parent agent must validate `SELF_REVIEW.md` with
`skills/labflow-self-review/scripts/check_self_review.py`. It must fix
`changes_requested` findings and launch a new fresh self-review subagent. If the
review is `blocked`, the parent must resolve the blocker or keep the task
blocked. A previous review does not remain valid after changes.

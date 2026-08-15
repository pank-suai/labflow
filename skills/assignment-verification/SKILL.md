---
name: assignment-verification
description: Independently verify assignment artifacts and deliverables.
version: 0.1.0
author: Vasilii Pankov (pank-su), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [assignments, verification, quality, testing]
    related_skills: [assignment-workflow, assignment-context, assignment-coding, assignment-math, assignment-report]
---

# Assignment Verification

Act as an independent quality gate for an academic assignment. Verify the
implementation, calculations, evidence, and report against the context. Do not
rewrite the solution while reviewing it.

## When to Use

- At the end of every `assignment-workflow` run.
- After changing code, calculations, report structure, or report format.

## Procedure

1. Read the original checklist and identify every required item.
2. Confirm all required inputs and outputs exist.
3. Re-run build, tests, representative commands, notebooks, or report compilation.
4. Check that report claims match saved outputs and logs.
5. Check figures, tables, formulas, and source references for broken paths.
6. Record pass, fail, blocked, and not-applicable statuses in `VERIFICATION.md`.
7. Return to the responsible phase for every failure and repeat the checks.

## Rules

- A missing input is `blocked`, not `passed`.
- An unexecuted command is `not verified`, not `passed`.
- Do not infer correctness from file presence alone.
- Do not silently downgrade a requirement because it is inconvenient.
- Preserve the command and exit code for each executable check.

## Output Contract

```text
VERIFICATION.md
```

The file must include a status table, commands run, important outputs, known
limitations, and a final status of `passed`, `blocked`, or `failed`.

## Verification

The reviewer is finished only when the final status is explicit and every
non-passed item has an owner, cause, and next action.

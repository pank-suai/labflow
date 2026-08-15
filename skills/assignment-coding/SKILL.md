---
name: assignment-coding
description: Implement and test the programming part of an assignment.
version: 0.1.0
author: Vasilii Pankov (pank-su), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [assignments, coding, testing, reproducibility]
    related_skills: [assignment-workflow, assignment-context, assignment-self-review]
---

# Assignment Coding

Implement the software portion of an assignment from the structured context.
Use language-specific, testing, debugging, and data-processing skills when they
are available. This skill produces executable artifacts and evidence, not prose
for the final report.

## When to Use

- The context requires a program, simulation, algorithm, interface, or data pipeline.

Do not use it when the assignment is purely theoretical or computational with no code.

## Procedure

1. Read `context/TASK.md`, `context/context.yaml`, and the checklist.
2. Select the language and toolchain from the context; do not default silently.
3. Design the smallest implementation that satisfies explicit requirements.
4. Add focused tests for normal cases, boundary cases, and required examples.
5. Run formatting, build, tests, and a representative execution.
6. Save stdout, stderr, commands, exit codes, and generated files under `artifacts/`.
7. Write `artifacts/code-results.md` mapping requirements to source files and tests.

## Rules

- Keep implementation under `src/` unless the context specifies another path.
- Keep tests separate from report sources.
- Never claim a test passed without running it.
- Preserve failed outputs when debugging; they are useful evidence.
- Do not put credentials or private data in source or artifacts.

## Output Contract

At minimum, produce:

```text
src/
tests/                 # when tests are applicable
artifacts/program-output.txt
artifacts/test-results.txt
artifacts/code-results.md
```

## Self-Review Handoff

Re-run the documented build and test commands from a clean state. Confirm that
all code-related checklist items point to a real file and a real execution result.

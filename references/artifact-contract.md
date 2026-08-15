# Artifact contract

labflow separates context, implementation, calculations, report sources, and verification.

## Required logical artifacts

| Artifact | Purpose |
|---|---|
| `context/TASK.md` | Human-readable assignment requirements |
| `context/context.yaml` | Machine-readable context |
| `context/open_questions.md` | Missing or contradictory information |
| `context/requirements-checklist.md` | Requirement-to-verification map |
| `artifacts/` | Raw execution outputs and logs |
| `math/` | Reproducible calculations and figures |
| `report/` | Report sources and compiled outputs |
| `VERIFICATION.md` | Independent quality gate |

Directories are logical, not mandatory. A project may configure different paths in `context.yaml`.

## Provenance rule

Every important report claim must point to at least one of:

- an input source;
- a code file plus execution log;
- a notebook or calculation script plus output;
- a generated table or figure;
- a verification command.

The report must not be the only place where a result exists.

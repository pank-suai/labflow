# Artifact contract

Labflow separates context, implementation, calculations, report sources, and verification.

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

- An input source;
- A code file plus execution log;
- A notebook or calculation script plus output;
- A generated table or figure;
- A verification command.

The report must not be the only place where a result exists.

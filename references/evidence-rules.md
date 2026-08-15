# Evidence rules

1. Every numerical result comes from a reproducible calculation or execution.
2. Every required feature maps to a source file, test, output, or review check.
3. Every figure and table has a generating file or command.
4. A failed or skipped check is recorded explicitly.
5. User-provided values are labeled as inputs, not independently verified facts.
6. Report prose must not claim more than the evidence supports.
7. When sources conflict, preserve both versions and ask for resolution if it affects correctness.

Recommended matrix:

| Requirement | Implementation | Evidence | Report section | Status |
|---|---|---|---|---|
| R-001 | `src/...` | `artifacts/...` | 3.1 | passed |

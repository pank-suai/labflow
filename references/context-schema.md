# Context schema

`context/context.yaml` is intentionally small and extensible. Empty values mean
unknown; they must not be replaced with guesses.

```yaml
kind: lab | practical | coursework | project | other
title: ""
subject: ""
variant: null
objective: ""

inputs:
  methodology: ""
  data_files: []
  source_files: []

requirements:
  code: false
  mathematics: false
  report: true
  tests: false
  figures: false
  tables: false

constraints:
  language: ""
  libraries: []
  tools: []
  file_formats: []
  forbidden_tools: []

deliverables:
  files: []
  report_format: ""
  report_sections: []

open_questions: []
```

Projects may add keys, but existing keys retain their meaning. Store university,
faculty, group, or teacher metadata only when the assignment requires it; these
are inputs, not universal defaults.

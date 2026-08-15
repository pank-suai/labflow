# Contributing

Keep the core skills university- and template-agnostic. Put format-specific
behavior under an optional skill or adapter.

Before committing:

```bash
python3 -m unittest discover -s tests -v
python3 optional-skills/typst-report/scripts/init_typst.py --help
```

If Typst is installed, compile a generated smoke report and confirm that the PDF
is non-empty. Do not add real student data or private assignment files.

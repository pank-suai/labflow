# Report adapters

The core workflow is format-neutral. A report adapter translates verified
artifacts into a requested document format.

## Adapter responsibilities

- Define the output extension and source layout;
- Map metadata into the format's title page or header;
- Compile or render the source;
- Report missing tools without pretending compilation succeeded;
- Preserve the requirement-to-evidence matrix.

## Default behavior

If the assignment does not specify a format, produce Markdown. Use an optional
formatter skill for Typst, LaTeX, DOCX, or PDF. University-specific title pages,
logos, GOST variants, and typography belong in adapters or templates, never in
the core workflow.

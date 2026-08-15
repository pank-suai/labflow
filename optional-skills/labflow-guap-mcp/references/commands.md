# GUAP CLI Commands

The CLI is provided by `mcp-guap`.

## Authentication

```bash
guap pro auth
guap pro check
```

`auth` opens browser-based login. `check` validates the saved session. Credentials
are entered by the user; the agent must not type or store passwords.

## Tasks

```bash
guap pro tasks --format json
guap pro tasks --status 1 --format json
guap pro task <TASK_ID> --format json
```

Important task fields:

- `task_id`
- `discipline`
- `name`
- `type`
- `semester`
- `teacher`
- `points_max`
- `deadline`
- `allowed_extensions`
- `description`
- `extra_materials`
- `submitted_reports`

Status values must be read from the live response. Do not infer them from an old archive.

## Materials and Profile

```bash
guap pro materials --urls --format json
guap pro materials --subject <SUBJECT_ID> --format json
guap pro profile --format json
```

## Submission

Before using an upload command or MCP `submit_report` tool:

1. Fetch the task details.
2. Confirm the allowed extension.
3. Confirm the current task is not already awaiting review.
4. Ask the user to approve the final file.
5. Submit the exact file and retain the response.

The MCP server also exposes profile, teacher, subject, group-order, material,
download, and report-submission tools. Consult the installed server version for
its exact tool schema.

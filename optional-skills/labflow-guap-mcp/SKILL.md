---
name: labflow-guap-mcp
description: Use the GUAP cabinet through MCP and CLI.
version: 0.1.0
author: Vasilii Pankov (pank-su), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [GUAP, MCP, CLI, pro.guap.ru, tasks]
    related_skills: [labflow, labflow-guap]
---

# Labflow GUAP MCP

Use the GUAP personal cabinet at `pro.guap.ru` through the `mcp-guap` MCP server
and its `guap` CLI. This skill documents access and task retrieval; it does not
contain teacher rules or solve laboratory work.

## When to Use

- The user asks for current GUAP tasks, deadlines, materials, profile data, or submission status.
- `labflow-guap` needs live task details before applying archive patterns.
- A report must be uploaded after the user has reviewed it.

Do not use it for Moodle. Moodle integration is intentionally a separate future project.

## Prerequisites

- `uv`.
- A GUAP account.
- The `mcp-guap` package from `https://github.com/overwaven/mcp-guap`.
- Authentication through the browser or a user-provided session cookie.

## Installation

For the CLI:

```bash
uvx --from git+https://github.com/overwaven/mcp-guap guap pro check
```

For an MCP client:

```json
{
  "mcpServers": {
    "guap": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/overwaven/mcp-guap", "mcp-guap"]
    }
  }
}
```

Authenticate interactively:

```bash
uvx --from git+https://github.com/overwaven/mcp-guap guap pro auth
```

Never ask the agent to receive or store the user's password. The user completes
browser authentication themselves.

## Procedure

1. Run `guap pro check`.
2. If authentication is invalid, run `guap pro auth` and let the user log in.
3. Retrieve current tasks with `guap pro tasks --format json`.
4. Retrieve the full task before planning with `guap pro task <ID> --format json`.
5. Read materials with `guap pro materials --urls --format json`.
6. Pass the task JSON and material paths to `labflow-guap` and the generic `labflow` workflow.
7. Before submission, confirm the task ID, extension, deadline, and current status.
8. Submit only after the user approves the final artifact.

## Safety Rules

- Treat live cabinet data as authoritative for current deadlines and statuses.
- Do not resubmit tasks marked `ожидает проверки` without explicit user instruction.
- Do not upload a report automatically after generation.
- Do not expose cookies, tokens, or private task URLs in committed files.

## References

See `references/commands.md` for the CLI command map and output fields.

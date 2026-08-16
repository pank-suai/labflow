# Installing `labflow`

`labflow` uses the open Agent Skills format. The repository contains portable
skill directories with `SKILL.md`, references, scripts, and templates. There is no
package build step.

## Claude Code, Codex CLI, and OpenCode

Install the core workflow globally. Leave out `--agent` and `--yes`: `npx skills`
will show the available harnesses, let the user select one or more targets, and
ask for an explicit confirmation before copying files.

```bash
npx skills add pank-su/labflow \
  --skill labflow \
  --skill labflow-context \
  --skill labflow-coding \
  --skill labflow-math \
  --skill labflow-report \
  --skill labflow-self-review \
  --global \
  --copy
```

Install the optional Typst adapter when reports need it:

```bash
npx skills add pank-su/labflow \
  --skill labflow-typst \
  --global \
  --copy
```

For a project-local installation, run the same commands from the project root and
remove `--global`.

Native discovery locations:

| Harness | Project | User |
| --- | --- | --- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex CLI | `.agents/skills/` | `~/.agents/skills/` |
| OpenCode | `.opencode/skills/` | `~/.config/opencode/skills/` |

## Hermes Agent

Install the core skills directly:

```bash
hermes skills install https://raw.githubusercontent.com/pank-su/labflow/main/skills/labflow/SKILL.md --name labflow
hermes skills install https://raw.githubusercontent.com/pank-su/labflow/main/skills/labflow-context/SKILL.md --name labflow-context
hermes skills install https://raw.githubusercontent.com/pank-su/labflow/main/skills/labflow-coding/SKILL.md --name labflow-coding
hermes skills install https://raw.githubusercontent.com/pank-su/labflow/main/skills/labflow-math/SKILL.md --name labflow-math
hermes skills install https://raw.githubusercontent.com/pank-su/labflow/main/skills/labflow-report/SKILL.md --name labflow-report
hermes skills install https://raw.githubusercontent.com/pank-su/labflow/main/skills/labflow-self-review/SKILL.md --name labflow-self-review
```

Optional Typst adapter:

```bash
hermes skills install https://raw.githubusercontent.com/pank-su/labflow/main/skills/labflow-typst/SKILL.md --name labflow-typst
```

Verify:

```bash
hermes skills list
```

## GUAP extension

Install `labflow` first, then install the separate GUAP skill:

```bash
npx skills add pank-su/guap-skill --skill guap-pro --global --copy
hermes skills install https://raw.githubusercontent.com/pank-su/guap-skill/main/skills/guap-pro/SKILL.md --name guap-pro
```

`guap-pro` supplies GUAP-specific references and cabinet access; it does not
replace the generic `labflow` workflow.

## Use from a checkout

```bash
python3 skills/labflow-typst/scripts/init_typst.py \
  --context context/context.yaml \
  --output-dir .
```

The skill's scripts, references, and templates are resolved relative to each
skill directory. Do not assume that the project CWD is the skill directory after
installation.

## Updating or removing

```bash
npx skills update labflow
npx skills remove labflow
hermes skills update
hermes skills uninstall labflow
```

Restart a harness if it does not discover an updated skill immediately.

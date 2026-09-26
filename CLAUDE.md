# Claude Code adapter

This repository's operating instructions live in **[AGENTS.md](AGENTS.md)**. Read
it first; it is the source of truth for how to work here. This file only adapts
that guidance to Claude Code and is intentionally thin — it does not restate the
workflow.

## Where things are

- **[PROJECT.md](PROJECT.md)** — research intent, context, supplied resources, constraints, desired outputs, and stopping conditions.
- **[AGENTS.md](AGENTS.md)** — operating instructions, evidence conventions, and stopping rules.
- **[STATE.md](STATE.md)** — the current checkpoint: answer, uncertainty, alternatives, and next action.
- **[ARCHITECTURE.md](ARCHITECTURE.md)** — the research loop and workspace boundaries.
- **[evidence/RECORDS.md](evidence/RECORDS.md)** — evidence (`E`), decisions (`D`), and consequential human input (`H`).
- **[outputs/REPORT.md](outputs/REPORT.md)** — the final synthesis; initially an explicitly unfinished outline.

## How to start or resume

- **New project:** run `/setup` (see [.claude/commands/setup.md](.claude/commands/setup.md)) after discussing the research idea. It writes PROJECT.md and initializes STATE.md.
- **Continue work:** run `/loop` (see [.claude/commands/loop.md](.claude/commands/loop.md)) to start or resume the research defined in PROJECT.md.

Both slash commands wrap the canonical prompts in [README.md](README.md); the
README prompts remain authoritative if the two ever differ.

## Evidence discipline

Keep the distinction: human-provided information (`H`) → agent interpretation →
evidence (`E`) → research conclusion, with consequential decisions in `D`.
Authorization preserves its stated limits and is not evidence for a claim. Do not
store routine conversation or exhaustive transcripts.

## Maintainer check

`python3 tools/validate_template.py .` validates the template's structure and that
STATE.md / REPORT.md remain uninitialized. It runs in CI on pull requests.

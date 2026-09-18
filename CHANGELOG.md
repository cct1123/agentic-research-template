# Changelog

All notable changes to this template are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- `tools/validate_template.py`: standard-library structural validator for the
  core files, internal Markdown links and anchors, fenced blocks, tables, spaced
  paths, and the uninitialized checkpoint/report state. Makes a "PASS - N
  structural checks" result reproducible from the repository.
- `.github/workflows/validate.yml`: CI that runs the validator on pushes to
  `main` and on pull requests.
- `.gitignore`: keep local credentials, private inputs, and working data out of
  version control (the template previously had none despite handling private data
  and running analysis code).
- `LICENSE`: MIT license (update the copyright holder before reuse).
- `CLAUDE.md` and `.claude/commands/setup.md` + `.claude/commands/loop.md`: a thin
  Claude Code adapter and slash commands that wrap the canonical README prompts.
- `CHANGELOG.md`: this file.
- README note pointing to the maintainer tooling above.
- `AGENTS.md`: a "Persistent loop robustness" section governing multi-run
  work — single-writer checkpoint ownership with stale-entry reclaim; recording
  intent before external, irreversible, costly, or long-running actions; treating
  an unresolved in-flight entry as an UNKNOWN outcome to verify rather than
  assume; clearing the in-flight entry last so an interruption is detectable;
  stall detection with an escalation ladder; and a ruled-out list that keeps
  negative knowledge cheap to find.
- `STATE.md`: a "Loop continuity" section carrying those rules across runs —
  session owner / last checkpoint, in-flight action, attempts on current
  question, and a "Ruled out / do not retry" table.
- Validator checks that the loop-continuity fields exist, that the template ships
  with no outstanding in-flight action, and that the robustness rules are present
  in `AGENTS.md`.
- README visual guides: a project lifecycle diagram (discussion → setup → loop →
  finished or blocked) and a persistence diagram showing resume reconciliation,
  intent-before-action, the numbered write order, and the no-new-evidence path.
  Both stay higher level than the detailed diagram in `ARCHITECTURE.md`.

### Changed

- `ARCHITECTURE.md`: the research loop diagram now shows resume reconciliation,
  saving records before state and clearing the in-flight entry last, and the
  no-new-evidence path to changing method, recording a ruled-out avenue, or
  escalating one specific question.
- Renamed `prompt record.txt` → `prompt-record.txt` for portability (no spaces in
  tracked paths).

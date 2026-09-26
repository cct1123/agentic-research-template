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

- Fixed the README diagram connection lines in GitHub dark mode. The diagrams
  set `theme: 'base'`, whose default `lineColor` is `#333333` — that reads at
  12.63:1 on the light canvas but only 1.50:1 on dark `#0d1117` and 1.19:1 on
  dark-dimmed `#22272e`, so the edges were effectively invisible to dark-mode
  readers. Set an explicit `lineColor` of `#768390`, chosen by computing WCAG
  relative-luminance contrast rather than by eye: 3.87:1 on light, 4.88:1 on
  dark, 3.88:1 on dark-dimmed, and 3.32:1 against the base theme's own node fill
  where an edge crosses a node. All clear the 3:1 threshold for non-text
  graphical elements. Only the line colour changes: the theme, the node fills,
  and `fontSize` are all untouched.
- Rewrote the research loop prompt. The previous one-liner delegated everything to
  `AGENTS.md`, which is the right instinct, but carried no posture: nothing told
  the agent to keep working through several actions, to decide routine reversible
  things without asking, or to checkpoint before stopping. Those are the parts a
  kickoff message has to supply, because they set stopping behaviour for the whole
  run. It still points at `AGENTS.md` for every procedure rather than restating
  it. Both prompts moved from blockquotes to fenced blocks so multi-paragraph text
  copies cleanly; the setup prompt's wording is unchanged.
  `.claude/commands/loop.md` is kept byte-identical to the README prompt.
- `ARCHITECTURE.md`: the research loop diagram now shows resume reconciliation,
  saving records before state and clearing the in-flight entry last, and the
  no-new-evidence path to changing method, recording a ruled-out avenue, or
  escalating one specific question.
- Renamed `prompt record.txt` → `prompt-record.txt` for portability (no spaces in
  tracked paths).

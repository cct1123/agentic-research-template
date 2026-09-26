#!/usr/bin/env python3
"""Structural validator for the autonomous agent workspace templates.

Standard-library only. Checks that the template's core files exist, that their
internal Markdown links and heading anchors resolve, that fenced code blocks and
Markdown tables are well formed, and that the checkpoint/report files remain in
their uninitialized template state (so the repository can be reused without stale
project claims).

This makes the "PASS - N structural checks" claim in the template's review notes
reproducible: run it and read the count it prints.

Usage:
    python3 tools/validate_template.py [REPO_ROOT]

REPO_ROOT defaults to the parent directory of this script. Exits 0 when every
assertion passes and 1 otherwise. The engineering and research templates share
this script; the expected file set is auto-detected from the layout.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# --- check accounting --------------------------------------------------------

_passed = 0
_failures: list[str] = []


def check(condition: bool, message: str) -> bool:
    """Record one structural assertion."""
    global _passed
    if condition:
        _passed += 1
    else:
        _failures.append(message)
    return bool(condition)


# --- markdown helpers --------------------------------------------------------

_FENCE_RE = re.compile(r"^\s*(```+|~~~+)")
_LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_INLINE_CODE_RE = re.compile(r"`+[^`]*`+")


def strip_code_fences(text: str) -> tuple[str, bool]:
    """Return (text-without-fenced-blocks, fences_balanced)."""
    out_lines: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        m = _FENCE_RE.match(line)
        if m:
            marker = m.group(1)[0] * 3
            if fence is None:
                fence = marker
                continue
            if line.strip().startswith(fence):
                fence = None
                continue
        if fence is None:
            out_lines.append(line)
    return "\n".join(out_lines), fence is None


def slug(heading_text: str) -> str:
    """GitHub-style heading anchor slug."""
    text = heading_text.strip().lower()
    # drop inline markdown links, keeping their text
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    # drop inline code/formatting markers
    text = text.replace("`", "")
    # remove characters other than word chars, spaces and hyphens
    text = re.sub(r"[^\w\s-]", "", text)
    text = text.replace(" ", "-")
    return text


def headings_of(text: str) -> list[str]:
    body, _ = strip_code_fences(text)
    out = []
    for line in body.splitlines():
        m = _HEADING_RE.match(line)
        if m:
            out.append(m.group(2))
    return out


def anchors_of(text: str) -> set[str]:
    seen: dict[str, int] = {}
    anchors: set[str] = set()
    for h in headings_of(text):
        base = slug(h)
        if base in seen:
            seen[base] += 1
            anchors.add(f"{base}-{seen[base]}")
        else:
            seen[base] = 0
            anchors.add(base)
    return anchors


def links_of(text: str) -> list[str]:
    # Skip fenced blocks and inline code spans: links shown there are format
    # examples, not real links to resolve.
    body, _ = strip_code_fences(text)
    body = _INLINE_CODE_RE.sub(" ", body)
    return _LINK_RE.findall(body)


def tables_consistent(text: str) -> bool:
    """Every contiguous GitHub table block has a uniform column count."""
    body, _ = strip_code_fences(text)
    lines = body.splitlines()
    ok = True
    i = 0
    while i < len(lines):
        line = lines[i]
        is_row = line.lstrip().startswith("|")
        if is_row:
            block = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                block.append(lines[i])
                i += 1
            if len(block) >= 2:
                counts = [row.count("|") for row in block]
                if len(set(counts)) != 1:
                    ok = False
        else:
            i += 1
    return ok


# --- template layout detection ----------------------------------------------


def core_files(root: Path) -> list[str]:
    """Core files common to both templates plus template-specific records."""
    common = [
        "README.md",
        "PROJECT.md",
        "AGENTS.md",
        "ARCHITECTURE.md",
        "STATE.md",
        "outputs/REPORT.md",
    ]
    if (root / "records").is_dir():
        # engineering template
        common += ["records/RECORDS.md", "records/HUMAN_INPUTS.md"]
    if (root / "evidence").is_dir():
        # research template
        common += ["evidence/RECORDS.md"]
    return common


# --- checks ------------------------------------------------------------------


def resolve_link(root: Path, source: Path, target: str) -> tuple[bool, str]:
    """Resolve a relative Markdown link (possibly with an #anchor)."""
    raw = target.strip()
    if raw.startswith(("http://", "https://", "mailto:", "tel:")):
        return True, ""  # external, not our concern
    path_part, _, anchor = raw.partition("#")
    if path_part == "":
        # pure in-page anchor
        dest = source
    else:
        dest = (source.parent / path_part).resolve()
        if not dest.exists():
            return False, f"{source.name}: link target missing: {raw}"
    if anchor:
        if dest.suffix.lower() != ".md":
            return True, ""  # can't introspect non-markdown anchors
        try:
            anchors = anchors_of(dest.read_text(encoding="utf-8"))
        except OSError as exc:
            return False, f"{source.name}: cannot read {dest} for anchor: {exc}"
        if anchor.lower() not in anchors:
            return False, f"{source.name}: anchor not found: {raw}"
    return True, ""


def run(root: Path) -> None:
    files = core_files(root)

    # 1. core files exist and are non-empty
    for rel in files:
        p = root / rel
        check(p.is_file(), f"core file missing: {rel}")
        if p.is_file():
            check(p.stat().st_size > 0, f"core file empty: {rel}")

    # 2. no tracked path contains a space (portability)
    for p in root.rglob("*"):
        if ".git" in p.parts:
            continue
        if p.is_file():
            check(" " not in p.name, f"path contains a space: {p.relative_to(root)}")

    # 3. Markdown structure: fences, tables, links across every .md file
    md_files = [
        p
        for p in root.rglob("*.md")
        if ".git" not in p.parts
    ]
    check(len(md_files) >= len(files), "expected at least the core Markdown files")
    for p in sorted(md_files):
        text = p.read_text(encoding="utf-8")
        _, balanced = strip_code_fences(text)
        check(balanced, f"unbalanced code fence: {p.relative_to(root)}")
        check(tables_consistent(text), f"inconsistent table columns: {p.relative_to(root)}")
        for target in links_of(text):
            ok, msg = resolve_link(root, p, target)
            check(ok, msg or f"unresolved link in {p.relative_to(root)}")

    # 4. checkpoint/report remain uninitialized (reusable, no stale claims)
    state = (root / "STATE.md").read_text(encoding="utf-8").lower()
    check("not started" in state or "not_started" in state,
          "STATE.md is not in the uninitialized 'not started' state")

    report = (root / "outputs" / "REPORT.md").read_text(encoding="utf-8").lower()
    check(
        "unfinished" in report or "not_started" in report or "not started" in report,
        "outputs/REPORT.md is not in its unfilled template state",
    )

    # 5. persistent-loop continuity fields are present in the checkpoint, so a
    #    successor always has somewhere to find in-flight work and dead ends.
    for field in (
        "loop continuity",
        "session owner",
        "in-flight action",
        "attempts on current",
        "ruled out / do not retry",
    ):
        check(field in state, f"STATE.md is missing the '{field}' field")

    # The template ships with no in-flight action outstanding.
    check(
        re.search(r"\*\*in-flight action:\*\*\s*none", state) is not None,
        "STATE.md must ship with an empty ('none') in-flight action",
    )

    agents = (root / "AGENTS.md").read_text(encoding="utf-8").lower()
    check(
        "persistent loop robustness" in agents,
        "AGENTS.md is missing the persistent loop robustness rules",
    )


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path(__file__).resolve().parent.parent
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 2
    run(root)
    total = _passed + len(_failures)
    if _failures:
        print(f"FAIL - {len(_failures)} of {total} structural checks failed:")
        for f in _failures:
            print(f"  - {f}")
        return 1
    print(f"PASS - {_passed} structural checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

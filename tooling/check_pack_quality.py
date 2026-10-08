#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
check_pack_quality.py: content-quality gate for a knowledge pack.

Usage:
    python tooling/check_pack_quality.py packs/<slug>
    python tooling/check_pack_quality.py --all

Checks (tags used in messages):
  [orphan-chapter]  every chapters/chNN-*.md file's basename must appear in
                    the pack's SKILL.md (disk-to-index; the reverse of
                    validate_pack's link check)
  [chapter-depth]   every chapters/chNN-*.md file must be at least
                    MIN_CHAPTER_LINES lines (truncation/stub gate, not a
                    quality judgment)
  [topic-index]     every chNN token inside the SKILL.md '## Topic Index'
                    section must resolve to an existing chapters/chNN-*.md
                    file; en-dash (U+2013) ranges expand to every covered
                    chapter; chNN tokens outside the section are prose and
                    are ignored

Content packs only: SKILL.md frontmatter matching kind: signpost or
kind: orchestrator skips all three checks, same classification as
validate_pack.py and check_release.py. A missing SKILL.md appends one
fail-closed [orphan-chapter] message, skips the orphan and topic scans,
and still runs the depth scan. A content pack with no ## Topic Index
section fails [topic-index] (all shipped content packs carry one).

No third-party dependencies. Exit code 0 = all checked packs pass;
1 = at least one failure.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

MIN_CHAPTER_LINES = 30


def check_pack(pack_dir: Path) -> list[str]:
    """Return a list of error strings; empty list means the pack passed."""
    errors: list[str] = []
    slug = pack_dir.name
    skill = pack_dir / "SKILL.md"

    # Kind detection: same two regexes as validate_pack.py / check_release.py
    # so all three tools classify a pack identically, case-insensitive.
    body = ""
    have_skill = skill.is_file()
    if have_skill:
        try:
            body = skill.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            have_skill = False
    if have_skill and (
        re.search(r"^kind:\s*signpost\s*$", body, re.I | re.M)
        or re.search(r"^kind:\s*orchestrator\s*$", body, re.I | re.M)
    ):
        return []
    if not have_skill:
        errors.append(
            f"[orphan-chapter] {slug}/SKILL.md missing or unreadable "
            "(fail-closed); orphan and topic checks skipped"
        )

    chapters = sorted((pack_dir / "chapters").glob("ch[0-9][0-9]-*.md"))
    disk_tokens = {p.name[:4] for p in chapters}

    # --- orphan scan: every chapter on disk is named in SKILL.md ---
    if have_skill:
        for p in chapters:
            if p.name not in body:
                errors.append(
                    f"[orphan-chapter] chapters/{p.name} on disk but not referenced in SKILL.md"
                )

    # --- depth scan: no chapter below the truncation floor ---
    for p in chapters:
        n = len(p.read_text(encoding="utf-8", errors="ignore").splitlines())
        if n < MIN_CHAPTER_LINES:
            errors.append(
                f"[chapter-depth] chapters/{p.name} has {n} lines, floor is {MIN_CHAPTER_LINES}"
            )

    # --- topic scan: every Topic Index token resolves to a chapter ---
    if have_skill:
        m = re.search(r"^##[ \t]*Topic Index[ \t]*$(.*?)(?=^##[ \t]|\Z)", body, re.M | re.S)
        if m is None:
            errors.append(f"[topic-index] {slug} has no Topic Index section")
        else:
            section = m.group(1)
            tokens: set[str] = set()

            def _expand(mt: re.Match[str]) -> str:
                lo, hi = int(mt.group(1)), int(mt.group(2))
                tokens.update(f"ch{n:02d}" for n in range(min(lo, hi), max(lo, hi) + 1))
                return " "

            # Consume en-dash ranges first: expand min..max, drop the match.
            section = re.sub(r"ch(\d{2})[ \t]*\u2013[ \t]*ch(\d{2})", _expand, section)
            tokens.update(re.findall(r"ch\d{2}", section))
            for tok in sorted(tokens):
                if tok not in disk_tokens:
                    errors.append(
                        f"[topic-index] Topic Index token {tok} resolves to no chapter in {slug}"
                    )

    return errors


def main(argv: list[str]) -> int:
    args = argv[1:]
    repo_root = Path(__file__).resolve().parent.parent
    if "--all" in args or not args:
        packs = sorted(p for p in (repo_root / "packs").iterdir() if p.is_dir())
    else:
        packs = [Path(a).resolve() for a in args]

    if not packs:
        print("No packs found to validate.")
        return 0

    total_fail = 0
    for pack in packs:
        errs = check_pack(pack)
        if errs:
            total_fail += 1
            print(f"FAIL  {pack.name}")
            for e in errs:
                print(f"        - {e}")
        else:
            print(f"PASS  {pack.name}")

    print(f"\n{len(packs) - total_fail}/{len(packs)} pack(s) passed.")
    return 1 if total_fail else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
check_overlap.py — multi-pack chapter-basename collision gate.

Detects chapter filenames that appear under more than one pack. Stdlib only.
Invoked by check_release.py (local/trusted; CI does not exec repo Python).

Scan scope: packs/*/chapters/*.md basenames only. Pack-root support files
(glossary.md, patterns.md, cheatsheet.md, SKILL.md, PACK.yaml) sit outside
chapters/ and are therefore excluded by design.

Threshold: any un-whitelisted chapter basename shared by two or more packs
fails the gate (exit 1). Whitelisted collisions are intentional and pass.

Whitelist: loaded from the shared data file tooling/overlap-whitelist.txt
(the same file the CI overlap step reads), fail-closed: an unreadable,
malformed, or empty data file fails the gate. The rationale for each entry
lives as a comment in the data file.

Usage:  python tooling/check_overlap.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Intentional cross-pack canonical chapter basenames (not collisions to block)
# live in this data file, shared with the CI overlap step. Kept as data, not a
# literal here, so the two gates cannot drift; loaded fail-closed.
OVERLAP_DATA = "tooling/overlap-whitelist.txt"
_TOKEN = re.compile(r"^[A-Za-z0-9.-]+$")


class OverlapDataError(Exception):
    """The whitelist data file is missing, empty, or malformed (fail closed)."""


def load_whitelist() -> set[str]:
    """Load whitelisted chapter basenames from OVERLAP_DATA, de-duplicated.

    Skips blank lines and '#' comments. Any other malformed line, an unreadable
    file, or zero tokens raises OverlapDataError so the gate fails closed
    instead of silently unblocking collisions. Mirrors
    check_release.load_banned_hosts (the link-policy-hosts.txt reader).
    """
    try:
        lines = (ROOT / OVERLAP_DATA).read_text(encoding="utf-8").splitlines()
    except OSError as e:
        raise OverlapDataError(f"cannot read {OVERLAP_DATA}: {e}") from e
    tokens: set[str] = set()
    for lineno, raw in enumerate(lines, 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if not _TOKEN.fullmatch(line):
            raise OverlapDataError(
                f"malformed line in {OVERLAP_DATA} (line {lineno}): {raw!r}"
            )
        tokens.add(line)
    if not tokens:
        raise OverlapDataError(f"whitelist empty ({OVERLAP_DATA} has no tokens)")
    return tokens


def fail(errs: list[str], msg: str) -> None:
    errs.append(msg)


def main() -> int:
    errs: list[str] = []
    chaps: dict[str, list[str]] = {}

    packs_root = ROOT / "packs"
    if packs_root.is_dir():
        for p in sorted(packs_root.glob("*/chapters/*.md")):
            slug = p.parent.parent.name
            chaps.setdefault(p.name, []).append(slug)

    try:
        whitelist = load_whitelist()
    except OverlapDataError as e:
        print("OVERLAP: FAIL (whitelist data file)")
        print(f"  {e}")
        return 1

    collisions = {name: packs for name, packs in chaps.items() if len(packs) > 1}
    bad = {name: packs for name, packs in collisions.items() if name not in whitelist}

    if bad:
        print(f"OVERLAP: FAIL ({len(bad)} issue(s))")
        for name in sorted(bad):
            packs = sorted(bad[name])
            fail(errs, f"{name}: {', '.join(packs)}")
            print(f"  {name}: {', '.join(packs)}")
        return 1

    print("OVERLAP: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

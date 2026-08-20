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

WHITELIST currently contains:
  - ch01-introduction.md — three distinct source packs (dau-se-guidebook,
    nasa-npr-7123, nasa-system-safety) legitimately share that canonical
    intro topic; different sources, same chapter name.

Usage:  python tooling/check_overlap.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Intentional cross-pack canonical chapter basenames (not collisions to block).
WHITELIST: set[str] = {
    "ch01-introduction.md",
}


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

    collisions = {name: packs for name, packs in chaps.items() if len(packs) > 1}
    bad = {name: packs for name, packs in collisions.items() if name not in WHITELIST}

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

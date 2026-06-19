#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
install.py — install the jgs-se-knowledge-packs catalogue into a Claude Code skills dir.

Each pack under packs/<slug>/ is an Agent Skill (a SKILL.md plus supporting files). This
installer copies the packs into your skills directory so they load as `/slug`.

Usage:
    python install.py --dry-run        # preview packs + target, copy nothing
    python install.py                  # install to ~/.claude/skills/jgs-se-knowledge-packs/
    python install.py --flat           # install each pack directly under ~/.claude/skills/
    python install.py --target DIR     # override the skills directory

Target resolution:
    skills dir = $CLAUDE_CONFIG_DIR/skills  (if CLAUDE_CONFIG_DIR set)
               = ~/.claude/skills           (otherwise)
    default layout = <skills>/jgs-se-knowledge-packs/<slug>   (vendor-namespaced)
    --flat layout  = <skills>/<slug>

No third-party dependencies — stdlib only.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

VENDOR = "jgs-se-knowledge-packs"
REPO_ROOT = Path(__file__).resolve().parent
PACKS_DIR = REPO_ROOT / "packs"


def discover_packs() -> list[Path]:
    """Every packs/<slug>/ that contains a SKILL.md is an installable pack."""
    if not PACKS_DIR.is_dir():
        return []
    return sorted(p for p in PACKS_DIR.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())


def resolve_skills_dir(override: str | None) -> Path:
    if override:
        return Path(override).expanduser().resolve()
    base = os.environ.get("CLAUDE_CONFIG_DIR")
    root = Path(base).expanduser() if base else Path.home() / ".claude"
    return (root / "skills").resolve()


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Install jgs-se-knowledge-packs into a skills directory.")
    ap.add_argument("--dry-run", action="store_true", help="show what would be installed, copy nothing")
    ap.add_argument("--flat", action="store_true", help="install packs directly under <skills>/ (no vendor namespace)")
    ap.add_argument("--target", help="override the skills directory")
    args = ap.parse_args(argv[1:])

    packs = discover_packs()
    if not packs:
        print("No packs found under packs/.", file=sys.stderr)
        return 1

    skills_dir = resolve_skills_dir(args.target)
    base = skills_dir if args.flat else skills_dir / VENDOR

    print(f"jgs-se-knowledge-packs installer")
    print(f"  packs found : {len(packs)}  ({', '.join(p.name for p in packs)})")
    print(f"  target      : {base}{'  (flat)' if args.flat else ''}")
    print()

    if args.dry_run:
        for p in packs:
            print(f"  would install  {p.name:<22} -> {base / p.name}")
        print("\nDry run — nothing copied. Re-run without --dry-run to install.")
        return 0

    base.mkdir(parents=True, exist_ok=True)
    for p in packs:
        dest = base / p.name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(p, dest)
        print(f"  installed  {p.name:<22} -> {dest}")

    print(f"\nInstalled {len(packs)} pack(s). Restart your agent, then try a pack by its slug, e.g. /{packs[0].name}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

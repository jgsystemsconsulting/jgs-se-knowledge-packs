#!/usr/bin/env python3
"""
validate_pack.py — structural + licence validator for a knowledge pack.

Usage:
    python tooling/validate_pack.py packs/<slug>
    python tooling/validate_pack.py --all          # validate every pack under packs/

Checks (see docs/PACK-SPEC.md and docs/SOURCE-VETTING.md):
  - required files present: SKILL.md, PACK.yaml, LICENSE, chapters/ with >=1 chapter
  - SKILL.md has YAML frontmatter with name + description; name matches folder slug
  - every chapters/chNN-*.md link in SKILL.md resolves to a real file
  - PACK.yaml has the mandatory fields filled
  - license_tier is 1, 2, or 3  (never the Excluded tier)

No third-party dependencies — uses a tiny YAML subset parser so CI needs only stdlib.
Exit code 0 = all checked packs pass; 1 = at least one failure.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_PACK_FIELDS = ("slug", "title", "license", "license_tier", "source_url", "commercial_use")
VALID_TIERS = {"1", "2", "3"}


def parse_simple_yaml(text: str) -> dict:
    """Parse the flat top-level scalar keys we require from PACK.yaml.

    Deliberately minimal: reads `key: value` pairs at column 0, strips quotes,
    and ignores nested blocks (e.g. `build:`) and folded scalars (`>`). That is
    enough to validate the mandatory fields without a PyYAML dependency.
    """
    out: dict[str, str] = {}
    for line in text.splitlines():
        if not line or line[0] in " \t#":
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val in (">", "|", ""):  # block scalar or nested mapping header — skip value
            continue
        out[key] = val.strip().strip('"').strip("'")
    return out


def check_pack(pack_dir: Path) -> list[str]:
    """Return a list of error strings; empty list means the pack passed."""
    errors: list[str] = []
    slug = pack_dir.name

    # --- required files ---
    skill = pack_dir / "SKILL.md"
    pack_yaml = pack_dir / "PACK.yaml"
    lic = pack_dir / "LICENSE"
    chapters = pack_dir / "chapters"

    if not skill.is_file():
        errors.append("missing SKILL.md")
    if not pack_yaml.is_file():
        errors.append("missing PACK.yaml")
    if not lic.is_file():
        errors.append("missing LICENSE (must reproduce the source's terms)")
    if not chapters.is_dir():
        errors.append("missing chapters/ directory")
    else:
        ch_files = sorted(chapters.glob("ch*.md"))
        if not ch_files:
            errors.append("chapters/ contains no chNN-*.md files")

    # --- SKILL.md frontmatter + chapter links ---
    if skill.is_file():
        body = skill.read_text(encoding="utf-8")
        fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", body, re.S)
        if not fm:
            errors.append("SKILL.md has no YAML frontmatter block")
        else:
            front = fm.group(1)
            name_m = re.search(r"^name:\s*(.+)$", front, re.M)
            if not name_m:
                errors.append("SKILL.md frontmatter missing 'name'")
            elif name_m.group(1).strip().strip('"').strip("'") != slug:
                errors.append(f"SKILL.md name '{name_m.group(1).strip()}' != folder slug '{slug}'")
            if not re.search(r"^description:\s*\S", front, re.M):
                errors.append("SKILL.md frontmatter missing 'description'")
        # every referenced chapter file must exist
        for link in re.findall(r"\((chapters/ch[0-9]{2}-[^)]+\.md)\)", body):
            if not (pack_dir / link).is_file():
                errors.append(f"SKILL.md links a missing chapter file: {link}")

    # --- PACK.yaml mandatory fields + tier ---
    if pack_yaml.is_file():
        meta = parse_simple_yaml(pack_yaml.read_text(encoding="utf-8"))
        for field in REQUIRED_PACK_FIELDS:
            if not meta.get(field):
                errors.append(f"PACK.yaml missing required field: {field}")
        tier = meta.get("license_tier", "")
        if tier and tier not in VALID_TIERS:
            errors.append(
                f"PACK.yaml license_tier='{tier}' invalid — must be 1, 2, or 3 "
                "(Excluded sources are never packageable; see docs/SOURCE-VETTING.md)"
            )
        if meta.get("slug") and meta["slug"] != slug:
            errors.append(f"PACK.yaml slug '{meta['slug']}' != folder name '{slug}'")

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

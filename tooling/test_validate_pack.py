#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based checks for validate_pack.check_pack signpost parity (no framework).

Run:  python tooling/test_validate_pack.py
Exits 0 when content-pack and signpost-pack shapes classify as PACK-SPEC expects.
Any failed assert raises and exits nonzero. Fixtures are built in a temp dir;
the live tree is only read (case 7), never mutated.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_pack  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent

CONTENT_SKILL = """---
name: {slug}
description: "Demo content pack used by the validator probe."
---
"""

SIGNPOST_SKILL = """---
name: {slug}
kind: signpost
description: "Demo signpost used by the validator probe."
---
"""

SIGNPOST_NO_DESC = """---
name: {slug}
kind: signpost
---
"""

PACK_YAML = """slug: {slug}
title: "Demo Pack"
publisher: "JG Systems Consulting Ltd."
license: "MIT"
license_tier: 2
commercial_use: true
"""


def build_pack(root: Path, slug: str, *, skill: str | None, pack_yaml: bool = True,
               license_: bool = True, chapters: bool = True) -> Path:
    d = root / slug
    d.mkdir()
    if skill is not None:
        (d / "SKILL.md").write_text(skill.format(slug=slug), encoding="utf-8")
    if pack_yaml:
        (d / "PACK.yaml").write_text(PACK_YAML.format(slug=slug), encoding="utf-8")
    if license_:
        (d / "LICENSE").write_text("MIT", encoding="utf-8")
    if chapters:
        (d / "chapters").mkdir()
        (d / "chapters" / "ch01-intro.md").write_text("# Intro\n", encoding="utf-8")
    return d


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        # (1) full content-pack shape passes
        full = build_pack(root, "full-pack", skill=CONTENT_SKILL)
        assert validate_pack.check_pack(full) == [], validate_pack.check_pack(full)

        # (2) content pack minus LICENSE fails with the LICENSE error
        no_lic = build_pack(root, "no-license", skill=CONTENT_SKILL, license_=False)
        errs = validate_pack.check_pack(no_lic)
        assert errs == ["missing LICENSE (must reproduce the source's terms)"], errs

        # (3) content pack minus chapters/ fails with the chapters error
        no_ch = build_pack(root, "no-chapters", skill=CONTENT_SKILL, chapters=False)
        errs = validate_pack.check_pack(no_ch)
        assert errs == ["missing chapters/ directory"], errs

        # (4) signpost shape (SKILL.md + PACK.yaml only) passes
        sign = build_pack(root, "demo-signpost", skill=SIGNPOST_SKILL,
                          license_=False, chapters=False)
        assert validate_pack.check_pack(sign) == [], validate_pack.check_pack(sign)

        # (5) signpost missing SKILL.md fails: kind cannot be proven
        bare = build_pack(root, "bare-signpost", skill=None,
                          license_=False, chapters=False)
        errs = validate_pack.check_pack(bare)
        assert errs == ["missing SKILL.md",
                        "missing LICENSE (must reproduce the source's terms)",
                        "missing chapters/ directory"], errs

        # (6a) signpost missing PACK.yaml still fails
        no_meta = build_pack(root, "no-meta-signpost", skill=SIGNPOST_SKILL,
                             pack_yaml=False, license_=False, chapters=False)
        errs = validate_pack.check_pack(no_meta)
        assert errs == ["missing PACK.yaml"], errs

        # (6b) signpost frontmatter missing description still fails
        no_desc = build_pack(root, "no-desc-signpost", skill=SIGNPOST_NO_DESC,
                             license_=False, chapters=False)
        errs = validate_pack.check_pack(no_desc)
        assert errs == ["SKILL.md frontmatter missing 'description'"], errs

    # (7) both live signpost packs pass on the real tree (read-only)
    for slug in ("omg-signpost", "se-standards-signpost"):
        live = REPO_ROOT / "packs" / slug
        assert live.is_dir(), f"live signpost pack missing: {live}"
        assert validate_pack.check_pack(live) == [], slug

    print("validate_pack tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

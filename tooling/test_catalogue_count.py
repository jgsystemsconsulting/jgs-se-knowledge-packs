#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based probe for landing catalogue-count parsers (P15; no framework).

Run:  python tooling/test_catalogue_count.py
Exits 0 when h2 extraction, chip summing, signpost-chip exclusion, SVG N/M
parse, frontmatter signpost detection, and the real-tree check all hold.
Any failed assert raises and exits nonzero.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_release  # noqa: E402


SECTION = """<!-- §06 The catalogue -->
<section><div class="wrap">
  <div class="sec-head"><span class="label">§06 · The catalogue</span>
    <h2>3 packs &middot; 1 signposts</h2></div>
  <div class="packs">
    <div class="pk"><b>NASA &middot; 2</b><span>includes 99 noise digits</span></div>
    <div class="pk"><b>OMB / cross-federal &middot; 1</b><span>federal-bca</span></div>
    <div class="pk"><b>Signposts &middot; 1</b><span>download pointers</span></div>
  </div>
  <figcaption>FIG.06 · 3 packs plus 1 signposts across open sources; filter the full list on packs.html.</figcaption>
</div></section>
<!-- §07 Licensing -->
"""

SECTION_DOT = SECTION.replace("&middot;", "·")

SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675">
  <text x="64" y="188">3 packs  ·  1 signposts  ·  open sources only</text>
  <text x="80" y="250">NASA</text>
  <text x="400" y="250">02</text>
  <text x="56" y="640">3 PACKS · 1 SIGNPOSTS · FILTER ON packs.html</text>
</svg>
"""


def main() -> int:
    # frontmatter signpost detection via inventory
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        packs = root / "packs"
        (packs / "alpha").mkdir(parents=True)
        (packs / "beta").mkdir()
        (packs / "omega-sign").mkdir()
        (packs / "alpha" / "SKILL.md").write_text(
            "---\nname: alpha\ndescription: a\n---\n# a\n", encoding="utf-8"
        )
        (packs / "beta" / "SKILL.md").write_text(
            "---\nname: beta\ndescription: b\n---\n# b\n", encoding="utf-8"
        )
        (packs / "omega-sign" / "SKILL.md").write_text(
            "---\nname: omega-sign\nkind: signpost\ndescription: s\n---\n# s\n",
            encoding="utf-8",
        )
        n, m, errs = check_release.inventory_pack_counts(packs)
        assert errs == [], errs
        assert (n, m) == (2, 1), (n, m)

        (packs / "omega-orch").mkdir()
        (packs / "omega-orch" / "SKILL.md").write_text(
            "---\nname: omega-orch\nkind: orchestrator\ndescription: o\n---\n# o\n",
            encoding="utf-8",
        )
        n, m, errs = check_release.inventory_pack_counts(packs)
        assert errs == [], errs
        assert (n, m) == (2, 1), (n, m)  # orchestrator in neither bucket

        # missing SKILL.md fails closed
        (packs / "ghost").mkdir()
        n2, m2, errs2 = check_release.inventory_pack_counts(packs)
        assert any("missing SKILL.md" in e for e in errs2), errs2
        assert n2 == 2 and m2 == 1

    # h2 entity-aware
    sec = check_release.slice_catalogue_section(SECTION)
    assert sec is not None and "§07" not in sec
    assert check_release.parse_catalogue_h2(sec) == (3, 1)
    sec_dot = check_release.slice_catalogue_section(SECTION_DOT)
    assert check_release.parse_catalogue_h2(sec_dot) == (3, 1)

    # chip sum ignores span digits; signpost chip excluded from content sum
    content_sum, sp_count, sp_n, chip_errs = check_release.parse_catalogue_chips(sec)
    assert chip_errs == [], chip_errs
    assert content_sum == 3, content_sum
    assert sp_count == 1 and sp_n == 1

    # SVG subtitle + footer
    sub, foot = check_release.parse_svg_catalogue_nm(SVG)
    assert sub == (3, 1), sub
    assert foot == (3, 1), foot

    # end-to-end helper: matching fixture passes; stale h2 fails with live vs stated
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        packs = root / "packs"
        (packs / "a").mkdir(parents=True)
        (packs / "b").mkdir()
        (packs / "c").mkdir()
        (packs / "s").mkdir()
        for name in ("a", "b", "c"):
            (packs / name / "SKILL.md").write_text(
                f"---\nname: {name}\ndescription: x\n---\n# {name}\n",
                encoding="utf-8",
            )
        (packs / "s" / "SKILL.md").write_text(
            "---\nname: s\nkind: signpost\ndescription: s\n---\n# s\n",
            encoding="utf-8",
        )
        good = check_release.check_catalogue_count(packs, SECTION, SVG)
        assert good == [], good

        stale = SECTION.replace("3 packs &middot; 1 signposts", "62 packs &middot; 1 signposts")
        bad = check_release.check_catalogue_count(packs, stale, SVG)
        assert any(
            "[catalogue-count]" in e
            and "62 packs" in e
            and "live inventory is 3 packs" in e
            for e in bad
        ), bad

    # real tree: live inventory matches landing after P15 fix
    real = check_release.check_catalogue_count(
        ROOT / "packs",
        (ROOT / "docs" / "index.html").read_text(encoding="utf-8"),
        (ROOT / "docs" / "assets" / "still-catalogue.svg").read_text(encoding="utf-8"),
    )
    assert real == [], real

    print("catalogue-count probe: OK (parsers, fixtures, real tree)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

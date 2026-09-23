#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based probe for catalog live-set parity (P16; no framework).

Run:  python tooling/test_catalog_live_set.py
Exits 0 when inventory slugs, matching fixtures, signpost exclusion, mismatch
messages, and the real-tree check all hold. Any failed assert raises and exits
nonzero.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_release  # noqa: E402


def _write_skill(
    path: Path, name: str, *, signpost: bool = False, orchestrator: bool = False
) -> None:
    if signpost:
        kind = "kind: signpost\n"
    elif orchestrator:
        kind = "kind: orchestrator\n"
    else:
        kind = ""
    path.write_text(
        f"---\nname: {name}\n{kind}description: x\n---\n# {name}\n",
        encoding="utf-8",
    )


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        packs = root / "packs"
        (packs / "alpha").mkdir(parents=True)
        (packs / "beta").mkdir()
        (packs / "omega-sign").mkdir()
        _write_skill(packs / "alpha" / "SKILL.md", "alpha")
        _write_skill(packs / "beta" / "SKILL.md", "beta")
        _write_skill(packs / "omega-sign" / "SKILL.md", "omega-sign", signpost=True)

        content, signs, orchs, errs = check_release.inventory_pack_slugs(
            packs, tag="[catalog-live-set]"
        )
        assert errs == [], errs
        assert content == {"alpha", "beta"}, content
        assert signs == {"omega-sign"}, signs
        assert orchs == set(), orchs

        good_catalog = {
            "updated": "2026-08-27",
            "packs": [
                {"slug": "alpha", "status": "live"},
                {"slug": "beta", "status": "live"},
            ],
            "planned": [{"slug": "future", "status": "planned"}],
        }
        assert check_release.check_catalog_live_set(packs, good_catalog) == []

        # status absent counts as live
        no_status = {
            "packs": [{"slug": "alpha"}, {"slug": "beta"}],
        }
        assert check_release.check_catalog_live_set(packs, no_status) == []

        # phantom catalog slug fails with only-in-catalog
        stale = {
            "packs": [
                {"slug": "alpha", "status": "live"},
                {"slug": "beta", "status": "live"},
                {"slug": "phantom", "status": "live"},
            ],
        }
        bad = check_release.check_catalog_live_set(packs, stale)
        assert any(
            "[catalog-live-set]" in e
            and "live slug set mismatch" in e
            and "phantom" in e
            for e in bad
        ), bad

        # missing content pack fails only-in-packs
        missing = {
            "packs": [{"slug": "alpha", "status": "live"}],
        }
        bad2 = check_release.check_catalog_live_set(packs, missing)
        assert any(
            "[catalog-live-set]" in e and "beta" in e and "only in packs/" in e
            for e in bad2
        ), bad2

        # signpost in catalog fails
        with_sign = {
            "packs": [
                {"slug": "alpha", "status": "live"},
                {"slug": "beta", "status": "live"},
                {"slug": "omega-sign", "status": "live"},
            ],
        }
        bad3 = check_release.check_catalog_live_set(packs, with_sign)
        assert any(
            "[catalog-live-set]" in e
            and "signpost" in e.lower()
            and "omega-sign" in e
            for e in bad3
        ), bad3

        (packs / "omega-orch").mkdir()
        _write_skill(packs / "omega-orch" / "SKILL.md", "omega-orch", orchestrator=True)
        # still clean: orchestrator absent from catalog like a signpost
        assert check_release.check_catalog_live_set(packs, good_catalog) == []
        # catalog listing an orchestrator fails like a signpost
        bad_orch = dict(
            good_catalog,
            packs=good_catalog["packs"] + [{"slug": "omega-orch", "status": "live"}],
        )
        errs = check_release.check_catalog_live_set(packs, bad_orch)
        assert any(
            "[catalog-live-set]" in e and "omega-orch" in e for e in errs
        ), errs

        # ghost dir without SKILL.md fails closed
        (packs / "ghost").mkdir()
        bad4 = check_release.check_catalog_live_set(packs, good_catalog)
        assert any("missing SKILL.md" in e and "ghost" in e for e in bad4), bad4

    # real tree
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    assert catalog.get("updated") == "2026-08-27", catalog.get("updated")
    real = check_release.check_catalog_live_set(ROOT / "packs", catalog)
    assert real == [], real

    print("catalog-live-set probe: OK (inventory, fixtures, real tree)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

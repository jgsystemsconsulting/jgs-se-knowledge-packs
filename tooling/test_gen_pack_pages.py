#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based probe for gen_pack_pages post-P51 contracts (P52; no framework).

Run:  python tooling/test_gen_pack_pages.py
Exits 0 when the title join, the sitemap writer, pack-page REV, and the
html-assets membership set all hold. Any failed assert raises and exits
nonzero.

Local pre-tag story: run this probe before tagging, next to the other
tooling/test_*.py probes. Generators stay out of CI. This file does not
add a validate.yml step and does not pin tooling/test_ci_gate.py.
"""
from __future__ import annotations

import json
import re
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_release  # noqa: E402
import gen_pack_pages  # noqa: E402

TITLE_JOIN = (
    "{title} as an installable skill for AI coding agents | JGS SE Knowledge Packs"
)
OLD_TITLE = "{title}: installable skill"
OLD_RENDERED = "Foo: Bar: installable"
LIVE_JOIN = "Foo: Bar as an installable skill for AI coding agents"
GLOB_DOCS = 'docs.glob("*.html")'
GLOB_PACKS = 'docs.glob("packs/*/index.html")'
PLANT = ROOT / "docs" / "superpowers" / "gen_pack_pages_probe.html"


def _pack(slug: str, title: str) -> dict:
    return {
        "slug": slug,
        "name": slug,
        "title": title,
        "desc": "plain desc",
        "chapters": [],
    }


def _cat() -> dict:
    return {
        "license": "MIT",
        "license_tier": "permissive",
        "commercial_use": True,
        "source_version": "1",
        "publisher": "probe",
    }


def _title_text(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html)
    assert m, "render produced no title"
    return m.group(1)


def case_source_pins(src: str, gate: str) -> None:
    # write_sitemap takes no slug list. Signature is the def line, not a call.
    assert "def write_sitemap() -> int:" in src
    assert "def write_sitemap(slugs" not in src
    # main always writes the sitemap, and the call carries no run list.
    assert "write_sitemap()" in src
    assert "live = write_sitemap()" in src
    # only-flag token stays inside the help string, and the help still says
    # the sitemap is always rewritten from the full live catalog.
    assert '"--only"' in src
    # help must carry the decoupling promise; the docstring may echo it, so pin
    # the help-specific span: the phrase appears inside help="..." assignment.
    help_hits = src.count("limits which pack pages this run rewrites")
    assert help_hits >= 2  # docstring + help literal
    assert 'help="comma-separated slugs; limits which pack pages this run rewrites"' in src
    assert "docs/sitemap.xml is always rewritten from the full live catalog" in src
    # current title join, not the doubled-colon form that commit 20ba23a fixed.
    assert "<title>" + TITLE_JOIN + "</title>" in src
    assert OLD_TITLE not in src
    # check 12 glob literals still live in the gate, so the scan set and the
    # generator dest cannot drift apart unnoticed.
    assert GLOB_DOCS in gate
    assert GLOB_PACKS in gate
    assert "PACK_REV_MASTHEAD_RE" in gate
    assert "PACK_REV_FOOTER_RE" in gate


def case_title_join() -> None:
    slug = "probe-slug"
    html = gen_pack_pages.render(_pack(slug, "Foo: Bar"), _cat(), "1.2.3")
    title = _title_text(html)
    assert LIVE_JOIN in title
    assert title.count("Foo: Bar") == 1
    assert OLD_RENDERED not in title
    assert ": installable skill" not in title
    # output id is the catalog slug, not a slugified title.
    canon = f"{gen_pack_pages.PAGES}/packs/{slug}/"
    assert f'href="{canon}"' in html
    other = gen_pack_pages.render(_pack(slug, "Other: Title"), _cat(), "1.2.3")
    assert f'href="{canon}"' in other


def case_sitemap_ignores_run_list() -> None:
    saved = gen_pack_pages.ROOT
    try:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "docs").mkdir()
            catalog = {
                "packs": [
                    {"slug": "zeta", "status": "live"},
                    {"slug": "alpha"},
                    {"slug": "drafted", "status": "draft"},
                ]
            }
            (root / "catalog.json").write_text(
                json.dumps(catalog), encoding="utf-8"
            )
            gen_pack_pages.ROOT = root
            n = gen_pack_pages.write_sitemap()
            assert n == 2
            text = (root / "docs" / "sitemap.xml").read_text(encoding="utf-8")
            locs = [
                el.text.strip()
                for el in ET.fromstring(text).iter(check_release.SITEMAP_NS + "loc")
                if el.text and el.text.strip()
            ]
            pages = gen_pack_pages.PAGES
            expected = sorted([
                f"{pages}/",
                f"{pages}/packs.html",
                f"{pages}/packs/alpha/",
                f"{pages}/packs/zeta/",
            ])
            assert locs == expected
            assert f"{pages}/packs/drafted/" not in locs
    finally:
        gen_pack_pages.ROOT = saved


def case_real_sitemap() -> int:
    errs = check_release.check_sitemap(ROOT)
    assert errs == [], errs
    live = gen_pack_pages.live_catalog_slugs(gen_pack_pages.catalog_packs())
    text = (ROOT / "docs" / "sitemap.xml").read_text(encoding="utf-8")
    locs = [
        el.text.strip()
        for el in ET.fromstring(text).iter(check_release.SITEMAP_NS + "loc")
        if el.text and el.text.strip()
    ]
    assert len(locs) == 2 + len(live)
    return len(locs)


def case_real_rev() -> None:
    errs = check_release.check_pack_rev(ROOT)
    assert errs == [], errs
    live = gen_pack_pages.live_catalog_slugs(gen_pack_pages.catalog_packs())
    assert live, "catalog has no live slug"
    slug = sorted(live)[0]
    ver = gen_pack_pages.version()
    html = gen_pack_pages.render(_pack(slug, "Probe Title"), _cat(), ver)
    mast = check_release.PACK_REV_MASTHEAD_RE.search(html)
    foot = check_release.PACK_REV_FOOTER_RE.search(html)
    assert mast and mast.group(1) == ver
    assert foot and foot.group(1) == ver


def case_html_assets() -> int:
    docs = ROOT / "docs"
    pages = sorted(
        list(docs.glob("*.html")) + list(docs.glob("packs/*/index.html"))
    )
    assert pages, "html-assets set empty"
    pack_pages = list(docs.glob("packs/*/index.html"))
    assert pack_pages, "no pack pages"
    assert any(p.parent == docs for p in pages), "docs/*.html glob contributed nothing"
    for page in pack_pages:
        assert page in pages
    PLANT.parent.mkdir(parents=True, exist_ok=True)
    try:
        PLANT.write_text("<html></html>\n", encoding="utf-8")
        again = sorted(
            list(docs.glob("*.html")) + list(docs.glob("packs/*/index.html"))
        )
        assert PLANT not in again
        assert PLANT.is_file()
    finally:
        PLANT.unlink(missing_ok=True)
    assert not PLANT.exists()
    return len(pack_pages)


def main() -> int:
    src = (ROOT / "tooling" / "gen_pack_pages.py").read_text(encoding="utf-8")
    gate = (ROOT / "tooling" / "check_release.py").read_text(encoding="utf-8")
    case_source_pins(src, gate)
    case_title_join()
    case_sitemap_ignores_run_list()
    loc_n = case_real_sitemap()
    case_real_rev()
    page_n = case_html_assets()
    print(f"gen-pack-pages probe: OK ({page_n} pack pages, {loc_n} sitemap locs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

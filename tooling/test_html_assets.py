#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. - MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based probe for the [html-assets] self-containment scan (no framework).

Run:  python tooling/test_html_assets.py
Exits 0 when the scan flags every fixture class from the P12 spec, allows the
first-party/data/relative classes, and the real docs/*.html pages scan clean.
Any failed assert raises and exits nonzero.

Self-host convention (P12): images under docs/assets/, fonts under docs/fonts/,
relative references only. The scanner classifies URLs; it does not stat the
paths they reference.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_release  # noqa: E402

scan = check_release.scan_html_external_assets


def main() -> int:
    # (0) the allowlist is exactly the two first-party hosts
    assert check_release.FIRST_PARTY_HOSTS == {
        "github.com", "jgsystemsconsulting.github.io"
    }, check_release.FIRST_PARTY_HOSTS

    # (1) asset table: every element/attribute row flags a non-allowlisted host
    assert scan('<img src="https://cdn.example/p.png">') == ["https://cdn.example/p.png"]
    assert scan('<link rel="stylesheet" href="http://cdn.example/s.css">') == \
        ["http://cdn.example/s.css"]
    assert scan('<link rel="icon" href="https://cdn.example/f.ico">') == \
        ["https://cdn.example/f.ico"]
    assert scan('<script src="https://cdn.example/a.js"></script>') == \
        ["https://cdn.example/a.js"]
    assert scan('<iframe src="https://cdn.example/embed"></iframe>') == \
        ["https://cdn.example/embed"]
    assert scan('<object data="https://cdn.example/o.file"></object>') == \
        ["https://cdn.example/o.file"]
    # srcset: comma-split, first whitespace token per group is the URL
    assert scan('<img srcset="a.png 1x, https://cdn.example/b.png 2x, c.png 3x">') == \
        ["https://cdn.example/b.png"]

    # og:image / twitter:image content, both attribute orders
    assert scan('<meta property="og:image" content="https://cdn.example/og.png">') == \
        ["https://cdn.example/og.png"]
    assert scan('<meta content="https://cdn.example/og.png" property="og:image">') == \
        ["https://cdn.example/og.png"]
    assert scan('<meta property="og:image:secure_url" content="https://cdn.example/og2.png">') == \
        ["https://cdn.example/og2.png"]
    assert scan('<meta name="twitter:image" content="https://cdn.example/tw.png">') == \
        ["https://cdn.example/tw.png"]
    assert scan('<meta content="https://cdn.example/tw.png" name="twitter:image">') == \
        ["https://cdn.example/tw.png"]
    assert scan('<meta name="twitter:image:src" content="https://cdn.example/tw2.png">') == \
        ["https://cdn.example/tw2.png"]
    # non-image meta content is never an asset
    assert scan('<meta property="og:url" content="https://cdn.example/page">') == []
    assert scan('<meta name="twitter:card" content="summary">') == []

    # meta refresh: url= case-insensitive, whitespace around =, quotes stripped
    assert scan('<meta http-equiv="refresh" content="0; url=https://cdn.example/next">') == \
        ["https://cdn.example/next"]
    assert scan('<meta http-equiv="Refresh" content="0; URL=https://cdn.example/next">') == \
        ["https://cdn.example/next"]
    assert scan("<meta http-equiv='refresh' content=\"0; url = 'https://cdn.example/next'\">") == \
        ["https://cdn.example/next"]
    assert scan('<meta http-equiv="refresh" content="10">') == []

    # inline CSS: url() and @import in double-quote, single-quote, and url() forms
    assert scan('<style>body{background:url(https://cdn.example/bg.png)}</style>') == \
        ["https://cdn.example/bg.png"]
    assert scan("<style>body{background:url('https://cdn.example/bg.png')}</style>") == \
        ["https://cdn.example/bg.png"]
    assert scan('<style>@import "https://cdn.example/a.css";</style>') == \
        ["https://cdn.example/a.css"]
    assert scan("<style>@import 'https://cdn.example/b.css';</style>") == \
        ["https://cdn.example/b.css"]
    assert scan('<style>@import url(https://cdn.example/c.css);</style>') == \
        ["https://cdn.example/c.css"]
    assert scan('<style>@import url("https://cdn.example/d.css");</style>') == \
        ["https://cdn.example/d.css"]

    # quote-aware slicing: a > inside a quoted value must not cut the tag
    assert scan('<img alt="a > b" src="https://cdn.example/x.png">') == \
        ["https://cdn.example/x.png"]
    # unquoted attribute value
    assert scan("<img src=https://cdn.example/x.png>") == ["https://cdn.example/x.png"]
    # distinctness: one finding per distinct URL
    assert scan('<img src="https://cdn.example/d.png"><img src="https://cdn.example/d.png">') == \
        ["https://cdn.example/d.png"]

    # (2) allowed classes
    # data: URIs, including the real favicon payload shape with an embedded
    # http://www.w3.org/2000/svg URL, must never fail
    assert scan(
        "<link rel=\"icon\" href=\"data:image/svg+xml,%3Csvg "
        "xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3C/svg%3E\">"
    ) == []
    # relative and root-relative paths, including the real font references
    assert scan('<img src="assets/og.png">') == []
    assert scan('<script src="./x.js"></script>') == []
    assert scan('<img src="/root-relative.png">') == []
    assert scan("<style>@font-face{src:url('fonts/Inter-Regular.woff2')}</style>") == []
    assert scan('<link rel="stylesheet" href="css/site.css">') == []
    # allowlisted hosts with empty userinfo, exact match
    assert scan('<img src="https://github.com/jgs/asset/blob/main/x.png">') == []
    assert scan(
        '<meta property="og:url" content="https://jgsystemsconsulting.github.io/jgs-se-knowledge-packs/">'
    ) == []
    assert scan('<meta http-equiv="refresh" content="0; url=https://github.com/x">') == []
    # empty and fragment-only values are skipped
    assert scan('<link rel="icon" href="">') == []
    assert scan('<link rel="icon" href="#frag">') == []
    assert scan('<a href="https://cdn.example/nav">link</a>') == []  # anchors excluded

    # (3) fail classes
    # userinfo tricks rejected even on an allowlisted host
    assert scan('<img src="https://user@github.com/x.png">') == ["https://user@github.com/x.png"]
    assert scan('<script src="https://user:pw@github.com/x.js"></script>') == \
        ["https://user:pw@github.com/x.js"]
    # subdomains are not allowlisted (exact match only)
    assert scan('<img src="https://www.github.com/x.png">') == ["https://www.github.com/x.png"]
    # protocol-relative always fails
    assert scan('<script src="//cdn.example/x.js"></script>') == ["//cdn.example/x.js"]

    # (4) the real pages must scan clean (P12 acceptance: zero findings)
    pages = sorted((ROOT / "docs").glob("*.html"))
    assert pages, "no docs/*.html found under docs/"
    for page in pages:
        leaks = scan(page.read_text(encoding="utf-8", errors="ignore"))
        assert leaks == [], f"{page.name}: unexpected external asset(s): {leaks}"

    print(f"html-assets tests: OK ({len(pages)} real page(s) clean)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

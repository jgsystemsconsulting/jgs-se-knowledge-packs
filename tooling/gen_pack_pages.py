#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
Generate per-pack landing pages, docs/packs/<slug>/index.html, plus docs/sitemap.xml.

Parses catalog.json, each pack's SKILL.md frontmatter (name, description), its H1 title,
and its chapters/ listing, then emits self-contained, design-system-compliant pages under
the JGS ink family: site.css chrome, brand tokens sliced from docs/index.html at render
time (P13), no third-party assets. Pages give every pack a search-engine entry point keyed
to its source document name. Run after adding packs; --only limits the run to a pilot set.
Em dashes are stripped from emitted copy (RR-B-28). Pair with gen_packs_page.py, which
links a slug to its local page whenever docs/packs/<slug>/index.html exists.
"""
import argparse
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_packs_page import PAGES, REPO, ROOT, brand_tokens, deslop, version  # noqa: E402


def catalog_packs() -> dict:
    data = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    return {p["slug"]: p for p in data["packs"]}


def read_pack(slug: str) -> dict:
    """Collect everything one page needs from the repo, never from memory."""
    pdir = ROOT / "packs" / slug
    skill = (pdir / "SKILL.md").read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
    block = fm.group(1) if fm else ""
    nm = re.search(r'^name:\s*(.+)$', block, re.M)
    dm = re.search(r'^description:\s*"(.*)"\s*$', block, re.M) or re.search(
        r'^description:\s*(.+)$', block, re.M)
    h1 = re.search(r"^# (.+)$", skill[fm.end():] if fm else skill, re.M)
    chapters = []
    cdir = pdir / "chapters"
    if cdir.is_dir():
        for f in sorted(cdir.glob("ch*.md")):
            stem = f.stem
            cm = re.match(r"^ch(\d+)-(.*)$", stem)
            num, rest = (cm.group(1), cm.group(2)) if cm else ("", stem)
            rest = rest.replace("-", " ")
            rest = re.sub(r"(\d) (\d)", r"\1.\2", rest)
            rest = rest[:1].upper() + rest[1:]
            chapters.append((num, rest, f.name))
    return {
        "slug": slug,
        "name": nm.group(1).strip() if nm else slug,
        "title": h1.group(1).strip() if h1 else slug,
        "desc": deslop(dm.group(1).strip()) if dm else "",
        "chapters": chapters,
    }


def md_inline(text: str) -> str:
    """Render the frontmatter description's **bold** and `code` like packs.html does."""
    out = html.escape(text)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    return out


def clip(text: str, limit: int = 155) -> str:
    plain = text.replace("**", "").replace("`", "")
    return plain if len(plain) <= limit else plain[: plain.rfind(" ", 0, limit)] + "..."


CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--ink);color:var(--mute-2);font-family:var(--sans);font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:1200px;margin:0 auto;padding-left:var(--pad-x);padding-right:var(--pad-x)}
a{color:var(--text-hi);text-decoration:none;border-bottom:1px solid var(--line-2)}
a:hover{border-bottom-color:var(--paper)}
a:focus-visible{outline:2px solid var(--paper);outline-offset:2px}
h1{font-family:var(--mono);color:var(--text-hi);letter-spacing:-0.02em;font-weight:700;margin:0;font-size:clamp(1.6rem,4vw,2.4rem)}
.label{font-family:var(--mono);text-transform:uppercase;letter-spacing:0.14em;font-size:0.6875rem;font-weight:700;color:var(--mute)}
header.hd{border-bottom:1px solid var(--line);padding-top:var(--pad-section);padding-bottom:2rem}
header.hd p{margin:1rem 0 0;max-width:70ch;color:var(--text)}
header.hd p code{font-family:var(--mono);font-size:0.85em}
.backnav{margin-top:1.4rem;display:flex;flex-wrap:wrap;gap:8px 18px;font-family:var(--mono);font-size:0.8rem}
section{padding-top:1.75rem;padding-bottom:var(--pad-section)}
.meta{display:flex;flex-wrap:wrap;gap:10px}
.mcell{border:1px solid var(--line);background:var(--ink-2);padding:10px 14px;font-family:var(--mono);font-size:0.8rem;color:var(--mute-2);min-width:9rem}
.mcell b{display:block;color:var(--text-hi);font-size:0.9rem;margin-top:2px;font-weight:700}
.install{background:var(--ink-2);border:1px solid var(--line);padding:14px 16px;overflow-x:auto}
.install pre{margin:0 0 10px;font-family:var(--mono);font-size:0.85rem;color:var(--text);white-space:pre-wrap;overflow-wrap:anywhere}
.install pre:last-child{margin-bottom:0}
.install .cm{color:var(--mute)}
table{width:100%;border-collapse:collapse;border:1px solid var(--line);background:var(--ink)}
thead th{font-family:var(--mono);text-transform:uppercase;letter-spacing:0.1em;font-size:0.6875rem;font-weight:700;color:var(--mute);text-align:left;padding:12px 16px;background:var(--ink-2);border-bottom:1px solid var(--line)}
tbody td{padding:11px 16px;border-bottom:1px solid var(--line);vertical-align:top;font-size:0.9rem;color:var(--text)}
tbody tr:last-child td{border-bottom:none}
td.ch{font-family:var(--mono);white-space:nowrap;color:var(--mute-2);font-size:0.8rem}
td.t{color:var(--text)}
.companions{display:flex;flex-wrap:wrap;gap:8px 18px;font-family:var(--mono);font-size:0.8rem}
@media (max-width:760px){
  .meta{flex-direction:column}
  thead{display:none}
  table,tbody,tr,td{display:block;width:100%}
  table{border:none;background:transparent}
  tbody tr{border:1px solid var(--line);margin-bottom:8px;padding:4px 0;background:var(--ink-2)}
  tbody td{border-bottom:none;padding:4px 12px;overflow-wrap:anywhere}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
""".replace("\n", "\n")


def render(pack: dict, cat: dict, ver: str) -> str:
    slug = html.escape(pack["slug"])
    title = html.escape(deslop(pack["title"]))
    name = html.escape(pack["name"])
    desc = md_inline(pack["desc"])
    meta_desc = html.escape(clip(pack["desc"]))
    chapters_n = len(pack["chapters"])
    licence = html.escape(deslop(str(cat.get("license", "see NOTICE"))))
    tier = cat.get("license_tier", "")
    commercial = "Permitted" if cat.get("commercial_use") else "Not granted"
    src_ver = html.escape(deslop(str(cat.get("source_version", ""))))
    if len(src_ver) > 140:
        src_ver = src_ver[: src_ver.rfind(" ", 0, 140)] + "..."
    publisher = html.escape(deslop(str(cat.get("publisher", ""))))

    rows = []
    for num, rest, relpath in pack["chapters"]:
        rows.append(
            f'<tr><td class="ch">Ch {html.escape(num)}</td>'
            f'<td class="t"><a href="{REPO}/blob/main/packs/{slug}/chapters/{html.escape(relpath)}">{html.escape(rest)}</a></td></tr>'
        )
    chapters_html = "\n".join(rows) or '<tr><td class="t">Reference pack without chapter files; see SKILL.md.</td></tr>'

    return f"""<!doctype html>
<!--
  Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see ../../LICENSE).
  SPDX-License-Identifier: MIT
  GENERATED by tooling/gen_pack_pages.py. Do not hand-edit (RR-B-00).
  Landing page for the {name} pack. JGS ink family stylesheet (site.css) plus inline page
  CSS; no third-party asset. Regenerate with: python tooling/gen_pack_pages.py --only {slug}
-->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>{title}: an installable skill for AI coding agents | JGS SE Knowledge Packs</title>
<meta name="description" content="Install the {name} as an on-demand Agent Skill: {meta_desc}">
<link rel="canonical" href="{PAGES}/packs/{slug}/">
<link rel="icon" type="image/svg+xml" href="../../favicon.svg">
<link rel="stylesheet" href="../../site.css">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}, installable as an AI agent skill">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="{PAGES}/packs/{slug}/">
<meta property="og:image" content="{PAGES}/assets/og-default.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}, installable as an AI agent skill">
<meta name="twitter:description" content="{meta_desc}">
<meta name="twitter:image" content="{PAGES}/assets/og-default.png">
<style>
__BRAND_TOKENS__
{CSS}
</style>
</head>
<body>

<header class="masthead"><div class="wrap">
  <span>CLASSIFICATION: <b>PUBLIC</b></span>
  <span>LICENCE: <b>MIT</b></span>
  <span>DOC-ID: <b>JGS-SE-KP/PACK</b></span>
  <span>REV <b>{ver}</b></span>
</div></header>

<header class="hd"><div class="wrap">
  <span class="label">JG Systems Consulting Ltd. · Knowledge pack · /{slug}</span>
  <h1>{title}</h1>
  <p>{desc}</p>
  <div class="backnav">
    <a href="../../packs.html">&larr; All packs</a>
    <a href="../../index.html">Overview</a>
    <a href="{REPO}/blob/main/packs/{slug}/SKILL.md">SKILL.md on GitHub</a>
  </div>
</div></header>

<section><div class="wrap">
  <div class="meta">
    <div class="mcell"><span class="label">Source</span><b>{publisher}</b></div>
    <div class="mcell"><span class="label">Licence</span><b>{licence}</b></div>
    <div class="mcell"><span class="label">Tier</span><b>{html.escape(str(tier))}</b></div>
    <div class="mcell"><span class="label">Commercial use</span><b>{commercial}</b></div>
    <div class="mcell"><span class="label">Chapters</span><b>{chapters_n}</b></div>
    <div class="mcell"><span class="label">Invoke</span><b>/{slug} &lt;question&gt;</b></div>
  </div>
</div></section>

<section><div class="wrap">
  <span class="label">Install the pack</span>
  <div class="install">
<pre><span class="cm"># with the Vercel skills CLI</span>
npx skills add jgsystemsconsulting/jgs-se-knowledge-packs --skill {slug}

<span class="cm"># as a Claude Code plugin</span>
/plugin marketplace add jgsystemsconsulting/jgs-se-knowledge-packs
/plugin install jgs-se-knowledge-packs@jgs-se-knowledge-packs

<span class="cm"># or clone and install the whole catalogue</span>
python install.py</pre>
  </div>
</div></section>

<section><div class="wrap">
  <span class="label">Document and source version</span>
  <p style="color:var(--text);max-width:80ch;font-size:0.9rem">{src_ver}</p>
</div></section>

<section><div class="wrap">
  <span class="label">Chapters, {chapters_n} on demand</span>
  <table style="margin-top:10px">
    <thead><tr><th style="width:6rem">Chapter</th><th>Topic</th></tr></thead>
    <tbody>
{chapters_html}
    </tbody>
  </table>
</div></section>

<section><div class="wrap">
  <span class="label">Pack files on GitHub</span>
  <div class="companions" style="margin-top:10px">
    <a href="{REPO}/blob/main/packs/{slug}/SKILL.md">SKILL.md</a>
    <a href="{REPO}/blob/main/packs/{slug}/glossary.md">glossary.md</a>
    <a href="{REPO}/blob/main/packs/{slug}/patterns.md">patterns.md</a>
    <a href="{REPO}/blob/main/packs/{slug}/cheatsheet.md">cheatsheet.md</a>
    <a href="{REPO}/blob/main/packs/{slug}/LICENSE">LICENSE</a>
  </div>
</div></section>

<footer><div class="wrap">
  <div class="tblock">
    <div><span class="label">Product</span><b>jgs-se-knowledge-packs</b></div>
    <div><span class="label">Rev</span><b>{ver}</b></div>
    <div><span class="label">Pack licence</span><b>{licence}</b></div>
    <div><span class="label">Repository</span><b><a href="{REPO}">github.com/jgsystemsconsulting</a></b></div>
    <div><span class="label">All packs</span><b><a href="../../packs.html">packs.html</a></b></div>
    <div><span class="label">Owner</span><b>JG Systems Consulting Ltd</b></div>
  </div>
  <p class="foot-note">&copy; 2026 JG Systems Consulting Ltd. Tooling MIT; this pack's content carries {licence} (see <a href="{REPO}/blob/main/packs/{slug}/LICENSE">the pack licence</a>). Commercial or academic licensing: <a href="https://labs.jgsystemsconsulting.com/licensing.html">labs.jgsystemsconsulting.com/licensing.html</a>.</p>
</div></footer>

</body>
</html>
""".replace("__BRAND_TOKENS__", brand_tokens())


def write_sitemap(slugs: list) -> None:
    urls = [f"{PAGES}/", f"{PAGES}/packs.html"] + [f"{PAGES}/packs/{s}/" for s in slugs]
    today = date.today().isoformat()
    body = "\n".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in urls)
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n</urlset>\n"
    )
    out = ROOT / "docs" / "sitemap.xml"
    out.write_text(xml, encoding="utf-8", newline="\n")


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate per-pack landing pages + sitemap")
    ap.add_argument("--only", default="", help="comma-separated slugs; default: all packs")
    args = ap.parse_args()
    cats = catalog_packs()
    slugs = [s.strip() for s in args.only.split(",") if s.strip()] if args.only else sorted(cats)
    missing = [s for s in slugs if s not in cats]
    if missing:
        print(f"ERROR: unknown pack slugs: {', '.join(missing)}", file=sys.stderr)
        return 1
    outdir = ROOT / "docs" / "packs"
    for slug in slugs:
        pack = read_pack(slug)
        dest = outdir / slug / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(pack, cats[slug], version()), encoding="utf-8", newline="\n")
        print(f"wrote {dest.relative_to(ROOT)} ({len(pack['chapters'])} chapters)")
    write_sitemap(slugs)
    print(f"wrote docs/sitemap.xml ({len(slugs)} pack pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

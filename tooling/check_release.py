#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
check_release.py — local release-readiness gate for jgs-se-knowledge-packs.

Run before tagging a release. Aggregates every mechanical check the JGS release
standard requires for this repo and exits non-zero on any failure:

  1. Required files present (governance, identity, versioning, RR-S furniture).
  2. No leak sentinels (confidential markers, private-key blocks).
  3. No source-material links published (link policy — see docs/LICENSING.md).
     Banned hosts load from tooling/link-policy-hosts.txt at runtime; the list
     is data, not a literal in this file.
  4. Version single-source agreement: plugin.json == CHANGELOG top ==
     RELEASE-INFO.txt == the two website product YAMLs under docs/products/website.
  5. Every pack passes tooling/validate_pack.py (structure + licence tier).
  6. SKILLS.md entry count == number of shipped packs.
  7. JGSC + SPDX header present on authored files (NOT pack content).
  8. Multi-pack chapter-basename overlap via check_overlap.main() (local/trusted).
  9. Capability-pack map freshness via check_capability_map.main() (local/trusted).
 10. Classification-rules completeness via check_classification_rules.main()
     (MAP-21-01; local/trusted).
 11. Capability-map generator replay via generate_capability_map.main() --check
     (MAP-21-05; local/trusted; uses on-disk map generated_on).
  12. HTML self-containment ([html-assets]): every docs/*.html page is scanned
     for external http(s) asset references; hosts must be exactly
     FIRST_PARTY_HOSTS (github.com, jgsystemsconsulting.github.io) with empty
     userinfo; data: URIs and relative paths are allowed; protocol-relative
     URLs fail; zero pages fails closed.
     Plus brand-token parity ([brand-tokens], P13): the exclusive BRAND-TOKENS
     slice extracted from docs/index.html must appear verbatim in
     docs/packs.html.
  13. Landing catalogue counts ([catalogue-count], P15): live content count N and
     signpost count M from packs/*/SKILL.md frontmatter must equal the §06
     headline, chip COUNT sum (with exactly one Signposts chip equal to M),
     figcaption N/M, and still-catalogue.svg subtitle/footer N/M.
  14. Catalog live-set parity ([catalog-live-set], P16): content pack slug set from
     packs/*/SKILL.md (signposts and orchestrators excluded) must equal
     catalog.json packs[].slug where status is live or absent; signpost and
     orchestrator slugs must not appear in catalog.packs. planned[] is free.
     updated is review-only after the b-03 bump.
  15. Routing map coverage ([routing-map], /se): exactly one kind: orchestrator
     member; ROUTING-MAP markers and four subheadings; pack-cell slug resolution
     and Topics coverage of every content slug; licence parity for non-Public-Domain
     content packs.

stdlib only. This is a LOCAL/trusted gate and may run repo code; the CI workflow
(.github/workflows/validate.yml) inlines its own checks and never executes repo code.
CI-covered: version, index, overlap, map/rules data invariants, html-assets,
catalogue-count, catalog-live-set, routing-map. Local-only required before tag: pack validation,
packs.html freshness, full map/rules checks, replay.

Pre-tag rule: run this gate at the exact commit being tagged and require a PASS
line whose sha matches that commit (a `@ no-git` receipt never satisfies it).

Usage:  python tooling/check_release.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "LICENSE", "COPYRIGHT", "NOTICE", "README.md", "CHANGELOG.md", "SECURITY.md",
    "CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "SKILLS.md", "RELEASE-INFO.txt",
    ".gitignore", "catalog.json",
    ".claude-plugin/marketplace.json", ".claude-plugin/plugin.json",
    "install.py", "install.sh", "install.ps1",
    "docs/SOURCE-VETTING.md", "docs/PACK-SPEC.md", "docs/LICENSING.md", "docs/skill-usage.md",
    "tooling/validate_pack.py", "tooling/build_pack.py", "tooling/link-policy-hosts.txt",
]

# Assembled from fragments so this scanner file does not flag itself as a leak.
_PK = "PRIVATE" + " KEY"
LEAK_SENTINELS = ["CONFI" + "DENTIAL", "BEGIN " + _PK, "BEGIN OPENSSH " + _PK, "BEGIN RSA " + _PK]

# Source-material hosts that must never appear as published links (link policy).
# The list is data: one plain token per line in tooling/link-policy-hosts.txt.
HOST_DATA = "tooling/link-policy-hosts.txt"
_HOST_TOKEN = re.compile(r"^[A-Za-z0-9.-]+$")


class LinkPolicyDataError(Exception):
    """The banned-host data file is missing, empty, or malformed (fail closed)."""


def load_banned_hosts() -> list[str]:
    """Load banned-host tokens from HOST_DATA, sorted and de-duplicated.

    Skips blank lines and '#' comments. Any other malformed line, an unreadable
    file, or zero tokens raises LinkPolicyDataError so the gate fails closed
    instead of silently unbanning hosts.
    """
    try:
        lines = (ROOT / HOST_DATA).read_text(encoding="utf-8").splitlines()
    except OSError as e:
        raise LinkPolicyDataError(f"cannot read {HOST_DATA}: {e}") from e
    tokens: list[str] = []
    for lineno, raw in enumerate(lines, 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if not _HOST_TOKEN.fullmatch(line):
            raise LinkPolicyDataError(
                f"malformed line in {HOST_DATA} (line {lineno}): {raw!r}"
            )
        tokens.append(line)
    if not tokens:
        raise LinkPolicyDataError(f"host list empty ({HOST_DATA} has no tokens)")
    return sorted(set(tokens))

# Authored-file header sentinels (RR-B-03/04) — checked on JGSC-authored files only,
# never on pack content (which carries the source's licence).
HEADER_SENTINEL = "Copyright (c) 2026 JG Systems Consulting Ltd."
SPDX_SENTINEL = "SPDX-License-Identifier: MIT"

# P12 html-assets: first-party allowlist for the docs/*.html self-containment scan.
FIRST_PARTY_HOSTS = {"github.com", "jgsystemsconsulting.github.io"}

# P13 brand-token markers; the same literals are pinned in test_ci_gate.HTML_ASSET_PAIR.
BRAND_BEGIN = "/* BRAND-TOKENS:BEGIN"
BRAND_END = "/* BRAND-TOKENS:END"

# Quote-aware open-tag slicer: does not stop on > inside quoted attribute values.
TAG_SLICE = re.compile(
    r"<(link|img|script|iframe|source|video|audio|embed|track|object|base|meta)\b"
    r"(?:\"[^\"]*\"|'[^']*'|[^>])*>",
    re.I,
)
# Three-branch attribute extractor. Do NOT merge into one conditional named-group
# quote: an empty optional quote group can take the wrong branch and yield an
# empty value for unquoted attributes. Value = first non-None of groups d, s, u.
ATTR = re.compile(
    r"""(?P<name>href|src|data|srcset|content|http-equiv|property|name)\s*=\s*"""
    r"""(?:"(?P<d>[^"]*)"|'(?P<s>[^']*)'|(?P<u>[^\s>]+))""",
    re.I,
)
# Inline CSS: url(...) with optional quotes, and @import in all three forms.
# Intentionally over-broad (a url( inside an inline script string is flagged);
# that direction is fail closed.
CSS_URL = re.compile(r"""url\(\s*(['"]?)([^)'"\s]+)\1\s*\)""", re.I)
CSS_IMPORT = re.compile(
    r"""@import\s+(?:url\(\s*(['"]?)([^)'"\s]+)\1\s*\)|(['"])([^'"]+)\3)\s*;?""",
    re.I,
)

_META_IMAGE_PROPS = {"og:image", "og:image:secure_url"}
_META_IMAGE_NAMES = {"twitter:image", "twitter:image:src"}
_HREF_ELEMENTS = {"link", "base"}
_SRC_ELEMENTS = {"img", "script", "iframe", "source", "video", "audio", "embed", "track"}


def scan_html_external_assets(text: str) -> list[str]:
    """Return the distinct external asset URLs in one HTML document.

    Two passes over the raw text, case-insensitive; regex, not html.parser, so
    the literals pin byte-identical between this gate and the CI twin
    (tooling/test_ci_gate.py). Ambiguities resolve toward failing.

    Pass one slices candidate open tags (quote-aware, so a > inside a quoted
    attribute value does not cut the tag) and reads the asset attributes from
    a closed taxonomy: link/base href; img/script/iframe/source/video/audio/
    embed/track src; object data; srcset on any sliced tag (comma-split, first
    whitespace token per group); meta property og:image / og:image:secure_url
    and meta name twitter:image / twitter:image:src content; and meta
    http-equiv=refresh (URL after url= inside content, case-insensitive, with
    surrounding quotes stripped). Anchors (<a href>) are never scanned: the
    github.com blob links in the page bodies are navigation, not fetched
    assets. <base> is included because an absolute base href silently re-hosts
    every relative asset on the page.

    Pass two sweeps inline CSS: url(...) and @import in double-quote,
    single-quote, and url(...) forms.

    Classification, in order: empty/# skipped; data: allowed (the favicon
    embeds http://www.w3.org/2000/svg inside a data URI and must never fail);
    http(s) allowed only on an exact FIRST_PARTY_HOSTS host with empty
    userinfo; protocol-relative //host/x fails; any relative form allowed
    without existence checks.

    Self-host convention: images under docs/assets/, fonts under docs/fonts/,
    relative references only. Accepted limits: no HTML entity decoding, the
    closed taxonomy above, no on-disk resolution of relative paths.
    """
    def is_external(url: str) -> bool:
        url = url.strip()
        if not url or url.startswith("#") or url[:5].lower() == "data:":
            return False
        if url[:7].lower() == "http://" or url[:8].lower() == "https://":
            parts = urlsplit(url)
            host = (parts.hostname or "").lower()
            if host in FIRST_PARTY_HOSTS and not parts.username and not parts.password:
                return False
            return True
        return url.startswith("//")

    found: list[str] = []

    def consider(raw: str) -> None:
        url = raw.strip()
        if is_external(url) and url not in found:
            found.append(url)

    for m in TAG_SLICE.finditer(text):
        tag = m.group(0)
        elem = m.group(1).lower()
        attrs = {}
        for a in ATTR.finditer(tag):
            value = a.group("d")
            if value is None:
                value = a.group("s")
            if value is None:
                value = a.group("u")
            name = a.group("name").lower()
            if name not in attrs:  # first attribute wins, matching browsers
                attrs[name] = value
        if elem in _HREF_ELEMENTS and "href" in attrs:
            consider(attrs["href"])
        if elem in _SRC_ELEMENTS and "src" in attrs:
            consider(attrs["src"])
        if elem == "object" and "data" in attrs:
            consider(attrs["data"])
        if "srcset" in attrs:
            for group in attrs["srcset"].split(","):
                tokens = group.strip().split()
                if tokens:
                    consider(tokens[0])
        if elem == "meta":
            prop = attrs.get("property", "").lower()
            name_attr = attrs.get("name", "").lower()
            if prop in _META_IMAGE_PROPS or name_attr in _META_IMAGE_NAMES:
                if "content" in attrs:
                    consider(attrs["content"])
            elif attrs.get("http-equiv", "").strip().lower() == "refresh" and "content" in attrs:
                m2 = re.search(r"url\s*=\s*(.*)", attrs["content"], re.I)
                if m2:
                    target = m2.group(1).strip()
                    if len(target) >= 2 and target[0] in "\"'" and target[-1] == target[0]:
                        target = target[1:-1]
                    consider(target)

    for m in CSS_URL.finditer(text):
        consider(m.group(2))
    for m in CSS_IMPORT.finditer(text):
        consider(m.group(2) if m.group(2) is not None else m.group(4))

    return found


def slice_brand_tokens(text: str) -> str:
    """Exclusive interior between the BRAND-TOKENS BEGIN and END marker lines
    in docs/index.html. Same algorithm as gen_packs_page.slice_brand_tokens,
    inlined by twin convention (this gate never imports generator code);
    raises ValueError on missing, duplicated, reversed, or unbalanced markers.
    """
    lines = text.splitlines()
    begins = [i for i, ln in enumerate(lines) if ln.startswith(BRAND_BEGIN)]
    ends = [i for i, ln in enumerate(lines) if ln.startswith(BRAND_END)]
    if len(begins) != 1 or len(ends) != 1:
        raise ValueError(
            f"docs/index.html: expected exactly one BRAND-TOKENS BEGIN and one END "
            f"marker line, found {len(begins)} BEGIN / {len(ends)} END"
        )
    if begins[0] >= ends[0]:
        raise ValueError(
            "docs/index.html: BRAND-TOKENS:BEGIN must precede BRAND-TOKENS:END"
        )
    return "\n".join(lines[begins[0] + 1:ends[0]])


# P15 catalogue-count: section marker, h2, chip COUNT, SVG N/M. Literals below are
# pinned byte-identical in .github/workflows/validate.yml (test_ci_gate CATALOGUE_COUNT_PAIR).
CATALOGUE_SECTION_MARKER = "<!-- §06 The catalogue -->"
CATALOGUE_H2_RE = re.compile(
    r"<h2>\s*(\d+)\s+packs\s*(?:&middot;|·)\s*(\d+)\s+signposts\s*</h2>",
    re.I,
)
CATALOGUE_CHIP_RE = re.compile(
    r'<div\s+class="pk"\s*>\s*<b>(.*?)</b>',
    re.I | re.S,
)
CATALOGUE_CHIP_COUNT_RE = re.compile(
    r"^(?P<label>.*?)\s*(?:&middot;|·)\s*(?P<count>\d+)\s*$",
    re.S,
)
CATALOGUE_SVG_NM_RE = re.compile(
    r"(\d+)\s+packs\s*(?:&middot;|·)\s*(\d+)\s+signposts",
    re.I,
)
STILL_CATALOGUE_SVG = "docs/assets/still-catalogue.svg"


def inventory_pack_slugs(
    packs_root: Path, tag: str = "[catalogue-count]"
) -> tuple[set[str], set[str], set[str], list[str]]:
    """Return (content_slugs, signpost_slugs, orchestrator_slugs, errors).

    Every immediate child directory must contain SKILL.md with parseable YAML
    frontmatter between --- fences. A frontmatter line matching
    ^kind:\\s*signpost\\s*$ (case-insensitive) marks a signpost;
    ^kind:\\s*orchestrator\\s*$ marks an orchestrator; all others are content
    packs. Live sets never come from a hardcoded constant. ``tag`` prefixes
    fail messages so callers can attribute catalogue-count vs catalog-live-set.
    """
    errs: list[str] = []
    content: set[str] = set()
    signposts: set[str] = set()
    orchestrators: set[str] = set()
    if not packs_root.is_dir():
        return content, signposts, orchestrators, [
            f"{tag} packs root missing: {packs_root}"
        ]
    for child in sorted(p for p in packs_root.iterdir() if p.is_dir()):
        skill = child / "SKILL.md"
        if not skill.is_file():
            errs.append(f"{tag} missing SKILL.md in packs/{child.name}")
            continue
        try:
            text = skill.read_text(encoding="utf-8")
        except OSError as e:
            errs.append(f"{tag} cannot read packs/{child.name}/SKILL.md: {e}")
            continue
        m = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.S)
        if not m:
            errs.append(
                f"{tag} unparseable frontmatter in packs/{child.name}/SKILL.md"
            )
            continue
        fm = m.group(1)
        if re.search(r"^kind:\s*signpost\s*$", fm, re.I | re.M):
            signposts.add(child.name)
        elif re.search(r"^kind:\s*orchestrator\s*$", fm, re.I | re.M):
            orchestrators.add(child.name)
        else:
            content.add(child.name)
    return content, signposts, orchestrators, errs


def inventory_pack_counts(packs_root: Path) -> tuple[int, int, list[str]]:
    """Return (content_N, signpost_M, errors); wrapper over inventory_pack_slugs."""
    content, signposts, _orchestrators, errs = inventory_pack_slugs(
        packs_root, tag="[catalogue-count]"
    )
    return len(content), len(signposts), errs


def slice_catalogue_section(html: str) -> str | None:
    """Return docs/index.html text from §06 marker to the next section comment."""
    start = html.find(CATALOGUE_SECTION_MARKER)
    if start < 0:
        return None
    rest = html[start + len(CATALOGUE_SECTION_MARKER):]
    nxt = re.search(r"\n<!--\s*§", rest)
    if nxt:
        return html[start:start + len(CATALOGUE_SECTION_MARKER) + nxt.start()]
    return html[start:]


def parse_catalogue_h2(section: str) -> tuple[int, int] | None:
    """Parse §06 h2 as (packs_N, signposts_M); entity-aware middot."""
    m = CATALOGUE_H2_RE.search(section)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def parse_catalogue_chips(section: str) -> tuple[int, int | None, int, list[str]]:
    """Return (content_sum, signpost_count_or_None, signpost_chip_n, errors).

    COUNT is only the integer after the separator in the <b> label. Digits inside
    <span> descriptions are ignored. Exactly one chip whose label contains
    'signpost' (case-insensitive) is required by the caller.
    """
    errs: list[str] = []
    content_sum = 0
    signpost_count: int | None = None
    signpost_chips = 0
    for m in CATALOGUE_CHIP_RE.finditer(section):
        inner = re.sub(r"\s+", " ", m.group(1)).strip()
        cm = CATALOGUE_CHIP_COUNT_RE.match(inner)
        if not cm:
            errs.append(
                f"[catalogue-count] unparseable chip label: {inner!r}"
            )
            continue
        label = cm.group("label")
        count = int(cm.group("count"))
        if re.search(r"signpost", label, re.I):
            signpost_chips += 1
            signpost_count = count
        else:
            content_sum += count
    return content_sum, signpost_count, signpost_chips, errs


def parse_svg_catalogue_nm(svg_text: str) -> tuple[tuple[int, int] | None, tuple[int, int] | None]:
    """Return (subtitle_NM, footer_NM) pairs from still-catalogue.svg text nodes."""
    texts = re.findall(r"<text\b[^>]*>(.*?)</text>", svg_text, re.I | re.S)
    subtitle = None
    footer = None
    for raw in texts:
        t = re.sub(r"\s+", " ", raw).strip()
        m = CATALOGUE_SVG_NM_RE.search(t)
        if not m:
            continue
        pair = (int(m.group(1)), int(m.group(2)))
        if "open sources" in t.lower():
            subtitle = pair
        elif "filter" in t.lower() or "packs.html" in t.lower():
            footer = pair
        elif subtitle is None:
            subtitle = pair
        else:
            footer = pair
    return subtitle, footer


def check_catalogue_count(
    packs_root: Path,
    index_html: str,
    svg_text: str | None,
    svg_missing: bool = False,
) -> list[str]:
    """Fail-closed equality of live N/M vs landing §06 and still-catalogue.svg."""
    errs: list[str] = []
    n_live, m_live, inv_errs = inventory_pack_counts(packs_root)
    errs.extend(inv_errs)
    if inv_errs:
        return errs

    section = slice_catalogue_section(index_html)
    if section is None:
        errs.append(
            "[catalogue-count] missing section marker "
            f"{CATALOGUE_SECTION_MARKER!r} in docs/index.html"
        )
        return errs

    h2 = parse_catalogue_h2(section)
    if h2 is None:
        errs.append(
            f"[catalogue-count] §06 h2 must match '<N> packs · <M> signposts' "
            f"(live {n_live} packs / {m_live} signposts)"
        )
    else:
        n_h2, m_h2 = h2
        if n_h2 != n_live or m_h2 != m_live:
            errs.append(
                f"[catalogue-count] §06 h2 states {n_h2} packs / {m_h2} signposts "
                f"but live inventory is {n_live} packs / {m_live} signposts"
            )

    content_sum, signpost_count, signpost_chips, chip_errs = parse_catalogue_chips(section)
    errs.extend(chip_errs)
    if signpost_chips != 1:
        errs.append(
            f"[catalogue-count] expected exactly one Signposts chip, found {signpost_chips} "
            f"(live signposts {m_live})"
        )
    elif signpost_count != m_live:
        errs.append(
            f"[catalogue-count] Signposts chip COUNT {signpost_count} != live signposts {m_live}"
        )
    if content_sum != n_live:
        errs.append(
            f"[catalogue-count] content chip COUNT sum {content_sum} != live content packs {n_live}"
        )

    # Figcaption: digits N and M, or prescribed word-form caption.
    caps = re.findall(r"<figcaption\b[^>]*>(.*?)</figcaption>", section, re.I | re.S)
    if not caps:
        errs.append("[catalogue-count] §06 figcaption missing")
    else:
        cap = re.sub(r"\s+", " ", caps[0]).strip()
        prescribed = (
            "FIG.06 · Sixty-three packs plus two signposts across open sources; "
            "filter the full list on packs.html."
        )
        cap_norm = cap.replace("&middot;", "·")
        ok = False
        if re.sub(r"\s+", " ", prescribed).strip() == cap_norm:
            ok = True
        elif str(n_live) in cap and str(m_live) in cap:
            ok = True
        else:
            # word-form: sixty-three / two when live is 63/2; else require digits
            words = {
                0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
            }
            # Accept "Sixty-three" style for 63 via digits-or-words containing both
            if n_live == 63 and m_live == 2:
                if re.search(r"sixty[-\s]?three", cap, re.I) and re.search(
                    r"\btwo\b", cap, re.I
                ):
                    ok = True
            if not ok and n_live in words and m_live in words:
                if re.search(rf"\b{words[n_live]}\b", cap, re.I) and re.search(
                    rf"\b{words[m_live]}\b", cap, re.I
                ):
                    ok = True
        if not ok:
            errs.append(
                f"[catalogue-count] §06 figcaption must carry live N={n_live} and M={m_live} "
                f"(digit or word form); got {cap!r}"
            )

    if svg_missing or svg_text is None:
        errs.append(f"[catalogue-count] missing {STILL_CATALOGUE_SVG}")
    else:
        sub_nm, foot_nm = parse_svg_catalogue_nm(svg_text)
        if sub_nm is None:
            errs.append(
                f"[catalogue-count] {STILL_CATALOGUE_SVG} subtitle missing "
                f"'N packs · M signposts' (live {n_live}/{m_live})"
            )
        elif sub_nm != (n_live, m_live):
            errs.append(
                f"[catalogue-count] {STILL_CATALOGUE_SVG} subtitle states "
                f"{sub_nm[0]} packs / {sub_nm[1]} signposts but live is "
                f"{n_live} packs / {m_live} signposts"
            )
        if foot_nm is None:
            errs.append(
                f"[catalogue-count] {STILL_CATALOGUE_SVG} footer missing "
                f"'N packs · M signposts' (live {n_live}/{m_live})"
            )
        elif foot_nm != (n_live, m_live):
            errs.append(
                f"[catalogue-count] {STILL_CATALOGUE_SVG} footer states "
                f"{foot_nm[0]} packs / {foot_nm[1]} signposts but live is "
                f"{n_live} packs / {m_live} signposts"
            )
    return errs


# P16 catalog-live-set: live slug set vs packs/. Literals pinned in validate.yml
# (test_ci_gate CATALOG_LIVE_SET_PAIR).
CATALOG_JSON_PATH = "catalog.json"
CATALOG_LIVE_SET_TAG = "[catalog-live-set]"


def check_catalog_live_set(
    packs_root: Path, catalog: dict | None, catalog_error: str | None = None
) -> list[str]:
    """Fail-closed equality of content pack slugs vs catalog.json live packs[].

    Live catalog slugs are entries with status 'live' or missing status. Signpost
    and orchestrator pack dirs must not appear in catalog.packs under any status.
    planned[] is free.
    """
    errs: list[str] = []
    if catalog_error:
        errs.append(f"{CATALOG_LIVE_SET_TAG} {catalog_error}")
        return errs
    if not isinstance(catalog, dict):
        errs.append(f"{CATALOG_LIVE_SET_TAG} {CATALOG_JSON_PATH} root must be an object")
        return errs

    content, signposts, orchestrators, inv_errs = inventory_pack_slugs(
        packs_root, tag=CATALOG_LIVE_SET_TAG
    )
    errs.extend(inv_errs)
    if inv_errs:
        return errs

    packs_list = catalog.get("packs")
    if not isinstance(packs_list, list):
        errs.append(
            f"{CATALOG_LIVE_SET_TAG} {CATALOG_JSON_PATH} packs must be a list"
        )
        return errs

    live: set[str] = set()
    all_slugs: set[str] = set()
    duplicates: list[str] = []
    bad_entries = 0
    for i, entry in enumerate(packs_list):
        if not isinstance(entry, dict):
            bad_entries += 1
            continue
        slug = entry.get("slug")
        if not isinstance(slug, str) or not slug.strip():
            bad_entries += 1
            continue
        slug = slug.strip()
        if slug in all_slugs:
            duplicates.append(slug)
        all_slugs.add(slug)
        status = entry.get("status")
        if status is None or status == "live":
            live.add(slug)

    if bad_entries:
        errs.append(
            f"{CATALOG_LIVE_SET_TAG} {CATALOG_JSON_PATH} packs has {bad_entries} "
            "entries missing a non-empty string slug"
        )
    if duplicates:
        errs.append(
            f"{CATALOG_LIVE_SET_TAG} duplicate slug(s) in {CATALOG_JSON_PATH} packs: "
            f"{sorted(set(duplicates))}"
        )

    only_packs = sorted(content - live)
    only_catalog = sorted(live - content)
    if only_packs or only_catalog:
        parts = []
        if only_packs:
            parts.append(f"only in packs/: {only_packs}")
        if only_catalog:
            parts.append(f"only in catalog.packs live: {only_catalog}")
        errs.append(
            f"{CATALOG_LIVE_SET_TAG} live slug set mismatch "
            f"(content packs {len(content)} vs catalog live {len(live)}): "
            + "; ".join(parts)
        )

    signposts_in_catalog = sorted(signposts & all_slugs)
    if signposts_in_catalog:
        errs.append(
            f"{CATALOG_LIVE_SET_TAG} signpost slug(s) must not appear in "
            f"{CATALOG_JSON_PATH} packs: {signposts_in_catalog}"
        )
    orchestrators_in_catalog = sorted(orchestrators & all_slugs)
    if orchestrators_in_catalog:
        errs.append(
            f"{CATALOG_LIVE_SET_TAG} orchestrator slug(s) must not appear in "
            f"{CATALOG_JSON_PATH} packs: {orchestrators_in_catalog}"
        )
    return errs


# P17 routing-map: /se orchestrator map coverage. Literals pinned in validate.yml
# (test_ci_gate ROUTING_MAP_PAIR; twin lands in Task 6).
ROUTING_MAP_TAG = "[routing-map]"
ROUTING_MAP_BEGIN = "<!-- ROUTING-MAP:BEGIN -->"
ROUTING_MAP_END = "<!-- ROUTING-MAP:END -->"
ROUTING_MAP_HEADINGS = (
    "### Topics",
    "### Agency contexts",
    "### Deliverables",
    "### Licences",
)
# Pack-bearing column indexes (zero-based) per pinned header.
ROUTING_MAP_PACK_COLS = {
    "### Topics": (2,),  # Packs (best first)
    "### Agency contexts": (2,),  # Packs
    "### Deliverables": (2, 3, 4),  # Draft, Review, Verify
    "### Licences": (0,),  # Pack
}
ROUTING_MAP_SLUG_RE = re.compile(r"^[a-z0-9-]+$")
ROUTING_MAP_BACKTICK_RE = re.compile(r"`([^`]*)`")
ROUTING_MAP_SEP_RE = re.compile(r"^[\|\-:\s]+$")
ROUTING_MAP_LICENSE_RE = re.compile(r"^license:\s*(.*)$", re.M)


def _routing_map_split_row(line: str) -> list[str]:
    """Split a Markdown table row into stripped cell strings."""
    raw = line.strip()
    if raw.startswith("|"):
        raw = raw[1:]
    if raw.endswith("|"):
        raw = raw[:-1]
    return [c.strip() for c in raw.split("|")]


def _routing_map_is_separator(line: str) -> bool:
    s = line.strip()
    return bool(s) and ROUTING_MAP_SEP_RE.fullmatch(s) is not None


def _routing_map_pack_yaml_license(pack_dir: Path) -> str | None:
    """Return PACK.yaml license value with surrounding double quotes stripped, or None."""
    path = pack_dir / "PACK.yaml"
    if not path.is_file():
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    m = ROUTING_MAP_LICENSE_RE.search(text)
    if not m:
        return None
    val = m.group(1).strip()
    if len(val) >= 2 and val[0] == '"' and val[-1] == '"':
        val = val[1:-1]
    return val


def check_routing_map(packs_root: Path) -> list[str]:
    """Fail-closed routing-map coverage for the single orchestrator member.

    Rules 1-6: exactly one kind: orchestrator; ROUTING-MAP markers and four
    subheadings; backticked slug resolution; pack-cell grammar; Topics Packs
    column covers every content slug; Licences parity for non-Public-Domain
    content packs. Every message is prefixed [routing-map].
    """
    tag = ROUTING_MAP_TAG
    errs: list[str] = []

    content, _signposts, orchestrators, inv_errs = inventory_pack_slugs(
        packs_root, tag=tag
    )
    errs.extend(inv_errs)

    if len(orchestrators) != 1:
        errs.append(
            f"{tag} exactly one orchestrator member required: "
            f"{len(orchestrators)} found"
        )
        return errs

    orch_slug = next(iter(orchestrators))
    skill_path = packs_root / orch_slug / "SKILL.md"
    try:
        skill_text = skill_path.read_text(encoding="utf-8")
    except OSError as e:
        errs.append(f"{tag} cannot read packs/{orch_slug}/SKILL.md: {e}")
        return errs

    n_begin = skill_text.count(ROUTING_MAP_BEGIN)
    n_end = skill_text.count(ROUTING_MAP_END)
    if n_begin != 1 or n_end != 1:
        errs.append(
            f"{tag} expected exactly one {ROUTING_MAP_BEGIN} and one "
            f"{ROUTING_MAP_END}, found {n_begin} BEGIN / {n_end} END"
        )
        return errs
    begin_at = skill_text.find(ROUTING_MAP_BEGIN)
    end_at = skill_text.find(ROUTING_MAP_END)
    if begin_at >= end_at:
        errs.append(
            f"{tag} {ROUTING_MAP_BEGIN} must precede {ROUTING_MAP_END}"
        )
        return errs

    region = skill_text[begin_at + len(ROUTING_MAP_BEGIN) : end_at]

    # Heading presence and order (each exactly once).
    positions: dict[str, int] = {}
    for h in ROUTING_MAP_HEADINGS:
        matches = list(re.finditer(re.escape(h), region))
        if len(matches) != 1:
            errs.append(
                f"{tag} expected exactly one '{h}' in routing map, "
                f"found {len(matches)}"
            )
            continue
        positions[h] = matches[0].start()
    if len(positions) != len(ROUTING_MAP_HEADINGS):
        return errs
    ordered = sorted(positions, key=positions.get)
    if ordered != list(ROUTING_MAP_HEADINGS):
        errs.append(
            f"{tag} routing-map subheadings must appear in order "
            f"{list(ROUTING_MAP_HEADINGS)}; found {ordered}"
        )
        return errs

    # Slice region into per-heading bodies (text after heading until next heading).
    heading_spans: list[tuple[str, str]] = []
    for i, h in enumerate(ROUTING_MAP_HEADINGS):
        start = positions[h] + len(h)
        end = (
            positions[ROUTING_MAP_HEADINGS[i + 1]]
            if i + 1 < len(ROUTING_MAP_HEADINGS)
            else len(region)
        )
        heading_spans.append((h, region[start:end]))

    topics_pack_tokens: set[str] = set()
    licence_rows: dict[str, str] = {}  # pack slug -> licence cell text

    for heading, body in heading_spans:
        pack_cols = ROUTING_MAP_PACK_COLS[heading]
        lines = body.splitlines()
        table_lines = [ln for ln in lines if ln.strip().startswith("|")]
        if not table_lines:
            errs.append(f"{tag} {heading}: no table rows found")
            continue

        # Classify rows: first non-separator is header; skip separators; rest data.
        header_cells: list[str] | None = None
        data_rows: list[tuple[str, list[str]]] = []  # (raw_line, cells)
        for ln in table_lines:
            if _routing_map_is_separator(ln):
                continue
            cells = _routing_map_split_row(ln)
            if header_cells is None:
                header_cells = cells
                continue
            data_rows.append((ln.strip(), cells))

        if header_cells is None:
            errs.append(f"{tag} {heading}: missing header row")
            continue

        needed = max(pack_cols) + 1
        if len(header_cells) < needed:
            errs.append(
                f"{tag} {heading}: header has {len(header_cells)} column(s), "
                f"need at least {needed}"
            )
            continue

        for raw_line, cells in data_rows:
            row_label = cells[0] if cells else raw_line
            if len(cells) < needed:
                errs.append(
                    f"{tag} {heading}: row {row_label!r} has {len(cells)} "
                    f"column(s), need at least {needed}"
                )
                continue

            # Rule 3: every backticked span on the row must be a slug token, and
            # must name an existing packs/<token>/SKILL.md (not the orchestrator).
            for m in ROUTING_MAP_BACKTICK_RE.finditer(raw_line):
                token = m.group(1)
                if not ROUTING_MAP_SLUG_RE.fullmatch(token):
                    errs.append(
                        f"{tag} {heading}: backticked span `{token}` is not a "
                        f"slug token on row {row_label!r}"
                    )
                    continue
                if token == orch_slug:
                    errs.append(
                        f"{tag} {heading}: orchestrator slug `{token}` must not "
                        f"appear as a routing target on row {row_label!r}"
                    )
                    continue
                target = packs_root / token / "SKILL.md"
                if not target.is_file():
                    errs.append(
                        f"{tag} {heading}: unknown pack slug `{token}` on row "
                        f"{row_label!r}"
                    )

            # Rule 4: pack-bearing cells hold only backticked slugs or are empty.
            for col_i in pack_cols:
                cell = cells[col_i]
                remainder = ROUTING_MAP_BACKTICK_RE.sub("", cell)
                if re.search(r"[^\s,]", remainder):
                    errs.append(
                        f"{tag} {heading}: pack cell has non-slug text on row "
                        f"{row_label!r}: {cell!r}"
                    )
                    continue
                # Collect Topics coverage tokens (column index 2 only).
                if heading == "### Topics" and col_i == 2:
                    for tm in ROUTING_MAP_BACKTICK_RE.finditer(cell):
                        tok = tm.group(1)
                        if ROUTING_MAP_SLUG_RE.fullmatch(tok):
                            topics_pack_tokens.add(tok)

            # Rule 6 gather: Licences pack + licence cells.
            if heading == "### Licences":
                pack_cell = cells[0]
                lic_cell = cells[1] if len(cells) > 1 else ""
                slugs_in_pack = [
                    tm.group(1)
                    for tm in ROUTING_MAP_BACKTICK_RE.finditer(pack_cell)
                    if ROUTING_MAP_SLUG_RE.fullmatch(tm.group(1))
                ]
                if len(slugs_in_pack) != 1:
                    errs.append(
                        f"{tag} {heading}: Pack cell must hold exactly one "
                        f"backticked slug on row {row_label!r}"
                    )
                else:
                    slug = slugs_in_pack[0]
                    if slug in licence_rows:
                        errs.append(
                            f"{tag} {heading}: duplicate Pack row for `{slug}`"
                        )
                    licence_rows[slug] = lic_cell.strip()

    # Rule 5: Topics Packs column covers every content slug.
    missing = sorted(content - topics_pack_tokens)
    for slug in missing:
        errs.append(
            f"{tag} content slug `{slug}` missing from ### Topics Packs column"
        )

    # Rule 6: licence parity for non-Public-Domain content packs.
    expected_lic: dict[str, str] = {}
    for slug in sorted(content):
        lic = _routing_map_pack_yaml_license(packs_root / slug)
        if lic is None:
            errs.append(
                f"{tag} cannot read license: from packs/{slug}/PACK.yaml"
            )
            continue
        if not lic.startswith("Public Domain"):
            expected_lic[slug] = lic

    expected_set = set(expected_lic)
    found_set = set(licence_rows)
    for slug in sorted(expected_set - found_set):
        errs.append(
            f"{tag} ### Licences missing row for non-Public-Domain pack `{slug}`"
        )
    for slug in sorted(found_set - expected_set):
        errs.append(
            f"{tag} ### Licences extra row for `{slug}` "
            f"(not a non-Public-Domain content pack)"
        )
    for slug in sorted(expected_set & found_set):
        cell = licence_rows[slug]
        want = expected_lic[slug]
        if cell != want:
            errs.append(
                f"{tag} ### Licences licence cell for `{slug}` is {cell!r}, "
                f"expected {want!r}"
            )

    return errs


def fail(errs: list[str], msg: str) -> None:
    errs.append(msg)


def main() -> int:
    errs: list[str] = []

    # 1. required files
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            fail(errs, f"[files] missing required file: {rel}")

    # collect text files. Exclude version-control and gitignored build/artifact dirs:
    # those never ship, and they legitimately contain source URLs (extracted source text
    # under sources/.build/) or QA snapshots (.playwright-mcp/) — scanning them is a
    # false positive against the link/leak policy, which only governs shippable content.
    # .planning/ is internal GSD workflow state that never ships (not in installers or the
    # packaged plugin) and legitimately holds research URLs as vetting evidence — same
    # precedent as sources/.build. .superpowers/ and docs/superpowers/ hold the same
    # class of ephemeral SDD/planning briefs (spec text quotes banned source URLs).
    SKIP_DIRS = {".git", "sources", ".build", ".playwright-mcp", "__pycache__",
                 ".worktrees", ".ruff_cache", ".pytest_cache", ".venv", "venv", ".idea", ".vscode",
                 ".planning", ".superpowers", "superpowers"}
    text_files = [p for p in ROOT.rglob("*")
                  if p.is_file() and p.suffix in {".md", ".py", ".json", ".yaml", ".yml", ".txt", ".sh", ".ps1"}
                  and not (SKIP_DIRS & set(p.parts))]

    # 2. leak sentinels (whole repo)
    for p in text_files:
        body = p.read_text(encoding="utf-8", errors="ignore")
        for s in LEAK_SENTINELS:
            if s in body:
                fail(errs, f"[leak] sentinel '{s}' found in {p.relative_to(ROOT)}")

    # 3. no source-material links (exclude pack chapter content — those are prose, but
    #    they are synthesized and should also be clean; include them to be strict)
    # ponytail: a "signpost" pack is pure citation — it MUST name where a spec lives, so it
    # is exempt from the link ban. Marked by `kind: signpost` in its SKILL.md frontmatter.
    signpost_dirs = {p.parent for p in ROOT.glob("packs/*/SKILL.md")
                     if re.search(r"^kind:\s*signpost\s*$", p.read_text(encoding="utf-8", errors="ignore"), re.M)}
    try:
        hosts = load_banned_hosts()
        source_hosts = re.compile(
            r"https?://[^\s)\"']*(" + "|".join(re.escape(t) for t in hosts) + ")"
        )
    except LinkPolicyDataError as e:
        fail(errs, f"[links-parity] {e}")
        source_hosts = None
    if source_hosts is not None:
        for p in text_files:
            if p.parent in signpost_dirs:
                continue
            body = p.read_text(encoding="utf-8", errors="ignore")
            m = source_hosts.search(body)
            if m:
                fail(errs, f"[links] source-material URL in {p.relative_to(ROOT)}: {m.group(0)}")

    # 4. version single-source
    versions = {}
    try:
        versions["plugin.json"] = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")).get("version", "")
    except Exception as e:
        fail(errs, f"[version] cannot read plugin.json: {e}")
    cl = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8") if (ROOT / "CHANGELOG.md").is_file() else ""
    m = re.search(r"^##\s*\[(\d+\.\d+\.\d+)\]", cl, re.M)
    versions["CHANGELOG.md"] = m.group(1) if m else ""
    ri = (ROOT / "RELEASE-INFO.txt").read_text(encoding="utf-8") if (ROOT / "RELEASE-INFO.txt").is_file() else ""
    m = re.search(r"Version:\s*([0-9]+\.[0-9]+\.[0-9]+)", ri)
    versions["RELEASE-INFO.txt"] = m.group(1) if m else ""
    # 4a. CR-01: the two website product YAMLs (RR-B-19 website sources) must carry
    # the release version too. Scoped to exactly these two paths; packs/*/PACK.yaml
    # uses source_version (different class) and docs carry keep-class history.
    expected = versions["RELEASE-INFO.txt"]
    for rel in ("docs/products/website/01-jgs-se-knowledge-packs.yaml",
                "docs/products/website/catalog.yaml"):
        body = (ROOT / rel).read_text(encoding="utf-8", errors="ignore") if (ROOT / rel).is_file() else ""
        m = re.search(r'version:\s*"([0-9]+\.[0-9]+\.[0-9]+)"', body)
        got = m.group(1) if m else ""
        if got != expected:
            fail(errs, f"[version] {rel}: website YAML version '{got}' "
                       f"!= RELEASE-INFO '{expected}'")
    distinct = {v for v in versions.values() if v}
    if len(distinct) > 1 or "" in versions.values():
        fail(errs, f"[version] disagreement / missing: {versions}")

    # 5. validate every pack
    sys.path.insert(0, str(ROOT / "tooling"))
    try:
        import validate_pack  # type: ignore
        packs = sorted(p for p in (ROOT / "packs").iterdir() if p.is_dir() and p not in signpost_dirs)
        for pack in packs:
            perrs = validate_pack.check_pack(pack)
            for e in perrs:
                fail(errs, f"[pack:{pack.name}] {e}")
    except Exception as e:
        fail(errs, f"[pack] validate_pack failed to run: {e}")
        packs = []

    # 5b. RR-S-13: every content pack's SKILL.md has a '## When to use' section and a
    #     prerequisites marker (skip signposts, which carry minimal frontmatter-only bodies).
    for pack in packs:
        skill = pack / "SKILL.md"
        if not skill.is_file():
            continue
        body = skill.read_text(encoding="utf-8", errors="ignore")
        if not re.search(r"^##\s*When to use\s*$", body, re.M | re.I):
            fail(errs, f"[rr-s-13:{pack.name}] SKILL.md missing '## When to use' section")
        if not re.search(r"Prerequisites|Requirements|^compatibility:", body, re.M | re.I):
            fail(errs, f"[rr-s-13:{pack.name}] SKILL.md missing a prerequisites marker")

    # 5c. RR-B-30: docs/packs.html exists, is em-dash-free, and matches a fresh
    #     generation from SKILLS.md (generated artifact must not drift, RR-B-00).
    #     The "no third-party asset" half of RR-B-30 is enforced by check 12
    #     ([html-assets]) below, which scans docs/packs.html like every page.
    packs_html = ROOT / "docs" / "packs.html"
    if not packs_html.is_file():
        fail(errs, "[rr-b-30] docs/packs.html missing")
    else:
        ph = packs_html.read_text(encoding="utf-8")
        if "—" in ph:
            fail(errs, "[rr-b-30] docs/packs.html contains an em dash")
        try:
            import gen_packs_page  # type: ignore
            fresh = gen_packs_page.render(gen_packs_page.parse_skills(), gen_packs_page.version())
            if fresh != ph:
                fail(errs, "[rr-b-30] docs/packs.html is stale; rerun tooling/gen_packs_page.py")
        except Exception as e:
            fail(errs, f"[rr-b-30] cannot verify packs.html generation: {e}")

    # 12. html-assets (P12): every docs/*.html page is self-contained. External
    #     http(s) assets must sit on an exact FIRST_PARTY_HOSTS host with empty
    #     userinfo; data: URIs and relative paths are allowed; protocol-relative
    #     //host/x fails; zero pages fails closed. docs-level glob only (not
    #     rglob) so docs/superpowers/ planning files stay out of scope.
    html_pages = sorted((ROOT / "docs").glob("*.html"))
    if not html_pages:
        fail(errs, "[html-assets] no docs/*.html found")
    for page in html_pages:
        for url in scan_html_external_assets(page.read_text(encoding="utf-8", errors="ignore")):
            fail(errs, f"[html-assets] external asset in "
                       f"{page.relative_to(ROOT).as_posix()}: {url}")

    # 12b. brand-token parity (P13): the exclusive BRAND-TOKENS slice extracted
    #     from docs/index.html must appear verbatim in docs/packs.html. A miss
    #     means the generated page is stale against the token source of truth.
    try:
        index_html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        brand_block = slice_brand_tokens(index_html)
        packs_text = (ROOT / "docs" / "packs.html").read_text(encoding="utf-8")
        if brand_block not in packs_text:
            fail(errs, "[brand-tokens] docs/packs.html does not carry the index.html "
                       "brand token block verbatim; rerun tooling/gen_packs_page.py")
    except ValueError as e:
        fail(errs, f"[brand-tokens] {e}")
    except OSError as e:
        fail(errs, f"[brand-tokens] cannot read page: {e}")

    # 13. catalogue-count (P15): live packs/ N+M must equal landing §06 headline,
    #     chip COUNTs (with Signposts chip), figcaption, and still-catalogue.svg
    #     subtitle/footer. Family membership and SVG row counts are review-only.
    try:
        index_for_cat = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
    except OSError as e:
        fail(errs, f"[catalogue-count] cannot read docs/index.html: {e}")
        index_for_cat = ""
    svg_path = ROOT / STILL_CATALOGUE_SVG
    svg_missing = not svg_path.is_file()
    svg_text = None
    if not svg_missing:
        try:
            svg_text = svg_path.read_text(encoding="utf-8")
        except OSError as e:
            fail(errs, f"[catalogue-count] cannot read {STILL_CATALOGUE_SVG}: {e}")
            svg_missing = True
    if index_for_cat:
        for msg in check_catalogue_count(
            ROOT / "packs", index_for_cat, svg_text, svg_missing=svg_missing
        ):
            fail(errs, msg)

    # 14. catalog-live-set (P16): content pack slug set must equal catalog.json
    #     packs[].slug where status is live or absent; signposts stay out of packs[].
    catalog_obj: dict | None = None
    catalog_err: str | None = None
    catalog_path = ROOT / CATALOG_JSON_PATH
    if not catalog_path.is_file():
        catalog_err = f"missing {CATALOG_JSON_PATH}"
    else:
        try:
            raw = json.loads(catalog_path.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                catalog_obj = raw
            else:
                catalog_err = f"{CATALOG_JSON_PATH} root must be an object"
        except (OSError, json.JSONDecodeError) as e:
            catalog_err = f"cannot read/parse {CATALOG_JSON_PATH}: {e}"
    for msg in check_catalog_live_set(ROOT / "packs", catalog_obj, catalog_err):
        fail(errs, msg)

    # 15. routing map coverage ([routing-map], /se)
    errs.extend(check_routing_map(ROOT / "packs"))

    # 6. SKILLS.md entry count == pack count
    skills = (ROOT / "SKILLS.md").read_text(encoding="utf-8") if (ROOT / "SKILLS.md").is_file() else ""
    signpost_names = {d.name for d in signpost_dirs}
    entry_slugs = re.findall(r"\[`([^`]+)`\]\(packs/", skills)
    entry_count = len([s for s in entry_slugs if s not in signpost_names])
    if packs and entry_count != len(packs):
        fail(errs, f"[index] SKILLS.md lists {entry_count} packs but {len(packs)} are shipped")

    # 6b. Cursor marketplace manifest lists every commercially-redistributable pack
    #     (MA-01 backstop: plugin.json skills must not drift behind packs/*/SKILL.md).
    cursor_plugin = ROOT / ".cursor-plugin" / "plugin.json"
    if cursor_plugin.is_file():
        try:
            cursor = json.loads(cursor_plugin.read_text(encoding="utf-8"))
            skills_list = cursor.get("skills")
            if not isinstance(skills_list, list):
                fail(errs, "[cursor] .cursor-plugin/plugin.json missing skills array")
            else:
                all_skill_dirs = sorted(
                    p.parent for p in (ROOT / "packs").glob("*/SKILL.md")
                )
                nc_packs = {
                    p.name for p in all_skill_dirs
                    if (p / "PACK.yaml").is_file()
                    and "commercial_use: false" in (p / "PACK.yaml").read_text(
                        encoding="utf-8", errors="ignore"
                    )
                }
                pack_slugs = {p.name for p in all_skill_dirs} - nc_packs
                cursor_slugs = set()
                for s in skills_list:
                    if not isinstance(s, str):
                        continue
                    # paths look like ./packs/<slug>/SKILL.md (normalize separators)
                    m = re.search(r"packs[/\\]([^/\\]+)[/\\]", s)
                    if m:
                        cursor_slugs.add(m.group(1))
                missing = sorted(pack_slugs - cursor_slugs)
                extra = sorted(cursor_slugs - pack_slugs)
                if len(cursor_slugs) != len(pack_slugs) or missing or extra:
                    detail = []
                    if missing:
                        detail.append(f"missing={missing}")
                    if extra:
                        detail.append(f"extra={extra}")
                    fail(
                        errs,
                        f"[cursor] manifest skills count {len(cursor_slugs)} "
                        f"!= eligible packs {len(pack_slugs)}"
                        + (f" ({'; '.join(detail)})" if detail else ""),
                    )
        except Exception as e:
            fail(errs, f"[cursor] cannot verify .cursor-plugin/plugin.json: {e}")

    # 5d. overlap (TOOL-20): multi-pack chapter-basename collisions (same process)
    try:
        import check_overlap  # type: ignore
        rc = check_overlap.main()
        if rc != 0:
            fail(errs, "[overlap] check_overlap.py failed (see output above)")
    except Exception as e:
        fail(errs, f"[overlap] check_overlap failed to run: {e}")

    # 5e. MAP-19-04: capability-pack map freshness (same process; prints its own counts)
    try:
        import check_capability_map  # type: ignore
        rc = check_capability_map.main()
        if rc != 0:
            fail(errs, "[map] check_capability_map.py failed (see output above)")
    except Exception as e:
        fail(errs, f"[map] check_capability_map failed to run: {e}")

    # 5f. classification-rules (MAP-21-01): every live chapter has a rule assignment
    try:
        import check_classification_rules  # type: ignore
        rc = check_classification_rules.main()
        if rc != 0:
            fail(
                errs,
                "[classification-rules] check_classification_rules.py failed "
                "(see output above)",
            )
    except Exception as e:
        fail(errs, f"[classification-rules] check_classification_rules failed to run: {e}")

    # 5g. MAP-21-05: generator replay --check against on-disk map (local/trusted)
    try:
        import generate_capability_map  # type: ignore
        map_path = ROOT / "docs" / "capability-pack-map.json"
        if not map_path.is_file():
            fail(errs, "[map-replay] docs/capability-pack-map.json missing")
        else:
            try:
                map_obj = json.loads(map_path.read_text(encoding="utf-8"))
            except Exception as e:
                fail(errs, f"[map-replay] cannot read capability-pack-map.json: {e}")
                map_obj = None
            if isinstance(map_obj, dict):
                disk_on = map_obj.get("generated_on")
                if not isinstance(disk_on, str) or not disk_on:
                    fail(
                        errs,
                        "[map-replay] capability-pack-map.json missing generated_on",
                    )
                else:
                    rc = generate_capability_map.main(
                        ["--generated-on", disk_on, "--check"]
                    )
                    if rc != 0:
                        fail(
                            errs,
                            "[map-replay] generate_capability_map.py --check failed "
                            "(see output above)",
                        )
            elif map_obj is not None:
                fail(
                    errs,
                    "[map-replay] capability-pack-map.json top-level must be an object",
                )
    except Exception as e:
        fail(errs, f"[map-replay] generate_capability_map failed to run: {e}")

    # 7. authored-file headers (root + docs + tooling + installers; NOT packs/)
    authored = [ROOT / "README.md", ROOT / "SECURITY.md", ROOT / "CODE_OF_CONDUCT.md",
                ROOT / "CHANGELOG.md", ROOT / "SKILLS.md", ROOT / "CONTRIBUTING.md",
                ROOT / "install.py", ROOT / "install.sh", ROOT / "install.ps1",
                ROOT / "tooling/validate_pack.py", ROOT / "tooling/build_pack.py",
                ROOT / "tooling/check_release.py",
                ROOT / "docs/LICENSING.md", ROOT / "docs/SOURCE-VETTING.md",
                ROOT / "docs/PACK-SPEC.md", ROOT / "docs/skill-usage.md"]
    for p in authored:
        if not p.is_file():
            continue
        head = p.read_text(encoding="utf-8", errors="ignore")[:600]
        if HEADER_SENTINEL not in head:
            fail(errs, f"[header] missing JGSC copyright header: {p.relative_to(ROOT)}")
        elif SPDX_SENTINEL not in head:
            fail(errs, f"[header] missing SPDX line: {p.relative_to(ROOT)}")

    # report
    if errs:
        print(f"RELEASE CHECK: FAIL ({len(errs)} issue(s))")
        for e in errs:
            print(f"  - {e}")
        return 1
    # PASS receipt: version + short sha of the exact commit the gate ran at, so
    # a pasted transcript is verifiable. Pre-tag rule (docstring): require the
    # sha to match the commit being tagged. `@ no-git` is distinct and can
    # never satisfy that match.
    version = versions["RELEASE-INFO.txt"]
    try:
        short_sha = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, cwd=ROOT, check=True,
        ).stdout.strip()
        receipt = f"v{version} @ {short_sha}"
    except Exception:
        receipt = f"v{version} @ no-git"
    print(f"RELEASE CHECK: PASS ({receipt})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

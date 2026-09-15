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

stdlib only. This is a LOCAL/trusted gate and may run repo code; the CI workflow
(.github/workflows/validate.yml) inlines its own checks and never executes repo code.
CI-covered: version, index, overlap, map/rules data invariants, html-assets. Local-only
required before tag: pack validation, packs.html freshness, full map/rules checks, replay.

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

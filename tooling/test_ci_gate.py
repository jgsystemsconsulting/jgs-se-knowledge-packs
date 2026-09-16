#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based probe for the six inline CI gates in .github/workflows/validate.yml.

Run:  python tooling/test_ci_gate.py
Exits 0 when regex literal parity, heredoc extraction, negative demos, and
positive clean-tree runs all hold. Any failed assert raises and exits nonzero.

The probe extracts each heredoc from the workflow by its pinned step name and
executes the shipped workflow text (not a copy of it), so workflow breakage
fails here too. Mirror-functions fallback: the P4 pattern would re-implement
the gates as local functions if extraction matched zero heredocs, but zero
extraction already fails this probe loudly, so the fallback is effectively
unreachable and no mirror lives in this file.

Regex parity pins (P4 pin-plus-parity, extended to the six pinned steps):
  - three version regexes, the SKILLS link regex, and the signpost regex must
    appear verbatim in both tooling/check_release.py and validate.yml
  - MAP_VERSION_RE / GENERATED_ON_RE must appear verbatim in validate.yml and
    both local twins (check_capability_map.py, check_classification_rules.py)
  - the html-assets host set, TAG_SLICE/ATTR/CSS_URL/CSS_IMPORT pattern text,
    and the meta image tokens plus the BRAND-TOKENS marker literals (P13) must
    appear verbatim in both check_release.py and validate.yml (HTML_ASSET_PAIR)
  - catalogue-count section marker, h2/chip/SVG regexes, SVG path, and tag
    (P15) must appear verbatim in both check_release.py and validate.yml
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOW = ROOT / ".github" / "workflows" / "validate.yml"
RELEASE_TWIN = ROOT / "tooling" / "check_release.py"
MAP_TWIN = ROOT / "tooling" / "check_capability_map.py"
RULES_TWIN = ROOT / "tooling" / "check_classification_rules.py"

# Extraction markers; byte-for-byte the `- name:` values in validate.yml.
PINNED_STEPS = [
    "Version single-source",
    "SKILLS index count",
    "Chapter basename overlap",
    "Map and classification data invariants",
    "HTML self-containment",
    "Landing catalogue counts",
]

# Literals that must appear verbatim in check_release.py AND validate.yml.
RELEASE_PAIR = [
    ("changelog version", r"^##\s*\[(\d+\.\d+\.\d+)\]"),
    ("RELEASE-INFO version", r"Version:\s*([0-9]+\.[0-9]+\.[0-9]+)"),
    ("website YAML version", r'version:\s*"([0-9]+\.[0-9]+\.[0-9]+)"'),
    ("SKILLS link", r"\[`([^`]+)`\]\(packs/"),
    ("signpost kind", r"^kind:\s*signpost\s*$"),
]

# Literals that must appear verbatim in check_release.py AND validate.yml
# ([html-assets] self-containment scan, P12). Byte parity is the drift control.
HTML_ASSET_PAIR = [
    ("first-party host (github)", '"github.com"'),
    ("first-party host (pages)", '"jgsystemsconsulting.github.io"'),
    ("TAG_SLICE element list",
     r"<(link|img|script|iframe|source|video|audio|embed|track|object|base|meta)\b"),
    ("TAG_SLICE quote-aware tail", r"(?:\"[^\"]*\"|'[^']*'|[^>])*>"),
    ("ATTR name groups",
     r"(?P<name>href|src|data|srcset|content|http-equiv|property|name)\s*=\s*"),
    ("ATTR value branches",
     r"""(?:"(?P<d>[^"]*)"|'(?P<s>[^']*)'|(?P<u>[^\s>]+))"""),
    ("CSS_URL", r"""url\(\s*(['"]?)([^)'"\s]+)\1\s*\)"""),
    ("CSS_IMPORT",
     r"""@import\s+(?:url\(\s*(['"]?)([^)'"\s]+)\1\s*\)|(['"])([^'"]+)\3)\s*;?"""),
    ("meta og:image", '"og:image"'),
    ("meta og:image:secure_url", '"og:image:secure_url"'),
    ("meta twitter:image", '"twitter:image"'),
    ("meta twitter:image:src", '"twitter:image:src"'),
    ("brand-tokens BEGIN marker", '"/* BRAND-TOKENS:BEGIN"'),
    ("brand-tokens END marker", '"/* BRAND-TOKENS:END"'),
]

# Literals that must appear verbatim in check_release.py AND validate.yml
# ([catalogue-count] landing honesty, P15). Byte parity is the drift control.
CATALOGUE_COUNT_PAIR = [
    ("catalogue section marker", '"<!-- §06 The catalogue -->"'),
    ("catalogue h2 pattern",
     r"<h2>\s*(\d+)\s+packs\s*(?:&middot;|·)\s*(\d+)\s+signposts\s*</h2>"),
    ("catalogue chip pattern", r'<div\s+class="pk"\s*>\s*<b>(.*?)</b>'),
    ("catalogue chip count pattern",
     r"^(?P<label>.*?)\s*(?:&middot;|·)\s*(?P<count>\d+)\s*$"),
    ("catalogue svg nm pattern",
     r"(\d+)\s+packs\s*(?:&middot;|·)\s*(\d+)\s+signposts"),
    ("still-catalogue svg path", '"docs/assets/still-catalogue.svg"'),
    ("catalogue-count tag", "[catalogue-count]"),
]

# Literals pinned per local twin (map/classification envelope).
MAP_VERSION_LITERAL = r're.compile(r"^\d+\.\d+\.\d+$")'
GENERATED_ON_LITERAL = r're.compile(r"^\d{4}-\d{2}-\d{2}$")'


def extract_heredoc(workflow_text: str, step_name: str) -> str | None:
    """Return the dedented python3 heredoc body under `- name: <step_name>`.

    Returns None when the pinned step line, its `python3 - <<'PY'` invocation,
    the `PY` terminator, or a non-empty body is missing.
    """
    lines = workflow_text.splitlines()
    for start, line in enumerate(lines):
        if line.strip() == f"- name: {step_name}":
            break
    else:
        return None
    for begin in range(start, len(lines)):
        if "python3 - <<'PY'" in lines[begin]:
            begin += 1
            break
    else:
        return None
    body: list[str] = []
    for line in lines[begin:]:
        if line.strip() == "PY":
            break
        body.append(line)
    else:
        return None  # unterminated heredoc
    if not any(l.strip() for l in body):
        return None
    return textwrap.dedent("\n".join(body)) + "\n"


def run_gate(body: str, cwd: Path) -> tuple[int, str]:
    """Run an extracted heredoc body with cwd set; return (returncode, output)."""
    proc = subprocess.run(
        [sys.executable, "-c", body],
        cwd=str(cwd),
        capture_output=True,
        text=True,
    )
    return proc.returncode, proc.stdout + proc.stderr


def write_tree(root: Path, files: dict[str, str]) -> None:
    for rel, content in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")


VERSION_BASE = {
    ".claude-plugin/plugin.json": '{"version": "1.2.3"}\n',
    "CHANGELOG.md": "# Changelog\n\n## [Unreleased]\n\n## [1.2.3]: 2026-01-01\n",
    "RELEASE-INFO.txt": "Version:    1.2.4\n",
    "docs/products/website/01-jgs-se-knowledge-packs.yaml": 'version: "1.2.3"\n',
    "docs/products/website/catalog.yaml": 'version: "1.2.3"\n',
}

SKILLS_FILTERED = (
    "# Skills\n\n"
    "- [`alpha`](packs/alpha/SKILL.md)\n"
    "- [`beta`](packs/beta/SKILL.md)\n"
    "- [`omg-signpost`](packs/omg-signpost/SKILL.md)\n"
)
SKILLS_ONE_LINK = (
    "# Skills\n\n"
    "- [`alpha`](packs/alpha/SKILL.md)\n"
    "- [`omg-signpost`](packs/omg-signpost/SKILL.md)\n"
)
SKILLS_CONTENT_ONLY = (
    "# Skills\n\n"
    "- [`alpha`](packs/alpha/SKILL.md)\n"
    "- [`beta`](packs/beta/SKILL.md)\n"
)
SIGNPOST_MARKED = "---\nname: omg-signpost\nkind: signpost\n---\nbody\n"
SIGNPOST_UNMARKED = "---\nname: omg-signpost\n---\nbody\n"


def index_tree(skills: str, signpost_skill: str) -> dict[str, str]:
    return {
        "SKILLS.md": skills,
        "packs/alpha/SKILL.md": "---\nname: alpha\n---\nbody\n",
        "packs/beta/SKILL.md": "---\nname: beta\n---\nbody\n",
        "packs/omg-signpost/SKILL.md": signpost_skill,
    }


def overlap_tree(with_whitelist_file: bool) -> dict[str, str]:
    files = {
        "packs/alpha/chapters/ch01-introduction.md": "intro\n",
        "packs/beta/chapters/ch01-introduction.md": "intro\n",
        "packs/alpha/chapters/ch09-shared.md": "shared\n",
        "packs/beta/chapters/ch09-shared.md": "shared\n",
    }
    if with_whitelist_file:
        files["tooling/overlap-whitelist.txt"] = "# intentional\nch01-introduction.md\n"
    return files


VALID_MAP = {
    "schema_version": 2,
    "map_version": "1.0.0",
    "generated_on": "2026-01-01",
    "clusters": [
        {"name": "C", "chapters": [{"pack": "alpha", "chapter": "ch01.md", "note": ""}]},
    ],
}
VALID_RULES = {
    "schema_version": 1,
    "map_version": "1.0.0",
    "generated_on": "2026-01-01",
    "cluster_names": ["C"],
    "signpost_packs": [],
    "support_policy": "p",
    "rules_of_construction": ["r"],
    "support_filenames": ["glossary.md", "patterns.md", "cheatsheet.md"],
    "assignments": [
        {"pack": "alpha", "chapter": "ch01.md", "cluster": "C", "is_support": False},
    ],
}


def map_rules_tree(
    map_obj: dict | None = None,
    rules_obj: dict | None = None,
    extra_disk: list[str] | None = None,
) -> dict[str, str]:
    files: dict[str, str] = {"packs/alpha/chapters/ch01.md": "a\n"}
    for rel in extra_disk or []:
        files[rel] = "x\n"
    files["docs/capability-pack-map.json"] = json.dumps(map_obj or VALID_MAP)
    files["docs/classification-rules.json"] = json.dumps(rules_obj or VALID_RULES)
    return files


HTML_CLEAN_PAGE = (
    '<!doctype html>\n'
    '<link rel="icon" href="data:image/svg+xml,%3Csvg '
    "xmlns='http://www.w3.org/2000/svg'%3E\">\n"
    '<link rel="canonical" href="https://jgsystemsconsulting.github.io/jgs-se-knowledge-packs/">\n'
    '<img src="https://github.com/jgs-se/asset/raw/main/og.png" alt="hero">\n'
    "<style>@font-face{src:url('fonts/Inter-Regular.woff2')}\n"
    '@import "css/site.css";</style>\n'
    "<style>\n"
    "/* BRAND-TOKENS:BEGIN (single source; tooling/gen_packs_page.py copies this verbatim) */\n"
    ":root{--ink:#0a0a0b;--paper:#f4f2ec}\n"
    "/* BRAND-TOKENS:END */\n"
    "</style>\n"
)

BRAND_SLICE = ":root{--ink:#0a0a0b;--paper:#f4f2ec}\n"


def main() -> int:
    workflow_text = WORKFLOW.read_text(encoding="utf-8")
    release_text = RELEASE_TWIN.read_text(encoding="utf-8")

    # 1. literal parity: the drift control comes first, it is the cheapest check
    for name, literal in RELEASE_PAIR:
        assert literal in release_text, (
            "regex drifted between check_release.py and validate.yml; sync them: "
            f"{name} missing from check_release.py"
        )
        assert literal in workflow_text, (
            "regex drifted between check_release.py and validate.yml; sync them: "
            f"{name} missing from validate.yml"
        )
    for name, literal in (
        ("MAP_VERSION_RE", MAP_VERSION_LITERAL),
        ("GENERATED_ON_RE", GENERATED_ON_LITERAL),
    ):
        assert literal in MAP_TWIN.read_text(encoding="utf-8"), (
            "regex drifted between validate.yml and check_capability_map.py; "
            f"sync them: {name} missing from check_capability_map.py"
        )
        assert literal in RULES_TWIN.read_text(encoding="utf-8"), (
            "regex drifted between validate.yml and check_classification_rules.py; "
            f"sync them: {name} missing from check_classification_rules.py"
        )
        assert literal in workflow_text, (
            "regex drifted between validate.yml and "
            "check_capability_map.py / check_classification_rules.py; sync them: "
            f"{name} missing from validate.yml"
        )

    for name, literal in HTML_ASSET_PAIR:
        assert literal in release_text, (
            "regex drifted between check_release.py and validate.yml; sync them: "
            f"{name} missing from check_release.py"
        )
        assert literal in workflow_text, (
            "regex drifted between check_release.py and validate.yml; sync them: "
            f"{name} missing from validate.yml"
        )

    for name, literal in CATALOGUE_COUNT_PAIR:
        assert literal in release_text, (
            "regex drifted between check_release.py and validate.yml; sync them: "
            f"{name} missing from check_release.py"
        )
        assert literal in workflow_text, (
            "regex drifted between check_release.py and validate.yml; sync them: "
            f"{name} missing from validate.yml"
        )

    # 2. extraction of the shipped heredocs by pinned step name
    bodies: dict[str, str] = {}
    for step in PINNED_STEPS:
        body = extract_heredoc(workflow_text, step)
        assert body is not None, (
            f"extraction failed: pinned step '{step}' has no python3 heredoc in "
            ".github/workflows/validate.yml; the probe runs the shipped workflow "
            "text, so fix the step name or the heredoc markers"
        )
        bodies[step] = body
    assert len(bodies) == len(PINNED_STEPS), "expected exactly six pinned heredocs"

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)

        def demo(files: dict[str, str], step: str, expect: str, label: str) -> None:
            d = tmp / label
            write_tree(d, files)
            rc, out = run_gate(bodies[step], d)
            assert rc != 0, f"{label}: expected failure, got exit 0\n{out}"
            assert expect in out, f"{label}: expected {expect!r} in output\n{out}"

        def demo_ok(files: dict[str, str], step: str, label: str) -> None:
            d = tmp / label
            write_tree(d, files)
            rc, out = run_gate(bodies[step], d)
            assert rc == 0, f"{label}: expected exit 0\n{out}"

        # version: plugin.json vs RELEASE-INFO disagreement
        demo(VERSION_BASE, "Version single-source",
             "[version] disagreement / missing", "version-disagreement")
        # version: missing website YAML version line
        v2 = dict(VERSION_BASE)
        v2["RELEASE-INFO.txt"] = "Version:    1.2.3\n"
        v2["docs/products/website/01-jgs-se-knowledge-packs.yaml"] = "title: x\n"
        demo(v2, "Version single-source",
             "website YAML version '' != RELEASE-INFO '1.2.3'",
             "version-website-missing")

        # index: with the signpost marker, the signpost link is NOT counted,
        # so one content link vs two shipped packs fails
        demo(index_tree(SKILLS_ONE_LINK, SIGNPOST_MARKED), "SKILLS index count",
             "[index] SKILLS.md lists 1 packs but 2 are shipped", "index-mismatch")
        # index positive: the signpost link is filtered and the count matches
        demo_ok(index_tree(SKILLS_FILTERED, SIGNPOST_MARKED),
                "SKILLS index count", "index-filter-ok")
        # index negative: signpost pack present but NOT marked, so the filter
        # must not drop it from the shipped count
        demo(index_tree(SKILLS_CONTENT_ONLY, SIGNPOST_UNMARKED), "SKILLS index count",
             "[index] SKILLS.md lists 2 packs but 3 are shipped",
             "index-signpost-unmarked")

        # overlap: an un-whitelisted shared basename fails with both packs
        demo(overlap_tree(True), "Chapter basename overlap",
             "[overlap] ch09-shared.md: alpha, beta", "overlap-collision")
        # overlap: a missing whitelist data file fails closed
        demo(overlap_tree(False), "Chapter basename overlap",
             "[overlap] whitelist data file", "overlap-missing-file")
        # overlap positive: the whitelisted ch01-introduction.md collision passes
        demo_ok({
            "tooling/overlap-whitelist.txt": "ch01-introduction.md\n",
            "packs/alpha/chapters/ch01-introduction.md": "i\n",
            "packs/beta/chapters/ch01-introduction.md": "i\n",
        }, "Chapter basename overlap", "overlap-whitelisted-ok")

        # map: an on-disk chapter missing from the map fails on the disk side
        demo(map_rules_tree(extra_disk=["packs/alpha/chapters/ch02.md"]),
             "Map and classification data invariants",
             "[map-data] chapter-set: on disk not in map: alpha/ch02.md",
             "map-missing-chapter")
        # rules: an assignment row pointing at a nonexistent file
        r1 = json.loads(json.dumps(VALID_RULES))
        r1["assignments"].append(
            {"pack": "alpha", "chapter": "ch09-missing.md", "cluster": "C",
             "is_support": False}
        )
        demo(map_rules_tree(rules_obj=r1), "Map and classification data invariants",
             "coverage: assignment has no on-disk chapter: "
             "packs/alpha/chapters/ch09-missing.md", "rules-phantom-assignment")
        # rules: wrong schema_version
        r2 = json.loads(json.dumps(VALID_RULES))
        r2["schema_version"] = 2
        demo(map_rules_tree(rules_obj=r2), "Map and classification data invariants",
             "schema_version must be int 1, got 2", "rules-schema")
        # rules/map: generated_on mismatch between the two files
        r3 = json.loads(json.dumps(VALID_RULES))
        r3["generated_on"] = "2026-01-02"
        demo(map_rules_tree(rules_obj=r3), "Map and classification data invariants",
             "generated_on mismatch: map '2026-01-01' != rules '2026-01-02'",
             "rules-date-mismatch")

        # html-assets: an external img fails with a file-tagged annotation
        demo({"docs/index.html":
              '<!doctype html>\n<img src="https://cdn.example/track.png">\n'},
             "HTML self-containment",
             "[html-assets] external asset in docs/index.html", "html-external-img")
        # html-assets: protocol-relative src fails
        demo({"docs/index.html": '<script src="//cdn.example/x.js"></script>\n'},
             "HTML self-containment",
             "[html-assets] external asset in docs/index.html: //cdn.example/x.js",
             "html-protocol-relative")
        # html-assets: zero pages fails closed
        demo({"README.md": "x\n"}, "HTML self-containment",
             "[html-assets] no docs/*.html found", "html-zero-files")
        # html-assets: data URI, relative fonts/@import, and allowlisted hosts pass;
        # brand-token parity holds when packs.html carries the index.html slice
        demo_ok({"docs/index.html": HTML_CLEAN_PAGE,
                 "docs/packs.html": "<style>\n" + BRAND_SLICE + "</style>\n"},
                "HTML self-containment", "html-clean-ok")
        # brand-tokens: a hand-edited hex in the packs.html copy fails
        demo({"docs/index.html": HTML_CLEAN_PAGE,
              "docs/packs.html": "<style>:root{--ink:#0b0b0c;--paper:#f4f2ec}</style>\n"},
             "HTML self-containment",
             "[brand-tokens] docs/packs.html does not carry the index.html brand "
             "token block verbatim", "html-brand-drift")
        # brand-tokens: missing markers fail [brand-tokens], not a crash
        demo({"docs/index.html":
              "<!doctype html>\n<style>:root{--ink:#0a0a0b}</style>\n"},
             "HTML self-containment",
             "[brand-tokens] expected exactly one BRAND-TOKENS BEGIN",
             "html-brand-markers-missing")

        # catalogue-count: stale h2 (62 packs) fails live-versus-stated
        cat_pack = (
            "---\nname: alpha\ndescription: x\n---\n# alpha\n"
        )
        cat_index_stale = (
            "<!-- §06 The catalogue -->\n"
            "<section><div class=\"wrap\">\n"
            "  <h2>62 packs &middot; 0 signposts</h2>\n"
            "  <div class=\"packs\">\n"
            "    <div class=\"pk\"><b>Demo &middot; 1</b><span>one pack</span></div>\n"
            "    <div class=\"pk\"><b>Signposts &middot; 0</b><span>none</span></div>\n"
            "  </div>\n"
            "  <figcaption>FIG.06 · 1 packs plus 0 signposts across open sources; "
            "filter the full list on packs.html.</figcaption>\n"
            "</div></section>\n"
            "<!-- §07 Licensing -->\n"
        )
        cat_svg_ok = (
            '<svg xmlns="http://www.w3.org/2000/svg">\n'
            '<text>1 packs  ·  0 signposts  ·  open sources only</text>\n'
            '<text>1 PACKS · 0 SIGNPOSTS · FILTER ON packs.html</text>\n'
            "</svg>\n"
        )
        demo({
            "packs/alpha/SKILL.md": cat_pack,
            "docs/index.html": cat_index_stale,
            "docs/assets/still-catalogue.svg": cat_svg_ok,
        }, "Landing catalogue counts",
             "[catalogue-count] §06 h2 states 62 packs / 0 signposts "
             "but live inventory is 1 packs / 0 signposts",
             "catalogue-stale-h2")

    # 3. positive runs against the real repo tree: what CI sees on a clean tree
    for step in PINNED_STEPS:
        rc, out = run_gate(bodies[step], ROOT)
        assert rc == 0, (
            f"positive run against the real tree failed for '{step}':\n{out}"
        )

    print("ci-gate probe: OK (parity, extraction, negative demos, positive runs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

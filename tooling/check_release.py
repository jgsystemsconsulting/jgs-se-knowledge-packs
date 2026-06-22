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
  4. Version single-source agreement: plugin.json == CHANGELOG top == RELEASE-INFO.txt.
  5. Every pack passes tooling/validate_pack.py (structure + licence tier).
  6. SKILLS.md entry count == number of shipped packs.
  7. JGSC + SPDX header present on authored files (NOT pack content).

stdlib only. This is a LOCAL/trusted gate and may run repo code; the CI workflow
(.github/workflows/validate.yml) inlines its own checks and never executes repo code.

Usage:  python tooling/check_release.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "LICENSE", "COPYRIGHT", "NOTICE", "README.md", "CHANGELOG.md", "SECURITY.md",
    "CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "SKILLS.md", "RELEASE-INFO.txt",
    ".gitignore", "catalog.json",
    ".claude-plugin/marketplace.json", ".claude-plugin/plugin.json",
    "install.py", "install.sh", "install.ps1",
    "docs/SOURCE-VETTING.md", "docs/PACK-SPEC.md", "docs/LICENSING.md", "docs/skill-usage.md",
    "tooling/validate_pack.py", "tooling/build_pack.py",
]

# Assembled from fragments so this scanner file does not flag itself as a leak.
_PK = "PRIVATE" + " KEY"
LEAK_SENTINELS = ["CONFI" + "DENTIAL", "BEGIN " + _PK, "BEGIN OPENSSH " + _PK, "BEGIN RSA " + _PK]

# Source-material hosts that must never appear as published links (link policy).
SOURCE_HOSTS = re.compile(r"https?://[^\s)\"']*(sebokwiki|nasa\.gov|ntrs|nist\.gov|govinfo\.gov|omg\.org|ocw\.mit|dodcio|dod\.mil|dla\.mil|eur-lex|europa\.eu|nato\.int|dau\.edu)")

# Authored-file header sentinels (RR-B-03/04) — checked on JGSC-authored files only,
# never on pack content (which carries the source's licence).
HEADER_SENTINEL = "Copyright (c) 2026 JG Systems Consulting Ltd."
SPDX_SENTINEL = "SPDX-License-Identifier: MIT"


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
    SKIP_DIRS = {".git", "sources", ".build", ".playwright-mcp", "__pycache__",
                 ".worktrees", ".ruff_cache", ".pytest_cache", ".venv", "venv", ".idea", ".vscode"}
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
    for p in text_files:
        if p.parent in signpost_dirs:
            continue
        body = p.read_text(encoding="utf-8", errors="ignore")
        m = SOURCE_HOSTS.search(body)
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

    # 6. SKILLS.md entry count == pack count
    skills = (ROOT / "SKILLS.md").read_text(encoding="utf-8") if (ROOT / "SKILLS.md").is_file() else ""
    signpost_names = {d.name for d in signpost_dirs}
    entry_slugs = re.findall(r"\[`([^`]+)`\]\(packs/", skills)
    entry_count = len([s for s in entry_slugs if s not in signpost_names])
    if packs and entry_count != len(packs):
        fail(errs, f"[index] SKILLS.md lists {entry_count} packs but {len(packs)} are shipped")

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
    print("RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

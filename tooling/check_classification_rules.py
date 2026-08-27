#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
check_classification_rules.py — validate docs/classification-rules.json (MAP-21-01).

Checks every packs/*/chapters/*.md file has a non-support assignment, assignment
shape, uniqueness, signpost guard, and support-row file existence. Stdlib only.
Invoked by check_release.py (local/trusted; CI does not exec repo Python).
This is MAP-21-01 input validation, not a generator.

Usage:  python tooling/check_classification_rules.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES_PATH = ROOT / "docs" / "classification-rules.json"
MAP_PATH = ROOT / "docs" / "capability-pack-map.json"
PACKS_ROOT = ROOT / "packs"
SUPPORT_SUFFIX = " (support file)"
MAP_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
GENERATED_ON_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def fail(errs: list[str], msg: str) -> None:
    errs.append(msg)


def check_rules(data: dict, packs_root: Path | None = None) -> list[str]:
    """Validate a rules object against packs_root (default PACKS_ROOT)."""
    errs: list[str] = []
    if packs_root is None:
        packs_root = PACKS_ROOT

    if not isinstance(data, dict):
        fail(errs, "envelope: top-level JSON must be an object")
        return errs

    schema = data.get("schema_version")
    if schema is None:
        fail(errs, "envelope: missing schema_version (expected int 1)")
    elif not isinstance(schema, int) or isinstance(schema, bool) or schema != 1:
        fail(errs, f"envelope: schema_version must be int 1, got {schema!r}")

    map_version = data.get("map_version")
    if not map_version:
        fail(errs, "envelope: missing or empty map_version")
    elif not isinstance(map_version, str) or not MAP_VERSION_RE.fullmatch(map_version):
        fail(errs, f"envelope: map_version must match N.N.N, got {map_version!r}")

    generated_on = data.get("generated_on")
    if not generated_on:
        fail(errs, "envelope: missing or empty generated_on")
    elif not isinstance(generated_on, str) or not GENERATED_ON_RE.fullmatch(generated_on):
        fail(errs, f"envelope: generated_on must match YYYY-MM-DD, got {generated_on!r}")

    support_policy = data.get("support_policy")
    if not isinstance(support_policy, str) or not support_policy.strip():
        fail(errs, "envelope: support_policy must be a non-empty string")

    roc = data.get("rules_of_construction")
    if not isinstance(roc, list) or not roc or not all(isinstance(x, str) and x for x in roc):
        fail(errs, "envelope: rules_of_construction must be a non-empty list of strings")

    support_filenames = data.get("support_filenames")
    expected_support = ["glossary.md", "patterns.md", "cheatsheet.md"]
    if support_filenames != expected_support:
        fail(
            errs,
            f"envelope: support_filenames must be {expected_support!r}, got {support_filenames!r}",
        )

    signpost_packs = data.get("signpost_packs")
    if not isinstance(signpost_packs, list):
        fail(errs, "envelope: signpost_packs must be a list")
        signpost_packs = []
    signpost_set = {s for s in signpost_packs if isinstance(s, str)}

    cluster_names = data.get("cluster_names")
    if not isinstance(cluster_names, list) or not all(
        isinstance(n, str) and n for n in cluster_names
    ):
        fail(errs, "envelope: cluster_names must be a list of non-empty strings")
        cluster_names = []
    cluster_name_set = set(cluster_names)

    assignments = data.get("assignments")
    if not isinstance(assignments, list):
        fail(errs, "envelope: assignments must be a list")
        return errs

    seen: set[tuple[str, str]] = set()
    non_support: set[tuple[str, str]] = set()
    for i, entry in enumerate(assignments):
        if not isinstance(entry, dict):
            fail(errs, f"assignments[{i}]: not an object")
            continue
        pack = entry.get("pack")
        chapter = entry.get("chapter")
        cluster = entry.get("cluster")
        is_support = entry.get("is_support")
        if not isinstance(pack, str) or not pack:
            fail(errs, f"assignments[{i}]: pack must be a non-empty string")
            continue
        if not isinstance(chapter, str) or not chapter:
            fail(errs, f"assignments[{i}]: chapter must be a non-empty string")
            continue
        if SUPPORT_SUFFIX in chapter or chapter.endswith(SUPPORT_SUFFIX.strip()):
            fail(
                errs,
                f"assignments[{i}]: chapter must not contain support-file suffix: {chapter!r}",
            )
        if "/" in chapter or "\\" in chapter:
            fail(errs, f"assignments[{i}]: chapter must be a basename, got {chapter!r}")
        if not isinstance(cluster, str) or cluster not in cluster_name_set:
            fail(
                errs,
                f"assignments[{i}]: cluster {cluster!r} not in cluster_names "
                f"(pack={pack}, chapter={chapter})",
            )
        if type(is_support) is not bool:
            fail(
                errs,
                f"assignments[{i}]: is_support must be bool, got {is_support!r}",
            )
            continue
        key = (pack, chapter)
        if key in seen:
            fail(errs, f"uniqueness: duplicate (pack, chapter): {pack}/{chapter}")
        else:
            seen.add(key)
        if pack in signpost_set:
            fail(errs, f"signpost: assignment for signpost pack {pack!r} ({chapter})")
        if is_support is True:
            if chapter not in expected_support:
                fail(
                    errs,
                    f"support: chapter {chapter!r} not in support_filenames "
                    f"(pack={pack})",
                )
            rel_path = Path(chapter)
            if (
                ".." in rel_path.parts
                or rel_path.is_absolute()
                or "/" in chapter
                or "\\" in chapter
            ):
                fail(
                    errs,
                    f"support: path rejected (must be plain filename at pack root): "
                    f"{chapter!r} (pack={pack})",
                )
            else:
                path = packs_root / pack / chapter
                if not path.is_file():
                    fail(
                        errs,
                        f"support: missing file packs/{pack}/{chapter}",
                    )
        elif is_support is False:
            non_support.add(key)
            path = packs_root / pack / "chapters" / chapter
            if not path.is_file():
                fail(
                    errs,
                    f"coverage: assignment has no on-disk chapter: "
                    f"packs/{pack}/chapters/{chapter}",
                )

    # Live-chapter coverage: every packs/*/chapters/*.md needs is_support false row
    if packs_root.is_dir():
        for path in sorted(packs_root.glob("*/chapters/*.md")):
            pack = path.parent.parent.name
            chapter = path.name
            if (pack, chapter) not in non_support:
                fail(
                    errs,
                    f"coverage: on-disk chapter has no assignment: {pack}/{chapter}",
                )

    # Fidelity vs live capability-pack-map.json (independent load; no import)
    if not MAP_PATH.is_file():
        fail(errs, f"fidelity: map file missing: {MAP_PATH.relative_to(ROOT).as_posix()}")
        return errs
    try:
        with MAP_PATH.open(encoding="utf-8") as fh:
            live = json.load(fh)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        fail(errs, f"fidelity: JSON decode error in map: {exc}")
        return errs
    if not isinstance(live, dict):
        fail(errs, "fidelity: map top-level must be an object")
        return errs

    live_schema = live.get("schema_version")
    if not isinstance(live_schema, int) or isinstance(live_schema, bool) or live_schema != 2:
        fail(errs, f"fidelity: live map schema_version must be int 2, got {live_schema!r}")

    live_mv = live.get("map_version")
    if live_mv != map_version:
        fail(
            errs,
            f"fidelity: rules map_version {map_version!r} != live map {live_mv!r}",
        )

    live_clusters = live.get("clusters")
    if not isinstance(live_clusters, list):
        fail(errs, "fidelity: live map missing clusters list")
        return errs

    live_names = []
    for c in live_clusters:
        if isinstance(c, dict) and isinstance(c.get("name"), str):
            live_names.append(c["name"])
        else:
            fail(errs, "fidelity: live cluster entry missing name")
            live_names.append("<unnamed>")

    if cluster_names != live_names:
        fail(
            errs,
            f"fidelity: cluster_names must equal live clusters[].name in order "
            f"(rules_len={len(cluster_names)}, live_len={len(live_names)})",
        )
        for i, (a, b) in enumerate(zip(cluster_names, live_names)):
            if a != b:
                fail(errs, f"fidelity: cluster_names[{i}] {a!r} != live {b!r}")
                break
        if len(cluster_names) != len(live_names):
            fail(
                errs,
                f"fidelity: cluster_names length {len(cluster_names)} != "
                f"live {len(live_names)}",
            )

    expected_signposts = ["omg-signpost", "se-standards-signpost"]
    if list(signpost_packs) != expected_signposts:
        fail(
            errs,
            f"fidelity: signpost_packs must be {expected_signposts!r}, "
            f"got {signpost_packs!r}",
        )

    mkeys: dict[tuple[str, str], tuple[str, bool]] = {}
    for c in live_clusters:
        if not isinstance(c, dict):
            continue
        cname = c.get("name")
        if not isinstance(cname, str):
            continue
        chapters = c.get("chapters")
        if not isinstance(chapters, list):
            continue
        for ch in chapters:
            if not isinstance(ch, dict):
                continue
            pack = ch.get("pack")
            raw = ch.get("chapter")
            if not isinstance(pack, str) or not isinstance(raw, str):
                continue
            is_s = raw.endswith(SUPPORT_SUFFIX)
            base = raw[: -len(SUPPORT_SUFFIX)] if is_s else raw
            mkeys[(pack, base)] = (cname, is_s)

    akeys: dict[tuple[str, str], tuple[str, bool]] = {}
    for entry in assignments:
        if not isinstance(entry, dict):
            continue
        pack = entry.get("pack")
        chapter = entry.get("chapter")
        cluster = entry.get("cluster")
        is_support = entry.get("is_support")
        if (
            isinstance(pack, str)
            and isinstance(chapter, str)
            and isinstance(cluster, str)
            and type(is_support) is bool
        ):
            akeys[(pack, chapter)] = (cluster, is_support)

    only_rules = sorted(set(akeys) - set(mkeys))
    only_map = sorted(set(mkeys) - set(akeys))
    if only_rules or only_map:
        fail(
            errs,
            f"fidelity: key-set mismatch (rules_only={len(only_rules)}, "
            f"map_only={len(only_map)})",
        )
        for pack, chapter in only_rules[:10]:
            fail(errs, f"fidelity: in rules not in map: {pack}/{chapter}")
        for pack, chapter in only_map[:10]:
            fail(errs, f"fidelity: in map not in rules: {pack}/{chapter}")

    for key, (cluster, is_s) in akeys.items():
        if key not in mkeys:
            continue
        m_cluster, m_is_s = mkeys[key]
        pack, chapter = key
        if cluster != m_cluster:
            fail(
                errs,
                f"fidelity: cluster mismatch for {pack}/{chapter}: "
                f"rules={cluster!r} map={m_cluster!r}",
            )
        if is_s != m_is_s:
            fail(
                errs,
                f"fidelity: is_support mismatch for {pack}/{chapter}: "
                f"rules={is_s!r} map={m_is_s!r}",
            )

    return errs


def main() -> int:
    if not RULES_PATH.is_file():
        print(f"FAIL: rules file missing: {RULES_PATH.relative_to(ROOT).as_posix()}")
        return 1

    try:
        with RULES_PATH.open(encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        print(
            f"FAIL: JSON decode error in {RULES_PATH.relative_to(ROOT).as_posix()}: {exc}"
        )
        return 1

    if not isinstance(data, dict):
        print("FAIL: 1 issue(s)")
        print("  - envelope: top-level JSON must be an object")
        return 1

    errs = check_rules(data)
    if errs:
        print(f"FAIL: {len(errs)} issue(s)")
        for msg in errs:
            print(f"  - {msg}")
        return 1
    print("PASS: classification rules OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

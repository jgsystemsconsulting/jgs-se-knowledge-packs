#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
check_capability_map.py — validate docs/capability-pack-map.json for agent consumption.

Checks:
  1. v2 envelope (schema_version==2, map_version, generated_on present).
  2. Pack/chapter staleness vs packs/ (both directions; support-file rows excluded
     from chapter-set equality; signpost packs have no chapters/ and are ignored).
  3. File existence for every map entry (support files at pack root; chapters under
     packs/<pack>/chapters/).
  4. (pack, chapter) uniqueness across all entries; per-cluster counts printed.
  5. Name-keyed threshold minimums for thin clusters (never by array index).

stdlib only. Invoked by check_release.py (local/trusted); CI still does not exec repo Python.

Usage:  python tooling/check_capability_map.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP_PATH = ROOT / "docs" / "capability-pack-map.json"
SUPPORT_SUFFIX = " (support file)"
MAP_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
GENERATED_ON_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Thresholds resolve by cluster NAME so renames fail loudly (unknown name → non-zero).
THRESHOLDS: dict[str, int] = {
    "Training & Documentation Delivery": 1,
    "Requirements Traceability & Allocation": 3,
    "Interface Management & ICIDs": 4,
    "Opportunity/Benefit Management": 2,
    "Decision Analysis & Trade Studies": 4,
    "Validation": 4,
    "Integration": 4,
    "Operations, Maintenance & Disposal": 4,
}


def fail(errs: list[str], msg: str) -> None:
    errs.append(msg)


def main() -> int:
    errs: list[str] = []

    if not MAP_PATH.is_file():
        print(f"FAIL: map file missing: {MAP_PATH.relative_to(ROOT).as_posix()}")
        return 1

    try:
        with MAP_PATH.open(encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        print(f"FAIL: JSON decode error in {MAP_PATH.relative_to(ROOT).as_posix()}: {exc}")
        return 1

    if not isinstance(data, dict):
        fail(errs, "envelope: top-level JSON must be an object")
        data = {}

    schema = data.get("schema_version")
    if schema is None:
        fail(errs, "envelope: missing schema_version (expected int 2)")
    elif not isinstance(schema, int) or isinstance(schema, bool) or schema != 2:
        fail(errs, f"envelope: schema_version must be int 2, got {schema!r}")

    map_version = data.get("map_version")
    if not map_version:
        fail(errs, "envelope: missing or empty map_version")
    elif not isinstance(map_version, str) or not MAP_VERSION_RE.fullmatch(map_version):
        fail(
            errs,
            f"envelope: map_version must match N.N.N, got {map_version!r}",
        )

    generated_on = data.get("generated_on")
    if not generated_on:
        fail(errs, "envelope: missing or empty generated_on")
    elif not isinstance(generated_on, str) or not GENERATED_ON_RE.fullmatch(generated_on):
        fail(
            errs,
            f"envelope: generated_on must match YYYY-MM-DD, got {generated_on!r}",
        )

    clusters = data.get("clusters")
    if not isinstance(clusters, list):
        fail(errs, "envelope: missing or non-list clusters")
        clusters = []

    # --- collect map entries ---
    all_entries: list[tuple[str, str, str]] = []  # (pack, chapter, note-cluster)
    counts: dict[str, int] = {}
    seen_names: set[str] = set()
    for cluster in clusters:
        if not isinstance(cluster, dict):
            fail(errs, "clusters: entry is not an object")
            continue
        name = cluster.get("name")
        if not isinstance(name, str) or not name:
            fail(errs, "clusters: entry missing name")
            name = "<unnamed>"
        if name in seen_names:
            fail(errs, f"clusters: duplicate cluster name: {name!r}")
        else:
            seen_names.add(name)
        chapters = cluster.get("chapters")
        if not isinstance(chapters, list):
            fail(errs, f"clusters: {name!r} missing chapters list")
            chapters = []
        counts[name] = len(chapters)
        for entry in chapters:
            if not isinstance(entry, dict):
                fail(errs, f"clusters: {name!r} has non-object chapter entry")
                continue
            pack = entry.get("pack")
            chapter = entry.get("chapter")
            if not isinstance(pack, str) or not pack:
                fail(errs, f"clusters: {name!r} entry missing pack")
                continue
            if not isinstance(chapter, str) or not chapter:
                fail(errs, f"clusters: {name!r} entry missing chapter")
                continue
            all_entries.append((pack, chapter, name))

    total = len(all_entries)

    # --- print counts ---
    print("Capability map cluster counts:")
    for cluster in clusters:
        if isinstance(cluster, dict) and isinstance(cluster.get("name"), str):
            n = cluster["name"]
            print(f"  {n}: {counts.get(n, 0)}")
    print(f"  TOTAL: {total}")

    # uniqueness of (pack, chapter)
    pairs = [(p, c) for p, c, _ in all_entries]
    unique = set(pairs)
    if len(unique) != total:
        fail(
            errs,
            f"uniqueness: {total - len(unique)} duplicate (pack, chapter) pair(s) "
            f"(unique={len(unique)}, total={total})",
        )

    # --- pack-level staleness (both directions) ---
    packs_root = ROOT / "packs"
    on_disk_packs = {
        p.name
        for p in packs_root.iterdir()
        if p.is_dir() and (p / "chapters").is_dir()
    } if packs_root.is_dir() else set()
    mapped_packs = {p for p, _, _ in all_entries}

    missing_packs = sorted(on_disk_packs - mapped_packs)
    stale_packs = sorted(mapped_packs - on_disk_packs)
    for pack in missing_packs:
        fail(errs, f"staleness: pack on disk not in map: {pack}")
    for pack in stale_packs:
        fail(errs, f"staleness: pack in map has no chapters/ on disk: {pack}")

    # --- chapter-set equality (exclude support-file rows) ---
    map_chapters: set[tuple[str, str]] = set()
    for pack, chapter, _ in all_entries:
        if chapter.endswith(SUPPORT_SUFFIX):
            continue
        map_chapters.add((pack, chapter))

    disk_chapters: set[tuple[str, str]] = set()
    for pack_name in sorted(on_disk_packs):
        ch_dir = packs_root / pack_name / "chapters"
        for path in ch_dir.iterdir():
            if path.is_file():
                disk_chapters.add((pack_name, path.name))

    only_disk = sorted(disk_chapters - map_chapters)
    only_map = sorted(map_chapters - disk_chapters)
    if only_disk or only_map:
        fail(
            errs,
            f"chapter-set: mismatch vs packs/*/chapters "
            f"(on_disk_only={len(only_disk)}, map_only={len(only_map)})",
        )
        for pack, chapter in only_disk[:20]:
            fail(errs, f"chapter-set: on disk not in map: {pack}/{chapter}")
        if len(only_disk) > 20:
            fail(errs, f"chapter-set: ... and {len(only_disk) - 20} more on-disk-only")
        for pack, chapter in only_map[:20]:
            fail(errs, f"chapter-set: in map not on disk: {pack}/{chapter}")
        if len(only_map) > 20:
            fail(errs, f"chapter-set: ... and {len(only_map) - 20} more map-only")

    # --- file existence (branch on support-file suffix) ---
    for pack, chapter, cname in all_entries:
        if chapter.endswith(SUPPORT_SUFFIX):
            rel = chapter[: -len(SUPPORT_SUFFIX)]
            # Support files are plain filenames at pack root — reject traversal/abs.
            rel_path = Path(rel)
            if (
                ".." in rel_path.parts
                or rel_path.is_absolute()
                or "/" in rel
                or "\\" in rel
            ):
                fail(
                    errs,
                    f"existence: support file path rejected (must be plain filename "
                    f"at pack root): {rel!r} (cluster={cname})",
                )
                continue
            path = packs_root / pack / rel
            if not path.is_file():
                fail(
                    errs,
                    f"existence: support file missing: packs/{pack}/{rel} "
                    f"(cluster={cname})",
                )
        else:
            path = packs_root / pack / "chapters" / chapter
            if not path.is_file():
                fail(
                    errs,
                    f"existence: chapter missing: packs/{pack}/chapters/{chapter} "
                    f"(cluster={cname})",
                )

    # --- name-keyed thresholds ---
    for name, minimum in THRESHOLDS.items():
        if name not in counts:
            fail(errs, f"threshold: unknown cluster name (not in map): {name!r}")
            continue
        n = counts[name]
        if n < minimum:
            fail(errs, f"threshold: {name!r} has {n} entries, need >={minimum}")

    if errs:
        print(f"FAIL: {len(errs)} issue(s)")
        for msg in errs:
            print(f"  - {msg}")
        return 1

    print("PASS: capability map OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

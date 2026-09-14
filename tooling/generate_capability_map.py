#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
generate_capability_map.py — rebuild docs/capability-pack-map.json from
classification-rules.json + capability-pack-map-note-overrides.json (MAP-21-02/03/04).

Cluster assignment and envelope fields are generator output. Notes come only from
the mandatory 644-row overrides file (H-01). Support membership comes from
is_support rows, not rules_of_construction (H-03). Does not import sibling
checkers (H-07). Stdlib only.

Usage:
  python tooling/generate_capability_map.py --generated-on YYYY-MM-DD [--sync-md]
  python tooling/generate_capability_map.py --generated-on YYYY-MM-DD --check
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES_PATH = ROOT / "docs" / "classification-rules.json"
OVERRIDES_PATH = ROOT / "docs" / "capability-pack-map-note-overrides.json"
MAP_PATH = ROOT / "docs" / "capability-pack-map.json"
MD_PATH = ROOT / "docs" / "capability-pack-map.md"

SUPPORT_SUFFIX = " (support file)"
MAP_VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
GENERATED_ON_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ASSIGNMENT_KEYS = {"pack", "chapter", "cluster", "is_support"}
NOTE_KEYS = {"pack", "chapter", "note"}
_CLUSTER_NAME_FORBIDDEN = ("|", "\r", "\n", "\t")


def _bad_path_part(value: str) -> bool:
    if "/" in value or "\\" in value or ":" in value:
        return True
    return ".." in Path(value).parts or Path(value).is_absolute()


def _deslop(text: str) -> str:
    return re.sub(r"\s*—\s*", ", ", text)


def dumps_map(obj: dict) -> str:
    """Pretty JSON matching the live on-disk style (indent 2, insertion order)."""
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def generate_map(rules: dict, overrides: dict, generated_on: str) -> dict:
    """Build the v2 capability map object. Raises ValueError on validation failure."""
    if not isinstance(rules, dict):
        raise ValueError("rules: top-level must be an object")
    if not isinstance(overrides, dict):
        raise ValueError("overrides: top-level must be an object")
    if not isinstance(generated_on, str) or not GENERATED_ON_RE.fullmatch(generated_on):
        raise ValueError(f"generated_on must match YYYY-MM-DD, got {generated_on!r}")
    try:
        datetime.date.fromisoformat(generated_on)
    except ValueError as exc:
        raise ValueError(
            f"generated_on must be a valid calendar date, got {generated_on!r}"
        ) from exc

    schema = rules.get("schema_version")
    if not isinstance(schema, int) or isinstance(schema, bool) or schema != 1:
        raise ValueError(f"rules schema_version must be int 1, got {schema!r}")

    map_version = rules.get("map_version")
    if not isinstance(map_version, str) or not MAP_VERSION_RE.fullmatch(map_version):
        raise ValueError(f"rules map_version must match N.N.N, got {map_version!r}")

    cluster_names = rules.get("cluster_names")
    if (
        not isinstance(cluster_names, list)
        or not cluster_names
        or not all(isinstance(n, str) and n for n in cluster_names)
    ):
        raise ValueError("rules cluster_names must be a non-empty list of strings")
    for i, name in enumerate(cluster_names):
        if any(c in name for c in _CLUSTER_NAME_FORBIDDEN):
            raise ValueError(
                f"rules cluster_names[{i}] contains a forbidden character "
                f"(|, CR, LF, tab): {name!r}"
            )
    cluster_name_set = set(cluster_names)

    assignments = rules.get("assignments")
    if not isinstance(assignments, list):
        raise ValueError("rules assignments must be a list")

    o_schema = overrides.get("schema_version")
    if not isinstance(o_schema, int) or isinstance(o_schema, bool) or o_schema != 1:
        raise ValueError(f"overrides schema_version must be int 1, got {o_schema!r}")

    notes = overrides.get("notes")
    if not isinstance(notes, list):
        raise ValueError("overrides notes must be a list")

    akeys: set[tuple[str, str]] = set()
    assignment_rows: list[dict] = []
    for i, entry in enumerate(assignments):
        if not isinstance(entry, dict):
            raise ValueError(f"assignments[{i}]: not an object")
        actual = set(entry.keys())
        if actual != ASSIGNMENT_KEYS:
            extra = sorted(actual - ASSIGNMENT_KEYS)
            missing = sorted(ASSIGNMENT_KEYS - actual)
            bits = []
            if extra:
                bits.append(f"unexpected keys {extra}")
            if missing:
                bits.append(f"missing keys {missing}")
            raise ValueError(f"assignments[{i}]: " + "; ".join(bits))
        pack = entry["pack"]
        chapter = entry["chapter"]
        cluster = entry["cluster"]
        is_support = entry["is_support"]
        if not isinstance(pack, str) or not pack:
            raise ValueError(f"assignments[{i}]: pack must be a non-empty string")
        if not isinstance(chapter, str) or not chapter:
            raise ValueError(f"assignments[{i}]: chapter must be a non-empty string")
        if "\n" in pack or "\r" in pack:
            raise ValueError(f"assignments[{i}]: pack contains CR or LF: {pack!r}")
        if "\n" in chapter or "\r" in chapter:
            raise ValueError(f"assignments[{i}]: chapter contains CR or LF: {chapter!r}")
        if _bad_path_part(pack) or _bad_path_part(chapter):
            raise ValueError(
                f"assignments[{i}]: pack/chapter path rejected: {pack!r}/{chapter!r}"
            )
        if not isinstance(cluster, str) or cluster not in cluster_name_set:
            raise ValueError(
                f"assignments[{i}]: cluster {cluster!r} not in cluster_names "
                f"(pack={pack}, chapter={chapter})"
            )
        if type(is_support) is not bool:
            raise ValueError(
                f"assignments[{i}]: is_support must be bool, got {is_support!r}"
            )
        key = (pack, chapter)
        if key in akeys:
            raise ValueError(f"assignments: duplicate (pack, chapter): {pack}/{chapter}")
        akeys.add(key)
        assignment_rows.append(entry)

    note_map: dict[tuple[str, str], str] = {}
    nkeys: set[tuple[str, str]] = set()
    for i, entry in enumerate(notes):
        if not isinstance(entry, dict):
            raise ValueError(f"notes[{i}]: not an object")
        actual = set(entry.keys())
        if actual != NOTE_KEYS:
            extra = sorted(actual - NOTE_KEYS)
            missing = sorted(NOTE_KEYS - actual)
            bits = []
            if extra:
                bits.append(f"unexpected keys {extra}")
            if missing:
                bits.append(f"missing keys {missing}")
            raise ValueError(f"notes[{i}]: " + "; ".join(bits))
        pack = entry["pack"]
        chapter = entry["chapter"]
        note = entry["note"]
        if not isinstance(pack, str) or not pack:
            raise ValueError(f"notes[{i}]: pack must be a non-empty string")
        if not isinstance(chapter, str) or not chapter:
            raise ValueError(f"notes[{i}]: chapter must be a non-empty string")
        if not isinstance(note, str) or not note:
            raise ValueError(f"notes[{i}]: note must be a non-empty string")
        if "\n" in pack or "\r" in pack:
            raise ValueError(f"notes[{i}]: pack contains CR or LF: {pack!r}")
        if "\n" in chapter or "\r" in chapter:
            raise ValueError(f"notes[{i}]: chapter contains CR or LF: {chapter!r}")
        if "\n" in note or "\r" in note:
            raise ValueError(f"notes[{i}]: note contains CR or LF: {note!r}")
        if _bad_path_part(pack) or _bad_path_part(chapter):
            raise ValueError(
                f"notes[{i}]: pack/chapter path rejected: {pack!r}/{chapter!r}"
            )
        key = (pack, chapter)
        if key in nkeys:
            raise ValueError(f"notes: duplicate (pack, chapter): {pack}/{chapter}")
        nkeys.add(key)
        note_map[key] = note

    only_a = sorted(akeys - nkeys)
    only_n = sorted(nkeys - akeys)
    if only_a or only_n or len(notes) != 644:
        parts = []
        if only_a:
            p, c = only_a[0]
            parts.append(f"in assignments not in notes: {p}/{c}")
        if only_n:
            p, c = only_n[0]
            parts.append(f"in notes not in assignments: {p}/{c}")
        if len(notes) != 644:
            parts.append(f"notes length must be 644, got {len(notes)}")
        raise ValueError(
            "notes key set must equal assignments key set "
            f"(assignments_only={len(only_a)}, notes_only={len(only_n)}); "
            + "; ".join(parts)
        )

    buckets: dict[str, list[dict]] = {name: [] for name in cluster_names}
    for entry in assignment_rows:
        pack = entry["pack"]
        base = entry["chapter"]
        cluster = entry["cluster"]
        is_support = entry["is_support"]
        key = (pack, base)
        note = note_map[key]
        chapter_field = base + SUPPORT_SUFFIX if is_support else base
        buckets[cluster].append(
            {"pack": pack, "chapter": chapter_field, "note": note}
        )

    clusters = []
    for name in cluster_names:
        chapters = buckets[name]
        if not chapters:
            raise ValueError(f"cluster {name!r} has zero assignments")
        clusters.append({"name": name, "chapters": chapters})

    return {
        "schema_version": 2,
        "map_version": map_version,
        "generated_on": generated_on,
        "clusters": clusters,
    }


def _load_json(path: Path, label: str) -> dict:
    if not path.is_file():
        raise ValueError(f"{label} file missing: {path.relative_to(ROOT).as_posix()}")
    try:
        with path.open(encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ValueError(
            f"JSON decode error in {path.relative_to(ROOT).as_posix()}: {exc}"
        ) from exc
    if not isinstance(data, dict):
        raise ValueError(f"{label}: top-level JSON must be an object")
    return data


def render_md(map_obj: dict, header_prefix: str) -> str:
    """Rebuild Summary + cluster tables; keep header_prefix (up to ## Summary)."""
    clusters = map_obj["clusters"]
    lines: list[str] = []
    prefix = header_prefix.rstrip("\n")
    lines.append(prefix)
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Cluster | Entries |")
    lines.append("|---|---|")
    total = 0
    for i, cluster in enumerate(clusters, start=1):
        n = len(cluster["chapters"])
        total += n
        name = cluster["name"].replace("|", "\\|")
        lines.append(f"| {i}. {name} | {n} |")
    lines.append(f"| **Total** | **{total}** |")
    lines.append("")

    for i, cluster in enumerate(clusters, start=1):
        name = cluster["name"].replace("|", "\\|")
        lines.append(f"## {i}. {name}")
        lines.append("")
        lines.append("| Pack | Chapter | Why it fits / one-line value |")
        lines.append("|---|---|---|")
        for ch in cluster["chapters"]:
            pack = _deslop(ch["pack"]).replace("|", "\\|")
            chapter = _deslop(ch["chapter"]).replace("|", "\\|")
            note = _deslop(ch["note"]).replace("|", "\\|")
            lines.append(f"| {pack} | {chapter} | {note} |")
        lines.append("")

    return "\n".join(lines).rstrip("\n") + "\n"


def _split_md_header(text: str) -> str:
    marker = "## Summary"
    idx = text.find(marker)
    if idx < 0:
        raise ValueError("capability-pack-map.md missing ## Summary heading")
    return text[:idx]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate docs/capability-pack-map.json from rules + note overrides."
    )
    parser.add_argument(
        "--generated-on",
        required=True,
        help="YYYY-MM-DD envelope date (required; no wall-clock default)",
    )
    parser.add_argument(
        "--sync-md",
        action="store_true",
        help="Rewrite Summary and cluster tables in capability-pack-map.md",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated object to on-disk map; write nothing",
    )
    args = parser.parse_args(argv)

    if args.check and args.sync_md:
        print("FAIL: illegal combination --check and --sync-md (write nothing)")
        return 1

    if not GENERATED_ON_RE.fullmatch(args.generated_on):
        print(f"FAIL: --generated-on must match YYYY-MM-DD, got {args.generated_on!r}")
        return 1
    try:
        datetime.date.fromisoformat(args.generated_on)
    except ValueError:
        print(
            f"FAIL: --generated-on must be a valid calendar date, "
            f"got {args.generated_on!r}"
        )
        return 1

    try:
        rules = _load_json(RULES_PATH, "rules")
        overrides = _load_json(OVERRIDES_PATH, "overrides")
        built = generate_map(rules, overrides, args.generated_on)
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    if args.check:
        try:
            disk = _load_json(MAP_PATH, "map")
        except ValueError as exc:
            print(f"FAIL: {exc}")
            return 1
        if built != disk:
            print("FAIL: generated map does not match on-disk capability-pack-map.json")
            # Point at envelope drift first when that is the only difference.
            for key in ("schema_version", "map_version", "generated_on"):
                if built.get(key) != disk.get(key):
                    print(
                        f"  - envelope {key}: generated={built.get(key)!r} "
                        f"disk={disk.get(key)!r}"
                    )
            return 1
        print("PASS: generated map matches on-disk capability-pack-map.json")
        return 0

    # Prepare md text before any write when --sync-md so a missing ## Summary
    # fails closed before MAP_PATH is touched.
    md_text: str | None = None
    if args.sync_md:
        try:
            existing = MD_PATH.read_text(encoding="utf-8")
            header = _split_md_header(existing)
            md_text = render_md(built, header)
        except (OSError, ValueError) as exc:
            print(f"FAIL: md sync: {exc}")
            return 1

    MAP_PATH.write_text(dumps_map(built), encoding="utf-8", newline="\n")
    print(f"wrote {MAP_PATH.relative_to(ROOT).as_posix()}")

    if md_text is not None:
        MD_PATH.write_text(md_text, encoding="utf-8", newline="\n")
        print(f"wrote {MD_PATH.relative_to(ROOT).as_posix()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""
check_source_watch.py — validate and record docs/source-watchlist.json.

Two modes. validate (default, also --validate) reads the watchlist and
reports; it never writes. record (--record SLUG VERSION DATE) rewrites one
entry's version and last_checked. No web access, no repo imports, no third
mode. Stdlib only.

Dates are checked by datetime.date.fromisoformat, not by regex, so an
impossible date such as 2026-02-31 fails. STALE_DAYS is 62: two missed
month-ends plus margin.

Usage:  python tooling/check_source_watch.py
        python tooling/check_source_watch.py --record SLUG VERSION DATE
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WATCH_PATH = ROOT / "docs" / "source-watchlist.json"
CATALOG_PATH = ROOT / "catalog.json"
PACKS_ROOT = ROOT / "packs"

STALE_DAYS = 62
ENTRY_KEYS = ["slug", "publisher", "document", "version", "last_checked", "hint"]
SLUG_RE = re.compile(r"^[a-z0-9-]+$")
URL_RE = re.compile(r"https?://")
KIND_RE = re.compile(r"^kind:\s*(\S+)\s*$", re.M | re.I)
EXCLUDED_KINDS = {"signpost", "orchestrator"}


def fail(errs: list[str], msg: str) -> None:
    errs.append(msg)


def parse_date(value: str) -> date | None:
    # Shape first: date.fromisoformat on Python 3.11+ also accepts compact
    # and ISO-week forms, which the spec's YYYY-MM-DD-only rule rejects.
    if not (len(value) == 10 and value[4] == "-" and value[7] == "-"):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def value_shape_error(value: str, label: str) -> str | None:
    """Rule-2 value checks shared by validate and record. None when clean."""
    if not isinstance(value, str) or not value.strip():
        return f"{label}: empty"
    if value.strip().lower() == "unknown":
        return f"{label}: sentinel 'unknown' is not a revision"
    if URL_RE.search(value):
        return f"{label}: url-shaped value"
    return None


def check_watchlist(
    data: dict,
    catalog: dict,
    kinds: dict[str, str],
    today: date,
    include_staleness: bool = True,
) -> list[str]:
    """Validate a watchlist object. Never touches disk.

    include_staleness=False skips rule 5, which is what record uses: recording
    is what cures staleness, so a stale entry must still be recordable.
    """
    errs: list[str] = []
    if not isinstance(data, dict):
        fail(errs, "envelope: top-level JSON must be an object")
        return errs

    unexpected = set(data) - {"schema_version", "sources"}
    if unexpected:
        fail(errs, f"envelope: unexpected keys {sorted(unexpected)}")

    schema = data.get("schema_version")
    if not isinstance(schema, int) or isinstance(schema, bool) or schema != 1:
        fail(errs, f"envelope: schema_version must be int 1, got {schema!r}")

    sources = data.get("sources")
    if not isinstance(sources, list):
        fail(errs, "envelope: sources must be a list")
        return errs

    seen: set[str] = set()
    watch_slugs: list[str] = []
    for i, entry in enumerate(sources):
        where = f"sources[{i}]"
        if not isinstance(entry, dict):
            fail(errs, f"{where}: not an object")
            continue
        actual = list(entry)
        if actual != ENTRY_KEYS:
            missing = [k for k in ENTRY_KEYS if k not in entry]
            extra = [k for k in entry if k not in ENTRY_KEYS]
            fail(errs, f"{where}: key set {actual} != {ENTRY_KEYS} "
                       f"(missing {missing}, extra {extra})")
        slug = entry.get("slug")
        if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
            fail(errs, f"{where}: slug must match {SLUG_RE.pattern}, got {slug!r}")
        elif slug in seen:
            fail(errs, f"{where}: duplicate slug {slug!r}")
        else:
            seen.add(slug)
            watch_slugs.append(slug)
        for key in ("publisher", "document", "version"):
            val = entry.get(key)
            if not isinstance(val, str) or not val.strip():
                fail(errs, f"{where}: {key} must be a non-empty string")
        hint = entry.get("hint")
        if not isinstance(hint, str):
            fail(errs, f"{where}: hint must be a string")
        checked = entry.get("last_checked")
        if not isinstance(checked, str):
            fail(errs, f"{where}: last_checked must be a string")
        elif checked != "" and parse_date(checked) is None:
            fail(errs, f"{where}: last_checked must be YYYY-MM-DD or empty, "
                       f"got {checked!r}")
        for key, val in entry.items():
            if isinstance(val, str) and URL_RE.search(val):
                fail(errs, f"{where}: url-shaped value in {key}")
        if include_staleness and isinstance(checked, str):
            parsed = parse_date(checked) if checked else None
            if parsed is None or (today - parsed).days > STALE_DAYS:
                fail(errs, f"{where}: stale last_checked {checked!r} "
                           f"(older than {STALE_DAYS} days or never checked)")

    live = set()
    planned = set()
    if isinstance(catalog, dict):
        for row in catalog.get("packs", []):
            if isinstance(row, dict) and row.get("status", "live") in ("live", None, ""):
                slug = row.get("slug")
                if isinstance(slug, str):
                    live.add(slug)
        for row in catalog.get("planned", []):
            if isinstance(row, dict) and isinstance(row.get("slug"), str):
                planned.add(row["slug"])

    for slug in sorted(live - set(watch_slugs)):
        fail(errs, f"coverage: catalog live slug {slug!r} has no watchlist entry")
    for slug in watch_slugs:
        if slug not in live:
            fail(errs, f"coverage: watchlist slug {slug!r} is not a live catalog pack")
        kind = kinds.get(slug, "").lower()
        if kind in EXCLUDED_KINDS:
            fail(errs, f"coverage: {slug!r} is a {kind} and must not be watched")
        if slug in planned:
            fail(errs, f"coverage: {slug!r} is a planned entry and must not be watched")

    return errs


def load_kinds(packs_root: Path) -> dict[str, str]:
    kinds: dict[str, str] = {}
    if not packs_root.is_dir():
        return kinds
    for skill in sorted(packs_root.glob("*/SKILL.md")):
        head = skill.read_text(encoding="utf-8", errors="ignore").split("---", 2)
        front = head[1] if len(head) > 2 else head[0]
        m = KIND_RE.search(front)
        if m:
            kinds[skill.parent.name] = m.group(1)
    return kinds


def record_entry(
    path: Path,
    slug: str,
    version: str,
    date_str: str,
    catalog: dict | None = None,
    kinds: dict[str, str] | None = None,
) -> int:
    """Rewrite one entry. Returns 0 on a completed write, 1 on any refusal."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"FAIL: cannot read {path}: {exc}")
        return 1

    try:
        if catalog is None:
            catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
        if kinds is None:
            kinds = load_kinds(PACKS_ROOT)
    except (json.JSONDecodeError, OSError) as exc:
        print(f"FAIL: cannot read catalog or packs: {exc}")
        return 1

    errs = check_watchlist(data, catalog, kinds, date.today(),
                           include_staleness=False)
    if errs:
        print(f"FAIL: {len(errs)} issue(s)")
        for msg in errs:
            print(f"  - {msg}")
        return 1

    for label, value in (("VERSION", version), ("DATE", date_str)):
        err = value_shape_error(value, label)
        if err:
            print(f"FAIL: {err}")
            return 1
    parsed = parse_date(date_str)
    if parsed is None:
        print(f"FAIL: DATE must be YYYY-MM-DD, got {date_str!r}")
        return 1
    if parsed > date.today():
        print(f"FAIL: DATE {date_str} is in the future")
        return 1

    target = next((e for e in data["sources"] if e.get("slug") == slug), None)
    if target is None:
        print(f"FAIL: slug {slug!r} is not in the watchlist")
        return 1

    old = target["version"]
    target["version"] = version
    target["last_checked"] = date_str
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"recorded {slug}: {old!r} -> {version!r} @ {date_str}")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args[:1] == ["--record"]:
        if len(args) != 4:
            print("FAIL: usage: --record SLUG VERSION DATE")
            return 1
        return record_entry(WATCH_PATH, args[1], args[2], args[3])
    if args not in ([], ["--validate"]):
        print(f"FAIL: unknown arguments {args}")
        return 1

    if not WATCH_PATH.is_file():
        print(f"FAIL: watchlist missing: {WATCH_PATH.relative_to(ROOT).as_posix()}")
        return 1
    try:
        data = json.loads(WATCH_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        print(f"FAIL: JSON decode error in "
              f"{WATCH_PATH.relative_to(ROOT).as_posix()}: {exc}")
        return 1
    if not isinstance(data, dict):
        print("FAIL: 1 issue(s)")
        print("  - envelope: top-level JSON must be an object")
        return 1

    try:
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"FAIL: cannot read catalog.json: {exc}")
        return 1
    errs = check_watchlist(data, catalog, load_kinds(PACKS_ROOT), date.today())
    if errs:
        print(f"FAIL: {len(errs)} issue(s)")
        for msg in errs:
            print(f"  - {msg}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

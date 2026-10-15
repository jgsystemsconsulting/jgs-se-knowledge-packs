#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based checks for the source watchlist validator (no framework).

Run:  python tooling/test_source_watch.py
Exits 0 when every case holds. Any failed assert raises and exits nonzero.

URL fixtures are assembled from fragments so this file never contains a
contiguous banned-host URL, or a scheme literal, and does not trip the
link scan against itself.
"""
from __future__ import annotations

import json
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_source_watch  # noqa: E402

TODAY = date(2026, 10, 11)
KEYS = ["slug", "publisher", "document", "version", "last_checked", "hint"]


def entry(slug="faa-rma", **over):
    base = {
        "slug": slug,
        "publisher": "FAA",
        "document": "FAA-HDBK-006D",
        "version": "FAA-HDBK-006D (8 October 2020)",
        "last_checked": "2026-10-01",
        "hint": "",
    }
    base.update(over)
    return base


def watch(entries):
    return {"schema_version": 1, "sources": entries}


def catalog(*slugs, status="live"):
    rows = []
    for s in slugs:
        row = {"slug": s}
        if status is not None:
            row["status"] = status
        rows.append(row)
    return {"packs": rows}


def check(data, cat, kinds=None, today=TODAY):
    return check_source_watch.check_watchlist(data, cat, kinds or {}, today)


def expect_fail(errs, needle):
    assert errs, "expected at least one error"
    assert any(needle in e for e in errs), f"{needle!r} not in {errs}"


def test_valid_passes():
    assert KEYS == check_source_watch.ENTRY_KEYS
    errs = check(watch([entry()]), catalog("faa-rma"))
    assert errs == [], errs


def test_missing_key_fails():
    bad = entry()
    del bad["document"]
    expect_fail(check(watch([bad]), catalog("faa-rma")), "document")


def test_extra_key_fails():
    bad = entry()
    bad["note"] = "x"
    expect_fail(check(watch([bad]), catalog("faa-rma")), "note")


def test_duplicate_slug_fails():
    errs = check(watch([entry(), entry()]), catalog("faa-rma"))
    expect_fail(errs, "duplicate")


def test_url_shaped_value_fails():
    # Fragments: the scheme is split so this file has no scheme literal.
    scheme = "ht" + "tps://ex" + "ample.test/"
    bad = entry(hint=scheme + "doc")
    expect_fail(check(watch([bad]), catalog("faa-rma")), "url")


def test_bad_date_fails():
    # A regex would accept this; a real parse must not.
    bad = entry(last_checked="2026-02-31")
    expect_fail(check(watch([bad]), catalog("faa-rma")), "last_checked")


def test_bad_slug_fails():
    bad = entry(slug="FAA_RMA")
    errs = check(watch([bad]), catalog("FAA_RMA"))
    expect_fail(errs, "slug")


def test_catalog_slug_absent_fails():
    errs = check(watch([entry()]), catalog("faa-rma", "nist-ssdf"))
    expect_fail(errs, "nist-ssdf")


def test_signpost_slug_present_fails():
    errs = check(
        watch([entry(), entry("autosign")]),
        catalog("faa-rma"),
        {"autosign": "signpost"},
    )
    expect_fail(errs, "must not be watched")


def test_planned_slug_present_fails():
    cat = catalog("faa-rma")
    cat["planned"] = [{"slug": "mit-ocw-se"}]
    errs = check(watch([entry(), entry("mit-ocw-se")]), cat)
    expect_fail(errs, "planned")


def test_stale_date_fails():
    old = (TODAY - timedelta(days=check_source_watch.STALE_DAYS + 1)).isoformat()
    errs = check(watch([entry(last_checked=old)]), catalog("faa-rma"))
    expect_fail(errs, "stale")


def test_fresh_date_passes():
    fresh = (TODAY - timedelta(days=check_source_watch.STALE_DAYS)).isoformat()
    errs = check(watch([entry(last_checked=fresh)]), catalog("faa-rma"))
    assert errs == [], errs


def test_empty_last_checked_fails_rule_5_only():
    errs = check(watch([entry(last_checked="")]), catalog("faa-rma"))
    expect_fail(errs, "stale")
    errs_no_stale = check_source_watch.check_watchlist(
        watch([entry(last_checked="")]), catalog("faa-rma"), {}, TODAY,
        include_staleness=False,
    )
    assert errs_no_stale == [], errs_no_stale


def test_missing_status_counts_as_live():
    # No status key: live, same as check_release.py:586-588.
    cat = catalog("faa-rma", status=None)
    assert "status" not in cat["packs"][0]
    errs = check(watch([entry()]), cat)
    assert errs == [], errs
    missing = check(watch([entry("nist-ssdf", publisher="NIST")]), cat)
    expect_fail(missing, "has no watchlist entry")


def test_empty_string_status_is_not_live():
    # An explicit empty string is neither absent nor "live".
    cat = catalog("faa-rma", status="")
    assert cat["packs"][0]["status"] == ""
    errs = check(watch([entry()]), cat)
    expect_fail(errs, "is not a live catalog pack")


def test_record_updates_one_entry(tmp_path):
    data = watch([entry("faa-rma"), entry("nist-ssdf", publisher="NIST")])
    path = tmp_path / "watch.json"
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    before = json.loads(path.read_text(encoding="utf-8"))
    rc = check_source_watch.record_entry(
        path, "faa-rma", "FAA-HDBK-006E", "2026-10-11",
        catalog=catalog("faa-rma", "nist-ssdf"), kinds={},
    )
    assert rc == 0
    after = json.loads(path.read_text(encoding="utf-8"))
    assert after["sources"][0]["version"] == "FAA-HDBK-006E"
    assert after["sources"][0]["last_checked"] == "2026-10-11"
    assert after["sources"][1] == before["sources"][1]
    assert [e["slug"] for e in after["sources"]] == ["faa-rma", "nist-ssdf"]
    assert path.read_text(encoding="utf-8").endswith("\n")


def test_record_refuses_unknown_sentinel(tmp_path):
    data = watch([entry()])
    path = tmp_path / "watch.json"
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    original = path.read_text(encoding="utf-8")
    for bad in ("unknown", "Unknown", "UNKNOWN"):
        rc = check_source_watch.record_entry(
            path, "faa-rma", bad, "2026-10-11",
            catalog=catalog("faa-rma"), kinds={},
        )
        assert rc == 1, bad
        assert path.read_text(encoding="utf-8") == original, bad


def main() -> int:
    import tempfile
    test_valid_passes()
    test_missing_key_fails()
    test_extra_key_fails()
    test_duplicate_slug_fails()
    test_url_shaped_value_fails()
    test_bad_date_fails()
    test_bad_slug_fails()
    test_catalog_slug_absent_fails()
    test_signpost_slug_present_fails()
    test_planned_slug_present_fails()
    test_stale_date_fails()
    test_fresh_date_passes()
    test_empty_last_checked_fails_rule_5_only()
    test_missing_status_counts_as_live()
    test_empty_string_status_is_not_live()
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        test_record_updates_one_entry(root)
        test_record_refuses_unknown_sentinel(root)
    print("source-watch tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

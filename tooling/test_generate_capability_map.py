#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""Assert-based probes for capability-map tooling hardening (no framework).

Run:  python tooling/test_generate_capability_map.py
Exits 0 when cluster-name validation, renderer escaping, the --check md
freshness gate, the rules-vs-map generated_on fidelity check, and clean-tree
byte stability all hold. Any failed assert raises and exits nonzero.

Probe (c) points the generator module's MAP_PATH/MD_PATH at files inside a
TemporaryDirectory and restores the real paths in finally; docs/ is never
written by this file.
"""
from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_classification_rules  # noqa: E402
import generate_capability_map  # noqa: E402

FORBIDDEN = ("|", "\r", "\n", "\t")


def rules_fixture(cluster_names, on="2026-01-01"):
    return {
        "schema_version": 1,
        "map_version": "1.0.0",
        "generated_on": on,
        "support_policy": "Support files ship with every pack.",
        "rules_of_construction": ["Construction rule one."],
        "support_filenames": ["glossary.md", "patterns.md", "cheatsheet.md"],
        "signpost_packs": ["omg-signpost", "se-standards-signpost"],
        "cluster_names": list(cluster_names),
        "assignments": [],
    }


def map_fixture(cluster_names, on="2026-01-01"):
    return {
        "schema_version": 2,
        "map_version": "1.0.0",
        "generated_on": on,
        "clusters": [{"name": n, "chapters": []} for n in cluster_names],
    }


def main() -> int:
    # (a) every rejected character fails closed in both entry points
    for ch in FORBIDDEN:
        name = "A" + ch + "B"
        raised = False
        try:
            generate_capability_map.generate_map(
                rules_fixture([name]), {}, "2026-01-01"
            )
        except ValueError as exc:
            raised = True
            assert (
                "rules cluster_names[0] contains a forbidden character"
                in str(exc)
            ), f"wrong generator rejection message for {name!r}: {exc}"
        assert raised, f"generate_map accepted forbidden character in {name!r}"
        errs = check_classification_rules.check_rules(
            rules_fixture([name]), live_map=map_fixture([name])
        )
        assert any(
            "envelope: cluster_names[0] contains a forbidden character" in m
            for m in errs
        ), f"check_rules missed forbidden character in {name!r}: {errs}"

    # (b) renderer escapes pipes; clean names pass through byte-identical
    piped = generate_capability_map.render_md(map_fixture(["A|B"]), "Header line\n")
    lines = piped.splitlines()
    row = next(ln for ln in lines if ln.startswith("| 1. "))
    head = next(ln for ln in lines if ln.startswith("## 1. "))
    assert row == "| 1. A\\|B | 0 |", f"summary row not escaped: {row!r}"
    assert head == "## 1. A\\|B", f"heading not escaped: {head!r}"
    clean = generate_capability_map.render_md(map_fixture(["Clean"]), "Header line\n")
    assert "| 1. Clean | 0 |" in clean, clean
    assert "## 1. Clean" in clean, clean

    # (d) rules-vs-map generated_on drift fails; equal dates yield no date error
    errs = check_classification_rules.check_rules(
        rules_fixture(["C1"], on="2026-01-01"),
        live_map=map_fixture(["C1"], on="2026-02-02"),
    )
    assert (
        "fidelity: rules generated_on '2026-01-01' != live map '2026-02-02'"
        in errs
    ), f"date drift not reported: {errs}"
    errs = check_classification_rules.check_rules(
        rules_fixture(["C1"]), live_map=map_fixture(["C1"])
    )
    assert not any(
        m.startswith("fidelity: rules generated_on") for m in errs
    ), f"false date error on equal dates: {errs}"

    # (c) --check md freshness: stale, missing, missing marker, fresh
    tmp = tempfile.TemporaryDirectory()
    real_map_path = generate_capability_map.MAP_PATH
    real_md_path = generate_capability_map.MD_PATH
    try:
        generate_capability_map.MAP_PATH = Path(tmp.name) / "map.json"
        generate_capability_map.MD_PATH = Path(tmp.name) / "map.md"
        rules = generate_capability_map._load_json(
            generate_capability_map.RULES_PATH, "rules"
        )
        overrides = generate_capability_map._load_json(
            generate_capability_map.OVERRIDES_PATH, "overrides"
        )
        built = generate_capability_map.generate_map(rules, overrides, "2026-01-01")
        generate_capability_map.MAP_PATH.write_text(
            generate_capability_map.dumps_map(built), encoding="utf-8"
        )
        good_md = generate_capability_map.render_md(built, "Probe header\n")

        def run_check():
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = generate_capability_map.main(
                    ["--generated-on", "2026-01-01", "--check"]
                )
            return rc, buf.getvalue()

        generate_capability_map.MD_PATH.write_text(
            good_md.replace("## Summary", "## Summary\n<!-- tampered -->", 1),
            encoding="utf-8",
        )
        rc, out = run_check()
        assert rc == 1, f"stale md did not fail: rc={rc}"
        assert "capability-pack-map.md is stale" in out, out

        generate_capability_map.MD_PATH.unlink()
        rc, out = run_check()
        assert rc == 1, f"missing md did not fail: rc={rc}"
        assert "md check: capability-pack-map.md missing" in out, out

        generate_capability_map.MD_PATH.write_text("no marker here\n", encoding="utf-8")
        rc, out = run_check()
        assert rc == 1, f"missing ## Summary did not fail: rc={rc}"
        assert "md check:" in out and "## Summary" in out, out

        generate_capability_map.MD_PATH.write_text(good_md, encoding="utf-8")
        rc, out = run_check()
        assert rc == 0, f"fresh md failed: rc={rc} out={out}"
        assert "PASS: capability-pack-map.md is fresh" in out, out
    finally:
        generate_capability_map.MAP_PATH = real_map_path
        generate_capability_map.MD_PATH = real_md_path
        tmp.cleanup()

    # (e) clean tree stays byte-stable green
    disk_map = json.loads(
        generate_capability_map.MAP_PATH.read_text(encoding="utf-8")
    )
    disk_on = disk_map["generated_on"]
    disk_rules = generate_capability_map._load_json(
        generate_capability_map.RULES_PATH, "rules"
    )
    assert disk_rules["generated_on"] == disk_on, "rules vs map date drift"
    names = disk_rules["cluster_names"]
    assert len(names) == 32, f"expected 32 cluster names, got {len(names)}"
    assert not any(
        c in n for n in names for c in FORBIDDEN
    ), "live cluster name carries a forbidden character"
    built = generate_capability_map.generate_map(
        disk_rules,
        generate_capability_map._load_json(
            generate_capability_map.OVERRIDES_PATH, "overrides"
        ),
        disk_on,
    )
    disk_md = generate_capability_map.MD_PATH.read_text(encoding="utf-8")
    assert generate_capability_map.render_md(
        built, generate_capability_map._split_md_header(disk_md)
    ) == disk_md, "fresh render differs from on-disk capability-pack-map.md"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = generate_capability_map.main(["--generated-on", disk_on, "--check"])
    out = buf.getvalue()
    assert rc == 0, f"--check failed on clean tree: rc={rc} out={out}"
    assert "PASS: generated map matches on-disk capability-pack-map.json" in out, out
    assert "PASS: capability-pack-map.md is fresh" in out, out

    print("generate-capability-map tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

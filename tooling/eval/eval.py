#!/usr/bin/env python3
# Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
# SPDX-License-Identifier: MIT
"""eval.py — closed-loop eval harness (v1, read-only) for the knowledge packs.

Deterministic scoring core. Does NOT call any LLM: answer+judge records are
produced by Claude subagents in-session and fed in as JSON. See tooling/eval/README.md.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
VALID_STATUS = {"complete", "seed"}
SCORED_TYPES = {"topic", "chapter", "applied"}
TRIGGER_TYPES = {"trigger-positive", "trigger-negative"}


def validate_bank(bank: dict) -> list[str]:
    """Return a list of error strings; empty means the bank is structurally valid."""
    errs: list[str] = []
    if not bank.get("slug"):
        errs.append("missing 'slug'")
    if bank.get("status") not in VALID_STATUS:
        errs.append(f"'status' must be one of {sorted(VALID_STATUS)}")
    questions = bank.get("questions", [])
    if not isinstance(questions, list):
        return errs + ["'questions' must be a list"]
    seen: set[str] = set()
    for q in questions:
        qid = q.get("id", "<no-id>")
        if not q.get("id"):
            errs.append("a question is missing 'id'")
        elif qid in seen:
            errs.append(f"duplicate question id: {qid}")
        seen.add(qid)
        qtype = q.get("type")
        if qtype in SCORED_TYPES:
            if "routing" not in q:
                errs.append(f"{qid}: scored question missing 'routing'")
            if not q.get("must_include"):
                errs.append(f"{qid}: scored question missing 'must_include'")
            if not q.get("provenance"):
                errs.append(f"{qid}: scored question missing 'provenance'")
        elif qtype in TRIGGER_TYPES:
            if "expect_fire" not in q:
                errs.append(f"{qid}: trigger question missing 'expect_fire'")
        else:
            errs.append(f"{qid}: unknown type '{qtype}'")
    return errs


def load_bank(path: Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


GATE_FLOOR = 2  # a scored dimension at or below this fails the question


def gate_verdict(record: dict) -> str:
    """PASS/FAIL for one question. A question FAILS if any scored dimension <= GATE_FLOOR
    or triggering == FAIL. Scored dims are None for trigger-type questions (ignored)."""
    j = record["judge"]
    for dim in ("faithfulness", "routing", "completeness"):
        v = j.get(dim)
        if v is not None and v <= GATE_FLOOR:
            return "FAIL"
    if j.get("triggering") == "FAIL":
        return "FAIL"
    return "PASS"


def trend_scalar(record: dict) -> float:
    """0.0 on a gated fail, else mean of the three scored dimensions (ignoring None)."""
    if gate_verdict(record) == "FAIL":
        return 0.0
    j = record["judge"]
    vals = [j[d] for d in ("faithfulness", "routing", "completeness") if j.get(d) is not None]
    return sum(vals) / len(vals) if vals else 0.0


def disposition(record: dict) -> str:
    """Human-review routing for one question:
      QUARANTINE      — faithfulness failure (<=2) or any must_not_include hit; needs human,
                        never auto-fixed. Highest priority.
      ANCHOR_REVIEW   — answer is otherwise strong (faithfulness>=4) but a must_use_term is
                        missing; the anchor itself may be stale/wrong — review the bank, not the skill.
      NONE            — no human review needed for faithfulness/anchor reasons.
    """
    j = record["judge"]
    faith = j.get("faithfulness")
    if j.get("must_not_include_hits"):
        return "QUARANTINE"
    if faith is not None and faith <= GATE_FLOOR:
        return "QUARANTINE"
    if (faith is None or faith >= 4) and j.get("must_use_terms_missing"):
        return "ANCHOR_REVIEW"
    return "NONE"


REQUIRED_JUDGE_METHOD = "anchors-only"


def attestation_errors(record: dict) -> list[str]:
    """Verify a record attests it was produced under the design's two faithfulness rules:
      1. judge_method == 'anchors-only'  (faithfulness scored only vs human anchors)
      2. faithfulness_saw_loaded_files == False  (loaded-file list withheld from faithfulness)
    eval.py can't observe the driver, but it refuses to trust records that don't attest.
    Returns a list of error strings (empty == well-attested)."""
    errs: list[str] = []
    if record.get("judge_method") != REQUIRED_JUDGE_METHOD:
        errs.append(f"{record.get('id', '?')}: judge_method must be '{REQUIRED_JUDGE_METHOD}' "
                    f"(got {record.get('judge_method')!r})")
    # `is not False` (identity, not ==): a missing key (.get -> None) is caught, and we
    # require the literal JSON `false`, not a falsy 0. The schema pins it to const:false.
    if record.get("faithfulness_saw_loaded_files") is not False:
        errs.append(f"{record.get('id', '?')}: faithfulness_saw_loaded_files must be false "
                    "(the loaded-file list must be withheld from the faithfulness pass)")
    return errs


CANARY_MIN_LOAD_BEARING = 5  # below this, a canary slice has no statistical power


def canary_is_load_bearing(records: list[dict]) -> bool:
    return sum(1 for r in records if r.get("canary")) >= CANARY_MIN_LOAD_BEARING


def aggregate(slug: str, status: str, records: list[dict]) -> dict:
    """Per-pack roll-up. A 'seed' (stub) bank is always INCOMPLETE. A complete bank is
    FAIL if any question fails, else PASS."""
    verdicts = {r["id"]: gate_verdict(r) for r in records}
    if status == "seed":
        pack_status = "INCOMPLETE"
    elif any(v == "FAIL" for v in verdicts.values()):
        pack_status = "FAIL"
    else:
        pack_status = "PASS"
    return {
        "slug": slug,
        "status": pack_status,
        "verdicts": verdicts,
        "dispositions": {r["id"]: disposition(r) for r in records},
        "trend": {r["id"]: trend_scalar(r) for r in records},
        "canary_load_bearing": canary_is_load_bearing(records),
    }


def suite_status(pack_aggregates: list[dict], total_packs: int) -> str:
    """Suite-level status. INCOMPLETE unless every pack is evaluated and none is a stub;
    FAIL if any evaluated pack failed; else PASS."""
    if len(pack_aggregates) < total_packs:
        return "INCOMPLETE"
    statuses = [p["status"] for p in pack_aggregates]
    if any(s == "INCOMPLETE" for s in statuses):
        return "INCOMPLETE"
    if any(s == "FAIL" for s in statuses):
        return "FAIL"
    return "PASS"


def baseline_diff(baseline: dict, current: dict) -> dict:
    """Compare current {qid: verdict} against a committed baseline's 'expected' map.
      regressions — was PASS in baseline, now FAIL
      fixed       — was FAIL in baseline, now PASS
      new         — qid present now but absent from baseline (needs a baseline update)
    """
    expected = baseline.get("expected", {})
    regressions, fixed, new = [], [], []
    for qid, verdict in current.items():
        if qid not in expected:
            new.append(qid)
        elif expected[qid] == "PASS" and verdict == "FAIL":
            regressions.append(qid)
        elif expected[qid] == "FAIL" and verdict == "PASS":
            fixed.append(qid)
    return {"regressions": sorted(regressions), "fixed": sorted(fixed), "new": sorted(new)}


def baseline_gate_ok(diff: dict) -> bool:
    """The gate bites ONLY on regressions. 'fixed' and 'new' do not fail the gate
    (they signal the baseline should be refreshed)."""
    return not diff["regressions"]


def render_report(pack_aggregates: list[dict], suite: str, total_packs: int,
                  judge_model: str, bank_sha: str) -> str:
    """Markdown run report. Failures listed first. Shows N/total denominator, judge model,
    and bank git SHA so any two reports are self-describingly comparable."""
    n = len(pack_aggregates)
    lines = [
        "# Eval run report",
        "",
        f"- **Suite status:** {suite}",
        f"- **Packs evaluated:** {n}/{total_packs}",
        f"- **Judge model:** {judge_model}",
        f"- **Bank git SHA:** {bank_sha}",
        "",
        "## Packs",
        "",
    ]
    for p in sorted(pack_aggregates, key=lambda a: 0 if a["status"] == "FAIL" else 1):
        lines.append(f"### {p['slug']} — {p['status']}")
        fails = [q for q, v in p["verdicts"].items() if v == "FAIL"]
        if fails:
            lines.append("")
            lines.append("Failing questions (severity-first):")
            for q in fails:
                lines.append(f"- `{q}` — verdict FAIL, disposition {p['dispositions'].get(q, 'NONE')}")
        passes = [q for q, v in p["verdicts"].items() if v == "PASS"]
        lines.append("")
        lines.append(f"Passing: {len(passes)} | canary load-bearing: {p['canary_load_bearing']}")
        lines.append("")
    return "\n".join(lines)


def render_quarantine(slug: str, records: list[dict]) -> str:
    """VERDICT-ONLY digest of questions needing human review. NEVER includes the answer
    text or any source quotation (honors the repo's raw-source-text prohibition).
    Returns '' if nothing needs review."""
    out: list[str] = []
    for r in records:
        disp = disposition(r)
        if disp == "NONE":
            continue
        j = r["judge"]
        out.append(f"### `{r['id']}` — {disp}")
        out.append(f"- faithfulness: {j.get('faithfulness')}")
        out.append(f"- unmapped claims: {len(j.get('unmapped_claims', []))}")
        out.append(f"- must_not_include hits: {len(j.get('must_not_include_hits', []))}")
        out.append(f"- must_use_terms missing: {j.get('must_use_terms_missing', [])}")
        out.append("")
    if not out:
        return ""
    return "\n".join([f"# Quarantine / anchor-review digest — {slug}",
                      "",
                      "Verdict-only. No answer text or source quotations are included by design.",
                      "Review each item by re-running the question and inspecting the answer locally.",
                      ""] + out)


import argparse


def _cmd_validate(args) -> int:
    bank = load_bank(Path(args.bank))
    errs = validate_bank(bank)
    if errs:
        print(f"FAIL  {args.bank}")
        for e in errs:
            print(f"        - {e}")
        return 1
    print(f"PASS  {args.bank} ({len(bank.get('questions', []))} questions)")
    return 0


def _cmd_runplan(args) -> int:
    """Emit the (id, type, prompt) list a driver must dispatch to answerer subagents."""
    bank = load_bank(Path(args.bank))
    plan = [{"id": q["id"], "type": q["type"], "prompt": q["prompt"],
             "slug": bank["slug"]} for q in bank.get("questions", [])]
    print(json.dumps(plan, indent=2))
    return 0


def _cmd_score(args) -> int:
    """Consume collected records (JSON list) + bank + baseline; write report + quarantine."""
    bank = load_bank(Path(args.bank))
    records = json.loads(Path(args.records).read_text(encoding="utf-8"))
    canary = {q["id"]: q.get("canary", False) for q in bank.get("questions", [])}
    for r in records:
        r.setdefault("canary", canary.get(r["id"], False))
    att = [e for r in records for e in attestation_errors(r)]
    if att:
        print("REFUSED — records not attested to the faithfulness rules:")
        for e in att:
            print(f"  - {e}")
        return 2  # distinct from a gate FAIL (1): the run itself is untrusted
    agg = aggregate(bank["slug"], bank["status"], records)
    current = agg["verdicts"]
    gate_ok = True
    if args.baseline and Path(args.baseline).is_file():
        diff = baseline_diff(load_bank(Path(args.baseline)), current)
        gate_ok = baseline_gate_ok(diff)
        print(f"baseline: regressions={diff['regressions']} fixed={diff['fixed']} new={diff['new']}")
    report = render_report([agg], suite=("INCOMPLETE" if bank["status"] == "seed" else agg["status"]),
                           total_packs=args.total_packs, judge_model=args.judge_model,
                           bank_sha=args.bank_sha)
    quarantine = render_quarantine(bank["slug"], records)
    out_dir = ROOT / "results" / "latest"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "report.md").write_text(report, encoding="utf-8")
    if quarantine.strip():
        (out_dir / "faithfulness-review.md").write_text(quarantine, encoding="utf-8")
    return 0 if gate_ok else 1


def coverage_summary(manifest: dict) -> dict:
    packs = manifest.get("packs", [])
    seeded = sum(1 for p in packs if p.get("status") == "seeded")
    stub = sum(1 for p in packs if p.get("status") == "stub")
    return {"seeded": seeded, "stub": stub, "total": len(packs),
            "suite": "COMPLETE" if stub == 0 and seeded == len(packs) else "INCOMPLETE"}


def _cmd_coverage(args) -> int:
    path = ROOT / "tooling" / "eval" / "coverage.json"
    try:
        manifest = load_bank(path)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"coverage: cannot read {path}: {e}")
        return 1
    s = coverage_summary(manifest)
    print(f"coverage: {s['seeded']} seeded / {s['stub']} stub / {s['total']} total — {s['suite']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Knowledge-pack eval harness (v1, read-only).")
    sub = p.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("validate", help="structurally validate a bank")
    v.add_argument("bank")
    v.set_defaults(func=_cmd_validate)

    rp = sub.add_parser("runplan", help="emit the dispatch plan for a bank")
    rp.add_argument("bank")
    rp.set_defaults(func=_cmd_runplan)

    sc = sub.add_parser("score", help="score collected records + gate vs baseline")
    sc.add_argument("bank")
    sc.add_argument("records")
    sc.add_argument("--baseline", default=None)
    sc.add_argument("--total-packs", type=int, default=13, dest="total_packs")
    sc.add_argument("--judge-model", default="unknown", dest="judge_model")
    sc.add_argument("--bank-sha", default="unknown", dest="bank_sha")
    sc.set_defaults(func=_cmd_score)

    cv = sub.add_parser("coverage", help="print the 13-pack seeding coverage")
    cv.set_defaults(func=_cmd_coverage)
    return p


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    import sys
    raise SystemExit(main(sys.argv[1:]))

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

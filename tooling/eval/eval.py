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

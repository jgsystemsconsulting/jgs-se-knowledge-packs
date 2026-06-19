# Skill Eval Harness (v1, read-only) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a stdlib-Python harness that grades the knowledge-pack skills' answers against hand-curated ground truth on four dimensions (faithfulness, routing, completeness, triggering), gated by a committed baseline, with faithfulness failures quarantined for human review.

**Architecture:** `eval.py` is the deterministic core — it loads JSON question banks, validates them, and (given a set of *already-collected* answer + judge records) computes per-dimension scores, ranks findings, diffs against a committed baseline, and writes a report + a quarantine digest. The actual answering and judging are done by Claude subagents driven *outside* `eval.py` (in-session); `eval.py` never calls an LLM, so its logic is fully unit-testable with fixture records. A thin `runplan` command emits the list of (pack, question) prompts a driver must dispatch, and an `score` command consumes the collected records. v1 is **read-only**: no pack file is ever auto-edited.

**Tech Stack:** Python 3 stdlib only (`json`, `argparse`, `pathlib`, `re`, `statistics`, `unittest`) — matches `tooling/validate_pack.py` / `tooling/check_release.py` (zero third-party deps; CI runs them directly). JSON for banks/baselines/records (stdlib-parseable). Tests use `unittest` (stdlib) so `python -m unittest` runs them with no pytest dependency.

---

## Conventions every task follows

- **Authored-file header.** Every `.py` file created starts with exactly:
  ```python
  #!/usr/bin/env python3
  # Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
  # SPDX-License-Identifier: MIT
  ```
  (This is what `check_release.py`'s `HEADER_SENTINEL` / `SPDX_SENTINEL` look for. JSON banks carry no header — JSON has no comments; the release checker only checks `.py`/`.md` authored files, not `banks/*.json`.)
- **Root discovery.** `ROOT = Path(__file__).resolve().parent.parent.parent` (eval.py is at `tooling/eval/eval.py`, so three parents up = repo root).
- **No LLM calls in `eval.py`.** Determinism and testability depend on this. Answer/judge records are produced by subagents and fed in as JSON.
- **Run tests with:** `python -m unittest discover -s tooling/eval/tests -t .` from repo root.
- **Commit after every task** with a `feat:`/`test:`/`docs:` prefix.

---

## File structure (decomposition locked here)

```
tooling/eval/
  eval.py                       # CLI + all scoring logic (single focused module, ~400 lines)
  rubric.md                     # explanatory rubric; machine rules live in eval.py + schema
  schemas/
    bank.schema.json            # JSON Schema (draft-07) for a question bank
    record.schema.json          # JSON Schema for a collected answer+judge record
  banks/
    nasa-risk.json              # FULLY seeded reference pack (Task 9)
    requirements-writing.json   # fan-out seed (Task 12)
    sebok.json                  # fan-out seed (Task 12)
  baselines/
    nasa-risk.baseline.json     # committed expected pass/fail (Task 10)
    requirements-writing.baseline.json
    sebok.baseline.json
  coverage.json                 # 13-pack manifest: status seeded|stub (Task 11)
  README.md                     # how to run / add questions / read reports / quarantine (Task 13)
  tests/
    __init__.py
    fixtures/                   # JSON fixture records for scoring tests
    test_bank_loading.py
    test_scoring.py
    test_aggregation.py
    test_baseline.py
    test_report.py
    test_coverage.py
results/                        # gitignored (Task 1); run outputs only
```

**Why one `eval.py` not many modules:** the scoring logic is one cohesive responsibility (~400 lines) and the repo's existing tools are each single files. Splitting into `loader.py`/`scorer.py`/`reporter.py` would fight the established pattern and add import ceremony for no isolation benefit. If `eval.py` exceeds ~600 lines during implementation, split `report` rendering into `report.py` then.

---

## Data shapes (referenced by every task)

**Bank** (`banks/<slug>.json`):
```json
{
  "slug": "nasa-risk",
  "status": "complete",
  "questions": [ { "...": "see question shapes below" } ]
}
```

**Question — `topic`/`chapter`/`applied` type:**
```json
{
  "id": "nr-01",
  "type": "topic",
  "prompt": "How does NASA set a performance commitment, and what makes it risk-normalised?",
  "routing": { "any_of": ["ch05"], "all_of": [] },
  "must_include": ["performance measure value at a defined risk tolerance percentile",
                   "equal probability of failure across alternatives"],
  "must_use_terms": [{ "term": "performance commitment", "synonyms": [] }],
  "provenance": "NASA/SP-2011-3422 ch05",
  "must_not_include": ["performance commitment is the worst-case value"],
  "canary": false
}
```

**Question — `trigger-positive`/`trigger-negative` type:**
```json
{ "id": "nr-tn-01", "type": "trigger-negative",
  "prompt": "Write a Python function to parse a CSV.", "expect_fire": false, "canary": false }
```

**Record** (one per question, produced by subagents, fed to `eval.py score`):
```json
{
  "id": "nr-01",
  "loaded_files": ["packs/nasa-risk/SKILL.md", "packs/nasa-risk/chapters/ch05-ridm-part3-risk-informed-selection.md"],
  "answer": "A performance commitment is a performance measure value at a defined risk tolerance percentile ...",
  "fired": true,
  "judge_method": "anchors-only",
  "faithfulness_saw_loaded_files": false,
  "judge": {
    "faithfulness": 5,
    "routing": 5,
    "completeness": 5,
    "triggering": "PASS",
    "unmapped_claims": [],
    "must_not_include_hits": [],
    "must_use_terms_missing": []
  }
}
```
`judge` is the **median-of-3 already collapsed** by the driver before being written (eval.py receives final integer/string scores, not the 3 raw runs). `triggering` is `"PASS"`/`"FAIL"`/`null` (null for non-trigger questions). `routing`/`completeness`/`faithfulness` are `null` for trigger-type questions. `judge_method` and `faithfulness_saw_loaded_files` are the **attestation fields**: the driver MUST set them to `"anchors-only"` and `false` respectively, asserting it scored faithfulness only against the human anchors and never showed the loaded-file list to the faithfulness judge. `eval.py score` refuses (exit 2) any record missing or contradicting these.

**Baseline** (`baselines/<slug>.baseline.json`):
```json
{ "slug": "nasa-risk", "expected": { "nr-01": "PASS", "nr-02": "PASS", "nr-tn-01": "PASS" } }
```

---

### Task 1: Gitignore the results tree + scaffold dirs

**Files:**
- Modify: `.gitignore`
- Create: `tooling/eval/tests/__init__.py` (empty)
- Create: `tooling/eval/tests/fixtures/.gitkeep` (empty)

- [ ] **Step 1: Add results/ to .gitignore**

Append to `.gitignore` (after the existing `*.full_text.txt` block):
```
# Eval harness run outputs (reports + quarantine digests; never source text)
results/
```

- [ ] **Step 2: Create empty test package files**

Create `tooling/eval/tests/__init__.py` with no content. Create `tooling/eval/tests/fixtures/.gitkeep` with no content.

- [ ] **Step 3: Verify gitignore works**

Run: `mkdir -p results/x && touch results/x/y.md && git status --porcelain results/`
Expected: no output (results/ is ignored).
Then: `rm -rf results/x`

- [ ] **Step 4: Commit**

```bash
git add .gitignore tooling/eval/tests/__init__.py tooling/eval/tests/fixtures/.gitkeep
git commit -m "chore: gitignore eval results tree + scaffold test package"
```

---

### Task 2: Bank loader + structural validation

**Files:**
- Create: `tooling/eval/eval.py`
- Test: `tooling/eval/tests/test_bank_loading.py`

- [ ] **Step 1: Write the failing test**

Create `tooling/eval/tests/test_bank_loading.py`:
```python
import json
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import eval as ev  # noqa: E402


class TestBankLoading(unittest.TestCase):
    def _bank(self, **over):
        b = {"slug": "demo", "status": "complete", "questions": [
            {"id": "d-01", "type": "topic", "prompt": "p",
             "routing": {"any_of": ["ch01"], "all_of": []},
             "must_include": ["x"], "provenance": "src ch01"}]}
        b.update(over)
        return b

    def test_valid_bank_returns_no_errors(self):
        self.assertEqual(ev.validate_bank(self._bank()), [])

    def test_missing_slug_is_error(self):
        b = self._bank(); del b["slug"]
        self.assertIn("missing 'slug'", " ".join(ev.validate_bank(b)))

    def test_bad_status_is_error(self):
        self.assertTrue(any("status" in e for e in ev.validate_bank(self._bank(status="done"))))

    def test_duplicate_ids_is_error(self):
        b = self._bank()
        b["questions"].append(dict(b["questions"][0]))
        self.assertTrue(any("duplicate" in e for e in ev.validate_bank(b)))

    def test_trigger_question_requires_expect_fire(self):
        b = self._bank(questions=[{"id": "d-tn", "type": "trigger-negative", "prompt": "p"}])
        self.assertTrue(any("expect_fire" in e for e in ev.validate_bank(b)))

    def test_topic_question_requires_routing(self):
        b = self._bank(questions=[{"id": "d-01", "type": "topic", "prompt": "p",
                                   "must_include": ["x"], "provenance": "s"}])
        self.assertTrue(any("routing" in e for e in ev.validate_bank(b)))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tooling.eval.tests.test_bank_loading -v` (from repo root)
Expected: FAIL — `ModuleNotFoundError: No module named 'eval'` or `AttributeError: module 'eval' has no attribute 'validate_bank'`.

- [ ] **Step 3: Write minimal implementation**

Create `tooling/eval/eval.py`:
```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tooling.eval.tests.test_bank_loading -v`
Expected: PASS (6 tests).

- [ ] **Step 5: Commit**

```bash
git add tooling/eval/eval.py tooling/eval/tests/test_bank_loading.py
git commit -m "feat: eval bank loader + structural validation"
```

---

### Task 3: Per-dimension scoring → gate verdict

**Files:**
- Modify: `tooling/eval/eval.py`
- Test: `tooling/eval/tests/test_scoring.py`

- [ ] **Step 1: Write the failing test**

Create `tooling/eval/tests/test_scoring.py`:
```python
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import eval as ev  # noqa: E402


def scored_record(**judge):
    base = {"faithfulness": 5, "routing": 5, "completeness": 5,
            "triggering": None, "unmapped_claims": [],
            "must_not_include_hits": [], "must_use_terms_missing": []}
    base.update(judge)
    return {"id": "q", "judge": base}


class TestScoring(unittest.TestCase):
    def test_all_fives_passes(self):
        self.assertEqual(ev.gate_verdict(scored_record()), "PASS")

    def test_faithfulness_2_fails(self):
        self.assertEqual(ev.gate_verdict(scored_record(faithfulness=2)), "FAIL")

    def test_routing_2_fails(self):
        self.assertEqual(ev.gate_verdict(scored_record(routing=2)), "FAIL")

    def test_completeness_2_fails(self):
        self.assertEqual(ev.gate_verdict(scored_record(completeness=2)), "FAIL")

    def test_trigger_fail_fails(self):
        r = {"id": "t", "judge": {"faithfulness": None, "routing": None,
             "completeness": None, "triggering": "FAIL"}}
        self.assertEqual(ev.gate_verdict(r), "FAIL")

    def test_trigger_pass_passes(self):
        r = {"id": "t", "judge": {"faithfulness": None, "routing": None,
             "completeness": None, "triggering": "PASS"}}
        self.assertEqual(ev.gate_verdict(r), "PASS")

    def test_must_not_include_hit_is_faithfulness_fail(self):
        # judge should already cap faithfulness<=2 on a hit; gate must fail regardless
        r = scored_record(faithfulness=2, must_not_include_hits=["bad claim"])
        self.assertEqual(ev.gate_verdict(r), "FAIL")

    def test_trend_scalar_zero_on_gated_fail(self):
        self.assertEqual(ev.trend_scalar(scored_record(completeness=2)), 0.0)

    def test_trend_scalar_is_mean_when_passing(self):
        self.assertAlmostEqual(
            ev.trend_scalar(scored_record(faithfulness=4, routing=5, completeness=3)),
            (4 + 5 + 3) / 3)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tooling.eval.tests.test_scoring -v`
Expected: FAIL — `AttributeError: module 'eval' has no attribute 'gate_verdict'`.

- [ ] **Step 3: Write minimal implementation**

Append to `tooling/eval/eval.py`:
```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tooling.eval.tests.test_scoring -v`
Expected: PASS (9 tests).

- [ ] **Step 5: Commit**

```bash
git add tooling/eval/eval.py tooling/eval/tests/test_scoring.py
git commit -m "feat: per-question gate verdict + trend scalar"
```

---

### Task 4: Quarantine classification (faithfulness + anchor-integrity)

**Files:**
- Modify: `tooling/eval/eval.py`
- Test: `tooling/eval/tests/test_scoring.py` (add a class)

- [ ] **Step 1: Write the failing test**

Append to `tooling/eval/tests/test_scoring.py`:
```python
class TestQuarantine(unittest.TestCase):
    def _rec(self, **judge):
        base = {"faithfulness": 5, "routing": 5, "completeness": 5, "triggering": None,
                "unmapped_claims": [], "must_not_include_hits": [], "must_use_terms_missing": []}
        base.update(judge)
        return {"id": "q", "judge": base}

    def test_faithfulness_fail_quarantines(self):
        self.assertEqual(ev.disposition(self._rec(faithfulness=2)), "QUARANTINE")

    def test_must_not_include_hit_quarantines(self):
        self.assertEqual(
            ev.disposition(self._rec(faithfulness=2, must_not_include_hits=["x"])), "QUARANTINE")

    def test_strong_answer_with_term_miss_is_anchor_review(self):
        # faithfulness high but a must_use_term missing => suspect stale anchor, not model fault
        self.assertEqual(
            ev.disposition(self._rec(faithfulness=5, must_use_terms_missing=["RIDM"])),
            "ANCHOR_REVIEW")

    def test_clean_pass_needs_no_review(self):
        self.assertEqual(ev.disposition(self._rec()), "NONE")

    def test_routing_only_fail_is_not_quarantine(self):
        # routing fail with healthy faithfulness is a model/index issue, not quarantine
        self.assertEqual(ev.disposition(self._rec(routing=2)), "NONE")


class TestAttestation(unittest.TestCase):
    """The headline guarantees (faithfulness scored only vs human anchors; loaded-file
    list withheld from the faithfulness pass) are enforced by the DRIVER, not by eval.py
    (which only sees collapsed scores). eval.py cannot verify the wall was honored, but it
    CAN refuse to trust a record that doesn't attest to it — converting the guarantee from
    'documented' to 'attested in-band'."""

    def _rec(self, judge_method="anchors-only", faithfulness_saw_loaded_files=False):
        return {"id": "q", "judge_method": judge_method,
                "faithfulness_saw_loaded_files": faithfulness_saw_loaded_files,
                "judge": {"faithfulness": 5, "routing": 5, "completeness": 5, "triggering": None,
                          "unmapped_claims": [], "must_not_include_hits": [],
                          "must_use_terms_missing": []}}

    def test_well_attested_record_is_trusted(self):
        self.assertEqual(ev.attestation_errors(self._rec()), [])

    def test_missing_method_is_flagged(self):
        r = self._rec(); del r["judge_method"]
        self.assertTrue(ev.attestation_errors(r))

    def test_wrong_method_is_flagged(self):
        self.assertTrue(ev.attestation_errors(self._rec(judge_method="trust-me")))

    def test_faithfulness_saw_loaded_files_is_flagged(self):
        self.assertTrue(ev.attestation_errors(self._rec(faithfulness_saw_loaded_files=True)))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tooling.eval.tests.test_scoring -v`
Expected: FAIL — `AttributeError: module 'eval' has no attribute 'disposition'`.

- [ ] **Step 3: Write minimal implementation**

Append to `tooling/eval/eval.py`:
```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tooling.eval.tests.test_scoring -v`
Expected: PASS (18 tests total in file).

- [ ] **Step 5: Commit**

```bash
git add tooling/eval/eval.py tooling/eval/tests/test_scoring.py
git commit -m "feat: quarantine + anchor-review disposition routing"
```

---

### Task 5: Aggregation with INCOMPLETE rule + canary power check

**Files:**
- Modify: `tooling/eval/eval.py`
- Test: `tooling/eval/tests/test_aggregation.py`

- [ ] **Step 1: Write the failing test**

Create `tooling/eval/tests/test_aggregation.py`:
```python
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import eval as ev  # noqa: E402


def rec(qid, verdict="PASS", canary=False):
    j = {"faithfulness": 5, "routing": 5, "completeness": 5, "triggering": None,
         "unmapped_claims": [], "must_not_include_hits": [], "must_use_terms_missing": []}
    if verdict == "FAIL":
        j["completeness"] = 2
    return {"id": qid, "canary": canary, "judge": j}


class TestAggregation(unittest.TestCase):
    def test_all_pass_complete_bank_is_pass(self):
        agg = ev.aggregate("nasa-risk", "complete", [rec("a"), rec("b")])
        self.assertEqual(agg["status"], "PASS")

    def test_a_fail_makes_bank_fail(self):
        agg = ev.aggregate("nasa-risk", "complete", [rec("a"), rec("b", "FAIL")])
        self.assertEqual(agg["status"], "FAIL")

    def test_seed_status_forces_incomplete(self):
        agg = ev.aggregate("demo", "seed", [rec("a")])
        self.assertEqual(agg["status"], "INCOMPLETE")

    def test_partial_pack_coverage_is_incomplete_at_suite_level(self):
        suite = ev.suite_status([
            {"status": "PASS"}, {"status": "PASS"}], total_packs=13)
        self.assertEqual(suite, "INCOMPLETE")  # only 2/13 evaluated

    def test_full_coverage_all_pass_is_pass(self):
        suite = ev.suite_status([{"status": "PASS"}] * 13, total_packs=13)
        self.assertEqual(suite, "PASS")

    def test_any_fail_makes_suite_fail_even_if_complete(self):
        suite = ev.suite_status([{"status": "PASS"}] * 12 + [{"status": "FAIL"}], total_packs=13)
        self.assertEqual(suite, "FAIL")

    def test_canary_load_bearing_only_at_five(self):
        self.assertFalse(ev.canary_is_load_bearing([rec("a", canary=True)] * 4))
        self.assertTrue(ev.canary_is_load_bearing([rec(str(i), canary=True) for i in range(5)]))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tooling.eval.tests.test_aggregation -v`
Expected: FAIL — `AttributeError: module 'eval' has no attribute 'aggregate'`.

- [ ] **Step 3: Write minimal implementation**

Append to `tooling/eval/eval.py`:
```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tooling.eval.tests.test_aggregation -v`
Expected: PASS (7 tests).

- [ ] **Step 5: Commit**

```bash
git add tooling/eval/eval.py tooling/eval/tests/test_aggregation.py
git commit -m "feat: pack + suite aggregation with INCOMPLETE rule and canary power gate"
```

---

### Task 6: Baseline diff (the no-regression gate)

**Files:**
- Modify: `tooling/eval/eval.py`
- Test: `tooling/eval/tests/test_baseline.py`

- [ ] **Step 1: Write the failing test**

Create `tooling/eval/tests/test_baseline.py`:
```python
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import eval as ev  # noqa: E402


class TestBaseline(unittest.TestCase):
    def test_no_change_is_clean(self):
        base = {"slug": "s", "expected": {"a": "PASS", "b": "PASS"}}
        cur = {"a": "PASS", "b": "PASS"}
        self.assertEqual(ev.baseline_diff(base, cur), {"regressions": [], "fixed": [], "new": []})

    def test_regression_detected(self):
        base = {"slug": "s", "expected": {"a": "PASS"}}
        cur = {"a": "FAIL"}
        self.assertEqual(ev.baseline_diff(base, cur)["regressions"], ["a"])

    def test_fixed_detected(self):
        base = {"slug": "s", "expected": {"a": "FAIL"}}
        cur = {"a": "PASS"}
        self.assertEqual(ev.baseline_diff(base, cur)["fixed"], ["a"])

    def test_new_question_not_in_baseline_is_flagged_new(self):
        base = {"slug": "s", "expected": {"a": "PASS"}}
        cur = {"a": "PASS", "z": "PASS"}
        self.assertEqual(ev.baseline_diff(base, cur)["new"], ["z"])

    def test_gate_fails_on_regression(self):
        base = {"slug": "s", "expected": {"a": "PASS"}}
        self.assertFalse(ev.baseline_gate_ok(ev.baseline_diff(base, {"a": "FAIL"})))

    def test_gate_ok_when_only_fixed_or_new(self):
        base = {"slug": "s", "expected": {"a": "FAIL"}}
        self.assertTrue(ev.baseline_gate_ok(ev.baseline_diff(base, {"a": "PASS", "z": "PASS"})))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tooling.eval.tests.test_baseline -v`
Expected: FAIL — `AttributeError: module 'eval' has no attribute 'baseline_diff'`.

- [ ] **Step 3: Write minimal implementation**

Append to `tooling/eval/eval.py`:
```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tooling.eval.tests.test_baseline -v`
Expected: PASS (6 tests).

- [ ] **Step 5: Commit**

```bash
git add tooling/eval/eval.py tooling/eval/tests/test_baseline.py
git commit -m "feat: baseline diff + no-regression gate"
```

---

### Task 7: Report + quarantine digest rendering

**Files:**
- Modify: `tooling/eval/eval.py`
- Test: `tooling/eval/tests/test_report.py`

- [ ] **Step 1: Write the failing test**

Create `tooling/eval/tests/test_report.py`:
```python
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import eval as ev  # noqa: E402


def agg(slug="nasa-risk", status="PASS"):
    return {"slug": slug, "status": status,
            "verdicts": {"a": "PASS", "b": "FAIL"},
            "dispositions": {"a": "NONE", "b": "QUARANTINE"},
            "trend": {"a": 5.0, "b": 0.0},
            "canary_load_bearing": True}


class TestReport(unittest.TestCase):
    def test_report_shows_denominator(self):
        md = ev.render_report([agg()], suite="INCOMPLETE", total_packs=13,
                              judge_model="claude-x", bank_sha="abc123")
        self.assertIn("1/13", md)
        self.assertIn("INCOMPLETE", md)

    def test_report_lists_failures_first(self):
        # Two packs: one FAIL, one PASS. The FAIL pack's heading must appear before the
        # PASS pack's heading. (Do NOT assert on a bare letter like "b" — it matches the
        # 'b' in a bank_sha and passes vacuously.)
        fail_pack = agg(slug="pack-fail", status="FAIL")
        pass_pack = agg(slug="pack-pass", status="PASS")
        pass_pack["verdicts"] = {"a": "PASS"}
        pass_pack["dispositions"] = {"a": "NONE"}
        pass_pack["trend"] = {"a": 5.0}
        md = ev.render_report([pass_pack, fail_pack], suite="FAIL", total_packs=13,
                              judge_model="claude-x", bank_sha="0000000")
        self.assertLess(md.index("### pack-fail"), md.index("### pack-pass"))
        self.assertIn("FAIL", md)

    def test_quarantine_digest_has_no_source_quotations(self):
        # digest is verdict-only: it must contain the qid and disposition, never the answer text
        recs = [{"id": "b", "canary": False,
                 "answer": "SECRET SOURCE TEXT THAT MUST NOT LEAK",
                 "judge": {"faithfulness": 2, "routing": 5, "completeness": 5,
                           "triggering": None, "unmapped_claims": ["foo"],
                           "must_not_include_hits": ["bad"], "must_use_terms_missing": []}}]
        digest = ev.render_quarantine("nasa-risk", recs)
        self.assertIn("b", digest)
        self.assertIn("QUARANTINE", digest)
        self.assertNotIn("SECRET SOURCE TEXT", digest)

    def test_quarantine_digest_empty_when_nothing_to_review(self):
        recs = [{"id": "a", "canary": False, "answer": "x",
                 "judge": {"faithfulness": 5, "routing": 5, "completeness": 5,
                           "triggering": None, "unmapped_claims": [],
                           "must_not_include_hits": [], "must_use_terms_missing": []}}]
        self.assertEqual(ev.render_quarantine("nasa-risk", recs).strip(), "")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tooling.eval.tests.test_report -v`
Expected: FAIL — `AttributeError: module 'eval' has no attribute 'render_report'`.

- [ ] **Step 3: Write minimal implementation**

Append to `tooling/eval/eval.py`:
```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tooling.eval.tests.test_report -v`
Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add tooling/eval/eval.py tooling/eval/tests/test_report.py
git commit -m "feat: report + verdict-only quarantine digest rendering"
```

---

### Task 8: CLI (`validate`, `runplan`, `score`) + JSON schemas

**Files:**
- Modify: `tooling/eval/eval.py`
- Create: `tooling/eval/schemas/bank.schema.json`
- Create: `tooling/eval/schemas/record.schema.json`
- Test: `tooling/eval/tests/test_coverage.py` (CLI smoke + coverage; coverage logic added Task 11)

- [ ] **Step 1: Write the failing test**

Create `tooling/eval/tests/test_coverage.py`:
```python
import json
import subprocess
import sys
import unittest
from pathlib import Path

EVAL = Path(__file__).resolve().parent.parent / "eval.py"
ROOT = Path(__file__).resolve().parent.parent.parent.parent


class TestCli(unittest.TestCase):
    def test_validate_runs_and_reports_pass_on_a_good_bank(self):
        # write a tiny valid bank to a temp path under results/ (gitignored)
        tmp = ROOT / "results" / "_t_bank.json"
        tmp.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_text(json.dumps({"slug": "demo", "status": "complete", "questions": [
            {"id": "d-01", "type": "topic", "prompt": "p",
             "routing": {"any_of": ["ch01"], "all_of": []},
             "must_include": ["x"], "provenance": "s ch01"}]}), encoding="utf-8")
        r = subprocess.run([sys.executable, str(EVAL), "validate", str(tmp)],
                           capture_output=True, text=True)
        tmp.unlink()
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
        self.assertIn("PASS", r.stdout)

    def test_validate_fails_on_bad_bank(self):
        tmp = ROOT / "results" / "_t_bad.json"
        tmp.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_text(json.dumps({"status": "complete", "questions": []}), encoding="utf-8")
        r = subprocess.run([sys.executable, str(EVAL), "validate", str(tmp)],
                           capture_output=True, text=True)
        tmp.unlink()
        self.assertEqual(r.returncode, 1)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tooling.eval.tests.test_coverage -v`
Expected: FAIL — eval.py has no CLI yet (returncode not 0, no "PASS").

- [ ] **Step 3: Write minimal implementation**

Create `tooling/eval/schemas/bank.schema.json`:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Eval question bank",
  "type": "object",
  "required": ["slug", "status", "questions"],
  "properties": {
    "slug": { "type": "string" },
    "status": { "enum": ["complete", "seed"] },
    "questions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "type", "prompt"],
        "properties": {
          "id": { "type": "string" },
          "type": { "enum": ["topic", "chapter", "applied", "trigger-positive", "trigger-negative"] },
          "prompt": { "type": "string" },
          "routing": {
            "type": "object",
            "properties": {
              "any_of": { "type": "array", "items": { "type": "string" } },
              "all_of": { "type": "array", "items": { "type": "string" } }
            }
          },
          "must_include": { "type": "array", "items": { "type": "string" } },
          "must_use_terms": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["term"],
              "properties": {
                "term": { "type": "string" },
                "synonyms": { "type": "array", "items": { "type": "string" } }
              }
            }
          },
          "must_not_include": { "type": "array", "items": { "type": "string" } },
          "provenance": { "type": "string" },
          "expect_fire": { "type": "boolean" },
          "canary": { "type": "boolean" }
        }
      }
    }
  }
}
```

Create `tooling/eval/schemas/record.schema.json`:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Collected answer+judge record",
  "type": "object",
  "required": ["id", "judge", "judge_method", "faithfulness_saw_loaded_files"],
  "properties": {
    "id": { "type": "string" },
    "loaded_files": { "type": "array", "items": { "type": "string" } },
    "answer": { "type": "string" },
    "fired": { "type": "boolean" },
    "canary": { "type": "boolean" },
    "judge_method": { "const": "anchors-only" },
    "faithfulness_saw_loaded_files": { "const": false },
    "judge": {
      "type": "object",
      "required": ["faithfulness", "routing", "completeness", "triggering"],
      "properties": {
        "faithfulness": { "type": ["integer", "null"], "minimum": 1, "maximum": 5 },
        "routing": { "type": ["integer", "null"], "minimum": 1, "maximum": 5 },
        "completeness": { "type": ["integer", "null"], "minimum": 1, "maximum": 5 },
        "triggering": { "enum": ["PASS", "FAIL", null] },
        "unmapped_claims": { "type": "array", "items": { "type": "string" } },
        "must_not_include_hits": { "type": "array", "items": { "type": "string" } },
        "must_use_terms_missing": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

Append the CLI to `tooling/eval/eval.py`:
```python
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
    # attach canary flags from the bank so aggregation can see them
    canary = {q["id"]: q.get("canary", False) for q in bank.get("questions", [])}
    for r in records:
        r.setdefault("canary", canary.get(r["id"], False))
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
    qu, = (render_quarantine(bank["slug"], records),)
    out_dir = ROOT / "results" / "latest"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "report.md").write_text(report, encoding="utf-8")
    if qu strip := qu .strip():  # placeholder line replaced below
        pass
    return 0 if gate_ok else 1


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
    return p


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    import sys
    raise SystemExit(main(sys.argv[1:]))
```

> **Implementation note:** the `_cmd_score` body above contains an intentionally-broken
> placeholder (`qu, =` / `if qu strip :=`) to force you to write the quarantine-writing block
> correctly rather than copy a typo. Replace the marked region with:
> ```python
>     quarantine = render_quarantine(bank["slug"], records)
>     out_dir = ROOT / "results" / "latest"
>     out_dir.mkdir(parents=True, exist_ok=True)
>     (out_dir / "report.md").write_text(report, encoding="utf-8")
>     if quarantine.strip():
>         (out_dir / "faithfulness-review.md").write_text(quarantine, encoding="utf-8")
>     return 0 if gate_ok else 1
> ```
> Delete the three placeholder lines (`qu , = ...`, `if qu strip ...`, `pass`) and the
> duplicate `out_dir`/`report.md` write above them.
>
> **Also add the attestation gate** near the top of `_cmd_score`, right after the
> `for r in records: r.setdefault("canary", ...)` loop and before `agg = aggregate(...)`:
> ```python
>     att = [e for r in records for e in attestation_errors(r)]
>     if att:
>         print("REFUSED — records not attested to the faithfulness rules:")
>         for e in att:
>             print(f"  - {e}")
>         return 2  # distinct from a gate FAIL (1): the run itself is untrusted
> ```
> This makes `score` refuse (exit 2) any record set that doesn't carry
> `judge_method: "anchors-only"` and `faithfulness_saw_loaded_files: false`.

- [ ] **Step 4: Fix the placeholder, then run test to verify it passes**

Apply the implementation note's correction. Then run:
`python -m unittest tooling.eval.tests.test_coverage -v`
Expected: PASS (2 tests). Also re-run the full suite:
`python -m unittest discover -s tooling/eval/tests -t .`
Expected: all tests PASS.

- [ ] **Step 5: Commit**

```bash
git add tooling/eval/eval.py tooling/eval/schemas/
git commit -m "feat: eval CLI (validate/runplan/score) + bank & record JSON schemas"
```

---

### Task 9: Seed the nasa-risk bank (reference pack)

**Files:**
- Create: `tooling/eval/banks/nasa-risk.json`

This is a **human-authored** task: the anchors are the ground truth, so they must be written by
someone who has read `packs/nasa-risk/` (the chapters and SKILL.md). The content below is the
required starting bank; the author verifies each anchor against the pack before committing.

- [ ] **Step 1: Write the bank**

Create `tooling/eval/banks/nasa-risk.json` (≥5 canary items; ≥1 `applied`; trigger-negatives):
```json
{
  "slug": "nasa-risk",
  "status": "complete",
  "questions": [
    {
      "id": "nr-01",
      "type": "topic",
      "prompt": "How does NASA set a performance commitment, and what makes the comparison risk-normalised?",
      "routing": { "any_of": ["ch05"], "all_of": [] },
      "must_include": ["performance measure value at a defined risk tolerance percentile",
                       "equal probability of failure to meet the commitment across alternatives"],
      "must_use_terms": [{ "term": "performance commitment", "synonyms": [] }],
      "provenance": "NASA/SP-2011-3422 ch05",
      "must_not_include": ["a performance commitment is the worst-case value"],
      "canary": false
    },
    {
      "id": "nr-02",
      "type": "topic",
      "prompt": "What are the two integrated processes that make up NASA Risk Management, and what question does each answer?",
      "routing": { "any_of": ["ch01", "ch02"], "all_of": [] },
      "must_include": ["RIDM — which alternative should we implement",
                       "CRM — how do we manage risk during implementation"],
      "must_use_terms": [{ "term": "RIDM", "synonyms": ["Risk-Informed Decision Making"] },
                         { "term": "CRM", "synonyms": ["Continuous Risk Management"] }],
      "provenance": "NASA/SP-2011-3422 ch01",
      "must_not_include": ["RIDM and CRM are the same process under different names"],
      "canary": true
    },
    {
      "id": "nr-03",
      "type": "chapter",
      "prompt": "Give the NASA individual risk statement format.",
      "routing": { "any_of": ["ch07"], "all_of": [] },
      "must_include": ["Given that [CONDITION]", "there is a possibility of [DEPARTURE]",
                       "adversely impacting [ASSET]", "leading to [CONSEQUENCE]"],
      "must_use_terms": [{ "term": "individual risk statement", "synonyms": [] }],
      "provenance": "NASA/SP-2011-3422 ch07",
      "must_not_include": ["the consequence should be written net of mitigations"],
      "canary": true
    },
    {
      "id": "nr-04",
      "type": "topic",
      "prompt": "List the six CRM risk disposition types.",
      "routing": { "any_of": ["ch08"], "all_of": [] },
      "must_include": ["Accept", "Mitigate", "Watch", "Research", "Elevate", "Close"],
      "must_use_terms": [{ "term": "disposition", "synonyms": ["disposition types"] }],
      "provenance": "NASA/SP-2011-3422 ch08",
      "must_not_include": ["Transfer", "Avoid"],
      "canary": true
    },
    {
      "id": "nr-05",
      "type": "topic",
      "prompt": "What is a risk burn-down schedule and what triggers the Plan step?",
      "routing": { "any_of": ["ch06"], "all_of": [] },
      "must_include": ["risk tolerance profile over time",
                       "Tolerable / Marginal / Intolerable zones",
                       "Plan step triggered when performance risk exceeds Marginal"],
      "must_use_terms": [{ "term": "burn-down schedule", "synonyms": ["burn down schedule"] }],
      "provenance": "NASA/SP-2011-3422 ch06",
      "must_not_include": ["the burn-down schedule tracks project budget spend"],
      "canary": true
    },
    {
      "id": "nr-06",
      "type": "applied",
      "prompt": "A team writes: 'Given that the thruster vendor is late, the mission will fail.' Critique this against the NASA individual risk statement format and the rule on consequences.",
      "routing": { "any_of": ["ch07"], "all_of": [] },
      "must_include": ["missing explicit DEPARTURE / ASSET / CONSEQUENCE structure",
                       "states an outcome as certain rather than a possibility",
                       "consequence should be written without regard to mitigations / tied to a performance requirement"],
      "must_use_terms": [{ "term": "individual risk statement", "synonyms": [] }],
      "provenance": "NASA/SP-2011-3422 ch07",
      "must_not_include": ["the statement is correctly formed"],
      "canary": true
    },
    {
      "id": "nr-tn-01",
      "type": "trigger-negative",
      "prompt": "Write a Python function to parse a CSV file.",
      "expect_fire": false,
      "canary": false
    },
    {
      "id": "nr-tn-02",
      "type": "trigger-negative",
      "prompt": "What does MIL-STD-882 say about software safety criticality?",
      "expect_fire": false,
      "canary": false
    },
    {
      "id": "nr-tp-01",
      "type": "trigger-positive",
      "prompt": "How should I structure a continuous risk management process for a safety-critical NASA project?",
      "expect_fire": true,
      "canary": false
    }
  ]
}
```

- [ ] **Step 2: Validate the bank structurally**

Run: `python tooling/eval/eval.py validate tooling/eval/banks/nasa-risk.json`
Expected: `PASS  tooling/eval/banks/nasa-risk.json (9 questions)`

- [ ] **Step 3: Human anchor-verification (human-gated)**

Open `packs/nasa-risk/SKILL.md` and the cited chapters (`ch01`, `ch02`, `ch05`, `ch06`, `ch07`, `ch08`). For each scored question, confirm every `must_include` string is a faithful claim of the cited chapter and every `must_not_include` is genuinely absent/contradicted.
Acceptance criterion: every anchor is confirmed against the pack; correct any that drift.
Verify completion: re-run Step 2 (still PASS) after edits.

- [ ] **Step 4: Commit**

```bash
git add tooling/eval/banks/nasa-risk.json
git commit -m "feat: seed nasa-risk eval bank (reference pack, anchors verified)"
```

---

### Task 10: Commit the nasa-risk baseline + prove the gate bites (red→green)

**Files:**
- Create: `tooling/eval/baselines/nasa-risk.baseline.json`
- Create (transient, gitignored): `results/_demo_records.json`

This task is the **definition-of-done proof** from the spec (§8 step 4): the no-regression gate
must demonstrably go RED on a regression and GREEN when restored.

- [ ] **Step 1: Collect a real all-pass record set (driver step)**

Using the in-session subagent driver (see README, Task 13), run each `nasa-risk` question and
its judge, collapse median-of-3, and write the records to `results/_demo_records.json`. For the
purpose of establishing the baseline, this set should be all-PASS (fix any genuine skill issues
first, or quarantine faithfulness items and exclude them from the baseline).

Acceptance criterion: `results/_demo_records.json` is a JSON list of records (one per question id) conforming to `schemas/record.schema.json` — including `judge_method: "anchors-only"` and `faithfulness_saw_loaded_files: false` on every record (else `score` will refuse with exit 2).

- [ ] **Step 2: Generate the baseline from the all-pass run**

Run:
```bash
python tooling/eval/eval.py score tooling/eval/banks/nasa-risk.json results/_demo_records.json \
  --judge-model "$(echo claude-opus-4-8)" --bank-sha "$(git rev-parse --short HEAD)"
```
Then read `results/latest/report.md` and confirm every question is PASS. Hand-write the baseline from those verdicts:

Create `tooling/eval/baselines/nasa-risk.baseline.json`:
```json
{
  "slug": "nasa-risk",
  "expected": {
    "nr-01": "PASS", "nr-02": "PASS", "nr-03": "PASS", "nr-04": "PASS",
    "nr-05": "PASS", "nr-06": "PASS",
    "nr-tn-01": "PASS", "nr-tn-02": "PASS", "nr-tp-01": "PASS"
  }
}
```

- [ ] **Step 3: Prove the gate goes RED on a regression**

Hand-edit `results/_demo_records.json` to set one question's `completeness` to `2` (simulating a skill regression). Then run with the baseline:
```bash
python tooling/eval/eval.py score tooling/eval/banks/nasa-risk.json results/_demo_records.json \
  --baseline tooling/eval/baselines/nasa-risk.baseline.json \
  --judge-model claude-opus-4-8 --bank-sha "$(git rev-parse --short HEAD)"; echo "exit=$?"
```
Expected: prints `baseline: regressions=['<that id>'] ...` and `exit=1` (gate bit).

- [ ] **Step 4: Restore and prove GREEN**

Revert the hand-edit (set completeness back to `5`). Re-run the same command.
Expected: `regressions=[]` and `exit=0` (gate clean). Then `rm -f results/_demo_records.json`.

- [ ] **Step 5: Commit**

```bash
git add tooling/eval/baselines/nasa-risk.baseline.json
git commit -m "feat: nasa-risk baseline + verified red->green no-regression gate"
```

---

### Task 11: 13-pack coverage manifest + coverage command

**Files:**
- Create: `tooling/eval/coverage.json`
- Modify: `tooling/eval/eval.py` (add `coverage` subcommand)
- Test: `tooling/eval/tests/test_coverage.py` (add a class)

- [ ] **Step 1: Write the failing test**

Append to `tooling/eval/tests/test_coverage.py`:
```python
class TestCoverage(unittest.TestCase):
    def test_coverage_counts_seeded_vs_stub(self):
        manifest = {"packs": [
            {"slug": "nasa-risk", "status": "seeded"},
            {"slug": "sebok", "status": "stub"}]}
        summary = ev.coverage_summary(manifest)
        self.assertEqual(summary["seeded"], 1)
        self.assertEqual(summary["stub"], 1)
        self.assertEqual(summary["total"], 2)
        self.assertEqual(summary["suite"], "INCOMPLETE")

    def test_coverage_all_seeded_is_complete(self):
        manifest = {"packs": [{"slug": "a", "status": "seeded"}]}
        self.assertEqual(ev.coverage_summary(manifest)["suite"], "COMPLETE")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tooling.eval.tests.test_coverage -v`
Expected: FAIL — `AttributeError: module 'eval' has no attribute 'coverage_summary'`.

- [ ] **Step 3: Write implementation**

Append to `tooling/eval/eval.py` (before `build_parser`):
```python
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
```
Add to `build_parser` (before `return p`):
```python
    cv = sub.add_parser("coverage", help="print the 13-pack seeding coverage")
    cv.set_defaults(func=_cmd_coverage)
```

Create `tooling/eval/coverage.json`:
```json
{
  "packs": [
    { "slug": "nasa-risk", "status": "seeded" },
    { "slug": "requirements-writing", "status": "stub" },
    { "slug": "sebok", "status": "stub" },
    { "slug": "nasa-se-handbook", "status": "stub" },
    { "slug": "nasa-npr-7123", "status": "stub" },
    { "slug": "nasa-system-safety", "status": "stub" },
    { "slug": "nasa-hsi", "status": "stub" },
    { "slug": "mil-std-882", "status": "stub" },
    { "slug": "dodaf", "status": "stub" },
    { "slug": "nist-ai-rmf", "status": "stub" },
    { "slug": "nist-ssdf", "status": "stub" },
    { "slug": "nist-csf", "status": "stub" },
    { "slug": "eu-ai-act", "status": "stub" }
  ]
}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m unittest tooling.eval.tests.test_coverage -v`
Expected: PASS. Then: `python tooling/eval/eval.py coverage`
Expected: `coverage: 1 seeded / 12 stub / 13 total — INCOMPLETE`

- [ ] **Step 5: Commit**

```bash
git add tooling/eval/eval.py tooling/eval/coverage.json tooling/eval/tests/test_coverage.py
git commit -m "feat: 13-pack coverage manifest + coverage command"
```

---

### Task 12: Fan-out seeds — requirements-writing + sebok banks

**Files:**
- Create: `tooling/eval/banks/requirements-writing.json`
- Create: `tooling/eval/banks/sebok.json`
- Modify: `tooling/eval/coverage.json` (flip both to `seeded`)

Both are human-authored against their packs. `requirements-writing` exercises the simple/clean
routing path; `sebok` (CC BY-NC-SA) is included so the licence-stratification quarantine path
has a real pack to point at when v2 auto-fix lands.

- [ ] **Step 1: Write requirements-writing.json**

Create `tooling/eval/banks/requirements-writing.json`:
```json
{
  "slug": "requirements-writing",
  "status": "complete",
  "questions": [
    {
      "id": "rw-01",
      "type": "topic",
      "prompt": "Which EARS pattern handles a fault or safety condition, and what is its shape?",
      "routing": { "any_of": ["ch03"], "all_of": [] },
      "must_include": ["unwanted-behaviour (If/Then) pattern",
                       "If <condition>, then the <system> shall <response>"],
      "must_use_terms": [{ "term": "unwanted behaviour", "synonyms": ["unwanted behavior"] }],
      "provenance": "pack ch03 (EARS / Mavin et al. 2009)",
      "must_not_include": ["EARS defines a dedicated Severity pattern"],
      "canary": false
    },
    {
      "id": "rw-02",
      "type": "topic",
      "prompt": "Name the EARS patterns by their trigger keyword.",
      "routing": { "any_of": ["ch03"], "all_of": [] },
      "must_include": ["Ubiquitous", "When (event-driven)", "While (state-driven)",
                       "Where (optional-feature)", "If/Then (unwanted-behaviour)"],
      "must_use_terms": [{ "term": "EARS", "synonyms": [] }],
      "provenance": "pack ch03",
      "must_not_include": ["Unless pattern", "Because pattern"],
      "canary": false
    },
    {
      "id": "rw-03",
      "type": "topic",
      "prompt": "What are the verification methods to assign when writing a requirement?",
      "routing": { "any_of": ["ch06"], "all_of": [] },
      "must_include": ["Test", "Analysis", "Inspection", "Demonstration"],
      "must_use_terms": [{ "term": "verification method", "synonyms": [] }],
      "provenance": "pack ch06",
      "must_not_include": ["Validation is one of the four verification methods"],
      "canary": false
    },
    {
      "id": "rw-04",
      "type": "applied",
      "prompt": "Critique: 'The system shall be fast and user-friendly.' Identify the defects and rewrite one as a verifiable EARS requirement.",
      "routing": { "any_of": ["ch05"], "all_of": [] },
      "must_include": ["compound requirement (two needs in one)",
                       "weak/vague words (fast, user-friendly)",
                       "not verifiable / no measurable response"],
      "must_use_terms": [{ "term": "verifiable", "synonyms": ["verifiability"] }],
      "provenance": "pack ch05",
      "must_not_include": ["the requirement is acceptable as written"],
      "canary": true
    },
    {
      "id": "rw-tn-01",
      "type": "trigger-negative",
      "prompt": "How do I configure a GitHub Actions workflow?",
      "expect_fire": false,
      "canary": false
    },
    {
      "id": "rw-tp-01",
      "type": "trigger-positive",
      "prompt": "Help me rewrite these shall-statements so they're unambiguous and verifiable.",
      "expect_fire": true,
      "canary": false
    }
  ]
}
```

- [ ] **Step 2: Write sebok.json**

Create `tooling/eval/banks/sebok.json`:
```json
{
  "slug": "sebok",
  "status": "complete",
  "questions": [
    {
      "id": "sb-01",
      "type": "topic",
      "prompt": "What does SEBoK identify as the distinguishing characteristics of a system of systems (SoS)?",
      "routing": { "any_of": ["ch25"], "all_of": [] },
      "must_include": ["operational independence of constituent systems",
                       "managerial independence of constituent systems"],
      "must_use_terms": [{ "term": "system of systems", "synonyms": ["SoS"] }],
      "provenance": "SEBoK v2.13 ch25",
      "must_not_include": ["a system of systems has a single owning authority over all constituents"],
      "canary": false
    },
    {
      "id": "sb-02",
      "type": "topic",
      "prompt": "How does SEBoK distinguish verification from validation?",
      "routing": { "any_of": ["ch16", "ch18"], "all_of": [] },
      "must_include": ["verification — building the system right / conforms to specification",
                       "validation — building the right system / meets stakeholder needs"],
      "must_use_terms": [{ "term": "verification", "synonyms": [] },
                         { "term": "validation", "synonyms": [] }],
      "provenance": "SEBoK v2.13 (technical processes)",
      "must_not_include": ["verification and validation are interchangeable terms"],
      "canary": true
    },
    {
      "id": "sb-03",
      "type": "topic",
      "prompt": "What is MBSE according to SEBoK, and how does it differ from document-centric SE?",
      "routing": { "any_of": ["ch06", "ch18"], "all_of": [] },
      "must_include": ["formalised application of modelling",
                       "model as the authoritative source rather than documents"],
      "must_use_terms": [{ "term": "MBSE", "synonyms": ["model-based systems engineering"] }],
      "provenance": "SEBoK v2.13 (representing systems / MBSE)",
      "must_not_include": ["MBSE means generating more documents automatically"],
      "canary": true
    },
    {
      "id": "sb-tn-01",
      "type": "trigger-negative",
      "prompt": "What's the capital of France?",
      "expect_fire": false,
      "canary": false
    }
  ]
}
```

- [ ] **Step 3: Validate both banks**

Run:
```bash
python tooling/eval/eval.py validate tooling/eval/banks/requirements-writing.json
python tooling/eval/eval.py validate tooling/eval/banks/sebok.json
```
Expected: both `PASS`.

- [ ] **Step 4: Human anchor-verification (human-gated)**

Verify each anchor against `packs/requirements-writing/` and `packs/sebok/` chapters. For `sebok`, confirm the cited chapter numbers actually contain the claims (SEBoK chapter numbering is in `packs/sebok/chapters/`). Correct any drift.
Acceptance criterion: every anchor confirmed; re-run Step 3 (still PASS).

- [ ] **Step 5: Flip coverage to seeded and commit**

Edit `tooling/eval/coverage.json`: change `requirements-writing` and `sebok` from `"stub"` to `"seeded"`.
Run: `python tooling/eval/eval.py coverage`
Expected: `coverage: 3 seeded / 10 stub / 13 total — INCOMPLETE`
```bash
git add tooling/eval/banks/requirements-writing.json tooling/eval/banks/sebok.json tooling/eval/coverage.json
git commit -m "feat: fan-out seed banks (requirements-writing, sebok) + coverage update"
```

---

### Task 13: README — run / add questions / read reports / quarantine / driver protocol

**Files:**
- Create: `tooling/eval/README.md`
- Create: `tooling/eval/rubric.md`

- [ ] **Step 1: Write rubric.md**

Create `tooling/eval/rubric.md` with the explanatory rubric. It must state, at minimum: the four dimensions and their 1–5 anchors (faithfulness, routing, completeness) + triggering PASS/FAIL; the **faithfulness-scored-only-against-human-anchors** rule; the **loaded-file-list withheld from the faithfulness pass** rule; determinism (temp 0, median-of-3); and that the machine-checkable thresholds live in `eval.py` (`GATE_FLOOR`, `CANARY_MIN_LOAD_BEARING`) and `schemas/`. (Author this from spec §4 — it is explanatory prose, not duplicated logic.)

- [ ] **Step 2: Write README.md**

Create `tooling/eval/README.md` covering:
- **What this is / is not** (v1 read-only; no auto-fix; no LLM calls inside `eval.py`).
- **CI status:** the gate runs **locally**, not in CI — the workflow file is shipped as `.github/workflows/validate.yml.disabled` (the `.disabled` suffix means GitHub does not run it); re-enabling it is a separate task. Name the file exactly so a reader can find it.
- **Routing targets are not cross-checked against chapter files.** `eval.py` treats routing as an opaque 1–5 score from the judge; it never compares a bank's `routing.any_of`/`all_of` against the pack's real chapter filenames. A typo like `any_of:["ch99"]` is caught only by the human anchor-verification step (Tasks 9/12 Step 4), not by any command. Say this so authors verify routing manually.
- **Run it:** `validate`, `runplan`, `score`, `coverage` command examples (copy the exact commands from Tasks 8/10/11).
- **The driver protocol** (how a human/agent collects records): for each item in `runplan` output, dispatch an answerer subagent that loads only `packs/<slug>/` and answers; capture `loaded_files`, `answer`, `fired`; then dispatch a judge subagent **3 times** (temp 0) with the question + human anchors + answer (and, for routing only, `loaded_files`), take the median per scored dimension; write the collapsed record. Emphasise: **the judge is never given the loaded chapter text for the faithfulness pass.**
- **Add a question:** point at `nr-06` in `banks/nasa-risk.json` as the copy-paste template; list required fields per type; note `provenance` is mandatory on scored questions.
- **Read a report:** `results/latest/report.md` (denominator, failures-first) and `results/latest/faithfulness-review.md` (verdict-only quarantine — never commit answer text).
- **Refresh a baseline:** when `score` reports `fixed`/`new`, update `baselines/<slug>.baseline.json` to match the new verdicts.
- **Exit codes:** `score` returns `0` (clean), `1` (a real regression vs baseline), or `2` (records are **unattested** — missing/contradicting `judge_method: "anchors-only"` / `faithfulness_saw_loaded_files: false`; the run is untrusted, not merely failing). A future CI step treats any non-zero as red, but the codes are distinct for humans.
- **Schemas are reference contracts, not runtime validators.** `schemas/bank.schema.json` and `schemas/record.schema.json` document the shapes; runtime enforcement lives in `eval.py` (`validate_bank` reimplements the bank rules in Python; `attestation_errors` enforces the record attestation in `score`). The record schema's `const` fields are not executed at runtime — they exist so a contributor can see what the driver must produce.

- [ ] **Step 3: Verify the full suite + all commands still work**

Run:
```bash
python -m unittest discover -s tooling/eval/tests -t .
python tooling/eval/eval.py coverage
python tooling/eval/eval.py validate tooling/eval/banks/nasa-risk.json
```
Expected: all tests PASS; coverage prints `3 seeded / 10 stub`; bank validates.

- [ ] **Step 4: Enrol eval.py in the release header gate (it is NOT auto-scanned)**

`tooling/check_release.py`'s header check iterates a **hardcoded `authored` list** (around line 131) — it does **not** glob `tooling/**`, so `eval.py` is not header-checked unless you add it. (The leak-sentinel and source-host *link* scans DO `rglob` the whole repo, so they already cover every new file — see Step 4b.) Make the JGSC+SPDX convention actually enforced: add `eval.py` to the list.

Edit `tooling/check_release.py`, in the `authored = [...]` block, after the `ROOT / "tooling/check_release.py",` line, add:
```python
                ROOT / "tooling/eval/eval.py",
```
Then run: `python tooling/check_release.py`
Expected: still passes (eval.py carries the JGSC+SPDX header per the Conventions section); the run now *enforces* it. (Test files under `tooling/eval/tests/` are intentionally NOT added — they are test scaffolding, consistent with the repo not header-checking its own test helpers.)

- [ ] **Step 4b: Confirm no source-corpus URLs leaked into the new files**

`check_release.py`'s link gate (`SOURCE_HOSTS`) fails the release if any scanned file contains a URL to `nasa.gov`, `nist.gov`, `sebokwiki`, `eur-lex`, `dau.edu`, etc. The seeded banks use bare citations (`"NASA/SP-2011-3422 ch05"`) with **no URLs** — keep it that way. **Do not** put source-corpus links in `README.md`, `rubric.md`, or any bank; cite by document name + chapter only.
Run: `python tooling/check_release.py`
Expected: no `[link]` failure naming a `tooling/eval/` file.

- [ ] **Step 5: Commit**

```bash
git add tooling/eval/README.md tooling/eval/rubric.md tooling/check_release.py
git commit -m "docs: eval harness README (driver protocol, CI status) + rubric; enrol eval.py in header gate"
```

---

## Self-review

**Spec coverage** (spec §-by-§):
- §2 architecture/layout → Tasks 1–8, 11, 13 (eval.py, schemas, results/, coverage.json, README/rubric). ✓
- §3 bank format (set routing, must_include vs must_use_terms+synonyms, provenance, applied type, canary, status) → schema (Task 8) + validation (Task 2) + seeded banks (Tasks 9, 12). ✓
- §4 rubric (faithfulness-vs-anchors, file-list walled off, dims, aggregation, anchor-integrity) → scoring/disposition (Tasks 3–4), aggregation (Task 5), rubric.md + driver protocol (Task 13). ✓ *(temp-0/median-of-3 are driver-side, documented in Task 13. The two headline guarantees — faithfulness-scored-only-vs-anchors and file-list-walling — are enforced driver-side AND **attested in-band**: every record must carry `judge_method: "anchors-only"` + `faithfulness_saw_loaded_files: false`, and `eval.py score` REFUSES (exit 2) records that don't — Task 4 `attestation_errors`, schema `const` in Task 8, gate in Task 8 `_cmd_score`. This converts the guarantee from documented to attested.)*
- §5 reports (denominator, INCOMPLETE, latest/, model+SHA) → Tasks 5, 7, 8. ✓
- §6 v1 read-only loop + quarantine → Tasks 4, 7, 8 (no auto-fix anywhere; v2 explicitly out of scope). ✓
- §7 repo-fit (stdlib, stub tolerance, gitignore results, verdict-only digest) → Tasks 1, 2, 5, 7. ✓
- §8 rollout (nasa-risk first + red→green proof, fan-out, manifest, applied probe, CI-is-local) → Tasks 9–13. ✓

**Placeholder scan:** The one deliberate broken-placeholder in Task 8 `_cmd_score` is *intentional and immediately corrected in the same step's implementation note* with the exact replacement code — it is a guard against blind copy, not an unresolved placeholder. Human-gated steps (Tasks 9/10/12 anchor verification, record collection) name the exact resource (`packs/<slug>/` chapters), state acceptance criteria, and give the verify command — valid per the skill's human-gated exception. No "TBD"/"add error handling"/"similar to" placeholders. ✓

**Type consistency:** `validate_bank`, `gate_verdict`, `trend_scalar`, `disposition`, `attestation_errors`, `aggregate`, `suite_status`, `canary_is_load_bearing`, `baseline_diff`, `baseline_gate_ok`, `render_report`, `render_quarantine`, `coverage_summary` — names are used identically across the test that defines them and any later task that references them. (`attestation_errors` defined in Task 4, called in Task 8 `_cmd_score`; `REQUIRED_JUDGE_METHOD = "anchors-only"` matches the schema `const` and the README prose.) Record shape (`judge.faithfulness|routing|completeness|triggering|unmapped_claims|must_not_include_hits|must_use_terms_missing`) is identical in the schema (Task 8), every scoring test (Tasks 3–7), and the seeded records (Task 10). Constants `GATE_FLOOR`, `CANARY_MIN_LOAD_BEARING` defined once, referenced consistently. ✓

<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Eval judge rubric

This is the **explanatory** rubric for the human/agent driver that judges skill answers.
The machine-checkable thresholds live in `eval.py` (`GATE_FLOOR`, `CANARY_MIN_LOAD_BEARING`,
`REQUIRED_JUDGE_METHOD`) and in `schemas/`. Where this prose and the code disagree, the code wins.

## The four dimensions

A judge scores each scored question (`topic` / `chapter` / `applied`) on three 1–5 dimensions;
trigger questions (`trigger-positive` / `trigger-negative`) are scored only on triggering.

### Faithfulness (1–5) — QUARANTINE-ONLY, never auto-edited

**Critical rule: score faithfulness ONLY against the human-authored anchors**
(`must_include`, `must_use_terms`, `must_not_include`, `provenance`) — **never against the loaded
chapter text.** The loaded chapter could itself be wrong relative to the real upstream source;
trusting it would make faithfulness unfalsifiable.

- 5 — every load-bearing claim maps to an anchor; attribution matches `provenance`; all
  `must_use_terms` (or a listed synonym) present; no `must_not_include` hit. A score ≥4 requires
  the judge to **enumerate any load-bearing claim it could not map to an anchor** and cap if any exist.
- 2 (hard cap) — any `must_not_include` hit, or any misattribution vs `provenance`.
- 1 — fabricated or contradicted content.
- Confidence and citation *formatting* are NOT evidence of faithfulness.

### Routing (1–5)

`routing` is a **set** (`any_of` / `all_of`). 5 = satisfied `any_of` and all `all_of`, nothing
irrelevant; 4 = correct + a harmless adjacent extra; 2 = missing a required `all_of` chapter; 1 = wrong.

### Completeness (1–5) — conditioned on responsiveness

Fraction of `must_include` present by **semantic** match, with a required evidence quote per matched
point. Length must not raise the score; a near-dump caps at 4 via a precision penalty.

### Triggering (PASS/FAIL)

Binary gate. PASS iff the skill's firing matches `expect_fire` on **both** must-fire and
must-not-fire cases. Score with **all 13 pack descriptions present** so inter-pack collision is visible.

## Determinism

Run the judge at **temperature 0**. Score faithfulness and completeness as the **median of 3**
judge runs (at the per-point match decision, not just the final number). Record the judge model id
and the bank git SHA in every report.

## Aggregation & disposition

A question FAILS if `faithfulness ≤ 2` OR `routing ≤ 2` OR `completeness ≤ 2` OR `triggering = FAIL`.
A `must_not_include` hit or a faithfulness ≤ 2 routes to **QUARANTINE** (human review, never auto-fixed).
A `must_use_terms` miss on an otherwise-strong answer routes to **ANCHOR_REVIEW** (suspect a stale
anchor — review the bank, not the skill). See `disposition()` in `eval.py`.

## Anchor integrity

The rubric is only as trustworthy as the anchors. Periodically audit the banks against the source
packs, independent of any eval run. When the harness flags ANCHOR_REVIEW, fix the bank if the anchor
drifted from what the pack actually says (this happened during seeding: a SEBoK V&V anchor and a
NASA-risk `must_not_include` trap were both corrected against the real chapters).

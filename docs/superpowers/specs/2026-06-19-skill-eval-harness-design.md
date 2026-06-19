<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../../../LICENSE).
SPDX-License-Identifier: MIT
-->

# Closed-Loop Eval Harness for the SE Knowledge Packs — Design

**Status:** Approved design (brainstormed 2026-06-19; hardened over 3 BMAD party-mode review rounds).
**Author:** JG Systems Consulting Ltd.
**Scope:** A test harness that runs the knowledge-pack skills, grades the answers with an
LLM-as-judge against human-authored ground truth, surfaces weaknesses, and closes the loop
back to skill improvement.

---

## 1. Problem & goal

The repo ships 13 pure-Markdown "knowledge oracle" Claude Code skills (plus one signpost).
Each skill = `SKILL.md` (always loaded; carries a topic index + chapter index) +
`chapters/chNN-*.md` (loaded on demand) + `glossary.md`/`patterns.md`/`cheatsheet.md`.
"Running" a skill = an agent loads the pack, **routes** to the right chapter, and **answers**.

There is structural validation (`tooling/validate_pack.py`) but **no test of answer quality**.
We want a repeatable way to:

1. **Run** each skill against a bank of questions (via Claude subagents, in-session).
2. **Grade** the answers on four dimensions: **faithfulness, routing/retrieval, completeness, triggering**.
3. **Surface** weaknesses ranked by severity.
4. **Close the loop** back to skill improvement — read-only in v1 (human fixes), auto-fix in v2.

### Decisions locked during brainstorming
- Grade all four dimensions (faithfulness, routing, completeness, triggering).
- Execution model: **Claude subagents, in-session** (closest to real user experience; no API key).
- Question bank: **hand-curated, version-controlled** (a trustworthy regression suite).
- Loop: user asked for **auto-fix then re-test**, with **faithfulness failures quarantined**
  (never auto-edited). *Hardening note (§6): auto-fix is deferred to **v2**; v1 is read-only
  with human fixes via quarantine. The gate still bites; this removes the highest-risk
  component from the first cut. This is a deliberate change from the literal v1 ask, agreed
  during review.*

---

## 2. Architecture & layout

```
tooling/eval/
  eval.py                  # stdlib-Python harness: load banks, score, report, baseline-diff
  rubric.md                # judge rubric (explanatory; machine-checkable rules live in schemas/)
  schemas/
    bank.schema.json       # JSON Schema for a question bank
    answer.schema.json     # structured output an answerer subagent returns
    judge.schema.json      # structured output a judge subagent returns
  banks/
    nasa-risk.json         # FULLY seeded (v1 reference pack)
    requirements-writing.json
    sebok.json
  baselines/
    <slug>.baseline.json   # committed expected pass/fail per question id (CI/local gate)
  coverage.json            # manifest of all 13 packs: status seeded|stub
  README.md                # how to run, add questions, read reports, quarantine process
results/                   # git-ADD a .gitignore entry for this tree (see §7)
  latest/                  # stable pointer (overwritten each run)
  <runid>/
    report.md              # scored matrix; findings ranked by severity; N/13 denominator
    faithfulness-review.md # QUARANTINE — verdict-only digest, NO source quotations
```

**Why stdlib Python, not a `.mjs`/Workflow script.** The repo has a hard, stated constraint:
all tooling is stdlib Python with **zero third-party dependencies** (`validate_pack.py` even
hand-rolls a YAML subset parser to avoid PyYAML, and CI runs it directly). The harness matches
that contract: `eval.py` does bank loading (stdlib `json`), scoring math, report + baseline
generation. The subagent answer/judge calls are orchestrated in-session by the agent driving
`eval.py` (the script emits a run-plan and consumes structured results). No Node, no npm.

### Data flow (v1, read-only)
```
load banks (json)
  -> for each question: answerer subagent loads the pack, routes, answers  (parallel)
  -> for each answer:   judge subagent(s) grade vs HUMAN anchors           (parallel)
                        (faithfulness & completeness: median of 3; temp 0)
  -> aggregate -> report.md (ranked findings, N/13 denominator)
  -> diff vs committed baseline -> PASS/FAIL gate (no-regression)
  -> faithfulness failures -> faithfulness-review.md (quarantine, human review)
```

---

## 3. Question bank format (JSON, stdlib-parseable)

One bank per pack. Ground truth is **human-authored** and is the *only* oracle for faithfulness
(see §4). Example:

```json
{
  "slug": "requirements-writing",
  "status": "complete",
  "questions": [
    {
      "id": "rw-01",
      "type": "topic",
      "prompt": "What EARS pattern handles a fault or safety condition, and what is its shape?",
      "routing": { "any_of": ["ch03"], "all_of": [] },
      "must_include": ["If/Then unwanted-behaviour pattern", "If <condition>, then the <system> shall <response>"],
      "must_use_terms": [{ "term": "unwanted behaviour", "synonyms": ["unwanted behavior"] }],
      "provenance": "EARS / Mavin et al. 2009; pack ch03",
      "must_not_include": ["EARS Severity pattern"],
      "canary": false
    },
    {
      "id": "rw-ap-01",
      "type": "applied",
      "prompt": "A requirement says 'the system shall be fast and user-friendly.' Identify the defects.",
      "routing": { "any_of": ["ch05"], "all_of": [] },
      "must_include": ["compound requirement (two needs)", "weak/vague words (fast, user-friendly)", "unverifiable"],
      "provenance": "pack ch05 defect catalogue",
      "canary": true
    },
    {
      "id": "rw-tn-01",
      "type": "trigger-negative",
      "prompt": "Write a Python function to parse a CSV.",
      "expect_fire": false,
      "canary": false
    }
  ]
}
```

### Question types
- `topic` / `chapter` — exercise routing + completeness + faithfulness.
- `applied` — a question whose answer is **applied judgment**, not a definitional restatement
  (e.g. classify a hazard's severity×probability, or whether a system is EU AI Act Annex III
  high-risk). Proves the schema/rubric can represent non-extractive answers. **At least one
  `applied` probe must be in the v1 seed** (see §8 C3).
- `trigger-positive` / `trigger-negative` — exercise triggering only (`expect_fire`),
  scored **with all 13 pack descriptions present** so inter-pack collision is visible.

### Fields & semantics
- `routing`: `{ any_of:[chNN], all_of:[chNN] }` — a **set**, because packs route one topic to
  many chapters (verified in `nasa-risk`'s index). Scalar `expect_chapter` was rejected.
- `must_include[]`: **concept coverage** → completeness. Semantic match, evidence-quote required.
- `must_use_terms[]`: **verbatim terminology** → faithfulness; `synonyms` allow current
  terminology not to be penalized against a stale anchor.
- `must_not_include[]`: hallucination traps → faithfulness **floor only** (a hit caps
  faithfulness; absence is *not* evidence of correctness).
- `provenance`: source clause/section id, so the misattribution cap is enforceable **from the
  anchor**, not from the judge's own memory of the standard.
- `canary`: held-out from any future auto-fix; informational gate unless ≥5 per pack (§6).
- bank-level `status`: `complete | seed` (a stub) — drives the `INCOMPLETE` aggregate rule.

---

## 4. Judge rubric

The judge is a Claude subagent given the **question + human ground truth + the skill's answer**.
Determinism: judge pinned to **temperature 0**; faithfulness & completeness scored by the
**median of 3** judge runs (at the per-point match decision, not just the final score);
triggering also majority-of-3. Model id + bank git SHA recorded in every report.

**Critical rule: faithfulness is scored ONLY against the human anchors**
(`must_include` / `must_use_terms` / `must_not_include` / `provenance`), **never against the
loaded chapter** — because the loaded chapter could itself be wrong vs the real upstream source.
The loaded-file list is given **only to the routing judge**, walled off from the faithfulness
pass (otherwise the judge infers chapter-derived credit and the anchor-only rule is nominal).

### Dimensions
- **FAITHFULNESS (1–5, QUARANTINE-ONLY, never auto-edited).**
  5 = every load-bearing claim maps to an anchor, attribution matches `provenance`, all
  `must_use_terms` (or synonyms) present, no `must_not_include` hit. ≥4 requires the judge to
  **enumerate any load-bearing claim it could NOT map to an anchor** and cap if any exist
  (closes the out-of-anchor hallucination channel). Hard cap at 2 for any `must_not_include`
  hit or any misattribution vs `provenance`. Confidence/citation formatting are NOT evidence.
- **ROUTING (1–5; set-based).** 5 = satisfied `any_of` and all `all_of`, nothing irrelevant;
  4 = correct + harmless adjacent extra; 2 = missing a required `all_of` chapter; 1 = wrong.
- **COMPLETENESS (1–5; conditioned on responsiveness).** Fraction of `must_include` present by
  semantic match with a required evidence quote per point. Length must not raise the score; a
  near-dump caps at 4 via a precision penalty (defined measurably in `rubric.md`).
- **TRIGGERING (binary → gate, reported PASS/FAIL).** PASS iff `fire` matches `expect_fire` on
  both must-fire and must-not-fire cases, scored with all 13 descriptions present.

### Aggregation
Report the full vector. A question **FAILS** if `faithfulness≤2 OR routing≤2 OR completeness≤2
OR triggering=FAIL`. Trend scalar = `0 if gated-fail else mean(faithfulness, routing,
completeness)` so a single 2 cannot be averaged away. A separate **triggering-health** metric
is reported so chronic collision-misfire on otherwise-passing questions stays visible.

### Anchor-integrity (the rubric is only as good as the anchors)
- A `must_not_include` hit **or** a `must_use_terms` miss **on an otherwise-strong answer**
  routes to **human anchor review**, not a model-fault verdict — it may be a stale/wrong anchor.
- Periodic **bank-vs-source audit**, independent of the eval run, guards against the bank itself
  becoming a wrong attractor.

---

## 5. Reports & findings

`report.md` per run: a scored matrix (pack × question × dimension), findings ranked by severity
(gated fails first), the **`N/13` evaluated denominator**, the resolved judge model id, and the
bank git SHA. `results/latest/` is overwritten each run for easy diffing; timestamped run dirs
keep history. The aggregate status is **`INCOMPLETE`** (never `PASS`) while any pack is
`status: seed` — no green run can be cited as suite-complete (§8 C2).

---

## 6. The loop — v1 (read-only) and v2 (auto-fix)

### v1 — read-only (this design's first cut)
Failures are **reported and quarantined for human fix**. No file in any pack is auto-edited.
This preserves the entire safety value (the gate bites; regressions are caught) while removing
the highest-blast-radius component. Faithfulness failures go to `faithfulness-review.md` as a
**verdict-only digest** (no source quotations — honors the raw-source prohibition, §7).

### v2 — auto-fix then re-test (deferred, designed here so v1 doesn't preclude it)
When added, auto-fix obeys these hardened rules:

- **Boundary on EDIT-TYPE, not dimension.** Auto-fixable **iff** the edit is
  EXTRACTIVE/STRUCTURAL: (i) an index line whose target anchor **provably exists** in a chapter;
  (ii) a frontmatter description change whose claimed topics are backed by real chapter headings
  **with a minimum content threshold** (not stub headings); (iii) summary text that is a
  **complete-semantic-unit** verbatim/near-verbatim extract of existing source **with citation**.
  Anything that introduces a net-new factual assertion, edits chapter body, is faithfulness-
  flagged, or can't be mechanically verified extractive → **QUARANTINE, fail-closed**.
- **Licence-stratified extraction.** Verbatim content extraction into `SKILL.md` is auto-fixable
  **only for public-domain packs**. For CC BY-NC-SA / attribution-required packs (e.g. `sebok`,
  `eu-ai-act`) all content-bearing extraction is **quarantined** — a verbatim copy into a
  differently-governed region is exactly the share-alike/attribution event. Validator reads the
  pack's `license_tier` and fails closed. **A negative test is mandatory**: a `sebok` content
  question where auto-fix is attempted and must be refused, asserting no extractive edit occurred.
- **Re-test scope.** Any `SKILL.md` edit (shared state) forces a **full-pack re-run**; any
  description/index edit forces a **global re-run of all 13** (inter-pack collision). No green
  claim without a clean full-bank pass.
- **Termination.** Halts on SUCCESS (full-bank green AND canary not regressed vs run-start
  baseline); FIX-BUDGET (≥2 attempts/question or ≥N edits/skill → escalate to human); NO-PROGRESS
  (round delta ≤ empirically-measured judge-noise epsilon); OSCILLATION (a
  `(question, dimension, edit-hash)` repeats, or a previously-green question regresses);
  REGRESSION-FLOOR (any fix lowering full-bank score below baseline is reverted, path abandoned).
  A separate **re-run budget** is funded independently of the edit budget; on budget-trip-before-
  green, the skill's **entire auto-fix set is reverted** so main never depends on a half-applied
  series. Never terminates fully green while a faithfulness item is open → status
  **`green-with-open-quarantine`**.
- **Provenance.** Auto-fixes land on branch `eval/autofix-<runid>`, one atomic commit per fix
  (message: skill, dimension, question id, score delta; intermediate commits marked provisional,
  authoritative score on a final seal commit), with a tracked `FIX-LEDGER.md` (before/after
  snippet + classification + validator result). The run **opens a PR, never auto-merges**. The
  quarantine record is **committed to the branch** (verdict-only), not left only in gitignored
  `results/`.
- **Anti-overfit.** A rotating canary slice is **load-bearing only at ≥5 absolute held-out
  items**; below that, green is marked `overfit-unverified` and the canary is informational-only.

---

## 7. Repo-fit & safety constraints

- **Zero third-party deps**, stdlib Python only — matches `tooling/validate_pack.py` and CI.
- **Stub tolerance.** `coverage.json` lists all 13 packs with `status seeded|stub`. The schema's
  `status` enum + a validator branch make `status: seed` a **non-fatal WARN** (with a test that a
  stub bank passes validation while still emitting the warning) so stubs are *visibly* incomplete,
  never silently empty and never build-breaking.
- **Raw-source prohibition.** `.gitignore` blocks `**/.build/` and `*.full_text.txt` because raw
  source text must never be committed. The harness **must add `results/` to `.gitignore`**
  (it is not currently ignored) and any committed digest (quarantine, ledger) is **verdict-only,
  no source quotations**.
- **Licence stratification** of pack content (CC BY-NC-SA `sebok`; attribution-required
  `eu-ai-act`; public-domain US-gov packs; original CC BY 4.0 `requirements-writing`) governs
  what v2 auto-fix may touch (§6).

---

## 8. Rollout & seed plan

### v1 minimal first cut — prove the loop on ONE pack, then fan out
1. Build `eval.py` + `schemas/` + `rubric.md`.
2. **Fully seed `nasa-risk`** (public-domain → no licence edge cases): ~10 questions incl.
   `topic`/`chapter`, **≥1 `applied` probe**, trigger-negatives, ≥5 canary items **in this pack**,
   `provenance` on every anchor.
3. Commit `nasa-risk.baseline.json`.
4. **Definition of done = the gate demonstrably bites:** induce a known regression (a bad answer
   or a reverted skill edit), show the gate goes **RED**, restore, show **GREEN**. Demonstrate the
   canary is load-bearing at ≥5 items.
5. Wire the gate as a **local/pre-commit gate**, and **document that CI is not enforced yet**
   (the repo's `validate.yml` is shipped **disabled**; re-enabling it — and capturing *why* it was
   disabled — is a separate, explicit step, not a silent flip).
6. README points at a specific seeded question as the copy-paste template for contributors.

### Fan-out
7. Seed `requirements-writing` (original CC BY 4.0, clean routing) and `sebok` (CC BY-NC-SA —
   exercises the licence-stratification *quarantine* path; its v2 negative test is added when
   auto-fix lands).
8. Remaining 10 packs: a single `coverage.json` manifest marks them `stub` (cheaper than 10 stub
   files and one schema surface to maintain). Materialize a per-pack bank when work on it starts.

### Out of scope for v1
- Auto-fix and its licence negative-test (→ v2).
- CI enforcement (→ separate task to re-enable `validate.yml`).
- API/CI standalone runner (the chosen model is in-session subagents).

---

## 9. Review provenance

Hardened across three BMAD party-mode rounds. Criticals resolved:
- Faithfulness scored vs human anchors only; loaded-file list walled off (R1/R2).
- `routing` is a set, not a scalar (R1).
- stdlib Python + JSON banks, not `.mjs`/YAML (R1).
- Auto-fix boundary is edit-type + **licence-stratified**; verbatim extraction from NC/share-alike
  packs is quarantined (R1/R2).
- Deterministic judge (temp 0) + median-of-3; full-pack re-run on shared-state edits (R1/R2).
- Anchor-integrity escalation; bank-vs-source audit (R2).
- Convergence funded (separate re-run budget; auto-revert on budget trip); canary load-bearing
  only at ≥5 items (R2).
- CI is disabled → v1 is a local gate, not a CI gate (R3, verified).
- `INCOMPLETE` aggregate while any pack is a stub (R3).
- Seeds were all extractive → add an `applied` question type + probe (R3).
- Auto-fix deferred to v2; v1 read-only with human fixes via quarantine (R3, YAGNI).

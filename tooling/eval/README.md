<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Knowledge-pack eval harness (v1, read-only)

A closed-loop quality harness for the knowledge-pack skills. It runs a skill against a bank of
hand-curated questions, grades the answers against human-authored ground truth on four dimensions
(faithfulness, routing, completeness, triggering), gates the run against a committed baseline, and
quarantines faithfulness problems for human review.

## What this is — and is NOT

- **Is:** a deterministic scoring core (`eval.py`) + version-controlled JSON question banks + a
  committed baseline gate. `eval.py` **never calls an LLM** — it scores pre-collected records, so
  it is fully unit-testable (`python -m unittest discover -s tooling/eval/tests -t .`).
- **Is NOT (v1):** there is **no auto-fix**. Failures are reported and quarantined for a human to
  fix. (Auto-fix — with licence-stratified, extractive-only edits — is a planned v2.)

## CI status

The gate runs **locally**, not in CI. The repo's workflow is shipped as
`.github/workflows/validate.yml.disabled` — the `.disabled` suffix means GitHub does not run it.
Wiring the eval gate into CI (and re-enabling that workflow) is a separate, deliberate task.

## Commands

```bash
# structurally validate a bank
python tooling/eval/eval.py validate tooling/eval/banks/nasa-risk.json

# emit the dispatch plan (the questions a driver must run)
python tooling/eval/eval.py runplan tooling/eval/banks/nasa-risk.json

# score collected records and gate against the baseline
python tooling/eval/eval.py score \
  tooling/eval/banks/nasa-risk.json results/_records.json \
  --baseline tooling/eval/baselines/nasa-risk.baseline.json \
  --judge-model claude-opus-4-8 --bank-sha "$(git rev-parse --short HEAD)"

# show 13-pack seeding coverage
python tooling/eval/eval.py coverage
```

### Exit codes (`score`)

- `0` — clean (no regression vs baseline).
- `1` — a real regression vs baseline (the gate bit).
- `2` — records are **unattested** (missing/contradicting `judge_method: "anchors-only"` /
  `faithfulness_saw_loaded_files: false`). The run is *untrusted*, not merely failing. A CI step
  treats any non-zero as red, but the codes are distinct for humans.

## The driver protocol (how records get collected)

`eval.py` does not run skills. A human or agent **driver** produces the records it scores:

1. Run `runplan` to get the list of questions.
2. For each question, dispatch an **answerer** subagent that loads ONLY `packs/<slug>/` and answers.
   Capture `loaded_files`, `answer`, and (for trigger questions) whether the skill `fired`.
3. Dispatch a **judge** subagent **3 times at temperature 0** with the question + the human anchors
   + the answer. **For routing only**, give it `loaded_files`. **Never give the loaded chapter text
   to the faithfulness pass** — faithfulness is scored only against the anchors. Take the median per
   scored dimension.
4. Write each collapsed record with the attestation fields `judge_method: "anchors-only"` and
   `faithfulness_saw_loaded_files: false`. `score` refuses (exit 2) any record lacking them.

## Adding a question

Copy the `nr-06` block in `banks/nasa-risk.json` as your template (it is an `applied` question with
every field filled). Required fields by type:

- `topic` / `chapter` / `applied`: `id`, `type`, `prompt`, `routing` (`any_of`/`all_of`),
  `must_include`, `provenance` (mandatory). Optional: `must_use_terms`, `must_not_include`, `canary`.
- `trigger-positive` / `trigger-negative`: `id`, `type`, `prompt`, `expect_fire`.

**Routing targets are NOT cross-checked against chapter files.** `eval.py` treats routing as an
opaque 1–5 score from the judge; it never compares `routing.any_of` against the pack's real chapter
filenames. A typo like `any_of: ["ch99"]` is caught only by human anchor verification, not by any
command — so verify routing by hand when authoring.

## Reading a report

After `score`, see `results/latest/report.md` (suite status with the `N/13` denominator,
failures-first, judge model, bank SHA) and, if anything needs review,
`results/latest/faithfulness-review.md` (a **verdict-only** quarantine digest — no answer text or
source quotations, by design). `results/` is gitignored; never commit report or quarantine files.

## Refreshing a baseline

When `score` reports `fixed` or `new` question ids, update `baselines/<slug>.baseline.json` to match
the new verdicts. The gate bites only on **regressions** (was PASS, now FAIL), so `fixed`/`new` don't
fail the run — they signal the baseline is stale.

## Schemas are reference contracts

`schemas/bank.schema.json` and `schemas/record.schema.json` document the shapes. Runtime enforcement
lives in `eval.py` (`validate_bank` reimplements the bank rules in Python; `attestation_errors`
enforces the record attestation in `score`). The record schema's `const` fields are not executed at
runtime — they exist so a contributor can see what the driver must produce.

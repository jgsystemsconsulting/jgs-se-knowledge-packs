# Phase 8 Plan Review (8-01-PLAN.md)

Date: 2026-08-14
Plan reviewed: `.planning/phases/8-agent-enablement-surface/8-01-PLAN.md`
Method: adversarial plan-mode review. Every load-bearing plan claim re-verified against the live tree (`docs/capability-pack-map.json`, `packs/` filesystem, `capability-gap-report.md` §1, 7-GAP_ANALYSIS routing, REQUIREMENTS AE-01..03, ROLE-AGENTS-REQUIREMENTS-V2 FR-2.x). The gate design (Task 1) was traced entry-by-entry against the 570 existing map rows.

**Verdict:** NEEDS_WORK

## Claim re-verification (live)

| Plan claim | Result |
|---|---|
| Map is keyless v1: 32 clusters, 570 entries | CONFIRMED (`['clusters'] 32 570`) |
| 7 missing packs (the named slugs), 0 stale, 61 chapter-bearing packs | CONFIRMED (63 pack dirs = 61 + `omg-signpost`, `se-standards-signpost`) |
| New-pack chapter counts 10/8/8/7/7/6/6 = 52 | CONFIRMED by glob |
| Baselines 25=0, 3=2, 5=2, 15=1 | CONFIRMED (gap-report §1 rows + map md summary) |
| All four threshold cluster names exact-match JSON names | CONFIRMED (dict-key probe) |
| Support-file suffix literal ` (support file)`, 102 rows | CONFIRMED — but see BL-01: the files live at **pack root**, not in `chapters/` (verified: 0 of 63 packs have `glossary.md` inside `chapters/`; 61 have it at pack root; all 102 referenced support files exist at pack root) |

## Findings

### BL-01 — BLOCKER: support-file existence check resolves against the wrong directory; the gate can never go green

**File:** `8-01-PLAN.md:94-97` (Task 1 step 3)
**Issue:** The gate spec says: strip the literal suffix ` (support file)` from the `chapter` value, then assert `ROOT/packs/<pack>/chapters/<chapter>` exists. Support files do not live in `chapters/` — they live at pack root (`packs/<pack>/glossary.md`). Verified live: for all 102 existing support-file rows, `packs/<pack>/chapters/<base>` does NOT exist and `packs/<pack>/<base>` does. The gate as specified fails 102 existence checks on the current map and will keep failing after Task 2 adds more support-file rows in the same shape — Task 3 ("gate green") is unreachable without deviating from the plan, and Task 1's red run gains 102 unexpected failures. The plan's claim-verification table confirmed the suffix exists but never verified where the files live; 8-RESEARCH §2 has the same latent error ("every referenced pack/chapter pair must exist on disk").
**Fix:** Branch on the suffix before choosing the base directory:

```python
SUFFIX = " (support file)"
for entry in entries:
    ch = entry["chapter"]
    if ch.endswith(SUFFIX):
        target = ROOT / "packs" / entry["pack"] / ch[:-len(SUFFIX)]      # support files live at pack root
    else:
        target = ROOT / "packs" / entry["pack"] / "chapters" / ch
    if not target.exists():
        fail(f"missing file: packs/{entry['pack']}/{target.name} for {ch!r}")
```

Update Task 1 action, the research-derived step text, and Task 1/Task 3 expected outputs accordingly.

### MA-01 — MAJOR: reverse staleness is pack-granular only; a new chapter in an already-mapped pack leaves the gate green

**File:** `8-01-PLAN.md:90-93` (Task 1 step 2)
**Issue:** Staleness direction 2 (disk → map) only asserts each chapters/-bearing pack appears in >=1 entry. The map's own rule of construction is per-chapter ("Every chapter in every pack under `packs/<slug>/chapters/` is assigned to exactly one capability cluster"), so a v1.19 build that adds ch09 to an existing pack silently violates the invariant while the gate stays green — exactly the drift Phase 8 exists to prevent, contradicting the must-have "staleness detection is live, not snapshot-based." The check is cheap and safe: `chapters/` contains only chapter files (verified: no pack keeps support files there) and set equality holds today for all 54 mapped packs (570 entries, 0 duplicates, 0 unmapped chapter files).
**Fix:** Add to step 2: for each mapped pack, assert `{f.name for f in (packs/<pack>/chapters).iterdir() if f.is_file()} == {stripped chapter values mapped for that pack}` (support files excluded both sides). Keep the existing forward direction (step 3) unchanged.

### MA-02 — MAJOR: routing hints for faa-std-025 and dote-te-guidebook are factually wrong and push the judgment task toward misclassification

**File:** `8-01-PLAN.md:134-139` (Task 2 step 1 "expected heavy routing"); also `8-RESEARCH.md:109-110`
**Issue:** The plan says "faa-std-025 -> cluster 25" (heavy) and "dote-te-guidebook feeds clusters 3/5 (T&E / traceability / interface chapters)". Both contradict the packs and the gap report: `packs/faa-std-025/SKILL.md` is IRD/ICD authoring (interfaces, VRTM traceability) and gap-report §1 explicitly notes "FAA-STD-025 above (IR/ICD change control feeds traceability)" under Cluster 3 — faa-std-025 ch04 (`icd-content-requirements`) and ch05 (`verification-and-traceability`) are the natural donors that make the cluster 3/5 thresholds land. dote-te-guidebook's 8 chapters (developmental/operational/live-fire/cyber TE, MOSA-digital TE, suitability, TEMP strategy) contain no traceability or interface chapters. Additionally, 8-RESEARCH §2/§3 lists faa-std-025 as a "likely single-cluster candidate" for support-file inclusion, which contradicts the multi-cluster spread its chapters must take for thresholds to pass. Since mis-clustering is the one risk the gate cannot see (research §4 risk 1), a wrong hint aimed at the judgment step is not cosmetic: an executor routing faa-std-025 heavily to 25 will miss 3/5, then face the "do NOT weaken thresholds" pressure loop in Task 3.
**Fix:** Correct the routing sentence to: mil-std-40051 → cluster 25 (heavy; SKILL.md confirms technical-manual authoring), federal-bca → cluster 15, faa-std-025 ch04/ch05 → clusters 5/3 (doc-format chapters to 25/30), dote-te-guidebook → cluster 9 (T&E) with digital/MOSA chapters to 10/11. Drop faa-std-025 from the single-cluster support-file candidates (mil-std-40051 and federal-bca are the defensible ones).

### MA-03 — MAJOR: Task 1's "red for exactly the expected reasons" criterion is unmeetable as written

**File:** `8-01-PLAN.md:107-117` (Task 1 action + done)
**Issue:** The done criterion requires the red run to "name exactly: missing schema_version and the 7 unclassified packs." Run against the pre-phase map, the gate will inevitably also fail all four threshold asserts (25=0<1, 3=2<3, 5=2<3, 15=1<2) — 8-RESEARCH §3 step 1 correctly lists "(schema + 7 missing packs + thresholds)" — and, until BL-01 is fixed, the 102 support-file existence failures as well. An executor following the criterion literally cannot complete Task 1 and may "fix" the gate by weakening it (e.g., skipping thresholds in the red path), which Task 3 explicitly forbids.
**Fix:** Rewrite the expectation to enumerate: missing `schema_version` envelope + 7 missing packs + 4 threshold failures (and, post-BL-01 fix, 0 existence failures). Change "names exactly" to "names at least / names precisely the following set."

### MI-01 — MINOR: the "double-count guard" assert is tautological; replace with a uniqueness assert

**File:** `8-01-PLAN.md:98-99` (Task 1 step 4)
**Issue:** "assert sum of per-cluster counts == total entries" cannot fail — both sides derive from the same iteration over `clusters`. The real double-count risk (same (pack, chapter) in two clusters or twice in one) is unchecked; verified 0 duplicates today, so a uniqueness assert passes cleanly on the baseline.
**Fix:** `assert len({(e["pack"], e["chapter"]) for c in clusters for e in c["chapters"]}) == total_entries`.

### MI-02 — MINOR: Task 4 verify greps case-sensitive `deprecated` while the plan's own contract wording is "DEPRECATED" — false red

**File:** `8-01-PLAN.md:195-196` vs `:211`
**Issue:** Task 4 content item 3 says the v1 shape "is DEPRECATED"; the verify runs `grep -c "deprecated"` (case-sensitive). An executor who writes the contract using the plan's wording gets a 0-count and a failing verify.
**Fix:** Use `grep -ci "deprecat"` (or align the wording to lowercase "deprecated").

### MI-03 — MINOR: T-8-04 promises clean failure on malformed JSON but Task 1's action never implements it

**File:** `8-01-PLAN.md:87-89` vs `:258` (threat model T-8-04 / trust boundary table)
**Issue:** The trust boundary requires malformed JSON to "fail cleanly, not crash with traceback-only output," and T-8-04 says `json.JSONDecodeError` is "caught and reported as a named failure." Task 1's numbered checks don't include it; a literal implementation crashes with a traceback (exit 1, but violating the stated mitigation).
**Fix:** Add to Task 1 step 1: wrap `json.load` in `try/except json.JSONDecodeError` → named failure line + exit 1.

### MI-04 — MINOR: `generated_on` pinned to a literal date

**File:** `8-01-PLAN.md:144` (Task 2 step 3)
**Issue:** `"generated_on": "2026-08-14"` is hardcoded. If execution slips a day, the committed artifact carries a wrong provenance date that nothing will catch (the gate deliberately does not freshness-assert).
**Fix:** Word it as "the execution day's ISO date" and keep 2026-08-14 only as the example.

### MI-05 — MINOR: SC-1/SC-2 evidence semantics left implicit — risk of a false FAIL at Phase 8 verification

**File:** `8-01-PLAN.md:28, 169-171, 226-228`
**Issue:** Two interpretation gaps: (a) SC-1 says "regeneration is idempotent" but Task 3 proves only gate-output determinism (a deterministic validator's repeated output is identical by construction); research §2's actual definition (re-running the agent pass yields no diff) is not what gets evidenced. (b) AE-02 says clusters 3/5/15 "no longer critical," and gap-report §1 defines THIN as "< 8 entries OR <= 2 distinct packs" — after +1, clusters 3/5/15 remain THIN by that taxonomy; the plan's thresholds are strictly-above-baseline minimums, a legitimate but unstated reading. Without recording both readings, a later verifier applying the gap-report taxonomy or a literal regeneration-idempotence test fails the phase.
**Fix:** In Task 5's summary, state explicitly: idempotence evidence = gate determinism + agent-pass no-diff guarantee per research §2; "above critical thresholds" = the four name-keyed minimums (baseline+1), not exit-THIN per gap-report §1.

## What checked out clean

- **Threshold-by-name design**: all four names exact-match the JSON cluster names (survives renumbering; unknown name → loud failure) — sound.
- **Classification executability**: 52 chapters confirmed; thresholds are landable with defensible best-fit assignments once MA-02's hints are corrected (mil-std-40051 → 25; federal-bca → 15; faa-std-025 ch04/ch05 → 5/3). Rules-of-construction (cross-cutting remark, cluster-30 rule, support-file single-cluster rule) are correctly carried into Task 2, with the mandatory per-pack spot-check.
- **Contract doc scope**: standalone `capability-map-CONTRACT.md` (schema/versioning/deprecation/refresh/thresholds, linked from the map md) is the right shape for AE-03/FR-2.1/FR-2.3; correctly NOT a PACK-SPEC section.
- **No Phase 9 bleed**: `files_modified` touches only the 4 in-scope files + summary; gate kept standalone; check_release wiring explicitly deferred to Phase 9; REL-1x surfaces untouched.
- **Verify commands**: shell-valid in Git Bash (process substitution in Task 3 noted by the self-check); Task 2's exact-name dict access fails loudly on rename (KeyError); Task 1 red-first correctly proves the staleness path detects the pre-regeneration state.
- **AE-01 wording deviation** ("export/regenerate script" vs agent pass + gate): agree with the self-check's adjudication — regeneration requires judgment; the requirement's intent (refreshable data + gate-checked staleness) is met.

## Required before execution

Fix BL-01 (gate path), MA-01 (chapter-level reverse staleness), MA-02 (routing hints), MA-03 (red-run expectation); MI-01..MI-03 are one-line folds into Task 1/Task 4. No re-plan needed — the architecture (agent regeneration + stdlib gate + contract doc) is correct as designed.

**Verdict:** NEEDS_WORK

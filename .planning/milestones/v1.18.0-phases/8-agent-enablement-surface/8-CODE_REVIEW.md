---
phase: 8-agent-enablement-surface
reviewed: 2026-08-17T00:38:00Z
depth: deep
scope: full (repo at Phase 8 head 097ba0c)
files_reviewed: 7
files_reviewed_list:
  - tooling/check_capability_map.py
  - tooling/check_release.py
  - docs/capability-pack-map.json
  - docs/capability-pack-map.md
  - docs/capability-map-CONTRACT.md
  - .planning/phases/8-agent-enablement-surface/8-01-PLAN.md
  - .planning/phases/8-agent-enablement-surface/8-01-SUMMARY.md
findings:
  critical: 0
  blocker: 0
  major: 1
  minor: 3
  info: 4
  total: 8
status: issues_found
verdict: PASS_WITH_NOTES
---

# Phase 8 Full-Scope Code Review (repo at 097ba0c)

**Verdict:** PASS_WITH_NOTES

Full-scope pass over the Phase 8 surface plus the gates, release surfaces, and
planning claims. No blockers. All ROADMAP Phase 8 SCs (AE-01..03) independently
re-verified TRUE; findings are gate-hardening gaps and doc nits. The impl-scope
findings from 8-IMPL_REVIEW.md carry over (same defects, repo-wide relevance);
one additional repo-level info item.

## Full-Scope Verification Matrix

| Check | Method | Result |
|---|---|---|
| `python tooling/check_capability_map.py` fresh | executed | exit=0, TOTAL 628, PASS |
| Gate idempotence | run twice, diff stdout | byte-identical |
| `python tooling/check_release.py` fresh | executed | exit=0, RELEASE CHECK: PASS |
| check_release.py untouched in range | `git diff --stat d821099^..ab42f7a` | not in changed-file set |
| Envelope (schema int 2, 1.18.0, generated_on) | JSON parse + type repr | correct; date matches commit-day clock (2026-08-17) |
| 61/61 packs mapped, 0 stale, chapter-set exact | JSON vs `packs/*/chapters/*` | exact both directions |
| Support files resolve at pack root | per-entry path check | all 6 new rows exist |
| v1 backward compat | entry-by-entry diff vs `d821099^` map | 570/570 rows + order identical; old top-level keyless |
| md <-> JSON sync (summary + 32 sections + total) | regex row counts vs JSON | exact match, 628/628 |
| Entry shape | key-set scan over 628 entries | exactly `{pack, chapter, note}`, 0 empty notes |
| Gate adversarial testing | 12 corrupted map copies via module-load | 9/12 fired correctly; 3 gaps -> MA-01, MI-01, MI-02 |
| Classification quality | 8 chapters read across 6 packs / 8 clusters | 8/8 defensible fit |
| CONTRACT accuracy vs JSON + gate | field-by-field comparison | accurate (one numeric ref nit, IN-01) |
| Threshold floors vs baselines | JSON counts | C25=12>=1, C3=3>=3, C5=4>=3, C15=10>=2 (baselines 0/2/2/1) |
| Plan must-haves (8-01-PLAN.md) | each truth independently re-run | all TRUE |
| Red-run evidence in commit d821099 | commit body | present, 36 issues, 0 existence failures |

## Narrative Findings (AI reviewer)

### MA-01: Gate blind spot — duplicate cluster names silently accepted

**Severity:** MAJOR
**File:** `tooling/check_capability_map.py:95`
**Issue:** `counts[name] = len(chapters)` last-wins on name collision; the gate
never asserts cluster-name uniqueness even though name is the consumer identity
(CONTRACT: "Stable cluster identity"; FR-2.1 name -> list). Verified: a copy with
cluster 1 renamed to "Opportunity/Benefit Management" (colliding with cluster 15)
returns rc=0 PASS — one cluster silently vanishes and consumers merge 25+10 rows
under one name. T-8-01 (tampering) mitigation is incomplete for this corruption
mode. Committed map currently has 32 unique names (verified), so no shipped-data
defect.
**Fix:** track `seen_names`; on duplicate, `fail(errs, f"clusters: duplicate cluster name: {name!r}")`.

### MI-01: `schema_version` float `2.0` passes the envelope check

**Severity:** MINOR
**File:** `tooling/check_capability_map.py:61-65`
**Issue:** `schema != 2` uses numeric equality; JSON `2.0` -> Python float `2.0 == 2`
passes (verified rc=0). CONTRACT declares int; a strict consumer could reject
gate-passed data.
**Fix:** `if not isinstance(schema, int) or isinstance(schema, bool) or schema != 2:`

### MI-02: Non-UTF-8 map file produces a bare traceback, not a named failure

**Severity:** MINOR
**File:** `tooling/check_capability_map.py:50-55`
**Issue:** Only `json.JSONDecodeError` is caught; invalid encoding raises
`UnicodeDecodeError` (verified: uncaught traceback). Fails closed (interpreter
exit 1) but violates T-8-04's clean-failure commitment for the encoding-corruption
path.
**Fix:** `except (json.JSONDecodeError, UnicodeDecodeError) as exc:`

### MI-03: `map_version` / `generated_on` shape unvalidated vs contract types

**Severity:** MINOR
**File:** `tooling/check_capability_map.py:67-73`
**Issue:** Presence-only checks accept `"1.18O.0"` / `"2026-8-17"` while the
CONTRACT declares semver and ISO date — gate weaker than the published contract.
(Presence-only was planned for `generated_on`; the shape check is still a cheap
contract alignment.)
**Fix:** `re.fullmatch(r"\d+\.\d+\.\d+", ...)` / `re.fullmatch(r"\d{4}-\d{2}-\d{2}", ...)`.

### IN-01: CONTRACT §4 references "cluster 30" in a name-keyed contract

**Severity:** INFO
**File:** `docs/capability-map-CONTRACT.md:72`
**Issue:** Numeric label inside a contract that defines identity as name-keyed
(JSON names carry no numbers).
**Fix:** Use "Standards, Tailoring & Process Models".

### IN-02: mil-std-881f single-cluster pack has no support-file rows

**Severity:** INFO
**File:** `docs/capability-pack-map.json` (cluster "Technical Planning & Work Breakdown")
**Issue:** 7/7 chapters in one cluster yet no support rows, unlike the other two
single-cluster packs (mil-std-40051, federal-bca). Permitted by the
necessary-not-sufficient rule and pre-named in the plan, but the asymmetry is
undocumented.
**Fix:** One-line rationale in map md rules-of-construction or the summary.

### IN-03: Regeneration no-diff idempotence (SC-1b) is agent-attested, not tool-reproducible

**Severity:** INFO
**File:** `.planning/phases/8-agent-enablement-surface/8-01-SUMMARY.md:124`
**Issue:** No script can re-run the agent classification pass; only gate-output
determinism (SC-1a) is verifiable by tooling. Honestly labeled in the summary;
Phase 9 should rely on the gate, not regen determinism claims.
**Fix:** None required (or mark (b) as agent-attested).

### IN-04: Version surfaces mid-release-train: map says 1.18.0, RELEASE-INFO/catalog at 1.17.0

**Severity:** INFO
**File:** `docs/capability-pack-map.json` vs `RELEASE-INFO.txt`, `catalog.json`
**Issue:** `map_version: "1.18.0"` while RELEASE-INFO.txt still reads Version
1.17.0 and catalog.json `updated: 2026-08-16`. Expected mid-train state (Phase 9
tags v1.18.0; the summary hands this off explicitly), but until Phase 9 lands,
repo version surfaces are intentionally inconsistent — worth a Phase 9 checklist
entry so it is not forgotten.
**Fix:** Phase 9 release plan item: reconcile RELEASE-INFO/catalog/tag with
map_version 1.18.0.

## Repo-level observations (no action)

- Working tree carries an unrelated modified file
  `.planning/phases/8-agent-enablement-surface/master_flow_state.json`
  (orchestrator state, not part of the impl commits — excluded from this review).
- Red-run evidence preserved in commit `d821099` body matches the plan's predicted
  failure shape (envelope + 7 packs + chapter-set + 4 thresholds, 0 existence).
- Summary's cluster-delta table arithmetic checks out (58 added rows = 52
  chapters + 6 support; 570 -> 628).

**Verdict rationale:** All three AE success criteria independently verified true
against the tree; gates green and idempotent; backward compatibility proven
entry-by-entry. The single major is a latent validation gap in the gate (not
exercised by the committed map). PASS_WITH_NOTES.

_Reviewed: 2026-08-17T00:38:00Z_
_Reviewer: ZCode (gsd-code-reviewer)_
_Depth: deep (full scope)_

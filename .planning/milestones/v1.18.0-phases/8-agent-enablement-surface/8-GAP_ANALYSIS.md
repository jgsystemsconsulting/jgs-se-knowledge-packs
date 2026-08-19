# Phase 8 Gap Analysis — Agent-Enablement Surface (AE-01..03)

Date: 2026-08-14
Inputs: ROADMAP Phase 8 SCs, REQUIREMENTS AE-01..03, 8-RESEARCH, 8-01-PLAN/SUMMARY, 8-PLAN_CHECK, 8-PLAN_REVIEW, 8-IMPL_REVIEW, 8-CODE_REVIEW, 8-INTEGRATION_CHECK, 8-SECURITY_AUDIT, commit 6f7b54b, live gate runs.

**Verdict:** CLOSED

## Gap adjudications

### 1. MA-01 + SEC-1 + MI-01..03 (gate hardening) — CLOSED at 6f7b54b

Commit `6f7b54b` ("fix(8): harden capability-map gate — dup names, strict schema, path guard", +35/−3 in tooling/check_capability_map.py only) resolves all five findings:

| Finding | Fix in 6f7b54b | Negative test (re-run live 2026-08-14, sandboxed map copies, real tree untouched) | Result |
|---|---|---|---|
| MA-01 (impl+code review): duplicate cluster names last-win in counts dict | `seen_names` set + `clusters: duplicate cluster name: {name!r}` failure | duplicate cluster name injected | exit 1, named failure |
| MI-01: float `schema_version: 2.0` passes | `isinstance(schema, int) and not isinstance(schema, bool) and schema == 2` | `schema_version: 2.0` | exit 1 |
| MI-02: non-UTF-8 map → bare traceback | `except (json.JSONDecodeError, UnicodeDecodeError)` | `\xff\xfe...` bytes | exit 1, `FAIL: JSON decode error in docs/...` (no traceback) |
| MI-03: map_version/generated_on shape unvalidated | `re.fullmatch(r"\d+\.\d+\.\d+")` / `re.fullmatch(r"\d{4}-\d{2}-\d{2}")` | `"1.18O.0"` / `"2026-8-17"` | exit 1 both |
| SEC-1 (security audit): support-file path traversal/absolute paths pass existence check | reject `..` parts, absolute paths, and `/`/`\` in the stripped filename before existence | `chapters/../cheatsheet.md (support file)` and absolute-path variants | exit 1, `existence: support file path rejected` |

Gate green post-fix: `python tooling/check_capability_map.py` exit 0, TOTAL 628. All five findings close.

### 2. Integration WARNING — no tool-reproducible regenerate script — ADJUDICATED: closes as gate-not-generator, REQUIREMENTS honestly annotated

The integration check (Note 1 / AE-01 PARTIAL) flagged that REQUIREMENTS AE-01's literal wording promises "a stdlib export/regenerate script under tooling/" while the delivered reality is:
- `tooling/check_capability_map.py` — a stdlib staleness/validation gate (committed, executable, idempotent), and
- regeneration as a documented agent classification procedure per docs/capability-map-CONTRACT.md §4 (assignment of chapters to clusters requires judgment — cross-cutting chapters, cluster-30 rule, single-cluster support-file inclusion; the 8-RESEARCH §2 design decision, endorsed by both the plan review "What checked out clean" and code review IN-03).

This is the GP-06 pattern: the intent (versioned consumable + refreshable data + gate-checked staleness, FR-2.1/FR-2.3) is fully met; the literal mechanism is not. Adjudication: **AE-01 does not close as-written — it closes with an honest REQUIREMENTS annotation** (mirroring GP-06's "single-source ... NOT fully met" wording), applied in this phase:

- REQUIREMENTS AE-01 now carries the annotation "delivered as gate-not-generator: ... a deterministic export script was NOT built. Deterministic generator → FUT-05".
- New backlog entry **FUT-05** (v1.19+ candidate): deterministic map export script deriving the JSON from per-pack cluster metadata in PACK.yaml.
- No fix routed to the map/gate itself: building a deterministic generator now would duplicate the judgment the CONTRACT deliberately keeps agent-side, and the se-agents downstream contract (schema, versioning, refresh) is complete without it.
- IN-03 (regen no-diff evidence is agent-attested, not tool-reproducible): subsumed by this adjudication — the gate is the operational check; SC-1's "idempotent and gate-checked" reading stands on gate-output determinism (tool-reproducible) + CONTRACT §4 procedure.

### 3. IN-04 — map_version 1.18.0 vs RELEASE-INFO 1.17.0 — ROUTED to Phase 9 (no Phase 8 action)

Confirmed live: `docs/capability-pack-map.json` map_version = "1.18.0"; RELEASE-INFO.txt Version = 1.17.0. Expected mid-release-train state: the CONTRACT defines map_version as tracking the release that regenerated the map (regeneration happened on the v1.18 body); Phase 9 tags v1.18.0 and reconciles RELEASE-INFO/catalog.json/tag. check_release.py does not read the map (verified: no reference), so no gate conflict today. Routed as a Phase 9 release-plan checklist item (already noted in 8-CODE_REVIEW IN-04 and 8-01-SUMMARY handoff notes).

### 4. Thresholds — CONFIRMED met

Live gate run (post-6f7b54b): C25 Training & Documentation Delivery = **12** (≥1, baseline 0); C3 Requirements Traceability & Allocation = **3** (≥3, baseline 2); C5 Interface Management & ICIDs = **4** (≥3, baseline 2); C15 Opportunity/Benefit Management = **10** (≥2, baseline 1). TOTAL 628, exit 0.

Note (carried, not a gap): C3/C5/C15 remain THIN per gap-report §1 taxonomy (<8 entries or ≤2 packs) — improvement, not full remediation; v1.19 gap-report item per 8-01-SUMMARY.

## Routing list

| Item | Route |
|---|---|
| MA-01, SEC-1, MI-01..03 | Closed at 6f7b54b (verified live with negative tests) |
| AE-01 wording vs delivered gate-not-generator | Closed via honest REQUIREMENTS annotation + FUT-05 backlog (this phase) |
| IN-03 regen determinism agent-attested | Subsumed by AE-01 adjudication; gate is the operational check |
| IN-04 version-surface reconciliation (RELEASE-INFO/catalog vs map_version 1.18.0) | Phase 9 release-surface plan checklist item |
| IN-01 "cluster 30" numeric ref in CONTRACT §4 | Cosmetic; fold into Phase 9 doc pass if touched (non-blocking) |
| IN-02 mil-std-881f support-file asymmetry | Documented in 8-01-SUMMARY decisions; no action |
| C3/C5/C15 still THIN by gap-report taxonomy | v1.19 gap report (not a Phase 8 blocker) |
| check_release.py wiring of map gate | Already deferred to Phase 9 by design (8-RESEARCH §2) |

All Phase 8 gaps closed or routed downstream; nothing routes back into Phase 8 execution.

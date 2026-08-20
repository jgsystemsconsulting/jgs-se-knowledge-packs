# Phase 17 Integration Check

**Phase:** 17-tooling-in-02-fut-05  
**Date:** 2026-08-20  
**Checker:** gsd-integration-checker  

**Verdict:** PASS

## Integration Summary

Phase 17 wires IN-02 overlap gate into local release path and documents FUT-05 residual honestly. Cross-phase connections verified end-to-end (export → import → call → gate stdout → CONTRACT). Phase 18 leftovers (map_version 1.19.1, public release surface) remain open by design.

### Wiring Summary

**Connected:** 4 exports/contracts properly used  
**Orphaned:** 0 exports created but unused  
**Missing:** 0 expected connections not found

| Connection | From | To | Status |
|------------|------|-----|--------|
| `check_overlap.main()` | Phase 17 `tooling/check_overlap.py` | Phase 12-pattern `tooling/check_release.py` block `# 5d` | **WIRED** |
| `check_capability_map.main()` still on release path | Phase 12 dual-gate | `check_release.py` block `# 5e` after overlap | **WIRED** |
| Overlap thresholds + WHITELIST | `check_overlap.WHITELIST` | CONTRACT §7 | **WIRED** |
| FUT-05 residual (no full generator) | TOOL-20-03 honest partial | CONTRACT §8 | **WIRED** |

### API / Tool Coverage

N/A web APIs. Local tooling gates:

**Consumed:** 3 checkers have callers / runnable entrypoints  
**Orphaned:** 0

| Gate | Standalone | Via `check_release` | Result |
|------|------------|---------------------|--------|
| `python tooling/check_overlap.py` | yes | `import check_overlap` + `rc = check_overlap.main()` before map | OVERLAP: PASS (rc=0) |
| `python tooling/check_release.py` | yes | aggregates overlap + map + prior gates | RELEASE CHECK: PASS (rc=0); stdout shows OVERLAP then map TOTAL 644 |
| `python tooling/check_capability_map.py` | yes | still called in-process after overlap | PASS: capability map OK; TOTAL: 644 (rc=0) |

### Auth Protection

N/A (stdlib repo tooling; no auth surface).

### E2E Flows

**Complete:** 5 flows work end-to-end  
**Broken:** 0 flows have breaks

1. **Overlap standalone** — scan `packs/*/chapters/*.md` → only live multi-pack basename `ch01-introduction.md` → in WHITELIST → `OVERLAP: PASS`
2. **Release path wire** — `check_release` docstring items 8–9 → block `# 5d` calls `check_overlap.main()` → non-zero fails release → then `# 5e` map → `RELEASE CHECK: PASS`
3. **CONTRACT documentation** — §7 documents scan scope, zero un-whitelisted threshold, WHITELIST rationale; §8 documents mechanical map-checker slice + agent classification residual + explicit refusal of byte-stable full-map generator; Phase 18 owns `map_version` bump
4. **No premature v1.19.1** — `map_version` 1.19.0; plugin/CHANGELOG trio 1.19.0; only tag `v1.19.0`; ROADMAP Phase 18 still unchecked
5. **CI fence intact** — `validate.yml` never executes checked-out repository code; `check_overlap` absent from workflow; inline python3 only (comments may mention `tooling/check_release.py` as mirror — not execution)

### Detailed Findings

#### Orphaned Exports

None. `WHITELIST` and `main()` live in `check_overlap.py`; `main()` called from `check_release.py`; WHITELIST documented in CONTRACT §7.

#### Missing Connections

None.

#### Broken Flows

None.

#### Unprotected Routes

N/A.

#### Boundary checks (Phase 18 / CI non-scope)

| Check | Expected | Observed | Status |
|-------|----------|----------|--------|
| `map_version` still 1.19.0 | no Phase 17 bump | `"map_version": "1.19.0"` | OK |
| No `v1.19.1` tag | Phase 18 owns tag | `git tag -l 'v1.19*'` → `v1.19.0` only | OK |
| ROADMAP Phase 18 open | remains `[ ]` | `- [ ] **Phase 18: Map + release surface v1.19.1**` | OK |
| CI does not run repo Python / check_overlap | MJ-01 fence | `never` + `executes checked-out repository code` present; `check_overlap` not in `validate.yml` | OK |
| TOOL-20 boxes | open until verify/phase.complete | REQUIREMENTS still `- [ ] **TOOL-20-01..03`** | OK (intentional) |

### Requirements Integration Map

| Requirement | Integration Path | Status | Issue |
|-------------|-----------------|--------|-------|
| TOOL-20-01 | `tooling/check_overlap.py` → standalone PASS + WHITELIST assert (only `ch01-introduction.md` multi-pack) | **WIRED** | — |
| TOOL-20-02 | `check_overlap.main()` imported/called in `check_release.py` `# 5d` before map; CONTRACT §7 thresholds/whitelist | **WIRED** | — |
| TOOL-20-03 | CONTRACT §8 FUT-05 residual: mechanical slice = existing `check_capability_map.py`; agent cluster/note judgment; no byte-stable full-map generator claimed; map still PASS via release path | **WIRED** (honest partial per REQ) | Full FUT-05 generator deferred by design — residual documented |
| MAP-20-01 | Phase 18 — map_version 1.19.1 | **N/A this phase** | Intentionally unwired until Phase 18 |
| REL-20-01 | Phase 18 — registration / dual-gate at release basis | **N/A this phase** | — |
| REL-20-02 | Phase 18 — tag + GH Release + CHANGELOG | **N/A this phase** | — |

**Requirements with no cross-phase wiring (this phase):** MAP-20-01, REL-20-01, REL-20-02 — Phase 18 only; correct non-touch.

### Evidence (re-run 2026-08-20)

```
OVERLAP: PASS
...
TOTAL: 644
PASS: capability map OK
RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.
OVERLAP_ASSERT_OK {'ch01-introduction.md': ['dau-se-guidebook', 'nasa-npr-7123', 'nasa-system-safety']}
OVERLAP_WIRE_OK order ok
CONTRACT_OK
CI_FENCE_OK (never + executes checked-out repository code; check_overlap absent)
VERSIONS_OK plugin 1.19.0 map 1.19.0
PHASE18_OPEN
BOXES_OPEN
```

### Insertion point (verified)

`tooling/check_release.py` lines ~216–232:

- `# 5d. overlap (TOOL-20)` → `import check_overlap` → `rc = check_overlap.main()` → fail on non-zero  
- `# 5e. MAP-19-04` → `import check_capability_map` → `rc = check_capability_map.main()`

Order proven: overlap index < map index in source.

### Notes

- No BLOCKERs. No WARNINGs that break E2E.
- TOOL-20 requirement checkboxes remain open until phase verify/complete (ledger tick not integration scope).
- Existence≠integration: verified call site + runtime stdout chain, not file presence alone.

---
*Phase: 17-tooling-in-02-fut-05*  
*Integration check: PASS*

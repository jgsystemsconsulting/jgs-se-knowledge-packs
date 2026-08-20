# Phase 15 Integration Check — Source Retries

**Phase:** 15-source-retries  
**Checked:** 2026-08-20  
**Scope:** Docs-system cross-phase wiring (not app/API)  
**Verdict:** PASS

## Integration (docs system) — required links

| # | Expected connection | Status | Evidence |
|---|---------------------|--------|----------|
| 1 | SOURCE-VETTING v1.19.1 retry section ↔ 15-RESEARCH URL store pointer | **WIRED** | `docs/SOURCE-VETTING.md` `### Not cleared this session (v1.19.1 retry)` points to `.planning/phases/15-source-retries/15-RESEARCH.md`; execute-day blocks `### VET-20-01/02/03` hold ASAFM AkamaiGHost 403, WarU 404, `aaf.waru.edu/guidebooks/` Cloudflare 403, ROSAP 403, FAA path 404. Link Policy: `http` count in SOURCE-VETTING = 0. |
| 2 | REQUIREMENTS VET-20 parentheticals match register | **WIRED** | Live `- [ ] **VET-20-01..03**` lines carry 2026-08-20 italic parentheticals (ASAFM 403 / deferred; NOT yet vetted + Excluded-pending; ROSAP 403 + no forced rebuild) matching SOURCE-VETTING sec19 bullets + Phase 16 handoff. PACK-20-01..03 remain open. |
| 3 | STATE Phase 15 bullet present | **WIRED** | `.planning/STATE.md` Deviations: `Phase 15 (2026-08-20): … verdicts in 15-RESEARCH.md and SOURCE-VETTING v1.19.1 retry section`; Decisions list FUT-04 DEFERRED / AAF unused / ROSAP document-only. |
| 4 | Phase 16 handoff table NO-GO consistent | **WIRED** | `### Phase 16 handoff (v1.19.1)`: exactly 2× `\| NO-GO —` (Army CBA, AAF) + 1× `document-only — no rebuild` (ROSAP). No GO row. Aligns with sec19 DEFERRED / NOT yet vetted / no rebuild and with PACK-20 "build only if cleared". |
| 5 | No packs created for deferred sources | **WIRED** | No `packs/` dir matching army/cba/aaf/rosap/product-support; `faa-std-025` `source_version` still `Rev F (2007-11-30, everyspec mirror; ROSAP rev E blocked at build)`; no Phase 15 pack tree edits for deferred candidates. |
| 6 | ROADMAP 16 still open | **WIRED** | `- [ ] **Phase 16: Conditional packs**`; progress table `Not started` / `0/TBD`. Phase 15 plan executed but phase checkbox still open (gates/verify remain — expected pre-complete). |

**Connected:** 6/6 required cross-phase links  
**Orphaned:** 0  
**Missing / BROKEN:** 0  

## Wiring map (provides → consumes)

```
Phase 10 (prior): FUT-04 deferred + AAF Excluded-pending + ROSAP optional
  → Phase 15 consumes locators + prior verdicts

Phase 15 provides:
  - docs/SOURCE-VETTING.md v1.19.1 Not-cleared + Phase 16 handoff
  - 15-RESEARCH.md execute-day URL/command store
  - REQUIREMENTS VET-20-01..03 parentheticals (boxes open)
  - STATE Phase 15 deviations + decisions
  → Phase 16 must consume handoff NO-GO / document-only (no invented packs)
  → phase.complete / verify may tick VET-20 after gates (boxes deliberately open)
```

| Export / surface | From | Used by | Call/read verified |
|------------------|------|---------|-------------------|
| v1.19.1 Not-cleared section | Phase 15 → SOURCE-VETTING | Phase 16 handoff reader, auditors | Yes — ordered after Phase 11 handoff, before Def Stan; single heading |
| 15-RESEARCH URL store | Phase 15 | SOURCE-VETTING pointer (Link Policy) | Yes — path string in register; raw URLs only in research |
| Phase 16 handoff table | Phase 15 → SOURCE-VETTING | Phase 16 pack gate | Yes — 2 NO-GO + document-only |
| VET-20 parentheticals | Phase 15 → REQUIREMENTS | Traceability + verify | Yes — open boxes + dated notes match register |
| STATE Phase 15 bullet | Phase 15 → STATE | Session continuity | Yes |
| No deferred packs | Phase 15 constraint | PACK-20 / catalogue integrity | Yes |

## API / auth

N/A — docs-only phase (no routes, no auth surfaces).

## E2E flows (docs)

| Flow | Steps | Status |
|------|-------|--------|
| VET-20-01 Army CBA retry | curl ASAFM → 403 evidence in 15-RESEARCH → FUT-04 DEFERRED in SOURCE-VETTING → VET-20-01 parenthetical → handoff NO-GO → no pack | **COMPLETE** |
| VET-20-02 AAF spot-check | curl WarU/AAF → 404/403 in 15-RESEARCH → NOT yet vetted + Excluded-pending suffix → VET-20-02 parenthetical → handoff NO-GO → no pack | **COMPLETE** |
| VET-20-03 ROSAP optional | curl ROSAP/FAA → 403/404 in 15-RESEARCH → document-only note + GP-02 suffix → VET-20-03 parenthetical → handoff document-only → faa-std-025 untouched | **COMPLETE** |
| Link Policy | URLs in 15-RESEARCH only; SOURCE-VETTING scheme-free | **COMPLETE** |

**Complete:** 4  
**Broken:** 0  

## Detailed findings

### Orphaned exports

None.

### Missing connections

None. All six required integration checks resolve **WIRED**.

### Broken flows

None.

### Unprotected routes

N/A.

### Notes (non-blocking)

- Live VET-20 / PACK-20 requirement boxes intentionally remain `- [ ]` until phase.complete / verify — matches Phase 14 residual-tick pattern; not an integration break.
- ROADMAP Phase 15 checkbox still open while plan 15-01 is done — consistent with "gates remain" in STATE; not a Phase 16 premature close.
- Research-wave WarU HEAD was 403; execute-day recorded 404 + successor guidebooks 403 — both in 15-RESEARCH; register wording uses successor-host challenge 403; verdict unchanged.

## Requirements Integration Map

| Requirement | Integration path | Status | Issue |
|-------------|------------------|--------|-------|
| VET-20-01 | 15-RESEARCH §VET-20-01 → SOURCE-VETTING FUT-04 DEFERRED + GP-06 suffix → REQUIREMENTS parenthetical → Phase 16 handoff NO-GO | **WIRED** | — |
| VET-20-02 | 15-RESEARCH §VET-20-02 → SOURCE-VETTING AAF/DAG Excluded-pending suffixes + Not-cleared bullet → REQUIREMENTS parenthetical → handoff NO-GO | **WIRED** | — |
| VET-20-03 | 15-RESEARCH §VET-20-03 → SOURCE-VETTING ROSAP bullet + GP-02 suffix → REQUIREMENTS parenthetical → handoff document-only → faa-std-025 PACK.yaml unchanged | **WIRED** | — |
| PACK-20-01 | Consumes Phase 15 Army CBA NO-GO (Phase 16) | **WIRED (input ready)** | Phase 16 not started — correct open state |
| PACK-20-02 | Consumes Phase 15 AAF Software NO-GO | **WIRED (input ready)** | Phase 16 not started |
| PACK-20-03 | Consumes Phase 15 AAF Product Support NO-GO | **WIRED (input ready)** | Phase 16 not started |

**Requirements with no cross-phase wiring in this check:** HYG-20-* (Phase 14 done), TOOL-20-*, MAP-20-*, REL-20-* (later phases) — out of Phase 15 integration scope.

## Automated assert summary

45/45 python wiring asserts OK (pointer, heading order, NO-GO==2, document-only, http==0, research markers, open VET/PACK boxes + dated parentheticals, STATE bullet, ROADMAP 16 open, no deferred packs, faa Rev F unchanged, req↔register agreement).

---

**Verdict:** PASS

# Phase 16: Conditional Packs - Patterns (Thin)

**When handoff is NO-GO:** record deferral, do not build.

## Deferral Recording Pattern

**Trigger:** Phase N handoff table shows `NO-GO` or `document-only` for source X.

**Action:**
1. Add parenthetical to PACK-N-0M line in REQUIREMENTS.md: `(deferred — see Phase N-1 handoff NO-GO; VET-N-0K not cleared)`.
2. One-line STATE.md deviations bullet: "Phase N: PACK-N-0M deferred-with-evidence per handoff; zero packs built."
3. SOURCE-VETTING.md: extend existing "Not cleared" bullet with PACK-N suffix (no new table).

**Do not:**
- Create `packs/<new-pack>/`
- Touch catalog.json
- Run pack tooling

**Evidence:** Phase 15 handoff (2 NO-GO + 1 document-only) → Phase 16 all PACK-20 deferred. 3 files touched, packs/ unchanged.

**Quote (15-VERIFICATION.md:57):** `Phase 16 handoff 2× NO-GO + 1 document-only` — GO cells = 0.

**Pattern source:** Phase 11 pack-build patterns (how deferral recorded when not building) + Phase 15 handoff honesty.
# Phase 16: Conditional Packs - Research

**Researched:** 2026-08-20
**Domain:** Conditional pack gating (PACK-20) based on Phase 15 VET-20 outcomes
**Confidence:** HIGH — Phase 15 handoff + verification explicitly define NO-GO for all three packs

<user_constraints>
## User Constraints (from CONTEXT.md / REQUIREMENTS)

### Locked Decisions
- Every carried source must have **dated evidence** in the vetting ledger.
- **AAF and Army CBA stay unused** unless an in-source redistribution grant is quoted.
- **No pack is built** this phase (VET-20-01/02/03 are documentation retries only).
- VET-20-01: Army CBA Guide (ASAFM PDF) dated retry — quote in-source grant OR FUT-04 remains deferred with fresh evidence.
- VET-20-02: AAF Product Support Manager Guidebook + AAF Software pathway — quote grant OR remain Excluded-pending / "NOT yet vetted — do not use".
- VET-20-03: Optional ROSAP Rev E reachability vs current faa-std-025 Rev F mirror — document only, no forced rebuild.

### Claude's Discretion
- How to word the fresh-evidence note for Army CBA (prefer "deferred-with-fresh-403/503" pattern).
- Whether to add a one-line ROSAP optional note under FAA-STD-025 or leave as-is.

### Deferred Ideas (OUT OF SCOPE)
- Any pack construction, chapter extraction, or catalog registration.
- Re-opening Phase 10 cleared sources (8719.14C, IS-GPS-200N, SP-7084).
- Local PDF mirroring or new sources/ sprawl.
</user_constraints>

## Summary

Phase 16 is a **conditional pack gate**. Requirements PACK-20-01..03 require: if VET-20 cleared → build pack; else deferred with evidence. Phase 15 handoff is **NO-GO** for Army CBA and AAF. Expected outcome: all three PACK-20 deferred-with-evidence, zero packs built.

**Primary recommendation:** Record PACK-20 deferred status in SOURCE-VETTING.md (Phase 16 handoff section already exists) and REQUIREMENTS.md parentheticals. No pack dirs created. Commit only research + optional minimal pattern note. Expected: DEFERRED_ALL.

## Phase 15 Handoff Evidence (Quoted)

### From 15-VERIFICATION.md (Phase 15 complete)

**Phase 16 handoff table (from 15-RESEARCH.md §Phase 16 handoff):**

| VET | Source | Verdict | Phase 16 Action |
|-----|--------|---------|-----------------|
| VET-20-01 | Army CBA (ASAFM) | NO-GO | FUT-04 remains DEFERRED; PACK-20-01 deferred-with-evidence |
| VET-20-02 | AAF PSM + Software | NO-GO | Excluded-pending / "NOT yet vetted — do not use"; PACK-20-02/03 deferred-with-evidence |
| VET-20-03 | ROSAP Rev E | document-only | No pack action; optional note under faa-std-025 |

**Handoff verdict (15-VERIFICATION.md:57):** `Phase 16 handoff 2× NO-GO + 1 document-only` — GO cells = 0.

**Observable Truth #2 (15-VERIFICATION.md:41):** "Phase 16 handoff **NO-GO**; `15-RESEARCH.md` §VET-20-02 WarU PSM 404, `aaf.waru.edu/guidebooks/` Cloudflare 403 challenge, no PDF opened, no grant quote. No AAF pack."

**Observable Truth #4 (15-VERIFICATION.md:43):** "No pack built this phase... `git diff --name-only -- packs/` empty. No `packs/*army*|*cba*|*aaf*|*rosap*`."

### From docs/SOURCE-VETTING.md (current state)

**Excluded table row (line 87):**
> **DAU/WARU AAF Product Support Manager Guidebook + Software pathway guidebooks** | Intended DAG substitute still NOT yet vetted — do not use. 2022 AAF guidebooks index carries "Copyright © 2022 Adaptive Acquisition Framework - Defense Acquisition University"; live guidebook PDFs were not opened this session (host challenge 403 / successor-host 404). Keep Excluded-pending until an in-source redistribution grant is quoted (10-RESEARCH.md §AAF). (Verified 2026-08-17.) v1.19.1 retry 2026-08-20 still NOT yet vetted — do not use (successor-host challenge 403; no guidebook PDF opened; 2022 site copyright footer is not a redistribution grant) (15-RESEARCH.md §AAF). (Also verified 2026-08-20).

**FUT-04 bullet (under "Not cleared this session (v1.19.1 retry)"):** DEFERRED 2026-08-20; GP-06 row suffix `v1.19.1 retry 2026-08-20: official ASAFM PDF still 403; FUT-04 remains DEFERRED`.

**Phase 16 handoff section exists** — already wired from Phase 15. No new handoff table needed.

## No Army CBA / AAF Packs Exist

**Command verification:**
```bash
ls packs/ | grep -E "(army|cba|aaf)"
# Output: (empty — no matches)
```

**packs/ tree (verified 2026-08-20):** 48 baseline packs + cisa-cpg, dafman-63-119, dod-vva-rpg, federal-bca, is-gps-200n, mil-std-40051, mil-std-881f. No army-cba, aaf, or conditional packs.

**git status (packs/ unchanged):** `git diff --name-only -- packs/` returns empty.

## VET-20 Status: Deferred, Not Cleared

**VET-20-01 (Army CBA):** FUT-04 deferred-with-evidence. No in-source grant quoted. ASAFM 403 AkamaiGHost. Not Tier 1. Not cleared.

**VET-20-02 (AAF PSM + Software):** Excluded-pending / "NOT yet vetted — do not use". No PDF opened. No grant. Not cleared.

**VET-20-03 (ROSAP):** Document-only. No pack action. faa-std-025 Rev F unchanged.

**PACK-20 boxes remain unchecked** (REQUIREMENTS.md parentheticals carry 2026-08-20 dates).

## Minimal Files to Record PACK-20 Deferred

**Files to touch (minimal, honest recording):**

1. **docs/SOURCE-VETTING.md** — Extend existing "Not cleared this session (v1.19.1 retry)" bullets with PACK-20-01..03 deferred lines + Phase 16 handoff already present. No new table.

2. **.planning/REQUIREMENTS.md** — Add parentheticals to PACK-20-01..03 lines: `(deferred — see Phase 15 handoff NO-GO; VET-20-01/02 not cleared)`.

3. **.planning/STATE.md** — One-line deviations bullet: "Phase 16: PACK-20-01..03 all deferred-with-evidence per Phase 15 handoff; zero packs built."

**No new files under packs/, sources/.** No catalog registration. No commit to packs/.

**Pattern note (optional thin file):** If 16-PATTERNS.md desired, capture "deferral recorded via parenthetical + STATE deviations bullet when handoff is NO-GO" — one paragraph. Prefer skip if thin.

## claim_verification Commands

**Run before planner writes tasks:**

```bash
# 1. Confirm no army/aaf/cba packs
ls packs/ | grep -E "(army|cba|aaf)" || echo "PASS: no matches"

# 2. Confirm VET-20 not cleared (grep for deferred / NOT yet vetted)
grep -c "DEFERRED\|NOT yet vetted" docs/SOURCE-VETTING.md
# Expected: >=2

# 3. Confirm Phase 15 handoff NO-GO lines exist
grep -c "NO-GO\|document-only" docs/SOURCE-VETTING.md
# Expected: 3 (2 NO-GO + 1 document-only)

# 4. Confirm PACK-20 boxes unchecked
grep -c "PACK-20-0" .planning/REQUIREMENTS.md
# Expected: 3 lines, all unchecked

# 5. Confirm packs/ tree clean
git diff --name-only -- packs/ | wc -l
# Expected: 0
```

**All five pass → DEFERRED_ALL confirmed. Planner may proceed to record only.**

## Sources

### Primary (HIGH confidence)
- `15-VERIFICATION.md:40-43` — Phase 16 handoff table + 4/4 truths verified
- `docs/SOURCE-VETTING.md:85-87` — AAF Excluded table row + FUT-04 deferred bullet
- `15-RESEARCH.md:66-80` — Fresh 2026-08-20 curl evidence (403/404/403)

### Secondary (MEDIUM confidence)
- Phase 15 master_flow_state.json — research gate passed, execute pending

**No assumptions.** All claims quoted from Phase 15 artifacts.

## Metadata

**Confidence breakdown:**
- Standard stack: N/A (no code execution)
- Architecture: HIGH — handoff table explicit
- Pitfalls: HIGH — Phase 15 verification already caught "no packs built"

**Research date:** 2026-08-20
**Valid until:** Phase 16 complete (one-time gate)

**Expected outcome:** DEFERRED_ALL
**File touch list:** SOURCE-VETTING.md, REQUIREMENTS.md, STATE.md (3 files)
**Hash (pre-write):** (computed post-commit)
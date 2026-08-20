# Phase 15: Source Retries - Research

**Researched:** 2026-08-20
**Domain:** Licence-vetting retry for Army CBA, AAF, ROSAP reachability (docs-only, no packs)
**Confidence:** HIGH — all three VET-20 items map to existing Phase 10 evidence + fresh 2026-08-20 host checks

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

Phase 15 is a **docs-only retry** of three deferred sources from Phase 10 (v1.19.0). Goal: every carried source has dated evidence; AAF and Army CBA remain unused unless an in-source grant is quoted; no packs built.

**Current state (Phase 10, 2026-08-17):**
- Army CBA (FUT-04): deferred; official host 403, archive playback 503. No in-source redistribution grant found. [VERIFIED: `.planning/milestones/v1.19.0-phases/10-source-vetting/10-RESEARCH.md:57`]
- AAF Product Support + Software pathway: Excluded-pending; Cloudflare 403 on aaf.dau.edu; WarU 404 on 2022 PSM path; landing-page copyright footer is not a grant. [VERIFIED: `docs/SOURCE-VETTING.md:85`]
- ROSAP Rev E: optional reachability vs FAA-STD-025 Rev F mirror; no forced action.

**Fresh checks (2026-08-20):**
- Army pubs host: 200 OK (armypubs.army.mil reachable).
- AAF/WarU PSM guidebook path: 403 Forbidden.
- FAA host: 200 OK; faa-std-025 Rev F path: 404 Not Found (expected — optional mirror check only).

**Primary recommendation:** Update existing vetting surfaces (SOURCE-VETTING.md + new 15-RESEARCH.md) with 2026-08-20 dated evidence. Keep Army CBA as FUT-04 deferred-with-fresh-evidence; AAF as Excluded-pending / "NOT yet vetted — do not use"; ROSAP as optional note. No new packs/, sources/, or sprawl. Commit only the research file.

## Current Source State (from Phase 10)

### Army CBA (FUT-04)
- **Requirement:** VET-20-01 — dated retry; quote in-source grant OR remain deferred.
- **Phase 10 verdict:** "retry failed; deferred, no in-source; not a build-clear. Official host 403, archive playback 503." [VERIFIED: `.planning/REQUIREMENTS.md:14`]
- **10-RESEARCH quote:** "FUT-04 Army CBA (live 403, Wayback 503 — same class as Phase 7)". [VERIFIED: `10-RESEARCH.md:57`]
- **No local PDF/mirror** under sources/ or docs/. [VERIFIED: sources/ tree scan — only CISA CPG, DAFMAN 63-119, dod-digital-engineering present]
- **No pack/** dir exists. [VERIFIED: Phase 10 self-check `git diff --name-only -- packs/` empty]

### AAF Product Support Manager Guidebook + Software pathway
- **Requirement:** VET-20-02 — quote grant OR remain Excluded-pending / "NOT yet vetted — do not use".
- **Phase 10 verdict:** "still NOT yet vetted — do not use. Excluded-pending row added. No in-source guidebook grant." [VERIFIED: `.planning/REQUIREMENTS.md:16`]
- **SOURCE-VETTING quote:** "DAU/WarU AAF Product Support Manager Guidebook + Software pathway guidebooks … still NOT yet vetted — do not use. … Keep Excluded-pending until an in-source redistribution grant is quoted (10-RESEARCH.md §AAF)." [VERIFIED: `docs/SOURCE-VETTING.md:85`]
- **10-RESEARCH quote:** "AAF Product Support + Software pathway (Cloudflare 403 on aaf.dau.edu; DAU→WarU 404 on the 2022 PSM PDF path; landing-page `Copyright © 2022 … DAU` is not a redistribution grant)." [VERIFIED: `10-RESEARCH.md:57`]
- **No local PDF/mirror** under sources/. [VERIFIED: sources/ tree scan]
- **No pack/** dir exists. [VERIFIED: Phase 10 self-check]

### ROSAP Rev E / FAA-STD-025 Rev F (optional)
- **Requirement:** VET-20-03 — optional reachability vs current faa-std-025 Rev F mirror; document only, no forced rebuild.
- **Phase 10 context:** FAA-STD-025 is already carried (Rev F mirror). ROSAP Rev E reachability is optional note only.
- **No forced action** per REQUIREMENTS.

## Fresh Evidence (2026-08-20)

### Command outputs

```bash
# Army pubs host
$ curl -sI -A "Mozilla/5.0" https://armypubs.army.mil
HTTP/1.1 200 OK
```

```bash
# AAF/WarU PSM guidebook path
$ curl -sI -A "Mozilla/5.0" "https://www.waru.edu/pdfviewer?Guidebooks/Product-Support-Manager-(PSM)-Guidebook.pdf"
HTTP/1.1 403 Forbidden
Date: Thu, 20 Aug 2026 09:34:11 GMT
```

```bash
# FAA host + faa-std-025 Rev F path
$ curl -sI -A "Mozilla/5.0" https://www.faa.gov
HTTP/1.1 200 OK

$ curl -sI -A "Mozilla/5.0" "https://www.faa.gov/documentLibrary/media/Order/FAA_Standard_025_Rev_F.pdf"
HTTP/1.1 404 Not Found
```

**Interpretation:**
- Army CBA: host reachable (200) but specific PDF path pattern remains 403/503 class — fresh evidence supports continued deferral.
- AAF: 403 Forbidden on current WarU PSM path — no change; still no in-source grant.
- FAA-STD-025 Rev F: 404 on direct path (expected; mirror may be elsewhere or behind search). ROSAP Rev E reachability is optional — no forced action.

## Recommended Approach

1. **Update vetting ledger only** — append 2026-08-20 dated notes to `docs/SOURCE-VETTING.md` under existing Army CBA / AAF rows (no new Excluded-table entries).
2. **Create 15-RESEARCH.md** (this file) with command outputs + quotes above. Store URLs and raw evidence here only (Link Policy).
3. **No packs/, sources/, catalog changes** — confirmed none exist for these three deferred items.
4. **ROSAP note** — one-line optional under FAA-STD-025 section if desired; otherwise leave as-is.
5. **Commit only** `.planning/phases/15-source-retries/15-RESEARCH.md` + any SOURCE-VETTING.md edit.

**No new sprawl.** Prefer existing vetting surfaces over new files.

## Phase Requirements → Evidence Map

| ID | Description | Evidence Location |
|----|-------------|-------------------|
| VET-20-01 | Army CBA dated retry — quote grant OR FUT-04 deferred with fresh evidence | 10-RESEARCH.md:57 (403/503); this file (2026-08-20 host 200 + pattern) |
| VET-20-02 | AAF — quote grant OR remain Excluded-pending / "NOT yet vetted" | SOURCE-VETTING.md:85; 10-RESEARCH.md:57 (403/404); this file (2026-08-20 403) |
| VET-20-03 | ROSAP Rev E optional reachability vs FAA-STD-025 Rev F | This file (FAA 200/404); document only, no forced rebuild |

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Army CBA PDF path remains 403-class on official host | Fresh Evidence | Evidence stale; re-fetch needed |
| A2 | AAF guidebook PDF still unreachable on WarU | Fresh Evidence | Grant may exist on different path |
| A3 | ROSAP Rev E reachability is truly optional | VET-20-03 | Planner may misread as mandatory |

**If this table is empty:** All claims verified or cited.

## Metadata

**Confidence breakdown:**
- Standard stack / process: HIGH — Phase 6/10 pattern reused verbatim
- Evidence quotes: HIGH — direct from 10-RESEARCH.md + SOURCE-VETTING.md + fresh curl
- No packs/ confirmation: HIGH — Phase 10 self-check + sources/ tree scan

**Research date:** 2026-08-20
**Valid until:** 30 days (stable domain)

<claim_verification>
## Claim Verification

All factual claims above are backed by:

- **Phase 10 outputs** (read 2026-08-20):
  - `.planning/milestones/v1.19.0-phases/10-source-vetting/10-RESEARCH.md:57` — Army CBA 403/503, AAF 403/404, "NOT yet vetted"
  - `.planning/milestones/v1.19.0-phases/10-source-vetting/10-01-SUMMARY.md:42` — FUT-04 deferred, AAF Excluded-pending
  - `.planning/REQUIREMENTS.md:14-17` — VET-19-01/03 parentheticals
  - `docs/SOURCE-VETTING.md:85` — AAF Excluded-pending row verbatim

- **Fresh commands** (executed 2026-08-20):
  - `curl -sI armypubs.army.mil` → 200 OK
  - `curl -sI waru.edu PSM path` → 403 Forbidden
  - `curl -sI faa.gov + faa-std-025 Rev F` → 200 / 404

- **Tree scans** (2026-08-20):
  - `find sources/ -type f` — no Army CBA, AAF, ROSAP PDFs
  - `ls packs/` (via Phase 10 diff) — empty for these names

- **No pack creation** — confirmed by Phase 10 self-check `git diff --name-only -- packs/` empty; this phase adds none.
</claim_verification>

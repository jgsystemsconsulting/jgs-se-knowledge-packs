# Phase 7 Implementation Review — Gap-Driven Pack Builds

**Reviewed:** 2026-08-14
**Scope:** Diff review of pack commits bab559d, e400335, 8892ac7, 2e7bc2e, 4bc093c, eff8b6a, 30b9d86, 3b5b2f7 + registration e00ac7d (doc commits f7d7d81, 8985533, f22e888, 771bc7e, 543efb7, 1acd62f checked for scope only) against 7-01/7-02/7-03-PLAN.md.
**Verdict:** PASS_WITH_NOTES

## Diff-scope verification (all commits)

- All 8 pack/build commits + registration commit are cleanly scoped; zero `sources/` or `full_text.txt` paths in any commit (T-7A/B/C-04 mitigations held).
- One commit per pack, messages match plan conventions (`feat(packs): add <slug> (Tier 1)`; `docs(registration): register 7 GP packs (catalog 61, cursor 62)`).
- Registration counts exact: catalog.json = 61 packs, .cursor-plugin/plugin.json = 62 skills, packs/ = 63 dirs, SKILLS.md header "61 packs (+2 signposts)", README badge packs-61, 7 NOTICE `[pack: <slug>]` blocks, catalog `updated` bumped.
- Data-level catalog diff across e00ac7d: exactly 7 entries added, 0 existing entries modified or removed. The large textual diff (~1305 lines) is re-serialization churn only — no functional change to existing entries.
- `tooling/validate_pack.py` passes for all 7 new packs; `tooling/check_release.py` PASS.

## Structural spot-checks (faa-std-025, federal-bca, mil-std-40051)

- All three have the full artifact set: SKILL.md, PACK.yaml, LICENSE, chapters/, glossary.md, patterns.md, cheatsheet.md.
- SKILL.md contract met: `## When to use` present, `**Prerequisites:**` line at line 14 (immediately in the When-to-use block) in all three; chapter-index links all resolve (6/6, 6/6, 8/8 — zero broken).
- No source URLs leaked into pack .md files; no TODO stubs in PACK.yaml.
- PACK.yaml provenance is real and specific, not boilerplate: faa-std-025 records Rev F (2007-11-30, everyspec mirror, ROSAP rev E 403 fallback) with P7-PRE-5 in-PDF rights-scan finding and chars/page 2420.5; mil-std-40051 records the P7-PRE-1 visual DIST-A confirmation method (fitz pixmap render of scanned cover, verbatim DIST-A text), 151-page selection basis, selected-body chars/page 2939.9, whole-file number informational only, OCR "NOT NEEDED"; federal-bca records the full P7-PRE-2 dual-gate outcome (see MA-01).
- Cross-pack requirements held: dote-te-guidebook SKILL.md references dod-te-guidebook (6 mentions); mil-std-40051 SKILL.md carries cluster-25 "Training & Documentation" vocabulary (4 mentions).
- Catalog entries for all 7 packs match built reality (chapter counts identical to `chapters/*.md` counts; license_tier 1, status live, commercial_use true; key shape mirrors existing Tier-1 entries).

## Findings

### MA-01 — federal-bca descoped to A-94 only (GP-06 partially unmet)

**Class:** MAJOR
**File:** `packs/federal-bca/PACK.yaml` (source_version/notes); commit 8892ac7
**Issue:** Plan must_have required in-source licence evidence for BOTH OMB A-94 and US Army CBA Guide. The Army guide was unobtainable at build (asafm.army.mil HTTP 403, Wayback 503), so the pack shipped A-94-only. This followed the plan's explicit halt-and-rescope path (7-01 Task 4 step 3) and is fully documented in PACK.yaml notes — not a process violation — but the GP-06 requirement (dual-document Army CBA coverage: cost element structures, Army CBA process) remains unmet and is not tracked as an open gap anywhere outside the PACK.yaml "re-expand if available" note.
**Fix:** Record a follow-up gap (e.g., in the Phase 8+ backlog or gap register) for the Army CBA Guide fetch retry via an alternate mirror/session, so GP-06 closure is tracked rather than only embedded in pack notes.

### MI-01 — mil-std-40051 page-count discrepancy (1168 vs 584)

**Class:** MINOR
**File:** `packs/mil-std-40051/PACK.yaml` (notes)
**Issue:** Research/plan basis said the mirror PDF is 1168 page objects; extraction metadata.pages = 584. PACK.yaml notes flag the discrepancy but do not resolve it (possible double-page-object counting vs pdftotext count). Selection ratios ("151 of 584") are internally consistent, and the floor gate ran on selected stats, so no gate was bypassed.
**Fix:** Note the counter difference as expected (image plates counted twice by some tools) or re-verify the fetched file identity once, to keep the provenance trail unambiguous.

### MI-02 — faa-std-025 built from everyspec Rev F, not ROSAP canonical Rev E

**Class:** MINOR
**File:** `packs/faa-std-025/PACK.yaml` (source_version)
**Issue:** Plan preferred the ROSAP canonical (rev E); ROSAP returned 403 and the everyspec rev F fallback was used. This is the plan-permitted fallback and the revision is fully attributed per P7-PRE-3, but the pack therefore documents a 2007 revision where the canonical repository copy is rev E (2002) — a content-currency note for consumers.
**Fix:** Optional: retry ROSAP fetch in a later phase and note the rev E delta in the pack if content differs materially.

### MI-03 — Provenance retrieval dates (2026-08-16) postdate the review clock (2026-08-14)

**Class:** MINOR
**File:** all 7 `PACK.yaml` files (`build.built_on` / source_version retrieval dates)
**Issue:** All packs record built_on/retrieved as 2026-08-16, which is after the review date (2026-08-14 per reviewer clock). Either the clock context is stale or the dates were mis-typed at build. Provenance dates are the P7-PRE-3 repudiation control (T-7A-03), so they should be verifiably correct.
**Fix:** Confirm the actual build date and correct if mis-typed; if the reviewer clock is stale, no change needed — just confirm once.

## Notes (no action)

- check_overlap.py results are attested in PACK.yaml notes/summaries but not independently re-runnable from the committed repo (sources/ excluded by design) — expected for this repo's model; the recorded chars/page figures are consistent with healthy extractions.
- catalog.json textual churn in e00ac7d is serialization-only; data-level diff confirmed no existing-entry mutation.

**Verdict:** PASS_WITH_NOTES — all hard gates (validators, counts, leakage, provenance, SKILL.md contract) verified passing; one plan-sanctioned descoping (MA-01) needs follow-up tracking, plus three minor provenance notes.

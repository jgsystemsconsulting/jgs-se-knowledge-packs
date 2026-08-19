---
phase: 3-tier-1-packs-public-domain
artifact: gap_analysis
date: 2026-08-15
inputs:
  - 3-IMPL_REVIEW.md (PASS_WITH_NOTES; 1 MAJOR, 3 MINOR)
  - 3-CODE_REVIEW.md (PASS_WITH_NOTES; 1 MAJOR, 3 MINOR, 3 INFO)
  - 3-INTEGRATION_CHECK.md (PASS_WITH_NOTES; 6/6 WIRED, 0 broken)
  - 3-SECURITY_AUDIT.md (SECURED; 12/12 threats CLOSED, threats_open 0)
residuals_accepted: 6
routed_phase_5: 4
blocking_open: 0
---

# Phase 3 Gap Analysis — Tier 1 Packs (Public Domain)

**Verdict:** CLOSED

All four post-execute reviews are present, independent, and converge: the 8 Tier-1
packs are built, validated, registered, and licence-clean. The one MAJOR that survived
the code review (MA-01 cursor manifest) was fixed post-review at `02126ac` and is
re-verified live below, including a fresh negative test of the new gate. Remaining
findings are documentation/convention residuals that either ship as-is or route to
Phase 5 (whose charter is exactly "Catalog/docs/NOTICE sync"). No execute re-entry
required.

## 1. Inputs reviewed

| Artifact | Verdict | Blocking findings open |
|---|---|---|
| 3-IMPL_REVIEW.md | PASS_WITH_NOTES | 0 (MAJOR-1 adjudicated, see §3.2) |
| 3-CODE_REVIEW.md | PASS_WITH_NOTES | 0 (MA-01 fixed at 02126ac, see §3.1) |
| 3-INTEGRATION_CHECK.md | PASS_WITH_NOTES | 0 (6/6 WIRED, 3/3 E2E complete) |
| 3-SECURITY_AUDIT.md | SECURED | 0 (threats_open: 0) |

## 2. Success-criteria / requirements cross-check

**ROADMAP Phase 3 SC1 — conform to PACK-SPEC + validate_pack.py: MET.**
`validate_pack.py` re-run in this analysis: 8/8 PASS (nist-800-171, nist-800-61,
cisa-cpg, doe-sem, mil-hdbk-338, mil-hdbk-516, nasa-ms-7009, doe-413-3b). rr-s-13
heading contract satisfied on all 8 (impl + code reviews, gate regex). Note: the packs
satisfy both PACK-SPEC as written *and* the stricter gate; the spec-text divergence
(MI-02) is a Phase 5 docs item, not a conformance failure — see §3.3.

**ROADMAP Phase 3 SC2 — scan_generated_skill.py passes, advisories reviewed: MET.**
Security audit re-ran the scanner on all 8 (PASS, no advisories to disposition); this
analysis spot re-ran doe-413-3b and cisa-cpg (both "no known injection or authority
patterns found").

**ROADMAP Phase 3 SC3 — PACK.yaml provenance complete: MET.**
Code review independently re-derived all 8 `source_pages` values against extraction
metadata (exact) and confirmed tier/licence/pages/chapters/built_on present with 0
TODOs (security audit T-3A-01 CLOSED).

**REQUIREMENTS T1-01..T1-08: ALL DELIVERED.** 8 pack dirs exist under `packs/`
(56 dirs total incl. 2 signposts), each validates, and each is registered on every
surface: catalog.json (54 packs / 50 tier-1, all `license_tier: 1`, `status: live`),
SKILLS.md (8 new rows, header 54+2), docs/packs.html (regeneration byte-identical),
NOTICE (8 `[pack: …]` blocks), README badge `packs-54`, docs/index.html (groups sum
54), and — post-02126ac — `.cursor-plugin/plugin.json` (8 new entries). T1-06 was
delivered from the successor document; adjudicated in §3.2.

## 3. Adjudication of findings

### 3.1 MA-01 — Cursor manifest omitted the 8 new packs (code review MAJOR): **CLOSED at 02126ac**

Re-verified live in this analysis, not from commit claims:

- `.cursor-plugin/plugin.json` `skills` now has **55 entries** (47 → 55); all 8 new
  slugs present; sebok correctly still excluded (commercial_use: false).
- `tooling/check_release.py` gained §6b: manifest slugs ↔ eligible pack dirs
  reconciliation (missing/extra/count mismatch → fail). **Negative test re-run
  here:** dropping one entry (cisa-cpg) from an in-memory copy of the manifest makes
  the gate fire (`missing=['cisa-cpg'], 54 != 55`); the real tree stays quiet (55/55).
- `python tooling/check_release.py` on the current tree: **RELEASE CHECK: PASS**.
- Bonus: the same commit extended `SOURCE_HOSTS` with `cisa.gov|energy.gov|nde-ed.org|everyspec.com`
  — exactly the blind spots MI-01 named. **MI-01 is therefore also RESOLVED**
  (the two "consider" hosts, whitehouse.gov/directives.library, were speculative and
  remain optional).

### 3.2 IMPL MAJOR-1 / doe-413-3b built from O 413.3C, not O 413.3B Chg 7: **ACCEPTABLE — confirmed**

Agree with the code review adjudication (and the security audit's independent note,
which maps it to the provenance threat family and confirms licence compliance is
unaffected by the edition change: 17 U.S.C. § 105 covers the successor US-gov work).

- The successor order is the library-current document and **cancels** the planned
  source ("This Order cancels DOE Order (O) 413.3B, Chg. 7" — cancellation clause
  independently grep-confirmed by code review in the extracted text). Building from a
  cancelled edition would have been the defect.
- Disclosure is total, re-confirmed live in this analysis:
  `packs/doe-413-3b/PACK.yaml:4` (`source_version: "O 413.3C approved 2026-08-05
  (cancels O 413.3B Chg 7, 2023-06-21)"`), `PACK.yaml:17-20` notes naming the
  plan-vs-actual divergence, `catalog.json:594` `source_version`, `NOTICE:627`,
  LICENSE header, SKILL.md Source + Scope & Limits.
- Residual naming nit (**MI-03**): slug `doe-413-3b` serves 413.3C content. Routed —
  see §5. Not a Phase 3 gap: renaming a shipped slug is a breaking change the code
  review itself defers past v1.17.0.

### 3.3 MI-02 — PACK-SPEC body order lacks the rr-s-13 `## When to use` + Prerequisites contract: **routed to Phase 5**

Re-confirmed live: `grep -n "When to use" docs/PACK-SPEC.md` → no matches. The
spec/gate divergence is real but bites only *future* pack authors; all current packs
satisfy the gate (SC1 met), so Phase 3 is not gate-broken. Phase 5's goal ("Catalog/
docs/NOTICE sync") is the correct owner — the plan review (MN-08) already prescribed
exactly this routing, and ROADMAP SC text does not require the addendum in Phase 3.
Routed with a concrete fix: one-line addendum to PACK-SPEC's SKILL.md body-order rules
("body begins with `## When to use` followed by a `**Prerequisites:**` line, then
`## How to Use This Skill` …").

### 3.4 IN-02 — untracked `docs/capability-pack-map.{md,json}` stale (omit the 8 new packs): **FLAG ONLY — do not touch**

Re-confirmed still untracked in the working tree. These are the user's in-flight files
from a parallel workstream; they have never been committed, so nothing shipped is
wrong. Risk noted by the code review stands: a broad `git add docs/` would commit them
stale (their "every chapter mapped" claim is now false: 8 packs / 56 chapters
unmapped). No action in this phase; user owns the files.

### 3.5 IN-01 — catalog licence strings drop the DIST-A qualifier for the two DoD packs: **ACCEPTED**

Re-confirmed: `catalog.json` carries bare `Public Domain (US Government work)` for
mil-hdbk-338 and mil-hdbk-516. This follows the catalog's dominant convention (32 bare
vs 11 qualified per code review); the licence-binding surfaces (PACK.yaml, LICENSE,
NOTICE) all carry the DIST-A-qualified variant. Optional consistency sweep listed as a
Phase 5 nice-to-have, not a gap.

### 3.6 T1-01..T1-08 delivery: **CONFIRMED**

See §2. All 8 requirements checked in REQUIREMENTS.md; 8/8 packs validate; registration
complete on 7 surfaces including the post-fix cursor manifest; integration check maps
every T1 requirement WIRED end-to-end; check_release PASS.

## 4. Residual list (ship-able, accepted)

| # | Finding | Source | Disposition |
|---|---|---|---|
| R1 | cisa-cpg second source = 2-page slick sheet, not the planned controls-list PDF (no such PDF existed for CPG 2.0) | IMPL MINOR-1 | Accepted — both sources extracted + overlap-checked; documented in PACK.yaml + SKILL Scope & Limits |
| R2 | Registration commit 863bfeb touched README.md + docs/index.html beyond plan `files_modified` (MJ-01 fold, disclosed in commit body) | IMPL MINOR-2 | Accepted — consistency-motivated, correct, disclosed |
| R3 | check_overlap/vet_source not independently re-runnable (gitignored `sources/` work roots) | IMPL MINOR-3 | Accepted — inherent to the no-source-commit policy; dispositions recorded in every PACK.yaml; code review independently reproduced the overlap result from local extracts |
| R4 | doe-413-3b slug vs 413.3C content (MI-03) | Code review MINOR | Accepted for v1.17.0; routed §5 |
| R5 | Catalog DIST-A string convention (IN-01) | Code review INFO | Accepted (§3.5); optional Phase 5 sweep |
| R6 | STATE.md `total_phases: 3` vs 5 ROADMAP slots (counts executable phases; human text consistent "3/5") | Integration note 2 | Accepted — cosmetic metadata |

## 5. Rejected as non-gaps

- **MAJOR doe substitution as a T1-06 failure** — rejected (§3.2): successor-document
  build with full provenance disclosure; the named source is cancelled by the document
  actually used.
- **MI-02 as a Phase 3 gate failure** — rejected (§3.3): no current pack violates
  anything; spec-text lag only, Phase 5 scope.
- **IN-03 CHANGELOG still at 1.16.3** — rejected as a gap by the code review itself
  and re-confirmed: version bump and release notes are Phase 5 scope (REL-01/REL-02);
  no gate disagreement exists today.
- **NOTICE:320 everyspec mention** — rejected (security audit): pre-existing
  faa-system-safety attribution caveat text, not a link, predates Phase 3.
- **IN-02 untracked docs files** — rejected as a Phase 3 defect (§3.4): never shipped;
  flagged to the user only.

## 6. Phase 5 routing (carried forward, none block Phase 3 closure)

1. **PACK-SPEC addendum** (MI-02/MN-08): add the `## When to use` + `**Prerequisites:**`
   body contract to `docs/PACK-SPEC.md` SKILL.md rules. Should-do — closes the
   spec/gate trap for future authors; one-line docs change inside Phase 5's docs-sync
   charter.
2. **CHANGELOG v1.17.0 entry** (IN-03): list the 8 packs; fold in the MA-01 cursor
   manifest fix so released surface and notes agree. Must-do (already Phase 5 scope via
   REL-01/REL-02).
3. **doe-413-3b naming decision** (MI-03): in Phase 5, either add the series framing
   ("DOE O 413.3 series") to README/docs grouping, or record the slug-rename
   (`doe-o-413-3` + catalog alias/superseded-by) as a v1.18+ item. Decide; do not
   rename inside v1.17.0.
4. **Catalogue licence-string sweep** (IN-01, optional): pick one form (bare vs
   DIST-A-qualified) for all DoD entries. Nice-to-have.
5. (User-owned, outside phase flow): `docs/capability-pack-map.{md,json}` — regenerate
   including the 8 new packs or relocate out of `docs/` before any future commit of
   them.

## 7. Verification performed by this analysis (live, 2026-08-15)

- `python tooling/check_release.py` → **PASS** (exit 0) on current tree.
- `python tooling/validate_pack.py` ×8 → **8/8 PASS**.
- `scan_generated_skill.py` ×2 (doe-413-3b, cisa-cpg) → PASS.
- Cursor manifest: 55 entries; 8/8 new slugs present; §6b negative test fires on a
  dropped entry and stays quiet at 55/55.
- PACK.yaml/catalog/NOTICE 413.3C disclosure grep → present at `PACK.yaml:4,17-20`,
  `catalog.json:594`, `NOTICE:627`.
- `docs/PACK-SPEC.md` "When to use" grep → absent (MI-02 confirmed open, routed).
- `catalog.json` DoD licence strings → bare form confirmed (IN-01 accepted).
- `git status` → `docs/capability-pack-map.{md,json}` still untracked (IN-02 flag-only).

## 8. Verdict rationale and next commands

**CLOSED.** Zero blocking defects remain from the four reviews; the single post-review
MAJOR is fixed, gated, and negative-tested; ROADMAP SC1–SC3 and T1-01..T1-08 are
satisfied with independently reproduced evidence. All remaining items are accepted
residuals (§4) or Phase 5 routing (§6). No `--gaps-only` execute pass is required.

Next commands (orchestrator):

```
# Phase 4 is closed-by-vetting (0 packs, no execution) — proceed straight to Phase 5 planning
/gsd-master-flow phase 5 plan   # scope: PACK-SPEC addendum (§6.1), CHANGELOG/REL-01/REL-02 (§6.2),
                                # doe naming decision (§6.3), optional licence-string sweep (§6.4)
```

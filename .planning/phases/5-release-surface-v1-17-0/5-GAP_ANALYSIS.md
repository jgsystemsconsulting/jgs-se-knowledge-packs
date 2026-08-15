# Phase 5: Gap Analysis — Release surface v1.17.0

**Date:** 2026-08-14
**Inputs:** 5-IMPL_REVIEW, 5-CODE_REVIEW, 5-INTEGRATION_CHECK, 5-SECURITY_AUDIT (all present, none skipped) + 5-RESEARCH / 5-01-PLAN / 5-01-SUMMARY / 5-PLAN_CHECK / 5-PLAN_REVIEW / ROADMAP Phase 5 / REQUIREMENTS REL-01/REL-02
**Method:** Adjudication of all post-execute findings against ROADMAP success criteria, with independent live re-verification of the release state (gate re-run, catalog/dir counts, tag on origin, GitHub Release).

**Verdict:** CLOSED

All four reviews returned PASS / SECURED with zero blockers, zero majors, zero high/medium security findings open. Every Phase 5 success criterion is independently verified TRUE. Residual notes are ship-able; no execute re-entry (`--gaps-only`) is required.

## Success-Criteria Cross-Check (ROADMAP Phase 5 / REQUIREMENTS)

| Criterion | Requirement | Status | Evidence (independently reproduced at gap-analysis time) |
|---|---|---|---|
| SC-1: `check_release.py` exits 0; catalog basis 54 / directory basis 56 | REL-01 | VERIFIED | Live re-run: `RELEASE CHECK: PASS`, exit 0. `catalog.json` packs = 54; `packs/` dirs = 56 (48 baseline + 8 Tier-1, minus 2 signposts in catalog). All 8 Phase-3 slugs present on catalog.json, SKILLS.md, docs/packs.html, NOTICE (impl/code/integration reviews agree). |
| SC-2: v1.17.0 tagged and released | REL-02 | VERIFIED | Annotated tag `v1.17.0` (colon-style message) peels to release commit `bcd32af`; present on origin (`git ls-remote`). GitHub Release `v1.17.0` published, `isDraft: false`, `isPrerelease: false`, CHANGELOG-derived URL-free notes. |
| REL-01: catalog/SKILLS/packs.html/NOTICE include all new packs, no drift | REL-01 | VERIFIED | 10/10 integration connections WIRED; packs.html byte-identical on regeneration (§5c); README badge `packs-54` agrees with table (54 live rows + 1 planned). REQUIREMENTS REL-01 checked. |
| REL-02: tagged at 56-pack basis; packs pass validate + scan | REL-02 | VERIFIED | validate_pack spot checks PASS (nist-800-171, doe-413-3b); scan_generated_skill ran at Phase-3 build time, Phase-5 re-run was an accepted, recorded residual (see below). REQUIREMENTS REL-02 checked. |

## Thread Adjudication

1. **Impl MINOR-01/02/03 (EOF-newline in plugin.json, REQUIREMENTS.md edit scope, README framing-line placement)** — ACCEPT as ship-able residuals. All three are cosmetic or record-keeping only; the impl review itself marks each "Fix: None required". Content correctness of all 11 version surfaces, chapter counts, and README rows was verified live.
2. **Code MI-01 (CHANGELOG lists `docs/index.html` among "registered" surfaces)** — ACCEPT-AS-SHIPPED; carry wording fix to v1.18. `docs/index.html` is a version-bump surface, not a pack-enumeration surface, so the 1.17.0 entry prose overstates it. It is not a REL-01 defect (REL-01's surfaces — catalog.json, SKILLS.md, packs.html, NOTICE — are all verified correct), and the reviewer's own fix guidance is to correct it in the next CHANGELOG entry, never to rewrite published history.
3. **Integration WARNING (ROADMAP T2-ID citations resolve via REQUIREMENTS.md extra hop)** — ACCEPT. Documentation citation indirection with no functional impact; the chain resolves (ROADMAP L53 signposts REQUIREMENTS.md, which cross-links SOURCE-VETTING by source name). Doc-hygiene carry-forward for v1.18.
4. **Security Note 1 (branch-protection bypass notice on the release push to main)** — ACCEPT for this release; governance carry-forward for v1.18. Not phase-introduced attack surface, no declared threat covers repo governance, and tamper evidence is provided by the annotated tag + remote ref verification (T-5-02 CLOSED). Suggest enforced branch protection or a required release workflow in v1.18 planning.
5. **REL-01/REL-02 delivery** — CONFIRMED, both. Gate PASS at 54/56 basis, tag on origin, published GitHub Release, requirements checkboxes checked; see cross-check table above.

## Residual Notes That Ship (no action required)

- plugin.json trailing-newline-at-EOF included in the release commit (impl MINOR-01; history-only).
- fab28bd edited REQUIREMENTS.md beyond the Task 7 file list (impl MINOR-02; `.planning/`-only, content-consistent).
- README doe-413-3b framing line sits after the planned `mit-ocw-se` row rather than before it (impl MINOR-03; adjacent and functionally correct).
- Uncommitted workflow state (`master_flow_state.json` x2) + 3 untracked user files under `docs/` — correctly excluded from the release commit; explicit-path staging rule recorded (code MI-02).
- GitHub Release title em dash (code MI-03; documented house-style exception matching v1.16.3, so future reviewers do not re-flag).
- Bare source-host domain names in CHANGELOG/release notes prose (security Note 2; policy-conformant — named, not linked).
- Temp release-notes file left no repo residue (security Note 3; verified absent from tree and history).
- `scan_generated_skill.py` not re-run in Phase 5 (accepted residual recorded in SUMMARY/STATE; packs were scanned at Phase-3 build; content untouched since).

## Rejected as Non-Gaps

- **MI-01 as a release defect:** the imprecision lives in shipped prose, not in any gated or requirement-bearing surface; correcting it requires no code/path change and must not touch published history. Classified as v1.18 wording carry-forward, not a Phase 5 gap.
- **T2-03 open checkbox vs checked ROADMAP Phase 4:** designed reconciliation — Phase 4 closed by vetting (0 Tier-2 packs) while T2-03's future-half stays open as the documented v1.18+ revival path.
- **`immutable: false` on the GitHub Release:** informational, not part of the release gate.
- **Post-tag planning commits (fab28bd, d99c348, 85f4e5d + review artifacts):** touch only `.planning/`; release surfaces identical between tag and HEAD (verified via `git diff --name-only v1.17.0 HEAD` in prior reviews).

## v1.18 Carry-Forward List

1. **CHANGELOG wording fix:** in the next entry (e.g., a "Fixed" line), drop `docs/index.html` from the registered-surfaces claim or reword to "version surfaces bumped (incl. docs/index.html REV)". Do NOT rewrite the published 1.17.0 entry.
2. **Repo governance:** enforce branch protection on `main` (or adopt a required release workflow) so release pushes no longer rely on bypass; keep the annotated tag as tamper-evidence control.
3. **Doc hygiene:** add T2-01/T2-02/T2-03 tokens (or source-name anchors) to `docs/SOURCE-VETTING.md` so ROADMAP L12 citations resolve without the REQUIREMENTS.md hop.
4. **`doe-413-3b` → `doe-o-413-3` rename with catalog alias** (deferred decision recorded in SUMMARY key-decisions).
5. **Stale untracked user docs:** refresh or discard `docs/capability-pack-map.{md,json}` (claim pre-v1.17 completeness); keep `docs/ROLE-AGENTS-REQUIREMENTS-V2.md` out of commits unless the user directs otherwise.
6. **Re-run `scan_generated_skill.py` across all 56 packs** if any pack content changes in v1.18 (closes the accepted Phase 5 skip).

## Next Commands

None required — verdict is CLOSED. v1.18 planning should seed its backlog from the carry-forward list above; no `plan-phase --gaps` / `execute --gaps-only` re-entry is warranted for Phase 5.

---

*Gap analysis artifact — Phase 5, v1.17.0 release surface.*

# Integration Check — Phase 5 (Release surface v1.17.0)

**Date:** 2026-08-14
**Scope:** Phase 5 v1.17.0 release; cross-phase wiring to Phase 2 (vetting) and Phase 3 (Tier-1 packs)
**Method:** Independent re-execution of every E2E check; no SUMMARY claims taken on trust. Tag-tree content verified separately from working-tree content (fresh-clone view).

**Verdict:** PASS_WITH_NOTES

- BLOCKERS: 0
- WARNINGS: 1 (documentation citation indirection; no functional impact)
- All 8 requested E2E checks verified end-to-end.

---

## E2E Verification Results

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | Fresh-clone sim: `git ls-remote` tag v1.17.0 → release commit | WIRED | `refs/tags/v1.17.0` = `2a8b0cb` (annotated tag object), `refs/tags/v1.17.0^{}` = `bcd32af` = release commit `release(v1.17.0): 8 Tier-1 public-domain packs (54 +2 signposts)`. Local tag peels to same hash. `origin/main` (`d99c348`) is 2 planning-only commits ahead; `git diff --name-only v1.17.0..origin/main` shows only `.planning/*` files, so release surfaces at tag == working tree. |
| 2 | `python install.py --dry-run` discovers 56 packs | WIRED | 56 `would install` lines, exit 0, ends `Dry run — nothing written.` |
| 3 | catalog.json 54 entries, JSON-valid | WIRED | `json.load` OK, `len(packs) == 54`; schema key is `slug`. All 8 Phase-3 packs present (`nist-800-171`, `nist-800-61`, `cisa-cpg`, `doe-sem`, `mil-hdbk-338`, `mil-hdbk-516`, `nasa-ms-7009`, `doe-413-3b`). The 2 signposts (`omg-signpost`, `se-standards-signpost`) are intentionally absent from catalog — the designed 54+2 basis (56 dirs, 54 catalog). |
| 4 | `python tooling/check_release.py` | WIRED | Output `RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.`, exit 0. |
| 5 | `gen_packs_page.py` byte-identical (§5c) | WIRED | md5 before == after (`9edac9684cf465c9df791d86afd389d6`); `git status docs/packs.html` clean after regeneration. |
| 6 | GitHub Release v1.17.0 with notes | WIRED | `gh release view v1.17.0`: published, draft=false, prerelease=false, url `.../releases/tag/v1.17.0`; notes are CHANGELOG-derived (all 8 packs with matching chapter counts, SOURCE-VETTING register item, PACK-SPEC RR-S-13 item). |
| 7 | Version surfaces agree at 1.17.0 | WIRED | Verified in BOTH working tree and tag tree (`git show v1.17.0:...`): `.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json`, RELEASE-INFO (Version/Tag/Staged), README badge (L10) + prose (L58, L217), docs/index.html REV ×2, docs/packs.html REV, website YAMLs ×2, CHANGELOG `## [1.17.0]: 2026-08-15`. Zero stale `1.16.3` outside CHANGELOG history / `.planning` / `sources/`. |
| 8 | ROADMAP chain complete | WIRED | Phases 1, 2, 3, 5 checked; Phase 4 checked with explicit `closed by vetting: 0 packs` closure; 5-01-PLAN.md checked (ROADMAP L68). |

## Cross-Phase Wiring

| Connection | Status | Evidence |
|------------|--------|----------|
| Phase 3 packs → catalog.json | WIRED | All 8 slugs present among 54 entries |
| Phase 3 packs → SKILLS.md | WIRED | Each of the 8 slugs found |
| Phase 3 packs → README pack table | WIRED | 8 rows (README ~156–163) with chapter counts 8/6/5/7/9/8/7/6 matching PACK.yaml values recorded in SUMMARY |
| Phase 3 packs → NOTICE | WIRED | 8 slugs present (16 matches) |
| Phase 3 packs → install surface | WIRED | All 8 in dry-run output |
| Phase 3 packs → packs.html | WIRED | Generator reports 56 packs; byte-identical on re-run |
| Phase 2 vetting → Phase 4 closure | WIRED (with WARNING, see below) | ROADMAP Phase 4 → REQUIREMENTS.md T2-01/T2-02 (excluded-by-vetting, struck through) / T2-03 (deferred-excluded) → docs/SOURCE-VETTING.md Excluded rows for IEEE 15288.2-2014 and ECSS-E-ST-10C Rev.1 (Verified 2026-08-14) + Def Stan 00-051 "UNVERIFIED / excluded from this milestone" section. SOURCE-VETTING.md is committed at tag v1.17.0. |
| RELEASE-INFO → packs.html | WIRED | Regeneration from RELEASE-INFO is idempotent (§5c) |

## Detailed Findings

### Missing Connections (BLOCKER)

None.

### Warnings

1. **ROADMAP Phase-4 citation indirection (doc hygiene, no functional impact).** ROADMAP L12 reads `closed by vetting: 0 packs (T2-01/T2-02 Excluded, T2-03 deferred; see docs/SOURCE-VETTING.md)`, but the literal tokens `T2-01/T2-02/T2-03` appear nowhere in docs/SOURCE-VETTING.md — they resolve only through `.planning/REQUIREMENTS.md` L39–41, which does cross-link SOURCE-VETTING by source name (IEEE 15288.2-2014, ECSS-E-ST-10C Rev.1, Def Stan 00-051 — all present in the vetting doc with rationale and dates). The chain resolves via one extra hop that ROADMAP itself signposts at L53 (`see REQUIREMENTS.md`). A reader grepping `T2-01` in SOURCE-VETTING.md directly finds nothing.

### Informational Notes (no action required for this release)

- `origin/main` HEAD (`d99c348`) is 2 commits past the tag; both touch only `.planning/*`. This matches the stated pattern (planning records commit after the annotated tag); release-relevant files are identical between tag and working tree.
- REQUIREMENTS.md T2-03 remains an open `[ ]` checkbox while ROADMAP Phase 4 is checked. This is the designed reconciliation: Phase 4 is "closed by vetting" (0 Tier-2 packs), while T2-03's future-half (build if terms permit) stays open as a v1.18+ revival path with the 00-051/00-056 subject-mismatch correction recorded.
- `gh release view` reports `immutable: false` — informational only; not part of the release gate.
- Untracked user-owned files `docs/ROLE-AGENTS-REQUIREMENTS-V2.md`, `docs/capability-pack-map.{md,json}` were correctly kept out of the release commit (explicit-path staging confirmed by SUMMARY and by tag tree contents).

## Requirements Integration Map

| Requirement | Integration Path | Status | Issue |
|-------------|-----------------|--------|-------|
| REL-01 | Phase 3 packs → catalog/SKILLS/README/NOTICE/packs.html → gate PASS at 54/56 | WIRED | — |
| REL-02 | Release commit bcd32af → annotated tag v1.17.0 (remote peel verified) → GitHub Release with CHANGELOG-derived notes | WIRED | — |
| RO-01 | Research → docs/SOURCE-VETTING.md Excluded table (committed at tag) → ROADMAP Phase-2 checkbox | WIRED | — |
| T2-01 | Vetting outcome → REQUIREMENTS.md struck-through entry → SOURCE-VETTING IEEE 15288.2-2014 row | WIRED | — |
| T2-02 | Vetting outcome → REQUIREMENTS.md struck-through entry → SOURCE-VETTING ECSS-E-ST-10C row | WIRED | — |
| T2-03 | Vetting outcome → REQUIREMENTS.md open deferred entry → SOURCE-VETTING Def Stan 00-051 UNVERIFIED section → ROADMAP Phase-4 closure | WIRED | Open checkbox is intentional (future-half deferred); ROADMAP cites SOURCE-VETTING with tokens that live only in REQUIREMENTS.md (Warning 1) |
| T1-01..T1-08 | Phase 3 pack builds → 5 registration surfaces + install dry-run + release notes | WIRED | — |
| PACK-01..03, TOOL-01..03 | Self-contained within phases 1/3 (validated by gate + validate_pack) | WIRED (gate-mediated) | No direct cross-phase surface; integrity enforced through check_release.py, which PASSes |

**Requirements with no cross-phase wiring:** none — every release-relevant requirement terminates on at least one other phase's artifact.

## Summary

- E2E flows: 8/8 complete, 0 broken.
- Cross-phase connections: 10/10 WIRED; 1 carries a documentation-level WARNING (citation indirection).
- Fresh-clone guarantee: tag-tree content independently verified — version surfaces, vetting doc, catalog, and pack registration all present and consistent at `v1.17.0` itself, not just in the post-tag working tree.

**Verdict:** PASS_WITH_NOTES

# Phase 9 Integration Check — Release Surface v1.18.0

**Range audited:** release commit `d19be1a` + tag `v1.18.0` (tag object `cae0145`) + GitHub Release; tag tree vs working tree vs HEAD `98bd340`.
**Date:** 2026-08-17
**Method:** live command runs on the current tree (`install.py --dry-run`, `check_release.py`, `check_capability_map.py`, `gen_packs_page.py` regen + git-diff), `git ls-remote` / `gh release view` remote truth, programmatic JSON reconciliation of every registration surface, tag-object inspection (`git cat-file -p`).

**Verdict:** PASS_WITH_NOTES

## Wiring Summary

| # | Connection | Status | Evidence |
|---|---|---|---|
| 1 | Tag peels to release commit | WIRED | `git ls-remote --tags origin`: `refs/tags/v1.18.0` = `cae0145` (tag object), `refs/tags/v1.18.0^{}` = `d19be1a7463…` — exactly the release commit. Local tag resolves identically (`git rev-parse v1.18.0^{}` = `d19be1a`). No shadow variants (no rc/beta tags match `1.18`). |
| 2 | Tag tree == working tree for release surfaces | WIRED | `git diff --name-only v1.18.0 HEAD` = 6 files, all under `.planning/` (MILESTONES, REQUIREMENTS, ROADMAP, STATE, 9-01-SUMMARY, phase master_flow_state.json). Zero release-surface drift (packs/, catalog.json, docs/, tooling/, manifests untouched post-tag). Working tree clean (`git status --short` empty), so working tree == HEAD == tag for release surfaces. |
| 3 | Installer sees the full release payload | WIRED | `python install.py --dry-run` → 63 `would install` lines. Reconciles exactly: 63 dirs in `packs/` = 61 content packs + 2 signposts (`omg-signpost`, `se-standards-signpost`). Matches release-notes arithmetic "61 packs (+2 signposts)". |
| 4 | Release gate PASS | WIRED | `python tooling/check_release.py` → `RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.` (version single-source, SKILLS.md count, cursor-manifest coverage, packs-page freshness, file furniture all inside the gate). |
| 5 | Capability-map gate PASS (Phase 8 → 9 handoff) | WIRED | `python tooling/check_capability_map.py` → cluster totals incl. `Training & Documentation Delivery: 12`, `TOTAL: 628`, `PASS: capability map OK`. Map envelope on tag: `schema_version: 2`, `map_version: "1.18.0"`, `generated_on: "2026-08-17"` (32 clusters, 628 entries). |
| 6 | Generated page byte-identical | WIRED | `python tooling/gen_packs_page.py` → "wrote docs\packs.html (63 packs)"; `git status`/`git diff` on `docs/packs.html` → empty. File is tracked (`git ls-files` lists it) and not gitignored (`git check-ignore` exit 1), so the check is non-vacuous. (Also independently enforced inside `check_release.py` §"fresh".) |
| 7 | All version surfaces agree at 1.18.0 | WIRED | `.claude-plugin/plugin.json` `version: 1.18.0`; `.cursor-plugin/plugin.json` bumped in the release commit; README badge + line 58 + changelog pointer line 224; CHANGELOG `## [1.18.0]: 2026-08-17`; RELEASE-INFO.txt `Version: 1.18.0` / `Tag: v1.18.0`; docs/packs.html REV 1.18.0; docs/index.html REV ×2; capability-pack-map.json `map_version: 1.18.0`; capability-pack-map.md "(v1.18.0)" changelog line; SOURCE-VETTING.md "(v1.18.0)" section header. Stale-version sweep: zero `1.17.0` outside CHANGELOG history / `.planning`. |
| 8 | GitHub Release published, not draft | WIRED | `gh release view v1.18.0` → `isDraft: false`, `isPrerelease: false`, `publishedAt: 2026-08-17T01:03:47Z`, `tagName: v1.18.0`; `gh release list` shows it as `Latest`. Single release for the version, no duplicates. |
| 9 | ROADMAP phases 6–9 chain closed | WIRED | ROADMAP "v1.18 Phases": Phase 6 `[x]`, Phase 7 `[x]`, Phase 8 `[x]`, Phase 9 `[x]`. Dependency chain explicit: Phase 7 "Depends on: Phase 6", Phase 8 "Depends on: Phase 7", Phase 9 "Depends on: Phase 8". STATE.md `last_activity_desc: Phase 9 plan 01 executed — v1.18.0 released`. |
| 10 | Registration surfaces mutually consistent | WIRED | Programmatic reconciliation: catalog.json = 61 pack slugs, every slug matches a `packs/` dir, zero orphans either direction; `doe-413-3b` retained as `aliases` field on the `doe-o-413-3` entry (rename disclosed in release notes). Cursor manifest = 62 skills = all 63 dirs minus `sebok` (`commercial_use: false`, CC BY-NC-SA 3.0) — exclusion is gate-enforced by design (`check_release.py` §6b filters `commercial_use: false` packs), not drift. |
| 11 | Phase 8 exports consumed in Phase 9 | WIRED | `capability-pack-map.md:14` links `docs/capability-map-CONTRACT.md` (resolves); `docs/ROLE-AGENTS-REQUIREMENTS-V2.md` references map/contract 4×; map `map_version` tracks the release (1.18.0) per CONTRACT §"map_version tracks the release that regenerated the map". |

## E2E Flows

**Complete (4):**
1. User installs release: tag on origin → clone → `install.py` → 63 skills offered (dry-run verified end-to-end; nothing written).
2. Downstream agent consumes map: release tag → `capability-pack-map.json` v2 envelope (`schema_version`/`map_version`/`generated_on`) → `clusters[].chapters[].{pack, chapter}` reads verify (gate validates all 628 entries + existence on disk).
3. Release regeneration: `gen_packs_page.py` on a fresh clone of the tag → byte-identical `docs/packs.html` (proves the checked-in page is exactly what the generator emits at 1.18.0).
4. Validator reproduces release readiness: both gates green on the tag tree in one working session.

**Broken:** none.

## Notes (non-blocking)

1. **Map gate is standalone, not chained into `check_release.py`** (WARNING, documented deferral): a green `check_release.py` alone does not prove map freshness — `check_capability_map.py` must be run as a second command. Tracked at STATE.md ("Optional map-gate wiring into check_release (Phase 8 deferred)") and adjacent to FUT-05. Current release is unaffected: both gates were run and both PASS.
2. **Informational — catalog.json `updated: 2026-08-16`** vs release date 2026-08-17: a content-date field (last catalog-content edit), not a semver surface; `check_release.py` does not and need not compare it to the release date. No action required.

## Requirements Integration Map

| Requirement | Integration Path | Status | Issue |
|-------------|-----------------|--------|-------|
| VET-01 | Phase 6 vetting → SOURCE-VETTING "(v1.18.0)" vetted rows (GP tokens greppable, dated) → Phase 7 build licence basis | WIRED | — |
| VET-02 | Phase 6 → SOURCE-VETTING Excluded table additions → gate/file furniture checks | WIRED | — |
| GP-01 (dod-vva-rpg) | Phase 7 build → Phase 8 map classification → Phase 9 registration (catalog/SKILLS.md/packs.html/NOTICE/README/cursor) + tag | WIRED | — |
| GP-02 (faa-std-025) | same chain | WIRED | — |
| GP-03 (dote-te-guidebook) | same chain | WIRED | — |
| GP-04 (dafman-63-119) | same chain | WIRED | — |
| GP-05 (mil-std-881f) | same chain | WIRED | — |
| GP-06 (federal-bca) | same chain; single-source honesty recorded (PACK.yaml + FUT-04) | WIRED | — |
| GP-07 (mil-std-40051) | same chain; empty cluster 25 fattened to 12 entries (map run output) | WIRED | — |
| AE-01 | Phase 8 gate + CONTRACT → map_version tracked to release 1.18.0 (delivered gate-not-generator, honestly annotated) | WIRED | — |
| AE-02 | Phase 7 packs → Phase 8 map regen (628 entries, thresholds live) → Phase 9 release carries it | WIRED | — |
| AE-03 | Phase 8 → docs/ROLE-AGENTS-REQUIREMENTS-V2.md ↔ map/CONTRACT cross-links (4 refs) | WIRED | — |
| REL-1x-01 | 7 new packs registered on all 6 surfaces + check_release PASS | WIRED | — |
| REL-1x-02 | Tag `v1.18.0` (annotated, origin) + GitHub Release published; CHANGELOG carries v1.17.0 wording fix + rename note | WIRED | — |
| GP-08 (descoped) | decision record only (REQUIREMENTS Out of Scope, strikethrough) | N/A (no wiring intended) | — |
| FUT-04 / FUT-05 | backlog records only | N/A (future) | — |

**Requirements with no cross-phase wiring:** GP-08 (descoped by decision), FUT-04/FUT-05 (future backlog) — self-contained by design, not missing connections.

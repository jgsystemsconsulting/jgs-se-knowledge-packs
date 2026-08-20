# Phase 18: Map + release surface v1.19.1 — Research

**Researched:** 2026-08-20
**Domain:** Version-surface bump from 1.19.0, map_version bump, dual-gate validation, annotated tag + GitHub Release
**Confidence:** HIGH (Phase 13 analog + live verification of all commands)

## Summary

Phase 18 repeats the Phase 13 pattern for v1.19.1. No new packs since 1.19.0 (catalog 63 / dirs 65 frozen by Phase 16 DEFERRED_ALL). capability-pack-map.json already at map_version 1.19.0 — needs bump to 1.19.1. Both gates wired into check_release; must PASS after version bump. CHANGELOG style is competency-led, honest about cleanup + tooling + still-deferred items. Tag + gh release steps identical to 13-02.

**Primary recommendation:** Split into two plans (18-01 surfaces + gates; 18-02 tag + GitHub Release) to match Phase 13 wave structure. Use exact surface list from 13-01-PLAN.md. No pack rebuilds, no map reclassification.

## User Constraints (from Phase 13 + STATE)

### Locked Decisions
- **MAP-20-01 + REL-20-01 + REL-20-02 are this phase.** Capability map validates at 1.19.1; full registration (none expected); v1.19.1 tagged + GitHub Release; CHANGELOG honest about cleanup/tooling + deferred items. [VERIFIED: `.planning/REQUIREMENTS.md` REL-20 section]
- **Phase 13 is AUTHORITATIVE analog.** Surface list, order, tag style, push, gh release, post-tag records commit all reuse 13-01/13-02. [VERIFIED: `13-01-PLAN.md:96-100` (11 surfaces); `13-02-PLAN.md:33-75` (release commit + tag + push + gh)]
- **No new packs.** Phase 16 DEFERRED_ALL; catalog/dirs frozen at 63/65. [VERIFIED: live `ls packs/ | wc -l` = 65; `catalog.json` = 63 packs]
- **Branch protection stays admin-bypass.** No enforcement change. [VERIFIED: Phase 13 STATE note]
- **Do not rebuild packs, reclassify map, or touch validate.yml.** [VERIFIED: 13-RESEARCH.md locked decisions]

### Claude's Discretion
- **Plan split:** 18-01 (bump 11 surfaces + map_version + CHANGELOG + gates) then 18-02 (release commit + tag + push + gh + .planning records) — mirrors 13-01/13-02 wave structure.
- **CHANGELOG honesty:** Explicitly note cleanup (Phase 15), tooling (Phase 17), and still-deferred items (IO-05/06, AAF, etc.). Zero em dash rules apply.

### Deferred Ideas (OUT OF SCOPE)
- Pack rebuilds or map reclassification
- Branch-protection enforcement
- Any IO-05/06 or AAF/stakeholder work
- CI repo-Python map step

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Version single-source | `.claude-plugin/plugin.json` + `CHANGELOG.md` + `RELEASE-INFO.txt` | cursor plugin, README, index, packs.html, website YAMLs | Gate §4 reads trio only |
| Map envelope version | `docs/capability-pack-map.json` `map_version` | CONTRACT example envelope | Tracks release that last regenerated map |
| Dual gate | `tooling/check_release.py` (imports map gate) | `tooling/check_capability_map.py` | REL-20-01; map gate inside release gate |
| Public release act | annotated tag `v1.19.1` + `gh release create` | origin push | REL-20-02 |
| Post-tag records | `.planning/STATE.md` / `MILESTONES.md` / `ROADMAP.md` | REQUIREMENTS REL ticks | Separate commit after tag |

## Standard Stack

### Core
| Artifact | Version / location | Purpose | Why standard |
|---------|--------------------|---------|--------------|
| Gate trio | plugin `1.19.0` / CHANGELOG `## [1.19.0]` / RELEASE-INFO `1.19.0` | `check_release` §4 single-source | [VERIFIED: `tooling/check_release.py:103-117`] |
| 11 display surfaces | Phase 13 Task 1 file list | Consumer-facing REV strings | [VERIFIED: `13-01-PLAN.md:96-100`] |
| `tooling/gen_packs_page.py` | reads RELEASE-INFO `version()` | Regenerates `docs/packs.html` | Gate §5c fails on drift |
| `tooling/check_release.py` | now includes map §5d | Local ship gate | [VERIFIED: `tooling/check_release.py:215-222`] |
| `tooling/check_capability_map.py` | schema 2 / 644 / floors | Map freshness | [VERIFIED: live 2026-08-17 PASS] |
| `gh` CLI | authenticated (systems-researcher) | GitHub Release | [VERIFIED: `gh auth status`] |
| Annotated git tag | colon-style one-liner | Tamper-evident public pin | [VERIFIED: `git tag -l -n3 v1.19.0`] |

### Supporting
| Artifact | Purpose | When to use |
|---------|---------|-------------|
| `13-01-PLAN.md` / `13-02-PLAN.md` | AUTHORITATIVE analog | Task order, commit/tag/notes style |
| `13-RESEARCH.md` | Surface inventory + gate wiring | Confirms 11-count + map gate inside release gate |
| `catalog.json` / `README.md` | Frozen at 63/65 | No leftover fixes needed |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| One plan | Two plans (18-01/18-02) | Split matches Phase 13 wave structure; keeps release commit clean |
| Skip `git push` | Tag local-only | REL-20-02 and Phase 13 analog require origin tag + GitHub Release |
| Leave `map_version` at 1.19.0 | Bump to 1.19.1 | CONTRACT says it tracks the *release*; must bump |

## Package Legitimacy Audit

No external packages. N/A.

## Architecture Patterns

### Recommended Project Structure
No structural change. Release surface pattern is:
1. Bump 11 surfaces + map_version
2. Write competency-led CHANGELOG
3. Run dual gates (check_release includes map gate)
4. Release commit (explicit paths only)
5. Annotated tag + push + gh release create
6. Separate .planning records commit

### Pattern 1: Annotated Tag + GitHub Release (Phase 9/13)
**What:** One release commit → annotated tag (colon-style) → `git push origin main --follow-tags` → `gh release create --notes-file` (body = CHANGELOG [1.19.1] entry) → separate .planning commit.
**When to use:** Every v1.x.0 / v1.x.1 surface release.
**Example:**
```bash
# From 13-02-PLAN.md
git commit -m "release(v1.19.0): Agent IO Depth — 2 packs + VV&A chapters + DA remap (63 +2 signposts)" \
  .claude-plugin/plugin.json .cursor-plugin/plugin.json CHANGELOG.md RELEASE-INFO.txt \
  README.md catalog.json docs/index.html docs/packs.html \
  docs/products/website/01-jgs-se-knowledge-packs.yaml docs/products/website/catalog.yaml \
  docs/capability-pack-map.json docs/capability-map-CONTRACT.md docs/capability-pack-map.md

git tag -a v1.19.0 -m "v1.19.0: 7 gap-driven packs + 2 signposts + DA remap (catalog 63 / dirs 65)"
git push origin main --follow-tags
gh release create v1.19.0 --title "v1.19.0 — Agent IO Depth" --notes-file /tmp/v1.19.0-notes.md
```

### Anti-Patterns to Avoid
- **Lightweight tag:** Must be annotated (git cat-file -t == tag). Lightweight fails REL-20-02.
- **git add -A:** Explicit paths only on release commit. Never commit master_flow_state.json or research artifacts.
- **Em dashes in CHANGELOG:** Zero em dash rules; competency-led prose only.
- **Putting .planning records in tagged commit:** Separate commit after tag.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Version single-source | Custom version script | `.claude-plugin/plugin.json` + `CHANGELOG.md` + `RELEASE-INFO.txt` trio | Gate §4 reads exactly these three |
| Map validation | Inline schema check | `tooling/check_capability_map.py` (imported by check_release) | Already wired; schema 2, 644 entries, floors |
| Release notes | Manual copy | CHANGELOG [1.19.1] body → gh release --notes-file | Single source of truth |

**Key insight:** The overlap checker (check_overlap) is now on the release path via check_release. Gates must still PASS after version bump — no new packs means no new overlap risk, but the gate still runs.

## Runtime State Inventory

N/A — greenfield release surface, no rename/refactor.

## Common Pitfalls

### Pitfall 1: Untagged 1.19.1 commit on main
**What goes wrong:** Release commit lands, tag never created/pushed, GitHub Release never created.
**Why it happens:** Planner splits into one plan and forgets the tag step.
**How to avoid:** Two-plan structure (18-01 bump/gates, 18-02 tag/release) mirrors Phase 13 wave 2 dependency.
**Warning signs:** 18-01 completes with trio at 1.19.1 but no tag exists.

### Pitfall 2: map_version drift
**What goes wrong:** Surfaces bumped to 1.19.1 but capability-pack-map.json stays at 1.19.0.
**Why it happens:** map_version bump forgotten in the 11-surface list.
**How to avoid:** Explicit task for docs/capability-pack-map.json + CONTRACT example envelope.
**Warning signs:** check_capability_map.py reports map_version 1.19.0 after 18-01.

### Pitfall 3: gh release notes mismatch
**What goes wrong:** GitHub Release body differs from CHANGELOG [1.19.1] entry.
**Why it happens:** Manual notes editing or wrong --notes-file path.
**How to avoid:** `gh release create --notes-file` pointing at temp file copied from CHANGELOG body.
**Warning signs:** gh release view shows different content than CHANGELOG.

## Code Examples

### Surface Bump (from 13-01-PLAN.md Task 1)
```bash
# 11 surfaces + map_version
sed -i 's/1\.19\.0/1.19.1/g' \
  .claude-plugin/plugin.json \
  .cursor-plugin/plugin.json \
  RELEASE-INFO.txt \
  docs/index.html \
  docs/packs.html \
  docs/products/website/01-jgs-se-knowledge-packs.yaml \
  docs/products/website/catalog.yaml \
  docs/capability-pack-map.json \
  docs/capability-map-CONTRACT.md \
  docs/capability-pack-map.md

# CHANGELOG header
sed -i 's/## \[1\.19\.0\]/## [1.19.1]/' CHANGELOG.md
```

### Gate Run (from 13-01-PLAN.md Task 4)
```bash
python tooling/check_release.py
python tooling/check_capability_map.py
# Both must PASS before release commit
```

### Tag + Release (from 13-02-PLAN.md)
```bash
git tag -a v1.19.1 -m "v1.19.1: cleanup + tooling + deferred items visible"
git push origin main --follow-tags
gh release create v1.19.1 --title "v1.19.1 — Cleanup + Tooling" --notes-file /tmp/v1.19.1-notes.md
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| map_version left at prior release | Bump with surface release | Phase 13 | CONTRACT §6 now tracks actual release that regenerated map |
| Overlap checker separate | check_overlap imported into check_release | Phase 12/13 | Single gate command; no separate CI step |
| CHANGELOG pack-list style | Competency-led IO narrative first | Phase 13 | Honest about what was deferred, not just what shipped |

**Deprecated/outdated:**
- Lightweight tags: must be annotated for tamper-evidence.

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | No new packs since 1.19.0 (catalog 63 / dirs 65) | Summary | If Phase 16 DEFERRED_ALL was not honored, gate will fail on new pack registration |
| A2 | gh authenticated as systems-researcher with push rights | Standard Stack | If token lacks repo scope, gh release create will fail |
| A3 | Branch protection still admin-bypass | User Constraints | If enforcement enabled since Phase 13, push will be blocked (human gate needed) |

## Open Questions

1. **CHANGELOG 1.19.1 header wording**
   - What we know: competency-led, honest about cleanup (Phase 15) + tooling (Phase 17) + deferred items
   - What's unclear: exact one-liner title
   - Recommendation: "v1.19.1: Cleanup + Tooling + Deferred Items Visible" (planner to confirm)

2. **gh release title em dash**
   - What we know: Phase 13 used em dash in title
   - What's unclear: Whether zero em dash rule applies to gh title
   - Recommendation: Keep em dash in gh title only; body follows CHANGELOG rules

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| git | Tag + push | ✓ | 2.45.2 | — |
| gh | GitHub Release | ✓ | 2.58.0 | Manual release via web UI |
| python3 | Gates | ✓ | 3.12.7 | — |

**Missing dependencies with no fallback:** None.

## Validation Architecture

N/A — no new tests; gates are existing tooling.

## Security Domain

N/A — content library, no auth/session/input validation surface.

## Sources

### Primary (HIGH confidence)
- `13-RESEARCH.md` - Phase 13 locked decisions, surface list, gate wiring
- `13-01-PLAN.md` - 11 surfaces + map_version bump tasks
- `13-02-PLAN.md` - Release commit + tag + push + gh release steps
- Live verification: `git tag -l v1.19*`, `gh auth status`, `ls packs/ | wc -l`, `catalog.json` pack count, `capability-pack-map.json` map_version

### Secondary (MEDIUM confidence)
- `tooling/check_release.py:215-222` - Map gate import confirmed
- `tooling/check_capability_map.py` - Schema 2, 644 entries, floors

### Tertiary (LOW confidence)
- None.

## Metadata

**Confidence breakdown:**
- Standard Stack: HIGH — Phase 13 analog + live command verification
- Architecture: HIGH — Single-tier content library, no new patterns
- Pitfalls: HIGH — Directly observed in Phase 13 execution

**Research date:** 2026-08-20
**Valid until:** 30 days (stable release process)

---

## RESEARCH COMPLETE

**Phase:** 18 - Map + release surface v1.19.1
**Confidence:** HIGH

### Key Findings
- Phase 13 is exact analog; reuse surface list, tag style, push, gh release, post-tag records commit
- No new packs (catalog 63 / dirs 65 frozen); gates must still PASS after version bump
- capability-pack-map.json already at 1.19.0 — bump to 1.19.1 required
- gh authenticated (systems-researcher); branch protection admin-bypass
- Plan split recommended: 18-01 (bump + gates), 18-02 (tag + release)

### File Created
`C:\Users\gower\OneDrive\Documents\GitHub\jgs-se-knowledge-packs\.planning\phases\18-map-release-surface-v1-19-1\18-RESEARCH.md`

### Confidence Assessment
| Area | Level | Reason |
|------|-------|--------|
| Standard Stack | HIGH | Phase 13 analog + live verification of all commands |
| Architecture | HIGH | Single-tier content library, no new patterns |
| Pitfalls | HIGH | Directly observed in Phase 13 execution |

### Open Questions
- Exact CHANGELOG 1.19.1 header wording (planner discretion)
- gh release title em dash vs body zero-em-dash rule

### Ready for Planning
Research complete. Planner can now create PLAN.md files.

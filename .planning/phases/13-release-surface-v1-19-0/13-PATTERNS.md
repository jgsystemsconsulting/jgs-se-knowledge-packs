# Phase 13: Release surface + v1.19.0 - Pattern Map

**Mapped:** 2026-08-17
**Files analyzed:** 14 (explicit surfaces + planning records)
**Analogs found:** 14 / 14

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `.claude-plugin/plugin.json` | config | request-response (gate) | Phase 9 Task 1 | exact |
| `.cursor-plugin/plugin.json` | config | request-response (gate) | Phase 9 Task 1 | exact |
| `CHANGELOG.md` | doc | request-response (gate) | Phase 9 Task 2 | exact |
| `RELEASE-INFO.txt` | config | request-response (gate) | Phase 9 Task 1 | exact |
| `README.md` | doc | request-response | Phase 9 Task 1 | exact |
| `docs/index.html` | doc | request-response | Phase 9 Task 1 | exact |
| `docs/packs.html` | doc | request-response | Phase 9 Task 1 | exact (regenerated) |
| `docs/products/website/catalog.yaml` | config | request-response | Phase 9 Task 1 | exact |
| `docs/products/website/01-jgs-se-knowledge-packs.yaml` | config | request-response | Phase 9 Task 1 | exact |
| `docs/capability-pack-map.json` | config | request-response | Phase 9 Task 1 | exact |
| `docs/capability-map-CONTRACT.md` | doc | request-response | Phase 9 Task 3 | exact |
| `catalog.json` | config | request-response | Phase 9 (leftover pattern) | role-match |
| `.planning/STATE.md` | doc | request-response | Phase 9 Task 6 | exact |
| `.planning/MILESTONES.md` | doc | request-response | Phase 9 Task 6 | exact |
| `.planning/ROADMAP.md` | doc | request-response | Phase 9 Task 6 | exact |

## Pattern Assignments

### All 11 version surfaces + map_version (config/doc, request-response)

**Analog:** `.planning/phases/9-release-surface-v1-18-0/9-01-PLAN.md` Task 1

**Core pattern** (lines 96-101):
```
Bump 1.17.0 → 1.18.0 on all 11 surfaces. Order matters: edit RELEASE-INFO.txt FIRST (Version: 1.18.0, Tag: v1.18.0, Staged: real execution timestamp), then run `python tooling/gen_packs_page.py` to regenerate docs/packs.html (never hand-edit packs.html), then hand-edit the rest.
```

**Verify pattern** (line 99):
```
grep -rn "1\.17\.0" --exclude-dir=.planning --exclude-dir=.git --exclude-dir=sources . returns ONLY CHANGELOG history + 5 whitelisted historical lines.
```

### CHANGELOG entry (doc, request-response)

**Analog:** `.planning/phases/9-release-surface-v1-18-0/9-01-PLAN.md` Task 2

**Core pattern** (lines 104-108):
```
Insert `## [1.18.0]: <date>` entry above prior version. First line under heading is the rename note as plain paragraph (LEADS because breaking-adjacent). Then ### Added / ### Fixed / ### Changed sections. No em dashes; no URLs. Chapter counts sourced live from each packs/<slug>/PACK.yaml `chapters:` immediately before writing.
```

### Post-release records (doc, request-response)

**Analog:** `.planning/phases/9-release-surface-v1-18-0/9-01-PLAN.md` Task 6

**Core pattern** (lines 139-143):
```
After tag exists: STATE.md records shipped release (commit hash, tag, GitHub Release URL) + closes routing items + carries v1.19 backlog. MILESTONES.md converts "in execution" section to shipped record. ROADMAP.md ticks phase checkbox and fills **Plans** with plan filename. Separate .planning-only commit.
```

### Release commit / tag / push / gh (utility, event-driven)

**Analog:** `.planning/phases/9-release-surface-v1-18-0/9-01-PLAN.md` Task 5

**Core pattern** (lines 129-135):
```
Stage with EXPLICIT paths only (never -A). Commit message: `release(vX.Y.Z): …`. Annotated tag in colon style matching live tags: `git tag -a vX.Y.Z -m "vX.Y.Z: …"`. Push `git push origin main --follow-tags`. GitHub Release title uses em dash; body = CHANGELOG entry body written to phase-dir tmp file. Verify with `git ls-remote --tags` + `gh release view`.
```

## Shared Patterns

### Explicit-path staging only
**Source:** `9-01-PLAN.md:130` and `9-01-SUMMARY.md:221-226`
**Apply to:** Task 5 release commit
```
git status --short  # audit first
git add -- <explicit list of 11+ files>
# never git add -A or git add docs/
```

### Gate re-run immediately before commit
**Source:** `9-01-PLAN.md:123` (OneDrive sync-lag mitigation)
**Apply to:** Task 4 final step
```
python tooling/check_release.py  # must be last action before commit
```

### Competency-led CHANGELOG narrative
**Source:** RESEARCH.md §Pattern 4 + ROADMAP SC-2
**Apply to:** Task 2 CHANGELOG entry
```
Lead with IO-01..07 by competency (not pack slugs). IO-05/06 deferred, IO-07 accepted are first-class lines. Chapter counts = live PACK.yaml values.
```

### Historical 1.x.0 whitelist
**Source:** `9-01-PLAN.md:79`
**Apply to:** All version-bump tasks
```
1.17.0 references survive in: capability-map-CONTRACT.md:54, capability-pack-map.md:16, SOURCE-VETTING.md:93/144/149. Do not touch.
```

## No Analog Found

None. Every file has an exact Phase 9 analog.

## Metadata

**Analog search scope:** `.planning/phases/9-release-surface-v1-18-0/9-01-PLAN.md` + live 2026-08-17 files
**Files scanned:** 14
**Pattern extraction date:** 2026-08-17
**Key constraint:** One execute plan only; do not split bump vs tag.
# Phase 18: Map + release surface v1.19.1 — Patterns

**Researched:** 2026-08-20
**Domain:** Release surface bump + tag + GitHub Release patterns from Phase 13
**Confidence:** HIGH

## Pattern Library

### Pattern 1: 11-Surface Version Bump (Phase 9/13)
**What:** Single sed command updates all 11 consumer-facing version strings + map_version in one pass.
**When to use:** Every v1.x.0 / v1.x.1 surface release.
**Example:**
```bash
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
```
**Source:** `13-01-PLAN.md:96-100`

### Pattern 2: Competency-Led CHANGELOG Header
**What:** CHANGELOG [1.19.1] entry starts with competency narrative (IO-01..07), not pack list. Honest about deferred items.
**When to use:** Every release where IO work was primary driver.
**Example:**
```markdown
## [1.19.1] — Cleanup + Tooling + Deferred Items Visible

**IO Depth:** Phase 15 cleanup (gap-driven packs + signposts) + Phase 17 tooling (vet_source.py, check scripts) land on main. Deferred items (IO-05/06, AAF, stakeholder, DoDM/SP-7084/IS-300) remain visible in ROADMAP — not papered over.

**Packs:** 63 catalog / 65 dirs (frozen — Phase 16 DEFERRED_ALL). No new registration.

**Map:** capability-pack-map.json map_version 1.19.1; CONTRACT example envelope updated. 644 entries, schema 2, floors intact.

**Gates:** check_release PASS (includes map gate); check_capability_map PASS.
```
**Source:** `13-RESEARCH.md` locked decision on CHANGELOG shape

### Pattern 3: Annotated Tag + GitHub Release (Phase 9/13)
**What:** One release commit → annotated tag (colon-style message) → `git push origin main --follow-tags` → `gh release create --notes-file` (body = CHANGELOG entry) → separate .planning records commit.
**When to use:** Every v1.x.0 / v1.x.1 surface release.
**Example:**
```bash
# Release commit (explicit paths only)
git commit -m "release(v1.19.1): Cleanup + Tooling + Deferred Items Visible" \
  .claude-plugin/plugin.json .cursor-plugin/plugin.json CHANGELOG.md RELEASE-INFO.txt \
  README.md catalog.json docs/index.html docs/packs.html \
  docs/products/website/01-jgs-se-knowledge-packs.yaml docs/products/website/catalog.yaml \
  docs/capability-pack-map.json docs/capability-map-CONTRACT.md docs/capability-pack-map.md

# Annotated tag
git tag -a v1.19.1 -m "v1.19.1: cleanup + tooling + deferred items visible"

# Push + GitHub Release
git push origin main --follow-tags
gh release create v1.19.1 --title "v1.19.1 — Cleanup + Tooling" --notes-file /tmp/v1.19.1-notes.md
```
**Source:** `13-02-PLAN.md:33-75`

### Pattern 4: Dual-Gate Validation (Phase 13)
**What:** Single `check_release.py` invocation runs both catalog gate and map gate (map gate imported). No separate CI step.
**When to use:** Before every release commit.
**Example:**
```bash
python tooling/check_release.py
python tooling/check_capability_map.py
# Both must PASS before release commit
```
**Source:** `tooling/check_release.py:215-222` (map gate import)

### Pattern 5: Post-Tag Records Commit (Phase 9/13)
**What:** Separate commit after tag ticks REL boxes, records SHA/tag/URL in STATE + MILESTONES, ticks ROADMAP Phase, lists Plans.
**When to use:** After every v1.x.0 / v1.x.1 tag + GitHub Release.
**Example:**
```bash
git commit -m "docs(18): tick REL-20-01/02, record v1.19.1 shipped state" \
  .planning/STATE.md .planning/MILESTONES.md .planning/ROADMAP.md .planning/REQUIREMENTS.md
```
**Source:** `13-02-PLAN.md:44-51`

## Anti-Patterns

### Anti-Pattern 1: Lightweight Tag
**What:** `git tag v1.19.1` (no -a) creates lightweight tag.
**Why bad:** REL-20-02 requires annotated tag for tamper-evidence. GitHub Release will fail or show incorrect tag type.
**Fix:** Always use `git tag -a v1.19.1 -m "..."`.

### Anti-Pattern 2: git add -A on Release Commit
**What:** `git add -A` stages everything including master_flow_state.json, research artifacts, /tmp files.
**Why bad:** Release commit must be explicit paths only. Artifacts pollute the tagged commit.
**Fix:** List exact 11 surfaces + map files in git commit command.

### Anti-Pattern 3: Em Dash in CHANGELOG Body
**What:** Using — in CHANGELOG prose.
**Why bad:** Zero em dash rule from Phase 13 locked decisions.
**Fix:** Use colon or rephrase. Em dash allowed only in gh release title.

### Anti-Pattern 4: .planning Records in Tagged Commit
**What:** Including STATE.md / MILESTONES.md / ROADMAP.md / REQUIREMENTS.md in the release commit.
**Why bad:** .planning commit must come after tag. Tagging a commit that includes future-dated records breaks the audit trail.
**Fix:** Two commits: release commit (content only) → tag → .planning commit (records only).

## Edge Cases

### Edge Case 1: gh Release Notes Mismatch
**Symptom:** GitHub Release body differs from CHANGELOG [1.19.1] entry.
**Cause:** Manual notes editing or wrong --notes-file path.
**Fix:** Copy CHANGELOG body to /tmp file, then `gh release create --notes-file /tmp/v1.19.1-notes.md`.

### Edge Case 2: Push Blocked by Branch Protection
**Symptom:** `git push origin main --follow-tags` fails with protection error.
**Cause:** Branch protection enforcement enabled since Phase 13.
**Fix:** Human gate required. Document in 18-02-PLAN.md as checkpoint:human-verify.

### Edge Case 3: map_version Already at 1.19.1
**Symptom:** capability-pack-map.json map_version is already 1.19.1 before 18-01.
**Cause:** Phase 12 or 16 bumped it accidentally.
**Fix:** Verify live state; if already correct, 18-01 Task 1 skips the bump (idempotent sed still works).

## Verification Commands

```bash
# Pre-release
python tooling/check_release.py
python tooling/check_capability_map.py

# Post-tag
git cat-file -t $(git rev-parse v1.19.1)  # must be "tag"
git ls-remote --tags origin | grep v1.19.1
gh release view v1.19.1
gh release view v1.19.1 --json body | jq -r '.body' | head -20  # matches CHANGELOG
```

## Sources

- `13-01-PLAN.md` - Surface bump + gate tasks
- `13-02-PLAN.md` - Tag + release + records commit
- `13-RESEARCH.md` - Locked decisions on CHANGELOG shape, em dash rule, map_version bump
- Live verification: `git tag -l v1.19*`, `gh auth status`, gate scripts

**Research date:** 2026-08-20

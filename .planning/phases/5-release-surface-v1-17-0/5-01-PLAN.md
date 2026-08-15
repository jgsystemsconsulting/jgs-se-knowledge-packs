---
phase: 5-release-surface-v1-17-0
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - .claude-plugin/plugin.json
  - .cursor-plugin/plugin.json
  - CHANGELOG.md
  - RELEASE-INFO.txt
  - README.md
  - docs/index.html
  - docs/packs.html
  - docs/products/website/01-jgs-se-knowledge-packs.yaml
  - docs/products/website/catalog.yaml
  - docs/PACK-SPEC.md
  - .planning/STATE.md
  - .planning/MILESTONES.md
  - .planning/ROADMAP.md
autonomous: true
requirements: [REL-01, REL-02]
estimate:
  tokens: 45000
  raw_tokens: 30000
  tasks: 7
  confidence: low

must_haves:
  truths:
    - "python tooling/check_release.py prints RELEASE CHECK: PASS with catalog basis 54 packs / 56 directory basis"
    - "grep '1\\.16\\.3' over tracked release surfaces returns zero hits outside CHANGELOG.md history entries and .planning/"
    - "docs/packs.html is byte-identical to a fresh python tooling/gen_packs_page.py run"
    - "Annotated tag v1.17.0 exists on origin/main and a GitHub Release v1.17.0 exists"
    - "The release commit is the last content commit on main before the tag"
  artifacts:
    - "CHANGELOG.md with '## [1.17.0]: <date>' entry per research §2 draft"
    - "docs/PACK-SPEC.md body-order list starting with '## When to use' + '**Prerequisites:**' item"
    - "README.md doe-413-3b series-framing prose line"
  key_links:
    - "RELEASE-INFO.txt Version -> gen_packs_page.py regeneration -> docs/packs.html REV span (gate §5c)"
    - "CHANGELOG entry -> gh release create --notes-file (release notes body)"
---

<objective>
Synchronize all 11 version surfaces to 1.17.0, land the CHANGELOG/PACK-SPEC/README
content updates, validate the full release gate, then tag and publish v1.17.0 and
record the shipped state.

Purpose: REL-01 (release surface in sync, gate PASS at 54/56 basis) and REL-02
(v1.17.0 tagged and released) — the final phase of the v1.17.0 milestone.
Output: release commit + annotated tag v1.17.0 + GitHub Release + updated
.planning records.
</objective>

<execution_context>
@$HOME/.zcode/gsd-core/workflows/execute-plan.md
@$HOME/.zcode/gsd-core/templates/summary.md
</execution_context>

<context>
@.planning/ROADMAP.md
@.planning/phases/5-release-surface-v1-17-0/5-RESEARCH.md
@CHANGELOG.md
@.claude-plugin/plugin.json
@RELEASE-INFO.txt
@docs/PACK-SPEC.md
</context>

<claim_verification>
| claim | command | observed | status |
|---|---|---|---|
| 11 version surfaces carry 1.16.3 (research §1 table) | grep -rn "1\.16\.3" (md/json/txt/html/yaml, excl .planning, CHANGELOG, packs/) | all 11 surfaces present: plugin.json:4, cursor plugin.json:5, RELEASE-INFO.txt:3-4, README.md:10/58/207, docs/index.html:110/226, docs/packs.html:86, website yaml x2 | VERIFIED |
| gate reads exactly 3 authorities | 5-RESEARCH.md §1 citing tooling/check_release.py lines 102-116 | research cites lines; plugin.json/CHANGELOG/RELEASE-INFO all at 1.16.3 consistent | VERIFIED |
| packs.html is generated from RELEASE-INFO.txt | 5-RESEARCH.md §1 row 9 (gen_packs_page.py:version()) | tooling/gen_packs_page.py exists; research §4 sequence includes regeneration step | VERIFIED |
| tags v1.16.2/v1.16.3 are annotated with one-line messages | git tag -l -n1 v1.16.3 v1.16.2 | both annotated, one-line `vX.Y.Z: summary` style | VERIFIED |
| PACK-SPEC.md lacks any 'When to use' body-order item | grep -n "When to use\|RR-S-13" docs/PACK-SPEC.md | zero matches — addendum needed per research §3.1 | VERIFIED |
| README has no doe-413 framing line yet | grep -n "doe-413" README.md | zero matches — line must be added near pack list | VERIFIED |
| CHANGELOG first entry is `## [1.16.3]: 2026-06-26` | grep -n "## \[1.16" CHANGELOG.md | line 12 — new 1.17.0 entry goes above it | VERIFIED |
| untracked user files live in docs/ (never broad-add) | git status --short | 3 untracked: docs/ROLE-AGENTS-REQUIREMENTS-V2.md, docs/capability-pack-map.{md,json} | VERIFIED |
| repo publishes GitHub Releases (gh release create required) | 5-RESEARCH.md §4 (gh release list showed v1.16.0-1.16.3) | research evidence; executor re-confirms via `gh release view v1.16.3` before creating notes | VERIFIED |
| exact chapter counts per pack | 5-RESEARCH.md §2 note ("to be confirmed from each SKILLS.md") | counts must be read from packs' SKILLS.md rows during execution | ASSUMPTION — Task 2 verifies each count against SKILLS.md |
</claim_verification>

<tasks>

<task type="auto">
  <name>Task 1: Version bump — all 11 surfaces</name>
  <files>.claude-plugin/plugin.json, RELEASE-INFO.txt, .cursor-plugin/plugin.json, README.md, docs/index.html, docs/products/website/01-jgs-se-knowledge-packs.yaml, docs/products/website/catalog.yaml, docs/packs.html</files>
  <action>Bump 1.16.3 → 1.17.0 on all 11 surfaces per 5-RESEARCH.md §1 table. Order matters: edit RELEASE-INFO.txt FIRST (Version: 1.17.0, Tag: v1.17.0, Staged: release timestamp in 2026-08-15T…Z form), then run `python tooling/gen_packs_page.py` to regenerate docs/packs.html (never hand-edit packs.html — gate §5c fails on drift), then hand-edit the rest: .claude-plugin/plugin.json line 4, .cursor-plugin/plugin.json line 5, README.md lines 10 (badge `version-1.17.0-green` + alt text) / 58 / 207, docs/index.html lines 110 and 226 (both REV spans), the two website YAMLs (lines 15 / 13). install.py/.sh/.ps1 and marketplace.json carry no version field — do not touch. Do NOT touch CHANGELOG.md here (Task 2 owns its heading).</action>
  <verify>grep -rn "1\.16\.3" --include="*.json" --include="*.md" --include="*.txt" --include="*.html" --include="*.yaml" . | grep -v ".planning/" | grep -v "packs/" returns ONLY the CHANGELOG.md history entries `## [1.16.3]` region (lines ~12-19); all other hits are zero. Then `python tooling/gen_packs_page.py && git diff --stat docs/packs.html` shows no further change (byte-identical regeneration).</verify>
  <done>All 11 surfaces read 1.17.0 (or 1.17.0-equivalent badge/tag strings); packs.html regenerated, idempotent on re-run; no 1.16.3 string remains on release surfaces outside CHANGELOG history.</done>
</task>

<task type="auto">
  <name>Task 2: CHANGELOG v1.17.0 entry per research draft</name>
  <files>CHANGELOG.md</files>
  <action>Insert the `## [1.17.0]: 2026-08-15` entry above `## [1.16.3]: 2026-06-26` (line 12) using the draft in 5-RESEARCH.md §2 verbatim in structure (### Added with the 8 pack one-liners + SOURCE-VETTING.md + PACK-SPEC.md items, "Catalogue now 54 packs (+2 signposts)." line, ### Fixed with the cursor-manifest item, ### Changed with the 4 items). Before writing, read each of the 8 new packs' SKILLS.md rows and correct the chapter counts in the one-liners if any pack is not 8 ch (research flagged counts as unconfirmed). HARD CONSTRAINTS: no em dashes anywhere in the entry; no URLs / source-host links in the entry (check_release link-policy scans CHANGELOG.md); keep publisher names bare. Also update any link-reference definitions at the bottom of CHANGELOG.md only if house style requires them for the new heading (it does not — versions are plain headings, verify against 1.16.3 entry).</action>
  <verify>grep -c "## \[1.17.0\]" CHANGELOG.md == 1; python tooling/check_release.py section 4 (version single-source) passes as part of a full run: `python tooling/check_release.py` prints RELEASE CHECK: PASS. Em-dash gate: grep for the em-dash character in the new entry returns zero.</verify>
  <done>CHANGELOG first version heading is `## [1.17.0]: 2026-08-15`; chapter counts match SKILLS.md rows; entry is em-dash-free and URL-free; full gate PASS.</done>
</task>

<task type="auto">
  <name>Task 3: PACK-SPEC addendum — When to use + Prerequisites</name>
  <files>docs/PACK-SPEC.md</files>
  <action>Per 5-RESEARCH.md §3.1 (MI-02 / MN-08, RR-S-13): in the SKILL.md rules body-order ordered list (starts at line ~31 with `## How to Use This Skill`), add a new first item `## When to use` immediately followed by a `**Prerequisites:**` line naming what the reader should already have/know, noting it is enforced by tooling/check_release.py — exact wording per the research §3.1 markdown block. Keep the existing list items and their order unchanged below the new item. This is a documentation sync only; no tooling change.</action>
  <verify>grep -n "When to use" docs/PACK-SPEC.md returns >= 1 hit inside the body-order list; `python tooling/check_release.py` still prints RELEASE CHECK: PASS (PACK-SPEC is not gated, but confirms no collateral damage).</verify>
  <done>PACK-SPEC body-order list starts with the When to use + Prerequisites item per research §3.1; rest of the list untouched.</done>
</task>

<task type="auto">
  <name>Task 4: README doe-413-3b series-framing line (no rename)</name>
  <files>README.md</files>
  <action>Per 5-RESEARCH.md §3.2 (MI-03): add ONE prose line to README near the DOE pack mention / pack list stating that the `doe-413-3b` slug is retained for continuity but the pack tracks the current DOE O 413.3 series edition (O 413.3C, which cancels O 413.3B Chg 7); no slug rename in v1.17.0. Do NOT rename the pack, catalog entry, or any manifest. The v1.18+ rename-to-`doe-o-413-3` deferral is recorded in .planning only (Task 7), NOT in README. Em-dash-free line.</action>
  <verify>grep -n "doe-413-3b" README.md returns the framing line; grep for the em-dash character in that line is zero; catalog.json slug unchanged (grep -c '"doe-413-3b"' catalog.json or the catalog file path still 1).</verify>
  <done>README carries the series-framing line; slug untouched everywhere; deferral noted only in .planning records.</done>
</task>

<task type="auto">
  <name>Task 5: Final validation — gate PASS + packs.html byte-identical</name>
  <files></files>
  <precondition>Tasks 1-4 edits complete and staged nowhere yet; working tree contains ONLY the intended release files as modifications (plus known untracked user files in docs/ which must remain untracked).</precondition>
  <action>Run the full validation battery per 5-RESEARCH.md §4: (1) `python tooling/gen_packs_page.py` then confirm docs/packs.html has zero diff (byte-identical); (2) `python tooling/check_release.py` — must print RELEASE CHECK: PASS and the gate's catalog basis must read 54 packs / 56 directory basis (48 + 8 new, minus 2 signposts) per ROADMAP Phase 5 SC1; (3) `python tooling/validate_pack.py` spot-check two of the new packs (e.g. nist-800-171, doe-413-3b); (4) re-run check_release one final time immediately before commit (OneDrive sync-lag risk, research §5.6). If any step fails, STOP and fix before proceeding — do not tag on a red gate.</action>
  <verify>python tooling/check_release.py exits 0 with "RELEASE CHECK: PASS" and 54/56 basis; gen_packs_page.py re-run leaves docs/packs.html with `git diff --stat docs/packs.html` empty.</verify>
  <done>Gate PASS at 54 packs / 56 directory basis; packs.html byte-identical; validate_pack spot-checks green; validation run is the last action before the release commit.</done>
</task>

<task type="auto" tdd="false">
  <name>Task 6: Release commit, annotated tag, push, GitHub Release</name>
  <files>.claude-plugin/plugin.json, .cursor-plugin/plugin.json, CHANGELOG.md, RELEASE-INFO.txt, README.md, docs/index.html, docs/packs.html, docs/products/website/01-jgs-se-knowledge-packs.yaml, docs/products/website/catalog.yaml, docs/PACK-SPEC.md</files>
  <precondition>Task 5 gate PASS just re-confirmed; `gh auth status` succeeds.</precondition>
  <action>Execute the release sequence per 5-RESEARCH.md §4. Stage with EXPLICIT paths only — list every modified file by name; NEVER `git add docs/`, `git add .`, or `git add -A` (three untracked user files in docs/ — ROLE-AGENTS-REQUIREMENTS-V2.md, capability-pack-map.md, capability-pack-map.json — must not be committed; verify with `git status --short` that nothing untracked is staged). Commit message: `release(v1.17.0): 8 Tier-1 public-domain packs (54 +2 signposts)` with a body covering: the 8 packs, cursor-manifest fix, PACK-SPEC addendum, ruled-out register, GSD onboarding; gate PASS. This must be the LAST content commit on main. Then: annotated tag matching existing style (one-line message, em dash as in v1.16.3 style): `git tag -a v1.17.0 -m "v1.17.0 — 8 Tier-1 public-domain packs (54 +2 signposts)"`. Push `git push origin main --follow-tags`. Then check `gh release view v1.16.3` for the existing notes format, and `gh release create v1.17.0 --title "v1.17.0 — 8 Tier-1 public-domain packs" --notes-file <tmp file containing the CHANGELOG 1.17.0 entry body>`. REL-02 is NOT done until `git ls-remote --tags origin v1.17.0` and `gh release view v1.17.0` both succeed.</action>
  <reversibility rating="costly">Publishing a tag + GitHub Release is hard to retract, but it is pre-approved by the phase charter (REL-02 mandates tag + release); everything before it is reversible edits, so no decision checkpoint.</reversibility>
  <verify>git ls-remote --tags origin | grep v1.17.0 returns the tag ref; gh release view v1.17.0 --json name,tagName succeeds; git log --oneline -1 shows the release commit as HEAD of origin/main.</verify>
  <done>Release commit is the last content commit on main; annotated tag v1.17.0 pushed; GitHub Release v1.17.0 published with notes from the CHANGELOG entry; no untracked docs/ user files in the commit.</done>
</task>

<task type="auto">
  <name>Task 7: Post-release records — STATE, MILESTONES, ROADMAP</name>
  <files>.planning/STATE.md, .planning/MILESTONES.md, .planning/ROADMAP.md</files>
  <action>After the tag exists (Task 6 done): (1) STATE.md — record v1.17.0 shipped, including the deferred decision: rename `doe-413-3b` to `doe-o-413-3` with catalog alias is DEFERRED to v1.18+ (per 5-RESEARCH.md §3.2, so it survives into v1.18 planning), and the accepted residual: catalog licence-string sweep skipped (§3.3), user-owned stale capability-pack-map files flagged not committed (§3.4); (2) MILESTONES.md — add v1.17.0 shipped record consistent with prior version entries; (3) ROADMAP.md — check the Phase 5 checkbox (line 13) and set Phase 5 `**Plans**: 1` with the plan listed. Commit these .planning files separately (docs/chore commit, explicit paths — they are intentionally not part of the release commit).</action>
  <verify>grep -n "v1.17.0" .planning/STATE.md and .planning/MILESTONES.md return the shipped records; grep -n "Phase 5" .planning/ROADMAP.md line 13 shows `- [x]`; the release commit remains the last CONTENT commit (planning-docs commit after it touches only .planning/).</verify>
  <done>v1.17.0 shipped record with deferral + residuals in STATE.md; MILESTONES.md updated; ROADMAP Phase 5 checked; .planning-only follow-up commit does not disturb the released tree.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| repo → public GitHub | Tag + GitHub Release are the public release act; errors are visible and hard to retract |
| working tree → release commit | Untracked user files in docs/ must not cross into the release commit |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-5-01 | Tampering | Release commit staging | high | mitigate | Explicit-path-only `git add`; `git status --short` audit before commit; never `git add docs/`/`-A` (3 untracked user files) |
| T-5-02 | Repudiation | Tag/release provenance | medium | mitigate | Annotated tag (not lightweight) with one-line message; release commit convention matches 6ede444 |
| T-5-03 | Tampering | OneDrive sync lag on Windows | medium | mitigate | Re-run check_release.py immediately before tagging (research §5.6) |
| T-5-04 | Information disclosure | CHANGELOG link policy | low | mitigate | No URLs/em dashes in the new entry; gate scans CHANGELOG for source-host links |
| T-5-05 | DoS (of release) | Public release on red gate | high | mitigate | Task 5 hard-stops on any non-PASS; tag only after final green run |
</threat_model>

<verification>
1. `python tooling/check_release.py` → RELEASE CHECK: PASS, catalog basis 54/56 (REL-01).
2. `grep -rn "1\.16\.3"` release surfaces → only CHANGELOG history entries remain.
3. `git ls-remote --tags origin | grep v1.17.0` + `gh release view v1.17.0` → both exist (REL-02).
4. Release commit is last content commit; `git show --stat HEAD~0` contains no docs/ untracked user files.
</verification>

<success_criteria>
- REL-01: check_release.py PASS at 54 packs / 56 directory basis; all 11 surfaces at 1.17.0.
- REL-02: annotated tag v1.17.0 pushed; GitHub Release v1.17.0 published with CHANGELOG-derived notes.
- CHANGELOG v1.17.0 entry accurate (SKILLS.md-verified chapter counts), em-dash/URL free.
- PACK-SPEC When-to-use/Prerequisites addendum and README doe-413-3b framing line landed.
- v1.18 deferrals and accepted residuals recorded in .planning; ROADMAP Phase 5 checked.
</success_criteria>

<output>
Create `.planning/phases/5-release-surface-v1-17-0/5-01-SUMMARY.md` when done
</output>


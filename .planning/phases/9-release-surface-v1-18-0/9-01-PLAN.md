---
phase: 9-release-surface-v1-18-0
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
  - docs/capability-map-CONTRACT.md
  - docs/SOURCE-VETTING.md
  - .planning/STATE.md
  - .planning/MILESTONES.md
  - .planning/ROADMAP.md
autonomous: true
requirements: [REL-1x-01, REL-1x-02]
estimate:
  tokens: 55000
  raw_tokens: 35000
  tasks: 6
  confidence: low

must_haves:
  truths:
    - "python tooling/check_release.py exits 0 printing RELEASE CHECK: PASS; independently python -c \"import json;print(len(json.load(open('catalog.json'))['packs']))\" prints 61 and `ls packs | wc -l` prints 63"
    - "python tooling/check_capability_map.py exits 0 (schema_version 2, map_version 1.18.0 — now matching RELEASE-INFO 1.18.0, closing IN-04)"
    - "grep -rn '1\\.17\\.0' (excl .planning, .git, sources) returns only CHANGELOG history plus the 5 known-historical doc lines (capability-map-CONTRACT.md:54, capability-pack-map.md:16, SOURCE-VETTING.md:93/144/149)"
    - "docs/packs.html is byte-identical to a fresh python tooling/gen_packs_page.py run"
    - "Annotated tag v1.18.0 exists on origin/main and a GitHub Release v1.18.0 exists with CHANGELOG-derived notes"
    - "The release commit is the last content commit on main before the tag"
  artifacts:
    - "CHANGELOG.md with '## [1.18.0]: <date>' entry LEADING with the doe-o-413-3 rename note"
    - "docs/capability-map-CONTRACT.md §4 with cluster-name replacing the numeric 'cluster 30' reference (IN-01)"
    - "docs/SOURCE-VETTING.md:130 OUSW typo corrected to OUSD(R&E)"
  key_links:
    - "RELEASE-INFO.txt Version 1.18.0 -> gen_packs_page.py regeneration -> docs/packs.html REV span; RELEASE-INFO 1.18.0 == capability-pack-map.json map_version 1.18.0 (IN-04 reconciliation)"
    - "CHANGELOG 1.18.0 entry -> gh release create --notes-file (release notes body)"
---

<objective>
Synchronize all 11 version surfaces to 1.18.0, land the CHANGELOG v1.18.0 entry
(rename note first) plus the IN-01/IN-04/OUSD carry-forwards, validate the full
release gate at the 61/63 basis, then tag and publish v1.18.0 and record the
shipped state with the v1.19 backlog.

Purpose: REL-1x-01 (surfaces synchronized, gates PASS) and REL-1x-02 (v1.18.0
tagged + released with the mandated CHANGELOG notes) — final phase of the
v1.18.0 milestone. Structure reuses the proven Phase 5 template (5-01-PLAN.md).
Output: release commit + annotated tag v1.18.0 + GitHub Release + updated
.planning records.
</objective>

<execution_context>
@$HOME/.zcode/gsd-core/workflows/execute-plan.md
@$HOME/.zcode/gsd-core/templates/summary.md
</execution_context>

<context>
@.planning/ROADMAP.md
@.planning/phases/5-release-surface-v1-17-0/5-01-PLAN.md
@.planning/phases/7-gap-driven-pack-builds/7-GAP_ANALYSIS.md
@.planning/phases/8-agent-enablement-surface/8-GAP_ANALYSIS.md
@CHANGELOG.md
@RELEASE-INFO.txt
@docs/capability-map-CONTRACT.md
</context>

<claim_verification>
| claim | command | observed | status |
|---|---|---|---|
| 11 version surfaces carry 1.17.0 | grep -rn "1\.17\.0" excl .planning/.git/sources/CHANGELOG | plugin.json:4, cursor plugin.json:5, RELEASE-INFO.txt:3-4, README.md:10/58/224, docs/index.html:110/226, docs/packs.html:86, catalog.yaml:13, 01-jgs...yaml:15 | VERIFIED |
| 5 historical 1.17.0 doc refs must survive the bump | same grep, doc files | capability-map-CONTRACT.md:54 ("pre-envelope (v1) map corresponds to release `1.17.0`" — true history), capability-pack-map.md:16 (map changelog), SOURCE-VETTING.md:93/144/149 (v1.17.0 candidate sections) | VERIFIED |
| chapter counts per pack (live PACK.yaml) | grep "chapters:" packs/<slug>/PACK.yaml | dote-te-guidebook=8, faa-std-025=6, federal-bca=6, dafman-63-119=7, mil-std-881f=7, mil-std-40051=8, dod-vva-rpg=10 — never uniform | VERIFIED |
| catalog/dirs/cursor basis | python len(catalog packs); ls packs \| wc -l; cursor plugin skills len | 61 / 63 / 62 | VERIFIED |
| map envelope | python on docs/capability-pack-map.json | schema_version 2, map_version "1.18.0", 32 clusters, 628 chapter entries; check_capability_map.py exit 0 | VERIFIED |
| gates currently green | python tooling/check_release.py; check_capability_map.py | both exit 0 pre-phase | VERIFIED |
| doe-o-413-3 rename already shipped with alias | grep slug catalog.json | "slug": "doe-o-413-3" with alias "doe-413-3b" (rename landed post-tag in c9d5e7e) | VERIFIED |
| 1.17.0 entry's index.html registration claim to be corrected | grep -n "index.html" CHANGELOG.md | CHANGELOG.md:58 lists docs/index.html among "Registered the 8 packs on every surface" — index.html is a version surface, not a registration surface (REL-1x-02 wording fix) | VERIFIED |
| CI/local .planning skip already in 1.17.0 entry | sed CHANGELOG 1.17.0 Changed | "Release-gate and CI link-policy scans skip `.planning/`" already present — do NOT duplicate in 1.18.0 | VERIFIED |
| OUSD typo residual | grep -n "OUSW" docs/SOURCE-VETTING.md | line 130 only (immutable phase records in .planning excluded) | VERIFIED |
| CONTRACT numeric cluster ref (IN-01) | grep -n "cluster 30" docs/capability-map-CONTRACT.md | line 73 in §4 Refresh path; cluster 30's name is "Standards, Tailoring & Process Models" (capability-pack-map.md:748) | VERIFIED |
| ROLE-AGENTS doc now tracked | git ls-files docs/ROLE-AGENTS-REQUIREMENTS-V2.md | tracked (05eb9ad) — no untracked docs/ strays expected; verify git status before staging | VERIFIED |
| tag + release-notes conventions | git tag -l -n3 v1.17.0; gh release view v1.17.0 | annotated, colon style "v1.17.0: 8 Tier-1 ..."; release notes body = CHANGELOG entry body, title "vX.Y.Z — summary" | VERIFIED |
</claim_verification>

<tasks>

<task type="auto">
  <name>Task 1: Version bump — all 11 surfaces, 1.17.0 to 1.18.0</name>
  <files>.claude-plugin/plugin.json, RELEASE-INFO.txt, .cursor-plugin/plugin.json, README.md, docs/index.html, docs/products/website/01-jgs-se-knowledge-packs.yaml, docs/products/website/catalog.yaml, docs/packs.html</files>
  <action>Bump 1.17.0 → 1.18.0 on all 11 surfaces. Order matters: edit RELEASE-INFO.txt FIRST (Version: 1.18.0, Tag: v1.18.0, Staged: real execution timestamp in 2026-08T…Z form — use the actual date/time, not a hardcoded value), then run `python tooling/gen_packs_page.py` to regenerate docs/packs.html (never hand-edit packs.html — drift fails the gate), then hand-edit the rest: .claude-plugin/plugin.json line 4, .cursor-plugin/plugin.json line 5, README.md lines 10 (badge `version-1.18.0-green` + alt text) / 58 / 224 ("Current: 1.18.0"), docs/index.html lines 110 and 226 (both REV spans), the two website YAMLs (catalog.yaml:13, 01-jgs-se-knowledge-packs.yaml:15). Do NOT touch CHANGELOG.md here (Task 2 owns its heading). IN-04 closes by this bump: docs/capability-pack-map.json map_version is already "1.18.0", so RELEASE-INFO 1.18.0 reconciles it — verify but do not edit the map. Do NOT touch the 5 historical 1.17.0 doc references (capability-map-CONTRACT.md:54, capability-pack-map.md:16, SOURCE-VETTING.md:93/144/149) — they record v1.17.0 history and must remain.</action>
  <verify>grep -rn "1\.17\.0" --exclude-dir=.planning --exclude-dir=.git --exclude-dir=sources . returns ONLY: CHANGELOG.md history (the `## [1.17.0]` region) plus exactly docs/capability-map-CONTRACT.md:54, docs/capability-pack-map.md:16, docs/SOURCE-VETTING.md:93/144/149. Then `python tooling/gen_packs_page.py && git diff --stat docs/packs.html` shows no further change (byte-identical regeneration). grep -n '"map_version"' docs/capability-pack-map.json shows "1.18.0" and grep -n "Version:" RELEASE-INFO.txt shows 1.18.0 (IN-04 reconciled).</verify>
  <done>All 11 surfaces read 1.18.0 (or 1.18.0-equivalent badge/tag strings); packs.html regenerated and idempotent; the only remaining 1.17.0 strings are CHANGELOG history plus the 5 known-historical doc lines; RELEASE-INFO version equals map_version (both 1.18.0).</done>
</task>

<task type="auto">
  <name>Task 2: CHANGELOG v1.18.0 entry — rename note leads</name>
  <files>CHANGELOG.md</files>
  <action>Insert the `## [1.18.0]: <execution date>` entry above `## [1.17.0]: 2026-08-15` (line 12) in house format (Keep-a-Changelog, three level-3 sections). STRUCTURE — first line under the heading is the rename note as a plain paragraph: the `doe-413-3b` pack was renamed to `doe-o-413-3` (same content, catalog alias retained), so downstream references update automatically; this note LEADS because the rename is the breaking-adjacent change consumers must see first (per REL-1x-02 and 7-GAP_ANALYSIS carry-forward). Then: ### Added — the 7 pack one-liners in the bold-slug `(N ch): description — Tier 1` style of the 1.17.0 entry, chapter counts sourced live from each packs/<slug>/PACK.yaml `chapters:` field (verified 2026-08-14: dote-te-guidebook=8, faa-std-025=6, federal-bca=6, dafman-63-119=7, mil-std-881f=7, mil-std-40051=8, dod-vva-rpg=10 — re-read each PACK.yaml immediately before writing; the counts are intentionally non-uniform, a uniform value means a copy error); plus `docs/capability-pack-map.{md,json}` v2 (schema_version 2, 32 clusters, 628 chapter entries, map_version tracking the release, enforced by `python tooling/check_capability_map.py`); plus `docs/capability-map-CONTRACT.md` (versioned map contract for the se-agents generator). Close Added with "Catalogue now 61 packs (+2 signposts)." ### Fixed — (1) the v1.17.0 entry's registration-surface list wrongly included docs/index.html, which is a version surface, not a registration surface (REL-1x-02 wording fix); (2) OUSD(R&E) attribution typo in docs/SOURCE-VETTING.md GP-01 row; (3) capability-map gate hardenings (duplicate names, strict schema, path guard); (4) Cursor manifest gained the 7 new packs (62 skills total) in the post-tag v1.17.x commit e00ac7d — surfaced here so the release notes are complete. ### Changed — registration of the 7 packs on every registered surface (catalog.json, SKILLS.md, docs/packs.html, NOTICE, README, Cursor manifest). HARD CONSTRAINTS: no em dashes anywhere in the entry; no URLs / source-host links (check_release link-policy scans CHANGELOG.md); keep publisher names bare. Do NOT restate the `.planning/` CI/local scan skip — it is already in the 1.17.0 entry's Changed section (verified); duplication would be an error. Consumer-facing caveats (per 7-GAP_ANALYSIS R1/R2): fold into the relevant pack one-liners — dod-vva-rpg notes chapter PDFs carry internal dates circa 2011 inside an undated web-edition container; faa-std-025 notes it is built from the Rev F mirror where ROSAP hosts canonical Rev E; mil-std-40051 notes some PDF page counters report 1168 against the metadata authority of 584.</action>
  <verify>grep -c "## \[1.18.0\]" CHANGELOG.md == 1 and it appears above `## [1.17.0]`. For each of the 7 packs the one-liner's "(N ch)" equals the live `grep "chapters:" packs/<slug>/PACK.yaml` value (8/6/6/7/7/8/10). The rename paragraph precedes the first `###` heading. grep for the em-dash character within the new entry returns zero; grep for "http" within the new entry returns zero. `python tooling/check_release.py` prints RELEASE CHECK: PASS.</verify>
  <done>CHANGELOG first version heading is `## [1.18.0]: <date>`; rename note leads the entry; chapter counts equal live PACK.yaml values; caveats present on vva/faa/40051 one-liners; entry is em-dash-free and URL-free; no duplication of the 1.17.0 scan-skip item; full gate PASS.</done>
</task>

<task type="auto">
  <name>Task 3: Carry-forward doc fixes — CONTRACT cluster-name (IN-01), OUSD typo</name>
  <files>docs/capability-map-CONTRACT.md, docs/SOURCE-VETTING.md</files>
  <action>(1) IN-01: in docs/capability-map-CONTRACT.md §4 Refresh path (line ~73), the parenthetical "process definitions → cluster 30" uses a numeric cluster reference while the rest of the CONTRACT speaks in names; replace with the cluster's name so the reference survives renumbering: "process definitions → the Standards, Tailoring & Process Models cluster" (name verified against docs/capability-pack-map.md:748, cluster 30's heading). Change only that clause; the surrounding numbered steps stay untouched. (2) OUSD typo: docs/SOURCE-VETTING.md line 130 GP-01 row reads "OUSW(R&E)" — correct to "OUSD(R&E)" matching the fixed attribution surfaces (e4699c4). Occurrences of OUSW inside .planning/ are immutable phase records — do not edit them. Both files are docs-only; no gate input changes.</action>
  <verify>grep -n "cluster 30" docs/capability-map-CONTRACT.md returns zero; grep -n "Standards, Tailoring" docs/capability-map-CONTRACT.md returns >= 1; grep -n "OUSW" docs/SOURCE-VETTING.md returns zero; `python tooling/check_capability_map.py` and `python tooling/check_release.py` still exit 0.</verify>
  <done>CONTRACT §4 references the cluster by name with no numeric ref remaining (IN-01 closed); SOURCE-VETTING.md has no OUSW occurrences; both gates stay green.</done>
</task>

<task type="auto">
  <name>Task 4: Final validation — both gates + residual-version sweep</name>
  <files></files>
  <precondition>Tasks 1-3 edits complete; working tree contains ONLY the intended release files as modifications; `git status --short` shows no untracked files outside .planning/ (docs/ROLE-AGENTS-REQUIREMENTS-V2.md is tracked since 05eb9ad — if any new untracked stray appears, STOP and surface it rather than staging broadly).</precondition>
  <action>Run the full validation battery: (1) `python tooling/gen_packs_page.py` then confirm `git diff --stat docs/packs.html` is empty (byte-identical); (2) `python tooling/check_release.py` — must exit 0 printing RELEASE CHECK: PASS; independently measure the basis per ROADMAP Phase 9 SC1: `python -c "import json;print(len(json.load(open('catalog.json'))['packs']))"` prints 61 and `ls packs | wc -l` prints 63; (3) `python tooling/check_capability_map.py` — must exit 0 (schema/envelope, staleness vs packs/, thresholds); (4) `python tooling/validate_pack.py` spot-check two packs touched this cycle (e.g. dod-vva-rpg, mil-std-40051); (5) residual-version sweep: `grep -rn "1\.17\.0" --exclude-dir=.planning --exclude-dir=.git --exclude-dir=sources .` returns only CHANGELOG history + the 5 whitelisted historical doc lines (capability-map-CONTRACT.md:54, capability-pack-map.md:16, SOURCE-VETTING.md x3); (6) re-run check_release one final time immediately before commit (OneDrive sync-lag risk, per Phase 5 experience). If any step fails, STOP and fix before proceeding — do not tag on a red gate.</action>
  <verify>check_release.py exits 0 PASS; check_capability_map.py exits 0; catalog.json packs == 61; ls packs | wc -l == 63; gen_packs_page.py re-run leaves docs/packs.html with empty git diff; the 1.17.0 sweep returns only the whitelisted hits.</verify>
  <done>Both gates green at the 61 catalog / 63 dirs basis; packs.html byte-identical; version sweep clean except whitelisted history; validation is the last action before the release commit.</done>
</task>

<task type="auto">
  <name>Task 5: Release commit, annotated tag, push, GitHub Release</name>
  <files>.claude-plugin/plugin.json, .cursor-plugin/plugin.json, CHANGELOG.md, RELEASE-INFO.txt, README.md, docs/index.html, docs/packs.html, docs/products/website/01-jgs-se-knowledge-packs.yaml, docs/products/website/catalog.yaml, docs/capability-map-CONTRACT.md, docs/SOURCE-VETTING.md</files>
  <precondition>Task 4 gates PASS just re-confirmed; `gh auth status` succeeds.</precondition>
  <action>Execute the release sequence per the Phase 5 template. Stage with EXPLICIT paths only — list every modified file by name; never stage by directory or `-A`/`.`; first run `git status --short` and confirm nothing untracked is staged (docs/ROLE-AGENTS-REQUIREMENTS-V2.md is already tracked; any surprise untracked file is a STOP condition). Commit message: `release(v1.18.0): 7 gap-driven Tier-1 packs (61 +2 signposts), capability map v2` with a body covering the 7 packs, doe-o-413-3 rename (+alias), capability map v2 + CONTRACT + gate, the v1.17.0 wording correction, and gate PASS at 61/63. This must be the LAST content commit on main. Then annotated tag in live repo colon style (copy `git tag -l -n3 v1.17.0` exactly): `git tag -a v1.18.0 -m "v1.18.0: 7 gap-driven Tier-1 packs (61 +2 signposts), capability map v2"`. Push `git push origin main --follow-tags`. Then check `gh release view v1.17.0` for notes format (title "vX.Y.Z — summary" line, body = CHANGELOG entry body) and create `gh release create v1.18.0 --title "v1.18.0 — 7 gap-driven Tier-1 packs + capability map v2" --notes-file <tmp file containing the CHANGELOG 1.18.0 entry body, rename note first>`. REL-1x-02 is NOT done until `git ls-remote --tags origin v1.18.0` and `gh release view v1.18.0` both succeed.</action>
  <reversibility rating="costly">Publishing a tag + GitHub Release is hard to retract, but it is pre-approved by the phase charter (REL-1x-02 mandates tag + release); everything before it is reversible edits, so no decision checkpoint.</reversibility>
  <verify>git ls-remote --tags origin | grep v1.18.0 returns the tag ref; gh release view v1.18.0 --json name,tagName succeeds; gh release view v1.18.0 notes body leads with the doe-o-413-3 rename paragraph; git log --oneline -1 shows the release commit as HEAD of origin/main; git show --stat HEAD contains no untracked strays.</verify>
  <done>Release commit is the last content commit on main; annotated colon-style tag v1.18.0 pushed; GitHub Release v1.18.0 published with CHANGELOG-derived notes leading with the rename note; no stray files in the commit.</done>
</task>

<task type="auto">
  <name>Task 6: Post-release records — STATE, MILESTONES, ROADMAP, v1.19 backlog</name>
  <files>.planning/STATE.md, .planning/MILESTONES.md, .planning/ROADMAP.md</files>
  <action>After the tag exists (Task 5 done): (1) STATE.md — record v1.18.0 shipped (release commit hash, tag, GitHub Release URL) and close the routing items: IN-04 (map_version == RELEASE-INFO == tag at 1.18.0) and IN-01 (CONTRACT cluster-name). Carry the v1.19 backlog explicitly: FUT-04 Army CBA retry; FUT-05 (as recorded at bdc6c9e); IN-02 minimal committed overlap checker; thin-cluster fattening for clusters 3/5/15; optional PACK.yaml note additions and ROSAP Rev E retry per 7-GAP_ANALYSIS R1/R2/R5. (2) MILESTONES.md — convert the "v1.18.0 (in execution …)" section into a shipped record in the v1.17.0 entry's format (prose summary + release commit + tag + release URL bullets). (3) ROADMAP.md — tick the Phase 9 checkbox (line 79) and fill `**Plans**: 1 plan` with `9-01-PLAN.md` listed under Phase 9 Details. Commit these .planning files separately with explicit paths (docs commit, intentionally not part of the release commit).</action>
  <verify>grep -n "v1.18.0" .planning/STATE.md and .planning/MILESTONES.md return the shipped records; grep -n "FUT-04\|FUT-05\|IN-02" .planning/STATE.md return backlog entries; grep -n "Phase 9" .planning/ROADMAP.md line 79 shows `- [x]`; the release commit remains the last CONTENT commit (the follow-up commit touches only .planning/).</verify>
  <done>v1.18.0 shipped record + IN-01/IN-04 closure in STATE.md; MILESTONES shipped entry; ROADMAP Phase 9 checked with plan listed; v1.19 backlog (FUT-04, FUT-05, IN-02, clusters 3/5/15) carried; .planning-only commit does not disturb the released tree.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| repo → public GitHub | Tag + GitHub Release are the public release act; errors are visible and hard to retract |
| working tree → release commit | Untracked strays must not cross into the release commit (explicit-path staging) |
| CHANGELOG → release notes | Notes body ships publicly; wrong chapter counts or a buried rename note mislead consumers |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-9-01 | Tampering | Release commit staging | high | mitigate | Explicit-path-only `git add`; `git status --short` audit before commit; STOP on any surprise untracked file |
| T-9-02 | Repudiation | Tag/release provenance | medium | mitigate | Annotated tag (not lightweight) with colon-style one-line message matching v1.17.0 convention |
| T-9-03 | Tampering | OneDrive sync lag on Windows | medium | mitigate | Re-run check_release.py immediately before the release commit (Task 4 step 6) |
| T-9-04 | Information disclosure | CHANGELOG link policy | low | mitigate | No URLs/em dashes in the new entry; gate scans CHANGELOG for source-host links |
| T-9-05 | DoS (of release) | Public release on red gate | high | mitigate | Task 4 hard-stops on any non-PASS; tag only after final green run |
</threat_model>

<verification>
1. `python tooling/check_release.py` → exit 0, RELEASE CHECK: PASS; independently catalog.json packs == 61, packs/ dirs == 63 (REL-1x-01, SC1).
2. `python tooling/check_capability_map.py` → exit 0; map_version 1.18.0 == RELEASE-INFO 1.18.0 (IN-04 closed).
3. `grep -rn "1\.17\.0"` → only CHANGELOG history + the 5 whitelisted historical doc lines; all 11 surfaces at 1.18.0.
4. `git ls-remote --tags origin | grep v1.18.0` + `gh release view v1.18.0` → both exist; notes lead with the rename note (REL-1x-02, SC2).
5. CHANGELOG 1.18.0 entry contains the v1.17.0 wording correction and the doe-o-413-3 rename note (SC2).
</verification>

<success_criteria>
- REL-1x-01: check_release.py PASS at 61 catalog / 63 dirs; all 11 surfaces version-consistent at 1.18.0; packs.html byte-identical regeneration.
- REL-1x-02: annotated tag v1.18.0 pushed; GitHub Release published with CHANGELOG-derived notes; CHANGELOG entry leads with the doe-o-413-3 rename note and includes the v1.17.0 wording correction.
- Chapter counts in the entry equal live PACK.yaml values (8/6/6/7/7/8/10); vva/faa/40051 currency caveats present.
- IN-01 (CONTRACT cluster-name) and IN-04 (map_version reconciliation) closed; OUSD typo fixed.
- v1.19 backlog carried into STATE; ROADMAP Phase 9 checked.
</success_criteria>

<output>
Create `.planning/phases/9-release-surface-v1-18-0/9-01-SUMMARY.md` when done
</output>

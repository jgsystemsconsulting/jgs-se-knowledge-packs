# Phase 13 Plan Check

**Phase:** 13-release-surface-v1-19-0
**Plans checked:** 2 (`13-01-PLAN.md`, `13-02-PLAN.md`)
**Checked:** 2026-08-17
**Method:** Goal-backward verification against ROADMAP Phase 13 goal + SC-1..SC-2, REQUIREMENTS REL-19-01/02, `13-RESEARCH.md` (recommended shape + user_constraints), `13-PATTERNS.md`, `13-VALIDATION.md`, analog `9-01-PLAN.md`, and live re-measurement of every `claim_verification` current-state row.

**Verdict:** NEEDS_WORK

The two waves will synchronize the 11 analog surfaces + map envelope, close the catalog/README leftovers, land a competency-led CHANGELOG, pass both gates at 63/65, then publish an annotated `v1.19.0` + GitHub Release and record shipped state -- **if** Task 2 automated verify is rewritten. As written, that verify fails on a correct post-edit tree and can induce a README corruption. Fix the two predicates before execute. Coverage of REL-19-01/02 is otherwise complete. Do not treat this as a rewrite or a phase split.

---

## Goal-backward trace

Phase goal: *Catalog/docs/manifests synchronized; v1.19.0 tagged and released*

| Success criterion | Required truth | Covering task | Provably delivered? |
|---|---|---|---|
| SC-1 / REL-19-01 -- both gates PASS at updated catalog/directory basis | check_release.py PASS; check_capability_map.py PASS; catalog 63 / dirs 65 | 13-01 T3 (battery + last check_release re-run); 13-02 T1 re-runs both before tag | **Yes.** Independent 63/65 asserts in T3 action; map block prints first because Phase 12 already wired section 5d. |
| SC-1 / REL-19-01 -- full registration honesty | catalog.json dod-vva-rpg.chapters 10 to 13; README live rows for nasa-std-8719-14 + is-gps-200n; RPG (10 chapters) to (13 chapters) | 13-01 T2 | **Yes in the action.** Thin-register (SKILLS / NOTICE / cursor) already green -- plan correctly does not re-edit those. T2 automated currently **cannot go green** on a correct tree (B1). |
| SC-1 -- 11 surfaces + trio + packs.html regeneration | RELEASE-INFO first then gen_packs_page.py then remaining surfaces 1.19.0; CHANGELOG heading in T2 | 13-01 T1 + T2 | **Yes.** Analog order locked. Trio split after T1 is expected; T3 requires agreement. |
| SC-1 -- map_version tracks the release that publishes the regen | JSON + CONTRACT example envelope to 1.19.0; membership stays 644 | 13-01 T1 | **Yes.** RESEARCH Q1 recommendation implemented. No cluster rewrite. |
| SC-2 / REL-19-02 -- CHANGELOG lists IO-unlocks by competency | IO-01..07 named; slugs are evidence; 7/6/13 live counts; IO-05/06 deferred; IO-07 accept; no em dash; no http in the new entry | 13-01 T2 | **Yes in the draft + hard constraints.** Verify http / live (10 chapters) predicates are wrong (B1). |
| SC-2 / REL-19-02 -- annotated tag + push + GitHub Release | git tag -a; git cat-file -t == tag; git push origin main --follow-tags; gh release create with phase-dir notes; ls-remote + gh release view | 13-02 T1 | **Yes.** Phase 9 analog commands, colon tag, em-dash title, Windows notes path, no /tmp. |
| Post-tag records | STATE SHA/tag/URL + backlog; MILESTONES shipped; ROADMAP Phase 13 ticked + both plan files; REL boxes ticked | 13-02 T2 | **Yes.** Separate .planning commit; tagged tree unchanged. |

Requirements frontmatter: both plans list [REL-19-01, REL-19-02]. 13-01 produces REL-19-01 + the CHANGELOG prerequisite for SC-2 and explicitly does not tag. 13-02 publishes REL-19-02 and re-confirms REL-19-01 on the tagged tree. No ROADMAP requirement ID is missing from all plans.

claim_verification is present and populated on both plans (not missing/empty). Live re-run matches every current-state row (see below).

---

## First principles / inversion

**Current Assumptions:**
- Assumption 1: RESEARCH one-execute-plan / do-not-split-bump-vs-tag is a locked user decision -- challenged: **false**. No 13-CONTEXT.md. The one-plan rule existed to avoid an untagged 1.19.0 commit on main. 13-02 soft-resets 13-01 per-task commits into one release(v1.19.0) content commit before tagging. A 6-task clone of 9-01 would itself be a scope blocker (5+ tasks).
- Assumption 2: REL-19-01 means rebuild / re-register SKILLS/NOTICE/cursor -- challenged: **false**. Thin-register already lists both slugs. Leftover is catalog integer + README rows.
- Assumption 3: map_version can stay 1.18.0 because classification happened under the 1.18 tree -- challenged: **false**. CONTRACT section 2 + RESEARCH Q1: bump with this release.
- Assumption 4: Task 2 verify new=cl.split(1.18.0 heading)[0] is the new entry -- challenged: **false**. That slice includes the Keep-a-Changelog / SemVer header URLs. http is already in the file before any T2 edit.
- Assumption 5: live (10 chapters) disappearing from README proves RPG was updated -- challenged: **false**. nasa-risk line 114 is a legitimate live (10 chapters) that must survive.

**Fundamental Truths:**
- REL-19-01 is honesty + both gates at 63/65, not a pack rebuild.
- REL-19-02 is origin annotated tag + GitHub Release; local tag alone fails the requirement.
- CHANGELOG SC-2 is competency coverage, including three non-builds.
- A verify that fails on a correct tree is not verification -- it is a stall or a corruption prompt.

**Guaranteed Failure Modes:**
1. Tag on a red / dirty tree: Avoid by 13-02 T1 hard-stop + explicit-path add.
2. Lightweight tag or /tmp notes: Avoid by git cat-file -t == tag + phase-dir notes file.
3. Slug-only CHANGELOG: Avoid by IO-01..07 tokens + DEFERRED/ACCEPT asserts (once the slice is correct).
4. Leave dod-vva-rpg.chapters at 10: Avoid by named leftover in T2 + T3 assert == 13.
5. Executor fixes T2 verify by deleting README nasa-risk 10-chapter text or header URLs: Avoid by rewriting the predicates (B1).
6. Redo Phase 11/12 or invent AAF/CBA/DoDM packs: Avoid by must-NOT + T3 fence.

**Anti-Goals (Never Do):**
- Rebuild packs or reverse the MAP-19-03 MOVE
- Unwire the map gate / add CI repo-Python
- git add -A / hand-edit docs/packs.html / lightweight tag / /tmp notes
- Claim IO-05/06/07 were built
- Put the .planning records commit into the tagged tree

**Remaining Risk:** After B1 is fixed, T3 automated still does not encode the residual-1.18.0 whitelist or packs dir count == 65 (W1). Action text does. 13-02 T1 automated does not grep release notes for IO-01..07 (W2).

---

## Dimension results

| Dim | Result | Notes |
|---|---|---|
| 1 Requirement coverage | PASS | REL-19-01 and REL-19-02 appear in both plans requirements fields and have covering tasks. |
| 2 Task completeness | FAIL | verify.plan-structure: 5/5 auto tasks have Files + Action + Verify + Done. 13-01 T2 automated always fails on a correct tree (B1). |
| 3 Dependencies | PASS | 13-01 wave 1 depends_on empty. 13-02 wave 2 depends_on 13-01 (same convention as 12-02). Acyclic. Soft-reset consumes 13-01 commits. |
| 4 Key links | PASS | RELEASE-INFO to gen_packs_page.py to packs.html; trio to check_release section 4; map JSON to CONTRACT envelope; CHANGELOG body to gh notes-file; tag to origin to GitHub Release; records commit after tag. |
| 5 Scope sanity | PASS with note | 13-01: 3 tasks / 13 files (file-count warning threshold; analog surface set -- do not split). 13-02: 2 tasks; files_modified lists 17 because T1 restages 13-01 paths -- unique new edits are 4 .planning files. estimate-check --calibrated: 45000 (0.45) and 35000 (0.35) of 100000; over_budget false. Plan confidence high vs tool confidence low (sample_count: 0) -- advisory only. |
| 6 Verification derivation | FAIL | Truths are user-observable. T2 automated contradicts those truths (B1). T3/13-02 T1 automated under-measure some acceptance lines (W1, W2). |
| 7 Context compliance | SKIPPED (no CONTEXT.md) | Discuss skipped. Locked RESEARCH user_constraints honored: Phase 9 analog sequence; tag+push+gh required; admin-bypass untouched; map membership frozen; no AAF/CBA/DoDM/stakeholder/IS-300; no CI repo-Python; stay on main. |
| 7b Scope reduction | PASS | Two-plan split is a scope-budget split, not a reduced REL-19. Leftovers, competency CHANGELOG, annotated tag, push, and gh release create are full. No v1 static labels. |
| 7c Architectural tier | PASS | Responsibility map is version trio + catalog/README honesty + generated packs.html + map envelope + dual gate + public tag + post-tag records. Tasks match those tiers. |
| 8 Nyquist | PASS with VALIDATION drift | 13-VALIDATION.md exists. All five tasks have automated (no MISSING, no --watch). Sampling 3/3 and 2/2. Wave 0 N/A (existing gates). VALIDATION per-task map is the old 6-task/one-plan shape (W3). |
| 9 Cross-plan contracts | PASS | 13-01 produces the 1.19.0 tree. 13-02 restages the same paths (no second transform) then tags. Records commit does not rewrite tagged content. |
| 10 CLAUDE.md | SKIPPED | No ./CLAUDE.md. |
| 11 Research resolution | WARN | Open Questions has no (RESOLVED) suffix and no inline RESOLVED markers (W4). Each item already has a Recommendation the plans implemented. |
| 12 Pattern compliance | PASS | Surfaces, CHANGELOG, release act, and records map to PATTERNS.md / 9-01 analogs. Shared explicit-path staging, gate re-run, competency narrative, and historical whitelist are in the covering tasks. |

### Smart-zone estimates

| Plan | estimate.tokens | budget | over_budget | plan confidence | tool confidence |
|---|---|---|---|---|---|
| 13-01 | 45000 | 100000 | false | high | low (sample_count: 0) |
| 13-02 | 35000 | 100000 | false | high | low (sample_count: 0) |

Calibration not yet applied for this project (sample_count: 0). Weigh the 3-task / 13-file and 2-task restage counts more heavily than the token figures.

### Dimension 8: Nyquist Compliance

| Task | Plan | Wave | Automated Command | Status |
|------|------|------|-------------------|--------|
| T1 version bump | 13-01 | 1 | python surface/map/CONTRACT asserts + gen_packs_page.py + empty packs.html diff | PASS |
| T2 CHANGELOG + leftovers | 13-01 | 1 | python CHANGELOG/catalog/README asserts | FAIL (B1 -- always red on a correct tree) |
| T3 dual-gate + sweep | 13-01 | 1 | both gates + catalog 63 + rpg 13 + validate_pack x3 + SOURCE-VETTING http==0 | PASS (W1 residual/65) |
| T1 tag + push + gh | 13-02 | 2 | git cat-file -t + ls-remote + gh release view + annotated/em-dash asserts | PASS (W2 notes IO tokens) |
| T2 records | 13-02 | 2 | STATE/MILESTONES/ROADMAP/REL box asserts | PASS |

Sampling: Wave 1: 3/3 have automated -> PASS (one command is wrong, not missing). Wave 2: 2/2 verified -> PASS.
Wave 0: none required -> PASS (existing check_release / check_capability_map / validate_pack / gh).
Overall: FAIL until B1 is fixed (8a presence holds; the automated command fails the correct tree).

No 2>/dev/null || echo 0, no || true feeding a comparison, no caret-anchored package-manager grep.

---

## Targeted checks (orchestrator brief)

### Requirement to task mapping

| Req | Planned delivery | Gap |
|---|---|---|
| REL-19-01 both gates at 63/65 | 13-01 T3 + 13-02 T1 precondition | T3 automated omits dirs==65 and residual 1.18.0 whitelist (W1) |
| REL-19-01 catalog leftover | 13-01 T2 dod-vva-rpg.chapters 10 to 13 | Named leftover. Live is 10 vs disk/PACK.yaml 13. |
| REL-19-01 README leftover | 13-01 T2 two live rows + RPG 13 | Action correct. Automated live (10 chapters) not in rd is wrong (B1). |
| REL-19-01 11 surfaces + packs.html | 13-01 T1 RELEASE-INFO first then gen | None in the action |
| REL-19-01 map_version 1.19.0 | 13-01 T1 JSON + CONTRACT example | Membership 644 asserted; no regen |
| REL-19-02 competency CHANGELOG | 13-01 T2 IO-01..07 draft + hard constraints | http not in new hits header URLs (B1) |
| REL-19-02 annotated tag + push + gh | 13-02 T1 exact Phase 9 commands | Automated does not grep notes for IO-01..07 (W2) |
| REL-19-02 records | 13-02 T2 STATE/MILESTONES/ROADMAP/REL | None material |

### Locked prohibitions (confirmed present)

| Prohibition | Where encoded | Live now |
|---|---|---|
| No pack rebuild / no invented AAF/CBA/DoDM/stakeholder/IS-300 | 13-01 + 13-02 must-NOT + T3 fence | packs not in 13-01 files_modified |
| No map reclassify / reverse MOVE | T1 envelope only; T3 no membership files | map_version 1.18.0 / 644 live |
| No CI repo-Python / no validate.yml edit | must-NOT + T3 fence | validate.yml:4-6 never execs repo Python; check_capability_map absent from YAML |
| No git add -A / no /tmp notes / no lightweight tag | 13-02 T1 explicit paths + phase-dir notes + cat-file -t | surprise untracked is .planning state only |
| No branch-protection change | 13-02 must-NOT + T-13-11 accept | STATE:61 admin-bypass |
| No SKILLS/NOTICE/cursor skill rewrite | 13-01 T2 + must-NOT | thin-register already has both slugs; cursor 64 |
| 13-01 does not tag | must_haves truth + prohibitions | no local v1.19* tag |

### claim_verification accuracy (live re-run, 2026-08-17)

| Plan | Claim | Live | Status |
|---|---|---|---|
| both | Branch is main; no v1.19 tag | main; git tag -l v1.19* empty | Accurate |
| 13-01 | Version trio still 1.18.0; no [1.19.0] | plugin/cursor 1.18.0; CHANGELOG ## [1.18.0]: 2026-08-17; RELEASE-INFO Version/Tag 1.18.0 Staged 2026-08-17T00:59:27Z; ## [1.19.0] absent | Accurate |
| 13-01 | map envelope 1.18.0 / schema 2 / 644 | matches | Accurate |
| 13-01 | CONTRACT example envelope 1.18.0; line 54 historical 1.17.0 | line 15 1.18.0; line 35 e.g. 1.18.0; historical 1.17.0 present | Accurate |
| 13-01 | Catalog leftover: n=63; rpg chapters 10; nasa 7; gps 6 | matches | Accurate |
| 13-01 | Disk chapter files 7 / 6 / 13 | matches | Accurate |
| 13-01 | PACK.yaml build.chapters 7 / 6 / 13 | packs/*/PACK.yaml:13 | Accurate |
| 13-01 | README leftovers | no nasa-std-8719-14; no is-gps-200n; line 164 (10 chapters); line 170 mil-std-40051 then 171 mit-ocw-se | Accurate |
| 13-01 | Thin-register already done | SKILLS both slugs + 63 packs; NOTICE both; cursor skills 64 includes both | Accurate |
| 13-01 | dirs 65 | 65 | Accurate |
| 13-01 | SOURCE-VETTING http count 0 | 0 | Accurate |
| 13-01 | CI never execs repo Python | validate.yml:4-6; check_capability_map absent | Accurate |
| 13-01 | Surprise untracked must not ship | ?? / M master_flow_state.json and .edge-coverage.json under .planning/phases/* | Accurate |
| 13-02 | MILESTONES still in-planning | ## v1.19.0 (in planning -- scoped 2026-08-17) | Accurate |
| 13-02 | REL boxes open | REQUIREMENTS:46-47 unchecked | Accurate |
| 13-02 | ROADMAP Phase 13 open | Phase 13 unchecked; Plans: TBD | Accurate |

No missing/empty claim_verification. No numeric conflict with RESEARCH that required a prescribed correction. Future-state 1.19.0 / chapters 13 / tag existence are labeled expected, not asserted as current.

### Both gates / leftover / CHANGELOG / tag (orchestrator must-confirm)

| Required | In executable plan content? |
|---|---|
| Both gates PASS | 13-01 T3 action+automated; 13-02 T1 step 1 hard-stop |
| Catalog leftover dod-vva-rpg 10 to 13 | 13-01 T2 action + automated rpg chapters==13 |
| CHANGELOG competency-led IO-01..07 | 13-01 T2 draft + token asserts |
| Annotated tag | 13-02 T1 git tag -a + cat-file -t == tag |
| Push | 13-02 T1 git push origin main --follow-tags + ls-remote |
| gh release create | 13-02 T1 phase-dir notes + gh release view |

---

## Findings

### Blockers (must fix)

**B1. [task_completeness / verification_derivation] 13-01 Task 2 automated verify fails on a correct post-edit tree**
- Plan: 13-01 Task 2
- Two predicates in the same automated block:

  1. new=cl.split(1.18.0 heading)[0] then assert http not in new. Live CHANGELOG header (lines 8-10, before any version heading) already contains https://keepachangelog.com and https://semver.org/. The slice is file prefix through the old heading, not the new [1.19.0] entry body. A correct competency-led entry still fails.
  2. assert live (10 chapters) not in README. Live README line 114 (nasa-risk) is a legitimate live (10 chapters) that must survive. After the leftover edit, RPG becomes 13 and nasa-risk stays 10. A correct README still fails.

- An executor who fixes the red verify by deleting header URLs or rewriting the nasa-risk row damages shipped docs. That is worse than a stall.
- Fix: assert only the slice between ## [1.19.0] and ## [1.18.0] for http / em dash / IO tokens. For README, assert the dod-vva-rpg row contains (13 chapters) and does not contain (10 chapters), plus the two new slug rows -- do not ban every live (10 chapters) in the file.

### Warnings (should fix; execution can proceed after B1)

**W1. [verification_derivation] 13-01 Task 3 automated omits residual 1.18.0 whitelist and dirs==65**
- Plan: 13-01 Task 3
- Action + acceptance + must_haves require residual 1.18.0 history-only and packs dir count == 65. Automated runs both gates, catalog 63, rpg 13, validate_pack x3, and SOURCE-VETTING http==0.
- Fix: add the residual grep (whitelist CHANGELOG [1.18.0] region, capability-pack-map.md v1.18.0 changelog, SOURCE-VETTING v1.18.0 heading) and an independent dirs count.

**W2. [verification_derivation] 13-02 Task 1 automated does not assert notes include IO-01..07**
- Plan: 13-02 Task 1
- Acceptance requires GitHub Release notes to include IO-01..07. Automated checks annotated tag, remote tag, tagName, and em dash in the title only.
- Fix: gh release view v1.19.0 --json body and assert IO-01..07 / DEFERRED / ACCEPT.

**W3. [nyquist] 13-VALIDATION.md Per-Task map is the old one-plan / three-row shape**
- File: 13-VALIDATION.md
- Rows: 13-01-01 check_release, 13-01-02 catalog/README, 13-01-03 tag/gh. Actual plans are 13-01 T1-T3 (bump / CHANGELOG+leftovers / gates) and 13-02 T1-T2 (publish / records). Frontmatter still nyquist_compliant: false.
- Fix: remap rows to the five execute tasks, or leave as advisory (8a-8d presence still holds once B1 is fixed).

**W4. [research_resolution] Open Questions unmarked**
- File: 13-RESEARCH.md Open Questions (no suffix; no inline RESOLVED)
- All three items already have Recommendations the plans followed (bump map_version; record Integration deferred not a fake +0; tick only REL-19 boxes).
- Fix: retitle Open Questions (RESOLVED) and prefix each item RESOLVED with the plan-chosen path. Do not reopen the decisions.

### Non-issues (checked, not raised)

- claim_verification present, non-empty, and live-accurate on both plans. Not missing.
- Two-plan split vs RESEARCH one plan: 13-02 consolidates to one release commit before tag; 6-task 9-01 clone would fail scope_sanity. Not a locked-decision contradiction.
- 13-02 files_modified 17 is restage listing, not 17 new edits.
- 13-01 T3 empty files matches analog 9-01 Task 4 (validation-only).
- Structure-tool: both plans valid=true, zero errors/warnings, 3+2 tasks complete.
- CHANGELOG draft in the plan uses ASCII hyphen / -> (RESEARCH draft still has em dashes -- plan correctly did not copy them).
- No version-trio steal into a tag from 13-01; no CI Python; no pack rebuild; no SKILLS/NOTICE rewrite.
- No CONTEXT.md / CLAUDE.md / REVIEWS.md -- those dimensions skipped, not failed.
- Verify-command format: no swallowed-error comparisons, no caret-anchored package-manager list.
- 13-02 T2 does not push the .planning commit -- same as 9-01 Task 6; not a REL-19 requirement.

---

## Structured issues

```yaml
issues:
  - plan: "13-01"
    dimension: task_completeness
    severity: blocker
    task: 2
    description: "Task 2 automated verify always fails on a correct tree. (1) split on the 1.18.0 heading includes Keep-a-Changelog/SemVer header URLs, so assert http not in new cannot pass. (2) assert live (10 chapters) not in README fails because nasa-risk line 114 is a legitimate 10-chapter live row that must survive the RPG 10 to 13 leftover."
    fix_hint: "Slice only the text between heading 1.19.0 and heading 1.18.0 for http/em-dash/IO asserts. For README, assert the dod-vva-rpg row is 13 chapters and that nasa-std-8719-14 / is-gps-200n rows exist -- do not ban every live (10 chapters)."

  - plan: "13-01"
    dimension: verification_derivation
    severity: warning
    task: 3
    description: "Task 3 action/acceptance/must_haves require residual 1.18.0 whitelist-only and dirs==65; automated verify does not measure either."
    fix_hint: "Add residual 1.18.0 grep with the three history whitelist hits, and assert packs dir count == 65."

  - plan: "13-02"
    dimension: verification_derivation
    severity: warning
    task: 1
    description: "Acceptance requires GitHub Release notes to include IO-01..07; automated only checks annotated tag, remote ref, tagName, and an em dash in the release title."
    fix_hint: "Assert IO-01..07 (and DEFERRED/ACCEPT) in gh release view --json body."

  - plan: null
    dimension: nyquist
    severity: warning
    description: "13-VALIDATION.md still maps three lumped 13-01 rows including tag/gh on plan 01. Actual work is 13-01 T1-T3 plus 13-02 T1-T2."
    fix_hint: "Remap the Per-Task table to the five execute tasks, or leave as advisory after B1."

  - plan: null
    dimension: research_resolution
    severity: warning
    description: "13-RESEARCH.md Open Questions has neither a (RESOLVED) suffix nor inline RESOLVED markers, though each item already has a Recommendation the plans implemented."
    fix_hint: "Mark the section Open Questions (RESOLVED) and stamp each item RESOLVED with the chosen path. Do not change verdicts."
```

---

## Recommendation

blockers: 1. 4 warnings. Verdict **NEEDS_WORK**.

Highest-leverage pre-execute fix: rewrite 13-01 Task 2 automated so a correct CHANGELOG + README leftover can print CHANGELOG_LEFTOVERS_OK. Then optionally add T3 residual/65 asserts, 13-02 notes IO greps, VALIDATION row remap, and Open Questions stamps.

Plans reduce 0 locked user decisions (no CONTEXT.md; RESEARCH constraints delivered in full). Both gates, catalog leftover, competency-led CHANGELOG, annotated tag, push, and gh release are planned. No phase split required. Do not execute until B1 is fixed.

**Verdict:** NEEDS_WORK

## ISSUES FOUND

**Phase:** 13-release-surface-v1-19-0
**Plans checked:** 2
**Issues:** blockers: 1, 4 warning(s), 0 info

### Blockers (must fix)

**1. [task_completeness] 13-01 T2 automated verify fails on a correct tree**
- Plan: 13-01
- Task: 2
- Fix: slice only the new [1.19.0] body for http/em-dash; do not ban README nasa-risk live (10 chapters)

### Warnings (should fix)

**1. [verification_derivation] 13-01 T3 omits residual 1.18.0 whitelist and dirs==65**
- Plan: 13-01
- Task: 3
- Fix: add residual grep + dirs count to automated

**2. [verification_derivation] 13-02 T1 does not assert notes include IO-01..07**
- Plan: 13-02
- Task: 1
- Fix: grep gh release view body for IO-01..07

**3. [nyquist] VALIDATION.md still describes the one-plan shape**
- Plan: null
- Fix: remap five execute-task rows

**4. [research_resolution] Open Questions unmarked**
- Plan: null
- Fix: Open Questions (RESOLVED) + inline RESOLVED stamps

1 blocker requires revision. Returning to planner with feedback.

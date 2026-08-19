# Phase 9 Plan Review

**Plan:** `9-01-PLAN.md` (6 tasks, wave 1, autonomous)
**Reviewed:** 2026-08-14, plan-mode, against `9-PLAN_CHECK.md`, `.planning/ROADMAP.md` Phase 9 (REL-1x-01/02, SC1/SC2), `.planning/REQUIREMENTS.md` REL-1x-01/02, `CHANGELOG.md` house format, `5-01-PLAN.md` + `5-PLAN_REVIEW.md` (proven template and its MA/MI lessons), `7-GAP_ANALYSIS.md` residual table, `8-GAP_ANALYSIS.md` routed items, and live-tree verification (both gates run, basis measured, chapter counts read from PACK.yaml, residual sweep executed on this Windows tree, tag/release conventions inspected, all six referenced commits resolved and ancestry-checked).

**Verdict:** APPROVE_WITH_NOTES

The release skeleton is sound and every load-bearing claim was independently re-verified live: all 11 version surfaces sit at 1.17.0 today at exactly the plan's cited lines (plugin.json:4, cursor plugin.json:5, RELEASE-INFO.txt:3-4, README.md:10/58/224, docs/index.html:110/226, docs/packs.html:86, catalog.yaml:13, 01-jgs-se-knowledge-packs.yaml:15); the residual sweep returns exactly the 5 whitelisted historical doc lines (capability-map-CONTRACT.md:54, capability-pack-map.md:16, SOURCE-VETTING.md:93/144/149) plus CHANGELOG history; chapter counts match live PACK.yaml (8/6/6/7/7/8/10); the basis is 61 catalog / 63 dirs / 62 cursor skills; the map envelope is schema_version 2, map_version "1.18.0", 32 clusters, 628 entries; both gates exit 0 live; the doe-o-413-3 rename + alias is in catalog.json (lines 591, 600-601); CHANGELOG.md:57-58 does list docs/index.html as a registration surface (the wording fix is real); OUSW survives only at SOURCE-VETTING.md:130; "cluster 30" survives only at CONTRACT line 73 and its name matches capability-pack-map.md:748; e00ac7d/c9d5e7e/05eb9ad/e4699c4/bdc6c9e all exist and are post-tag v1.17.0; tag colon style and release-title em-dash style confirmed against the live v1.17.0 tag and GitHub Release. All five v1.17 plan-review lessons are incorporated (see disposition table). The three findings below are plan-text hygiene: none ships wrong data, none false-fails a verify block. No BLOCKER, no MAJOR.

## Findings

### MI-01. Caveat citation "per 7-GAP_ANALYSIS R1/R2/R5" misattributes the mil-std-40051 caveat — MINOR

**File:** `9-01-PLAN.md:106` (Task 2 action, caveats sentence); `:179` (success_criteria repeats "vva/faa/40051 currency caveats")
**Issue:** The plan grounds three caveats in "7-GAP_ANALYSIS R1/R2/R5". Live residual table: R1 = vva ~2011 internal dates (owner: Phase 9 CHANGELOG caveat) — matches the vva caveat; R2 = faa-std-025 Rev F vs Rev E (owner: Phase 9 CHANGELOG caveat) — matches the faa caveat; but R5 = federal-bca "(c)" wording imprecise (class: cosmetic, owner: v1.19 polish), NOT mil-std-40051. The mil-std-40051 1168-vs-584 page-counter caveat the plan instructs to write appears in 7-GAP_ANALYSIS only under "Rejected as non-gaps" ("accepted-ambiguity disposition is the code review's own sanctioned option"). The caveat text itself is factually accurate and consistent with that sanctioned ambiguity disclosure, so the shipped content is fine — but the plan's stated source is a false audit trail, and a verifier tracing "R5 caveat present" would look for a federal-bca caveat that the plan (correctly) never instructs.
**Fix:** In Task 2, cite "per 7-GAP_ANALYSIS R1/R2 plus the 7-CODE_REVIEW sanctioned accepted-ambiguity note on mil-std-40051's page counters". (Task 6's backlog citation "optional PACK.yaml note additions and ROSAP Rev E retry per R1/R2/R5" is defensible — R5 genuinely is a v1.19 backlog item — but the same clarity pass would help there.)

### MI-02. Task 2's one-liner style sketch embeds an em dash, contradicting the entry's own hard constraint — MINOR

**File:** `9-01-PLAN.md:106` (Task 2 action: "the bold-slug `(N ch): description — Tier 1` style of the 1.17.0 entry")
**Issue:** The same action imposes "no em dashes anywhere in the entry" as a HARD CONSTRAINT, and the actual 1.17.0 one-liners end "... orientation. Tier 1 (US-gov public domain)." — a period, no dash, with the tier parenthesized. An executor copying the inline sketch literally injects an em dash and then fails the task's own verify ("grep for the em-dash character within the new entry returns zero") — self-correcting, but the plan text contradicts itself and nudges toward the error.
**Fix:** Change the sketch to "(N ch): description. Tier 1 (US-gov public domain)." — matching the 1.17.0 entry verbatim.

### MI-03. Task 6 does not tick the ROADMAP plan-list checkbox for 9-01-PLAN.md — MINOR

**File:** `9-01-PLAN.md:141-142` (Task 6 action/verify); `.planning/ROADMAP.md:132`
**Issue:** Task 6 ticks the Phase 9 checkbox (line 79) and says "fill `**Plans**: 1 plan` with `9-01-PLAN.md` listed" — but the plan is already listed at ROADMAP.md:132 as `- [ ] 9-01-PLAN.md`, and every completed phase in the ROADMAP shows its plan entries as `- [x]`. Without an explicit instruction, the likely outcome is a checked phase with an unchecked plan entry — the exact stale-bookkeeping pattern R8 of 7-GAP_ANALYSIS flagged for Phase 7. The verify block only greps line 79, so it would not catch the miss.
**Fix:** Add to Task 6: "and tick the `- [ ] 9-01-PLAN.md` entry in the Phase 9 Plans list (ROADMAP.md:132)"; extend the verify to grep ROADMAP.md:132 for `- [x]`.

### IN-01. IN-02 namespace collision between the 7-series and 8-series code-review IDs — INFO

**File:** `9-01-PLAN.md:141` (Task 6: "IN-02 minimal committed overlap checker")
**Issue:** Two IN-numbering series are live in the phase tree: 7-GAP_ANALYSIS's v1.19 backlog carries "IN-02 minimal committed overlap checker" while 8-GAP_ANALYSIS's IN-02 is "mil-std-881f support-file asymmetry (no action)". The plan's usage is self-qualifying ("minimal committed overlap checker"), so execution is unambiguous, but the STATE.md backlog entry should keep the qualifier so future grep of "IN-02" against STATE cannot be misread against the 8-series item.
**Fix:** Record the backlog item in STATE.md as "IN-02 (Phase 7 review): minimal committed overlap checker".

## Phase 5 lessons diff-check (5-PLAN_REVIEW MA/MI vs this plan)

| v1.17 lesson | Phase 9 disposition |
|---|---|
| MA-01 chapter counts wrong in draft (public notes risk) | Incorporated — live PACK.yaml values hardcoded (8/6/6/7/7/8/10), re-read-before-write instruction, non-uniformity tripwire ("a uniform value means a copy error"); counts re-verified live 2026-08-14 |
| MA-02 Windows grep false-fail (`grep -v ".planning/"` misses backslash paths) | Incorporated — all sweep commands use the MA-02 fix form (`--exclude-dir=...`); exact pipeline executed live on this Windows tree and returns exactly the claimed hit set |
| MA-03 gate never prints the catalog/dir basis | Incorporated — truth[0] and Task 4 split into "gate prints PASS" + independent `python -c` / `ls | wc -l` measurements (61/63) |
| MI-01 tag message style | Incorporated — colon style with "copy `git tag -l -n3 v1.17.0` exactly" (live tag confirmed colon style) |
| MI-02 README table/badge mismatch | Resolved upstream — Phase 7 landed all 7 pack rows + doe-o-413-3 row; badge reads packs-61 (verified live) |
| MI-03 hardcoded release date | Incorporated — "use the actual date/time, not a hardcoded value" in Task 1 and Task 2 |
| MI-04 scanner residual recording | N/A this cycle — scan_generated_skill.py is a Phase 7 SC2 item, discharged and recorded there; Phase 9 has no pack-body changes |

## Verified non-issues (checked, not raised)

- Dual-gate validation is real and origin-tied: both gates run live now (check_release PASS, capability-map PASS printing TOTAL: 628); Task 4 re-runs both plus a final pre-commit check_release (OneDrive sync-lag, T-9-03); Task 5's done criteria require `git ls-remote --tags origin v1.18.0` AND `gh release view v1.18.0` — REL-1x-02 is not claimable on local state alone.
- Release sequencing matches the proven Phase 5 template and repo convention: release commit last content commit on main, annotated tag, `--follow-tags`, `.planning`-only records commit afterward (matches the 61-post-tag-commits precedent); commit/tag message style matches v1.17.0's live forms.
- Explicit-path staging is thoroughly mitigated: Task 4 precondition (no untracked outside .planning/), Task 5 explicit-path-only add + `git status --short` audit + STOP-on-stray, T-9-01; live `git status` shows only .planning workflow state, and docs/ROLE-AGENTS-REQUIREMENTS-V2.md plus both capability-pack-map files are tracked (verified) — the Phase 5 untracked-files hazard no longer exists.
- No duplicate Changed items: the `.planning/` scan-skip line already sits in the 1.17.0 entry's Changed section (CHANGELOG.md:54-55, verified) and Task 2 explicitly forbids restating it.
- Registration-surface claims in the planned Changed section are true today: NOTICE and SKILLS.md both carry the new packs, catalog 61, cursor 62 (verified live), and the corrected surface list rightly omits docs/index.html.
- Whitelist arithmetic is exact: the live sweep returns only CHANGELOG history (lines 12, 38) + the 11 surface hits + exactly the 5 whitelisted doc lines — nothing in packs/ or docs/capability-pack-map.json.
- CHANGELOG insertion point (`## [1.17.0]: 2026-08-15` at line 12), "Catalogue now 61 packs (+2 signposts)" (63 dirs - 2 signposts = 61 catalog, consistent with the 54/56 precedent), three-section house format, and RELEASE-INFO-first -> gen_packs_page ordering (gate §5c regeneration dependency) all check out.
- Task 6 anchors exist: MILESTONES.md:16 "v1.18.0 (in execution ...)"; ROADMAP.md:79 Phase 9 checkbox; FUT-04/FUT-05 defined in the REQUIREMENTS FUT register (FUT-05 recorded at bdc6c9e, confirmed); thin clusters 3/5/15 named consistently with the live map (3/4/2 entries respectively).
- 9-PLAN_CHECK's 13-claim "all VERIFIED" table was spot-re-checked claim-by-claim against the live tree; none is stale. Its verdict PASS is consistent with this review.
- Fixed-item attributions are accurate: gate hardenings match 6f7b54b; cursor-manifest registration matches e00ac7d ("register 7 GP packs (catalog 61, cursor 62)"); e00ac7d/c9d5e7e are confirmed post-tag v1.17.0, so "post-tag v1.17.x commit" is correct.

## Required before execute

Nothing blocking. MI-01 through MI-03 are small plan-text edits best applied in one pass before execution (MI-01 and MI-02 touch the public-notes path, so applying them pre-execute keeps the audit trail honest); IN-01 is a STATE-recording qualifier. No task restructuring, no scope change.

---
_Reviewer: ZCode (gsd plan-mode review) — 2026-08-14_

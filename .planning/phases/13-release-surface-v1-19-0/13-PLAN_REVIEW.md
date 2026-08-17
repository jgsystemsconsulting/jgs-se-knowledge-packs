# Phase 13 Plan Review — 13-01-PLAN.md + 13-02-PLAN.md

**Reviewed:** 2026-08-17
**Depth:** deep (plan vs live tree: ROADMAP Phase 13 SC-1..SC-2, REQUIREMENTS REL-19-01/02, 13-RESEARCH recommended shape + user_constraints + Patterns 1–7, 13-PLAN_CHECK rev 2 after `e988867`, 13-VALIDATION, analog 9-01-PLAN.md / 9-PLAN_REVIEW.md / 12-PLAN_REVIEW.md; live re-run of every `claim_verification` row; Git Bash `bash -n` + CPython `compile()` on every `<automated>` block)
**Plans:** `.planning/phases/13-release-surface-v1-19-0/13-01-PLAN.md` (post `e988867`), `13-02-PLAN.md`
**Plan check:** 13-PLAN_CHECK.md — PASS_WITH_FIXES (blockers: 0, 3 warnings; B1 closed)
**Files reviewed:** both plans against locked RESEARCH constraints + live version/catalog/map/release surfaces

**Verdict:** PASS_WITH_FIXES

The two waves will bump the 11 analog surfaces plus `map_version` / CONTRACT example, land a competency-led `[1.19.0]`, close the catalog/README leftovers, dual-gate at 63/65, then publish an annotated tag + GitHub Release and record shipped state — if the executor follows the actions. B1 is closed: T2 now slices the new entry body only (Keep-a-Changelog / SemVer header URLs excluded) and scopes the leftover integer to the `dod-vva-rpg` row (nasa-risk `live (10 chapters)` is allowed). No success criterion is missing. No plan would `git add -A`, create a lightweight tag, unwire the map gate, rebuild packs, or still false-fail T2 on header URLs / nasa-risk.

What keeps this off APPROVE is the same class as 13-PLAN_CHECK W5: two leftover indents inside `python -c` strings raise `IndentationError` if pasted literally. Predicates themselves are correct. One-line de-indents, no redesign, no split, no verdict changes.

---

## Findings

### MN-01 [MINOR] 13-01 Task 2 leftover-indented heading-order assert (W5 still present)

**File:** 13-01-PLAN.md, Task 2 `<verify><automated>` line 344
**Issue:** `    assert cl.find('## [1.19.0]') < cl.find('## [1.18.0]')` is indented four spaces inside a `python -c` string. A literal paste raises `IndentationError: unexpected indent` before any assert. After de-indent, live pre-release tree fail-closes at `assert cl.count('## [1.19.0]')==1`. In-memory correct tree (new-entry slice + RPG 13 + two slug rows) PASSES; header URLs and nasa-risk `live (10 chapters)` are not consulted.

This is **not** B1. The predicates no longer ban Keep-a-Changelog `http` in the file prefix and no longer ban every README `live (10 chapters)` row. It is a paste hazard. Executor: de-indent that one assert to column 0 of the `python -c` body.

**Fix:** unindent line 344. Optional pre-execute tidy; may be done at run time.

### MN-02 [MINOR] 13-01 Task 3 first `python -c` has a tab-indented `print`

**File:** 13-01-PLAN.md, Task 3 `<verify><automated>` lines 411–412
**Issue:** After `assert mp['map_version']=='1.19.0'` the snippet is a literal tab + `print('BASIS_OK')` then a leftover tab before the closing quote. CPython `compile()` this session: `IndentationError: unexpected indent` on that `print`. Same paste class as MN-01 / W5; 13-PLAN_CHECK did not name it.

The `&&` chain runs both gates *before* this block, so REL-19-01 gate truth still executes if the executor follows the action. The automated tail (catalog 13 / `map_version` / `validate_pack` x3 / residual 1.18.0 / dirs==65) never starts until the tab is removed. Fail-closed, not a false green.

**Fix:** de-indent `print('BASIS_OK')` to the same column as the surrounding asserts. Drop the stray tab on the closer.

### MN-03 [MINOR] 13-VALIDATION.md Per-Task map is still the old one-plan / three-row shape

**File:** 13-VALIDATION.md
**Issue:** Rows: 13-01-01 `check_release`, 13-01-02 catalog/README, 13-01-03 tag/gh. Actual plans are 13-01 T1–T3 and 13-02 T1–T2. Frontmatter still `nyquist_compliant: false`. Nyquist 8a–8d still pass (every execute task has `<automated>`). 13-PLAN_CHECK W3.

**Fix:** remap rows to the five execute tasks, or leave as advisory.

### MN-04 [MINOR] 13-RESEARCH.md Open Questions unmarked

**File:** 13-RESEARCH.md Open Questions
**Issue:** No `(RESOLVED)` suffix and no inline RESOLVED markers. All three items already have Recommendations the plans implemented (`map_version` 1.19.0; Integration recorded deferred; tick REL-19 only). 13-PLAN_CHECK W4.

**Fix:** retitle `Open Questions (RESOLVED)` and prefix each item RESOLVED with the chosen path. Do not reopen.

### MN-05 [MINOR] T2 automated does not pin CHANGELOG chapter counts 7/6/13

**File:** 13-01-PLAN.md, Task 2 `<verify><automated>`
**Issue:** Acceptance requires the new entry's counts equal live `PACK.yaml` `build.chapters` 7/6/13. Automated greps IO-01..07 / `Catalogue now 63` / DEFERRED / ACCEPT / no `http` / no em dash, and asserts catalog integers + README row text. A slug-led entry that names the IOs but writes a uniform `8 ch` would still print `CHANGELOG_LEFTOVERS_OK`. Action + draft already lock 7/6/13 and say re-read PACK.yaml immediately before writing.

**Fix:** `assert '7 ch' in new and '6 ch' in new and '13' in new` (or bind to the IO-03/04/02 lines). Not execute-blocking.

### IN-01 [INFO] `gh` default account is not the publisher

**File:** 13-02-PLAN.md `claim_verification` row "gh authenticated as publisher"; Task 1 precondition `gh auth status succeeds`
**Issue:** Live 2026-08-17: `systems-researcher` is the **active** `gh` account; `jgsystemsconsulting` is logged in but inactive. `gh api repos/jgsystemsconsulting/jgs-se-knowledge-packs` as the active identity returns `push: false`. `gh release view v1.18.0` still works (read). `git push` / `gh release create` as the default account will not satisfy REL-19-02.

This is environment drift, not a missing command. The plan's analog (`git push origin main --follow-tags` + phase-dir notes) is correct.

**Fix:** executor `gh auth switch --user jgsystemsconsulting` (or equivalent) before 13-02 Task 1. Do not change branch protection.

---

## Verify-command re-run (this session)

All five `<automated>` blocks extracted verbatim. `bash -n` via `C:\Program Files\Git\bin\bash.exe` 5.3.15 (not WSL `bash`, which cannot translate this cwd):

| Task | `bash -n` | CPython `compile()` of each `python -c` | Distinguishes live tree? |
|---|---|---|---|
| 13-01 T1 | SYNTAX_OK | COMPILE_OK | Yes. Live plugin/RELEASE-INFO/README still 1.18.0; `## [1.19.0]` absent (T2 owns heading) |
| 13-01 T2 | SYNTAX_OK | **IndentationError** on leftover-indented heading-order assert (MN-01) | After de-indent: fail-closed `AssertionError` at missing `## [1.19.0]`. Header URLs / nasa-risk not consulted. In-memory correct tree PASSES |
| 13-01 T3 py1 | SYNTAX_OK | **IndentationError** on tab-indented `print('BASIS_OK')` (MN-02) | After de-indent: fail-closed on `map_version=='1.19.0'` and `chapters==13` (live 1.18.0 / 10) |
| 13-01 T3 py2 | SYNTAX_OK | COMPILE_OK | Residual live-file `1.18.0` ban + dirs==65 + SOURCE-VETTING `http==0`. Live plugin/README still contain 1.18.0 (expected until T1) |
| 13-02 T1 | SYNTAX_OK | COMPILE_OK | Yes. No local `v1.19.0` tag; `git rev-parse` would fail closed |
| 13-02 T2 | SYNTAX_OK | COMPILE_OK | Yes. MILESTONES heading still `in planning`; REL boxes unchecked; ROADMAP Phase 13 `[ ]` |

No `2>/dev/null || echo 0`. No `|| true` feeding a comparison. No caret-anchored package-manager grep.

T2 rewrite confirmed against the two B1 predicates on an in-memory correct tree (no writes):

- New slice between `## [1.19.0]` and `## [1.18.0]`: `http` false; `keepachangelog` false; IO-01..07 + `Catalogue now 63` + DEFERRED + ACCEPT present.
- Prefix-through-`## [1.18.0]` still contains `https://keepachangelog.com` / `https://semver.org` — the **old** http-ban would still false-fail. That predicate is gone.
- README leftover edit: 8719 `live (7 chapters)`, GPS `live (6 chapters)`, RPG `(13 chapters)`; nasa-risk `live (10 chapters)` still present. The **old** ban-every-`live (10 chapters)` would still false-fail. That predicate is gone.

---

## claim_verification live re-run (cwd repo root, 2026-08-17)

No missing/empty `claim_verification`. No invented replacements. Current-state rows match except the publisher-account active flag (IN-01):

| Plan | Claim | Live | Status |
|---|---|---|---|
| 13-01 / 13-02 | Branch is main; no `v1.19*` tag | `main`; `git tag -l 'v1.19*'` empty | Accurate |
| 13-01 | Both gates PASS at 1.18.0 basis | map `PASS: capability map OK` TOTAL 644 exit 0; `RELEASE CHECK: PASS` exit 0 (map block printed first) | Accurate |
| 13-01 | Version trio still 1.18.0; no `[1.19.0]` | plugin `1.18.0`; cursor `1.18.0`; `## [1.18.0]: 2026-08-17`; `Version: 1.18.0` `Tag: v1.18.0` `Staged: 2026-08-17T00:59:27Z`; `## [1.19.0]` absent | Accurate |
| 13-01 | map envelope 1.18.0 / 644 | schema 2, `map_version` `1.18.0`, `generated_on` `2026-08-17`, 32 clusters, 644 entries | Accurate |
| 13-01 | CONTRACT example envelope 1.18.0 | :15 `"map_version": "1.18.0"`; :35 `e.g. "1.18.0"`; :54 historical `1.17.0` | Accurate |
| 13-01 | Catalog leftover | n_catalog 63; `dod-vva-rpg` 10; nasa-std-8719-14 7; is-gps-200n 6 | Accurate |
| 13-01 | Disk chapter files / PACK.yaml `build.chapters` | 7 / 6 / 13 files; PACK.yaml 7 / 6 / 13 | Accurate |
| 13-01 | README leftovers | no `nasa-std-8719-14`; no `is-gps-200n`; :164 `(10 chapters)`; :170 `mil-std-40051` then :171 `mit-ocw-se`; badge `packs-63`; version 1.18.0; :114 nasa-risk `live (10 chapters)` | Accurate |
| 13-01 | Thin-register already done | SKILLS `63 packs (+2 signposts)` + both slugs; cursor skills 64; NOTICE both slugs | Accurate |
| 13-01 | dirs 65 | 65 | Accurate |
| 13-01 | Historical 1.17.0 whitelist | CHANGELOG history; CONTRACT:54; capability-pack-map.md; SOURCE-VETTING.md | Accurate |
| 13-01 | CI never execs repo Python | `validate.yml:4-5` wrap `never` / `executes checked-out repository code`; `check_capability_map` absent | Accurate (phrase is line-wrapped) |
| 13-01 | Link policy | `docs/SOURCE-VETTING.md` `http` count 0 | Accurate |
| 13-01 / 13-02 | gh authenticated; v1.18.0 release exists | `gh release view v1.18.0` title `v1.18.0 — 7 gap-driven Tier-1 packs + capability map v2`; both accounts logged in | Publisher exists; **active** identity is `systems-researcher` (IN-01) |
| 13-02 | Live tag style | `v1.17.0: 8 Tier-1…`; `v1.18.0: 7 gap-driven…` (colon, annotated) | Accurate |
| 13-02 | Phase 9 analog did push + `/tmp` fail + soft-reset | `9-01-PLAN.md` has `git push origin main --follow-tags`; `9-01-SUMMARY.md:221-232` soft-reset + `/tmp` `cannot find the file specified` | Accurate |
| 13-02 | Surprise untracked | `??` `.planning/phases/*/master_flow_state.json` and `.edge-coverage.json` | Accurate |
| 13-02 | Admin-bypass; MILESTONES in-planning; REL boxes open; ROADMAP Phase 13 open | STATE:61; MILESTONES:25 `in planning`; REQUIREMENTS:46-47 unchecked; ROADMAP:27 `[ ]` / :84 `Plans: TBD` | Accurate |

---

## Plan-check incorporation

All three 13-PLAN_CHECK warnings are in-scope as small edits (one T2 de-indent, advisory VALIDATION/Open-Questions stamps). B1 is independently re-closed this session. The new T3 tab (MN-02) is the same paste class as W5, not a new false-fail.

| Check finding | In-scope? | Covered by |
|---|---|---|
| B1 T2 false-fail (Keep-a-Changelog prefix + ban-every-live-10) | Closed — slice is new-entry body; rpg_row scoped | Confirmed live + in-memory |
| W3 VALIDATION.md lumps execute tasks | Yes — advisory row | MN-03 |
| W4 Open Questions unmarked | Yes — stamp only | MN-04 |
| W5 T2 leftover indent | Yes — still present; IndentationError if pasted | MN-01 |
| (new) T3 tab-indented `print('BASIS_OK')` | Yes — sibling paste hazard | MN-02 |

---

## Confirmed correct (checked, not raised)

- ROADMAP SC-1 / SC-2 and REQUIREMENTS REL-19-01 / REL-19-02 are all tasked. Frontmatter IDs: both plans list `[REL-19-01, REL-19-02]`. 13-01 owns honesty + both gates + competency CHANGELOG; 13-02 owns annotated tag + push + `gh release create` + records.
- Analog order locked: RELEASE-INFO first → `gen_packs_page.py` → remaining surfaces; CHANGELOG heading is Task 2 (trio intentionally split after T1).
- `map_version` bump is string-only (RESEARCH Q1 YES). Membership asserted 644. No cluster rewrite. CONTRACT :54 historical `1.17.0` left alone.
- Two-plan split vs RESEARCH "one execute plan" is a scope-budget split. 13-02 soft-resets to `PRE_RELEASE_HEAD` and restages explicit paths into one `release(v1.19.0)` content commit (Phase 9 deviation #1). Not a locked-decision contradiction. Do not merge the plans.
- Must-NOT holds: no pack rebuild; no map reclassify / reverse MOVE; no unwire; no CI repo-Python; no `git add -A` / `git add docs/` / `git add .`; no `/tmp` notes; no lightweight tag; no AAF/CBA/DoDM/stakeholder packs; no SKILLS/NOTICE/cursor skill-list rewrite; no REL box ticks in 13-01; records commit is `.planning`-only after the tag.
- T2 http/em-dash bans apply to the **new-entry slice**, not the Keep-a-Changelog header. nasa-risk `live (10 chapters)` is allowed. rpg_row must contain `(13 chapters)` and must not contain `(10 chapters)`.
- 13-02 T1 verify requires `git cat-file -t == tag`, origin `ls-remote`, and `gh release view` body tokens IO-01..07 + DEFERRED + ACCEPT. Title em dash is public-only.
- 13-02 T2 ticks Phase 13 + both plan filenames + REL-19-01/02; MILESTONES must leave `in planning` on the v1.19.0 heading; STATE carries FUT-04 / FUT-05 / IN-02 / AAF deferral.
- 13-01 45000 and 13-02 35000 are under the 100k smart-zone.
- Stay on `main`. No branches / worktrees. EDGE_ABSENT=1 honored.
- Unclassified `.edge-coverage.json` / `master_flow_state.json` remain untracked by instruction.

---

## Recommendation

De-indent the two leftover `python -c` lines (13-01 T2 heading-order assert; 13-01 T3 `print('BASIS_OK')`) before or while executing. Stamp Open Questions / VALIDATION.md if convenient — not execute-blocking. Switch `gh` to `jgsystemsconsulting` before 13-02 Task 1. No verdict changes, no scope changes, no re-plan, no phase split.

B1 stays closed. Execute may proceed.

---

**Verdict:** PASS_WITH_FIXES

blockers: 0
**majors:** 0
**minors:** 5

Path: `.planning/phases/13-release-surface-v1-19-0/13-PLAN_REVIEW.md`

Two-wave plan covers every Phase 13 success criterion and both REL-19 IDs. Actions match 13-RESEARCH and the Phase 9 analog (including push). T2 no longer false-fails on Keep-a-Changelog URLs or nasa-risk. Advance after de-indenting the two leftover `python -c` lines.

# Phase 5 Plan Review

**Plan:** `5-01-PLAN.md` (7 tasks, wave 1, autonomous)
**Reviewed:** 2026-08-14, plan-mode, against `5-RESEARCH.md`, `5-PLAN_CHECK.md` (W1-W6), `.planning/ROADMAP.md` Phase 5 (REL-01/REL-02, SC1/SC2), `CHANGELOG.md` house format, `.claude-plugin/plugin.json`, `RELEASE-INFO.txt`, git tag list, and live-tree verification (gate run, gate source read, chapter files counted, grep pipelines executed).

**Verdict:** NEEDS_WORK

The release skeleton is sound: sequencing (edits -> gate -> commit -> annotated tag -> push -> `gh release create` -> origin-tied done-criteria) matches research §4 and the 6ede444 convention; all 11 version surfaces are tasked at verified-current line numbers; explicit-path staging with the three untracked docs/ files named; Task 7's .planning-after-tag commit matches established practice (61 commits after v1.16.3, 46 touching .planning). Three MAJOR defects remain unincorporated from plan_check (the plan predates it): one ships incorrect data into a public, hard-to-retract artifact, and two make the plan's own verify blocks false-fail or unmeasurable. All three are small plan-text fixes; apply them and this is an APPROVE.

## Findings

### MA-01. CHANGELOG chapter-count correction points at a source with no counts; draft is wrong for 6 of 8 packs — MAJOR

**File:** `5-01-PLAN.md:98` (Task 2 action), `:99` (verify), `:82` (claim_verification last row); `5-RESEARCH.md:64-84` (draft)
**Issue:** Task 2 instructs "read each of the 8 new packs' SKILLS.md rows and correct the chapter counts", and its verify requires "chapter counts match SKILLS.md rows". Live SKILLS.md rows (lines 59-66) contain no `(N ch)` figures — the named source cannot correct anything. Actual counts from `packs/<slug>/chapters/`: nist-800-171=8, nist-800-61=6, cisa-cpg=5, doe-sem=7, mil-hdbk-338=9, mil-hdbk-516=8, nasa-ms-7009=7, doe-413-3b=6. The research §2 draft claims `(8 ch)` for all 8 — wrong for 6. The CHANGELOG entry also becomes the GitHub Release notes body (Task 6 `--notes-file`), so wrong counts ship publicly and are annoying to retract. (Incorporates plan_check W3.)
**Fix:** Re-point Task 2 at `packs/<slug>/PACK.yaml` `build.chapters` (or `ls packs/<slug>/chapters/*.md | wc -l`), pre-correct the draft one-liners to 8/6/5/7/9/8/7/6, and restate the verify as "one-liner counts equal chapter-file counts per pack".

### MA-02. Task 1 verify grep pipeline false-fails on this Windows tree — MAJOR

**File:** `5-01-PLAN.md:91` (Task 1 verify); `:32` (must_haves truth 2)
**Issue:** The exact pipeline (`grep -rn "1\.16\.3" --include=... . | grep -v ".planning/" | grep -v "packs/"`) run live returns 65 hits, of which 52 are `.planning\...` paths: Windows grep emits backslash separators (cf. live output `.claude-plugin\plugin.json:4`), so `grep -v ".planning/"` does not match them. After a correct bump the executor sees 52 phantom hits — a false FAIL that plan_check already warned "can send the executor into .planning edits that Task 1 does not own". A verifier scoring must_haves truth 2 with the written command also fails it. (Incorporates plan_check W1.)
**Fix:** Replace with `grep -rn "1\.16\.3" --include="*.json" --include="*.md" --include="*.txt" --include="*.html" --include="*.yaml" --exclude-dir=.git --exclude-dir=.planning --exclude-dir=packs .` — verified live: returns exactly the 12 release-surface hits plus the `CHANGELOG.md:12` history heading, nothing else.

### MA-03. must_haves truth 1 / Task 5 verify require the gate to print a 54/56 catalog basis it never prints — MAJOR

**File:** `5-01-PLAN.md:31` (must_haves truth 1), `:123-124` (Task 5 action/verify)
**Issue:** Live `python tooling/check_release.py` prints only `RELEASE CHECK: PASS — repo is release-ready against the mechanical gate.` (source: `tooling/check_release.py:237`; pack/dir counts appear only inside FAIL messages at line 166). The 54/56 state is real (54 catalog packs, 56 dirs, gate PASS confirmed live), but the truth as written is unobservable via gate stdout, so verification will score it false or force improvisation. ROADMAP Phase 5 SC1 is what demands the 54/56 wording. (Incorporates plan_check W2.)
**Fix:** Restate truth 1 as two assertions: (a) gate exits 0 printing `RELEASE CHECK: PASS`; (b) separate measurement: `catalog.json` packs == 54, `packs/` directories == 56, SKILLS.md header reads 54 packs (+2 signposts).

### MI-01. Annotated-tag message deviates from the repo's own tag convention and misstates it — MINOR

**File:** `5-01-PLAN.md:132` (Task 6 action)
**Issue:** Task 6 tags with an em dash subject (`v1.17.0 — 8 Tier-1...`) justified as "em dash as in v1.16.3 style". Live tags use colon style (`v1.16.3: RR-S-13 compliance + browsable pack reference page`); the em dash matches GitHub Release titles, not git tag messages. The plan's own claim_verification row 4 (:76) verified the colon style — Task 6 contradicts the plan's own evidence. Cosmetic and releasable either way. (plan_check "Minor style nit", not yet incorporated.)
**Fix:** `-m "v1.17.0: 8 Tier-1 public-domain packs (54 +2 signposts)"`, or keep the em dash but delete the false "as in v1.16.3 style" claim.

### MI-02. Task 4 framing line has no anchor: README has zero DOE mentions and its catalogue table omits all 8 new packs while the badge claims 54 — MINOR

**File:** `5-01-PLAN.md:114` (Task 4 action); README.md:11, :155-156
**Issue:** Live `grep "doe-413\|DOE" README.md` returns zero hits; the table ends at `faa-rma` + planned `mit-ocw-se` while the badge says `packs-54-blueviolet`. The "near the DOE pack mention / pack list" placement instruction points at a mention that does not exist, and post-release README self-contradicts (badge 54, table 47 rows, plus a doe-413-3b framing line next to nothing). REL-01's named surfaces (catalog.json/SKILLS.md/packs.html/NOTICE) are already synced, so this does not block SC1 — hence MINOR, not MAJOR. (Incorporates plan_check W5 at recommendation strength.)
**Fix:** Either add the 8 catalogue rows (small, in-scope docs edit inside the release commit, matching the 54 badge) or name the exact anchor explicitly (e.g., after the badge/pack-count prose at README line ~58) so the line lands deliberately.

### MI-03. Hardcoded release date 2026-08-15 in the CHANGELOG heading and RELEASE-INFO Staged — MINOR

**File:** `5-01-PLAN.md:90` (Staged), `:98` (`## [1.17.0]: 2026-08-15`)
**Issue:** Today is 2026-08-14. If execution slips past the 15th, the shipped public CHANGELOG carries a wrong date against the Keep-a-Changelog convention of actual release dates (all prior entries use real dates).
**Fix:** Parameterize: "release date = execution date (expected 2026-08-15)".

### MI-04. Task 7 residual list omits the scan_generated_skill.py residual — MINOR

**File:** `5-01-PLAN.md:141` (Task 7 action)
**Issue:** REL-02's text requires all packs pass `scan_generated_skill.py`; the plan does not re-run it (correctly — the scanner lives in jgs-reference-skill, not this repo, and pack bodies are untouched since Phase 3), but Task 7 records only the licence-sweep and capability-map residuals in STATE.md. The scanner residual should be recorded too so it survives into v1.18 planning. (Incorporates plan_check W6 as a record-only change.)
**Fix:** Add to Task 7's STATE.md residual list: "scan_generated_skill.py not re-run in Phase 5 (scanner external; packs unchanged since Phase 3 review)".

## plan_check findings disposition

| plan_check | Disposition here |
|---|---|
| W1 grep portability | Incorporated as MA-02 (must fix) |
| W2 gate stdout | Incorporated as MA-03 (must fix) |
| W3 chapter counts | Incorporated as MA-01 (must fix) |
| W4 7 tasks / 13 files | Accepted — do not split a release sequence; estimate within budget |
| W5 README table | Incorporated as MI-02 (recommended, non-blocking for SC1) |
| W6 scanner residual | Incorporated as MI-04 (record-only) |

## Verified non-issues (checked, not raised)

- Link policy cannot flag the draft's bare domain names (`cisa.gov, energy.gov, nde-ed.org, everyspec.com` in the Changed bullet): `tooling/check_release.py:47` requires an `https?://` prefix. The draft is gate-safe as written.
- Gate reads exactly three authorities (`check_release.py:102-116`); Task 1+2 split (CHANGELOG reserved for Task 2) keeps section 4 green at Task 5, not mid-flight.
- Task 1 ordering is correct: RELEASE-INFO first, then `gen_packs_page.py` regeneration — section 5c (`check_release.py:143-158`) regenerates via `gen_packs_page.version()` from RELEASE-INFO, so regen-before-bump would fail the drift check.
- All 11 surfaces verified at the plan's cited lines (plugin.json:4, cursor plugin.json:5, RELEASE-INFO:3-4, README:10/58/207, index.html:110/226, packs.html:86, YAMLs 15/13). Cursor manifest holds 55 entries — the draft's "55 eligible skills" is accurate.
- Explicit-path staging, the three untracked docs/ user files, and the `git status --short` audit all match the live tree; T-5-01 mitigation is real.
- Gate-before-tag hard stop (Task 5 / T-5-05) plus re-run immediately before commit (OneDrive, T-5-03) is present; reversibility rating is honest (edits reversible; tag/release pre-approved by REL-02 charter).
- Task 7 .planning-only commit after the tag matches convention (v1.16.3 sits on release commit 6ede444 with 61 later main commits, 46 touching .planning).
- PACK-SPEC body-order list confirmed at docs/PACK-SPEC.md:32-33 starting `## How to Use This Skill` — Task 3 insert point exists as described.
- `validate_pack.py` with no args walks every pack (live PASS), so Task 5's spot-check phrasing is harmless; the gate's section 5 already covers all packs.

## Required before execute

Apply MA-01, MA-02, MA-03 (small plan-text edits; MA-01 also pre-corrects the research draft counts). MI-01 through MI-04 are one-line plan edits recommended in the same pass. No task restructuring, no phase split, no scope change.

---
_Reviewer: ZCode (gsd plan-mode review) — 2026-08-14_

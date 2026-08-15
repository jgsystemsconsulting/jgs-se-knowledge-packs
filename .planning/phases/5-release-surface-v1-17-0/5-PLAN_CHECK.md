# Phase 5 Plan Check

**Phase:** 5-release-surface-v1-17-0
**Plans checked:** 1 (`5-01-PLAN.md`)
**Checked:** 2026-08-15
**Method:** Goal-backward verification against ROADMAP Phase 5 goal + SC1-SC2, REQUIREMENTS REL-01/REL-02, live `tooling/check_release.py` (section 4 / 5c / 6 / 6b), `CHANGELOG.md` house format, `5-RESEARCH.md`, and live measurements of the 11 version surfaces, pack/catalog/NOTICE state, tags, and `gh release view v1.16.3`.

**Verdict:** PASS_WITH_FIXES

The 7 tasks will deliver REL-01 (gate PASS on an already-registered 54/56 tree) and REL-02 (annotated tag + GitHub Release on origin) if the executor follows the actions. Version-surface coverage, release sequencing, explicit-path `git add`, and origin-tied REL-02 done-criteria are sound. Several verify / claim_verification statements will not measure what they claim -- fix those before execute if the verifier scores the written commands strictly. Do not treat this as a rewrite.

---

## Goal-backward trace

Phase goal: *Catalog, docs, installers, and release artifacts include the new packs.*

| Required truth | Covering task | Provably delivered? |
|---|---|---|
| REL-01: catalog.json / SKILLS.md / docs/packs.html / NOTICE include the 8 new packs; no drift; gate passes | Task 1 (packs.html regen) + Task 2 (CHANGELOG heading so section 4 agrees) + Task 5 (`check_release.py`) | **Yes for the remaining work.** Live tree already has all 8 slugs in catalog.json (54 packs), SKILLS.md (56 index links), NOTICE (`[pack: ...]` blocks), and packs.html content. Phase 5 still must bump the 11 version surfaces and regenerate packs.html so section 4 / 5c stay green after 1.17.0. Task 5 does not re-grep the 8 slugs in catalog/NOTICE/SKILLS -- it trusts Phase 3 + the gate. |
| REL-01 / SC1: `check_release.py` exits 0 at catalog basis 54 / directory basis 56 | Task 5 (and Task 2 full-gate run) | **Yes for exit 0.** Live `check_release.py` prints only `RELEASE CHECK: PASS -- repo is release-ready against the mechanical gate.` It never prints "54/56". The 54/56 state is real (54 catalog packs, 56 dirs, 2 signposts) but must be asserted by a separate count, not by grepping gate stdout. |
| REL-02 / SC2: v1.17.0 tagged and released | Task 6 | **Yes.** Sequence is gate then explicit-path commit then `git tag -a v1.17.0` then `git push origin main --follow-tags` then `gh release create`. Done is explicitly not met until `git ls-remote --tags origin` and `gh release view v1.17.0` both succeed. |
| REL-02: all packs pass `validate_pack.py` | Task 5 via full `check_release.py` section 5 (every non-signpost pack) + spot-check | **Yes.** Spot-check is extra; the gate already walks every pack. `validate_pack.py --help` is correctly not used (live tool treats `--help` as a pack path). |
| REL-02: all packs pass `scan_generated_skill.py` | none | **Not re-run.** Scanner lives in `jgs-reference-skill` (`REF/tools/scan_generated_skill.py`), not this repo. Phase 3 already scanned the 8 packs; this plan does not touch pack bodies. Residual, not a missing build. |
| All 11 version surfaces to 1.17.0 | Task 1 (10 surfaces) + Task 2 (CHANGELOG first heading) | **Yes.** Live grep of `1.16.3` (excl `.git` / `.planning` / `packs`) matches the research section 1 table exactly: plugin.json:4, cursor plugin.json:5, RELEASE-INFO:3-4, README:10/58/207, index.html:110/226, packs.html:86, two website YAMLs, plus CHANGELOG:12. Task 1 order (RELEASE-INFO then `gen_packs_page.py` then hand edits; CHANGELOG reserved for Task 2) matches gate section 4 + 5c. installers / marketplace.json correctly left untouched (no version field). |
| CHANGELOG heading house format, no em dash, no source-host URLs | Task 2 | **Yes for structure.** Draft in research section 2 matches live 1.16.x headings. Chapter-count correction is tasked but pointed at SKILLS.md rows, which have **no** `(N ch)` figures. Live `PACK.yaml` `build.chapters` / chapter files: 171=8, 61=6, cpg=5, sem=7, 338=9, 516=8, 7009=7, 413=6. |
| PACK-SPEC When to use + Prerequisites addendum (MI-02) | Task 3 | **Yes.** Live `docs/PACK-SPEC.md` body-order list still starts at `## How to Use This Skill` (line 33). Research section 3.1 block is the required insert. |
| README doe-413-3b series framing; no slug rename (MI-03) | Task 4 + Task 7 deferral record | **Yes, location fuzzy.** Live README has **zero** `doe-413` / `doe-sem` hits and the catalogue table still ends at `faa-rma` + planned `mit-ocw-se` (47 rows). Framing line is tasked; table rows are not. |
| Explicit-path `git add` (never `docs/` / `.` / `-A`) | Task 6 + threat T-5-01 | **Yes.** Names the three untracked files (`docs/ROLE-AGENTS-REQUIREMENTS-V2.md`, `docs/capability-pack-map.{md,json}`) and requires `git status --short` before commit. Live `git status --short` matches that set. |
| Release commit is last content commit; `.planning` follow-up is separate | Task 6 + Task 7 | **Yes.** |
| Post-release STATE / MILESTONES / ROADMAP + v1.18 doe-rename deferral + accepted residuals | Task 7 | **Yes.** Licence-string sweep skip (research 3.3) and user-owned map files (research 3.4) are recorded, not implemented. |

Requirements frontmatter: `[REL-01, REL-02]` -- both present. No ROADMAP requirement ID is missing from the plan.

---

## Dimension results

| Dim | Result | Notes |
|---|---|---|
| 1 Requirement coverage | PASS | REL-01 and REL-02 claimed and tasked. Catalog/NOTICE/SKILLS inclusion is already true live; Phase 5 owns version agreement + gate + tag/release. REL-02 scanner clause is a Phase 3 leftover, not a new pack-build. |
| 2 Task completeness | PASS | verify.plan-structure: 7 auto tasks, all have Files + Action + Verify + Done. Task 5 files element is empty (validation-only) -- acceptable. Actions are specific (paths, line numbers, command order). |
| 3 Dependencies | PASS | Single plan, depends_on empty, wave 1. Intra-plan order Task 1-7 is sequential and acyclic. Task 6 precondition requires Task 5 green + gh auth status. |
| 4 Key links | PASS | RELEASE-INFO to gen_packs_page.py to packs.html REV is in Task 1 action + must_haves.key_links. CHANGELOG body to gh release create --notes-file is in Task 6. Gate section 4 three-way agreement is created by Task 1+2 together. |
| 5 Scope sanity | WARN | 7 tasks (threshold 5+ normally split) and 13 files_modified (warn at 10). estimate-check --calibrated on 45000: budget 100000, ratio 0.45, over_budget false, confidence low (sample_count 0). Do not split: tagging from a half-bumped tree is worse than one sequential release plan. |
| 6 Verification derivation | WARN | must_haves truths are user-observable except check_release prints 54/56 (tool does not print that). Task 1 grep -v .planning/ does not drop Windows backslash paths (live: 54 hits). Task 2 chapter-count verify cannot succeed from SKILLS.md rows. |
| 7 Context compliance | SKIPPED | No CONTEXT.md (discuss skipped). |
| 7b Scope reduction | PASS | Licence sweep and doe slug rename are explicit research skip/defer, recorded in Task 7, not silent v1 stubs. README framing still delivers retain-slug / track 413.3C. |
| 7c Architectural tier | SKIPPED | No Architectural Responsibility Map in 5-RESEARCH.md. |
| 8 Nyquist | SKIPPED | No VALIDATION.md; nyquist_audit skipped in phase master_flow_state.json; RESEARCH has no Validation Architecture section. |
| 9 Cross-plan contracts | PASS | Single plan; no conflicting transforms. |
| 10 CLAUDE.md | SKIPPED | No ./CLAUDE.md. |
| 11 Research resolution | PASS | No Open Questions section. |
| 12 Pattern compliance | SKIPPED | No PATTERNS.md. |

---

## Targeted checks (orchestrator brief)

### 11 version surfaces tasked

All 11 research-section-1 surfaces are assigned:

| # | Surface | Task |
|---|---|---|
| 1 | .claude-plugin/plugin.json | 1 |
| 2 | CHANGELOG.md first heading | 2 (Task 1 correctly forbids touching it) |
| 3 | RELEASE-INFO.txt Version/Tag/Staged | 1 (edited first) |
| 4 | .cursor-plugin/plugin.json | 1 |
| 5-7 | README badge / line 58 / line 207 | 1 |
| 8 | docs/index.html REV x2 | 1 |
| 9 | docs/packs.html REV | 1 via python tooling/gen_packs_page.py (not hand-edit) |
| 10-11 | two docs/products/website/*.yaml | 1 |

Live 1.16.3 inventory matches that table. No 12th surface found in installers or marketplace.json.

### Grep-gate correctness

Intended truth is right; the written command is not portable.

Task 1 verify pipes grep -rn 1.16.3 into grep -v .planning/ and grep -v packs/. Live run of that exact pipeline still prints .planning backslash paths (MILESTONES, PROJECT, REQUIREMENTS, ROADMAP, Phase 3/5 planning files) because Windows grep emits backslashes. After a correct bump the command will false-fail and can send the executor into .planning edits that Task 1 does not own.

Fix: --exclude-dir=.git --exclude-dir=.planning --exclude-dir=packs, and treat CHANGELOG history lines as the only allowed hits. .git objects did not appear in the include-filtered grep; omitting --exclude-dir=.git is not the failure mode here.

### Release sequencing

Matches research section 4 and previous release commit 6ede444:

1. Tasks 1-4: surface + docs edits
2. Task 5: gen_packs_page.py idempotent, check_release.py PASS, validate_pack.py spot-check, re-run gate immediately before commit (OneDrive / T-5-03)
3. Task 6: explicit git add paths, release(v1.17.0) commit as last content commit, annotated tag, git push origin main --follow-tags, gh release create v1.17.0 --notes-file from CHANGELOG body
4. Task 6 verify: origin tag + gh release view + HEAD is the release commit
5. Task 7: .planning-only follow-up commit

Hard-stop on a red gate is written. gh release view v1.16.3 is a live precondition (name: v1.16.3 RR-S-13 compliance + browsable pack reference). Good.

Minor style nit: live annotated-tag messages are v1.16.3: summary (colon). Research + Task 6 use an em dash, which matches GitHub release titles, not the git tag subject. Either is releasable; claim_verification colon style is the more accurate tag analog.

### Explicit-path git add

Present in Task 6 action, done, threat T-5-01, and research risk 2. Three untracked docs files named. Task 7 also requires explicit .planning paths. This will prevent the IN-02 accident.

### REL-02 done-criteria

Tied to verifiable origin state, not a local tag. Action: REL-02 is NOT done until git ls-remote --tags origin v1.17.0 and gh release view v1.17.0 both succeed. Verify: git ls-remote --tags origin | grep v1.17.0 plus gh release view v1.17.0 --json name,tagName plus release commit is origin/main HEAD. Sufficient for SC2.

### claim_verification accuracy

| Claim | Live | Status |
|---|---|---|
| 11 surfaces at 1.16.3 | Exact match on the listed paths/lines | Accurate |
| Gate reads 3 authorities at check_release.py:102-116 | plugin.json / first CHANGELOG heading / RELEASE-INFO Version | Accurate |
| packs.html from RELEASE-INFO via gen_packs_page.version() | Confirmed | Accurate |
| v1.16.2 / v1.16.3 annotated, one-line vX.Y.Z: summary | git cat-file -t = tag; messages use colon | Accurate for tags; Task 6 then uses em dash |
| PACK-SPEC has no When to use | grep zero | Accurate |
| README has no doe-413 line | grep zero | Accurate |
| CHANGELOG first heading 1.16.3 dated 2026-06-26 | line 12 | Accurate |
| 3 untracked user files in docs/ | matches git status --short | Accurate |
| Repo publishes GitHub Releases | gh release view v1.16.3 succeeds | Accurate |
| Chapter counts from SKILLS.md rows | SKILLS.md rows have no chapter counts; PACK.yaml build.chapters does | Inaccurate -- Task 2 inherits this wrong source |

---

## Findings

### Warnings (should fix; execution can proceed)

**W1. [verification_derivation] Task 1 grep cannot exclude .planning/ on this Windows tree**
- Plan: 5-01 Task 1 verify
- Live: grep -v .planning/ still returns .planning backslash hits (54 total).
- Fix: grep -rn 1.16.3 --include filters --exclude-dir=.git --exclude-dir=.planning --exclude-dir=packs . and allow only CHANGELOG history lines.

**W2. [verification_derivation] Task 5 / must_haves claim check_release.py prints a 54/56 catalog basis**
- Plan: must_haves.truths[0], Task 5 verify / done
- Live: tooling/check_release.py:237 prints only RELEASE CHECK: PASS -- repo is release-ready against the mechanical gate. Pack/dir counts are not in stdout. Section 6 compares SKILLS entry count to non-signpost pack dirs; it does not print 54 or 56.
- Fix: keep RELEASE CHECK: PASS + exit 0, and add an explicit measurement: len(catalog[packs])==54, len(pack dirs)==56, SKILLS header 54 packs (+2 signposts).

**W3. [claim_verification / task_completeness] Task 2 chapter counts sourced from SKILLS.md rows**
- Plan: claim_verification last row + Task 2 action (read each of the 8 new packs SKILLS.md rows)
- Live: SKILLS.md descriptions have no (N ch); packs/*/PACK.yaml build.chapters and chapters/ file counts are 8/6/5/7/9/8/7/6. Research draft all-(8 ch) is wrong for 6 of 8 packs.
- Fix: read build.chapters (or ls packs/<slug>/chapters) before writing the CHANGELOG one-liners. Shipping 8 ch for cisa-cpg (5) / nist-800-61 (6) is a released-notes defect, not a gate failure.

**W4. [scope_sanity] 7 tasks / 13 files**
- Over the 2-3 task and 5-8 file targets. Estimate 45k/100k is inside budget (confidence low, uncalibrated). Do not split the release sequence.

**W5. [requirement_coverage] README catalogue table still omits the 8 packs**
- REL-01 names catalog.json / SKILLS.md / packs.html / NOTICE (already synced). The phase goal sentence also says docs include the new packs. README table (lines 108-156) still lists the v1.16.3 set; badge already says 54. Task 4 adds one framing line next to a DOE mention that does not exist.
- Fix (recommended, not required for SC1): add the 8 rows to the README table (or point the table at SKILLS.md only) so the framing line has a home. Not a blocker -- gated docs surfaces already include the packs; docs/index.html publisher groups already name them.

**W6. [requirement_coverage] REL-02 scanner clause not re-executed**
- scan_generated_skill.py is not in this repo; Phase 3 already reviewed all 8; this plan does not edit pack bodies. Accept as residual, or add an optional REF-path re-scan in Task 5.

### Non-issues (checked, not raised)

- All 11 surfaces tasked; CHANGELOG reserved for Task 2 so section 4 is not broken mid-Task-1.
- Sequence gate then commit then annotated tag then push --follow-tags then gh release create then origin verify.
- Explicit-path add + named untracked files + git status --short audit.
- REL-02 done waits on origin tag + GitHub Release, not a local-only tag.
- Task 7 .planning commit after the tag keeps the release tree clean.
- Licence-string sweep and doe slug rename are explicit skips/defers, not silent scope cuts.
- check_release.py section 6b cursor-manifest reconciliation is already in the tree (55 eligible skills); Task 1 only bumps the cursor version field, which is correct.
- No CONTEXT.md / CLAUDE.md / PATTERNS.md / VALIDATION.md / responsibility map -- those dimensions skipped, not failed.

---

## Structured issues

```yaml
issues:
  - dimension: verification_derivation
    severity: warning
    plan: "5-01"
    task: 1
    description: "Task 1 grep -v .planning/ does not exclude Windows .planning backslash paths; live command still lists planning files and will false-fail after a correct bump."
    fix_hint: "Use --exclude-dir=.git --exclude-dir=.planning --exclude-dir=packs; allow only CHANGELOG.md history hits."

  - dimension: verification_derivation
    severity: warning
    plan: "5-01"
    task: 5
    description: "must_haves and Task 5 verify require check_release.py to print catalog basis 54/56; live tool only prints RELEASE CHECK: PASS."
    fix_hint: "Assert exit 0 + PASS string; measure 54 catalog packs / 56 dirs / SKILLS header separately."

  - dimension: task_completeness
    severity: warning
    plan: "5-01"
    task: 2
    description: "Chapter-count correction is aimed at SKILLS.md rows, which have no counts. Live PACK.yaml build.chapters are 8/6/5/7/9/8/7/6, not all 8."
    fix_hint: "Read packs/<slug>/PACK.yaml build.chapters (or ls chapters/) before writing CHANGELOG one-liners."

  - dimension: scope_sanity
    severity: warning
    plan: "5-01"
    description: "7 tasks and 13 files exceed 2-3 / 5-8 targets. estimate 45000/100000, confidence low, not over budget."
    fix_hint: "Do not split. Keep one sequential release plan."

  - dimension: requirement_coverage
    severity: warning
    plan: "5-01"
    task: 4
    description: "README catalogue table still omits the 8 new packs; Task 4 framing line has no DOE row to sit next to. Gated REL-01 surfaces are already synced."
    fix_hint: "Optional: add 8 README table rows (or retarget the table) so docs match the 54-pack badge."

  - dimension: requirement_coverage
    severity: warning
    plan: "5-01"
    task: 5
    description: "REL-02 text includes scan_generated_skill.py; plan does not re-run it. Scanner is not in this repo; packs are unchanged since Phase 3."
    fix_hint: "Accept Phase 3 evidence, or add an optional REF/tools/scan_generated_skill.py spot-check."
```

---

## Recommendation

**Proceed to execute** after applying W1-W3 if the executor will treat verify blocks as literal (otherwise those three will false-fail or ship wrong CHANGELOG counts). W4-W6 do not block SC1/SC2.

Plans reduce 0 locked user decisions (no CONTEXT.md). No phase split required.

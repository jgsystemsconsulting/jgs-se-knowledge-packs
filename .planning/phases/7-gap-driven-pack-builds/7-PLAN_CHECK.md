# Phase 7 Plan Check

**Phase:** 7-gap-driven-pack-builds
**Plans checked:** 3 (`7-01-PLAN.md`, `7-02-PLAN.md`, `7-03-PLAN.md`)
**Checked:** 2026-08-16
**Method:** Goal-backward verification against ROADMAP Phase 7 goal + SC-1..SC-3, REQUIREMENTS GP-01..GP-07, `6-GAP_ANALYSIS.md` §Phase 7 Routing (P7-PRE-1..5), `7-RESEARCH.md` build sheets + registration table, `docs/PACK-SPEC.md`, live catalog/SKILLS/cursor/packs counts, and live re-measurement of every `claim_verification` numeric row.

**Verdict:** PASS_WITH_FIXES

The three waves will deliver GP-01..GP-07 as conforming packs and register them at 61 catalog / 62 cursor / 63 dirs if the executor follows the actions. Every P7-PRE obligation is a hard pre-generation gate in the covering task, not a note. Phase 9 version-surface work is explicitly excluded. Two verify blocks cannot measure what `<done>` claims (one is invalid bash). Fix those before execute if the verifier scores the written commands strictly. Do not treat this as a rewrite.

---

## Goal-backward trace

Phase goal: *7 public-domain packs (GP-01..GP-07) built, validated, and registered, fattening the empty + critical-thin clusters.*

| Success criterion | Required truth | Covering task | Provably delivered? |
|---|---|---|---|
| SC-1 — each pack conforms to PACK-SPEC; validate_pack + scan + overlap pass | 7 pack trees with required layout; three tools exit 0 | 7-01 T1–T4, 7-02 T1–T2, 7-03 T1 | **Yes in the actions.** Pipeline is the Phase 3 sequence plus the six research deltas. Each task runs validate/scan/overlap and forbids TODO stubs. |
| SC-2 — PACK.yaml provenance complete; no sources/ leaked; SKILL.md When-to-use + Prerequisites | edition/DIST-A/in-source notes; scoped commits; RR-S-13 headings | every pack task + leak `git show` | **Yes in the actions.** P7-PRE-1..5 are halt-and-surface gates before generate. Verify greps When-to-use / Prerequisites / no-TODO; leak check is per commit. |
| SC-3 — target clusters fattened (asserted in Phase 8) | Topic Index vocabulary now; baseline table captured for Phase 8 | pack generate steps + 7-03 T2 step 8 | **Yes as a Phase 7 obligation.** Cluster-25 vocabulary is a hard 7-02 T2 requirement. 7-03 copies the §5 table into SUMMARY. Actual re-score is Phase 8, matching ROADMAP. |
| P7-PRE-1 visual DIST-A (GP-05, GP-07) | visual cover check on the fetched copy, method recorded, halt if unseen | 7-02 T1, T2 | **Yes.** Explicitly not a text grep. 40051 scanned-cover case called out. |
| P7-PRE-2 dual in-source licence BEFORE generate (GP-06) | both A-94 and Army CBA pass in-source check or pack is rescoped/descoped | 7-01 T4 | **Yes.** Hard gate before chapter generation; halt-and-surface path is written. |
| P7-PRE-3 edition recording (GP-02, GP-03) | PACK.yaml version names the revision actually built | 7-01 T1, T2 | **Yes in the actions.** T1 verify greps `rev[ .]*[EF]`. T2 verify is looser (see W4). |
| P7-PRE-4 per-chapter DIST-A + provenance (GP-01) | each used chapter PDF checked; titles + retrieval date, no URLs | 7-03 T1 | **Yes in the action.** Verify only greps `retrieved` (see W2). |
| P7-PRE-5 in-copy rights re-confirm | statute-basis rows re-checked on the downloaded copy | 7-01 T1–T3; 7-02 via PRE-1; 7-03 via PRE-4 | **Yes in the actions.** DAFMAN halt if the releasability line is absent. T3 verify does not grep the line (see W4). |
| Registration 61 / 62 / 63 + check_release PASS | catalog 61, cursor 62 (sebok still out), dirs 63, SKILLS 61(+2), packs-61, 7 NOTICE blocks | 7-03 T2 | **Yes in the action.** Live arithmetic 54+7 / 55+7 / 56+7 is correct. Verify count assertions are right; NOTICE greps are not valid bash (W1). |
| No Phase 9 bleed | no CHANGELOG / plugin 1.18.0 / RELEASE-INFO bump | 7-03 T2 NOTE | **Yes.** Explicit exclusion. check_release version-agreement still holds at 1.17.0. |
| GP-08 / P7-FUT-1 / P7-BACKLOG out of scope | not built, not vetted here | — | **Yes.** No stretch NPR 7150.2 build. AAF spot-check and vet_source EXCLUDED-dict stay parked. |

Requirements frontmatter: `[GP-02, GP-03, GP-04, GP-06]` + `[GP-05, GP-07]` + `[GP-01]`. No ROADMAP requirement ID is missing from the plans.

`claim_verification` is present on all three plans. Numeric live rows match the tree today (see below).

---

## Dimension results

| Dim | Result | Notes |
|---|---|---|
| 1 Requirement coverage | PASS | GP-01..GP-07 each have a dedicated build task. PACK-SPEC layout + three validators are in every pack task. REL-1x version tag is correctly left to Phase 9; registration half of REL-1x-01 is 7-03 T2 (ROADMAP Phase 7 goal says "registered"). |
| 2 Task completeness | PASS with verify defects | `verify.plan-structure`: 8 auto tasks, all have Files + Action + Verify + Done. 7-03 T2 `<automated>` is not parseable as written (W1). 7-03 T1 verify path is not created by the action (W2). |
| 3 Dependencies | PASS | `7-01` wave 1 `depends_on: []`. `7-02` wave 2 `depends_on: ["7-01"]`. `7-03` wave 3 `depends_on: ["7-01","7-02"]`. Acyclic; no shared files across same-wave plans. Serializing B after A is conservative vs research "A cannot block B" — not a defect. |
| 4 Key links | PASS | SKILL.md chapter links → chapters/ via validate_pack. PACK.yaml pages ← metadata.json (summed for dual/chapter-wise). Registration surfaces → check_release + exact counts. Overlap ← work_dir full_texts (federal-bca both; GP-01 every chapter). |
| 5 Scope sanity | WARN | 7-01 has 4 tasks (warning threshold). All three `estimate.tokens` exceed the 100000 smart-zone (`150000` / `110000` / `120000`; `over_budget: true`; `confidence: low`, `sample_count: 0`). Do not split Wave A: same Phase 3 born-digital precedent; registration is already isolated in 7-03. |
| 6 Verification derivation | WARN | `must_haves` truths are user-observable. Several automated blocks cannot distinguish a conforming pack from a stub that greps (W1–W4). |
| 7 Context compliance | SKIPPED | No CONTEXT.md (discuss skipped). |
| 7b Scope reduction | PASS | No silent v1/static stubs. GP-08 is an explicit prior descope, not a plan cut. GP-06 halt-and-rescope is a recorded failure path, not a planned reduction. |
| 7c Architectural tier | SKIPPED | No Architectural Responsibility Map in `7-RESEARCH.md`. |
| 8 Nyquist | SKIPPED | No VALIDATION.md; `nyquist_audit` skipped in phase `master_flow_state.json`; RESEARCH has no Validation Architecture section. |
| 9 Cross-plan contracts | PASS | Packs are disjoint trees. Registration is a single late sweep. No conflicting transforms. 7-01/7-02 leave catalog at 54; only 7-03 writes it. |
| 10 CLAUDE.md | SKIPPED | No `./CLAUDE.md`. |
| 11 Research resolution | PASS | No Open Questions section. |
| 12 Pattern compliance | SKIPPED | No PATTERNS.md. Analog is Phase 3 3-01/3-03, cited in `<context>`. |

---

## Targeted checks (orchestrator brief)

### GP → task mapping

| Req | Slug | Plan / task | P7-PRE encoded as hard gate? |
|---|---|---|---|
| GP-01 | `dod-vva-rpg` | 7-03 T1 | P7-PRE-4 per-chapter DIST-A/authorship before the chapter enters the set; provenance titles + date, no URLs |
| GP-02 | `faa-std-025` | 7-01 T1 | P7-PRE-3 rev E/F + source; P7-PRE-5 in-PDF rights |
| GP-03 | `dote-te-guidebook` | 7-01 T2 | P7-PRE-3 8.02 vs v3-June; slug distinct from `dod-te-guidebook`; Scope & Limits cross-ref |
| GP-04 | `dafman-63-119` | 7-01 T3 | rendered fetch; P7-PRE-5 releasability line in the downloaded copy or halt |
| GP-05 | `mil-std-881f` | 7-02 T1 | fallback chain QuickSearch → GovTribe → labelled 881E; P7-PRE-1 visual DIST-A |
| GP-06 | `federal-bca` | 7-01 T4 | P7-PRE-2 both docs before generate; dual extract + dual overlap |
| GP-07 | `mil-std-40051` | 7-02 T2 | P7-PRE-1 scanned-cover visual DIST-A; chars/page ≥ 300; OCR contingency; plates skipped; cluster-25 vocabulary |

### Registration counts (live re-measure)

| Surface | Live now | Plan target | Status |
|---|---|---|---|
| `packs/` dirs | **56** | 63 | 56+7. 7-01 after-check 60 and 7-02 after-check 62 are consistent. |
| `catalog.json` packs | **54** | 61 | 54+7. Catalog includes `sebok`, excludes 2 signposts. |
| Signposts | 2 (`omg-signpost`, `se-standards-signpost`) | 2 | Unchanged. |
| `SKILLS.md` header | `54 packs (+2 signposts)` (line 9) | `61 packs (+2 signposts)` | Distinctive grep. |
| README badge | `packs-54` | `packs-61` | Distinctive grep. |
| `.cursor-plugin/plugin.json` skills | **55** (sebok absent; signposts present) | **62** | 55+7. Matches check_release eligible set (all SKILL.md dirs minus `commercial_use: false` = sebok only). |
| NOTICE `[pack:` blocks | existing PD pattern | +7 `[pack: <slug>]` | Action correct; verify broken (W1). |
| `docs/packs.html` | generated | `gen_packs_page.py` only | Correct (RR-B-00/30). |
| `check_release.py` | PASS on current tree | PASS on 61/63 basis | Tool does not hard-code 61/63; it diffs SKILLS vs non-signpost dirs and cursor vs commercial packs. |

`gen_skills_index.py` is absent (live). SKILLS.md hand-edit + keep disclaimer is correct.

### claim_verification accuracy (live re-run)

| Plan | Claim | Live | Status |
|---|---|---|---|
| 7-01 | 56 dirs / catalog 54 | 56 / 54 | Accurate |
| 7-01 | `dod-te-guidebook` exists | `packs/dod-te-guidebook/` | Accurate |
| 7-01 | tooling py files present | validate_pack, check_release, gen_packs_page, build_pack | Accurate |
| 7-02 | 881E-only everyspec / 40051 37.7 MB scanned DIST-A / DIST-A string | via 7-RESEARCH | Accepted as research-authoritative (no PDF re-fetch here) |
| 7-03 | "before this plan: 56 dirs / catalog 54 / SKILLS 54(+2) / packs-54 / cursor 55" | true **today**; false after 7-01+7-02 (dirs will be 62, catalog still 54) | **Label is pre-phase, not pre-7-03** (W5) |
| 7-03 | target 63 / 61 / 61(+2) / packs-61 / 62 | 56+7 / 54+7 / 55+7 | Accurate arithmetic |

### Verify commands -- false-pass / false-fail

| Task | Command problem | Effect |
|---|---|---|
| 7-03 T2 | NOTICE `grep -c ... = 1` (dod-vva-rpg and 40051) | Live bash: `grep: =: No such file or directory` (exit 2). **False-fail.** Only 2 of 7 slugs attempted. |
| 7-03 T1 | `for f in sources/dod-vva-rpg/chapter_fulltexts/*.txt` | Action never creates `chapter_fulltexts/`. It writes `work_dir_chN.txt` or a dir listing. **False-fail** unless the executor invents the path. |
| 7-03 T2 | catalog/cursor/dir counts are exact; SKILLS / packs-61 greps are distinctive | OK. |
| 7-03 T2 | no slug-set assert (Phase 3 3-03 had `new<=slugs`) | Count-only: 7 wrong slugs would still print 61. |
| 7-01 T2 | edition grep includes bare `2022` | `2022` alone satisfies P7-PRE-3 verify without naming the edition. |
| 7-01 T3 | no releasability grep | P7-PRE-5 is action-only. |
| 7-01 T4 | no rights/licence-evidence grep | P7-PRE-2 is action-only after the fact. |
| 7-02 T2 | `training|documentation` grep | Does not pin Topic Index / "Training & Documentation". |
| all pack tasks | chars/page >= 300 computed in the action, never asserted in automated | Floor can be skipped and verify still goes green. |
| all pack tasks | `git show HEAD` leak grep | Fine if the scoped commit landed as HEAD. |

### Phase 9 / stretch / companion sources

- CHANGELOG, `.cursor-plugin` version 1.17.0 to 1.18.0, RELEASE-INFO: forbidden in 7-03 T2. Not in `files_modified`. Good.
- GP-08 / NPR 7150.2 + NASA-STD-8739.8: not tasked. Correct (stretch, not a Phase 7 must).
- REQUIREMENTS GP-01 parenthetical (+ DoDM 5000.102) is not in 7-RESEARCH section 1 or 7-03 T1. Research build sheet is RPG chapter-wise only; 5000.102 is a separate gap-report cluster-8 candidate. Not raised as scope reduction.

---

## Findings

### Warnings (should fix; execution can proceed)

**W1. [verification_derivation] 7-03 Task 2 NOTICE greps are not valid bash**
- Plan: 7-03 Task 2
- Live: `grep -c "[pack: dod-vva-rpg]" NOTICE = 1` -> `grep: =: No such file or directory`.
- Fix: `test "$(grep -c '\[pack: dod-vva-rpg\]' NOTICE)" = "1"` (and the same for all 7 slugs), or one loop over the slug list. Do not leave `grep -c ... = 1` as a bare token.

**W2. [verification_derivation / key_links] 7-03 Task 1 overlap verify path is not produced by the action**
- Plan: 7-03 Task 1
- Action: per-chapter `work_dir_chN.txt` or a dir listing; optional concatenate into one overlap source.
- Verify: `sources/dod-vva-rpg/chapter_fulltexts/*.txt`.
- Fix: pick one layout in the action (recommend `chapter_fulltexts/*.txt` plus the concat file) and point both overlap runs and `<automated>` at it. Also grep PACK.yaml notes for more than `retrieved` (chapter titles).

**W3. [verification_derivation] chars/page floor is a hard gate in prose only**
- Plans: every pack task; especially 7-02 T2 (GP-07 / P7-PRE)
- Action + `<done>` require `len(full_text)/pages >= 300`. No `<automated>` measures it.
- Fix: add a one-liner per work_dir that asserts n>=300 on the selected body (and on each GP-01 / federal-bca extract).

**W4. [verification_derivation] several P7-PRE greps are too loose or missing**
- 7-01 T2: drop the bare `2022` alternative; require `8.02` or `v3-June`.
- 7-01 T3: grep the recorded releasability finding (`no releasability restrictions` or the halt path).
- 7-01 T4: grep PACK.yaml notes for in-source evidence on both documents (not just `A-94` + `Cost Benefit`).
- 7-02 T2: grep `Training & Documentation` (or the Topic Index heading), not `training|documentation`.
- 7-03 T2: add a slug-set assert mirroring 3-03 (`new<=slugs` for the seven GP slugs).

**W5. [claim_verification] 7-03 "before this plan" counts are pre-phase-7**
- Plan: 7-03 `claim_verification` first row
- After 7-01+7-02 the tree is 62 dirs / catalog 54. The target row (63/61/62) is the one execute needs. Live numbers today match the quoted 56/54/55.
- Fix: relabel the row "pre-Phase-7 / after Wave C" or restate before = 62 dirs / 54 catalog.

**W6. [scope_sanity] estimates over budget; 7-01 is 4 tasks**
- `estimate-check --calibrated`: 150k / 110k / 120k vs 100k; `confidence: low` (`sample_count: 0`).
- 4 tasks is the warning threshold, not the 5+ split line. Same Wave-A shape as 3-01.
- Fix: none required. Do not split. Treat estimates as uncalibrated.

### Non-issues (checked, not raised)

- GP-08 not built -- prior descope; stretch NPR/8739.8 is optional, not a must.
- P7-FUT-1 (AAF) and P7-BACKLOG (external vet_source dict) stay out.
- Phase 9 version surfaces untouched; check_release version triple stays 1.17.0.
- Catalog live objects omit share_alike / attribution_required; extra keys in new objects would not break the gate. Executor should copy a live Tier-1 object, not invent a schema.
- Chars/page floor 300 vs research ~>=200 for GP-07 is stricter, not a reduction.
- GP-07 chapter band 6-10 vs research 5-7 is guidance (research: counts are not gates).
- DoDM 5000.102 is a REQUIREMENTS parenthetical / gap-report companion, not a 7-RESEARCH build-sheet input.
- depends_on ["7-01"] matches the Phase 3 3-01 style.
- Signpost math: 63 dirs - 2 signposts = 61 SKILLS content packs; cursor 63 - 1 sebok = 62. Plan targets match check_release.py.
- No source URLs tasked into packs/ or NOTICE (Link Policy). Research URLs stay in .planning/.
- Cluster fattening itself is Phase 8 SC; Phase 7 correctly plants vocabulary + the baseline table.

---

## Plan-by-plan

### 7-01 -- Wave A born-digital (GP-02, GP-03, GP-04, GP-06)

Will achieve its slice. P7-PRE-2 is a real pre-generate stop, not a comment. P7-PRE-3/5 are in the first three tasks. Registration correctly deferred. Fix W3/W4 greps if the verifier is strict.

### 7-02 -- Wave B DoD fetches (GP-05, GP-07)

Will achieve its slice. Fallback chain + labelled 881E, scanned-cover visual DIST-A, page selection, OCR contingency, and cluster-25 vocabulary are all tasked before generate. Tighten the cluster-25 grep and add the chars/page assert (W3/W4).

### 7-03 -- Wave C GP-01 + registration

Will achieve GP-01 and close the phase if the executor follows the action, including inventing a consistent chapter-fulltext layout. Rewrite the NOTICE verify (W1) and lock the overlap path (W2) before execute. Count targets 61/62/63 are correct; do not bump 1.18.0 here.

## Re-check (post-remediation)

**Re-checked:** 2026-08-16 against `3ab4e9a` (`docs(7): plan_remediate — BL-01/02 + MA-01..03 + MI fixes`).
**Method:** re-read `7-01`/`7-02`/`7-03`-PLAN.md + `7-PLAN_REVIEW.md` + ROADMAP Phase 7 SCs; `bash -n` every `<automated>` via Git Bash (`C:\Program Files\Git\bin\bash.exe`); live re-measure catalog/cursor/`packs/` counts; pattern-test remediated greps against scaffold-title / licence-string false positives.

**Verdict:** FAIL

Both Wave-C BLOCKERs are gone and the bash now parses. The highest-risk pack's acceptance command still does not measure the selected-body floor the action and `<done>` require, and it hard-fails on the whole-file average the action just labelled informational. That is the same class of defect MA-01/MA-03 were written to close. Do not execute until the GP-07 verify asserts `chars(selected_body)/selected_pages >= 300`.

### Required confirms

| Check | Status |
|---|---|
| `bash -n` every `<automated>` block (8/8) | **CLEARED.** 7-01 T1–T4, 7-02 T1–T2, 7-03 T1–T2 all `OK`. |
| No tautological greps | **MOSTLY CLEARED.** Residual: 7-02 T2 `grep -Eqi "distribution statement\|DIST-A" packs/mil-std-40051/PACK.yaml` still matches the DIST-A licence string `build_pack.py` writes at scaffold. |
| GP-07 floor on selected body | **NOT CLEARED.** See open blocker. |
| All 8 builds measure chars/page | **7/8 CLEARED** at `c>=300` (faa-std-025, dote-te-guidebook, dafman-63-119, federal-bca ×2, mil-std-881f, dod-vva-rpg per `work_dir_ch*.txt`). 40051 measures whole-file `c>=200` and only greps the string `chars/page` in PACK.yaml. |
| Slug-set assert | **CLEARED.** 7-03 T2: `new<=slugs` over the seven GP slugs. |

### Per-finding status (from 7-PLAN_REVIEW.md)

| ID | Sev | Status | Evidence |
|---|---|---|---|
| BL-01 | BLOCKER | **CLEARED** | 7-03 T2 NOTICE check is now `for s in …; do grep -q "\[pack: $s\]" NOTICE \|\| { echo "MISSING $s"; exit 1; }; done`. `bash -n` OK. All 7 slugs covered. |
| BL-02 | BLOCKER | **CLEARED** | 7-03 T1 action step 4 now `mkdir -p sources/dod-vva-rpg/chapter_fulltexts` and copies `chNN.txt`. Verify glob and overlap loop share that path. `work_dir_ch*.txt` naming is also pinned for the chars/page loop. |
| MA-01 | MAJOR | **ACTION CLEARED / VERIFY NOT CLEARED** | Action order is now extract (informational whole-file) → select ~150 pp → floor `chars(selected_body)/selected_pages >= 300` → OCR only if that floor fails. Verify still computes `len(full_text)/metadata.pages` on the unselected extract and `sys.exit(0 if c>=200 else 1)`. |
| MA-02 | MAJOR | **MOSTLY CLEARED** | FAA rev grep no longer matches `reverse` (`rev[. ]*[EF]\b\|Rev [EF]`). DOT&E edition is `^source_version:.*(8\.02\|v3-June)` (bare `2022` dropped). 881 revision is `^source_version:.*881[EF]` (title no longer satisfies). DAFMAN releasability greps the downloaded `full_text.txt`. Cluster-25 is `Training & Documentation`. Slug-set assert added. Residual tautology: 40051 DIST-A grep on PACK.yaml. Residual gap: federal-bca still greps document identity in the two full_texts, not in-source licence notes. |
| MA-03 | MAJOR | **NOT CLEARED for GP-07** | Seven pack extracts now hard-assert `c>=300`. GP-07 does not assert selected-body `>=300`. |
| MI-01 | MINOR | **CLEARED** | 7-03 T2 step 1 bumps catalog `updated`. |
| MI-02 | MINOR | **CLEARED** | Catalog key list matches live objects; share_alike / attribution_required stay on PACK.yaml. |
| MI-03 | MINOR | **CLEARED** | Claim row relabelled pre-Phase-7 and states 62/54/55 at 7-03 start. |
| MI-04 | MINOR | **ACCEPTED** | Estimates still 150k/110k/120k vs 100k smart-zone; `confidence: low`, `sample_count: 0`. Do not split. |

Original PLAN_CHECK W1–W6 map 1:1 onto BL-01, BL-02, MA-03, MA-02, MI-03, MI-04. W1/W2/W5 cleared; W3/W4 residual as above; W6 unchanged.

### Open issues

**1. [verification_derivation] BLOCKER — 7-02 Task 2 verify does not measure the selected-body floor and can false-fail a correct GP-07 build**
- Plan: 7-02 Task 2
- Action steps 3–5: whole-file chars/page is informational only because "1168 pp of mostly image plates would drag it below the floor even on a healthy body"; the hard gate is `chars(selected_body)/selected_pages >= 300` after selection; OCR triggers only on that failure.
- `<done>` and must_haves: `chars/page floor >= 300 on the selected main-body extraction`.
- `<automated>`: greps `chars/page` anywhere in PACK.yaml (a notes line of `whole-file chars/page: 40 (informational)` satisfies it), then `sys.exit(0 if c>=200 else 1)` on `work_dir/book_skill_work/full_text.txt` — the unselected 1168-page extract. No selected-body path, no `>=300` assert.
- Effect: (a) a skipped selection still goes green if the whole-file average luckily clears 200; (b) a correct ~150 pp body at >=300 can fail verify when plates pull the whole-file average under 200, which the action itself predicts. That re-opens the gratuitous-OCR / false-halt path MA-01 was written to close.
- Fix: persist the selected body (or record `selected_chars` + `selected_pages` in PACK.yaml notes) and assert `selected_chars/selected_pages >= 300` in `<automated>`. Drop the whole-file `c>=200` hard exit, or keep it print-only. Presence-grep of `chars/page` is not a floor.

**2. [verification_derivation] WARNING — 7-02 T2 DIST-A grep still matches the scaffold licence string**
- Plan: 7-02 Task 2
- `grep -Eqi "distribution statement|DIST-A" packs/mil-std-40051/PACK.yaml` is true the moment `build_pack.py` writes the DIST-A licence variant. It cannot fail if the P7-PRE-1 visual-confirmation note is missing.
- Fix: grep the notes for the confirmation method (`visual(ly)? confirm` or equivalent), not the licence field.

Federal-bca P7-PRE-2 notes are still action-only (identity greps on the two full_texts). Not re-raised as a new issue; leftover MA-02 residue, not a phase-goal block.

### What is newly sound

- All 8 `<automated>` blocks parse (`bash -n` OK). No `grep -c … = 1` word-split. No `2>/dev/null \|\| echo` comparison swallow.
- `chapter_fulltexts/` is produced by the action that the verify glob consumes.
- Registration arithmetic unchanged and still correct against live 56/54/55 and check_release.py (targets 63/61/62, packs-61, sebok still out).
- Wave graph still acyclic; Phase 9 version surfaces still excluded; GP-08 / P7-FUT-1 / P7-BACKLOG still absent.

### Structured issues

```yaml
issues:
  - plan: "7-02"
    dimension: verification_derivation
    severity: blocker
    task: 2
    description: "GP-07 <automated> hard-exits on whole-file chars/page >=200 and never asserts selected-body >=300, contradicting the remediated action/must_haves/<done>"
    fix_hint: "Assert chars(selected_body)/selected_pages >= 300 from a persisted selected extract or recorded selected_chars/selected_pages; do not sys.exit on the informational whole-file average"
  - plan: "7-02"
    dimension: verification_derivation
    severity: warning
    task: 2
    description: "DIST-A grep on PACK.yaml is satisfied by the scaffold licence string"
    fix_hint: "Grep PACK.yaml notes for the visual-confirmation method/finding, not distribution statement|DIST-A"
```


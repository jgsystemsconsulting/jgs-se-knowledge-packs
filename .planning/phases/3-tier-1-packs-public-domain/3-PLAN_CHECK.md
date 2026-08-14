# Phase 3 Plan Check

**Phase:** 3-tier-1-packs-public-domain
**Plans checked:** 3 (`3-01-PLAN.md`, `3-02-PLAN.md`, `3-03-PLAN.md`)
**Checked:** 2026-08-14
**Method:** Goal-backward verification against ROADMAP Phase 3 goal + SC1-SC3, REQUIREMENTS T1-01..T1-08, `docs/PACK-SPEC.md`, live `tooling/validate_pack.py` / `tooling/check_release.py` / `tooling/gen_packs_page.py`, `3-RESEARCH.md` pipeline, and P3-PRE-1/P3-PRE-2.

**Verdict:** FAIL

The eight pack-build tasks map T1-01..T1-08 onto the research pipeline and can produce PACK-SPEC trees that pass `validate_pack.py`. The planned closing gate cannot. 3-03 Task 3 as written edits the wrong catalog file, emits SKILLS.md rows the live parsers will not see, and calls `check_release.py` against SKILL.md bodies the generation steps were never told to write. Fix before execute; do not treat this as a proceed-with-nits check.

---

## Goal-backward trace

Phase goal: *8 public-domain packs built and validated.*

| Required truth | Covering task | Provably delivered? |
|---|---|---|
| T1-01 `nist-800-171` conforming pack | 3-01 Task 1 | Yes for PACK-SPEC + `validate_pack.py`. Provenance fill is tasked; not enforced by the validator (nested `build:` keys). |
| T1-02 `nist-800-61` | 3-01 Task 2 | Same. |
| T1-03 `mil-hdbk-338` with Part-2 chapter selection | 3-02 Task 1 | Action specifies 8-10 selected chapters and skip-annex. Verify only counts `ls chapters` -- does not assert the selection. |
| T1-04 `mil-hdbk-516` | 3-02 Task 2 | Yes at action/done level. |
| T1-05 `nasa-ms-7009` two-PDF one-pack | 3-03 Task 1 | Action covers two extracts + summed `source_pages` + overlap twice. Verify is `validate_pack` + grep-c 43. |
| T1-06 `doe-413-3b` consolidated Chg 7 | 3-03 Task 2 | Yes at action/done level. |
| T1-07 `cisa-cpg` + P3-PRE-1 statute licence | 3-01 Task 3 | Yes. Exact string Public Domain (US Government work, 17 U.S.C. section 105) is mandatory in vet and build_pack. Live vet_source.py has no cisa in US_GOV; PD_LICENSE includes public domain and 17 u.s.c. |
| T1-08 `doe-sem` + in-PDF third-party check + P3-PRE-2 record | 3-01 Task 4 | Yes. P3-PRE-2 accepted-gap text is tasked into 3-01 SUMMARY. |
| SC1 PACK-SPEC + validate_pack.py | every pack task | Yes. Live validator checks required files, frontmatter name/description, chapter-link resolve, PACK.yaml slug/title/publisher/license/license_tier/commercial_use. It does not take --help (treats it as a pack path) and does not check source_pages / chapters / built_on. |
| SC2 scan_generated_skill.py reviewed | every pack action | Tasked in actions + must_haves. No automated verify runs the scanner. |
| SC3 PACK.yaml provenance (tier, licence, pages, chapters, built_on) | every pack action/done | Tasked. Not mechanically verified (nested YAML). |
| No source PDF / full_text.txt committed | every pack action | Yes. sources/ and *.full_text.txt are gitignored (live .gitignore lines 13, 17). |
| Registration once (catalog / SKILLS.md / packs.html / NOTICE / check_release) | 3-03 Task 3 only | **No.** Path, row syntax, and SKILL heading contract are wrong vs the live tree. See B1. |
| P3-PRE-1 cisa statute string | 3-01 Task 3 | Yes. |
| P3-PRE-2 accepted gap (no Phase 3 build depends on it) | 3-01 Task 4 | Yes (record-only, as research recommended). |

Requirements frontmatter coverage: T1-01, T1-02, T1-07, T1-08 in 3-01; T1-03, T1-04 in 3-02; T1-05, T1-06 in 3-03. None missing from all plans.

claim_verification present on all three plans. Pipeline-order / licence-string / gitignore claims match live tools and .gitignore. Catalog path is not claimed; 3-03 invented packs/catalog.json.

---

## Dimension results

| Dim | Result | Notes |
|---|---|---|
| 1 Requirement coverage | PASS | All eight T1 IDs claimed and tasked. REL-01 pulled forward into 3-03 is extra, not a coverage gap. |
| 2 Task completeness | PASS | verify.plan-structure: 3-01 4 tasks, 3-02 2, 3-03 3; all auto with Files + Action + Verify + Done. |
| 3 Dependencies | PASS | 3-01/3-02 wave 1, depends_on empty. 3-03 wave 2, depends_on [3-01, 3-02]. Acyclic. No shared pack dirs across plans. Registration files only in 3-03. |
| 4 Key links | FAIL | 3-03 Task 3 wires catalog / SKILLS / packs.html / NOTICE / check_release, but to the wrong catalog path and an unparseable SKILLS row shape. Pack generation is not wired to the ## When to use + Prerequisites contract check_release.py actually enforces. |
| 5 Scope sanity | WARN | 3-01 has 4 tasks (warning threshold) and ~40 generated files. All three plans over the 100k smart-zone (140k/120k/120k, over_budget true, confidence low, sample_count 0). Over-budget is never a blocker. Research-justified 3-batch split is the right shape; do not split to 8 plans for this warning. |
| 6 Verification derivation | WARN | Several automated blocks do not test the corresponding done criteria (overlap/scan/provenance/chapter-selection). REF / TMPxxx are undefined in verify shells. grep-c 43 and inverted sources/ greps can false-pass. |
| 7 Context compliance | SKIPPED | No CONTEXT.md (discuss skipped). |
| 7b Scope reduction | PASS | No silent v1/static/hardcoded reduction of T1 decisions. P3-PRE-2 is an explicit accepted gap per research section 7. |
| 7c Architectural tier | SKIPPED | No Architectural Responsibility Map in 3-RESEARCH.md. |
| 8 Nyquist | SKIPPED | No Validation Architecture section; nyquist_audit skipped in master_flow. |
| 9 Cross-plan contracts | PASS | Shared pipeline is identical; no conflicting transforms. Registration is single-writer in 3-03. |
| 10 CLAUDE.md | SKIPPED | No ./CLAUDE.md. |
| 11 Research resolution | PASS | No Open Questions section. |
| 12 Pattern compliance | SKIPPED | No PATTERNS.md. |

---

## Findings per plan

### 3-01-PLAN.md -- Batch A (T1-01, T1-02, T1-07, T1-08)

**What works.** Pipeline command order and flags match 3-RESEARCH.md section 2 and live --help on vet_source.py, extract.py, outline.py, REF/tools/build_pack.py, check_overlap.py, scan_generated_skill.py. Uses python not python3. P3-PRE-1 is explicit and correct against live US_GOV / PD_LICENSE. P3-PRE-2 is record-only. Registration correctly deferred. One commit per pack; sources/ stays gitignored. claim_verification present.

**Gaps.** Task 1 verify does not run check_overlap.py even though done requires exit 0. Tasks 2/4 overlap verifies depend on undefined REF / TMP800_61 / TMPSEM. No task tells the generator to write ## When to use + a Prerequisites marker (live 48/48 packs have both; check_release.py rr-s-13 requires both). 4 tasks / large generated-file set / 140k estimate.

### 3-02-PLAN.md -- Batch B (T1-03, T1-04)

**What works.** Same pipeline. Distribution Statement A licence string is the research-exact variant. Mirror-then-verify-DIST-A and OCR-then-record contingencies are tasked. Chapter-selection rule for 338 is in the action. Wave 1 isolation from Batch A is correct. claim_verification present.

**Gaps.** Task 1 verify is validate_pack && ls chapters | wc -l -- does not assert 8-10, does not run overlap, does not check DIST-A on PACK.yaml/LICENSE. Task 2 overlap verify uses undefined REF / TMP516. Same missing ## When to use generation step.

### 3-03-PLAN.md -- Batch C (T1-05, T1-06) + registration

**What works.** Two-PDF nasa-ms-7009 variation (two extracts, one pack, summed pages, overlap twice) matches research section 6 risk 7. doe-413-3b uses the consolidated Chg 7 path and the in-PDF third-party check. depends_on [3-01, 3-02] is consistent. Registration is consolidated once here, not repeated in 3-01/3-02. claim_verification present.

**Gaps that fail the task.** See B1. Also: Task 1 verify grep-c 43 is not a two-source proof; Task 2 overlap verify uses undefined TMP413.

---

## Blockers (must fix)

**B1. [key_links_planned] 3-03 Task 3 cannot deliver the registration sweep or check_release.py PASS as written**
- Plan: 3-03 / Task 3 (and pack-generation actions in 3-01, 3-02, 3-03 Tasks 1-2)
- Live facts (measured 2026-08-14):
  - Catalog is repo-root catalog.json (46 live entries; 42 license_tier==1). packs/catalog.json does not exist. tooling/check_release.py REQUIRED_FILES lists catalog.json, not packs/catalog.json. README/CONTRIBUTING point at root catalog.json.
  - SKILLS.md rows are of the form pipe + bracket-backtick-slug-backtick + (packs/slug/SKILL.md). gen_packs_page.parse_skills and check_release index regex both require the backtick form. Plan action writes pipe + [slug](packs/<slug>/SKILL.md) without backticks -- those rows are invisible to both parsers.
  - check_release.py rr-s-13 requires ## When to use and a Prerequisites/Requirements/compatibility marker. Live packs: 48/48 have both. PACK-SPEC and every generation action omit them. After eight new packs, Task 3 python tooling/check_release.py fails even if catalog/SKILLS were correct.
  - Task 3 verify json.load(open("packs/catalog.json")) FileNotFoundErrors on the live tree. check_release.py does not read catalog contents, so a newly created packs/catalog.json would leave root catalog.json stale (Phase 5 54/56 basis never updates).
- Fix:
  1. Change files_modified, Task 3 files, action, verify, artifacts, and key_links to root catalog.json.
  2. Prescribe the live SKILLS.md row with backtick slug and header 54 packs (+2 signposts).
  3. Add to every pack generate step (3-01 T1-T4, 3-02 T1-T2, 3-03 T1-T2): write ## When to use plus a **Prerequisites:** line, matching packs/nist-csf/SKILL.md.
  4. Point Task 3 verify at catalog.json and assert the eight slugs plus check_release.py exit 0.

---

## Warnings (should fix)

**W1. [verification_derivation] Overlap / scan / provenance not in several automated blocks**
- 3-01 Task 1 verify: validate_pack + git show only. done requires check_overlap.py exit 0 and scan disposition.
- 3-02 Task 1 verify: no overlap, no DIST-A string, no 8-10 chapter assert.
- 3-03 Task 1 verify: no dual overlap.
- No plan runs scan_generated_skill.py in verify (SC2 is review-only).
- validate_pack.py cannot see nested build.source_pages / chapters / built_on -- SC3 needs an explicit grep/parse of those keys.
- Fix: add the overlap command (with a captured temp path written to a known file under sources/<slug>/), a scan_generated_skill.py run, and a PACK.yaml key check to each pack verify.

**W2. [verification_derivation] Undefined REF / TMPxxx in verify shells**
- 3-01 Tasks 2/4, 3-02 Task 2, 3-03 Task 2 reference REF, TMP800_61, TMPSEM, TMP516, TMP413. Actions say capture %TEMP% but never export those names. A fresh verify shell fails.
- Fix: write the printed book_skill_work path to sources/<slug>/work_dir.txt during extract; verify reads that file. Hardcode REF=C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill in each verify, or use the same assignment as the action.

**W3. [verification_derivation] Weak / inverted greps**
- 3-01 Task 1: git show --stat HEAD | grep -v -c sources/ counts lines that are not sources/ and is non-zero for any normal pack commit -- it does not fail a stray sources/ path.
- 3-03 Task 1: grep -c 43 matches any incidental 43.
- Fix: git show --name-only --pretty=format: HEAD must have zero sources/ or full_text.txt paths. For nasa, grep a distinctive two-source note in PACK.yaml, not 43.

**W4. [scope_sanity] Token estimates over budget; 3-01 at 4 tasks**
- estimate-check --calibrated: 3-01 140000 / 100000 (1.40x); 3-02 120000 (1.20x); 3-03 120000 (1.20x). confidence low (0 completed-phase actuals). 3-01 task count = 4 (warning). File counts are large because each pack is ~10 generated markdown files -- expected, not a split-to-8-plans case.
- Fix: none required for execution. If a run blows context, split Batch A into 2+2 after the first pack proves the pipeline.

**W5. [task_completeness] 3-01 Task 1 git show verify assumes the pack commit is already HEAD**
- Action says commit at the end. If the executor verifies before commit, or another commit landed, the stat check is meaningless.
- Fix: verify the working tree / named path, then commit, or git log -1 --name-only after the commit step only.

---

## Info

**I1.** python tooling/validate_pack.py --help is not a help interface -- it treats --help as a pack directory and prints FAIL --help. Plans correctly invoke python tooling/validate_pack.py packs/<slug>.

**I2.** depends_on [3-01, 3-02] uses prefixed ids while frontmatter plan is 01/02. Human-readable and acyclic; confirm the executor resolves them.

**I3.** check_release.py does not validate catalog membership. Even a correct root catalog.json edit is not proven by check_release.py alone -- Task 3 must keep an explicit slug assert.

**I4.** SOURCE_HOSTS in check_release.py do not include cisa.gov / energy.gov / nde-ed.org. The no-URL rule in pack actions is what blocks those hosts; do not drop it.

**I5.** Dimension 8 Nyquist, 7 context, 7c tier map, 10 CLAUDE.md, 12 PATTERNS: skipped (absent artifacts / nyquist disabled).

---

## Structured issues

```yaml
issues:
  - plan: "3-03"
    dimension: key_links_planned
    severity: blocker
    task: 3
    description: "Registration sweep targets packs/catalog.json (does not exist; live catalog is repo-root catalog.json), writes SKILLS.md rows without the backtick slug form gen_packs_page.py and check_release.py parse, and requires check_release.py PASS while no pack-generation task writes the ## When to use + Prerequisites heading that check_release rr-s-13 enforces on 48/48 existing packs."
    fix_hint: "Edit catalog.json at repo root; use backtick slug SKILLS.md rows and header 54 packs (+2 signposts); add ## When to use + Prerequisites to every pack SKILL.md generate step; point Task 3 verify at catalog.json and the eight slugs."
  - plan: "3-01"
    dimension: verification_derivation
    severity: warning
    task: 1
    description: "Task 1 verify omits check_overlap.py / scan_generated_skill.py / PACK.yaml provenance keys required by done and SC2/SC3. git show | grep -v -c sources/ cannot fail a leaked sources/ path."
    fix_hint: "Run overlap + scan; grep license_tier/source_pages/built_on; assert git show name-only has zero sources/ or full_text.txt paths."
  - plan: "3-01"
    dimension: verification_derivation
    severity: warning
    task: 2
    description: "Tasks 2 and 4 (and 3-02 T2 / 3-03 T2) call check_overlap via undefined REF / TMPxxx in the verify shell."
    fix_hint: "Persist the extract work-dir path under sources/<slug>/ and inline REF= in each automated block."
  - plan: "3-02"
    dimension: verification_derivation
    severity: warning
    task: 1
    description: "Task 1 verify does not assert 8-10 selected chapters, DIST-A licence string, or overlap exit 0."
    fix_hint: "Count chapters in 8-10; grep Distribution Statement A in PACK.yaml/LICENSE; run check_overlap."
  - plan: "3-03"
    dimension: verification_derivation
    severity: warning
    task: 1
    description: "grep -c 43 on SKILL.md does not prove two-PDF build, summed source_pages, or dual overlap."
    fix_hint: "Assert PACK.yaml notes record STD+HDBK and source_pages = sum; run check_overlap twice."
  - plan: "3-01"
    dimension: scope_sanity
    severity: warning
    description: "3-01 has 4 tasks and estimate 140k/100k (1.40x); 3-02 and 3-03 are 120k/100k. confidence=low (sample_count=0). Over-budget is advisory only."
    fix_hint: "Keep the 3-batch split. If Batch A blows context, cut to 2+2 after the nist-800-171 reference run."
```

---

## Recommendation

1 blocker. 5 warnings. Verdict **FAIL**.

Highest-leverage revision (same 3 plans, no re-batch): retarget 3-03 Task 3 at root catalog.json; copy the live SKILLS.md backtick row + 54 packs (+2 signposts) header; add ## When to use + Prerequisites to every pack generate action so check_release.py can actually pass. Tighten pack verifies so overlap, scan disposition, and nested PACK.yaml provenance are measured, not only claimed in done.

Do not execute 3-03 Task 3 until B1 is revised. Pack-build tasks may be executed only after the When-to-use generate step is added; otherwise the closing gate is guaranteed red.

**Verdict:** FAIL

---

## Re-check (post-remediation)

**Checked:** 2026-08-14 (plans as of `ffc3caf`)
**Method:** Goal-backward re-verification of each original finding against the remediated `3-01`/`3-02`/`3-03` plans, live `catalog.json` (46 packs, 42 `license_tier==1`), live `SKILLS.md` line 18 / header, and `tooling/check_release.py` rr-s-13 + index regex / `tooling/gen_packs_page.parse_skills`.

**Verdict:** PASS_WITH_FIXES

B1 is gone. The registration sweep now targets repo-root `catalog.json`, writes the live backtick-slug SKILLS row, and the eight pack generate steps write the rr-s-13 `## When to use` + `**Prerequisites:**` contract that `check_release.py` actually enforces. No new blockers. Two original warnings remain as residual verify-quality nits; they do not stop execution.

Live measurements used:

- `catalog.json` exists at repo root; `packs/catalog.json` does not. 46 entries, 42 tier-1. Entry shape: `slug, title, publisher, source_version, license, license_tier, commercial_use, chapters, status`.
- `SKILLS.md` header: `46 packs (+2 signposts)`. Row 18 (nist-csf) is the live backtick form required by both `parse_skills` and the check_release index regex.
- rr-s-13 (`tooling/check_release.py` lines 131-141): heading `## When to use` plus a Prerequisites/Requirements/compatibility marker. Live `packs/nist-csf/SKILL.md` has `## When to use` immediately followed by a `**Prerequisites:**` line.
- Pack dirs today: 48 (46 content + 2 signposts). After +8: catalog 54 / directory 56. Tier-1: 42+8=50.

### Per-finding status

| ID | Original | Status | Evidence |
|---|---|---|---|
| B1 catalog path | 3-03 Task 3 edited `packs/catalog.json` | **CLEARED** | `files_modified`, Task 3 files, action, verify, artifacts, and key_links all use repo-root `catalog.json`. Action forbids creating `packs/catalog.json`. Verify is `json.load(open('catalog.json'))`. |
| B1 SKILLS row form | `[slug](packs/<slug>/SKILL.md)` without backticks | **CLEARED** | Action prescribes the live backtick-slug row and tells the executor to copy a live row (nist-csf). Task 3 verify greps the eight slugs in backtick form. Header bump `46 packs (+2 signposts)` to `54 packs (+2 signposts)` is explicit. Sample row parses in both live parsers. |
| B1 When-to-use + Prerequisites | omitted from every generate step; `check_release.py` would fail | **CLEARED** | Mandatory contract in 3-01 T1 (reference) and restated in 3-01 T2/T3/T4, 3-02 T1/T2, 3-03 T1/T2. Every pack verify greps `## When to use` and `**Prerequisites:**`. Task 3 then runs `python tooling/check_release.py`. |
| B1 catalog math / slug assert | verify pointed at missing file; no 8-slug proof | **CLEARED** | Asserts the eight new slugs, `len(c['packs'])==54`, and 50 tier-1 entries. 46+8=54 and 42+8=50 match live counts. |
| W1 overlap / scan / provenance | several pack verifies omitted overlap/scan; no dual overlap; no DIST-A / 8-10 | **CLEARED** for overlap/scan/DIST-A/8-10/dual. **Residual:** nested `source_pages` / `built_on` / `license_tier` still not grepped -- only `! grep -q TODO`. | All eight pack verifies run `check_overlap.py` with a persisted work-dir path (cisa + nasa run it twice). All eight run `scan_generated_skill.py`. 3-02 T1 asserts chapter count in 8-10 and greps `Distribution Statement A` in PACK.yaml and LICENSE. 3-02 T2 same DIST-A greps. |
| W2 undefined REF / TMPxxx | verify shells referenced unset REF / TMP800_61 / TMPSEM / TMP516 / TMP413 | **CLEARED** | Those TMP names are gone. Every pack verify starts with a hardcoded `REF=` path and reads `sources/<slug>/work_dir.txt` (or the two-file variant). Actions persist those paths at extract time. |
| W3 weak / inverted greps | inverted `git show` sources count; `grep -c 43` incidental | **CLEARED** | 3-01 T1 now requires zero `sources/` or `full_text.txt` paths on `git show --name-only --pretty=format: HEAD`. 3-03 T1 replaced `grep -c 43` with greps for `STD-7009B` and `HDBK-7009B` on PACK.yaml. |
| W4 scope / estimates | 3-01 has 4 tasks; 140k/120k/120k over 100k smart-zone; confidence low | **STILL OPEN (advisory)** | Unchanged and still not a blocker (ADR-2629). `estimate-check --calibrated`: 3-01 140000/100000 (1.40x), 3-02 and 3-03 120000 (1.20x), confidence=low, sample_count=0. Keep the 3-batch split. |
| W5 3-01 T1 git show HEAD | verify assumes the pack commit is already HEAD | **STILL OPEN (warning)** | Action still commits at step 8; verify still reads HEAD. If verify runs before the commit, or another commit landed, the sources/ leak check is meaningless. Other pack verifies never added this check. |

### New issues introduced by the remediation?

None that block the phase goal.

Checked and discarded:

- `packs/catalog.json` appears only as a do-not-create warning in 3-03 Task 3.
- The only `tmp` hit is NASA's `system/files/tmp/` download path, not a shell var.
- Task 3 SKILLS grep of the eight-slug alternation exits 0 on any match (does not assert count==8). `check_release.py` still compares SKILLS non-signpost rows to shipped pack dirs, so a short SKILLS table fails the closing gate. Not a new blocker.
- NASA verify still does not assert `source_pages = STD+HDBK` numerically; it asserts both source names. Covered by done-criteria plus the residual W1 provenance note.

### Dimension roll-up (re-check)

| Dim | Result | Notes |
|---|---|---|
| 1 Requirement coverage | PASS | T1-01..T1-08 still claimed and tasked. |
| 2 Task completeness | PASS | `verify.plan-structure`: 3-01 4 / 3-02 2 / 3-03 3; all auto with Files+Action+Verify+Done. |
| 3 Dependencies | PASS | Unchanged: 3-01/3-02 wave 1; 3-03 wave 2 depends_on [3-01, 3-02]. |
| 4 Key links | PASS | Registration now wires root `catalog.json`, live SKILLS row shape, packs.html via `gen_packs_page.py`, NOTICE, and `check_release.py`. Generate steps are wired to rr-s-13. |
| 5 Scope sanity | WARN | Same as W4. Over-budget is advisory. |
| 6 Verification derivation | WARN | Residual: nested PACK.yaml provenance keys not parsed; 3-01 T1 HEAD leak-check ordering (W5). Overlap/scan/When-to-use/DIST-A/chapter-count/catalog math now measured. |
| 7 / 7b / 7c | SKIPPED / PASS / SKIPPED | No CONTEXT.md. No silent scope reduction. No responsibility map. |
| 8 Nyquist | SKIPPED | No Validation Architecture; no VALIDATION.md. |
| 9 Cross-plan contracts | PASS | Unchanged shared pipeline; single-writer registration. |
| 10 CLAUDE.md | SKIPPED | No ./CLAUDE.md. |
| 11 Research resolution | PASS | No Open Questions section. |
| 12 Pattern compliance | SKIPPED | No PATTERNS.md. |

### Residual (do not block execute)

1. **W4** -- token estimates over the 100k smart-zone; 3-01 at 4 tasks. If Batch A blows context, split 2+2 after the nist-800-171 reference run.
2. **W5** -- 3-01 Task 1 leak check should inspect the named pack commit / working tree, not assume HEAD. Optional: add the same name-only leak check to the other seven pack verifies.
3. **W1 residual** -- pack verifies still do not parse nested `license_tier` / `source_pages` / `built_on`. TODO-absence is the only mechanical provenance check; a one-line YAML parse would make SC3 mechanical.

### Structured issues (open after re-check)

```yaml
issues:
  - plan: "3-01"
    dimension: scope_sanity
    severity: warning
    description: "Unchanged: 3-01 has 4 tasks and estimate 140k/100k (1.40x); 3-02 and 3-03 are 120k/100k. confidence=low (sample_count=0). Over-budget is advisory only."
    fix_hint: "Keep the 3-batch split. If Batch A blows context, cut to 2+2 after the nist-800-171 reference run."
  - plan: "3-01"
    dimension: task_completeness
    severity: warning
    task: 1
    description: "Task 1 verify still uses git show HEAD for the sources/ leak check, which is meaningless if verify runs before the pack commit or HEAD has moved."
    fix_hint: "Verify the working tree / named path, then commit; or git log -1 --name-only after the commit step only."
  - plan: "3-01"
    dimension: verification_derivation
    severity: warning
    description: "Pack verifies still do not parse nested PACK.yaml license_tier / source_pages / built_on (SC3). TODO-absence is the only mechanical provenance check."
    fix_hint: "Optional: grep or python-parse those keys in each pack verify."
```

**Verdict:** PASS_WITH_FIXES

# Phase 7 Plan Review (plan-mode)

**Plans reviewed:** 7-01-PLAN.md, 7-02-PLAN.md, 7-03-PLAN.md
**Reviewed:** 2026-08-14
**Against:** .planning/ROADMAP.md Phase 7 (goal + SC-1..SC-3, GP-01..GP-07), 7-RESEARCH.md §1–§6, 6-GAP_ANALYSIS.md §Phase 7 Routing (P7-PRE-1..5), docs/PACK-SPEC.md, docs/SOURCE-VETTING.md:128-135, live tree (56 pack dirs / catalog 54 / SKILLS.md "54 packs (+2 signposts)" / README packs-54 / cursor 55), live tooling (tooling/check_release.py, tooling/validate_pack.py, tooling/gen_packs_page.py, jgs-reference-skill tools), 7-PLAN_CHECK.md (W1–W6 incorporated below).
**Method:** adversarial executability review — every `<automated>` block was traced against the action text that must produce its inputs, every count target against check_release.py's actual logic, every tool flag against the live argparse.

**Verdict:** NEEDS_WORK

The build actions are sound and approved as written: all 7 GP packs have dedicated tasks, every P7-PRE-1..5 obligation is a halt-and-surface pre-generation gate in the covering task, the wave structure is acyclic with disjoint file trees, registration arithmetic (61 catalog / 62 cursor / 63 dirs / packs-61) is correct against check_release.py's real checks, and Phase 9 version surfaces are correctly excluded. Two Wave-C `<automated>` blocks are defective as written (one invalid bash, one phantom path) and the highest-risk pack's quality gate has an internal sequencing contradiction. These are localized verify-block/step fixes — do not treat this as a rewrite. Fix the BLOCKERs (and ideally M1) before execute; the rest can be fixed in-pass.

---

## BLOCKER

### BL-01: 7-03 Task 2 verify — NOTICE greps are invalid bash; the block can never exit 0

**File:** `.planning/phases/7-gap-driven-pack-builds/7-03-PLAN.md:155`
**Issue:** `grep -c "\[pack: dod-vva-rpg\]" NOTICE = 1 && grep -c "\[pack: mil-std-40051\]" NOTICE = 1` — bash word-splitting makes `=` and `1` additional FILE arguments. Live behavior: `grep: =: No such file or directory` → exit 2 even when NOTICE matches, aborting the whole `&&` chain. The registration task's acceptance command false-fails on a perfect build. Secondary defect: only 2 of the 7 new slugs are checked at all.
**Fix:** `test "$(grep -c '\[pack: dod-vva-rpg\]' NOTICE)" = "1"` for each slug, or one loop: `for s in dod-vva-rpg faa-std-025 dote-te-guidebook dafman-63-119 mil-std-881f federal-bca mil-std-40051; do [ "$(grep -c "\[pack: $s\]" NOTICE)" = "1" ] || exit 1; done` (covers all 7 and closes the 2-of-7 gap PLAN_CHECK W1 also flagged).

### BL-02: 7-03 Task 1 verify — overlap glob path `chapter_fulltexts/` is never created by the action

**File:** `.planning/phases/7-gap-driven-pack-builds/7-03-PLAN.md:119` (verify) vs `:100-102` (action step 4) and `:113-115` (action step 8)
**Issue:** The verify runs `for f in sources/dod-vva-rpg/chapter_fulltexts/*.txt`. The action writes per-chapter `work_dir_ch1.txt ...` files (or "a dir listing") and *optionally* concatenates one overlap source file. Nothing creates `chapter_fulltexts/`; if the executor follows the action literally the glob does not expand, check_overlap gets a literal nonexistent path, and the loop's `|| exit 1` false-fails the GP-01 build. PLAN_CHECK W2 confirmed; still unfixed.
**Fix:** Pick one layout in the action and point both the overlap runs and `<automated>` at it — recommended: "copy each chapter's `full_text.txt` to `sources/dod-vva-rpg/chapter_fulltexts/chNN.txt` (these are the overlap sources and the concat inputs)" — then the existing verify glob is correct as written. While there, tighten the PACK.yaml provenance grep beyond bare `retrieved` (e.g. assert ≥8 chapter titles or a `chapters used:` notes key).

---

## MAJOR

### MA-01: 7-02 Task 2 (GP-07, highest-risk pack) — chars/page gate is sequenced before the selection that defines its region

**File:** `.planning/phases/7-gap-driven-pack-builds/7-02-PLAN.md:131-136` (step 3 gate) vs `:137-141` (step 4 selection), and must_haves `:21`
**Issue:** Step 3 gates on "avg chars/page = len(full_text.txt)/metadata.json pages **over the MAIN BODY region**; floor >= 300", but the main-body region is only defined by step 4's page selection, which comes after the gate. The must_haves truth says ">= 300 **on the selected main-body extraction**" — a third formulation. A literal executor computes len(full_text)/1168 whole-file: with ~150 pp of text-bearing body and ~1000 pp of near-empty image plates, the whole-file average can fall below 300 even when the body is healthy (7-RESEARCH §2 delta 2 calibrated the floor at ~>=200 for exactly this file), triggering the OCR contingency — `ocrmypdf` on a 37.7 MB / 1168-page PDF — for no reason, or halting outright.
**Fix:** Reorder in one of two ways, stated explicitly: (a) run the floor on the whole-file average with the research-calibrated threshold (~>=200) as the OCR trigger, then compute the >= 300 floor on the *selected* main-body slice after step 4 (matches must_haves wording); or (b) move the >= 300 gate after step 4 and compute it over the selected page range. Name which basis each number applies to so the deviation log entry is unambiguous.

### MA-02: P7-PRE verify greps are tautological or missing — several hard gates can silently pass on a stub

**Files/lines:**
- `7-02-PLAN.md:111` — `grep -Eqi "881[EF]"` is satisfied by the scaffold title ("MIL-STD-881F" appears in title/version regardless of revision resolution); `grep -Eqi "distribution statement|DIST-A"` is satisfied by the DIST-A licence string itself, which `build_pack.py` writes into PACK.yaml at scaffold — it cannot fail even if the P7-PRE-1 visual confirmation note is absent.
- `7-02-PLAN.md:160` — `grep -Eqi "training|documentation"` does not pin the Topic Index / "Training & Documentation" cluster-25 vocabulary (PLAN_CHECK W4).
- `7-01-PLAN.md:151` — `"8\.02|v3-june|2022"`: bare `2022` satisfies P7-PRE-3 without naming the edition (PLAN_CHECK W4).
- `7-01-PLAN.md:179` — no grep for the recorded releasability finding; P7-PRE-5 for DAFMAN is action-only (PLAN_CHECK W4).
- `7-01-PLAN.md:223` — `A-94` + `Cost Benefit` both appear in the scaffold title; the P7-PRE-2 in-source evidence notes for BOTH documents are not asserted (PLAN_CHECK W4).
- `7-01-PLAN.md:118` — `rev[ .]*[EF]` case-insensitively matches "reverse" (new; same family).
- `7-03-PLAN.md:155` — no slug-set assert; 7 wrong slugs registered would still count 61 (Phase 3 3-03-PLAN.md:181 has the pattern to copy: `new<=slugs` python assert).
**Fix:** For gate evidence, grep the notes field, not the scaffold: e.g. `grep -Eqi "visual(ly)? confirm" PACK.yaml` for P7-PRE-1, `grep -Eqi "8\.02|v3-june" ` (drop `2022`), `grep -Eqi "no releasability restrictions"` (or the recorded halt deviation), per-document evidence keys in notes for federal-bca, `grep -q "Training & Documentation" SKILL.md`, and add the 3-03-style slug-set assert in 7-03 T2.

### MA-03: chars/page >= 300 floor is a hard gate in prose only — no automated block measures it on any of the 8 pack builds

**Files/lines:** `7-01-PLAN.md:118,151,179,223`; `7-02-PLAN.md:111,160`; `7-03-PLAN.md:119` (verify blocks) vs the actions' step-4/step-3 floors and must_haves `7-01-PLAN.md:28`, `7-02-PLAN.md:21`
**Issue:** PLAN_CHECK W3 — every task's action and `<done>` require the floor, but a skipped computation leaves verify green. The gate that guards against wrong-PDF/scan-copy builds (the phase's core fetch-risk mitigation) is unmeasured.
**Fix:** One line per extraction in each `<automated>`: `python -c "import json,sys;from pathlib import Path;w=Path(open('sources/<slug>/work_dir.txt').read().strip());ft=(w/'book_skill_work/full_text.txt').read_text(errors='ignore');pg=json.load(open(w/'book_skill_work/metadata.json'))['pages'];import sys;sys.exit(0 if len(ft)/pg>=300 else 1)"` (adjust per-work-dir for federal-bca and per-chapter for dod-vva-rpg; confirm the metadata.json pages key name at build time).

---

## MINOR

### MI-01: 7-03 Task 2 omits the catalog `updated` bump required by the mechanics it cites

**File:** `.planning/phases/7-gap-driven-pack-builds/7-03-PLAN.md:131-134`
**Issue:** The plan says "mechanics per 3-RESEARCH §4", whose step 1 is "add a pack object ... bump `updated`" (3-03-PLAN must_haves carried "`updated` bumped"). The 7-03 action omits it; catalog.json's `updated` (currently 2026-08-15) goes stale through a 7-pack registration. Not caught by check_release.py.
**Fix:** Add "bump catalog.json `updated` to the registration date" to step 1.

### MI-02: 7-03 Task 2 instructs catalog keys no live object carries

**File:** `.planning/phases/7-gap-driven-pack-builds/7-03-PLAN.md:131-133`
**Issue:** Live catalog key union is exactly: slug, title, publisher, source_version, license, license_tier, commercial_use, chapters, status, aliases. The plan instructs adding `share_alike: false, attribution_required: false` — keys no live object has — creating schema drift inside one file (harmless to the gate, which never parses catalog contents, but inconsistent).
**Fix:** Reword to "copy a live Tier-1 object shape (slug/title/publisher/source_version/license/license_tier/commercial_use/chapters/status); PACK.yaml carries share_alike/attribution_required, the catalog does not."

### MI-03: 7-03 claim_verification "before this plan" row is pre-PHASE-7, not pre-7-03

**File:** `.planning/phases/7-gap-driven-pack-builds/7-03-PLAN.md:68`
**Issue:** PLAN_CHECK W5 — the row quotes 56/54/55, true today but false when 7-03 runs (tree will be 62 dirs / catalog 54 after Waves A+B). An executor re-verifying claims at 7-03 start would see a mismatch and may "fix" the wrong thing.
**Fix:** Relabel the row "pre-Phase-7 basis" and add "at 7-03 start: 62 dirs / catalog 54 / cursor 55".

### MI-04: Estimates exceed the 100k smart-zone; confidence low on all three plans

**Files:** `7-01-PLAN.md:14-18` (150k), `7-02-PLAN.md:11-15` (110k), `7-03-PLAN.md:16-20` (120k)
**Issue:** PLAN_CHECK W6 — accepted: same Wave-A shape as the proven 3-01; registration already isolated in 7-03. Do not split.
**Fix:** None required; treat estimates as uncalibrated and expect mid-plan checkpoint breaks.

---

## Verified sound (checked, not raised)

- **Registration arithmetic against the real gate:** check_release.py 6b computes cursor-eligible = all `packs/*/SKILL.md` dirs minus `commercial_use: false` (sebok only; signposts INCLUDED) → 63 − 1 = 62 ✓; check 6 counts non-signpost SKILLS.md rows vs non-signpost pack dirs → 61 ✓; check 5 validates every non-signpost pack → 61 validate_pack runs ✓. Plan targets 61/62/63/packs-61 all match.
- **Tool CLIs match every verify invocation:** check_overlap.py `--source/--pack` ✓, scan_generated_skill.py positional path ✓, outline.py `--source/--out` ✓, build_pack.py `--slug/--title/--publisher/--version/--license/--out-dir` ✓, vet_source.py `--title/--publisher/--license` ✓.
- **P7-PRE encoding matches obligations:** all five PREs (6-GAP_ANALYSIS.md:73-77, SOURCE-VETTING.md:128-135) are pre-generation halt-and-surface gates in the covering tasks — GP-06 dual gate before any chapter generation (7-01 T4 step 3), GP-07/GP-05 visual DIST-A not text-grep (7-02 T2 step 2 / T1 step 2), per-chapter DIST-A for GP-01 (7-03 T1 step 3), edition recording (7-01 T1/T2), DAFMAN releasability re-confirm in the fetched copy or halt (7-01 T3).
- **Leak posture:** `sources/` is gitignored (.gitignore:17); every task carries the `git show --name-only` leak check; check_release SOURCE_HOSTS would additionally catch any everyspec/dla/dod URL leaking into shippable files.
- **RR-S-13:** check_release.py:138-141 requires `^## When to use` + a Prerequisites marker — the plans' `## When to use` + `**Prerequisites:**` contract (PACK-SPEC.md:33) satisfies both.
- **packs.html:** generated from SKILLS.md by gen_packs_page.py and freshness-gated (RR-B-30) — plan step 6 (regenerate, never hand-edit) is correct.
- **Wave structure / Phase 9 exclusion:** 7-02 depends_on 7-01, 7-03 on both — acyclic, disjoint pack trees, single late registration sweep; CHANGELOG/plugin 1.18.0/RELEASE-INFO explicitly out of scope (version agreement stays 1.17.0).
- **Installers discover packs by glob** — no other hardcoded pack manifest exists to miss.
- **GP-08, P7-FUT-1 (AAF), P7-BACKLOG** correctly absent (prior descope / parked).

---

## Disposition summary

| ID | Sev | Plan / task | Must fix before execute? |
|----|-----|-------------|--------------------------|
| BL-01 | BLOCKER | 7-03 T2 verify (NOTICE bash) | Yes |
| BL-02 | BLOCKER | 7-03 T1 verify (phantom `chapter_fulltexts/`) | Yes |
| MA-01 | MAJOR | 7-02 T2 (GP-07 gate sequencing / floor basis) | Yes (risk of gratuitous OCR or false halt on the riskiest pack) |
| MA-02 | MAJOR | verify greps across 7-01/7-02/7-03 | Strongly recommended |
| MA-03 | MAJOR | chars/page floor unautomated (all pack tasks) | Strongly recommended |
| MI-01..04 | MINOR | 7-03 catalog details, claim label, estimates | In-pass |

**Verdict rationale:** the two BLOCKERs sit in Wave-C acceptance commands that cannot pass as written, and MA-01 leaves the phase's highest-risk quality gate ill-defined — fix those three, then execute. All build actions, gate semantics, counts, and scope boundaries are otherwise correct; no rewrite, no re-plan.

---

_Reviewer: ZCode (plan-mode code review), 2026-08-14_
_Incorporates 7-PLAN_CHECK.md W1–W6 (verified against the live tree before inclusion)_

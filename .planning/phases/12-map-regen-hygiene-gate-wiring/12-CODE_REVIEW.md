---
phase: 12-map-regen-hygiene-gate-wiring
reviewed: 2026-08-17
depth: deep
scope: full (Phase 12 surface + prior artifacts + cross-file; repo at HEAD dc0a7fb)
files_reviewed: 30
files_reviewed_list:
  - docs/capability-pack-map.json
  - docs/capability-pack-map.md
  - docs/capability-map-CONTRACT.md
  - tooling/check_capability_map.py
  - tooling/check_release.py
  - CHANGELOG.md
  - .gitattributes
  - packs/mil-std-881f/SKILL.md
  - packs/dafman-63-119/SKILL.md
  - packs/mil-std-40051/SKILL.md
  - packs/federal-bca/SKILL.md
  - packs/federal-bca/PACK.yaml
  - catalog.json
  - .claude-plugin/plugin.json
  - .cursor-plugin/plugin.json
  - RELEASE-INFO.txt
  - .github/workflows/validate.yml
  - .planning/REQUIREMENTS.md
  - .planning/ROADMAP.md
  - .planning/phases/12-map-regen-hygiene-gate-wiring/12-01-PLAN.md
  - .planning/phases/12-map-regen-hygiene-gate-wiring/12-02-PLAN.md
  - .planning/phases/12-map-regen-hygiene-gate-wiring/12-01-SUMMARY.md
  - .planning/phases/12-map-regen-hygiene-gate-wiring/12-02-SUMMARY.md
  - .planning/phases/12-map-regen-hygiene-gate-wiring/12-PLAN_REVIEW.md
  - .planning/phases/12-map-regen-hygiene-gate-wiring/12-VALIDATION.md
  - .planning/phases/12-map-regen-hygiene-gate-wiring/12-RESEARCH.md
  - .planning/phases/12-map-regen-hygiene-gate-wiring/12-INTEGRATION_CHECK.md
  - .planning/phases/12-map-regen-hygiene-gate-wiring/12-SECURITY_AUDIT.md
  - .planning/phases/11-io-unlocking-packs-decision-analysis-remap/11-CODE_REVIEW.md (analog)
findings:
  critical: 0
  blocker: 0
  major: 0
  minor: 0
  info: 3
  total: 3
status: issues_found
verdict: PASS_WITH_NOTES
---

# Phase 12 Full-Scope Code Review — Map regen + hygiene + gate wiring

**Verdict:** PASS_WITH_NOTES

**Reviewed:** 2026-08-17
**Depth:** deep (whole Phase 12 surface + 12-RESEARCH locked decisions + 12-01/12-02 PLAN+SUMMARY + 12-PLAN_REVIEW MJ-01 + analog 11-CODE_REVIEW)
**Scope:** execute commits `53099e0..bb39a3a` plus live tree at HEAD `dc0a7fb` on `main` (integration/security artifacts after execute do not change map/gate/hygiene files)

## Summary

Phase 12 regenerated the capability-pack map to **644 / 63**, MOVEd the three locked chapters into Decision Analysis (**5/4**), encoded listed-primary floors ≥4, landed the MAP-19-05 CONTRACT paragraph, wired the now-green map gate into `check_release.py` in-process, and closed HYG-01/02/04 in-tree plus HYG-03 as sibling PR #2. Version trio and `map_version` stay **1.18.0**. MAP-19 / HYG boxes stay open. No generator. No forbidden packs. CI still does not exec repo Python.

What keeps this off a clean PASS is leftover plan/advisory hygiene — the same class as `11-CODE_REVIEW.md`: 12-01 Task 1 `<automated>` was never rewritten to encode MJ-01's chapter-set set-diff, and the two advisory PLAN_REVIEW minors (VALIDATION task map, RESEARCH Open Questions) remain unstamped. Neither can mislead Phase 13 if the live JSON + both gates are the authority.

Unlike a copy-not-move remap, uniqueness + old-cluster absence prove MOVE. Unlike wiring a RED map, THRESHOLDS (`7134474`) precede the import (`ca27199`).

## Gates Run (all PASS)

| Check | Method | Result |
|---|---|---|
| `check_capability_map.py` | `python tooling/check_capability_map.py` | **PASS** (`PASS: capability map OK`; TOTAL **644**; exit 0) |
| `check_release.py` | `python tooling/check_release.py` | **PASS** (`RELEASE CHECK: PASS`; reprints map cluster-count block; exit 0) |
| Map wire | `rg check_capability_map tooling/check_release.py` | docstring check 8 + `import check_capability_map` + `main()` + `fail()` on non-zero; no subprocess |
| Envelope | JSON load | schema **2**; `map_version` **1.18.0**; `generated_on` **2026-08-17**; 32 clusters; 644 entries; 63 packs |
| Chapter-set | disk `packs/*/chapters/*.md` vs JSON (support excluded) | **on_disk_only=0, map_only=0** (536/536); missing files **0** |
| MAP-19-03 MOVE | DA want-set + old-cluster absence | DA **exactly** five locked rows / 4 packs; Opportunity does **not** hold federal-bca ch04/ch06; Assurance does **not** hold dod-vva-rpg ch06; each of the three sits in **one** cluster |
| Stay-put | membership walk | federal-bca ch01–ch03, ch05 + 3 support still Opportunity (8/2); dod-vva-rpg ch08 Validation; ch10 Risk; Integration **4/4** |
| Listed-primary conjunct | count + n_packs | DA 5/4; Validation 7/4; Integration 4/4; Interfaces 9/4; Ops 13/5; **none** is `<4 AND 1 pack` |
| THRESHOLDS | `tooling/check_capability_map.py:34-43` | Training 1 / Traceability 3 / Opportunity 2 unchanged; Interfaces **4**; DA / Validation / Integration / Ops **4** |
| CONTRACT MAP-19-05 | `docs/capability-map-CONTRACT.md` §6 | **628+** / post-regen **644**; **502** residue; Cybersecurity 69/10 + Digital Engineering 25/4 **unbound** |
| CONTRACT §4 / §5 | same file | §4 invokes `check_release.py` `main()` in-process; §5 floors match THRESHOLDS |
| Version trio / tag | plugin + CHANGELOG + RELEASE-INFO + `git tag -l 'v1.19*'` | all **1.18.0**; no `## [1.19.0]`; no `v1.19*` tag |
| HYG-01 | CHANGELOG first 8 + CRLF + `.gitattributes` | `3c212d2d0a436f70`; BOM **False**; CRLF **0**; pin exactly `*.md text eol=lf` |
| HYG-02 | four SKILL.md + `validate_pack.py` ×4 | 881F PM between Missile and Program Element; AFOTEC before Agile; `ch08, Topic Index` gone; Opportunity label renamed; all **PASS** |
| HYG-04 | `packs/federal-bca/PACK.yaml` notes | A-94 `(c)` recorded as enumeration markers; no URL |
| HYG-03 | sibling `vet_source.py` + `gh pr view 2` | keys `afotec` / `defense acquisition guidebook` / `dod dag` / `cmu` / `carnegie mellon` / `software engineering institute`; no bare `sei`; commit **1c8b781**; PR **OPEN** https://github.com/jgsystemsconsulting/jgs-reference-skill/pull/2 |
| Vendor ban | `test ! -e tooling/vet_source.py` | **holds** |
| Boxes | `grep '^- \[.\] \*\*(MAP-19\\|HYG-)'` | **9 open**; 0 checked |
| Catalog leftover | `catalog.json` `dod-vva-rpg.chapters` | still **10** (Phase 13) |
| Link policy | `grep -c http docs/SOURCE-VETTING.md` | **0** |
| Generator / forbidden packs | `ls tooling/gen*capability*` + `ls packs \| grep -Ei aaf\\|cba\\|stakeholder\\|dodm-5000` | **absent** |
| CI | `.github/workflows/validate.yml:4-6` | never execs repo Python; `check_capability_map` **absent** |
| Branch | `git branch --show-current` | **main** |

## PLAN_REVIEW majors — resolved in executed files

| ID | Required | Live evidence | Status |
|---|---|---|---|
| MJ-01 | 12-01 T1 verify must be chapter-set (or live gate), not pack-slug | Live `on_disk_only=0, map_only=0`. All 16 named chapters present (8719×7 Ops; 200N ch01 CM + ch02–06 Interfaces; RPG ch11 T&E, ch12+ch13 Validation). 12-01-SUMMARY records T1 close ran `check_capability_map.py` plus `(pack, chapter)` set-diff. A two-slug stub cannot pass the live gate | **RESOLVED** (executed files) |

The plan file itself was **not** rewritten (`git log` on `12-01-PLAN.md` is still `f43544e`). T1 `<automated>` is still the pack-level `disk-packs` assert. SUMMARY ran the extra conjunct as a post-hoc self-check. See IN-01.

## Verdict fidelity (12-RESEARCH → shipped)

| ID | RESEARCH decision | Shipped | Match |
|---|---|---|---|
| MAP-19-01 | agent pass + gate; no generator; 16 chapters | 644 entries; 16 classified; no `generate_capability_map.py` | 1:1 |
| MAP-19-03 | MOVE three locked rows only | DA exactly five-row want-set; old clusters vacated; stay-put held | 1:1 |
| MAP-19-02 | name-keyed ≥4; conjunct not a second schema; Integration floor-held | THRESHOLDS + one-shot print; Integration 4/4; "floor held; AAF still deferred; no raid" | 1:1 |
| MAP-19-05 | one CONTRACT paragraph: 628+ / 502 / Cyber+DE unbound | §6 quote matches; no binding tables | 1:1 |
| MAP-19-04 | in-process `main()` after GREEN | `7134474` ancestor of `ca27199`; import after cursor-manifest; both gates PASS | 1:1 |
| map_version | keep 1.18.0; md may add v1.19 *bullet* | envelope 1.18.0; `capability-pack-map.md:15` changelog bullet only | 1:1 |
| HYG-01..04 | BOM/LF pin; four nits; `(c)` wording; sibling PR or record | all landed; Path A PR #2; no vendor | 1:1 |
| Q4 ch11 | classify by reading; do not force Validation | ch11 → Test & Evaluation | 1:1 |

ROADMAP SC-1..SC-4 all hold on the live tree. REL-19 stays Phase 13.

## Scope / creep / deviations

Execute file set matches the two plans' `files_modified` plus SUMMARIES:

- `53099e0` — `docs/capability-pack-map.json` + `.md` (json+md together)
- `7134474` — `tooling/check_capability_map.py` THRESHOLDS only
- `48a2a63` — `docs/capability-map-CONTRACT.md` §5 floors + §6 paragraph
- `ca27199` — `check_release.py` wire + map-gate docstring + CONTRACT §4
- `bb39a3a` — CHANGELOG + `.gitattributes` + four SKILL.md + federal-bca PACK.yaml
- `7365fd6` / `d4d3c53` / `828e237` — SUMMARIES + ROADMAP/STATE close-out

No `catalog.json`. No `README.md` new-slug rows. No `validate.yml`. No `v1.19.0` tag. No `tooling/vet_source.py`.

| deviation | classification | where recorded |
|---|---|---|
| None | — | both SUMMARIES `## Deviations` = `None.` |

No undisclosed scope creep.

## Findings

### IN-01: Plan `<automated>` still omits the MJ-01 chapter-set conjunct

**File:** `12-01-PLAN.md` Task 1 `<verify>`
**Class:** INFO
**Issue:** 12-PLAN_REVIEW required a `packs/*/chapters` vs JSON `(pack, chapter)` set-diff (or a live `check_capability_map.py` run) in T1 automated so a two-slug stub cannot print `MAP_MOVE_OK`. That plan file was never edited. Executed content independently satisfies the major (chapter-set empty; SUMMARY re-ran the extra check). Residual risk is only a future re-execute treating the original pack-level gate as sufficient.
**Fix:** Optional — fold the chapter-set (or live-gate) assert into the plan verify, or leave the SUMMARY as the record. Do not weaken the shipped map to match the old grep.

### IN-02: PLAN_REVIEW advisory stamps still open (MN-02 / MN-03)

**File:** `12-VALIDATION.md` Per-Task map; `12-RESEARCH.md` Open Questions
**Class:** INFO
**Issue:** VALIDATION.md still lumps six execute tasks into four rows and `nyquist_compliant: false`. RESEARCH Open Questions lack `(RESOLVED)` suffixes. PLAN_REVIEW marked both advisory / not execute-blocking. Decisions were followed (Integration floor-held; `map_version` 1.18.0; HYG-03 Path A; ch11 T&E).
**Fix:** Stamp if convenient during verify/close-out. Do not reopen verdicts.

### IN-03: 12-01 T3 / 12-02 T2 plan greps still carry MN-01 / MN-04 dead weight

**File:** `12-01-PLAN.md` T3 `<verify>`; `12-02-PLAN.md` T2 `<verify>`
**Class:** INFO
**Issue:** T3 automated still greps only 628/502/Cyber/DE/unbound — not §5 floor names. T2 still takes the first `Training & Documentation` line (`SKILL.md:3` frontmatter) for the Topic Index assert. Live CONTRACT §5 **was** synced and 40051 `:77` no longer has `ch08, Topic Index`. Same class as 11-CODE_REVIEW IN-01: executed files are correct; plan greps were not tightened.
**Fix:** Optional verify-line polish. Do not revert §5 or the Topic Index row to make the old greps look necessary.

## Confirmed correct (checked, not raised)

- Remap is MOVE not copy: uniqueness 644/644; each of the three chapters appears in exactly one cluster (`Decision Analysis & Trade Studies`).
- New-pack support files omitted (multi-cluster). Arithmetic `628 + 16 = 644` holds.
- Classification vs When-to-use is defensible: 8719 all Ops (disposal/ODAR spine); 200N ch01 is IRN/CCB not the interface object; leftover RPG ch11 is a T&E/V&V checklist, not Integration (IO-05 is AAF).
- Wire insertion is after cursor-manifest (~215) and before authored-file headers; reuses existing `sys.path.insert` from `validate_pack`.
- CHANGELOG BOM strip is byte-minimal (`ef bb bf` removed; `## [1.18.0]: 2026-08-17` retained; JGSC + SPDX still in first 600 chars).
- HYG-03 did not add bare `sei` (substring trap). `defense acquisition` US_GOV publisher signal left as-is.
- MAP-19 / HYG / ROADMAP Phase 12 boxes left unchecked — verify owns the ticks.
- Tautology N/A. No MCP. No WINDOWS.md.

## SC Re-Verification (ROADMAP Phase 12)

| SC | Statement | Verdict |
|---|---|---|
| 1 | `check_capability_map.py` PASS; MAP-19-02 floor held (no listed primary still at <4 entries AND 1 pack) | TRUE — exit 0; conjunct all `floor_fail=False` |
| 2 | `check_release.py` invokes the map gate | TRUE — in-process `main()`; release stdout reprints cluster counts |
| 3 | CONTRACT.md notes live snapshot (not 502) and unbound Cyber/DE clusters | TRUE — §6 628+/644 / 502 residue / unbound |
| 4 | CHANGELOG BOM gone; `.gitattributes` pin present; topic-index nits fixed; vet_source EXCLUDED sync done or recorded as external-repo PR | TRUE — HYG-01/02 landed; HYG-03 Path A PR #2 (merge not required) |

**Verdict: PASS_WITH_NOTES** — map, MOVE, floors, CONTRACT, wire, and hygiene are faithful, version-unbumped, box-open, and Phase-13-consumable. Three info leftovers (unfixed plan verifies; unstamped advisory docs; leftover MN-01/MN-04 greps) do not block verify.

---

_Reviewer: gsd-code-reviewer (adversarial, full-scope)_
_Depth: deep_
_HEAD: dc0a7fb_

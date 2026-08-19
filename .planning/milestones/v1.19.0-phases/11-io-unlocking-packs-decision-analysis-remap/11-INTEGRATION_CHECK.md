# Phase 11 Integration Check — IO-unlocking packs + Decision Analysis remap

**Phase:** 11-io-unlocking-packs-decision-analysis-remap (Wave A packs + Wave B extend/remap/defer/thin-register)
**Scope of audit:** cross-phase wiring only — can Phase 12 apply the IO-01 remap table without re-guessing, and do the new packs exist for map regen?
**Method:** adversarial — every expected connection traced end-to-end (Phase 10 handoff → built slugs → remap table → registration → Phase 12 contract), not checked for existence.

**Verdict:** PASS_WITH_NOTES

---

## 1. Wiring Summary

| # | Expected connection | Status | Evidence |
|---|---------------------|--------|----------|
| 1 | Phase 10 SOURCE-VETTING handoff GO names ↔ built slugs | WIRED | Handoff: `nasa-std-8719-14` (IO-03), IS-GPS-200N exemplar (IO-04). Disk + PACK.yaml slugs: `packs/nasa-std-8719-14`, `packs/is-gps-200n`. No `is-300`, no ICD-GPS-153, no SP-7084 pack (optional, skipped). |
| 2 | Phase 10 NO-GO DoDM ↔ IO-02 chapter-add (not `dodm-5000-102`) | WIRED | `packs/dodm-5000-102` absent. `dod-vva-rpg` chapters 10→13 (`ch11-te-vv-checklist.md`, `ch12-developing-the-referent.md`, `ch13-conceptual-model-development-and-validation.md`). REQUIREMENTS IO-02: "chapters-not-a-pack". |
| 3 | Phase 10 NO-GO Army CBA / AAF ↔ IO-01 remap + IO-05/06 DEFERRED + IO-07 ACCEPT | WIRED | No `army-cba` / AAF / stakeholder pack. IO-05/06 parentheticals contain `DEFERRED`; IO-07 contains `ACCEPT`. All IO-01..07 boxes still `- [ ]` (no silent ticks). |
| 4 | 11-02-SUMMARY IO-01 remap table ↔ on-disk chapter files ↔ live map "From" | WIRED | All three named files exist. Live map still has `federal-bca` ch04+ch06 in Opportunity/Benefit and `dod-vva-rpg` ch06 in Assurance — matches table "From (today)". Phase 12 can apply without re-classifying. |
| 5 | Map JSON NOT edited (Phase 12 owns apply / regen) | WIRED | `git diff dc35907 HEAD -- docs/capability-pack-map.json` empty. Phase 11 commits do not list the map. `check_capability_map.py` FAIL (19 issues): new slugs + ch11–ch13 + 8719/200N chapters on disk not in map — correct pre-Phase-12 RED. |
| 6 | Thin-register keeps `check_release` green without version bump | WIRED | `python tooling/check_release.py` → **PASS**, exit 0. Plugin `.cursor-plugin/plugin.json` still `1.18.0`. No `v1.19.0` tag. CHANGELOG still `## [1.18.0]`. Catalog 63 includes both GO slugs. |
| 7 | catalog.json vs `packs/` vs check_release arithmetic | WIRED | dirs **65**, catalog **63**, SKILLS header **63 (+2 signposts)**, cursor skills **64** (65 − `sebok`). Catalog∩dirs: zero catalog orphans; dirs−catalog = `{omg-signpost, se-standards-signpost}` only. `install.py --dry-run` lists both new slugs. |
| 8 | Phase 10 SOURCE-VETTING still URL-free | WIRED | `grep -c 'http' docs/SOURCE-VETTING.md` = **0**. Last SOURCE-VETTING commits are Phase 10 (`02fab79`, `44f777f`). Handoff table still 3 `\| GO —` / 3 `\| NO-GO —`. |
| 9 | ROADMAP Phase 11 still unchecked (verify closes it) | WIRED | `- [ ] **Phase 11: IO-unlocking packs + Decision Analysis remap**`. Phase 12 "Depends on: Phase 11". Phase 10 remains `[x]`. |
| 10 | REQUIREMENTS IO annotations ↔ SUMMARY remap / deferrals | WIRED | IO-01 names the three chapter files + "Map apply is MAP-19-03 / Phase 12". IO-02 names leftover RPG ch11–ch13. IO-05/06 dated DEFERRED. IO-07 dated ACCEPT. Live count leave-2 deferred to Phase 12. |

## 2. Handoff consumption (Phase 12 does not re-guess)

Phase 12 planner inputs, all already decided:

| Input | Consume as | Do not re-open |
|---|---|---|
| `packs/nasa-std-8719-14` (7 chapters) | New pack for MAP-19-01 regen (Ops/Maint/Disposal / IO-03) | Re-vet 8719.14C; invent a different slug |
| `packs/is-gps-200n` (6 chapters) | New pack for MAP-19-01 regen (Interface Management / IO-04) | Search for IS-300; add 705J/800J/ICD-GPS-153 |
| `dod-vva-rpg` ch11–ch13 | On-disk leftover RPG chapters for regen (IO-02) | Create `dodm-5000-102` |
| IO-01 remap table (11-02-SUMMARY) | MAP-19-03 apply: three concrete files → Decision Analysis & Trade Studies | Re-pick which A-94 / VV&A chapters move |
| IO-05 / IO-06 | DEFERRED — no AAF pack to classify | Use `dod-rio` AAF chapters as a licence grant |
| IO-07 | ACCEPT — no invented stakeholder pack | Treat SEBoK ch26–ch28 rematch as a substitute for accept |
| `docs/capability-pack-map.json` | Stale on purpose (`map_version` 1.18.0, 628 entries, DA = 2/2) | Edit it in Phase 11 leftovers |

Leave federal-bca ch01–ch03, ch05 (+ support files) in Opportunity; leave dod-vva-rpg ch08 in Validation and ch10 in Risk — already specified. Result after apply: Decision Analysis 2→5 entries, 2→4 packs (Phase 12 SC-1 / MAP-19-03).

## 3. E2E Flow Trace: Phase 10 GO/NO-GO → Phase 11 artifacts → Phase 12 apply

1. SOURCE-VETTING Phase 11 handoff (3 GO / 3 NO-GO) → 11-01 built only GO slugs `nasa-std-8719-14` + `is-gps-200n` — VERIFIED (`validate_pack.py` PASS both)
2. NO-GO DoDM → 11-02 extended existing `dod-vva-rpg` (13 chapters, no new slug) — VERIFIED
3. NO-GO Army CBA → remap table of existing A-94 / VV&A decision chapters, not a CBA pack — VERIFIED (files exist; map "From" matches)
4. NO-GO AAF → IO-05/06 DEFERRED; IO-07 ACCEPT; boxes open — VERIFIED (bound greps + `- [ ]`)
5. Thin-register two Wave-A slugs; plugin stays 1.18.0; `check_release.py` PASS — VERIFIED
6. Map JSON byte-stable since Phase 8 classify (`dc35907`); map gate RED on new packs/chapters — VERIFIED (Phase 12 owns regen+apply)
7. SOURCE-VETTING `http` = 0; Phase 11 checkbox open for verify — VERIFIED

No break in the chain. Flow status: COMPLETE for Phase 12 consumption.

## 4. Requirements Integration Map

| Requirement | Integration path | Status | Issue |
|---|---|---|---|
| IO-01 | 11-02-SUMMARY table + REQUIREMENTS pointer → three on-disk chapters → MAP-19-03 (Phase 12) | WIRED (spec) | Apply + leave-2 count are Phase 12 (correctly not started) |
| IO-02 | leftover RPG ch11–ch13 in `dod-vva-rpg`; no `dodm-5000-102` | WIRED | Catalog/README still say 10 chapters (Phase 13 / NOTE-2) |
| IO-03 | handoff GO → `packs/nasa-std-8719-14` → catalog/SKILLS/cursor/NOTICE/packs.html | WIRED | REQUIREMENTS note still Phase-10-only (built slug is the consume path) |
| IO-04 | handoff GO → `packs/is-gps-200n` (exemplar, no IS-300) | WIRED | same as IO-03 |
| IO-05 | DEFERRED in REQUIREMENTS; no AAF pack | WIRED | — |
| IO-06 | DEFERRED in REQUIREMENTS; no AAF pack | WIRED | — |
| IO-07 | ACCEPT in REQUIREMENTS; no invented pack | WIRED | — |
| MAP-19-01 | new slugs + ch11–ch13 exist on disk; map stale | FORWARD-REF | Gate FAIL is the Phase 12 start state |
| MAP-19-03 | remap table names files that exist; JSON untouched | FORWARD-REF | Phase 12 apply |
| VET-19-01..04 | Phase 10 register unchanged; still URL-free | WIRED | Boxes remain open (Phase 10 verify already closed the phase) |
| REL-19-01/02 | thin-register only; no 1.19.0 bump/tag | FORWARD-REF | Phase 13 |

**Requirements with no cross-phase wiring:** none in Phase 11 scope.

## 5. SUMMARY ledger classification

| Plan | Ledger entry | Classification | Wiring impact |
|---|---|---|---|
| 11-01 | Overlap paraphrase of one nasa-std-8719-14 ch04 sentence | auto-fixed (licence gate) | None. Overlap exit 0 after fix. |
| 11-01 | When-to-use not literally adjacent to Prerequisites (analog body paragraph) | accepted analog match | None. RR-S-13 / `check_release` still PASS. |
| 11-02 | UCO skipped (HTML-only); Checklist + 2 live-index special topics | pre-authorized | None. Chapter count 13>10; no DoDM pack. |
| 11-02 | glossary/cheatsheet lightly updated for ch11–ch13 | accepted routing hygiene | None. |

No WINDOWS.md in this phase (none required; none present).

## 6. Findings

**BLOCKERS:** none.

**WARNINGS:** none that break Phase 12 consumption.

**NOTES:**

- **NOTE-1 (README catalogue table):** Badge is `packs-63` but the live-pack table still ends at `mil-std-40051` (no `nasa-std-8719-14` / `is-gps-200n` rows; `dod-vva-rpg` still "10 chapters"). Gate does not require those rows (`check_release` PASS). Phase 13 / REL-19-01 owns full surface sync.
- **NOTE-2 (thin-register honesty):** `catalog.json` `dod-vva-rpg.chapters` left at **10** while disk has **13**. 11-02-SUMMARY records this as Phase 13. Not a map-apply input.
- **NOTE-3 (ROADMAP Plans TBD):** Phase 11 detail still says `**Plans**: TBD` even though `11-01-PLAN.md` / `11-02-PLAN.md` exist. Phase 12 chain does not read that line.
- **NOTE-4 (STATE YAML hygiene):** Frontmatter still `status: planning`, `stopped_at: … ready to plan Phase 10`, `completed_phases: 1`. Body Deviations/Notes carry the Phase 11 bullet. Same class as Phase 10 NOTE-1.
- **NOTE-5 (map gate RED):** Expected. `is-gps-200n` + `nasa-std-8719-14` + `dod-vva-rpg` ch11–ch13 are the MAP-19-01 worklist. Do not "fix" the map in leftover Phase 11 commits.

## 7. Gate Results

- `python tooling/validate_pack.py` on `nasa-std-8719-14` / `is-gps-200n` / `dod-vva-rpg` → **PASS**
- `python tooling/check_release.py` → **PASS** (plugin **1.18.0**)
- `python tooling/check_capability_map.py` → **FAIL** 19 issues (staleness of new packs + ch11–ch13) — Phase 12 start state
- `grep -c 'http' docs/SOURCE-VETTING.md` → **0**
- `grep -c '| GO —'` / `grep -c '| NO-GO —'` → **3 / 3**
- ROADMAP `- [ ] **Phase 11: IO-unlocking packs + Decision Analysis remap**` → still unchecked
- IO-01..07 boxes → all `- [ ]`; IO-05/06 `DEFERRED`; IO-07 `ACCEPT`
- Remap files exist: `packs/federal-bca/chapters/ch04-uncertainty-and-sensitivity.md`, `ch06-reporting-and-decision-use.md`, `packs/dod-vva-rpg/chapters/ch06-accreditation-agent-role.md`
- No `packs/dodm-5000-102`, no Army CBA / AAF / SP-7084 pack
- `docs/capability-pack-map.json` untouched since `dc35907`

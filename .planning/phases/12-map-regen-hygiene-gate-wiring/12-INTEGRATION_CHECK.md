# Phase 12 Integration Check — Map regen + hygiene + gate wiring

**Phase:** 12-map-regen-hygiene-gate-wiring (Wave A regen/remap/floor/CONTRACT + Wave B check_release wire + HYG-01..04)
**Scope of audit:** cross-phase wiring only — can Phase 13 ship without re-guessing the map, and will a stale map fail `check_release`?
**Method:** adversarial — every expected connection traced end-to-end (Phase 11 remap table → live JSON membership → CONTRACT → check_release import → Phase 13 leftovers), not checked for existence.

**Verdict:** PASS_WITH_NOTES

---

## 1. Wiring Summary

| # | Expected connection | Status | Evidence |
|---|---------------------|--------|----------|
| 1 | 11-02-SUMMARY IO-01 remap table ↔ live map membership (MOVE, not copy) | WIRED | Three locked files sit **only** in Decision Analysis & Trade Studies. Opportunity no longer holds federal-bca ch04/ch06. Assurance no longer holds dod-vva-rpg ch06. Unique `(pack, chapter)` = 644 / 644 (0 dups). |
| 2 | Phase 11 leave-in-place rows still in original clusters | WIRED | federal-bca ch01–ch03, ch05 + 3 support files still Opportunity (10→8). dod-vva-rpg ch08 still Validation. ch10 still Risk. |
| 3 | Phase 11 new slugs + leftover RPG ch11–ch13 classified (MAP-19-01) | WIRED | 16/16 SUMMARY classifications match live JSON. nasa-std-8719-14 all 7 → Ops/Maint/Disposal. is-gps-200n ch01 → CM; ch02–ch06 → Interfaces. leftover RPG ch11 → T&E; ch12+ch13 → Validation. New-pack support-file rows = 0. |
| 4 | Chapter-set freshness (disk vs JSON) | WIRED | Disk chapters 536; map chapters (support excluded) 536; `on_disk_only=0`, `map_only=0`. 63 mapped packs. Envelope schema 2 / `map_version` 1.18.0 / `generated_on` 2026-08-17 / 644 entries. |
| 5 | MAP-19-02 floors + listed-primary conjunct | WIRED | THRESHOLDS name-keyed ≥4 for DA / Validation / Integration / Interfaces / Ops. Live: DA 5/4, Validation 7/4, Integration 4/4, Interfaces 9/4, Ops 13/5. None is `<4 AND 1 pack`. Integration held; no AAF raid. |
| 6 | CONTRACT for se-agents (MAP-19-05) | WIRED | `docs/capability-map-CONTRACT.md` §6: live **628+** / post-regen **644**; **502** residue; Cybersecurity 69/10 + Digital Engineering 25/4 **unbound** (se-agents-side). §4 says `check_release.py` invokes `main()` in-process. |
| 7 | `check_release` includes map so Phase 13 cannot ship a stale map (MAP-19-04) | WIRED | `tooling/check_release.py` §5d imports `check_capability_map.main()` after cursor-manifest, `fail()`s on non-zero. Both gates exit **0**. Cluster-count block prints inside `check_release`. |
| 8 | catalog.json still 63 / dod-vva-rpg.chapters still 10 (Phase 13 owns bump) | WIRED (leftover) | catalog **63** (includes both GO slugs). `dod-vva-rpg.chapters` **10** vs disk **13**. dirs **65** (dirs−catalog = `{omg-signpost, se-standards-signpost}`). Not a Phase 12 gap. |
| 9 | Version trio + tag leftover for Phase 13 | WIRED (leftover) | plugin **1.18.0**; CHANGELOG still `## [1.18.0]` (no `[1.19.0]`); RELEASE-INFO **1.18.0**; `map_version` **1.18.0**; `git tag -l 'v1.19*'` empty. |
| 10 | ROADMAP Phase 12 still unchecked (verify closes it); Phase 13 depends on 12 | WIRED | `- [ ] **Phase 12: Map regen + hygiene + gate wiring**`. `- [ ] **Phase 13: Release surface + v1.19.0**`. Phase 11 remains `[x]`. MAP-19/HYG boxes still `- [ ]`. |

---

## 2. Handoff consumption (Phase 13 does not re-guess)

Phase 13 planner inputs, all already decided:

| Input | Consume as | Do not re-open |
|---|---|---|
| Live map 644 / schema 2 / DA 5/4 | Frozen membership for REL-19-01 gate run | Re-classify 16 chapters; copy remap rows back to Opportunity/Assurance |
| MAP-19-03 MOVE applied | federal-bca ch04+ch06 + dod-vva-rpg ch06 live only in Decision Analysis | Re-pick which A-94 / VV&A chapters move |
| `check_release.py` §5d map import | Ship gate — a stale map fails release | Unwire; treat map as optional docs |
| CONTRACT §6 628+/644 / 502 residue / Cyber+DE unbound | se-agents consumer note already landed | Bind Cyber/DE in this repo; rewrite 502 as live |
| catalog 63 + `dod-vva-rpg.chapters` 10 | REL-19-01 full-register leftover (bump RPG to 13; README new-slug rows) | Treat 10 as truth; invent new slugs |
| plugin / CHANGELOG / RELEASE-INFO 1.18.0 | REL-19-02 version trio + `v1.19.0` tag + GitHub Release | Bump in leftover Phase 12 commits |
| IO-05/06 DEFERRED; IO-07 ACCEPT | No AAF / stakeholder pack to classify | Raid Integration; invent AAF/CBA/DoDM pack |
| HYG-03 sibling PR #2 | Recorded external sync; merge not required | Vendor `vet_source.py` into this repo |

Leave federal-bca ch01–ch03, ch05 + support files in Opportunity. Leave dod-vva-rpg ch08 in Validation and ch10 in Risk. Result after apply (already live): Decision Analysis 2→5 entries, 2→4 packs.

---

## 3. E2E Flow Trace: Phase 11 packs/remap → Phase 12 apply/wire → Phase 13 release

1. 11-02-SUMMARY IO-01 table named three files + From clusters → live JSON MOVEd all three into Decision Analysis only — VERIFIED (membership + 0 dups)
2. Phase 11 GO slugs `nasa-std-8719-14` (7) + `is-gps-200n` (6) + leftover RPG ch11–ch13 exist on disk → all 16 classified; chapter-set empty — VERIFIED
3. MAP-19-02 floors encoded name-keyed; listed primaries all `floor_fail=False`; Integration 4/4 held — VERIFIED (`check_capability_map.py` PASS)
4. CONTRACT §6 paragraph + §4 wired sentence landed for se-agents — VERIFIED (628 / 502 / Cybersecurity / Digital Engineering / unbound / `check_release.py`)
5. `check_release.py` in-process import of `check_capability_map.main()`; both gates PASS — VERIFIED (exit 0 / 0)
6. Hygiene landed without stealing REL-19: CHANGELOG no BOM / LF / still `[1.18.0]`; `.gitattributes` `*.md text eol=lf`; four SKILL nits; federal-bca `(c)` enumeration-markers; no `tooling/vet_source.py` — VERIFIED
7. Phase 13 leftovers intact: catalog 63 / RPG chapters 10 / README no new-slug rows / version trio 1.18.0 / no `v1.19.0` tag — VERIFIED
8. SOURCE-VETTING `http` = 0; no generator; no forbidden packs; CI still does not exec repo Python — VERIFIED

No break in the chain. Flow status: COMPLETE for Phase 13 consumption. A stale map now fails the ship gate.

---

## 4. Requirements Integration Map

| Requirement | Integration path | Status | Issue |
|---|---|---|---|
| IO-01 | 11-02 table → MAP-19-03 MOVE → DA 5/4 live | WIRED | REQUIREMENTS note still says "Live count leave-2 is Phase 12" (stale pointer; see NOTE-5) |
| IO-02 | leftover RPG ch11–ch13 on disk + in map (T&E / Validation / Validation) | WIRED | Catalog/README still say 10 chapters (Phase 13 / NOTE-1) |
| IO-03 | `nasa-std-8719-14` 7 chapters → Ops/Maint/Disposal | WIRED | README live-pack row missing (Phase 13 / NOTE-2) |
| IO-04 | `is-gps-200n` 6 chapters → CM + Interfaces | WIRED | same as IO-03 |
| IO-05 | DEFERRED; Integration held 4/4; no AAF pack | WIRED | — |
| IO-06 | DEFERRED; no AAF pack | WIRED | — |
| IO-07 | ACCEPT; no invented stakeholder pack | WIRED | — |
| MAP-19-01 | 644 entries / 63 packs / chapter-set empty / gate PASS | WIRED | Box still `- [ ]` (verify) |
| MAP-19-02 | THRESHOLDS ≥4; conjunct none of five primaries is `<4 AND 1 pack` | WIRED | Box still `- [ ]` (verify) |
| MAP-19-03 | three-row MOVE applied; old clusters vacated | WIRED | Box still `- [ ]` (verify) |
| MAP-19-04 | `check_release` imports `main()`; fail on non-zero | WIRED | Box still `- [ ]` (verify) |
| MAP-19-05 | CONTRACT §6 628+/644 / 502 / Cyber+DE unbound | WIRED | Box still `- [ ]` (verify) |
| HYG-01..04 | BOM/LF pin + four SKILL nits + `(c)` wording + sibling PR #2 | WIRED | Boxes still `- [ ]` (verify); sibling merge not required |
| REL-19-01 | catalog chapter integer + README slugs + both gates at updated basis | FORWARD-REF | Phase 13 — not a Phase 12 gap |
| REL-19-02 | version trio 1.19.0 + tag + GitHub Release | FORWARD-REF | Phase 13 — not a Phase 12 gap |

**Requirements with no cross-phase wiring:** none in Phase 12 scope.

---

## 5. SUMMARY ledger classification

| Plan | Ledger entry | Classification | Wiring impact |
|---|---|---|---|
| 12-01 | `## Deviations` = None. / `None - plan executed exactly as written.` | no deviation | None. Remap rows locked; 16 classifications match SUMMARY table. |
| 12-02 | `## Deviations` = None. / `None - plan executed exactly as written.` | no deviation | None. Wire + hygiene landed; version trio untouched. |

No WINDOWS.md in this phase (none required; none present).

---

## 6. Findings

**BLOCKERS:** none.

**WARNINGS:** none that break Phase 13 consumption.

**NOTES:**

- **NOTE-1 (catalog chapter integer):** `catalog.json` `dod-vva-rpg.chapters` left at **10** while disk + map have **13**. 11-02-SUMMARY and both Phase 12 SUMMARYs record this as Phase 13 / REL-19-01. Not a map-apply input.
- **NOTE-2 (README live-pack table):** Badge is `packs-63` but the live-pack table still ends at `mil-std-40051` (no `nasa-std-8719-14` / `is-gps-200n` rows; `dod-vva-rpg` still "10 chapters"). Gate does not require those rows (`check_release` PASS). Phase 13 / REL-19-01 owns full surface sync.
- **NOTE-3 (version trio + tag):** plugin / CHANGELOG top / RELEASE-INFO / `map_version` still **1.18.0**. No `## [1.19.0]`. No `v1.19.0` tag. Phase 13 / REL-19-02 owns the bump. `check_release` now includes the map, so Phase 13 cannot ship 1.19.0 against a stale map.
- **NOTE-4 (ROADMAP / REQUIREMENTS boxes):** Phase 12 checkbox and MAP-19/HYG boxes remain `- [ ]`. Verify closes them. Phase 13 chain does not read those ticks.
- **NOTE-5 (stale IO-01 pointer):** REQUIREMENTS IO-01 still says "Live count leave-2 is Phase 12." Live DA is now **5/4**. Annotation lag only; remap table + JSON agree.
- **NOTE-6 (HYG-03 sibling PR):** https://github.com/jgsystemsconsulting/jgs-reference-skill/pull/2 recorded; merge not required for Phase 12 close (ROADMAP SC-4 / 12-02 plan). `tooling/vet_source.py` absent here.
- **NOTE-7 (CI does not exec repo Python):** `.github/workflows/validate.yml` still "never executes checked-out repository code." Map freshness is a **local/trusted** `check_release` duty. Do not add a CI repo-Python step in Phase 13 leftovers.

---

## 7. Gate Results

- `python tooling/check_capability_map.py` → **PASS**, exit 0, TOTAL **644**
- `python tooling/check_release.py` → **PASS**, exit 0 (prints the same cluster-count block, then `RELEASE CHECK: PASS`)
- chapter-set `(pack, chapter)` set-diff → `on_disk_only=0`, `map_only=0` (536 / 536); support-file rows 108; new-pack support rows 0
- DA membership 5/4 matches locked five-row set; MOVE not copy
- Opportunity 8/2 (federal-bca ch04+ch06 vacated); Assurance no longer holds dod-vva-rpg ch06; ch08 Validation; ch10 Risk
- Conjunct: DA 5/4, Validation 7/4, Integration 4/4, Interfaces 9/4, Ops 13/5 — no listed primary is `<4 AND 1 pack`
- CONTRACT contains 628, 644, 502, Cybersecurity, Digital Engineering, unbound
- catalog **63**; `dod-vva-rpg.chapters` **10**; dirs **65**; cursor skills **64**; SKILLS header **63 (+2 signposts)**
- plugin **1.18.0**; CHANGELOG no BOM, 0 CRLF, still `## [1.18.0]`; RELEASE-INFO **1.18.0**; `map_version` **1.18.0**
- `.gitattributes` is exactly `*.md text eol=lf`
- `grep -c 'http' docs/SOURCE-VETTING.md` → **0**
- ROADMAP `- [ ] **Phase 12: Map regen + hygiene + gate wiring**` → still unchecked
- ROADMAP `- [ ] **Phase 13: Release surface + v1.19.0**` → unchecked (depends on Phase 12)
- MAP-19-01..05 and HYG-01..04 boxes → all `- [ ]`
- No `packs/dodm-5000-102`, no Army CBA / AAF / SP-7084 / IS-300 pack
- No generator; no `tooling/vet_source.py`; no `v1.19*` tag

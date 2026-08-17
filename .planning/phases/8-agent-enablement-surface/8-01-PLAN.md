---
phase: 8-agent-enablement-surface
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - tooling/check_capability_map.py
  - docs/capability-pack-map.json
  - docs/capability-pack-map.md
  - docs/capability-map-CONTRACT.md
autonomous: true
requirements: [AE-01, AE-02, AE-03]

estimate:
  tokens: 90000
  raw_tokens: 60000
  tasks: 5
  confidence: low

must_haves:
  truths:
    - "check_capability_map.py exits 0 against the regenerated map and non-zero against the pre-phase keyless map"
    - "docs/capability-pack-map.json carries schema_version==2, map_version=='1.18.0', and a generated_on ISO date"
    - "All 61 chapter-bearing packs (54 pre-existing + 7 GP packs) appear in at least one map entry"
    - "Cluster 'Training & Documentation Delivery' has >=1 entry; 'Requirements Traceability & Allocation' >=3; 'Interface Management & ICIDs' >=3; 'Opportunity/Benefit Management' >=2"
    - "docs/capability-map-CONTRACT.md documents schema, versioning, v1 deprecation, refresh path, and threshold table, and is linked from docs/capability-pack-map.md"
    - "Running the gate twice on an unchanged tree produces identical output (idempotent validation)"
  artifacts:
    - tooling/check_capability_map.py
    - docs/capability-pack-map.json (v2 envelope, 7 new packs classified)
    - docs/capability-pack-map.md (summary table + changelog updated)
    - docs/capability-map-CONTRACT.md
  key_links:
    - Gate reads docs/capability-pack-map.json and packs/ filesystem — staleness detection is live, not snapshot-based
    - Threshold asserts resolve clusters by NAME (lookup table), never by array index — survives cluster renumbering
    - capability-pack-map.md rules-of-construction block links to capability-map-CONTRACT.md
---

<objective>
Make docs/capability-pack-map.json a stable, versioned consumable for the se-agents generator:
add the v2 metadata envelope, classify the 52 new chapters of the 7 Phase-7 GP packs into the 32
capability clusters per the map's own rules of construction, gate the result with a stdlib
validator (tooling/check_capability_map.py), and document the downstream contract.

Purpose: ROADMAP Phase 8 goal — the map becomes the versioned input the se-agents generator
reads (ROLE-AGENTS-REQUIREMENTS-V2 FR-2.1/FR-2.3), and the thin-cluster fattening promised in
Phase 7 SC-3 is verified (cluster 25 non-empty; clusters 3/5/15 above critical thresholds).
Output: gate script + regenerated map JSON/md + contract doc (AE-01, AE-02, AE-03).
</objective>

<execution_context>
@$HOME/.zcode/gsd-core/workflows/execute-plan.md
@$HOME/.zcode/gsd-core/templates/summary.md
</execution_context>

<context>
@.planning/ROADMAP.md
@.planning/STATE.md
@.planning/phases/8-agent-enablement-surface/8-RESEARCH.md
@docs/capability-pack-map.md
@docs/capability-pack-map.json
@tooling/check_release.py
</context>

<claim_verification>
| claim | command | observed | status |
|---|---|---|---|
| Map JSON is keyless v1 (no schema_version) with 32 clusters / 570 entries | `python -c "import json; d=json.load(open('docs/capability-pack-map.json')); print(list(d.keys()), len(d['clusters']), sum(len(c['chapters']) for c in d['clusters']))"` | `['clusters'] 32 570` | VERIFIED |
| Exactly 7 packs missing from map; 0 stale entries | `python -c "import json,pathlib; d=json.load(open('docs/capability-pack-map.json')); m={e['pack'] for c in d['clusters'] for e in c['chapters']}; p={x.name for x in pathlib.Path('packs').iterdir() if (x/'chapters').exists()}; print(len(m),len(p),sorted(p-m),sorted(m-p))"` | 54 mapped, 61 on-disk, missing = dafman-63-119, dod-vva-rpg, dote-te-guidebook, faa-std-025, federal-bca, mil-std-40051, mil-std-881f; stale = [] | VERIFIED |
| New-pack chapter counts are 10/8/8/7/7/6/6 (=52) | `python -c` glob over packs/*/chapters | dod-vva-rpg 10, dote-te-guidebook 8, mil-std-40051 8, dafman-63-119 7, mil-std-881f 7, faa-std-025 6, federal-bca 6 | VERIFIED |
| Baseline thin clusters: 25=0, 3=2, 5=2, 15=1 | summary table in docs/capability-pack-map.md + 8-RESEARCH.md "Current state" | 25→0, 3→2, 5→2, 15→1 | VERIFIED |
| Support-file entries use the literal suffix "(support file)" in chapter field | python filter over entries | 102 entries, e.g. `{'pack': 'requirements-writing', 'chapter': 'glossary.md (support file)', ...}` | VERIFIED |
| tooling/ convention: stdlib-only, check_release.py header style, ROOT via `Path(__file__).resolve().parent.parent` | `head -12 tooling/check_release.py` | docstring header, usage, exit non-zero on failure | VERIFIED |
</claim_verification>

<tasks>

<task type="auto">
  <name>Task 1: Write tooling/check_capability_map.py and confirm it fails RED on the current map</name>
  <files>tooling/check_capability_map.py</files>
  <action>
Write `tooling/check_capability_map.py` (~80 lines, Python stdlib only, check_release.py
docstring-header style with usage line, `ROOT = Path(__file__).resolve().parent.parent`,
exit 0 on pass / 1 on any failure) implementing exactly the 8-RESEARCH.md §2 design:

1. Load `ROOT/docs/capability-pack-map.json` (utf-8). Hard-fail if top-level
   `schema_version` is missing or != 2, or if `map_version` / `generated_on` are missing
   (`generated_on` must merely be present and non-empty — no freshness assert, per research).
2. Staleness vs `packs/`: every pack directory under `ROOT/packs/` that contains a
   `chapters/` subdirectory must appear as the `pack` value in >=1 entry (this naturally
   excludes the two signpost packs, which have no chapters dir); conversely every referenced
   pack must have a chapters dir on disk.
3. File existence: for each entry, strip the literal suffix ` (support file)` from the
   `chapter` value when present, then assert `ROOT/packs/<pack>/chapters/<chapter>` exists
   (catches deleted/renamed chapters). Do NOT require support files to be present or absent
   for any pack — single-cluster judgment stays agent-side (research §4 risk 2).
4. Counts: print one line per cluster (name + entry count) and the total; assert
   sum of per-cluster counts == total entries (double-count guard).
5. Threshold asserts by cluster NAME via a module-level lookup table (never array index;
   unknown name -> loud non-zero failure, per research §4 risk 4):
   - "Training & Documentation Delivery" >= 1
   - "Requirements Traceability & Allocation" >= 3
   - "Interface Management & ICIDs" >= 3
   - "Opportunity/Benefit Management" >= 2

Then RUN it against the CURRENT (pre-regeneration) map and record the red output in the
summary: it must fail for exactly the expected reasons — missing `schema_version` envelope
AND the 7 missing packs (dafman-63-119, dod-vva-rpg, dote-te-guidebook, faa-std-025,
federal-bca, mil-std-40051, mil-std-881f) — proving the staleness path works. Paste the red
output into the commit message body. Keep the script standalone (no import of check_release)
per research §2 wiring recommendation; Phase 9 may wire it into check_release.
  </action>
  <verify>
    <automated>python tooling/check_capability_map.py; echo "exit=$?" — against the current map expects exit=1 with schema_version + 7 missing-pack failures named</automated>
  </verify>
  <done>Script exists, is stdlib-only, and its RED run names exactly: missing schema_version and the 7 unclassified packs. Committed.</done>
</task>

<task type="auto">
  <name>Task 2: Classify the 52 new chapters + support files; add v2 envelope; sync md summary + changelog</name>
  <files>docs/capability-pack-map.json, docs/capability-pack-map.md</files>
  <action>
Regenerate docs/capability-pack-map.json per 8-RESEARCH.md §2/§3 step 2 — an agent pass, not
a script (judgment required):

1. For each of the 7 new packs — dod-vva-rpg (10 ch), dote-te-guidebook (8), mil-std-40051 (8),
   dafman-63-119 (7), mil-std-881f (7), faa-std-025 (6), federal-bca (6) = 52 chapters —
   read the chapter files (titles/leads suffice) and the pack's SKILL.md When-to-use, then
   assign every chapter to exactly one of the 32 existing clusters (best fit) following the
   rules of construction in docs/capability-pack-map.md: cross-cutting chapters carry a remark
   noting the strong secondary fit; a standard's own process definitions go to cluster 30
   ("Standards, Tailoring & Process Models") while performing the capability goes to the
   capability cluster; expected heavy routing per research: mil-std-40051 -> cluster 25
   (Training & Documentation Delivery), federal-bca -> cluster 15 (Opportunity/Benefit
   Management), faa-std-025 -> cluster 25; dote-te-guidebook feeds clusters 3/5 (T&E /
   traceability / interface chapters). Every entry gets a one-line `note` like existing rows.
   Threshold targets that the assignments must land: cluster 25 >= 1, cluster 3 >= 3
   (baseline 2), cluster 5 >= 3 (baseline 2), cluster 15 >= 2 (baseline 1).
2. Support files: for each new pack judged essentially single-cluster, add
   glossary.md / patterns.md / cheatsheet.md entries with chapter value
   `<filename> (support file)` (same shape as the 102 existing support-file rows);
   multi-cluster packs' support files are omitted.
3. Add the v2 envelope from research §1 — exactly three new top-level keys:
   `"schema_version": 2` (int, not string), `"map_version": "1.18.0"`,
   `"generated_on": "2026-08-14"` — leaving `clusters`/`name`/`chapters`/`pack`/`chapter`/
   `note` byte-identical in shape so `data["clusters"]` consumers keep working.
4. Update docs/capability-pack-map.md: refresh the summary table counts (+ changelog line
   "Changelog (v1.18.0): added dod-vva-rpg, dote-te-guidebook, mil-std-40051, dafman-63-119,
   mil-std-881f, faa-std-025, federal-bca" — keep or fold the v1.17.0 line per the existing
   single-changelog-line convention) and update the JSON section body if one exists.
5. Spot-check protocol (mandatory, per research §4 risk 1): for EACH new pack, re-read its
   SKILL.md When-to-use and confirm every chapter assignment is defensible; record the
   spot-check (3 chapters per pack re-read, with the rationale) in the task summary.
  </action>
  <verify>
    <automated>python -c "import json; d=json.load(open('docs/capability-pack-map.json')); assert d['schema_version']==2 and d['map_version']=='1.18.0' and d['generated_on']; c={x['name']:len(x['chapters']) for x in d['clusters']}; assert c['Training & Documentation Delivery']>=1 and c['Requirements Traceability & Allocation']>=3 and c['Interface Management & ICIDs']>=3 and c['Opportunity/Benefit Management']>=2; print('envelope+thresholds OK', sum(c.values()), 'entries')"</automated>
  </verify>
  <done>Map JSON has v2 envelope, all 61 chapter-bearing packs represented (570 + 52 chapters + support files = total), clusters 25/3/5/15 above thresholds, md table + changelog synced, spot-check recorded. Committed.</done>
</task>

<task type="auto">
  <name>Task 3: Gate green — check_capability_map.py exits 0 including threshold asserts</name>
  <files></files>
  <action>
Run `python tooling/check_capability_map.py` against the regenerated map. It must print all
32 per-cluster counts + total and exit 0: schema envelope present, zero staleness vs packs/
(the 7 new packs now mapped, no referenced file missing), cluster-sum == total, and all four
NAME-keyed threshold asserts passing. Then run it a SECOND time unchanged and diff the two
outputs — must be byte-identical (idempotent validation of the committed artifact, per
research §2 idempotence note). If any threshold fails, return to Task 2 assignments — do NOT
weaken the thresholds. Record the green output in the summary. (No file changes expected in
this task; if the gate exposes a map defect, fix it in the map files and note that here.)
  </action>
  <verify>
    <automated>python tooling/check_capability_map.py && python tooling/check_capability_map.py | diff - <(python tooling/check_capability_map.py) && echo GATE_GREEN_IDEMPOTENT</automated>
  </verify>
  <done>Gate exits 0 twice with identical output; per-cluster counts and total recorded in summary. Committed (or documented no-change if gate passed without edits).</done>
</task>

<task type="auto">
  <name>Task 4: Write docs/capability-map-CONTRACT.md and link it from the map header</name>
  <files>docs/capability-map-CONTRACT.md, docs/capability-pack-map.md</files>
  <action>
Create `docs/capability-map-CONTRACT.md` (~60 lines) — the citable standalone artifact for
the se-agents generator repo (per 8-RESEARCH.md §3 step 4 recommendation; deliberately NOT a
PACK-SPEC.md section, which governs pack structure not cross-repo consumption). Contents:

1. Schema: the v2 JSON shape (schema_version int, map_version string, generated_on ISO date,
   clusters[] of {name, chapters[] of {pack, chapter, note}}) with the note that consumers
   read cluster name -> list of {pack, chapter} (FR-2.1) and should check
   `schema_version == 2` first.
2. Versioning rule: schema_version bumps only on breaking shape change (envelope additions
   are additive and do not bump); map_version tracks the release that regenerated the map
   (v1.17 map implicitly = 1.17.0).
3. Deprecation: the v1 keyless shape (top level = {"clusters": ...} only) is DEPRECATED;
   v1 consumers must read `schema_version` first; `data["clusters"]` access still works on v2.
4. Refresh path: agent classification pass per the rules of construction in
   docs/capability-pack-map.md -> run `python tooling/check_capability_map.py` (must exit 0,
   includes staleness vs packs/ and the threshold table) -> commit both .json and .md.
5. Threshold table: the four name-keyed minimums (Training & Documentation Delivery >= 1;
   Requirements Traceability & Allocation >= 3; Interface Management & ICIDs >= 3;
   Opportunity/Benefit Management >= 2) with the note that thresholds resolve by cluster
   NAME, so renames fail loudly.

Then add one link line to the rules-of-construction block in docs/capability-pack-map.md
header: e.g. "Consumption contract (schema, versioning, refresh): see
docs/capability-map-CONTRACT.md."
  </action>
  <verify>
    <automated>grep -c "capability-map-CONTRACT.md" "docs/capability-pack-map.md" | grep -qv '^0$' && grep -c "schema_version" "docs/capability-map-CONTRACT.md" | grep -qv '^0$' && grep -c "deprecated" "docs/capability-map-CONTRACT.md" | grep -qv '^0$' && echo CONTRACT_LINKED</automated>
  </verify>
  <done>Contract doc exists covering schema/versioning/deprecation/refresh/thresholds; linked from the map md header. Committed.</done>
</task>

<task type="auto">
  <name>Task 5: Verify Phase 8 success criteria (AE-01..AE-03) and hand off</name>
  <files>.planning/phases/8-agent-enablement-surface/8-01-SUMMARY.md</files>
  <action>
Goal-backward verification against ROADMAP Phase 8 SCs; write the plan summary
(8-01-SUMMARY.md per the summary template) recording:

- SC-1 / AE-01: map JSON carries schema + version + generated-on (show the three keys);
  the gate is the idempotent staleness check (two identical green runs from Task 3, red run
  from Task 1 quoted as evidence the staleness path detects drift).
- SC-2 / AE-02: all v1.18 packs present (61 chapter-bearing packs mapped, 0 stale);
  final counts for clusters 25/3/5/15 vs baselines 0/2/2/1; the spot-check protocol results
  from Task 2.
- SC-3 / AE-03: contract documented at docs/capability-map-CONTRACT.md, linked from the map
  header — cite the five sections.
- Phase 9 handoff notes: the optional check_release.py §8 bullet ("map gate passes" via
  check_capability_map.py main()) is deferred to the Phase 9 release-surface plan per
  research §2 wiring recommendation; REL-1x-02 surfaces stay untouched here.
  </action>
  <verify>
    <automated>python tooling/check_capability_map.py && test -s ".planning/phases/8-agent-enablement-surface/8-01-SUMMARY.md" && grep -c "AE-0" ".planning/phases/8-agent-enablement-surface/8-01-SUMMARY.md" | grep -qv '^0$' && echo SC_VERIFIED</automated>
  </verify>
  <done>Summary file exists covering SC-1/2/3 with evidence, gate green, handoff notes recorded. Committed.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| repo files -> gate script | gate reads committed JSON + packs/ tree; malformed JSON must fail cleanly, not crash with traceback-only output |
| this repo -> se-agents consumer | map JSON is a cross-repo public contract; shape regressions break the downstream generator |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-8-01 | Tampering | docs/capability-pack-map.json | medium | mitigate | Gate validates schema_version==2, file existence of every referenced chapter, and staleness vs packs/ (Task 1) |
| T-8-02 | Tampering | threshold asserts | medium | mitigate | NAME-keyed lookup table, unknown cluster name -> loud non-zero (research §4 risk 4); thresholds never weakened to pass (Task 3 action) |
| T-8-03 | Repudiation | regeneration provenance | low | mitigate | map_version + generated_on envelope + v1.18.0 changelog line (Task 2) |
| T-8-04 | DoS | gate script on malformed JSON | low | mitigate | json.JSONDecodeError caught and reported as a named failure with exit 1, per tooling/ exit conventions |
| T-8-05 | Information disclosure | contract doc | low | accept | CONTRACT doc contains only public repo structure info; repo is MIT-licensed public content |
</threat_model>

<verification>
- `python tooling/check_capability_map.py` exits 0 (schema, staleness, existence, counts, thresholds).
- JSON asserts: schema_version==2, map_version=="1.18.0", generated_on present, 61 packs covered, cluster 25/3/5/15 minimums met.
- docs/capability-map-CONTRACT.md exists, linked from docs/capability-pack-map.md.
- Summary records red run, green runs, per-cluster counts, spot-check protocol.
</verification>

<success_criteria>
- AE-01: versioned, gate-checked map consumable (envelope + idempotent stdlib gate).
- AE-02: all v1.18 packs mapped; cluster 25 non-empty; clusters 3/5/15 above critical thresholds.
- AE-03: contract documented and linked for the se-agents generator repo.
</success_criteria>

<output>
Create `.planning/phases/8-agent-enablement-surface/8-01-SUMMARY.md` when done
</output>

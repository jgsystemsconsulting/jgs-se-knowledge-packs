# Phase 11: IO-unlocking packs + Decision Analysis remap — Research

**Researched:** 2026-08-17
**Domain:** Pack construction from Phase 10 GO sources; honest deferral of NO-GO IOs; remap spec for Decision Analysis (map JSON is Phase 12)
**Confidence:** HIGH on pipeline, GO/NO-GO, remap-vs-Phase-12 split, and catalog ownership. MEDIUM on exact leftover VV&A special-topic filenames (index is live; only the dropped T&E/V&V Checklist is named in-repo).

<user_constraints>
## User Constraints (from STATE / REQUIREMENTS / ROADMAP / Phase 10; no CONTEXT.md)

**CRITICAL:** Discuss was skipped. There is no CONTEXT.md. Locked decisions below are taken from STATE.md, REQUIREMENTS.md, ROADMAP.md, SEED-001, SOURCE-VETTING Phase 11 handoff, and 10-GAP Phase 11 Routing — these MUST be honored. Phase 10 GO/NO-GO is AUTHORITATIVE — do not re-vet.

### Locked Decisions

- **Build only GO names.** NASA-STD-8719.14C → `nasa-std-8719-14` (IO-03). IS-GPS-200N exemplar (IO-04). SP-7084 is optional Training-diversity only, not an IO-01..07 must. [VERIFIED: `docs/SOURCE-VETTING.md:168-177` — Phase 11 handoff table]
- **Army CBA is NO-GO.** Do not build a CBA pack. IO-01 remaps existing A-94 / VV&A decision chapters. [VERIFIED: `.planning/REQUIREMENTS.md:21` — "Phase 10 handoff: Army CBA is NO-GO; take the remap existing A-94 / VV&A decision chapters path. Do not invent a CBA pack."]
- **DoDM 5000.102 is NO-GO.** Do not create `dodm-5000-102`. IO-02 = additional chapters in existing `dod-vva-rpg`. [VERIFIED: `.planning/REQUIREMENTS.md:22`]
- **AAF stays unused.** IO-05 / IO-06 record deferred. No AAF pack. `dod-rio` AAF chapters do not licence AAF guidebooks. [VERIFIED: `.planning/REQUIREMENTS.md:25-26`; `docs/SOURCE-VETTING.md:176`]
- **IO-07: no invented pack.** Record SEBoK-expansion-or-accept. [VERIFIED: `.planning/REQUIREMENTS.md:27`]
- **Tier 1 leaning is not skip-build-time-confirm.** 8719.14C needs third-party insert scan on the extracted copy; IS-GPS-200N needs DIST-A on the extracted copy. [VERIFIED: `docs/SOURCE-VETTING.md:142` — "Tier 1 leaning still requires Phase 11 build-time in-source confirmation on the copy actually extracted."]
- **No source URLs in packs or `docs/`.** URLs live only in `.planning` research. [VERIFIED: `docs/LICENSING.md:72-73`; `docs/SOURCE-VETTING.md:95-97`]
- **MAP-19-01..05 and HYG-01..04 are Phase 12.** REL-19-01/02 are Phase 13. [VERIFIED: `.planning/ROADMAP.md:60-84`]
- Stay on `main`. No branches / worktrees.

### Claude's Discretion

- Whether to thin-register new packs in Phase 11 so `check_release.py` stays green, or leave registration to Phase 13 (see §Catalog). Recommendation: thin-register **new pack dirs only** if they land on `main`; do not steal version bump / CHANGELOG / GitHub Release.
- Whether IO-04 adds optional IS-GPS-705J / 800J. Recommendation: **no** (YAGNI; one exemplar).
- Whether to build SP-7084. Recommendation: **no** (YAGNI; not an IO must).
- Exact leftover VV&A chapter set for IO-02 (beyond the already-named T&E/V&V Checklist).
- IO-07: SEBoK-expansion (Phase 12 rematch of existing SEBoK chapters) vs accept. Recommendation: **accept**.

### Deferred Ideas (OUT OF SCOPE)

- Capability-map regen, MAP-19-02 floor assert, MAP-19-04 gate wiring, CONTRACT.md 502 note (Phase 12)
- Version surface / GitHub Release (Phase 13)
- NASA-HDBK-2203 / NPR 7150.2 (REQUIREMENTS Out of Scope) [VERIFIED: `.planning/REQUIREMENTS.md:57`]
- Per-role packs; se-agents consumer refresh; FUT-05; committed overlap checker
- Inventing a Stakeholder Engagement or generic CBA pack
- Using AAF / WarU / DAG substitutes
- Searching for IS-300 or packaging ICD-GPS-153
</user_constraints>

<architectural_responsibility_map>
## Architectural Responsibility Map

Single-tier content library — no Browser/Client, API, or Database runtime. Phase 11 capabilities live in pack trees + planning records.

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| New pack synthesis (IO-03, IO-04) | `packs/<slug>/` | gitignored `sources/<slug>/` | PACK-SPEC layout; sources never commit |
| Existing-pack chapter add (IO-02) | `packs/dod-vva-rpg/` | `sources/dod-vva-rpg/` (chapter-wise) | Same P7-PRE-4 model; do not scaffold a second pack |
| IO-01 remap specification | This RESEARCH + Phase 11 SUMMARY / REQUIREMENTS annotation | Phase 12 `docs/capability-pack-map.json` | Map JSON is MAP-19-03; Phase 11 must not double-build |
| Honest deferral / accept records (IO-05/06/07) | REQUIREMENTS + STATE + Phase 11 SUMMARY | SOURCE-VETTING already carries NO-GO | No silent ticks |
| Thin registration (if taken) | `catalog.json`, `SKILLS.md`, `NOTICE`, `.cursor-plugin/plugin.json`, `docs/packs.html` | README badge | Only if new dirs land on `main`; version surfaces stay Phase 13 |
| Mechanical gates | `tooling/validate_pack.py` + sibling scan/overlap | `tooling/check_release.py` | SC-5; release gate is count-sensitive |
</architectural_responsibility_map>

<research_summary>
## Summary

Phase 11 fattens the poorest competency *primaries* from what Phase 10 cleared. Live map (schema 2, `1.18.0`, 628 entries) still has Decision Analysis at **2 entries / 2 packs** (`nasa-ceh` + `nasa-se-handbook` only). Validation is 5/4, Interfaces 4/3, Ops/Maint/Disposal 6/4, Integration 4/4, Logistics 12/2, Stakeholder 3/3. [VERIFIED: live `docs/capability-pack-map.json` clusters, 2026-08-17]

**Build (2 new packs):** `nasa-std-8719-14` from NASA-STD-8719.14C (77 pp, born-digital, Internet Public) and an **ICD exemplar** `is-gps-200n` from IS-GPS-200N (DIST-A; select interface-definition chapters — not the NAV-bit appendices). **Extend (1 existing pack):** add 2–4 leftover VV&A RPG chapters to `dod-vva-rpg` (start with the T&E/V&V Checklist already dropped as selection, not licence). **Remap (no new pack):** IO-01 is a **Phase 12 MAP-19-03** apply of a Phase 11-written chapter list — do not edit the map JSON here and do not invent a CBA pack. **Defer/accept:** IO-05/06 AAF deferred; IO-07 accept (no SEBoK pack invention); SP-7084 skip.

Each built/extended pack still owes the Phase 7 gate chain: PACK-SPEC + `validate_pack` + scan + overlap + `## When to use` + `**Prerequisites:**`. Catalog/version/release surfaces stay Phase 13 unless new dirs would break `check_release.py` on `main` (thin-register exception).
</research_summary>

<standard_stack>
## Standard Stack

This repo does not add a library for pack builds. Copy the Phase 3 / Phase 7 pipeline.

### Core

| Artifact | Version / location | Purpose | Why standard |
|---------|--------------------|---------|--------------|
| Phase 7 pipeline | `.planning/phases/7-gap-driven-pack-builds/7-RESEARCH.md` §2 | extract → outline → scaffold → generate → validate → scan → overlap | Proven on 7 GP packs |
| `docs/PACK-SPEC.md` | living | Required layout + SKILL.md contract + PACK.yaml schema | CI / validate_pack authority |
| `tooling/build_pack.py` | repo wrapper (no `--out-dir`; targets `./packs`) | Scaffold only; refuses if slug exists | Provenance stub |
| `$REF/tools/build_pack.py` | sibling `jgs-reference-skill` | Scaffold with `--out-dir packs` | What Phase 7 actually invoked |
| `tooling/validate_pack.py` | repo | Structure + mandatory PACK.yaml fields + `license_tier ∈ {1,2,3}` | SC-5 |
| `$REF/tools/vet_source.py` | sibling | Mechanical licence classifier at build | Exit 2 = Excluded |
| `$REF/scripts/extract.py` | sibling | PDF → `book_skill_work/{full_text.txt,metadata.json}` | `--mode technical --install-missing no` |
| `$REF/tools/outline.py` | sibling | Deterministic offsets | Skip for chapter-wise RPG adds |
| `$REF/tools/scan_generated_skill.py` | sibling | Advisory quality scan | Disposition in PACK.yaml notes |
| `$REF/tools/check_overlap.py` | sibling | Verbatim-run licence-safety gate | Exit 0 mandatory |
| `tooling/check_release.py` | repo | Local release gate (counts, links, RR-S-13) | Breaks if pack dirs increment without SKILLS/cursor |
| `tooling/check_capability_map.py` | repo | Map envelope + staleness | **Not** wired into check_release yet (MAP-19-04 = Phase 12) [VERIFIED: `tooling/check_capability_map.py:16-17`] |

`$REF` = `C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill`. On Windows/Git Bash use `python`.

### Licence strings (exact)

- Default NASA / statute: `Public Domain (US Government work, 17 U.S.C. § 105)`
- GPS / DoD DIST-A variant: `Public Domain (US Government work, 17 U.S.C. § 105; Distribution Statement A — Approved for public release; distribution is unlimited)`

Common PACK.yaml flags for these US-gov works: `license_tier: 1`, `commercial_use: true`, `share_alike: false`, `attribution_required: false`.

### Supporting

| Artifact | Purpose | When to use |
|---------|---------|-------------|
| `sources/<slug>/` | Gitignored PDF + extract work dirs | Every build [VERIFIED: `.gitignore:17` — `sources/`] |
| `work_dir.txt` convention | `printf '%s'` write, `tr -d '\r\n'` read | Capture `%TEMP%` book_skill_work path |
| chars/page floor ≥ 300 | `len(full_text)/metadata.json pages` | Halt on scan/placeholder PDF |
| `docs/SOURCE-VETTING.md` v1.19 rows | Published tier; no URLs | Quote Internet Public / DIST-A into PACK.yaml notes |
| Analog packs | `packs/nasa-ms-7009/` (NASA STD), `packs/faa-std-025/` (ICD family), `packs/dod-vva-rpg/` (IO-02 extend), `packs/federal-bca/` (IO-01 remap source) | Copy file list + LICENSE prose |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| New Army CBA / generic decision pack | Remap A-94 / VV&A chapters (IO-01) | Invented pack forbidden; remap already specified |
| New `dodm-5000-102` | More `dod-vva-rpg` chapters | DoDM PDF never opened |
| Whole IS-GPS-200N dump | ICD exemplar (interface definition + how-an-ICD-is-structured) | 200N appendices are NAV bit/code tables; bloat + overlap risk |
| SP-7084 this phase | Skip | Training already 12/2; not an IO must |
| Phase 11 map JSON edit | Remap **spec** now; MAP-19-03 apply in Phase 12 | Prevents double-build / regen clobber |
| AAF / `dod-rio` as Integration/Logistics | Honest deferral | Phase 6 MA-01 class |

**Installation:** none. Sibling reference-skill must already be present (Phase 7 path).
</standard_stack>

<architecture_patterns>
## Architecture Patterns

### System Architecture Diagram

```text
  Phase 10 decision table (AUTHORITATIVE)
           |
           +-- GO 8719.14C ---- extract + 3rd-party scan --> packs/nasa-std-8719-14
           +-- GO IS-GPS-200N -- extract + DIST-A confirm --> packs/is-gps-200n  (SELECT, not dump)
           +-- GO SP-7084 ------ SKIP (YAGNI)
           +-- NO-GO Army CBA -- remap SPEC (federal-bca / dod-vva-rpg chapters) --> Phase 12 MAP-19-03
           +-- NO-GO DoDM ------ add leftover RPG chapters --> packs/dod-vva-rpg (extend)
           +-- NO-GO AAF ------- IO-05/06 deferred record
           +-- IO-07 ----------- accept (no pack)
           v
  per-pack gates: vet → extract → (outline) → scaffold/extend → generate
                  → validate_pack → scan → overlap → When-to-use/Prerequisites
           v
  Phase 12: map regen includes new packs + applies IO-01 remap list
  Phase 13: full registration + version/release (unless thin-register exception fired)
```

### Recommended Project Structure (Phase 11 outputs)

```
packs/nasa-std-8719-14/     # NEW (IO-03)
packs/is-gps-200n/          # NEW (IO-04 exemplar)
packs/dod-vva-rpg/          # EXTEND chapters (IO-02) — do not create dodm-5000-102
sources/<slug>/             # gitignored
.planning/phases/11-io-unlocking-packs-decision-analysis-remap/
  11-RESEARCH.md            # this file (URL + remap spec store)
  11-0N-PLAN.md             # planner writes
docs/SOURCE-VETTING.md      # do not re-vet; do not add URLs
docs/capability-pack-map.json   # DO NOT EDIT (Phase 12)
```

Do **not** create `packs/army-cba`, `packs/dodm-5000-102`, `packs/aaf-*`, `packs/nasa-sp-7084`, or a stakeholder pack.

### Pattern 1: Phase 7 / Phase 3 pack-build pipeline (copy this)

Exact command order from 7-RESEARCH §2 / 3-RESEARCH §2:

1. `mkdir -p sources/$SLUG` and download official PDF(s). URLs only from this file / 10-RESEARCH (never from packs).
2. **VET FIRST:** `python "$REF/tools/vet_source.py" --title … --publisher … --license …` — expect tier 1, exit 0. Third-party-quote advisory is expected, not a blocker.
3. **Build-time in-source confirm** on the copy actually extracted (P11-PRE-1 / P11-PRE-2). Halt if contrary notice.
4. **EXTRACT:** `python "$REF/scripts/extract.py" sources/$SLUG/*.pdf --mode technical --install-missing no`. Copy `book_skill_work` under `sources/$SLUG/`. Write `work_dir.txt` via `printf '%s'`.
5. **chars/page ≥ 300** from `metadata.json` pages vs `full_text.txt` length. Fail = wrong/scan PDF.
6. **OUTLINE:** `python "$REF/tools/outline.py" --source "$WRK/book_skill_work/full_text.txt" --out sources/$SLUG/outline.json`. Skip for RPG chapter-wise adds (derive from the chapter set).
7. **SCAFFOLD** (new packs only): `$REF/tools/build_pack.py --slug … --out-dir packs` **or** repo `tooling/build_pack.py --slug … --tier 1 --commercial-use true`. Repo wrapper errors if the folder exists — do not re-scaffold `dod-vva-rpg`.
8. **GENERATE** per PACK-SPEC: chapters `chNN-*.md` (Core Idea / Frameworks / Key Concepts / Mental Models / Anti-patterns / Key Takeaways / Connects To); `glossary.md` / `patterns.md` / `cheatsheet.md`; `SKILL.md` body order with `## When to use` immediately followed by `**Prerequisites:**`; fill PACK.yaml TODOs (`source_pages` from metadata.json, `chapters`, `built_on`, notes); complete LICENSE (statute / DIST-A prose, no URL).
9. **VALIDATE:** `python tooling/validate_pack.py packs/$SLUG`
10. **SCAN:** `python "$REF/tools/scan_generated_skill.py" packs/$SLUG` — disposition in notes.
11. **OVERLAP:** `python "$REF/tools/check_overlap.py" --source "$WRK/book_skill_work/full_text.txt" --pack packs/$SLUG` — exit 0.
12. **Commit** one scoped commit per pack; `git show --name-only` must have zero `sources/` or `full_text.txt`.

Chapter counts are guidance (6–8 typical), not a validate_pack gate. [VERIFIED: `docs/PACK-SPEC.md:16-26` layout; `tooling/validate_pack.py:12-16` checks]

### Pattern 2: How Phase 7 actually shipped a pack (file list + fields)

Shipped analog trees (`dod-vva-rpg`, `federal-bca`, `faa-std-025`, `nasa-ms-7009`) all contain:

```
packs/<slug>/{SKILL.md, PACK.yaml, LICENSE, chapters/chNN-*.md, glossary.md, patterns.md, cheatsheet.md}
```

`PACK.yaml` fields in those analogs: `slug`, `title`, `publisher`, `source_version`, `license`, `license_tier`, `commercial_use`, `share_alike`, `attribution_required`, `build.{method,source_pages,chapters,built_on}`, `notes`, `change_indication: "reconstructed as synthesized reference notes"`.

LICENSE pattern: identify title + publisher + edition textually; reproduce 17 U.S.C. § 105 (and DIST-A if applicable); courtesy attribution; "no source-material download link"; pack-content licence independent of repo MIT. [VERIFIED: `packs/federal-bca/LICENSE:1-21`; `packs/dod-vva-rpg/LICENSE:1-25`]

DIST-A visual confirm: Phase 7 required it for DoD copies. GPS 200N cover text layer already has the sentence (re-confirm on extract). RPG chapter covers often **lack** a printed DIST-A block — Phase 7 accepted DEBoK `Copyright Details = Public Domain` + OSD/OUSD authorship as DIST-equivalent and recorded it. IO-02 must use that same per-chapter gate, not invent a new one. [VERIFIED: `packs/dod-vva-rpg/PACK.yaml:37-41`]

### Pattern 3: Extend an existing pack (IO-02) — do not new-pack

`build_pack.py` refuses an existing slug. [VERIFIED: `tooling/build_pack.py:98-102`] IO-02 is additional chapters in `dod-vva-rpg`:

1. Fetch leftover chapter PDFs from the same cto.mil index → DEBoK OTMM guest rendition path Phase 7 used.
2. VET is already done for the guide; still run **per-chapter** P7-PRE-4 (authorship / PD / no DIST B–F).
3. Extract each new PDF; chars/page ≥ 300; store `work_dir_ch11.txt`… and `chapter_fulltexts/chNN.txt`.
4. Write `chapters/ch11-*.md`…; update SKILL.md Chapter Index, Topic Index, chapter count in the header; bump PACK.yaml `build.chapters` / `source_pages` (sum) / notes provenance (titles + retrieval date, **no URLs**).
5. validate + scan + overlap against **new** full_texts (and re-run overlap on old ones if synthesis touches shared SKILL.md only — SKILL.md overlap is usually fine).
6. Do **not** create `dodm-5000-102`. Do not ingest 5000.102 from a random mirror.

### Pattern 4: IO-01 remap is Phase 12 map work (decision — do not double-build)

REQUIREMENTS puts the *requirement* IO-01 in Phase 11 and the *mechanism* MAP-19-03 in Phase 12:

> "Remap existing `federal-bca` / selected `dod-vva-rpg` decision chapters into Decision Analysis (cluster 16) if they currently sit only in Opportunity/Benefit — cheaper than a new pack" [VERIFIED: `.planning/REQUIREMENTS.md:33`]

Live placement today (name-keyed):

- **Decision Analysis & Trade Studies** = only `nasa-ceh/ch06-nasa-ceh-decision-support-analyses.md` + `nasa-se-handbook/ch34-6-8-decision-analysis.md` (n=2). [VERIFIED: live map]
- **All six** `federal-bca` chapters + 3 support files sit in **Opportunity/Benefit Management**. `ch06` note already says "also decision analysis". [VERIFIED: live map]
- `dod-vva-rpg` decision-ish chapters sit elsewhere: `ch06` Accreditation → Assurance; `ch10` Risk → Risk; `ch08` Validation fundamentals → Validation. SKILL.md already routes "Decision analysis / evidence for decisions" to ch06, ch08, ch10. [VERIFIED: `packs/dod-vva-rpg/SKILL.md:76`]

**Phase 11 does:** write the remap table (below), optionally tighten Topic Index vocabulary, annotate IO-01 as "remap specified; map apply is MAP-19-03". **Phase 11 does not** edit `docs/capability-pack-map.json` / `.md`. Phase 12 MAP-19-01 regen would clobber a premature JSON edit unless the remap list travels with the regen — so the list, not the JSON, is the Phase 11 artifact.

**Phase 11 SC-1** ("Decision Analysis cluster count leaves 2") is therefore a **specified outcome for Phase 12 to apply**, not a live map assertion at Phase 11 verify. Planner must write SC-1 acceptance as "remap table sufficient to leave 2 when MAP-19-03 runs" so verify does not demand a map edit.

Recommended remap set (move, do not copy — every chapter has exactly one cluster):

| Pack | Chapter | From (today) | To | Why |
|---|---|---|---|---|
| `federal-bca` | `ch06-reporting-and-decision-use.md` | Opportunity/Benefit | Decision Analysis & Trade Studies | Decision-use / OMB-facing choice documentation; map note already flags "also decision analysis" |
| `federal-bca` | `ch04-uncertainty-and-sensitivity.md` | Opportunity/Benefit | Decision Analysis & Trade Studies | Uncertainty/sensitivity is the A-94 decision-analysis method spine |
| `dod-vva-rpg` | `ch06-accreditation-agent-role.md` | Assurance & System Assurance | Decision Analysis & Trade Studies | Accreditation is the authority **decision**; 7-RESEARCH targeted cluster 16 for this pack |

Leave `federal-bca` ch01–ch03, ch05 (+ support files) in Opportunity so cluster 15 does not collapse (today 10/2). Leave `dod-vva-rpg` ch08 in Validation (IO-02 is trying to fatten Validation, not rob it). Leave ch10 in Risk unless Phase 12 harvest prefers it; not required for "leaves 2".

Result after Phase 12 apply: Decision Analysis **2 → 5** entries, **2 → 4** packs. SC-1 met without a new pack.

### Pattern 5: Honest deferral / accept write-up (IO-05/06/07)

Copy the Phase 10 FUT-04 / AAF pattern. A valid close is a **dated record**, not a pack.

Template (put in Phase 11 SUMMARY + REQUIREMENTS parenthetical; do not tick the IO as built):

```markdown
- [ ] **IO-0X**: <stem> — *Phase 11 (YYYY-MM-DD): DEFERRED/ACCEPT.
  Source: <name>. Why: <reachability / not vetted / no Tier-1 candidate>.
  Not built. Not invented. Unblock when: <in-source grant / official PDF>.
  See 11-RESEARCH.md §IO-0X.*
```

IO-05 / IO-06: AAF Product Support + Software pathway still "NOT yet vetted — do not use". [VERIFIED: `docs/SOURCE-VETTING.md:176`]
IO-07: accept — see §IO-07. Optional Phase 12 note that existing SEBoK ch26–ch28 are *enabling* chapters currently in Standards/Tailoring, not a licence to invent a pack.

### Pattern 6: ICD exemplar (not a 200-page dump)

IS-GPS-200N is a real ICD/IS: cover DIST-A, body §§1–3 (interface definition / identification / criteria), §§4–5 "NOT APPLICABLE", §6 notes, then huge NAV-data appendices (App II starts p.78, App III p.141, App IV p.212). [VERIFIED: in-PDF TOC this session]

Pack teaches **how an ICD/IS is structured** using 200N as the worked example, complementary to `faa-std-025` (preparation rules, not a live ICD). Do not transcribe PRN/Gold-code tables or CNAV/LNAV bit fields.

### Anti-Patterns to Avoid

- Using AAF / WarU / DAG / `dod-rio` AAF chapters as licence clearance
- Inventing packs (CBA framework, stakeholder handbook, "generic ICD")
- Putting source URLs in packs or SOURCE-VETTING
- Treating Tier 1 *leaning* as skip-build-time-confirm
- Bloating IS-GPS-200N into an appendix dump
- Searching for IS-300; packaging ICD-GPS-153
- Editing the capability map in Phase 11 **and** again in Phase 12
- Building SP-7084 to "use the GO"
- Silent-ticking IO-05/06/07
</architecture_patterns>

<dont_hand_roll>
## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| New pack scaffolder | Custom mkdir/SKILL templates | `build_pack.py` (REF or repo) | Provenance + licence fields forced |
| Licence classifier | New rubric | `$REF/tools/vet_source.py` + SOURCE-VETTING | Exit 2 hard-stop already exists |
| Map editor / generator | Phase 11 JSON surgery | Remap table → Phase 12 MAP-19-01/03 | FUT-05 still deferred; regen is Phase 12 |
| Decision Analysis depth | Invented CBA / trade-study pack | IO-01 remap table | Army CBA NO-GO |
| Validation depth | `dodm-5000-102` from a mirror | Leftover RPG chapters | DoDM unreachable |
| Integration / Logistics | AAF HTML / 2022 footer | Honest deferral | Not vetted |
| Stakeholder depth | Invented facilitation pack | IO-07 accept | No clean Tier-1/2 candidate |
| Catalog page | Hand-edit `docs/packs.html` | `python tooling/gen_packs_page.py` | RR-B-30 freshness |
| Overlap checker | New committed tool | `$REF/tools/check_overlap.py` | 7-CODE-REVIEW IN-02 still out of scope |
</dont_hand_roll>

<common_pitfalls>
## Common Pitfalls

### Pitfall 1: Using AAF

**What goes wrong:** `packs/aaf-*` from DAU/WarU HTML or a 2022 copyright footer. Takedown / Phase 6 MA-01 regression.
**How to avoid:** IO-05/06 deferred-record only. `dod-rio` AAF pathway chapters describe AAF from a *different* vetted source; they do not licence AAF guidebooks. [VERIFIED: `docs/SOURCE-VETTING.md:176-177`]
**Warning signs:** plan tasks `mkdir packs/aaf-*`.

### Pitfall 2: Inventing packs

**What goes wrong:** Generic CBA, "stakeholder engagement handbook", or a synthetic ICD.
**How to avoid:** No source, no pack. IO-01 remap / IO-07 accept are the recorded outcomes.
**Warning signs:** PACK.yaml with no identifiable edition.

### Pitfall 3: Putting URLs in packs

**What goes wrong:** Link Policy + `check_release.py` SOURCE_HOSTS + CI `nasa.gov` grep. NASA PDF host **is** `standards.nasa.gov` (matches `nasa.gov`). [VERIFIED: `tooling/check_release.py:47`; `.github/workflows/validate.yml:43-45`]
**How to avoid:** Title + publisher + version only. URLs stay in 10-RESEARCH / this file.
**Warning signs:** `https://` in `packs/**` or `docs/SOURCE-VETTING.md`.

### Pitfall 4: Treating leaning Tier 1 as skip-build-time-confirm

**What goes wrong:** Extract a different mirror; miss a contractor insert (GPS names SAIC on the cover) or a third-party figure.
**How to avoid:** P11-PRE-1 (8719.14C third-party scan) and P11-PRE-2 (200N DIST-A on **this** copy) are hard gates before generation. [VERIFIED: `docs/SOURCE-VETTING.md:152-153`]

### Pitfall 5: Bloating IS-GPS-200N

**What goes wrong:** 200+ pages of PRN tables and CNAV/LNAV bit fields; overlap failures; agent context waste. Cluster 5 needs an **ICD exemplar**, not a signal-processing dump.
**How to avoid:** Select §§1–3 conceptual interface + §6 notes + a short "how appendices work" chapter. Skip App II–IV payloads. Skip 705J/800J unless the first pack is somehow empty (it will not be).

### Pitfall 6: Double-building IO-01 (Phase 11 map edit + Phase 12 MAP-19-03)

**What goes wrong:** Phase 11 edits JSON; Phase 12 regen overwrites or double-counts; verify fights over who owns SC-1.
**How to avoid:** Phase 11 = remap **table**. Phase 12 = apply during MAP-19-01 regen. Do not create a new pack "to be safe".

### Pitfall 7: Stealing Phase 13 — or shipping unregistered dirs that fail check_release

**What goes wrong:** (a) CHANGELOG / plugin version / GitHub Release done early; or (b) new `packs/` dirs on `main` without SKILLS/cursor rows → `check_release.py` `[index]` and `[cursor]` fail. [VERIFIED: `tooling/check_release.py:160-210`]
**How to avoid:** Version surfaces stay Phase 13. If new dirs commit to `main`, thin-register those slugs only (catalog + SKILLS + NOTICE + cursor + `gen_packs_page.py`). CI `validate.yml` does **not** check catalog counts — only frontmatter + link policy — so CI can stay green while check_release is red. Prefer thin-register over a red local gate.

### Pitfall 8: Silent ticks

**What goes wrong:** IO-05/06/07 checked because "we discussed it".
**How to avoid:** Dated DEFERRED/ACCEPT parentheticals; boxes stay open until verify accepts the record. Same Phase 10 VET-19 pattern.

### Pitfall 9: Phantom IS-300 / ICD-GPS-153

**What goes wrong:** Executor searches for a non-existent IS-300 (SEED-001 naming error) or packages the request-only ICD-GPS-153.
**How to avoid:** Public set is IS-GPS-200N (+ optional 705J/800J) and ICD-GPS-240D / 870E. Select = **200N only**. [VERIFIED: `docs/SOURCE-VETTING.md:173`]

### Pitfall 10: Re-scaffolding `dod-vva-rpg` or dual-sourcing federal-bca

**What goes wrong:** `build_pack.py` errors; or Army CBA fetch is retried and a half-pack is generated.
**How to avoid:** Extend in place. federal-bca stays A-94-only. [VERIFIED: `packs/federal-bca/PACK.yaml:21-24`]
</common_pitfalls>

<code_examples>
## Code Examples

### Pipeline (new pack) — IO-03 / IO-04

```bash
REF="C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill"
SLUG=nasa-std-8719-14          # or is-gps-200n
mkdir -p sources/$SLUG
# download official PDF into sources/$SLUG/  (URL from §Sources below)

python "$REF/tools/vet_source.py" \
  --title "Process for Limiting Orbital Debris" \
  --publisher "NASA" \
  --license "Public Domain (US Government work, 17 U.S.C. § 105)"
# Expect tier 1, exit 0

python "$REF/scripts/extract.py" sources/$SLUG/*.pdf --mode technical --install-missing no
# copy book_skill_work under sources/$SLUG/; printf '%s' "$TMP" > sources/$SLUG/work_dir.txt
WRK=$(tr -d '\r\n' < sources/$SLUG/work_dir.txt)

# P11-PRE-1: grep extracted text for Copyright / All rights / third-party inserts
# P11-PRE-2 (GPS): grep DIST-A sentence on THIS copy
# chars/page >= 300 from metadata.json

python "$REF/tools/outline.py" --source "$WRK/book_skill_work/full_text.txt" --out sources/$SLUG/outline.json

python "$REF/tools/build_pack.py" \
  --slug $SLUG --title "…" --publisher "…" --version "…" \
  --license "…" --out-dir packs
# or: python tooling/build_pack.py --slug $SLUG --title "…" --publisher "…" \
#        --version "…" --license "…" --tier 1 --commercial-use true

# GENERATE chapters + SKILL.md + LICENSE + PACK.yaml TODOs  (agent; PACK-SPEC)

python tooling/validate_pack.py packs/$SLUG
python "$REF/tools/scan_generated_skill.py" packs/$SLUG
python "$REF/tools/check_overlap.py" --source "$WRK/book_skill_work/full_text.txt" --pack packs/$SLUG
```

### SKILL.md contract (RR-S-13 / SC-5)

```markdown
## When to use
Reach for this pack when …

**Prerequisites:** none — plain Markdown; no MCP server, API key, or licence tier needed at runtime.
```

Enforced by `check_release.py` on every non-signpost pack. [VERIFIED: `tooling/check_release.py:131-141`; `docs/PACK-SPEC.md:33-34`]

### IO-02 extend (do not scaffold)

```bash
# AFTER per-chapter fetch + P7-PRE-4 + extract into sources/dod-vva-rpg/chapter_fulltexts/ch11.txt …
python tooling/validate_pack.py packs/dod-vva-rpg
python "$REF/tools/scan_generated_skill.py" packs/dod-vva-rpg
python "$REF/tools/check_overlap.py" \
  --source sources/dod-vva-rpg/chapter_fulltexts/ch11.txt \
  --pack packs/dod-vva-rpg
# repeat per new chapter; update PACK.yaml source_pages = previous 283 + new metadata sums
```

### Thin-register exception (only if new dirs hit main)

Mirror 7-03 Task 2 **for the new slugs only**; do not bump CHANGELOG / plugin version / RELEASE-INFO:

- `catalog.json`: add objects (copy key shape from `nasa-ms-7009` / `faa-std-025`: slug, title, publisher, source_version, license, license_tier, commercial_use, chapters, status `live`); bump `updated`.
- `SKILLS.md`: add rows; header `63 packs (+2 signposts)` if both new packs ship (61+2).
- `NOTICE`: `[pack: nasa-std-8719-14]` and `[pack: is-gps-200n]` Public Domain blocks.
- `.cursor-plugin/plugin.json`: +2 skill paths (both Tier 1 / commercial).
- `python tooling/gen_packs_page.py`
- README badge is release-surface-ish; include it if check_release starts caring (today it does not parse the badge). Safer to bump badge with SKILLS to avoid human drift.
- `python tooling/check_release.py` PASS
- Do **not** tag v1.19.0 (REL-19-02).

Live basis now: 63 pack dirs, catalog 61, SKILLS "61 packs (+2 signposts)", cursor 62 (sebok excluded). [VERIFIED: `ls packs` = 63; catalog packs = 61; 7-03-SUMMARY counts]
</code_examples>

<sota_updates>
## State of the Art (this session, 2026-08-17)

| Assumption | Current observation | Impact |
|------------|---------------------|--------|
| Decision Analysis fattens via a new Army CBA pack | Army CBA still 403/503; federal-bca is A-94-only; all A-94 chapters mapped to Opportunity | IO-01 = remap spec, not a pack |
| DoDM 5000.102 is the Validation unlock | Never ingested; RPG already has 10 chapters; T&E/V&V Checklist was a **selection** drop | IO-02 = add leftover RPG chapters |
| "GPS ICD-IS-200/300" | Public IS-GPS-200N + 705J + 800J; no IS-300; 200N body is §§1–3 + giant NAV appendices | Exemplar, not dump |
| NASA-STD-8719.14 might be a GP-08 placeholder | Official PDF 905,584 bytes, 77 pp, real TOC §§1–4 + App A/B | GO build |
| Phase 11 must move the map | MAP-19-01/03 are Phase 12; check_capability_map not in check_release | Remap table only |
| SP-7084 is an IO must | Tier 1 reconfirmed; Training already 12/2; not in Phase 11 SC | Skip |

**Deprecated/outdated:**

- Dual-source `federal-bca` as if Army CBA were inside.
- "IS-300" as a public GPS ICD name.
- Treating `aaf.dau.edu/guidebooks/` as a PDF library.
- Assuming Phase 7 already mapped VV&A into Decision Analysis (it targeted cluster 16; live map did not place any `dod-vva-rpg` row there).
</sota_updates>

<candidate_findings>
## IO-by-IO findings (planner-consumable)

### Decision table (do not re-vet)

| ID | Action | Slug / artifact | Phase 11 produce? | Confidence |
|----|--------|-----------------|-------------------|------------|
| IO-01 | Remap spec (no pack) | Table in this file → Phase 12 MAP-19-03 | **Yes — spec only** | HIGH |
| IO-02 | Extend existing pack | `dod-vva-rpg` +2–4 chapters | **Yes** | HIGH (checklist named); MEDIUM (other special-topic titles) |
| IO-03 | New pack | `nasa-std-8719-14` | **Yes** | HIGH |
| IO-04 | New exemplar pack | `is-gps-200n` | **Yes** (200N only) | HIGH |
| IO-05 | Defer | no pack | **Record only** | HIGH |
| IO-06 | Defer | no pack | **Record only** | HIGH |
| IO-07 | Accept | no pack | **Record only** | HIGH |
| SP-7084 | Skip | — | **No** | HIGH |

---

### IO-01 — Decision Analysis remap (no new pack)

**Why not a pack:** Army CBA Guide remains FUT-04 deferred (403/503, no in-source). Inventing a CBA pack is forbidden. [VERIFIED: `.planning/REQUIREMENTS.md:21`]

**Why remap is not a Phase 11 map edit:** MAP-19-03 is a Phase 12 requirement. MAP-19-01 regenerates the whole JSON. Editing now double-builds and will be overwritten unless the chapter list is the handoff. Phase 11 SC-1 is satisfied by a **sufficient remap table**, applied in Phase 12.

**Recommended chapter list:** see Pattern 4. Cheapest path that leaves 2: move `federal-bca` ch04 + ch06 and `dod-vva-rpg` ch06. Do not move the whole A-94 pack (Opportunity would regress). Do not move `dod-vva-rpg` ch08 (Validation needs it).

**Optional Phase 11 pack-side nudge (not a map edit):** federal-bca Topic Index already has "Net present value" / "Sensitivity"; add an explicit **Decision Analysis** row pointing at ch04/ch06 if missing. dod-vva-rpg already has that row.

**Do not:** create `packs/federal-cba`, re-open Army fetch as a build task, or retitle federal-bca.

---

### IO-02 — Additional `dod-vva-rpg` chapters (not `dodm-5000-102`)

**Shipped set (10):** Key Concepts; User / Developer / M&S PM / V&V Agent / Accreditation Agent (new-development); Fidelity; Validation Fundamentals; Data V&V; Risk. `source_pages = 283`. [VERIFIED: `packs/dod-vva-rpg/PACK.yaml:25-36`]

**Already dropped (selection, DEBoK PD confirmed):** T&E/V&V Checklist (`TEVVchecklist-pr.PDF`). [VERIFIED: `.planning/phases/7-gap-driven-pack-builds/7-03-SUMMARY.md:108`]

**Still on the index (6-RESEARCH):** Legacy role guides; ~17 Special Topics; Reference Documents; Use Case Overview (`vva-rpg-uco`). [VERIFIED: `.planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md:55-61`]

**Build set (keep lean — Validation primary, not a second RPG pack):**

1. **Must try:** T&E/V&V Checklist — already licence-passed; dropped only to stay in the 8–10 band.
2. **Should try:** Use Case Overview if it is a fetchable document that frames intended-use / validation decisions.
3. **At most 1–2 more** validation-adjacent special topics discovered on the live index (referent, face validation, independent review, or similar). **Do not** pre-invent titles. **Do not** add all 17 special topics. **Do not** add legacy role guides (duplicate of new-dev roles).

Per-chapter P7-PRE-4 + chars/page ≥ 300 + provenance line in PACK.yaml notes (title + retrieved date, no URL). Fetch path: cto.mil index → DEBoK OTMM guest rendition (Phase 7 deviation #2). Index URL (research store only): `https://www.cto.mil/sea/vva_rpg/` ; UCO `https://www.cto.mil/sea/vva-rpg-uco/`.

Target-cluster vocabulary in new chapter Topic Index rows: **Validation** (primary), Verification, Test & Evaluation. Do not retarget ch08 away from Validation.

ROADMAP SC-2: "Validation … gained at least one new pack **or** documented deferral". Additional chapters in an **existing** pack are not a new pack. That still moves Validation **depth** (new map entries in Phase 12). If the planner wants a literal "new pack" reading, the honest alternative is to **document** that Validation gained chapters-not-a-pack (DoDM deferred) — not to invent `dodm-5000-102`. Prefer the chapter-add; record the SC-2 reading in the plan so verify does not demand a new slug.

---

### IO-03 — `nasa-std-8719-14` (NASA-STD-8719.14C)

**Identity:** Process for Limiting Orbital Debris; Version C; Approved 2021-11-05; ACTIVE; supersedes 8719.14B; **77 pp**; official PDF 905,584 bytes (`%PDF-1.7`). [VERIFIED: in-PDF title page + "5 of 77" this session; 10-RESEARCH.md:390-399]

**URLs (research store only):**

- NTSS record: `https://standards.nasa.gov/standard/nasa/nasa-std-871914`
- PDF: `https://standards.nasa.gov/sites/default/files/standards/NASA/C/0/nasa-std-871914c.pdf`

**Licence (re-confirm at extract):** NASA US-gov work; NTSS "Internet Public -- Standard is cleared for public accessibility on the internet." Phase 10 text-layer: 0 hits for Copyright / All rights. Contrast: this is a real standard, not a GP-08 placeholder. [VERIFIED: `docs/SOURCE-VETTING.md:152`; 10-RESEARCH.md:387-405]

**P11-PRE-1:** scan extracted copy for third-party inserts (IADC / UN / SPD-3 are cited as *consistency*, not licensed inserts — do not package NASA-HDBK-8719.14). Quote Internet Public + title-page lines in PACK.yaml notes.

**TOC (this session, pages 7–8 of 77):**

1. SCOPE (1.1 Purpose, 1.2 Applicability)
2. APPLICABLE AND REFERENCE DOCUMENTS
3. ACRONYMS AND DEFINITIONS
4. REQUIREMENTS
    - 4.1 Objectives of Orbital Debris Assessments and Planning
    - 4.2 Conducting Debris Assessments: An Overview
    - 4.3 Assessment of Debris Released During Normal Operations
    - 4.4 Assessment of Debris Generated by Explosions and Intentional Breakups
    - 4.5 Assessment of Debris Generated by On-orbit Collisions
    - 4.6 Postmission Disposal of Space Structures
    - 4.7 Assessment of Debris Surviving Atmospheric Reentry
    - 4.8 Additional Assessment Requirements for Special Classes of Space Missions
- Appendix A — Orbital Debris Assessment Reports (ODAR)
- Appendix B — EOMPs

**Chapter strategy (6–7 chapters; analog `nasa-ms-7009`):**

| Pack ch | Source slice | Cluster vocab |
|---|---|---|
| ch01 | §1 + NPR 8715.6 frame / applicability | Ops/Maint/Disposal; Standards |
| ch02 | §4.1–4.2 assessment overview + technical areas | Ops/Maint/Disposal |
| ch03 | §4.3 debris released during normal operations | Ops/Maint/Disposal |
| ch04 | §4.4–4.5 explosions/breakups + collisions | Safety (secondary); Ops |
| ch05 | §4.6 postmission disposal | **Ops/Maint/Disposal (primary gold)** |
| ch06 | §4.7 reentry surviving debris | Ops/Maint/Disposal |
| ch07 | §4.8 + App A/B ODAR / EOMP | Ops/Maint/Disposal; Governance |

Skip dumping every figure/table. Do not ingest NASA-HDBK-8719.14. `source_pages` from metadata.json (expect ~77).

**Slug:** `nasa-std-8719-14` (handoff-locked). [VERIFIED: `docs/SOURCE-VETTING.md:172`]
**Publisher:** NASA (Office of Safety and Mission Assurance).
**source_version:** `NASA-STD-8719.14C (Approved 2021-11-05)`.
**Licence string:** default statute.

Analog file list: copy `packs/nasa-ms-7009/`.

---

### IO-04 — `is-gps-200n` ICD exemplar (not whole 200N)

**Identity:** NAVSTAR GPS Space Segment / Navigation User Segment Interfaces; IS-GPS-200 Rev N; SSC / MilComm & PNT; PDF 3,338,120 bytes (`%PDF-1.6`). Cover DIST-A: "DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited." SAIC named Interface Control Contractor (watch-item, not an all-rights-reserved notice). [VERIFIED: in-PDF cover this session; 10-RESEARCH.md:421-441]

**URLs (research store only):**

- Index: `https://www.gps.gov/interface-control-documents-icds-interface-specifications-iss`
- PDF: `https://www.gps.gov/sites/default/files/2025-07/IS-GPS-200N.pdf`

**Do not search for IS-300. Skip ICD-GPS-153.** Optional 705J/800J: **do not build** unless 200N exemplar somehow fails to produce ≥5–6 chapters (it will not).

**P11-PRE-2:** DIST-A sentence must appear in the extracted copy. Record SAIC contractor line in notes as watch-item. Licence string = DIST-A variant.

**Structure (TOC this session):**

- §1 Introduction (scope; IS approval and changes)
- §2 Applicable documents
- §3 Requirements — **the ICD meat**
  - 3.1 Interface Definition
  - 3.2 Interface Identification (ranging codes, NAV data, L1/L2 signal structure)
  - 3.3 Interface Criteria (composite signal, PRN characteristics, NAV modulation, GPS time / Z-count)
- §4 / §5 NOT APPLICABLE
- §6 Notes (acronyms, definitions, SV blocks)
- App I Letters of exception (p.69)
- App II LNAV data PRN 1–32 (p.78)
- App III CNAV data (p.141)
- App IV LNAV data PRN 33–63 (p.212)

**Chapter strategy (5–6 chapters — exemplar, complementary to `faa-std-025`):**

| Pack ch | Source slice | What to synthesize | What to skip |
|---|---|---|---|
| ch01 | §1 + cover/change control | What an IS/ICD is; DIST-A; revision/IRN discipline | Contractor street address as content |
| ch02 | §3.1–3.2 | Interface definition vs identification; document-as-contract | Chip-by-chip P/Y/C/A/CM/CL tables |
| ch03 | §3.3.1 | Interface criteria pattern (freq plan, levels, phasing, polarization) as ICD shalls | Numeric RF dumps beyond illustrating the pattern |
| ch04 | §3.2.2 + §3.3.3 | NAV data as interface payload (message families, not bits) | FEC polynomials, bit fields |
| ch05 | §3.3.4 + §6 | Time/Z-count + definition hygiene (URA, CEI, reserved/invalid) | SV block history trivia |
| ch06 | Apps I–IV *as a map* | How ICD annexes carry the normative payload; when to open which appendix | **Do not transcribe Apps II–IV** |

`faa-std-025` already covers IRD/ICD *preparation* (6 chapters). This pack is a **worked ICD**. SKILL.md Scope & Limits **must** cross-reference `faa-std-025` (same slug-distinction pattern as dote vs dod-te-guidebook).

**Slug recommendation:** `is-gps-200n` (document ID; not locked in handoff — planner may pick `gps-is-200n`; do not use `gps-icd-is-200-300`).
**Publisher:** US Space Force / Space Systems Command (MilComm & PNT).
**source_version:** `IS-GPS-200 Rev N (cover date 01-AUG-2022; public-release revision record)`.
**Target cluster:** Interface Management & ICIDs (primary). Secondary: Requirements Traceability, CM (change/IRN).

---

### IO-05 / IO-06 — Honest deferral (no AAF pack)

AAF Product Support + Software pathway remain **NOT yet vetted — do not use** (Excluded-pending). Cloudflare 403 / WarU 404 / 2022 site `Copyright ©` footer is not a grant. [VERIFIED: `docs/SOURCE-VETTING.md:160-162, 176`]

Integration (4/4) and Logistics (12/2) do **not** get a pack this phase. ROADMAP SC-3: "Integration + Logistics built only if AAF cleared; otherwise deferred-recorded."

Write the Pattern 5 template into REQUIREMENTS IO-05/IO-06 parentheticals + STATE + 11-SUMMARY. Unblock condition: official guidebook PDF opened + in-source redistribution grant quoted in a future vetting phase.

---

### IO-07 — Accept (no invented pack)

Live Stakeholder Engagement & Needs = 3 entries / 3 packs: `nasa-se-handbook` ch17, `nist-ai-rmf` ch02, `sebok` ch16. [VERIFIED: live map]

SEED-001: "No clean Tier-1 source (gap report: SEBoK expansion only)". Phase 10 cleared no new stakeholder source. [VERIFIED: `.planning/seeds/SEED-001-agent-io-pack-depth.md:43-45`; `.planning/REQUIREMENTS.md:27`]

**Recorded outcome: ACCEPT.** Do not invent a facilitation/negotiation pack. "SEBoK expansion" would mean Phase 12 rematching existing `sebok` ch26–ch28 (enabling businesses/teams/individuals — currently Standards/Tailoring). That is optional map judgement, not a Phase 11 pack, and is likely the **wrong cluster** (enabling vs stakeholder-needs). Do not treat rematch as a substitute for accept.

---

### SP-7084 — skip (YAGNI)

Tier 1 RECONFIRMED (NTRS "Work of the US Gov. Public Use Permitted"). Optional Training-diversity only. Training is already 12 entries / 2 packs (`faa-std-025`, `mil-std-40051`). Not in Phase 11 success criteria 1–4. [VERIFIED: `docs/SOURCE-VETTING.md:174`; live map cluster Training]

If a later milestone wants it: prefer 1998 rev if text layer else NTRS 1990 canonical; record edition in PACK.yaml. URLs in 10-RESEARCH §5.

---

### Catalog / registration — Phase 13 unless dirs cannot exist on main

REL-19-01: "Full registration of any new packs; both gates PASS" is Phase 13. [VERIFIED: `.planning/REQUIREMENTS.md:46`; `.planning/ROADMAP.md:75-84`]

A pack **folder** can exist without a catalog row (Phase 7 Waves A/B did this). A pack **on `main` as a passing tree** cannot: `check_release.py` requires SKILLS.md entry count == non-signpost pack dirs and cursor manifest == commercial packs. [VERIFIED: `tooling/check_release.py:160-210`]

CI `validate.yml` does **not** enforce those counts (frontmatter + link policy + catalog JSON parse only). [VERIFIED: `.github/workflows/validate.yml:66-88`]

**Decision for planner:**

- Default (keep Phase 13 whole): build packs; if that would leave check_release red on `main`, take the **thin-register exception** for the two new slugs only (Pattern / code example above). That is "cannot exist without catalog rows" in the mechanical-gate sense.
- Do **not** steal REL-19-02 (tag / GitHub Release) or CHANGELOG IO-unlock narrative / version bump.
- Do **not** regenerate the capability map (Phase 12). Stale map vs new chapters is expected; `check_capability_map.py` is not in check_release yet.
- IO-02 chapter-count drift in `catalog.json` (`chapters: 10`) is **not** checked by validate_pack or check_release. Leave the catalog chapter integer for Phase 13 unless thin-register is already touching that object.

Expected post-thin-register basis if both new packs ship: dirs 65 / catalog 63 / SKILLS 63 (+2 signposts) / cursor 64 (sebok still out). Record in SUMMARY for Phase 13.
</candidate_findings>

<validation_architecture>
## Validation Architecture (Nyquist — how a planner knows Phase 11 is done)

No runtime. "Done" is **GO packs gated** + **NO-GO recorded**. Success is not "every IO produced a slug".

### Signals that must be true after execute

| Signal | How to measure | Pass |
|--------|----------------|------|
| IO-03 built | `python tooling/validate_pack.py packs/nasa-std-8719-14`; When-to-use + Prerequisites; no TODO in PACK.yaml; chars/page ≥ 300; overlap 0; P11-PRE-1 quote in notes | new pack exists and gated |
| IO-04 built | same gates on `packs/is-gps-200n`; DIST-A quote in notes; SKILL.md mentions `faa-std-025`; no App II–IV transcription | exemplar, not dump |
| IO-02 extended | `dod-vva-rpg` chapter count > 10; new chNN files linked from SKILL.md; per-new-chapter overlap 0; P7-PRE-4 notes; **no** `packs/dodm-5000-102` | Validation depth moved or deferral if fetch failed |
| IO-01 remap specified | Table present (this file or SUMMARY) naming ≥1 federal-bca and/or dod-vva-rpg chapter to move into Decision Analysis; **no** new CBA pack; **no** map JSON edit | Phase 12 can apply without guessing |
| IO-05/06 deferred | REQUIREMENTS parenthetical dated; no `packs/aaf-*` | honest |
| IO-07 accept | REQUIREMENTS parenthetical dated; no invented stakeholder pack | honest |
| SP-7084 | no `packs/nasa-sp-7084` (unless planner explicitly overrides YAGNI — then edition recorded) | skip |
| Link Policy | no `https://` in new/changed pack files; `grep -c http docs/SOURCE-VETTING.md` still `0` | true |
| Leak | no `sources/` or `full_text.txt` in commits | `git show --name-only` clean |
| SC-5 | each **built** pack: PACK-SPEC + validate + scan + overlap + When-to-use/Prerequisites | true |
| Map untouched | `git diff --name-only -- docs/capability-pack-map.json` empty | Phase 12 owns it |

### What is *not* a completion signal

- Decision Analysis live count already > 2 (that is Phase 12 after MAP-19-03).
- IO-05/06/07 checkboxes ticked as "built".
- `vet_source.py` exit 0 without opening the PDF.
- `check_capability_map.py` PASS on a hand-edited map.
- v1.19.0 tag.

### Residual risk after a correct Phase 11

Phase 12 must apply the remap table or SC-1 stays failed at the milestone level. Phase 13 must finish registration/version if thin-register was skipped or partial. GPS SAIC line remains a watch-item, not a licence defect, if DIST-A is on the extracted copy.
</validation_architecture>

<open_questions>
## Open Questions

1. **Thin-register in Phase 11 or leave check_release red until Phase 13?**
   - What we know: new dirs break SKILLS/cursor counts; CI does not care; REL-19-01 is Phase 13.
   - Recommendation: thin-register the two new slugs if they commit to `main`. Do not touch version surfaces.

2. **Literal ROADMAP SC-2 "new pack" vs chapter-add for Validation?**
   - What we know: IO-02 is specified as additional VV&A chapters. SC-2 says "new pack *or* documented deferral".
   - Recommendation: treat chapter-add as the IO-02 path; document that Validation's "new pack" was DoDM (deferred) and depth comes from chapters. Do not invent a slug to satisfy the noun "pack".

3. **Which extra RPG special topics besides the Checklist?**
   - What we know: ~17 exist; only Checklist is named in-repo as dropped.
   - Recommendation: fetch index at execute; add Checklist + at most 2 validation-adjacent docs. Do not block the phase on UCO if it is HTML-only.

4. **Human browser for leftover RPG PDFs?**
   - What we know: Phase 7 needed DEBoK OTMM guest session.
   - Recommendation: reuse that path; if Checklist cannot be fetched, record IO-02 partial deferral rather than substituting DoDM.
</open_questions>

<recommended_plan_shape>
## Recommended plan shape (do NOT write PLAN.md here)

Two execute plans. Wave-homogeneous. One scoped commit per new pack; one commit for the `dod-vva-rpg` extend; one commit for deferral/accept annotations (+ thin-register if taken).

**Plan 11-01 — Wave A: GO new packs (IO-03, IO-04)**

1. Build `nasa-std-8719-14` via Pattern 1 + IO-03 chapter table. P11-PRE-1 third-party scan. Analog: `nasa-ms-7009`.
2. Build `is-gps-200n` via Pattern 1 + IO-04 exemplar table. P11-PRE-2 DIST-A. Cross-link `faa-std-025`. Do not add 705J/800J. Do not ingest Apps II–IV.

Out of this plan: map JSON, catalog (unless planner folds thin-register into 11-02), SP-7084, AAF.

**Plan 11-02 — Wave B: extend + records (IO-02, IO-01 spec, IO-05/06/07)**

1. Extend `dod-vva-rpg` (Pattern 3): Checklist + ≤2 live-index validation topics. No `dodm-5000-102`.
2. Write/confirm IO-01 remap table into SUMMARY (Pattern 4). Optional Topic Index nudge. **No** `capability-pack-map.json` edit.
3. Honest deferral/accept annotations on IO-05, IO-06, IO-07 (Pattern 5). Do not tick as built.
4. Optional thin-register of `nasa-std-8719-14` + `is-gps-200n` (not version bump).

**Must-NOT across both plans:** Army CBA pack; AAF pack; stakeholder pack; SP-7084; IS-300; ICD-GPS-153; source URLs in packs; map regen; REL-19-02 tag.

Analog plan structure only: `.planning/phases/7-gap-driven-pack-builds/7-01-PLAN.md` (per-pack pipeline tasks + work_dir verify + When-to-use grep + no-TODO + scoped commit).
</recommended_plan_shape>

<project_constraints>
## Project Constraints (no CLAUDE.md / AGENTS.md in repo)

From `PROJECT.md` / PACK-SPEC / SOURCE-VETTING:

- Pack content licences are inherited from sources; **vetting is a hard stop, not advisory**. [VERIFIED: `.planning/PROJECT.md:29`]
- Packs stay plain Markdown, progressive-disclosure (SKILL.md < ~4,000 tokens).
- "Free to download" is not "free to redistribute." [VERIFIED: `docs/SOURCE-VETTING.md:15`]
- Transform, do not transcribe. [VERIFIED: `docs/LICENSING.md:60-67`]
- Design constraint: **no per-role packs**. [VERIFIED: `.planning/seeds/SEED-001-agent-io-pack-depth.md:78`]
</project_constraints>

<sources>
## Sources

### Primary (HIGH confidence)

- `.planning/REQUIREMENTS.md` IO-01..07 + Phase 10 handoff notes; MAP-19 / REL-19 phase split
- `.planning/ROADMAP.md` Phase 11–13 success criteria
- `.planning/STATE.md` current_phase 11; GO/NO-GO deviation
- `.planning/seeds/SEED-001-agent-io-pack-depth.md`
- `docs/SOURCE-VETTING.md` v1.19 rows + Phase 11 handoff
- `.planning/phases/10-source-vetting/10-RESEARCH.md` (URLs, quotes, decision table)
- `.planning/phases/10-source-vetting/10-GAP_ANALYSIS.md` §Phase 11 Routing
- `.planning/phases/7-gap-driven-pack-builds/7-RESEARCH.md`, `7-01-PLAN.md`, `7-03-PLAN.md`, `7-03-SUMMARY.md`
- `.planning/phases/3-tier-1-packs-public-domain/3-RESEARCH.md` §2 pipeline
- `docs/PACK-SPEC.md`, `docs/LICENSING.md` §4, `docs/capability-map-CONTRACT.md`
- `tooling/build_pack.py`, `tooling/validate_pack.py`, `tooling/check_release.py`, `tooling/check_capability_map.py`
- Analog packs: `packs/dod-vva-rpg/`, `packs/federal-bca/`, `packs/faa-std-025/`, `packs/nasa-ms-7009/`
- Live `docs/capability-pack-map.json` (schema 2, map_version 1.18.0, 628 entries)
- Official PDFs opened this session (gitignored `sources/_phase11-research/`): NASA-STD-8719.14C TOC; IS-GPS-200N cover + TOC

### Secondary (MEDIUM confidence)

- `.planning/research/capability-gap-report.md` — original candidate shortlist (several hosts now 403)
- `.planning/phases/6-source-vetting-unverified-resolution/6-RESEARCH.md` §1c leftover RPG inventory
- 17 U.S.C. § 105 [CITED: https://www.copyright.gov/title17/92chap1.html#105]

### Tertiary (LOW confidence — execute must resolve)

- Exact leftover VV&A special-topic filenames beyond `TEVVchecklist-pr.PDF`
- Whether UCO is a PDF or HTML-only
- Whether a rendered browser session would still clear Army CBA / DoDM (out of scope to retry as a build)
</sources>

<metadata>
## Metadata

**Research scope:**
- Core technology: pack pipeline / PACK-SPEC / DIST-A / 17 U.S.C. § 105
- Ecosystem: NASA NTSS 8719.14C, GPS.gov IS-200N, DoD VV&A RPG chapter-wise, capability map v2
- Patterns: Phase 7 build; Phase 7-03 registration; honest deferral; remap-spec vs map-edit
- Pitfalls: AAF; invented packs; URL leak; leaning-as-cleared; 200N dump; double-build MAP-19-03

**Confidence breakdown:**
- Standard stack / pipeline: HIGH — read 3-RESEARCH, 7-RESEARCH, 7-01-PLAN, tooling
- GO/NO-GO: HIGH — Phase 10 AUTHORITATIVE
- NASA / GPS outlines: HIGH — official PDFs this session
- Remap-vs-Phase-12: HIGH — REQUIREMENTS vs ROADMAP ownership
- Leftover RPG titles: MEDIUM — Checklist named; others live-index
- Catalog exception: HIGH on the check_release mechanism; MEDIUM on whether planner prefers red-gate vs thin-register

**Research date:** 2026-08-17
**Valid until:** 2026-09-16 (GPS/NASA editions move slowly; DEBoK/AAF/WHS hosts move faster)
</metadata>

---

*Phase: 11-io-unlocking-packs-decision-analysis-remap*
*Research completed: 2026-08-17*
*Ready for planning: yes*

---
phase: 3-tier-1-packs-public-domain
reviewed: 2026-08-15T02:30:00Z
depth: deep
files_reviewed: 9
files_reviewed_list:
  - packs/nist-800-171/** (PACK.yaml, SKILL.md, LICENSE, chapters/, glossary/patterns/cheatsheet)
  - packs/nist-800-61/**
  - packs/cisa-cpg/**
  - packs/doe-sem/**
  - packs/mil-hdbk-338/**
  - packs/mil-hdbk-516/**
  - packs/nasa-ms-7009/**
  - packs/doe-413-3b/**
  - registration commit 863bfeb (catalog.json, SKILLS.md, docs/packs.html, docs/index.html, README.md, NOTICE)
findings:
  critical: 0
  blocker: 0
  major: 1
  minor: 3
  info: 3
  total: 7
status: issues_found
verdict: PASS_WITH_NOTES
---

# Phase 3: Code Review Report (post-execute)

**Verdict:** PASS_WITH_NOTES

**Reviewed:** 2026-08-15
**Depth:** deep (packs cross-checked against local source extractions under `sources/`, live tooling, and all registration surfaces)
**Scope:** 8 new Tier-1 packs (nist-800-171, nist-800-61, cisa-cpg, doe-sem, mil-hdbk-338, mil-hdbk-516, nasa-ms-7009, doe-413-3b) + registration commit `863bfeb`
**Status:** issues_found (1 MAJOR, 3 MINOR, 3 INFO; 0 BLOCKER)

## Summary

The eight packs and the registration sweep are substantively correct, and — unusually —
almost every load-bearing claim in the three SUMMARYs survived independent re-verification
rather than just re-reading:

- **Mechanical gates:** `validate_pack.py` 8/8 PASS; `check_release.py` PASS.
- **Catalog consistency:** catalog.json = 54 packs / 50 tier-1; every new entry's
  `chapters` count equals the actual `chapters/ch*.md` file count (8/6/5/7/9/8/7/6); no
  stale `planned` entries; slug sets match the 56 pack dirs minus 2 signposts; SKILLS.md
  header "54 packs (+2 signposts)" and 8 new backtick-slug rows present (56 rows − 2
  signposts = 54 = shipped packs, matching gate §6); docs/packs.html matches a fresh
  generation (gate §5c).
- **rr-s-13:** all 8 SKILL.md files satisfy the exact gate regex (`^##\s*When to use\s*$`
  + Prerequisites marker); body order otherwise follows PACK-SPEC with `When to use`
  prepended; every description states scope limits; every chapter is linked from the
  Chapter Index with zero dead links and zero unlinked chapters.
- **Link policy (independently, beyond the gate):** manual grep of all 8 packs and all
  registration surfaces for URLs — including hosts the gate's `SOURCE_HOSTS` regex does
  NOT cover (energy.gov, cisa.gov, nde-ed.org, everyspec.com, standards.nasa.gov,
  nvlpubs) — found zero source-material links. Zero `sources/` / `full_text` / PDF
  leakage across all 9 commits (MN-01 re-verified per commit).
- **Licence safety (re-derived, not trusted):** an independent 12-word-shingle overlap
  check of every `.md` in all 8 packs against the actual extracted source texts
  (including both cisa-cpg sources and both nasa-ms-7009 sources) returned **zero**
  verbatim runs ≥12 words. The `check_overlap exit 0` claims are true.
- **Provenance (re-derived):** all 8 `PACK.yaml` `source_pages` values equal
  `metadata.json` exactly (120, 48, 36+2=38, 318, 1046, 527, 88+175=263, 132).
  Distribution Statement A strings confirmed in-copy in both DoD extracts, including the
  exact punctuation variants the summaries quote. CPG goal IDs (1.A–1.E, 2.x),
  800-61 Tables 2/3, and CD-0–CD-4 all confirmed present in the source texts — chapter
  content is grounded, not invented.
- **Folded MAJORs:** MJ-01 verified resolved (README badge `packs-54`; docs/index.html
  "54 packs · 2 signposts" with publisher groups summing exactly to 54: 15+13+9+6+4+2+1+4).
  MJ-02 verified resolved (nde-ed.org / everyspec.com mirrors recorded in PACK.yaml notes;
  DIST-A in-copy; page-count divergence explained, not hidden). MJ-03 verified resolved —
  chars/page independently recomputed from the extracted texts: 338 = 2,517,789/1046 =
  **2407.1**, 516 = 1,556,876/527 = **2954.2**, matching the SUMMARY to the decimal.

The one MAJOR is a registration-surface miss of exactly the class MJ-01 was folded to
close: the Cursor marketplace manifest still enumerates the pre-Phase-3 pack set.

## Deviation adjudication: doe-413-3b built from O 413.3C

**ACCEPTABLE — documented at every provenance surface.** The pack was built from the
successor consolidated Order (DOE O 413.3C, approved 2026-08-05) under the `doe-413-3b`
slug. The deviation is disclosed in: PACK.yaml `source_version` + `notes` (naming the
cancellation and the T1-06 continuity rationale), the LICENSE header ("DOE O 413.3C …
Cancels DOE O 413.3B, Chg. 7"), the SKILL.md frontmatter description, the SKILL.md
"Source" line and Scope & Limits, the catalog.json `source_version`, and the NOTICE
block. The cancellation clause was independently confirmed in the extracted source text
("2. CANCELLATION. This Order cancels DOE Order (O) 413.3B, Chg. 7"). Licence basis
(17 U.S.C. § 105) is unaffected by the edition change. Residual nit recorded as MI-03.

## Blockers

None.

## Major

### MA-01: Registration sweep missed `.cursor-plugin/plugin.json` — the Cursor marketplace manifest still ships the 47-pack pre-Phase-3 set

**File:** `.cursor-plugin/plugin.json` (`skills` array, 47 entries); registration commit `863bfeb` (file untouched; last modified in `6ede444`, v1.16.3)
**Issue:** The Cursor manifest enumerates packs explicitly and its own description
curates "genuinely open, commercially-redistributable sources". The 8 new packs are
Tier-1 public domain with `commercial_use: true` — the most eligible packs in the repo —
yet none is listed (the only other omission is sebok, correctly excluded as NC). The
manifest is a live, tracked, published install surface (RR-B-29): a user installing via
Cursor today gets 47 packs while the README badge says 54. `check_release.py` only
asserts the file exists (§1 REQUIRED_FILES); nothing verifies its contents, so this
drift is invisible to every gate — the same failure mode as folded MJ-01 (README badge /
docs/index.html), which this phase fixed while missing this third surface.
**Fix:** Add the 8 new packs to `.cursor-plugin/plugin.json` `skills` (47 → 55; sebok
stays excluded), then add a mechanical backstop so this cannot recur, e.g. in
`check_release.py`:
```python
cursor = json.loads((ROOT / ".cursor-plugin/plugin.json").read_text(encoding="utf-8"))
nc_packs = {p.name for p in packs
            if "commercial_use: false" in (p / "PACK.yaml").read_text(encoding="utf-8", errors="ignore")}
cursor_slugs = {s.get("name") or s.get("path", "").split("/")[-2] for s in cursor.get("skills", [])}
missing = {p.name for p in packs} - nc_packs - cursor_slugs
if missing:
    fail(errs, f"[cursor] manifest omits eligible packs: {sorted(missing)}")
```
Folding it into Phase 5 ("installers, and release artifacts include the new packs") is a
partial safety net, but the manifest is already published on main, so fix it now.

## Minor

### MI-01: Link-policy gate `SOURCE_HOSTS` has blind spots exactly where Phase 3 downloaded from

**File:** `tooling/check_release.py:47`
**Issue:** The host regex covers sebokwiki/nasa/nist/dla/dau/omg/etc. but not
`cisa.gov`, `energy.gov`, `standards.nasa.gov`-adjacent directives hosts, or the two
mirrors Phase 3 actually used (`nde-ed.org`, `everyspec.com`). The current packs are
clean (verified by manual grep), but a future edit that pastes a Phase-3-era source or
mirror URL into a pack or doc would pass the link-policy check.
**Fix:** Extend the regex, e.g. add `|cisa\.gov|energy\.gov|nde-ed\.org|everyspec\.com`
(and consider `whitehouse\.gov|directives\.library`).

### MI-02: MN-08 carry-forward (PACK-SPEC vs rr-s-13 divergence) still unexecuted and untracked

**File:** `docs/PACK-SPEC.md:28-40` (body-order list) vs `tooling/check_release.py` §5b
**Issue:** The plan review's MN-08 asked for a one-line PACK-SPEC addendum (`## When to
use` + Prerequisites as first body section) either in 3-03 Task 3 or as a Phase 5 docs
sync. Nothing in Phase 3 did it, and ROADMAP Phase 5's success criteria don't name it,
so the spec/gate trap for future pack authors remains. All Phase-3 packs satisfy the
gate, so this is not gate-breaking now.
**Fix:** Add the addendum to `docs/PACK-SPEC.md` SKILL.md rules ("body begins with
`## When to use` followed by a `**Prerequisites:**` line, then `## How to Use This
Skill` …") and record it as a Phase 5 docs-sync item.

### MI-03: `doe-413-3b` slug serves O 413.3C content

**File:** `packs/doe-413-3b/` (slug) vs `PACK.yaml` source_version
**Issue:** Acceptable as built (fully documented — see adjudication above), but the
installed skill name `/doe-413-3b` is misleading to end users invoking it, and the
Catalog/Topic routing will surface a "413.3b" name for 413.3C guidance as future Chg
letters ship. Cheap to hold; expensive to rename after wide adoption.
**Fix:** At the next major release (v1.18+, not a patch), consider renaming the slug to
`doe-o-413-3` with a catalog `superseded-by`/alias note, or add the series name to
README/docs grouping so users discover it as "O 413.3 series".

## Info

### IN-01: Catalog license strings for the two DoD packs drop the Distribution Statement A qualifier

**File:** `catalog.json` (mil-hdbk-338, mil-hdbk-516 entries)
**Issue:** Catalog uses the bare `Public Domain (US Government work)` while
PACK.yaml/LICENSE/NOTICE carry the DIST-A-qualified variant. Both forms already coexist
in the catalog (32 bare vs 11 qualified), so this follows the dominant convention; the
qualified form is preserved on the binding surfaces.
**Fix:** Optional consistency sweep — use the `…; Distribution A` form for DoD entries,
or the bare form everywhere.

### IN-02: Untracked working artifacts `docs/capability-pack-map.{md,json}` claim full chapter coverage they no longer have

**File:** `docs/capability-pack-map.md` ("Every chapter in every pack … assigned"), `docs/capability-pack-map.json`
**Issue:** Untracked (never committed), so not a shipped defect — but the claim is now
false (8 new packs / 56 chapters unmapped) and the files sit in `docs/` where a broad
`git add docs/` would commit them stale.
**Fix:** Either regenerate the map including the 8 new packs before ever committing, or
move it under a clearly-local path (e.g. `sources/` or `.planning/`) until it is maintained.

### IN-03: CHANGELOG still describes 1.16.3 / 48 skills

**File:** `CHANGELOG.md` (top entry `## [1.16.3]: 2026-06-26`)
**Issue:** Expected: version bump and release notes are Phase 5 scope (ROADMAP:
"Release surface + v1.17.0"; SOURCE-VETTING already labels the candidates "v1.17.0").
No gate disagreement exists (plugin.json == CHANGELOG == RELEASE-INFO == 1.16.3).
**Fix:** Ensure the v1.17.0 entry lists the 8 packs and folds in the MA-01 cursor
manifest fix so the released surface and notes agree.

## Evidence matrix (independent re-verification)

| Claim (from SUMMARYs / PACK.yaml) | Method | Result |
|---|---|---|
| validate_pack 8/8 PASS | ran `python tooling/validate_pack.py` ×8 | PASS |
| check_release PASS | ran `python tooling/check_release.py` | PASS |
| catalog 54 / tier-1 50; chapters match dirs | parsed catalog.json + counted files | exact |
| SKILLS.md 54+2 header, 8 new rows, gate §6 count | parsed + regex | exact |
| rr-s-13 heading contract on all 8 | gate's exact regex per SKILL.md | 8/8 |
| Chapter Index completeness (no unlinked/dead) | link set vs file set per pack | 8/8 clean |
| No source URLs in packs/docs (beyond gate's host list) | manual grep incl. cisa.gov/energy.gov/mirrors | clean |
| No ≥12-word verbatim runs vs sources | independent 12-gram shingle check vs local full_text (single and dual sources) | 0 hits ×8 |
| source_pages (120/48/38/318/1046/527/263/132) | compared to sources/*/metadata.json | all exact |
| DIST-A in-copy (338 `A.`, 516 `A:`) | grep of extracted full_text | confirmed |
| MJ-03 chars/page 2407.1 / 2954.2 | recomputed len(full_text)/pages | exact |
| MJ-01 badge + index counts | README.md:11, docs/index.html:196-205 | 54; groups sum 54 |
| MJ-02 mirrors recorded | PACK.yaml notes (nde-ed.org, everyspec.com) | present |
| MN-01 zero source leakage | `git show --name-only` ×9 commits | 0 paths |
| 413.3C cancels 413.3B Chg 7 | grep of extracted Order text | confirmed |
| Content grounding (CPG 1.A–2.x, CD-0–CD-4, 800-61 Tables 2/3) | grep of sources | confirmed |
| No cross-pack contamination / template artifacts | grep across packs | clean |
| Intra-pack ch-ref integrity (chapters + support files) | ref extraction vs stems | 8/8 clean |

---

_Reviewed: 2026-08-15_
_Reviewer: ZCode (gsd code reviewer)_
_Depth: deep_

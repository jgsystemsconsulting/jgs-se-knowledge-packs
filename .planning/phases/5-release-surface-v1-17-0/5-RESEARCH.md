---
phase: 5-release-surface-v1-17-0
artifact: research
date: 2026-08-14
inputs:
  - .planning/ROADMAP.md Phase 5, .planning/REQUIREMENTS.md REL-01/REL-02
  - .planning/phases/3-tier-1-packs-public-domain/3-GAP_ANALYSIS.md §6 (routed items)
  - tooling/check_release.py §4 (version single-source), §5c, §6, §6b
  - git log v1.16.3..HEAD, git show 6ede444 (previous release commit), git tag metadata
  - gh release list (repo DOES use GitHub Releases)
---

# Phase 5 Research — Release Surface Sync + v1.17.0

## 1. Version-bump surface inventory

check_release.py §4 (lines 102–116) enforces agreement across exactly three
authorities, reading:

- `.claude-plugin/plugin.json` → JSON `version` field (currently `1.16.3`, line 4)
- `CHANGELOG.md` → first `## [x.y.z]` heading via regex `^##\s*\[(\d+\.\d+\.\d+)\]` (currently `## [1.16.3]: 2026-06-26`, line 12)
- `RELEASE-INFO.txt` → `Version:\s*x.y.z` (line 3; also `Tag: v1.16.3` line 4 and `Staged:` line 5)

If these three disagree (or any is missing), the gate fails. **marketplace.json has
no version field** (grep confirms zero matches) — not a gate surface, no change needed.

Full version-string surface beyond the gate three (verified by grep for `1.16.3`,
plus the file list of the v1.16.3 release commit 6ede444):

| # | File | Line(s) | Current | Format |
|---|---|---|---|---|
| 1 | `.claude-plugin/plugin.json` | 4 | `"version": "1.16.3",` | JSON string (GATE) |
| 2 | `CHANGELOG.md` | 12 | `## [1.16.3]: 2026-06-26` | `## [x.y.z]: YYYY-MM-DD` (GATE, first match) |
| 3 | `RELEASE-INFO.txt` | 3–5 | `Version: 1.16.3` / `Tag: v1.16.3` / `Staged:` | key-colon (GATE on Version only) |
| 4 | `.cursor-plugin/plugin.json` | 5 | `"version": "1.16.3",` | JSON string (not gated, but touched by every release commit) |
| 5 | `README.md` | 10 | badge `version-1.16.3-green` + alt text | shields.io badge |
| 6 | `README.md` | 58 | `(version 1.16.3)` | prose |
| 7 | `README.md` | 207 | `Current: 1.16.3.` | prose |
| 8 | `docs/index.html` | 110, 226 | `REV: <span>1.16.3</span>` | HTML span ×2 |
| 9 | `docs/packs.html` | 86 | `REV: <span>1.16.3</span>` | HTML span — **generated**: `tooling/gen_packs_page.py:version()` reads RELEASE-INFO.txt, so it must be REGENERATED (rerun `python tooling/gen_packs_page.py`), not hand-edited; §5c of the gate fails if packs.html drifts from a fresh generation |
| 10 | `docs/products/website/01-jgs-se-knowledge-packs.yaml` | 15 | `version: "1.16.3"` | YAML (touched by 6ede444) |
| 11 | `docs/products/website/catalog.yaml` | 13 | `version: "1.16.3"` | YAML (touched by 6ede444) |

`install.py` / `install.sh` / `install.ps1`: grep found **no version refs** — nothing
to bump. `.claude-plugin/marketplace.json`: no version field.

Recommended order: edit RELEASE-INFO.txt first (Version + Tag + Staged
`2026-08-15T…Z`), then run `python tooling/gen_packs_page.py` to regenerate
packs.html, then the remaining hand edits.

## 2. CHANGELOG v1.17.0 entry draft

House format (from 1.16.3 / 1.16.2 entries): `## [x.y.z]: YYYY-MM-DD`, sections
`### Added` / `### Changed` / `### Fixed` as applicable, `###` bullets, no em dashes,
"Catalogue now N packs (+2 signposts)" line when packs added (1.16.0/1.15.0 style).
Note: earlier pack releases used long multi-sentence pack entries; Phase 3 asked for
one-line each — draft below uses compact one-liners matching SKILLS.md row text.

```markdown
## [1.17.0]: 2026-08-15

### Added

- **`nist-800-171`** (8 ch): NIST SP 800-171 Rev. 3 — protecting CUI in nonfederal
  systems; the 17 requirement families and assessment orientation. Tier 1 (US-gov public domain).
- **`nist-800-61`** (8 ch): NIST SP 800-61 Rev. 3 — CSF 2.0-aligned incident response
  life cycles, roles, playbooks, and coordination. Tier 1 (US-gov public domain).
- **`cisa-cpg`** (8 ch): CISA Cross-Sector Cybersecurity Performance Goals 2.0 —
  prioritized IT/OT baseline goals aligned to NIST CSF 2.0. Tier 1 (US-gov public domain).
- **`doe-sem`** (8 ch): DOE Systems Engineering Methodology (SEM) v3 — the DOE SDLC,
  Stage Exits, Structured Walkthroughs, In-Stage Assessments, requirements traceability.
  Tier 1 (US-gov public domain).
- **`mil-hdbk-338`** (8 ch): MIL-HDBK-338B Electronic Reliability Design Handbook —
  R/M/A theory, allocation/prediction, derating, FMEA/FTA/SCA, FRACAS/growth
  (Distribution A). Tier 1 (US-gov public domain).
- **`mil-hdbk-516`** (8 ch): MIL-HDBK-516C Airworthiness Certification Criteria —
  tailoring a certification basis and the domain criteria clusters
  (Distribution A). Tier 1 (US-gov public domain).
- **`nasa-ms-7009`** (8 ch): NASA-STD-7009B + NASA-HDBK-7009B models & simulations —
  M&S criticality, V&V domains, uncertainty/sensitivity, risk-informed reporting.
  Tier 1 (US-gov public domain).
- **`doe-413-3b`** (8 ch): DOE O 413.3 series (built from O 413.3C, which cancels
  O 413.3B Chg 7) — Critical Decisions CD-0 to CD-4, performance baselines, EVMS/PARS
  controls, risk-informed governance. Tier 1 (US-gov public domain).
- `docs/SOURCE-VETTING.md`: ruled-out register recording tier decisions for all 11
  v1.17.0 candidates (INCOSE Handbook, INCOSE Guide, ISO/IEC/IEEE 15288/29148/21839,
  ECSS, INCOSE Competency Framework excluded; Def Stan 00-051 deferred-excluded).
- PACK-SPEC.md: SKILL.md body-order rules now state the `## When to use` +
  `**Prerequisites:**` contract the release gate enforces (RR-S-13).

Catalogue now 54 packs (+2 signposts).

### Fixed

- Cursor manifest (`.cursor-plugin/plugin.json`) omitted the 8 new packs; now lists
  all 55 eligible skills, and the release gate reconciles manifest entries against
  eligible pack directories so the manifest cannot drift again (found in code review,
  fixed at 02126ac).

### Changed

- Release-gate and CI link-policy scans skip `.planning/` (internal workflow state);
  CI leak/link scans now mirror the local gate's skip set.
- Source-host link policy extended to cisa.gov, energy.gov, nde-ed.org, everyspec.com.
- Registered the 8 packs on every surface: catalog.json, SKILLS.md, docs/packs.html,
  NOTICE, README badge, docs/index.html, Cursor manifest.
- Repo onboarded to a GSD planning flow (`.planning/` roadmap, requirements, and
  per-phase review artifacts); internal-only, never shipped in installers or the plugin.

```

(Exact chapter counts per pack to be confirmed from each SKILLS.md during plan
execution; SKILLS.md rows above are the source of truth for one-liners.)

## 3. Routed-items disposition (from 3-GAP_ANALYSIS §6)

### 3.1 PACK-SPEC addendum (MI-02 / MN-08) — MUST-DO (docs sync, inside charter)

Current `docs/PACK-SPEC.md` "SKILL.md rules" body-order list (line ~31–40) starts at
`## How to Use This Skill` and never mentions `When to use`. Add one line item at the
top of the ordered list:

```markdown
- Body order: most important first (hosts truncate from the end on compaction).
  - `## When to use` (immediately followed by a `**Prerequisites:**` line naming what
    the reader should already have/know — RR-S-13; enforced by tooling/check_release.py)
  - `## How to Use This Skill`
  ...
```

### 3.2 doe-413-3b framing (MI-03) — DO NOT rename in v1.17.0; add framing + record deferral

Renaming a shipped slug is a breaking change (installers, catalog, manifests, links).
Decision for Phase 5: add series framing (the SKILLS.md row, catalog.json:594,
README/docs grouping, and docs/index.html:203 already say "O 413.3 series / built from
O 413.3C cancels O 413.3B Chg 7"). Two concrete Phase 5 actions:

1. Add one prose line to README (near the pack list or DOE mention): the `doe-413-3b`
   slug is retained for continuity but the pack tracks the current DOE O 413.3 series
   edition (O 413.3C); a rename to `doe-o-413-3` with catalog alias is deferred to
   v1.18+.
2. Record the deferral in the milestone decisions (STATE.md / 5-GAP_ANALYSIS
   residuals) so it survives into v1.18 planning.

### 3.3 Catalog licence-string sweep (IN-01) — RECOMMEND SKIP

Already adjudicated ACCEPTED in 3-GAP_ANALYSIS §3.5: catalog convention is majority
bare (`32 bare vs 11 qualified`); licence-binding surfaces (PACK.yaml, LICENSE, NOTICE)
carry the DIST-A-qualified string for both DoD packs. A sweep would touch ~11 catalog
entries for zero licence-clarity gain and add diff noise to a release commit.
Skip; note as accepted residual in the phase gap analysis. (Catalog line 100 already
shows the qualified form exists where it matters.)

### 3.4 User-owned capability-map files — FLAG ONLY, NOT in scope

`docs/capability-pack-map.{md,json}` are untracked user files from a parallel
workstream, now stale (claim "every chapter mapped" false for 8 new packs / 56
chapters). Phase 5 must NOT commit them; the release commit must use explicit paths
(never `git add docs/` or `git add -A`). Carried as a user-facing flag in the final
report, matching gap-analysis §3.4/§6.5.

## 4. Release sequence

Previous release commit 6ede444 convention: single commit
`release(vX.Y.Z): <summary>` with a detailed body, touching all version surfaces in
one shot; then annotated tag; then push; then a GitHub Release (repo uses
`gh release` — v1.16.3 exists as a GitHub Release titled
`v1.16.3 — RR-S-13 compliance + browsable pack reference`).

Tag style: v1.16.2 and v1.16.3 are **annotated** tags (v1.16.0/1.16.1 were
lightweight; annotated is the recent convention). Message is one line:
`v1.17.0 — 8 Tier-1 public-domain packs (54 +2 signposts)`.

Sequence:

```bash
# 1. surface edits (§1) + PACK-SPEC addendum + README doe framing note + CHANGELOG entry
python tooling/gen_packs_page.py        # regenerate docs/packs.html (picks up 1.17.0 REV)
python tooling/check_release.py         # must print RELEASE CHECK: PASS
python tooling/validate_pack.py         # spot-check a couple of packs (gate already runs all)
git add <explicit paths — NEVER 'git add docs/' or -A (untracked capability-map files)>
git commit -m "release(v1.17.0): 8 Tier-1 public-domain packs + release-surface sync" -m "<body: packs, cursor-manifest fix, PACK-SPEC addendum, ruled-out register, GSD onboarding; gate PASS>"
git tag -a v1.17.0 -m "v1.17.0 — 8 Tier-1 public-domain packs (54 +2 signposts)"
git push origin main --follow-tags      # or: git push origin main v1.17.0
gh release create v1.17.0 --title "v1.17.0 — 8 Tier-1 public-domain packs" --notes-file <tmp notes from CHANGELOG entry>
```

ROADMAP Phase 5 SC1 also expects the gate's catalog basis to read 54 packs / 56
directory basis (48 + 8 new, minus 2 signposts) — confirmed live in gap analysis
(check_release PASS, 55 cursor entries, SKILLS.md 54+2).

## 5. Risks

1. **Version drift surfaces missed** — the gate only checks 3 files; 8 more carry the
   string (§1 table). Mitigation: grep `1\.16\.3` after edits and expect zero hits
   outside `.planning/`, `packs/` (historical PACK.yaml? none found), and git history.
   docs/packs.html drift is separately gated (§5c) but only if regenerated.
2. **`git add docs/` would commit stale untracked capability-map files** (IN-02) —
   use explicit paths only.
3. **GitHub Release vs tag** — repo DOES publish GitHub Releases (v1.16.0–v1.16.3
   exist). Tagging without `gh release create` leaves an inconsistent public surface;
   RELEASE-INFO/README don't document this step, so it's easy to drop. Include it.
4. **CHANGELOG em-dash / link-policy** — the new entry must be em-dash-free
   (check_release scans CHANGELOG.md for source-host URLs; keep publisher names
   without URLs) and carry the JGSC/SPDX header (already present at top of file).
5. **Chapter-count accuracy** — draft one-liners assume 8 ch per pack; verify each
   against SKILLS.md before commit (wrong counts in a released CHANGELOG are
   annoying to fix).
6. **OneDrive working tree** — repo lives under OneDrive; file-lock/sync lag can
   occasionally make git operations flaky on Windows. Re-run check_release
   immediately before tagging.
```

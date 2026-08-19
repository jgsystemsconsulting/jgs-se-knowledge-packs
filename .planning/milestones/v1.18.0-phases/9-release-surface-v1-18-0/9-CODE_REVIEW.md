---
phase: 9-release-surface-v1-18-0
reviewed: 2026-08-17T01:13:00Z
depth: deep
scope: full (repo at HEAD 98bd340; tag v1.18.0 tree + working tree + GitHub Release surface)
files_reviewed: 9
files_reviewed_list:
  - CHANGELOG.md
  - RELEASE-INFO.txt
  - docs/packs.html
  - docs/capability-pack-map.json
  - docs/capability-map-CONTRACT.md
  - docs/SOURCE-VETTING.md
  - .planning/STATE.md
  - .planning/MILESTONES.md
  - .planning/REQUIREMENTS.md
findings:
  critical: 0
  blocker: 0
  major: 0
  minor: 0
  info: 2
  total: 2
status: issues_found
verdict: PASS_WITH_NOTES
---

# Phase 9 Full-Scope Code Review (repo at 98bd340; tag v1.18.0)

**Verdict:** PASS_WITH_NOTES

Full-scope adversarial pass over the v1.18.0 public release surface: both gates
re-executed fresh, the tag tree and working tree compared, the GitHub Release
notes diffed against the CHANGELOG substance, and every Phase 9 SC re-verified
independently of the SUMMARY. No blockers, no majors, no minors — two info-level
observations. The impl-scope findings (MI-01 planning-record hygiene) live in
9-IMPL_REVIEW.md and carry no repo-wide weight.

## Full-Scope Verification Matrix

| Check | Method | Result |
|---|---|---|
| `python tooling/check_release.py` fresh | executed now | exit=0, `RELEASE CHECK: PASS` |
| `python tooling/check_capability_map.py` fresh | executed now | exit=0, `PASS: capability map OK`, TOTAL: 628, 32 clusters |
| Catalog basis | `python -c len(json...)` | 61 packs |
| Directory basis | `ls packs \| wc -l` | 63 |
| Cursor manifest basis | parsed plugin.json | 62 skills (matches CHANGELOG "62 skills total") |
| packs.html generator idempotency | re-ran `gen_packs_page.py`, `git diff --stat docs/packs.html` | empty — byte-identical (never hand-edited) |
| IN-04 reconciliation | RELEASE-INFO vs capability-pack-map.json | Version 1.18.0 == map_version "1.18.0", schema_version 2 |
| Residual 1.17.0 sweep | grep excl .planning/.git/sources | CHANGELOG history + exactly the 5 whitelisted doc lines (CONTRACT:54, pack-map:16, VETTING:93/144/149) |
| 11 surfaces in tag tree | `git show v1.18.0:<f>` spot-checks | all 1.18.0 (plugin ×2, RELEASE-INFO, README ×3 lines, index ×2, packs.html, YAMLs ×2) |
| 11 surfaces in working tree | grep | all 1.18.0; zero content drift vs tag (`git diff v1.18.0 -- ':!.planning'` empty) |
| Working tree clean | `git status --short` | clean — nothing unstaged behind the release |
| Tag peel + annotation | `git cat-file -t/-p v1.18.0` | annotated tag object cae0145, tagger set, peels to d19be1a; `git diff v1.18.0 d19be1a` empty |
| Tag on origin | `git ls-remote --tags origin` | refs/tags/v1.18.0 + peeled ref present |
| Last content commit | stats for 7081649, 7e0de75, 98bd340 | all three touch `.planning/` only; d19be1a remains the last content commit |
| Release commit file set | `git show --stat d19be1a` | exactly the 11 expected files; CHANGELOG numstat 68/0 (pure insertion) |

## CHANGELOG Substance vs Live Sources

- Chapter counts: every "(N ch)" re-read from `packs/<slug>/PACK.yaml` `chapters:`
  — 8/6/6/7/7/8/10 all match (dote-te-guidebook, faa-std-025, federal-bca,
  dafman-63-119, mil-std-881f, mil-std-40051, dod-vva-rpg).
- Rename-leads: the doe-413-3b → doe-o-413-3 paragraph precedes the first `###`;
  catalog.json confirms `"slug": "doe-o-413-3"` with alias `doe-413-3b` retained,
  so the "update automatically via alias" claim is true against the shipped catalog.
- v1.17.0 wording fix present in Fixed; the historical 1.17.0 entry itself is
  intentionally unedited (numstat proves zero deletions) — correct
  Keep-a-Changelog behavior, corrected via the release note rather than history
  rewrite.
- Entry hygiene: em dash 0, en dash 0, `http` 0 within lines 12-79. Publisher
  names bare. No URL/link-policy violations (gate also PASS).
- No duplicated Changed items: the 1.18.0 Changed ("Registered the 7 packs on
  every registered surface: catalog.json, SKILLS.md, docs/packs.html, NOTICE,
  README, Cursor manifest") is distinct from 1.17.0's ("the 8 packs ... docs/index.html")
  and the 1.17.0 `.planning/` scan-skip item is correctly NOT restated.
- Caveats verified on the three mandated packs (vva ~2011 dates, faa Rev F vs
  ROSAP Rev E, 40051 counters 1168 vs 584).

## GitHub Release vs CHANGELOG Substance

`gh release view v1.18.0`: isDraft=false, published 2026-08-17T01:03:47Z, title
`v1.18.0 — 7 gap-driven Tier-1 packs + capability map v2` (house em-dash title
style, distinct from the entry's no-em-dash body rule), tagName v1.18.0. The notes
body is the CHANGELOG entry body verbatim: leads with the rename paragraph, then
the same Added (7 pack one-liners + map v2 + CONTRACT + "Catalogue now 61 packs
(+2 signposts)."), the same four Fixed items, the same single Changed item.
Substance matches; nothing added or dropped in transit.

## Planning Records (post-tag 7081649 / 7e0de75 / 98bd340)

- REQUIREMENTS.md: REL-1x-01 and REL-1x-02 both `[x]` with accurate substance
  (01: full registration + check_release PASS; 02: tag + release + wording fix +
  rename note).
- STATE.md: "Current focus: v1.18.0 SHIPPED"; IN-01 and IN-04 recorded closed
  with the exact reconciled values; v1.19 backlog carried (FUT-04 Army CBA retry,
  FUT-05, 7-CODE-REVIEW IN-02, thin clusters 3/5/15, ROSAP/optional notes).
- MILESTONES.md: v1.18.0 shipped record with release commit hash, tag text, and
  release URL — cross-checked against live git/gh data, all three match.
- ROADMAP.md: Phase 9 checkbox `[x]` (line 79) and `9-01-PLAN.md` listed `[x]`
  under Phase 9 Details.

## Findings

### CR-INFO-01: Pre-existing UTF-8 BOM on CHANGELOG.md line 1

**File:** `CHANGELOG.md:1`
**Class:** INFO
**Issue:** The file begins with EF BB BF before the `<!--` license comment. This
predates the release (parent d19be1a~1 carries the same BOM) — NOT introduced by
Phase 9 — and is harmless to the gate and to Markdown renderers, but it is a
latent nuisance for byte-diff tooling and BOM-sensitive consumers.
**Fix:** In a future docs-only commit, strip the BOM (`sed -i '1s/^\xEF\xBB\xBF//'`
equivalent or editor rewrite as UTF-8 without signature). Do not fix under the
v1.18.0 tag retroactively.

### CR-INFO-02: Working tree checked out with CRLF, blobs stored LF

**File:** `docs/packs.html` (and repo-wide on this Windows checkout)
**Class:** INFO
**Issue:** Working-tree head bytes show `0d` (CR) where git blobs store `0a` (LF) —
an autocrlf checkout artifact. Verified harmless: `git status` is clean and
`git diff v1.18.0` is empty after a fresh `gen_packs_page.py` run, so the
generator + git normalization keep packs.html drift-free. Noted only because
Phase 5 flagged OneDrive/Windows sync as a release risk class.
**Fix:** None required. Optionally pin `.gitattributes` (`* text=auto eol=lf` for
the generated file) in a future tooling pass to remove ambiguity for
non-Windows contributors.

## SC Re-Verification (ROADMAP Phase 9)

| SC | Statement | Verdict |
|---|---|---|
| 1 | check_release PASS at updated catalog/directory basis; all surfaces version-consistent | TRUE — gate fresh PASS; 61/63 basis; 11 surfaces at 1.18.0 in tree and tag |
| 2 | v1.18.0 tagged + GitHub Release; CHANGELOG includes the v1.17.0 wording correction and doe-o-413-3 rename note | TRUE — annotated tag on origin peeling to d19be1a; release published; notes lead with rename; wording fix in Fixed |

**Verdict: PASS_WITH_NOTES** — the v1.18.0 release surface is sound; both
findings are pre-existing/environmental observations, neither actionable before
a v1.19 cycle.

---
*Reviewed: 2026-08-17T01:13:00Z*
*Reviewer: gsd-code-reviewer (adversarial)*
*Depth: deep (full scope)*

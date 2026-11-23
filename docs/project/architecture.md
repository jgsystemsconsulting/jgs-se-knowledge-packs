# Architecture

## AD-1
status: verified
source: 2026-11-03-fix-516c-public-chip

The 516C to 516D correction ships as a prose-only edit of the two public surfaces. No check_release change, no new CI gate, and no edition-label pin belongs to this package (X1 resolved prose-only at the 2026-11-03 pick); the generic edition-label CI gate stays routed to backlog item b-57.

## AD-2
status: verified
source: 2026-11-03-fix-516c-public-chip

Historical 516C mentions stay untouched. CHANGELOG.md release rows record past releases. docs/SOURCE-VETTING.md:L109 is the vetting ledger row for the retired edition, and the 516D vetting record lives in packs/mil-hdbk-516/PACK.yaml:L16. Internal docs/superpowers/ rows are pipeline state. Rewriting any of them would falsify history or drag SOURCE-VETTING semantics into a text swap.

## AD-3
status: verified
source: 2026-11-03-fix-516c-public-chip

The landing page chip and the product YAML DoD list are one lockstep pair. Both edits land in a single diff so the HTML surface and the AI-ingestible YAML cannot disagree after the fix.

## AD-4
status: verified
source: 2026-11-03-cut-unreleased-drain-release

The drain ships as a new patch release 1.24.2, never an amend of 1.24.1: tag v1.24.1 exists at fd22869 and the drain is new content on top of a shipped release. The CHANGELOG cut takes the Keep a Changelog heading form `## [1.24.2]: 2026-11-03`, matching the 1.24.1 section, and moves the Unreleased body verbatim (1 Fixed plus 6 Changed bullets). The `## [Unreleased]` heading stays above it, empty, matching the 1.24.1 cut convention (git show v1.24.1:CHANGELOG.md).

## AD-5
status: verified
source: 2026-11-03-cut-unreleased-drain-release

Generated surfaces are regenerated, never hand edited: docs/packs.html and the 74 docs/packs/<slug>/index.html pages are outputs of tooling/gen_packs_page.py and tooling/gen_pack_pages.py, both reading the release version from the RELEASE-INFO.txt Version line. RELEASE-INFO.txt is bumped before either generator runs, so every generated REV stamps 1.24.2. Hand editing a generated page desyncs it from its writer.

## AD-6
status: verified
source: 2026-11-03-cut-unreleased-drain-release

Git hygiene for the cut: the release commit stages an explicit path list of the nine hand-edited files plus the 76 generator outputs (docs/packs.html, the 74 pack pages, docs/sitemap.xml), never `git add -A`. The four untracked PNGs at the repo root (med-device-hero-after.png, med-device-hero-final.png, med-device-hero-verified.png, signposts-hero-copy-btn.png) and every gitignored path stay unstaged. docs/superpowers/backlog.md is tracked but requires `git add -f`, so a plain add refuses it; it stays unstaged. The annotated tag v1.24.2 is created locally on the release commit only after tooling/check_release.py passes, and this package never pushes to any remote.

## AD-7
status: verified
source: 2026-11-03-cut-unreleased-drain-release

check_release.py regex semantics stay untouched; the cut relies on the gate's first-numbered-heading behavior as the acceptance authority. The three map JSONs (docs/capability-pack-map.json, docs/classification-rules.json, docs/capability-pack-map-note-overrides.json) keep map_version 1.22.0 and see no envelope change; map_version work and the optional map_version-vs-release parity gate belong to P15 after the X2 separate resolution (2026-11-03 pick).

## AD-8
status: verified
source: 2026-11-04-retire-scaffold-offset-vocab

Scaffold trust anchor stays the single PACK-SPEC canonical method string copied verbatim, never a paraphrase. build_pack.py PACK_YAML_TEMPLATE adopts the docs/PACK-SPEC.md:77 method text character for character so scaffold, spec example, and the P7-normalized live fleet read identically. A paraphrase would drift on the next PACK-SPEC edit; the verbatim copy diffs clean against the canonical line in review.

## AD-9
status: verified
source: 2026-11-04-retire-scaffold-offset-vocab

The three non-template loci (build_pack.py docstring, printed next-step 2, README How a pack is built) adopt contents-list freeze wording and drop the retired token set outright: no offset-mapped, chapter-offset, or chapter offsets string survives in any of them. The jgs-reference-skill URL and extraction credit stay; only the retired mapping step changes name. Smoke verifies with source greps plus a template-string read that imports build_pack without calling main, so no packs/ directory is created.

## AD-10
status: accepted
source: 2026-11-22-se-sector-pack-reconciliation

Each sector repo already holds the canonical copy of its publications. nhtsa-vehicle and nrc-nuclear are more complete in the sector repos. easa-rules, faa-8110-49, and fda-med-device match chapter counts and still differ by hash. The three signposts are sector-canonical. SE diffs are drift evidence. This cut does not transplant, merge, or import those diffs into any sector repo.

## AD-11
status: accepted
source: 2026-11-22-se-sector-pack-reconciliation

Removal class matches SE v1.24.4, which removed four UK defence slugs as a patch. This cut removes five content packs and three signposts and ships as patch 1.24.5, not minor 1.25.0. The tag is local. Push of the SE tag, the reference-skill commit, and any pointer commit waits for owner say-so.

## AD-12
status: accepted
source: 2026-11-22-se-sector-pack-reconciliation

The slug checker is copied unchanged into jgs-reference-skill/tools/. The UK copy stays, with a one-line note that the reference-skill path is canonical. Pointer sentences go in docs/FLEET-CONVENTIONS.md of the aviation, med-device, and automotive repos. Those repos have no AGENTS.md. No CI change. The nuclear repo is 42 commits ahead of origin and receives no edit, including no pointer.

## AD-13
status: accepted
source: 2026-11-22-se-sector-pack-reconciliation

Classification assignments and note overrides for the five content packs are deleted, then the capability map is regenerated. Measured on 2026-11-22, those packs account for 48 rows: faa-8110-49 13, fda-med-device 12, easa-rules 9, nrc-nuclear 8, nhtsa-vehicle 6. NOTES_COUNT moves from 710 to 662 if no other row changes. Recompute at cut time. expected_signposts drops automotive-signpost, functional-safety-signpost, and avionics-signpost and keeps the other five in current order. THRESHOLDS floors are not lowered. SE has no EMPTY_TREE_PAIR, and validate.yml does not pin NOTES_COUNT. Do not invent those pins.

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

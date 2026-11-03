# Architecture

## AD-1
status: accepted
source: 2026-11-03-fix-516c-public-chip

The 516C to 516D correction ships as a prose-only edit of the two public surfaces. No check_release change, no new CI gate, and no edition-label pin belongs to this package (X1 resolved prose-only at the 2026-11-03 pick); the generic edition-label CI gate stays routed to backlog item b-57.

## AD-2
status: accepted
source: 2026-11-03-fix-516c-public-chip

Historical 516C mentions stay untouched. CHANGELOG.md release rows record past releases. docs/SOURCE-VETTING.md:L109 is the vetting ledger row for the retired edition, and the 516D vetting record lives in packs/mil-hdbk-516/PACK.yaml:L16. Internal docs/superpowers/ rows are pipeline state. Rewriting any of them would falsify history or drag SOURCE-VETTING semantics into a text swap.

## AD-3
status: accepted
source: 2026-11-03-fix-516c-public-chip

The landing page chip and the product YAML DoD list are one lockstep pair. Both edits land in a single diff so the HTML surface and the AI-ingestible YAML cannot disagree after the fix.

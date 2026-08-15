# Patterns — NASA M&S Credibility (7009B)

## Pattern: Intended-use to permissible-use to proposed-use chain
- **When**: Any M&S that will inform decisions.
- **How**: Write intended use at start; freeze permissible uses at development exit; assess each proposed use against that freeze and V&V domains.
- **Trade-offs**: Extra documentation up front; prevents silent repurposing later.

## Pattern: Dual assessments (capability vs results)
- **When**: Developing an M&S and later using it for analysis.
- **How**: Rate capability factors at development/release; rate results factors per analysis; report both and gaps to thresholds.
- **Trade-offs**: Two ceremonies instead of one score; clearer ownership of residual risk.

## Pattern: Warning-first decision briefing
- **When**: Presenting M&S results to decision makers.
- **How**: Lead with required warnings (envelope breaks, open defects, waivers), then nominal results, uncertainty, and risk acceptance.
- **Trade-offs**: Less clean slides; far better decision hygiene.

## Pattern: Phase products as requirement evidence
- **When**: Mapping handbook life-cycle phases to STD shalls.
- **How**: For each phase exit, list which M&S requirement records were created or updated (pedigree, V&V, uncertainty, guidance).
- **Trade-offs**: Requires CM discipline; makes audits mechanical.

## Pattern: Sensitivity-guided pedigree investment
- **When**: Resources for data quality are limited.
- **How**: Run sensitivity early; spend pedigree and uncertainty effort on high-influence inputs first.
- **Trade-offs**: Early analysis cost; avoids polishing irrelevant inputs.

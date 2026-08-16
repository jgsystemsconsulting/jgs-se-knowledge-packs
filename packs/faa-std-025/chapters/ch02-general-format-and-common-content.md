# Chapter 2: General Format and Common Content

## Core Idea
Before type-specific detail, every IRD/ICD must meet shared preparation rules: reference the right companion standards, use a prescribed outline, complete required front matter, and fill common scope/responsibility/reference/QA sections so reviewers can navigate and verify consistently.

## Frameworks Introduced
- **Generic TOC outlines**: Figures in the standard define minimum section trees for facility/analog/discrete interfaces versus general-service/web-service interfaces.
- **Front-matter package**: Covers, approval signature page, revision record, and table of contents.
- **Common content block**: Scope wording templates, responsibility lists, referenced documents, quality assurance/verification scaffolding, delivery notes, and definitions/abbreviations.
- **Companion standards**: Prepare with the latest FAA-STD-005; requirement drawings per FAA-STD-002; clarity/legibility per ANSI/AIIM MS52 and MS38.

## Key Concepts
- **Header/footer and numbering**: Consistent headers/footers, page numbering, hierarchical paragraph numbering, and controlled drawings/tables.
- **N/A language**: When a required outline item does not apply, state explicitly that the IRD/ICD imposes no explicit requirements/characteristics for that titled item.
- **Incorporation by reference**: If a subsection is fully imposed by another approved IRD/ICD, list number/title plus the reference and applicable sections only.
- **Scope sentence templates**:
  - IRD (subsystem): interface requirements between [subsystem 1] and [subsystem 2] or [Service] (or "user").
  - ICD: satisfies interface design requirements in [parent requirements document number/title].
  - Facility IRD: interface between [facility] and [subsystem]/[Service].
- **Responsibility lists**: IRD lists interfacing subsystems/facilities and responsible FAA organizations; ICD adds program office and developing contractor. Web-service IRDs need not enumerate every possible "user" but should coordinate with known users.
- **Referenced documents**: Cite version/date; state tailoring and verification methods; keep references accessible for the document lifecycle (prefer FAA configuration control under Order 1800.66).
- **Appendices**: Allowed for lengthy detail; if they impose requirements they must be called from body sections.

## Mental Models
- **Template before content**: Choose the correct outline (decision tree) first, then fill; do not invent a novel structure.
- **Traceability starts in common sections**: Scope, parties, and references set the bilateral ownership context before technical shalls appear.
- **Silence is non-compliant**: Every required outline slot is either filled, N/A'd, referenced, or TBS'd.

## Anti-patterns
- Omitting approval/signature or revision-record front matter.
- Referencing undated standards or unreachable registries.
- Dumping all technical detail into appendices without body callouts.
- Using a service-interface outline for a pure facility space/power interface (or the reverse).

## Key Takeaways
1. Shared format and front matter are mandatory, not optional polish.
2. Common content fixes scope wording, owners, references, and verification scaffolding.
3. Explicit N/A, reference-only, and TBS patterns keep outlines complete without fake requirements.
4. Companion FAA/ANSI standards govern drawings and presentation quality.

## Connects To
- **ch01**: Why IRD/ICD exist and when each is required.
- **ch03**: Detailed IRD technical sections that hang off the common outline.
- **ch04**: Detailed ICD design-characteristic sections.
- **ch05**: QA/verification detail (VRTM, levels, methods).

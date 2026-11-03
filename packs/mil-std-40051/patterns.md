# Patterns: MIL-STD-40051E w/Change 1, 30 July 2025

Practice heuristics for authoring and review. When / How / Trade-offs. No matrix cells. No plates.

## Pattern: Select before you write

- **When:** A new TM type or maintenance level is on contract.
- **How:** Fill Appendix A with the acquiring activity and MATDEV. Open only the content objects the matrix requires. Then author against sections 4 and 5.
- **Trade-offs:** Up-front matrix time costs schedule early and saves noncompliant drafts later. Skipping the matrix creates silent scope fights.

## Pattern: One content model, two renders

- **When:** The program must ship page-based and interactive outputs.
- **How:** Author structured WPs once. Apply IETM functionality rules where the output is interactive. Do not maintain two unrelated manuscripts.
- **Trade-offs:** Structured authoring needs tooling discipline. Dual manuscripts drift and double the change cost.

## Pattern: WP as the citation atom

- **When:** Training, field use, or change packages must point at a stable unit.
- **How:** Give every WP a unique ID and a clear title. Keep sequence numbers coherent inside the module. Prefer WP references over fragile page numbers in cross-references.
- **Trade-offs:** Good IDs take editorial care. Page-only references break when pagination shifts.

## Pattern: Safety in two layers

- **When:** Procedures include hazards.
- **How:** Maintain the front warning summary and the step-adjacent WARNING/CAUTION/NOTE (and HAZMAT) presentations required by the general spine.
- **Trade-offs:** Dual layers add volume. Single-layer warnings hide hazards from users who skip the front matter or the step text.

## Pattern: Special types stay special

- **When:** BDAR, destruction, PMC, LO, software, hand receipt, TB, or ammunition products appear.
- **How:** Load the matching appendix (H-Q). Keep the shared front-matter and WP spine unless the appendix states an override.
- **Trade-offs:** Type-specific appendices add reading load. Stuffing special content into a generic operator book hides duties reviewers expect to find.

## Pattern: Change with visible effectivity

- **When:** Fielded manuals must move to a new issue.
- **How:** Use change packages or a revision path with markings, notices, and effective-page/WP lists that match the delivered files.
- **Trade-offs:** Honest effectivity costs configuration work. Hidden edits create mixed fleets and training mismatch.

## Pattern: Name, do not paste

- **When:** External standards, statutes, or DoDI-class documents are relevant.
- **How:** Name them. Point authors to the controlling issue in the contract. Do not paste long quotations into pack notes.
- **Trade-offs:** Naming forces readers to open the real source. Pasting creates license and drift risk.

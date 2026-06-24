# Chapter — Building the Model: Verification and Validation

## Core Idea

This part of NASA-HDBK-1009A (Rev A, 2025) is where the V&V metamodel stops being a schema and becomes a worked example. Sections 8.14 through 8.22 take the verification and validation elements defined in the handbook's metamodel (Section 7, Figures 7-1 and 7-2) and show each one rendered as an actual SysML diagram or as the table that holds the same content. The recurring move is to pair the metamodel fragment on one side of a figure with a sample diagram on the other side, so a modeler can see precisely which allowed elements and relationships a given view is exercising.

The chapter's organizing claim is that verification and validation are modeled with the *same machinery* but answer different questions. Verification asks whether the system was built to its requirements; validation asks whether it meets stakeholder intent in use. Both are expressed through requirements that carry a verify (or success) attribute, both trace to the requirements they cover, both spawn cases that own activities, and both reference a shared V&V configuration of equipment, people, and facilities. The handbook walks the verification thread first (8.14 through 8.20), then shows the validation thread reusing the identical pattern (8.21 through 8.22).

A second organizing claim is that a diagram and a table are two presentations of one underlying model, not two separate artifacts. Every requirements diagram of verification or validation content in this slice is explicitly paired with a tabular equivalent — a matrix or compliance spreadsheet — and the handbook repeatedly notes that the same information can be shown either way. The model is the source; the diagram and the matrix are both views of it. This keeps the SysML expression tool-agnostic and anchored to NPR 7123.1: the views can change without the SE-level content changing.

## Frameworks Introduced (exact source names, when/how)

- **NASA-HDBK-1009A V&V metamodel (Section 7, Figure 7-2)** — The governing schema. Every verification and validation view in 8.14 through 8.22 is described as following or drawing its metamodel fragment from Figure 7-2 (with the requirements anchor coming from Figure 7-1). Each figure shows the relevant metamodel piece on one side and the sample diagram or table on the other.
- **Requirements Diagram (req)** — Used in 8.14, 8.15, and 8.21 to show verification requirements/statements, their traceability, and validation requirements. This is the SysML view that carries the `verifies` relationship from a verification requirement to a system requirement, and the `satisfies` relationship for validation.
- **Use Case Diagram (uc)** — Used in 8.18 to show V&V cases. The handbook uses the use case to capture the V&V case that owns a V&V activity, with diagrams describing system functions and the interactions between those functions and actors or elements.
- **Block Definition Diagram (bdd)** — Used in 8.19 to decompose the V&V (verification) configuration, showing equipment, personnel, and support facilities.
- **Activity Diagram (act)** — Used in 8.20 to sequence a V&V case, detailing the steps of "Power Test Case 01" using swim lanes to allocate each step to a structural block of the verification configuration.
- **Requirements Verification Matrix** — A tabular view (8.16) of the verification requirements diagram content. The handbook ties it back to NASA/SP-2016-6105 and compares its example to the NASA SE Handbook's own sample matrix.
- **Verification Requirements Matrix / Verification Compliance Spreadsheet (VCS)** — A second table (8.17) presenting the verification requirements and their attributes and relationships directly, rather than indexed by system requirement.
- **Validation Requirements Matrix / Validation Compliance Spreadsheet (VCS)** — The validation analogue (8.22), a tabular view of the validation requirements diagram, again cross-referenced to NASA/SP-2016-6105.
- **NASA/SP-2016-6105 (the NASA SE Handbook), Revision 2** — Cited as the reference for both the Requirements Verification Matrix and the Validation Requirements Matrix; its Table D-1 and Table E-1 are the sample matrices the handbook compares its own examples against.

## Key Concepts

**The verify-method attribute lives in two possible homes.** In 8.14, the verification method is an attribute (`verifyMethod`) on the extended requirement — a SysML extension to the requirement element. The handbook is explicit that this attribute can be modeled either on the requirement itself or on the verification requirement, and that only one location is actually needed even though the example shows it in both places. The recommended practice is to put the method on the requirement during early life-cycle phases and migrate it to the verification requirement later.

**One requirement can have many verification requirements.** The `verifies` relationship is one-to-many: multiple verification requirements can trace to a single system requirement. This is why the model needs both a matrix indexed by system requirement (8.16) and a matrix that lists the verification requirements directly (8.17) — the two tables answer different lookup questions over the same data.

**Success criteria are captured as a constraint.** In both the verification thread (8.15) and the validation thread (8.21), the success criteria for a requirement are modeled as a constraint relationship shown in curly braces beneath the requirement element. This is the same mechanism for verification requirements and validation requirements alike — another instance of the shared pattern.

**V&V cases own activities and reference a configuration.** The use case diagram in 8.18 captures a V&V case that owns a V&V activity. The same V&V configuration can serve both a verification case and a validation case — the example reuses "Verification Configuration 1 — Power Test" across both. In that use case view, the verification configuration itself plays the actor role; actors here may stand for human users, external hardware, or other subjects.

**The configuration decomposes into equipment, people, and facilities.** The bdd in 8.19 breaks the verification configuration down so that the system block appears as a reference property while verification equipment, personnel, and support facilities appear as part properties. This configuration element is also where "facility or lab" information is captured — the matrices in 8.16 and 8.22 deliberately omit a facility column because that data is held in the V&V configuration parts instead.

**The activity diagram allocates steps to structure.** In 8.20 the act diagram explains the internals of "Power Test Case 01" (the same case introduced in 8.15 and 8.18). It uses swim lanes to allocate each test-case step to a block element of the verification configuration, tying the behavioral sequence back to the structural decomposition from 8.19.

**Validation reuses the verification pattern wholesale.** Sections 8.21 and 8.22 mirror 8.15 and 8.16/8.17 element-for-element: a validation requirements diagram with traceability and success-criteria constraints, followed by a validation requirements matrix / compliance spreadsheet. The example validation requirements ("Power During Mission Activity 1" and "Continuity Demonstration") follow the identical Figure 7-2 metamodel as their verification counterparts.

**The handbook's tables deliberately differ from the SE Handbook's.** For both verification (8.16) and validation (8.22), the handbook lists exactly how its example matrix diverges from NASA/SP-2016-6105's Table D-1 and Table E-1. For verification it drops columns like document, paragraph, phase, performing organization, and acceptance requirement, and adds an artifact-for-verification column. For validation it drops phase and performing organization, and adds validation cases, validation artifact, and validation event columns. The point is not that the SE Handbook is wrong — it is that the matrix is a tailorable view, and a project chooses which columns its model exposes.

## Mental Models

**Diagram and table are two windows on one room.** Do not think of the requirements diagram and the verification matrix as separate documents to keep in sync. They are two queries against the same model — the diagram is the graph view, the matrix is the spreadsheet view. The handbook says the same information can be shown either way precisely so a modeler treats them as interchangeable presentations rather than duplicated work.

**Verification and validation are the same shape with the relationship swapped.** Verification requirements carry `verifies`; validation requirements carry `satisfies`. Otherwise the threads are structurally identical — requirement with success-criteria constraint, traced to higher requirements, owning cases that own activities, referencing a shared configuration. Learn the verification thread once and the validation thread is the same diagram with a different label.

**The verify-method attribute migrates with maturity.** Picture the method tag starting life on the requirement when you only know "this will be tested" and moving onto the verification requirement once you know exactly how. The handbook frames this as an early-to-late life-cycle migration, so a single attribute tells you something about where in the program you are.

**The configuration is the bridge between behavior and structure.** The V&V configuration is the one element that the use case (8.18), the bdd (8.19), and the activity diagram (8.20) all reference. It is what lets a test-case step in an activity diagram be allocated to a real piece of equipment or a real person. Read it as the join that keeps behavioral and structural V&V views consistent.

**A matrix column is a modeling choice, not a fixed form.** Because the handbook documents every add and drop relative to the SE Handbook's tables, treat the matrix layout as something you design. Which columns appear is determined by what your model captures and what your program needs to report — the facility column, for instance, is absent only because that data is reachable through the configuration parts.

## Key Takeaways

- Sections 8.14 through 8.22 render the V&V metamodel (Figure 7-2) as concrete SysML views — req, uc, bdd, and act diagrams — each paired with the metamodel fragment it instantiates.
- The verify-method attribute is a SysML extension to the requirement; it can live on the requirement or on the verification requirement, only one is needed, and the recommended practice is to migrate it from requirement to verification requirement as the life cycle matures.
- The `verifies` relationship is one-to-many: several verification requirements can trace to one system requirement, which is why both a requirement-indexed matrix (8.16) and a verification-requirement-indexed matrix (8.17) exist.
- Success criteria are modeled as constraint relationships (in curly braces) on both verification and validation requirements.
- A V&V case owns a V&V activity and references a V&V configuration; the same configuration can be reused across a verification case and a validation case.
- The V&V configuration bdd decomposes into the system (reference property) plus equipment, personnel, and support facilities (part properties), and is where facility/lab information is captured.
- The activity diagram sequences a verification case and uses swim lanes to allocate each step to a structural block of the configuration.
- Validation (8.21, 8.22) follows the identical pattern as verification, differing chiefly in carrying `satisfies` rather than `verifies`.
- Every diagram in this slice has a tabular equivalent (a matrix or compliance spreadsheet); the model is the source and both diagram and table are views, keeping the approach tool-agnostic SysML tied to NPR 7123.1.
- The example matrices are deliberately tailored — the handbook documents exactly which columns it adds and drops versus NASA/SP-2016-6105 Tables D-1 and E-1 — signaling that matrix layout is a project-level modeling decision.

## Connects To

- **NASA-HDBK-1009A Section 7 (Figures 7-1 and 7-2)** — the metamodel these views instantiate; every V&V element here traces back to that schema.
- **NPR 7123.1** — the upstream SE governance the metamodel encodes, which is what makes these V&V views auditable against NASA process rather than tool convention.
- **NASA/SP-2016-6105 (NASA SE Handbook), Rev 2** — the cited source for the Requirements Verification Matrix and Validation Requirements Matrix; Tables D-1 and E-1 are the comparison baselines for the handbook's tailored examples.
- **The V&V configuration (bdd, Section 8.19)** — the shared structural element referenced by the use case, activity, and matrix views; the join point for facility/lab data and step-to-block allocation.
- **The handbook's diagram-and-table duality** — the principle, repeated throughout this slice, that a requirements diagram and its matrix are interchangeable presentations of one model.
- **Property-Based Requirements and the broader metamodel chapter** — the verify-method attribute is one of the SysML requirement extensions that the metamodel's Requirements pillar makes available.

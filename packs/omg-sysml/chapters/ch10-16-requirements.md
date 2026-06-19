# Chapter 10: 16 Requirements

## Core Idea
A requirement specifies a capability or condition that a system must or should satisfy. SysML bridges traditional requirements management tools and model-based design by providing constructs to represent text-based requirements and relate them to system architectures, design elements, test cases, and to each other through a governed set of relationships and hierarchies.

## Frameworks Introduced

- **«requirement»**: A stereotype of UML Class that specifies a capability, condition, function, or performance criterion. Serves as the base construct for requirement-specific taxonomies and analysis.
  - When to use: Define any constraint, need, or obligation that the system must fulfill; enables compound requirements via UML nesting.

- **«AbstractRequirement»**: A base stereotype establishing attributes and relationships essential to any requirement kind; intended for user-defined requirement specializations (operational, functional, interface, performance, physical, design constraints, reliability, etc.).
  - When to use: Create custom requirement taxonomies via stereotyping to enforce domain-specific constraints.

- **«Copy»**: A Trace specialization establishing a master/slave relationship where the client requirement's text is a read-only copy of the supplier requirement's text, enabling requirements reuse across product families and projects without namespace duplication.
  - When to use: Reuse a requirement (e.g., regulatory or contractual) in multiple contexts with centralized updates propagating to all slaves.

- **«DeriveReqt»**: A Trace specialization relating a derived (client) requirement to a source (supplier) requirement, typically indicating analysis that decomposes a higher-level requirement into lower-level requirements aligned to system hierarchy levels.
  - When to use: Link system-level requirements (e.g., vehicle acceleration) to derived requirements at subsystem levels (e.g., engine power, weight, drag).

- **«Satisfy»**: A Trace specialization linking a design or implementation model element (client) to a requirement (supplier) it fulfills, establishing the design-to-requirement contract.
  - When to use: Connect architecture blocks, behaviors, or design decisions to their corresponding requirements; support traceability matrices.

- **«Verify»**: A Trace specialization linking a test case or other model element (client) to a requirement (supplier) whose satisfaction it verifies, supporting inspection, analysis, demonstration, or test methods.
  - When to use: Map test cases to requirements and track verification results via a verdict property (consistent with UML Testing Profile).

- **«Refine»**: A specialization of UML Refine with property-path capability, relating a model element (client) to a requirement (supplier) that refines it (or vice versa), enabling decomposition of text-based requirements into behavioral or structural models.
  - When to use: Elaborate a text-based functional requirement with a use case or activity diagram; reciprocally, refine a coarse model element with detailed textual specification.

- **«Trace»**: A general-purpose relationship between a requirement and any model element with weak semantics (no real constraints), recommended only when other specific relationships do not apply.
  - When to use: Capture generic traceability or exploratory links not formalized by Derive, Satisfy, Verify, or Refine; avoid mixing with stronger relationships.

- **«TestCase»**: A stereotype of Behavior or Operation that verifies a requirement is satisfied, characterized by a return parameter of type VerdictKind (consistent with UML Testing Profile).
  - When to use: Represent verification procedures, test scenarios, or acceptance criteria with explicit verdict results.

- **Requirement Diagram (req)**: A diagram displaying requirements, packages, other classifiers, test cases, and rationale; relationships shown include containment, derivation, satisfaction, verification, refinement, copying, and tracing via graphical paths and callout notation.
  - When to use: Create requirements hierarchies, show relationships to design/test elements, and document rationale for design decisions.

## Key Concepts

- **Requirement**: A UML Class stereotype that establishes a contract between customer/stakeholder and system implementers; must have a unique identifier (`id`) and textual representation (`text`); may include verification status and user-defined properties.

- **Compound Requirement**: A requirement containing nested subrequirements via UML nesting (accessed through `nestedClassifier`). Unless stated otherwise, all nested requirements must be satisfied for the parent to be satisfied; deleting the parent deletes all children.

- **Requirements Hierarchy**: A containment-based decomposition enabling complex requirements to be broken into child requirements (e.g., "the system shall do A and B and C" → three child requirements); supports multi-level nesting.

- **Master/Slave Requirement Pair**: A Copy dependency relationship in which a slave requirement's text is a read-only copy of a master requirement's text, enabling reuse across multiple namespaces (families, versions, projects); updates to the master propagate to all slaves.

- **Derived Requirement**: A requirement (client of a DeriveReqt) obtained through analysis of a source requirement (supplier), typically supporting decomposition across system hierarchy levels (e.g., top-level acceleration → engine power, weight, drag).

- **Verify Relationship**: A formal link between a requirement and a verification method (test case, analysis, demonstration, inspection) that validates the requirement is satisfied; verdict property tracks the verification result (consistent with UML Testing Profile).

- **Requirements Reuse**: The mechanism of applying a single requirement across multiple contexts without duplication; achieved via the Copy relationship and master/slave pairing to maintain bidirectional traceability and centralized updates.

- **Rationale**: An optional annotation attached to any requirement or requirements relationship (e.g., satisfy, derive, verify), providing supporting justification such as trade study results, analysis reports, or test procedure references.

## Mental Models

- **Use compound requirements and nesting when decomposing complex needs**. If a system requirement states "the system shall perform tasks A, B, and C," structure it as a parent requirement with three nested children; the parent is satisfied only when all children are. This enables traceability at fine granularity without flattening the hierarchy.

- **Model derived requirements to show functional or performance decomposition across the system hierarchy**. When analyzing a top-level system requirement to generate subsystem or component requirements, use DeriveReqt to document the analysis path. This preserves the rationale and enables bidirectional traceability from lower-level requirements back to their source.

- **Use Satisfy to link design elements—blocks, operations, behaviors—to the requirements they fulfill**. Do not use Satisfy for verification; instead use Verify (linked to test cases) to separate the "does the design implement the requirement?" question from "is the requirement actually satisfied in operation?" question.

- **Adopt Copy (master/slave) for regulatory, contractual, or reusable requirements that appear in multiple product families or projects**. Centralize the master requirement and propagate updates to all slave instances, avoiding divergence and maintaining consistency across variants.

## Anti-patterns

- **Confusing Satisfy with Verify**: A Satisfy relationship asserts that a design element (e.g., an activity, state machine, or block) implements a requirement; a Verify relationship asserts that a test case validates the requirement is satisfied in operation. Using Satisfy alone does not guarantee verification; both relationships should be present in a complete traceability chain.

- **Mixing Trace with other specific relationships**: The Trace relationship has weak semantics and no formal constraints. Avoid using Trace when DeriveReqt, Satisfy, Verify, Refine, or Copy are more appropriate; mixing these leads to ambiguous traceability and breaks automated analysis tools.

- **Creating requirements that participate in associations or generalizations**: SysML forbids requirements from being used as types, from generalizing/being generalized, or from participating in associations. If the modeler needs to express type relationships, the design element (block, behavior) should be separated from the requirement; the Satisfy relationship links them.

- **Flattening requirements hierarchies unnecessarily**: Avoid creating a single flat list of requirements; instead, nest related requirements to reflect the system decomposition structure. This enables coarse-grained traceability at higher levels and fine-grained traceability at lower levels, supporting both stakeholder communication and verification planning.

## Key Takeaways

1. **Requirements are first-class modeling elements in SysML**, not just external artifacts. They are UML Classes stereotyped as «requirement» and can participate in diagrams alongside blocks, behaviors, and test cases, enabling integrated requirements and design models.

2. **Requirements relationships form a formal algebra**: Derive, Satisfy, Verify, Refine, and Copy are specializations of the Trace relationship with explicit semantics and UML OCL constraints. Use the appropriate relationship type to avoid ambiguity and enable tool-based traceability analysis.

3. **Master/slave copying enables requirements reuse without namespace conflicts**. A slave requirement's text is always synchronized with its master; updates to the master automatically propagate to all slaves, supporting reuse across product families and projects while maintaining consistency.

4. **Compound requirements and nesting support hierarchical decomposition**. A parent requirement with nested children is satisfied only when all children are satisfied (unless the parent explicitly states otherwise). This structure mirrors the system hierarchy and enables bidirectional traceability across decomposition levels.

5. **Rationale is a first-class traceability element**. Attach rationale to any requirement or relationship to document the trade studies, analysis reports, or test procedures justifying design decisions. Rationale is essential for requirements traceability reviews and impact analysis when requirements change.

6. **Verify and Satisfy are complementary**: Satisfy links design elements to requirements; Verify links test cases or other verification methods to requirements. A complete traceability chain includes both: Design satisfies Requirement, and Test verifies Requirement. Separation of concerns ensures both specification and validation are visible in the model.

7. **Custom requirement stereotypes extend the taxonomy without changing semantics**. Define subclasses of AbstractRequirement (e.g., «functionalRequirement», «performanceRequirement») to enforce domain-specific constraints (e.g., only behaviors can satisfy functional requirements). This enables modeler-defined requirement taxonomies while remaining compatible with SysML's core algebra.

## Connects To

- **UML Class & Nesting**: Requirements are UML Classes with specialized constraints. Compound requirements leverage UML's nesting mechanism (nestedClassifier) for hierarchy; the constraints enforce that requirements have no operations, attributes, or associations.

- **SysML Behaviors (Activity, Interaction, State Machine)**: Behaviors appear as clients of Satisfy and Refine relationships, showing how behavioral specifications implement or refine textual requirements. Behaviors are commonly used with Verify (via test cases) to validate requirement satisfaction.

- **SysML Blocks (IBD, Block Definition Diagram)**: Blocks and their ports appear as clients of Satisfy, showing how structural design choices implement system requirements. Internal block diagrams often include callout notation linking blocks to requirements they satisfy.

- **SysML Diagrams (req, bdd, ibd, act, par, sd)**: Requirements can be displayed on requirement diagrams (primary) or on other diagrams (bdd, ibd, act, par, sd) using callout notation to show relationships to other model elements. Callout notation abbreviates the full containment and relationship paths.

- **UML Testing Profile**: The TestCase stereotype is consistent with UML Testing Profile (TP), enabling tool interoperability. The verdict property on test cases (of type VerdictKind) follows TP conventions, supporting integration of verification tools with requirements models.

- **SysML Rationale (Clause 7)**: Rationale is a reusable annotation that documents justification for any requirement or relationship. Rationale is particularly valuable for Satisfy (design rationale via trade studies) and Verify (test procedure references) relationships.

- **ISO/IEC/IEEE 42010 (Viewpoints)**: Requirements diagrams serve as one viewpoint in a system architecture description. Combined with other SysML diagrams (block definitions, interactions, behaviors), requirements models support 42010-compliant architecture documentation.

- **SysML Allocations (Clause 15)**: Allocations express assignments of responsibilities (e.g., functions, flows, requirements) to system elements. Allocations and requirements relationships are often combined to trace requirements allocation across the architecture and to verify that allocated requirements are satisfied.

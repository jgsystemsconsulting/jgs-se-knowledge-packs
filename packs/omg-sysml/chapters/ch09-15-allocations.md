# Chapter 9: 15 Allocations

## Core Idea

Allocation is the mechanism for establishing cross-hierarchy mappings between model elements in SysML, enabling systems engineers to relate abstract and concrete representations (e.g., functions to components, logical structures to physical structures) without forcing them into a single hierarchy. This supports design flexibility, consistency checking, and incremental integration across the model.

## Frameworks Introduced

- **«allocate»** (stereotype of UML::Abstraction): a directional dependency for associating any two NamedElements across different model hierarchies or abstraction levels
  - When to use: mapping functions to components, logical to physical structures, behavior to structure, or flows across representation layers

- **«allocateActivityPartition»** (stereotype of UML::ActivityPartition): a partition on an Activity diagram representing the supplier (to) end of an allocate relationship, with actions within it as the client (from) end
  - When to use: depicting behavior allocation directly on activity diagrams

## Key Concepts

- **Allocation (abstract)**: the organized cross-association of elements within different structures or hierarchies; not constrained to a single design method, enabling abstract, preliminary, and tentative mappings early in design
  
- **Behavior allocation**: the allocation of Activities or Actions (functions) to Blocks or BehavioralFeatures (form), enabling segregation of function from structure

- **Flow allocation**: the mapping of control flow or object flow (ObjectFlow) in activities to flows in structural representations (Connector or ItemFlow)

- **Structure allocation**: the mapping between separate system representations at different abstraction levels (e.g., logical hierarchy to physical assembly hierarchy)

- **Directed allocation**: an Allocate dependency has a client (from, no arrow) and a supplier (to, with arrow), establishing direction of the mapping

- **Property path allocation**: Allocate specializes DirectedRelationshipPropertyPath, permitting source and target identification via multi-level property paths from context blocks (e.g., allocation from a nested part using property path syntax)

- **Element types in allocation**: allocated-from and allocated-to compartments display element type keywords (activity, action, objectFlow, controlFlow, objectNode, operation, block, property, itemFlow, connector, port, value) for clarity; fully qualified names (PackageName::ElementName.PropertyName) avoid ambiguity

## Mental Models

- **Use allocation early as a design driver**: Allocations function as precursors to more detailed rigorous specifications, enabling consistency checking and directing future design activity before concrete relationships are established.

- **Separate representation layers via allocation**: Construct separate logical and physical (or abstract and concrete) system hierarchies, then use allocations to document cross-hierarchy traceability without merging hierarchies.

- **Allocate flows to connectors or item flows**: Model behavior flows (ObjectFlow, ControlFlow) in activity diagrams and allocation relationships to map them to structural flows (Connector, ItemFlow) on internal block diagrams or port flows.

## Anti-patterns

- **Allocating Pin to Port directly**: SysML v1.6 does not address Pin-to-Port allocation; use ObjectNode or ObjectFlow allocation instead and map through the activity-to-structure boundary via allocation compartments or callouts.

- **Assuming AllocateActivityPartition implies scheduling responsibility**: The AllocateActivityPartition maintains structural constraints of UML::ActivityPartition but NOT its responsibility semantics; actions in the partition are not invoked by the classifier represented by the partition. Use standard UML ActivityPartition semantics if direct responsibility is required.

- **Allocating ObjectFlow to Connector as a structural relation**: Allocation of ObjectFlow to Connector is an allocation of usage (the flow instance) and does NOT imply any relationship between the defining Blocks of the ObjectFlow and the associations of the Connector.

## Key Takeaways

1. **Allocations enable flexible cross-hierarchy mapping**: Use them to express tentative, abstract, and preliminary relationships across different model structures (behavior–structure, logical–physical, functional–operational) without constraining design method.

2. **Allocate is a directed dependency**: Always document direction: client (from) represents the source element, supplier (to) represents the target. Render as a dashed line with an open arrow.

3. **Three primary allocation types support systems engineering workflows**: behavior allocation (functions to components), flow allocation (activity flows to structural connectors), and structure allocation (logical to physical or abstract to concrete blocks/parts).

4. **Use compartment and callout notations for diagram clarity**: Display allocated-from and allocated-to elements in model-element compartments or callouts with element-type keywords; use fully qualified names for nested properties when ambiguity is possible.

5. **Property paths enable nested allocation**: Allocate specializes DirectedRelationshipPropertyPath, allowing you to specify allocation sources and targets by traversing property chains from context blocks (e.g., allocating from a nested part without flattening the hierarchy).

6. **Allocations are precursor relationships**: Expect allocations to evolve into concrete relationships (operations, attributes, sub-classes) as design matures; use them for consistency audits and navigation, not as the final design artifact.

## Connects To

- **UML::Abstraction** (dependency superclass): Allocate redefines the base abstract syntax, inheriting UML's binary dependency constraint and extending it with property-path navigation.

- **§9 Ports and Flows**: Flow allocation maps ObjectFlow, ControlFlow, and ItemFlow elements; ItemFlow allocation is a key cross-diagram integration pattern.

- **§4 Blocks and their Structural Features**: Structure allocation maps Block hierarchies, Properties, and Parts across abstraction levels; AllocateActivityPartition integrates activities with block parts.

- **§5 Activities and Behaviors**: Behavior allocation maps Activity and Action elements to block operations and attributes; AllocateActivityPartition appears on Activity diagrams as a partition stereotype.

- **Internal Block Diagram and Activity Diagram syntaxes**: Allocations display in compartments, callouts, and activity partitions across all SysML diagram types; used in IBD, Activity, and tabular representations.

- **DirectedRelationshipPropertyPath** (base stereotype): Enables navigation of allocation sources/targets via multi-level property paths, critical for nested structure and part allocation.

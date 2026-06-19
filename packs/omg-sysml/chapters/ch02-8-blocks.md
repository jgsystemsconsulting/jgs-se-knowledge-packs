# Chapter 2: 8 Blocks

## Core Idea
Blocks are the primary modular units of system description in SysML. They capture structural and behavioral features—properties, operations, connections—that define a system or element of interest. Blocks provide a general-purpose capability to model hierarchical, multi-domain systems (logical, physical, software, hardware, human) across all lifecycle phases, with internal structure shown on Internal Block Diagrams (IBDs) and relationships defined on Block Definition Diagrams (BDDs).

## Frameworks Introduced

- **«block»**: A modular unit describing structure and behavior of a system via structural features (properties, parts, references) and behavioral features (operations, behaviors). Shown on Block Definition Diagrams (BDDs).
  - When to use: To define any reusable system element or conceptual entity; parts typed by blocks model hierarchical decomposition.

- **«valueType»**: A classifier for value entities that cannot be identified by reference—typed by UML DataType. May carry units and quantity kinds. Shown on BDDs.
  - When to use: To type value properties (e.g., Real, Integer, String, domain-specific quantities like Length or Mass).

- **Property**: A feature of a block representing state, relationships, or parts. Four classification types: *part* (composite, owns instances), *reference* (non-composite, shares instances), *value* (typed by ValueType), *constraint* (constrains others via ConstraintBlock).
  - When to use: To represent any structural element within a block's definition or internal structure.

- **PartProperty**: A property with composite aggregation typed by another block—owns one or more instances of the type.
  - When to use: To model decomposition and part-whole relationships in physical/logical hierarchies.

- **ReferenceProperty**: A property without composite aggregation—refers to shared instances.
  - When to use: To model associations and cross-cutting relationships without ownership.

- **ValueProperty**: A property typed by a SysML ValueType—always composite aggregation.
  - When to use: To represent quantitative, qualitative, or categorical attributes (mass, name, status).

- **Port**: A special property defining allowable interactions between blocks. Addresses cross-domain communication (software operations, discrete flows, continuous interactions). Detailed in Clause 9.
  - When to use: To specify external interfaces, communication contracts, and interaction types.

- **Connector**: A relationship between two properties of a block, specifying how parts or other properties link. May be typed by associations or binding connectors.
  - When to use: To capture internal wiring, data flow, or control flow within a block's structure.

- **«bindingConnector»**: A connector specifying that properties at both ends hold equal values (recursively for ValueTypes, same identity for Blocks).
  - When to use: To constrain nested property values in hierarchical configurations.

- **BoundReference**: A reference property that uses binding connectors to highlight constraint roles—types of constrained properties.
  - When to use: To make explicit which properties are constrained by which binding paths in configuration models.

- **«associationBlock»**: A block stereotype applied to an Association Class, enabling association instances to carry their own internal structure and properties.
  - When to use: To model relationships that have identity, behavior, and state (e.g., a supplier-part link with contract terms).

- **«participantProperty»**: A property of an association block identifying instances at each association end—linked objects at the association ends.
  - When to use: Inside association blocks to navigate from a link instance to its participant objects.

- **«connectorProperty»**: A property whose value is the instances of a connector's association block type.
  - When to use: To expose connector instances (links) as first-class objects accessible within a containing block.

- **«adjunctProperty»**: A property constrained to hold values of connectors, call actions, object nodes, variables, parameters, interaction uses, or submachine states—captures execution/token/assignment results.
  - When to use: To bind property values to behavioral execution context without explicit composition.

- **«classifierBehaviorProperty»**: A property constrained to hold executions of classifier behaviors.
  - When to use: To reify active behavior instances as properties.

- **«nestedConnectorEnd»**: A connector end that crosses nested property boundaries to connect to properties deep within a structure—used when strict encapsulation cannot be maintained.
  - When to use: When connector topology spans multiple levels of part decomposition; avoid if possible (prefer intermediate properties).

- **«boundReference» stereotype**: Applied alongside EndPathMultiplicity to redefine bound references with explicit path-end multiplicities (lower/upper cardinality constraints on nested targets).
  - When to use: To constrain the number of values reachable through a nested binding path in specializations.

- **PropertySpecificType**: A classifier typed by exactly one property and owned by that property's owner—instances auto-classify when added to the property, auto-declassify when removed.
  - When to use: To attach context-specific features (operations, properties) to values only while they occupy a specific role.

- **Compartment**: A labeled section within a block definition box partitioning features. Standard: *properties*, *parts*, *references*, *values*, *constraints*, *classifier behavior*, *owned behaviors*, *receptions*. Non-standard: *namespace* (nested blocks), *structure* (internal connectors), *bound references*, *initialValues*.
  - When to use: To organize and highlight feature categories for readability.

- **Internal Block Diagram (IBD)**: Diagram showing internal structure of a single block—properties as boxes (solid for parts/values, dashed for references), connectors as lines, multiplicity and nesting notation on connectors.
  - When to use: To detail composition, connectivity, and part interactions within a block.

- **Block Definition Diagram (BDD)**: Diagram showing block definitions, their features (properties, operations), relationships (associations, generalizations, dependencies), and compartmented structure.
  - When to use: To capture taxonomy, feature inventory, and relationships between system elements.

- **InitialValues compartment**: A compartment on an IBD showing context-specific default values for properties, overriding type defaults. Supports nested path notation.
  - When to use: To configure specific instances with design values different from the type definition.

## Key Concepts

- **Modular units of system description**: Blocks encapsulate a collection of features (structure and behavior) to define systems or elements of interest across logical/physical/software/hardware/human domains and all lifecycle phases.

- **Property type classification**: Four categories—*part property* (composite, owns; shown black diamond on BDD), *reference property* (non-composite, shares; shown dashed outline on IBD), *value property* (typed by ValueType; always composite), *constraint property* (constrains other properties via ConstraintBlock).

- **Part-whole semantics**: A part belongs to at most one composite instance at a time, though may be value of multiple part properties of containing block. Operations and relationships on wholes typically apply transitively to parts; domain-specific interpretations (delete, copy, move) may apply across all levels.

- **Context-specific values**: The InstanceValue/InstanceSpecification mechanism enables trees of values on an IBD's initialValues compartment to override type defaults for a particular usage context, recursively through nested properties.

- **Composition acyclicity constraint**: Within a block instance, values of composite properties must not form cycles—the composition hierarchy is an acyclic graph.

- **Navigation equivalence**: In SysML, navigation is equivalent to a named property; unnamed ends on associations exist only to record inverse multiplicity (not as navigable properties).

- **Encapsulation flag**: Block.isEncapsulated = true → black box (connections via ports or outer boundary only); false/unset → connections can reach internal structure via nested connector ends.

- **Binary-only connectors**: All connectors and block-typed associations must have exactly two ends (simplification vs. UML's n-ary support).

- **Binding path as constraint**: A binding connector specifies equality of values (or identity of objects) on both ends; nested ends follow property paths; bound references make these constraint roles explicit.

- **Default multiplicities**: On BDD, part/shared associations default to [0..1] on diamond end; unidirectional associations default to 1 on target. On IBD, connectors default to 1 on each end. Non-default multiplicities should always be shown to avoid ambiguity.

- **Property paths for nested access**: Internal properties may be referenced by dotted notation (e.g., `car.engine.cylinder.piston.length`) as a notational shorthand for deeply nested structure.

- **Quantity kinds and units**: ValueTypes may associate a QuantityKind (VIM concept of "kind of quantity") and Unit (VIM concept of "measurement unit"). Unit/QuantityKind instances are InstanceSpecifications classified by SysML library blocks; equivalence determined by definitionURI.

## Mental Models

- Use blocks as the primary vocabulary for decomposition, classification, and part-whole relationships across any system domain. Treat each block as a contract defining what instances of that block must have (features) and how they relate internally (connectors).

- Partition features into compartments (parts, references, values, constraints) to make modeling intent visible and diagrams readable. Use structure/namespace compartments on BDDs to embed IBD-like views for wide diagrams.

- Model hierarchical systems by typing parts with blocks: a wheel block can be used as a part property in a car block; the part defines a local usage of the wheel in a specific context (front wheel vs. rear wheel), allowing context-specific values (25 psi front, 30 psi rear) via initialValues.

- Reach encapsulation by setting isEncapsulated = true on a block definition and routing all external connections through ports. Nested connector ends bypass encapsulation—reserve them for cases where intermediate properties are infeasible or inappropriate.

- Use binding connectors and bound references to express invariant constraints on nested decomposition: "all wheels must have the same tire pressure" or "number of cylinders is fixed per vehicle specialization." Nested binding paths capture these constraint hierarchies.

- Build reusable association blocks (blocks applied to association classes) when relationship instances need their own properties and behavior (e.g., a Supplier-Part link with contract start date and terms).

- Apply property-specific types to distinguish role-contextual features: a Machine becomes a WarehouseItem (with location) when stored in a warehouse, automatically acquires location property, and loses it when leaving the warehouse.

## Anti-patterns

- **Mixing compartments without hierarchy**: Avoid showing both feature compartments and structural compartments (namespace, structure) in a single definition box if space is tight. Use separate boxes or nested compartment organization.

- **Ignoring multiplicity defaults**: Relying on implicit [0..1] or 1 multiplicities without showing them on diagram. Always display non-default multiplicities to prevent reader ambiguity.

- **Nested connector ends as primary decomposition**: Overusing nested connector ends to bypass encapsulation. Prefer adding intermediate properties at each containment level—encapsulation is more than black-box syntax; it reflects design intent.

- **Unconstrained association directions**: Using bidirectional associations (arrowheads on both ends) or unnamed inverse ends carelessly. SysML enforces navigation = ownership; unnamed ends exist only for inverse multiplicity bookkeeping.

- **Flat part-whole relationships**: Modeling complex systems with only one or two levels of decomposition. Leverage multi-level nesting and property paths to reflect system structure and facilitate reuse.

- **Confusing reference properties with shared aggregation**: SysML reference properties have aggregationKind = none (no semantic distinction). Shared aggregation (white diamond) is defined in UML but SysML leaves its interpretation to the domain—avoid if clear ownership can be expressed.

- **Over-constraining with binding connectors**: Binding connectors are powerful but can make models hard to read. Use them sparingly for critical invariants; document their purpose in notes.

## Key Takeaways

1. **Blocks are the standard reusable unit for system description**. Every system element, subsystem, or interface should be modeled as a block. Blocks work across logical, physical, software, hardware, and human domains without domain-specific variants.

2. **Property type matters for semantics**. Parts own instances (composite); references share them. Value properties are immutable data. Constraint properties bridge structure and behavior. Choose the right type to make intent clear and enable automated consistency checks.

3. **Internal Block Diagrams show structure; Block Definition Diagrams show taxonomy**. Use BDDs for class-level relationships (inheritance, associations), IBDs for instance-level wiring. Compartments on BDDs can embed structure or namespace views for wide diagrams.

4. **Context-specific values override type defaults**. Use initialValues compartments on IBDs to specify design configurations without creating new block types. This enables one wheel block to represent front and rear wheels with different pressures.

5. **Encapsulation and nested connectors are a tradeoff**. Set isEncapsulated = true and route all external access through ports for true black-box design. Nested connector ends pierce encapsulation for wiring that crosses part boundaries—use only when intermediate properties are infeasible.

6. **Binding connectors and bound references express hierarchical constraints**. Binding paths capture equalities or identity requirements that span nested structures. Use bound references to explicitly mark which reference properties are constrained and how.

7. **Association blocks turn relationships into first-class objects**. When a relationship (supplier-part, component-circuit) needs its own properties (contract, parameters), stereotype the association class as a block and add participant properties to navigate the link's endpoints.

## Connects To

- **UML Class, Association, Composite Structure**: SysML blocks extend UML classes and composite structures; associations and composite structure connectors are the basis for SysML connectors and binding connectors. SysML simplifies UML by excluding n-ary associations and navigation-end ownership.

- **Clause 9, Ports and Flows**: Ports are special properties defining interaction contracts; flows describe data or item transport between ports. Port hierarchies and port conjugation enable typed communication across block boundaries.

- **Clause 10, Constraint Blocks**: Constraint properties are properties typed by constraint blocks; they reify mathematical or domain constraints as block instances.

- **Clause 15, Allocations**: Allocations assign behavioral responsibilities to blocks and parts; often used to map abstract functions to concrete hardware or software blocks.

- **Behavioral Constructs (Activities, Interactions, State Machines)**: Blocks may own classifier behaviors or operations. Behaviors describe time-dependent or event-driven dynamics; blocks provide the structural context into which behaviors are placed.

- **ISO/IEC/IEEE 42010 (Architecture Description)**: Block hierarchies and block relationships (associations, generalizations) form the basis for system architecture models in SysML. Blocks map to architecture viewpoint elements; connectors to architecture relationships.

- **SysML v2 / TextualNotation**: SysML v1.6 blocks use graphical notation; SysML v2 introduces textual syntax for block definitions and properties with equivalent semantic meaning.

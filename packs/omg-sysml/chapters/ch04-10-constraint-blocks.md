# Chapter 4: 10 Constraint Blocks

## Core Idea
Constraint blocks integrate engineering analysis (performance, reliability, mathematical models) into SysML by packaging reusable constraints that bind to and constrain system properties. They enable formal specification of physical laws, trade-off analysis, and nested mathematical relationships within a model-based systems engineering lifecycle.

## Frameworks Introduced
- **«constraint» stereotype (on Block)**: Marks a block as a constraint block—a reusable package of one or more constraint parameters and mathematical expressions that constrain properties of other blocks.
  - When to use: Defining domain-specific or general-purpose constraint libraries (e.g., Newton's Laws F=m*a, thermal models, reliability equations) for reuse across multiple system contexts.

- **ConstraintProperty**: A property typed by a ConstraintBlock, localized to its containing context; holds a usage of the constraint block and binds its parameters to properties in the surrounding block.
  - When to use: Applying a constraint block to a specific system instance or assembly—each constraint property establishes one constraint instance with its own bindings.

- **ParametricDiagram**: A restricted form of internal block diagram showing only constraint properties and the value properties they constrain, along with binding connectors that bind constraint parameters to system properties.
  - When to use: Visualizing how constraints bind to system properties (mass, velocity, time, response time, displacement) and interact through shared parameters; supports trade-off analysis and objective functions.

- **Binding Connector**: Connects a constraint parameter to a system property, establishing the relationship that "this constraint parameter takes its value from that property."
  - When to use: Wiring constraint parameters to specific, possibly nested properties of the block containing the constraint instance.

## Key Concepts
- **Constraint parameters**: Properties of a constraint block that hold values (inputs and outputs) for the constraint equations; all properties of a constraint block are constraint parameters except those holding nested constraint properties.
- **Nested property reference (pathname dot notation)**: A notation (e.g., `vehicle.power_system.engine.displacement`) that allows constraints to reference properties deeply nested within a block hierarchy, accessed from the outer containing level.
- **Non-causal constraints**: Constraint blocks do not specify dependent or independent variables; the computational engine, initial conditions, and solver determine which variables are inputs and which are outputs.
- **Constraint nesting**: Constraints can be composed hierarchically; a constraint block can contain constraint properties that hold usages of other constraint blocks, enabling complex mathematical relationships built from simpler primitive operators.
- **Time properties**: Time can be modeled as a property (local clock, global clock, derived discrete time) that other properties may depend on; delays and skew can be introduced to express temporal relationships.
- **State-conditional constraints**: When system state (e.g., phase of water: liquid, solid, gas) determines which set of constraint equations apply, constraints can be conditioned on state property values.
- **Objective functions**: Constraint blocks can define objective functions to compare alternative solutions—constraining measures of effectiveness, utility-weighted criteria (performance, cost, physical characteristics), and probability distributions for trade-off analysis.

## Mental Models
- **Model constraints, not computations**: Constraint blocks express relationships between properties (what must be true), not algorithms (how to compute). The solver determines causality and execution order.
- **Use pathname notation for system-level constraints**: When a constraint must reference a deeply nested property (e.g., engine displacement within a vehicle power system), use dot notation from the outer block context to maintain proper namespace and avoid duplication.
- **Separate constraint definitions from constraint usages**: Define reusable constraint blocks on block definition diagrams with the «constraint» keyword; apply them on parametric diagrams as constraint properties with binding connectors, keeping the definition generic and the usage context-specific.
- **Compose complex constraints from simpler blocks**: Rather than embedding a single enormous constraint, nest simpler constraint blocks hierarchically (e.g., accelerometer output as a constraint on motion laws, which themselves constrain velocity and displacement).

## Anti-patterns
- **Embedding behavioral or structural elements in constraint blocks**: Constraint blocks shall contain only properties (constraint parameters), constraint properties (for nested usages), binding connectors, constraint expressions, and general model management elements—no methods, states, transitions, or use cases.
- **Using composite aggregation incorrectly**: Every property of a block that is typed by a ConstraintBlock must have composite aggregation. Omitting composite breaks the constraint instantiation semantics.
- **Misinterpreting constraint causality**: Assuming that constraint parameters have fixed input/output roles (e.g., F is always "computed from" m and a) is incorrect. Non-causality means the solver may treat any variable as an output; the computational engine and initial conditions determine causality.
- **Binding properties that are not reachable in the containing context**: Parametric diagrams restrict connectors to binding connectors only, and all properties shown must either bind directly to a constraint parameter or be contained within a property that does. Properties not on this binding path break the parametric diagram semantics.

## Key Takeaways
1. **Use constraint blocks for reusable analysis models**: Package mathematical and logical expressions (physics laws, performance equations, reliability models) as constraint blocks so they can be instantiated in multiple system contexts without duplication.
2. **Parametric diagrams are the execution surface for constraints**: Show constraint properties with binding connectors on parametric diagrams; they define the namespace and wiring that makes constraints executable.
3. **Nested properties reduce hierarchy copying**: Pathname dot notation allows a constraint at the system level to reference properties buried in sub-assemblies (e.g., vehicle.power_system.engine.displacement), avoiding redundant property copies.
4. **Non-causality enables multi-directional solving**: Because constraints do not specify which variables are inputs or outputs, a solver can compute any variable given sufficient information and initial conditions—use this for trade-off analysis and what-if scenarios.
5. **Constraint nesting builds composability**: Constraints can contain other constraint blocks, allowing complex relationships to be built from simpler primitives (e.g., composite acceleration constraint built from velocity and displacement constraints).
6. **Time and state make constraints dynamic**: Model time as a property and condition constraint equations on system state; this allows time-dependent and state-dependent analyses (e.g., switching constraint sets when water freezes) within a single parametric model.
7. **Objective functions enable design optimization**: Use constraints to define objective functions and measures of effectiveness, optionally with probability distributions, to support trade-off analysis and selection among alternative solutions.

## Connects To
- **UML Class, Property, and Compartment**: Constraint blocks extend UML Block with the «constraint» stereotype; constraint parameters are UML Properties; the parameters compartment is a special UML compartment extension.
- **SysML Blocks (Clause 9)**: ConstraintBlock generalizes Block; constraint properties are instances of blocks that are constraint blocks. All block structuring rules apply.
- **SysML Internal Block Diagram (Clause 8)**: Parametric diagrams are restricted internal block diagrams; they inherit the connector notation and internal property visualization but restrict connectors to binding connectors only.
- **SysML Binding Connectors (Clause 8.2.3.3)**: Binding connectors specifically connect constraint parameters to properties; they are the mechanism by which constraint parameters acquire their values in context.
- **ISO/IEC/IEEE 42010 (Architecture Description)**: Constraint blocks support the definition of architecture viewpoints and models that formalize relationships between system properties; they enable analytical description of quality attributes and constraints.
- **SysML Requirements (Clause 11) and Trade Study Extensions (Annex E)**: Constraint blocks with objective functions and probability distributions support requirements verification and trade-off analysis for design decisions; objective functions can be linked to requirements metrics.
- **Mathematical Expression Languages (external)**: SysML does not specify a computer-interpretable language for constraints; implementations typically use OCL, MathML, Python, MATLAB, or domain-specific expression languages provided by the modeling tool.

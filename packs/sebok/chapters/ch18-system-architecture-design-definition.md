# Chapter 18: System Architecture Design Definition

## Core Idea
System architecture design definition is the process of developing logical and physical architecture models that translate system requirements into a structured representation of how a system should operate and be implemented, providing a framework to verify requirements satisfaction across all operational scenarios.

## Frameworks Introduced
- **Logical Architecture Model Development**: Elaborates models and views of system functionality and behavior (logical operation) through functional, behavioral, and temporal architecture views independent of implementation decisions.
  - When to use: Early lifecycle stages to define *what* the system must do and *how* it behaves operationally before committing to physical solutions.
  
- **Physical Architecture Model Development**: Elaborates models of concrete physical elements (hardware, software, humans, processes) that realize the logical architecture and satisfy system requirements.
  - When to use: After logical architecture is baselined to translate abstract functions into implementable system elements, considering non-functional requirements and design properties.

- **Functional Architecture Model**: A set of functions and sub-functions defining transformations (inputs → outputs via data, materials, energy) that the system must perform to complete its mission.
  - When to use: Decomposing system mission into hierarchical levels of abstraction; identifies leaf-functions where physical solutions are feasible.

- **Behavioral Architecture Model**: Arrangement of functions, interfaces, and execution sequencing that defines control flows, data flows, operational modes, mode transitions, and performance levels necessary to satisfy requirements.
  - When to use: Capturing dynamic operation, state sequences, and scenario execution; represented via Functional Flow Block Diagrams (FFBD), activity diagrams, or state-transition diagrams.

- **Temporal Architecture Model**: Classification of functions by execution frequency (synchronous cyclic vs. asynchronous event-driven) and decisional hierarchy.
  - When to use: Real-time and command-control systems requiring separation of fast/slow loops and exception handling; establishes priority levels for processing.

## Key Concepts
- **Function**: An action transforming inputs and generating outputs (data, materials, energy); modeled as y = f(x, t) where t represents time; organized hierarchically from mission (F0) down to leaf-functions.

- **Input-Output Flow**: Flow items (data, material, energy) exchanged between functions; integral to defining function completeness alongside inputs and outputs.

- **Control Flow (Trigger)**: Signal or event (switch, alarm, temperature change, key press) that activates or deactivates a function; enables conditional execution.

- **Scenario of Functions**: Chain of functions performed sequentially and synchronized by control flows to achieve a global input-to-output transformation; expresses dynamic behavior of a higher-level function.

- **Operational Mode**: Abstraction of function state (active/inactive) and transitions between modes triggered by control flows; viewed as a scenario of mode sequences rather than function transformations.

- **Design Property**: Quantitative or qualitative property (reliability, availability, maintainability, modularity, robustness) obtained through allocation of non-functional requirements, analysis, simulation, or definition of existing elements; relates to or equals a requirement if compliant.

- **System Element**: Discrete part (hardware, software, data, human, process, procedure, facility, material) that can be implemented to fulfill design properties; assembled into layers with ~5±2 elements per level.

- **Allocation**: Assignment of logical architecture functions to physical system elements using criteria deduced from design properties and system requirements; creates traceability and identifies derived requirements.

- **Partitioning**: Decomposition, gathering, or separation of functions to facilitate identification of feasible system elements; uses affinity criteria (similar transformation, same technology, same input-output type, frequency level, dependability, environment resistance).

## Mental Models
- **Logical then Physical**: Design logical architecture *first* (independent of implementation), then physical architecture (grounded in concrete elements). Skipping logical architecture risks reinventing functions with domain-dependent performance assumptions.
- **Functions + Flows Together**: Always define inputs, outputs, and controls *alongside* functions; inputs and outputs are integral, not afterthoughts—missing them leads to incomplete definitions.
- **Scenarios Before Decomposition**: Establish behavioral scenarios and execution sequences before decomposing the static function tree; static decomposition alone is insufficient for understanding dynamic operation.
- **Temporal Hierarchy**: Separate synchronous (cyclic) and asynchronous (event-driven) aspects into distinct execution-frequency levels for real-time systems; prevents high-frequency disturbances from disrupting low-frequency mission objectives.

## Anti-patterns
- **Problem Irrelevance**: Logical architecture model disconnected from operational scenarios produced by mission analysis; loses grounding in real stakeholder concerns.

- **Insufficient Architectural Requirements**: Major architectural inputs (system requirements) fail to specify correct abstraction level, causing architects to invent solutions rather than deriving them from requirements.

- **Decomposition Too Deep**: Over-decomposing functions or overcrowding scenarios with too many functions and flows in a single system block; complicates navigation and management.

- **Inputs and Outputs Forgotten**: Focusing only on functions and decomposition while ignoring inputs, outputs, or considering them too late; treats inputs/outputs as separate rather than integral to function definition.

- **Static Decomposition Only**: Treating static functional hierarchy as the architecture; fails to capture sequences, state transitions, and how functions actually operate together dynamically.

- **Mixed Governance, Management, Operations**: Conflating strategic monitoring (governance), tactical monitoring (management), and basic operations in a single logical architecture; should be separated via behavioral and temporal models.

- **Direct Technology Allocation**: Jumping directly from high-level abstract requirements to low-level hardware or software without intermediate logical and physical architecture levels; loses system comprehension and multidisciplinary context.

- **No Logical Architecture (Repeating Systems)**: Bypassing logical architecture for "known" repeated products because functions are already understood; ignores that function performance is domain-dependent—if domain set changes, performance validity breaks.

## Key Takeaways
1. **Separate abstraction levels**: Logical architecture is implementation-independent; physical architecture grounds functions in concrete elements and design properties. Use both iteratively, not just logical alone.

2. **Define complete functions**: Every function requires specified inputs, outputs, and control flows. Missing any element leaves the architecture incomplete and unmappable to implementation.

3. **Scenarios drive behavior**: Establish dynamic scenarios and mode transitions *before* static decomposition; behavioral and temporal models are as essential as functional ones for capturing how the system actually operates.

4. **Allocate with criteria**: Partition functions to system elements using explicit affinity criteria (technology compatibility, frequency level, interface types, dependability, environment). Avoid ad hoc allocation.

5. **Verify across all scenarios**: Use traceability matrices and (where possible) executable models and simulation to verify that the selected architecture satisfies requirements in all operational scenarios and modes.

6. **Design properties drive selection**: Non-functional requirements (performance, safety, security, maintainability) often constrain the physical architecture more strongly than functional requirements; multiple physical implementations may satisfy one function.

7. **Continuous feedback**: Logical architecture refinement continues after physical architecture development; derived elements and requirements induced by physical solutions feed back to update both architectures and requirements baselines.

## Connects To
- **ISO/IEC/IEEE 15288 (System Life Cycle Processes)**: System Architecture Design Definition is a core process activity in requirements analysis → architecture → design → implementation lifecycle; traceability obligations derive from 15288.
- **ISO/IEC/IEEE 42010 (Architecture Description)**: Views, viewpoints, and concern-driven architecture models provide practical templates and notations for capturing architectural elements and their relationships.
- **SADT/IDEF0, FAST, eFFBD**: Functional modeling techniques for creating hierarchical function decompositions and flow diagrams; executable variants enable simulation and validation.
- **SysML (OMG Specification)**: Block definition diagrams (BDD), internal block diagrams (IBD), activity diagrams, and state-machine diagrams provide modern notations for functional, behavioral, and temporal architecture views.
- **System Analysis**: Trade studies, cost analysis, technical risk analysis, and effectiveness analysis evaluate candidate architectures against assessment criteria before final selection.
- **Decision Management**: Formal process for selecting among candidate architectures; traces decisions and rationale to architecture choices.

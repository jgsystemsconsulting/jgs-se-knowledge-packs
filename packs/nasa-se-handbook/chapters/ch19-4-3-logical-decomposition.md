# Chapter 19: 4.3 Logical Decomposition

## Core Idea
Logical Decomposition recursively breaks down stakeholder needs and system functions into increasingly refined architectural and functional models until all requirements are understood, viable, verifiable, and internally consistent—forming the basis for detailed design work.

## Frameworks Introduced
- **Logical Decomposition Process**: Recursive, iterative refinement of system architecture and requirements through functional and structural analysis, continuing until all levels of the system are fully defined and baselined.
  - When to use: When translating high-level stakeholder needs into a coherent system architecture and partitioned requirements ready for design decisions.

- **Product Breakdown Structure (PBS)**: Hierarchical breakdown of products (hardware, software, information items) carried to the lowest level where a cognizant engineer or manager exists.
  - When to use: During functional analysis and architecture definition to represent the "what" will be delivered.

- **Work Breakdown Structure (WBS)**: Hierarchical breakdown of work (not products) necessary to complete the project; contains the PBS.
  - When to use: Project planning and resource allocation; the PBS sits within the WBS.

- **DOD Architecture Framework (DODAF)**: A framework defining operational, systems, and technical-standards views with associated products (operational nodes, systems interconnectivity, standards dictionaries) to characterize complex systems-of-systems.
  - When to use: For complex, evolving systems where interoperability, stakeholder alignment, and strategic investment decisions are critical; NASA may adopt selective concepts and formalisms from DODAF for technical requirements and decision analysis.

## Key Concepts
- **System Architecture**: The structure of components, their relationships, and the principles and guidelines governing their design and evolution over time.

- **Functional Analysis Techniques**: Structured methods to decompose and understand system functions, including Functional Flow Block Diagrams (FFBDs) for task sequences, N² diagrams for interface/interaction matrices, and Timeline Analyses for time-critical function sequencing.

- **Derived Technical Requirements**: Requirements that arise from architectural definition and partitioning, not explicitly stated in baselined stakeholder requirements; must be allocated to the architecture and functions alongside baselined requirements.

- **Logical Decomposition Models**: Models defining relationships among requirements, functions, and behaviors; include system architecture models and the basis for partitioning requirements to a level where design work can proceed.

- **Recursive and Iterative Process**: Decomposition continues until all desired architectural levels have been analyzed, defined, and baselined; engineers must remain willing to revise earlier architectural decisions as the system becomes better understood.

- **Verification and Viability**: A core check before baselinesealing: all requirements must be known to be viable (achievable with available technology and resources), verifiable (observable/testable), and internally consistent with each other.

- **Alternative Decomposition Paths**: Multiple valid ways to decompose the same functions often exist (e.g., communications via RF, laser, or Internet); the outcome depends on engineer creativity, skills, and experience.

## Mental Models
- **Use iterative refinement when decomposing**: Early architectural decisions must be held lightly; as the system is better understood, revisit and revise earlier choices and cascade those changes through lower-level decompositions again.

- **Think of PBS and WBS as complementary perspectives**: PBS represents the hierarchical product structure, while WBS represents the hierarchical work structure; PBS sits within WBS to organize both products and work at each level.

- **Treat architecture frameworks (DODAF, SysML) as lenses for complex systems**: When interoperability, stakeholder clarity, and strategic decisions are at stake, architecture frameworks provide systematic ways to describe and compare alternative solutions.

- **Remember: cost to change design direction rises steeply**: Logical decomposition must resolve architecture questions early, before those hard-to-undo decisions are locked in; iterative assessment of alternatives is essential to avoid costly rework downstream.

## Key Takeaways
1. **Decomposition is recursive until complete**: Continue breaking down requirements and functions across all desired architectural levels; only baseline the system architecture and requirements when all are understood to be viable, verifiable, and internally consistent.

2. **Multiple valid decomposition paths exist**: Engineers must explore a range of alternatives (functional allocations, technology options, architectural strategies) before committing to a single path; stay objective and do not become emotionally attached to one design early.

3. **Capture work products, decisions, and rationale**: Document not just the logical models and derived requirements, but also key decisions, decision rationale, assumptions, and lessons learned during decomposition.

4. **Align architecture with stakeholder expectations and ConOps**: The three products—strawman architecture/design, ConOps, and derived requirements—must be consistent with each other and with programmatic constraints (cost, schedule); iterative alignment is essential.

5. **Functional analysis techniques provide structure**: Use FFBDs, N² diagrams, and Timeline Analyses to systematically depict task sequences, interfaces, and time-critical behaviors; these techniques make decomposition more disciplined and traceable.

6. **Baseline only when all uncertainty is resolved**: Premature baselinesealing of architecture and requirements before alternatives have been thoroughly understood and trade-offs assessed leads to costly change and rework; resist pressure to baseline too early.

## Connects To
- **Design Solution Definition Process (Section 4.4)**: Logical Decomposition outputs (logical models and derived requirements) feed directly into Design Solution Definition, where they are translated into alternative design solutions and trade-studied to reach a preferred design.

- **ISO/IEC/IEEE 15288 (System and Software Engineering — System Lifecycle Processes)**: Logical Decomposition aligns with the Requirements Definition and Requirements Analysis processes in 15288, ensuring traceability and consistency across the system lifecycle.

- **Technical Requirements Definition Process**: Logical Decomposition refines and partitions the technical requirements output by Technical Requirements Definition, cascading them through the architecture.

- **Decision Analysis Process**: Trade studies and the systematic comparison of alternatives during Logical Decomposition rely on decision analysis techniques to assess cost-effectiveness, risk, technical achievability, and performance trade-offs.

- **SysML and Architecture Description Languages**: Logical Decomposition models can be captured using SysML block diagrams, functional hierarchies, and parametric constraints, providing a formal foundation for architecture and requirements traceability.

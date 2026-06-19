# Chapter 13: Life Cycle Model Selection and Adaptation

## Core Idea
Every project is unique and demands thoughtful adaptation of both the life cycle model and development approach to its specific circumstances, constraints, and quality drivers; successful adaptation is led by experienced systems engineers in close consultation with domain experts.

## Frameworks Introduced
- **ISO/IEC/IEEE 24748-1** (Guidelines for Life Cycle Management): The normative reference for structured lifecycle management principles and process adaptation criteria
  - When to use: When establishing organization-wide lifecycle governance or tailoring processes for projects with diverse domain characteristics
- **Hump Diagram Principle** (Generic Relationships between Life Cycle Stages and Processes): A visual model showing that process activities peak at particular lifecycle stages but remain active across the entire lifecycle with varying intensity
  - When to use: When planning resource allocation and identifying forward-looking dependencies (e.g., ensuring verification resources are available before deployment)

## Key Concepts
- **Development Approach Adaptation**: Modification of methods, practices, and workflows to match project-specific circumstances, driven by technology maturity, domain diversity, cost-benefit tradeoffs, or organizational make-or-buy decisions
- **Domain-Specific Development**: Different system elements within a larger system may employ distinct development approaches (e.g., software-intensive vs. purely mechanical), requiring carefully timed alignment checkpoints to prevent interface inconsistencies
- **Synchronization Interval**: The time window between development cycle completion for different system elements; must be balanced—too short defeats the purpose, too long invites uncoordinated design decisions
- **Quality Characteristic Dominance**: Particular quality drivers (e.g., stealth in military systems, safety and security in healthcare) necessitate refinement of the entire development process, not just isolated components
- **Through-Life Process Activity**: Recognition that technical and management processes are active across all lifecycle stages, not compartmentalized to particular phases; this underpins resource planning and holistic systems thinking
- **Concurrency**: Parallel execution of processes that do not strongly depend on one another's outputs (e.g., risk management and measurement)
- **Iteration**: Repeated application of processes to accommodate stakeholder feedback, evolving requirements, architectural constraints, and design tradeoffs
- **Recursion**: Application of technical and management processes at each hierarchical level of system decomposition; outputs from one level serve as inputs for lower levels

## Mental Models
- **Use the "experienced systems engineer" lens**: Adaptation decisions require seasoned judgment informed by both technical domain knowledge and stakeholder concerns—involve those responsible for individual system elements to ensure buy-in and capture distributed expertise.
- **Think of lifecycle processes as a "hump diagram" activity profile**: Each process has peak intensity at particular stages but remains live throughout; forward-looking resource allocation ensures future activities have required inputs and prerequisites in place.
- **Adopt "middle-out" solution synthesis**: Most practical real-world problems benefit from combining top-down problem definition (driven by needs and constraints) with bottom-up reuse and evolution (driven by what already exists), rather than pure top-down or bottom-up approaches.

## Anti-patterns
- **Overly frequent synchronization intervals**: Requiring too-short alignment cycles between heterogeneous domain teams (e.g., two-week software releases forced against slower hardware development) adds overhead without meaningful coordination benefit.
- **Delayed synchronization intervals**: Allowing team checkpoints to stretch too long risks uncoordinated design decisions and incompatible interface assumptions that are difficult and expensive to resolve later.
- **Ignoring domain-specific quality drivers**: Failing to refine the development process to account for dominant quality characteristics (safety, security, stealth, etc.) undermines the very properties the system must deliver.
- **Treating processes as strictly sequential**: Assuming processes execute only within their designated lifecycle stage, missing critical through-life dependencies, forward planning, and feedback loops that ensure holistic system consistency.

## Key Takeaways
1. **Project adaptation is the rule, not the exception**: Since every project is unique in technology, domain composition, and business strategy, both the lifecycle model and development approach must be consciously tailored—don't apply a one-size-fits-all template.
2. **Multi-domain systems require explicit synchronization governance**: When different system elements use different development approaches (hardware vs. software, mechanical vs. electrical), establish regular but appropriately spaced alignment checkpoints to prevent interface drift.
3. **Quality drivers reshape the entire development process**: Dominant quality characteristics (stealth, safety, security, reliability) are not add-ons; they drive fundamental refinements to how the system is developed, integrated, and validated.
4. **Processes operate concurrently, iteratively, and recursively**: Lifecycle processes are not sequential boxes but overlapping, mutually informing activities across the entire lifecycle and at all system decomposition levels; plan resources and dependencies with this non-linear reality in mind.
5. **Experienced systems engineers lead adaptation with stakeholder involvement**: Adaptation decisions are judgment calls informed by technical expertise and organizational learning; involve domain leads and stakeholders to ensure adaptation is both feasible and accepted.
6. **Solution synthesis blends top-down and bottom-up thinking**: Start with stakeholder needs and problem constraints (top-down), but incorporate reusable and existing capabilities and learn from field experience (bottom-up); this "middle-out" approach balances innovation with pragmatism.
7. **Forward planning through the hump diagram**: Recognize that every process remains active across the lifecycle, with varying intensity; use the hump diagram model to identify forward-looking dependencies and ensure resources, tools, and prerequisites for future phases are in place during current phases.

## Connects To
- **ISO/IEC/IEEE 24748-1 and 24748-2** (Life Cycle Management): Normative standards for lifecycle process selection, tailoring, and governance
- **ISO/IEC/IEEE 15288** (System Life Cycle Processes): The foundational process standard referenced throughout; defines the process inventory to which adaptation and tailoring decisions apply
- **System Definition and System Realization Knowledge Areas**: Cover the detailed processes (concept definition, system definition, system realization) that require adaptation at each project and domain level
- **Requirements Management and Architecture Definition**: Key lifecycle activities that iterate with one another during system definition and are sensitive to domain-specific adaptation choices
- **Systems Approach**: Provides the foundational thinking (concurrency, iteration, recursion, decomposition) that underpins lifecycle adaptation and through-life process consistency

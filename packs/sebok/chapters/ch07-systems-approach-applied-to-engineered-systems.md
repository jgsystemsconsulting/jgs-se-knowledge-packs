# Chapter 7: Systems Approach Applied to Engineered Systems

## Core Idea
The systems approach is applied to an **engineered system context** (product, service, enterprise, or system of systems), not to isolated systems in isolation. Practitioners must understand the relationships between systems at multiple scopes—narrower, wider, and environmental—to realize stakeholder needs holistically within a lifecycle framework.

## Frameworks Introduced

**The Systems Approach Synthesis for SEBoK** consists of six sequential activities:
- Identify and understand relationships between problems and opportunities in a real-world situation
- Gain thorough understanding of the problem or opportunity within its wider system and environment context
- Synthesize viable system solutions to the selected problem
- Analyze and choose between alternative solutions (considering time, cost, and quality trade-offs)
- Provide evidence that a solution has been correctly implemented and integrated
- Deploy, sustain, and apply a solution to help solve the problem
- When to use: Any engineered systems engineering effort; all activities operate within a lifecycle framework that may require concurrent, recursive, and iterative execution.

**Open System Relationships Model** (from Flood & Carson 1993): Defines four boundary layers—
- Narrower System-of-Interest (NSoI): the system of direct concern; scope of authority/control
- Wider System-of-Interest (WSoI): logical boundary containing all elements needed to understand behavior
- Immediate Environment: engineered, natural, and/or social systems that exchange material, information, energy with WSoI
- Wider Environment: systems with no direct WSoI interaction but influencing decisions over the lifecycle
- **Extension**: Meta-system (MS) exercising direct control over the WSoI (Flood 1987)
- When to use: Defining system boundaries and scope for engineering activities; deciding what can be changed vs. what must remain fixed.

**Four Engineered System Contexts** (primary classification scheme):
1. **Product System Context**: SoI is the product itself; WSoI is product hierarchy, service, or enterprise using it.
2. **Service System Context**: SoI is the service system (technology, infrastructure, people, resources enabling service); value realized through service transactions where end-user co-creates value at request time.
3. **Enterprise System Context**: SoI is the enterprise system; WSoI is business environment. Enterprise includes people, knowledge, processes, policies, facilities, intellectual property—not just organizations.
4. **System of Systems (SoS) Capability Context**: Multiple cooperating systems, each with own objectives and ownership, contributing to shared goal; loose coupling; late binding; systems may move in/out of context dynamically.
- When to use: Classifying the scope and life-cycle strategy for engineering activities; choosing which systems to engineer vs. which to adapt or integrate.

## Key Concepts

- **Engineered System**: A system created by humans to satisfy stakeholder needs; requires systems thinking and managed technical activities across a lifecycle.

- **System-of-Interest (SoI)**: The system (or set of systems) that is the focus of engineering effort; boundary is chosen based on what can be changed and what must remain fixed.

- **System Context**: An organized set of relationships capturing the SoI, the systems with which it directly works, and relevant environmental and meta-system influences; enables both reductionist focus and holistic understanding.

- **Problem-Opportunity Situation**: The real-world condition requiring engineering attention; understood not in isolation but within its wider system, environment, and purpose-driven lifecycle.

- **Service**: Activities that cause transformation of state (person, product, business, region) by mutually agreed terms between provider and customer.

- **Enterprise**: Includes organizations, people, knowledge, processes, principles, policies, practices, doctrines, theories, beliefs, facilities, land, and intellectual property that together enable outcomes.

- **Stakeholder Needs**: Requirements and objectives of all parties impacted by or involved in the engineered system; must be captured across the system context.

- **Lifecycle Framework**: The temporal and process structure within which systems approach activities occur; may require concurrent, recursive, or iterative execution of any or all activities.

## Mental Models

- **Use Nested Scopes (NSoI / WSoI / Environment / Meta-system)** when you need to understand what decisions are within your control, which relationships must be managed, and which external forces constrain your options.

- **Think of Systems Approach as Context-First**: Before proposing a solution, establish the full system context and stakeholder landscape. The traditional product-focused SE approach tends to start narrow; the systems approach starts wide and contracts only as necessary.

- **Apply Reductionist + Holistic Simultaneously**: The system context allows you to focus narrowly on the SoI (reductionist) while maintaining awareness of consequences at the enterprise and environmental levels (holistic).

## Anti-patterns

- **Treating SE as product-only engineering**: Many organizations apply SE only to individual products without considering the service system, enterprise system, or SoS context in which the product operates. This leads to misaligned requirements and surprises in deployment.

- **Fixing the SoI boundary too early**: Choosing NSoI vs. WSoI boundary before understanding the problem fully can lock you into a solution space that doesn't address the real stakeholder needs or fails to account for critical system interactions.

- **Ignoring the enterprise and meta-system layers**: Particularly in service and enterprise contexts, failing to account for organizational constraints, policies, and external regulatory or business environment forces leads to technically sound but operationally non-viable solutions.

## Key Takeaways

1. **The systems approach applies to a context, not a single system.** Always define and agree on the SoI boundary, the wider system that contains it, the immediate environment with which it directly interacts, and any meta-system authority or constraints.

2. **Four distinct engineered system contexts exist:** product, service, enterprise, and SoS. Each has different implications for requirements capture, solution synthesis, and validation. Choose your context carefully; it drives lifecycle strategy.

3. **The Six-Step Synthesis frames all systems work**: understand relationships → understand problem in context → synthesize solutions → choose trade-offs → validate implementation → deploy/sustain. All steps operate within a lifecycle that may iterate and recurse.

4. **Enterprise systems are uniquely dynamic.** Unlike product and service systems, enterprises constantly evolve, have ill-defined and changing goals, rarely have fully configuration-controlled requirements, and exist in unstable environments. Engineering must account for this volatility.

5. **Service value is co-created at transaction time.** Service systems differ fundamentally from product systems in that the end-user participates in value realization. All necessary technology, infrastructure, people, and resources must be orchestrated to enable that moment.

6. **All three system contexts are interdependent.** Products are created by enterprises and used in services. Services are delivered by enterprises using products. Enterprises provide both. Systems engineering must account for these nested relationships.

## Connects To

- **ISO/IEC/IEEE 15288 (Systems and Software Engineering – System and Software Life Cycle Processes)**: The systems approach synthesis activities align with lifecycle process groups (planning, design, implementation, validation, transition); system context definitions support requirements engineering and stakeholder management across all domains.

- **Systems Thinking (Checkland, Senge)**: The systems approach operationalizes systems thinking concepts through structured activities; open system relationships provide a concrete framework for the "holistic view of system behavior" that thinking disciplines advocate.

- **SoS Engineering**: System of Systems contexts are a specialized application of the systems approach; the open relationships model and late-binding concepts support SoS independence, evolution, and emergence.

- **Service Systems Engineering**: The service system context and co-creation principle distinguish service-dominant logic from product-focused traditional SE; service systems demand broader problem exploration and lifecycle thinking.

- **Enterprise Architecture (ArchiMate, TOGAF reference)**: The enterprise system context and meta-system concept align with enterprise-level viewpoints; the systems approach provides a lifecycle methodology to operationalize enterprise architectural decisions.

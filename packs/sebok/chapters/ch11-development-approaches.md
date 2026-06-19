# Chapter 11: Development Approaches

## Core Idea
Development approaches—incremental, evolutionary, agile, and lean—define how systems are built over time when facing uncertainty, changing requirements, or evolving markets. Each approach trades off planning rigor for flexibility, with profound implications for risk management, stakeholder feedback, and delivery speed.

## Frameworks Introduced

- **Boehm's Incremental Commitment Spiral Model (ICSM)**: A modern incremental approach combining plan-driven rigor with iterative flexibility, centered on periodic commitment reviews where stakeholders decide whether to proceed to the next increment based on evidence gathered.
  - When to use: Defense, transportation, and critical infrastructure projects requiring formal reviews, traceability, and accountability across high-risk systems.

- **DevOps / Continuous Integration & Deployment (CI/CD)**: An evolutionary approach blending development and operations through automated pipelines, enabling rapid, frequent releases of system updates based on real-time feedback.
  - When to use: Cloud services, IoT systems, and large-scale software platforms where conditions change rapidly and innovation must be fast.

- **Scrum**: A widely used agile framework structuring work into time-boxed sprints (2–4 weeks) with defined roles (Product Owner, Scrum Master, Development Team) and ceremonies (stand-ups, planning, reviews, retrospectives).
  - When to use: Software-heavy projects with evolving requirements and close stakeholder feedback loops.

- **Scaled Agile Framework (SAFe)**: An enterprise agile framework extending Scrum principles across multiple teams and departments via Program Increment (PI) Planning, blending Agile, Lean, and systems thinking.
  - When to use: Large organizations needing to align multiple agile teams around shared strategic goals.

- **Large-Scale Scrum (LeSS)**: A lightweight alternative to SAFe extending Scrum to multiple teams working on the same product, emphasizing simplicity and team autonomy over adding management layers.
  - When to use: Smaller-to-medium enterprises seeking agile scalability without heavy governance overhead.

- **Lean Enablers for Systems Engineering (LEfSE)**: A collection of practices formulated as "dos and don'ts" anchored to six lean principles, designed to improve program value and reduce waste without replacing traditional SE.
  - When to use: Any SE program aiming to eliminate waste while maintaining mission assurance and SE discipline.

- **Agile Systems Engineering (Eight Core Aspects)**: A principle-based method for designing, building, sustaining, and evolving systems under uncertain knowledge and dynamic environments. Core aspects: adaptable modular architecture, iterative incremental development, attentive situational awareness, attentive decision making, common-mission teaming, shared-knowledge management, continual integration & test, and being agile.
  - When to use: Complex, multi-disciplinary systems where knowledge is uncertain or operational conditions are fluid; agility is a state of being, not a process.

- **Industrial DevOps (IDO)**: Extends Lean, Agile, and DevOps principles to cyber-physical systems throughout their full lifecycle, integrating digital engineering (digital twins), test automation, CI/CD, and infrastructure-as-code.
  - When to use: Industrial, aerospace, defense, or mission-critical cyber-physical systems requiring fast delivery, hardware/software integration, and continuous operational improvement.

## Key Concepts

- **Increment**: A tangible, deliverable portion of system capability produced at the end of an iteration; provides early stakeholder feedback and verification opportunities before the full system is complete.

- **Learning iteration**: A cycle that focuses on exploration (modeling, simulation, proof-of-concept) rather than producing a deliverable, serving to reduce technical uncertainty and guide future design decisions.

- **Adaptive planning**: A planning approach that adjusts long-term goals based on empirical data and learning cycles; enables response to change without abandoning structure.

- **Traceability in iterative contexts**: Version control and clear documentation of requirements, design, and assumptions across iterations to prevent confusion and rework when specifications evolve.

- **Configuration management**: Formal tracking of system versions, baselines, and changes across iterations; becomes more critical in incremental and evolutionary approaches where interfaces and requirements shift frequently.

- **Stakeholder commitment reviews**: Formal decision gates (as in ICSM) where evidence gathered in each cycle justifies moving forward, pivoting, or stopping—reducing risk of pursuing infeasible paths.

- **Modular architecture**: System design composed of loosely coupled, reusable components with well-defined interfaces, enabling rapid extension, modification, and adaptation across iterations without major rework.

- **Continuous integration**: Frequent (ideally automated) merging and testing of work from multiple disciplines to reveal integration issues early; essential in iterative and evolutionary approaches.

- **Value stream**: The end-to-end sequence of linked tasks, control nodes, and information flows necessary to deliver customer value; maps where waste (non-value-added activities) occurs.

- **Agility**: The capability to sense emergent risks and opportunities, respond decisively, and evolve systems in alignment with changing environments; a behavior and mindset, not a process.

## Mental Models

- **Use incremental or evolutionary approaches when uncertainty is high or requirements are evolving.** Sequential approaches assume knowledge is fixed upfront; iterative approaches embrace learning and adaptation as risk reduction.

- **Think of agility as "being" not "doing."** Many teams implement agile ceremonies (sprints, standups) without developing the underlying capability to sense change, make decisions quickly, and evolve systems—resulting in process without substance.

- **Use Lean thinking to eliminate waste while preserving mission assurance.** Lean SE is not "less SE"; it is rigorous SE with minimal waste, guided by the principle that any task legitimately required for success must be included, but executed efficiently.

- **Consider the modular architecture as the enabling constraint.** Iterative, evolutionary, and agile approaches depend critically on system design that permits rapid change without ripple effects; poor modularity forces either rework or abandonment of the approach.

## Anti-patterns

- **Committing too early to full system design in high-uncertainty projects.** Sequential approaches force stakeholders to lock in requirements and architecture before evidence is available, increasing the risk of pursuing infeasible paths and large-scale rework.

- **Treating agile as a silver bullet for all projects.** Agile principles originated in software and may not transfer seamlessly to complex, multi-disciplinary, safety-critical systems requiring formal reviews, long integration timelines, or hardware fabrication cycles.

- **Skipping traceability and configuration management in iterative projects.** The assumption that "agile means less documentation" leads to lost institutional memory, inability to assess impact of changes, and difficulty upgrading deployed systems.

- **Implementing agile ceremonies without developing decision-making speed.** Teams can hold daily standups, run 2-week sprints, and conduct retrospectives while remaining slow to sense problems, escalate decisions, or pivot direction—agility without effect.

- **Designing monolithic systems and expecting agile delivery.** Tight coupling between subsystems or components locks in integration dependencies, making it impossible to develop and test increments independently or to adapt quickly to change.

- **Confusing "frequently releasing code" with evolutionary development.** Continuous deployment without real user feedback loops, modular architecture, or integration discipline produces fragmentation and accumulated technical debt rather than true evolution.

## Key Takeaways

1. **Incremental approaches are essential for high-risk, high-uncertainty projects.** They reduce commitment and risk at each decision gate, align engineering effort with real-world learning, and support formal reviews required in defense and critical infrastructure.

2. **Evolutionary approaches succeed only with modular architecture, continuous integration, and strong feedback loops.** DevOps and CI/CD are not about "deploying faster"; they are about sensing and responding to operational reality.

3. **Agile is a principle-based capability, not a ceremony-based process.** The Agile Manifesto's four values—individuals over processes, working systems over documentation, collaboration over contracts, responding to change over plans—describe a behavior and mindset. Teams implementing Scrum or SAFe ceremonies without this capability are "doing agile," not "being agile."

4. **Lean thinking complements all iterative approaches.** The six lean principles—capture customer value, map and eliminate waste, flow work efficiently, pull by customer need, pursue process perfection, and respect people—are orthogonal to agile, incremental, and evolutionary methods; applying them amplifies delivery speed and reduces cost.

5. **Scalability requires more than framework adoption.** SAFe, LeSS, and other scaling frameworks introduce structure (PI Planning, synchronized cadences, scaled governance), but their effectiveness depends on the organization's maturity in modular architecture, cross-team communication, and decision speed.

6. **Traceability, configuration management, and version control are non-negotiable in evolving systems.** Without clear documentation of what changed, why, and what impact it had, teams cannot assess compatibility between increments, cannot upgrade deployed systems safely, and cannot maintain regulatory compliance.

7. **Choose the development approach to fit the life cycle model and risk profile, not the reverse.** Incremental and ICSM suit plan-driven governance and formal gate reviews; evolutionary approaches suit continuous deployment and real-time feedback; agile and lean suit uncertain or rapidly changing markets. Mismatch leads to process friction and poor outcomes.

## Connects To

- **ISO/IEC/IEEE 15288 (System Life Cycle Processes)**: Development approaches are concrete implementations of life cycle processes; SEBoK discusses how incremental, evolutionary, and agile approaches adapt traditional processes to handle uncertainty and change.

- **ISO/IEC/IEEE 24748-1 (Life Cycle Management Guidelines)**: Normative reference for distinguishing iterative development, agile, and incremental approaches in systems and software engineering lifecycle contexts.

- **ISO/IEC/IEEE 24748-10 (Systems Engineering Agility Guidelines)**: Emerging standard defining the eight core aspects of SE agility and how to operationalize agile SE across complex, multi-disciplinary systems.

- **ISO/IEC/IEEE 32675 (DevOps)**: Normative foundation for DevOps principles, practices, and principles guiding continuous integration, deployment, and operational feedback in system lifecycle.

- **Boehm's Spiral Model and ICSM**: Historical roots of incremental and iterative SE, providing the risk-management and commitment-review framework that underpins modern incremental approaches and ICSM.

- **The Agile Manifesto**: Foundational document for agile principles in software; SEBoK's treatment cautions that direct application to complex systems engineering requires adaptation and blending with traditional SE discipline.

- **Lean Thinking (Womack, 2003) and Lean Manufacturing**: Originating paradigm for lean SE; SEBoK discusses how six lean principles eliminate waste while preserving mission assurance across all lifecycle phases.

- **SAFe, Scrum, LeSS, and other agile scaling frameworks**: Practical implementations of agile principles at enterprise and multi-team scale; each trades off simplicity for governance structure differently.

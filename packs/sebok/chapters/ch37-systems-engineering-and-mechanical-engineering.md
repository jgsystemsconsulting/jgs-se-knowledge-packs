# Chapter 37: Loss-Driven Systems Engineering (LDSE)

## Core Idea

Loss-Driven Systems Engineering (LDSE) is a unified systems engineering approach that holistically integrates traditionally isolated specialty areas—safety, security, reliability, resilience, availability, and others—around a single overarching principle: addressing potential losses associated with systems. Rather than treating these domains in isolation, LDSE recognizes their shared concepts, requirements, and solutions and applies them collaboratively across the system lifecycle.

## Frameworks Introduced

- **Loss-Driven Systems Engineering (LDSE)**: An overarching systems engineering process that holistically addresses quality characteristics concerned with loss (system resilience, safety, security, and related attributes) by unifying specialty engineering areas that are typically treated in isolation.
  - When to use: When developing systems where multiple loss-driven concerns (safety, security, reliability, environmental impact, maintainability, availability) must coexist; to reduce redundant engineering effort and identify highly effective solutions that address multiple loss-driven objectives simultaneously.

- **Loss Control Design Principles** (Winstead 2021): A set of 19 coordinated design techniques for controlling loss in cyber-physical systems, including anomaly detection, defense-in-depth, redundancy, distributed privilege, and protective defaults.
  - When to use: During system architecture and design definition to ensure consistent loss mitigation across functional and non-functional requirements.

- **Integrated Product Teams (IPTs)**: Organizational structure and management discipline that mitigate "siloism" (unwillingness to share information across specialty teams) by encouraging collaborative information sharing among loss-driven specialists.
  - When to use: When loss-driven specialties operate in organizational silos; to ensure holistic consideration of adversities, weaknesses, assets, and coping mechanisms across all loss-driven domains.

## Key Concepts

- **Loss-Driven Specialty Areas**: The family of systems engineering domains that address potential losses—availability, environmental impact, maintainability, resilience, reliability, risk management, safety, security, and quality management. Each has its own definitions and scope, but all share commonality in protecting against loss.

- **Shared Loss Scenarios**: Risk situations that appear across multiple specialty areas (e.g., a component failure may affect both safety and security). LDSE leverages these overlaps to avoid redundant analysis.

- **Loss-Driven Attributes**: Five dimensions that define the scope of loss-driven specialty areas:
  - Types of assets considered
  - Types of loss addressed
  - Types of adversity addressed
  - Coping strategies employed
  - Aspects of the system and environment under consideration
  
  Different specialties have different scopes along these attributes; LDSE aggregates and aligns them.

- **Hazard Control**: The core principle that systems engineering must minimize hazards, control hazards that cannot be avoided, and ensure safe transitions between known acceptable states. Applies across safety, security, and resilience domains.

- **Loss Margins**: Designing systems to operate in a state space sufficiently distanced below the threshold at which loss occurs—a fundamental protective design principle.

- **Protective Failure**: The requirement that failure of any system element must neither result in unacceptable loss nor trigger another loss scenario.

- **Anomaly Detection**: Timely identification of salient anomalies in the system or its environment that enables effective response action—a foundational loss-control technique.

- **Defense-in-Depth**: Prevention or minimization of loss through multiple coordinated techniques and strategies rather than reliance on a single control.

## Mental Models

- **Think of LDSE as "loss as the organizing principle."** Instead of running separate safety, security, and reliability processes, unify them by asking: "What are all the ways this system could lose value?" and addressing those through a common architecture and design conversation.

- **Use the loss-driven attribute framework when scoping a system.** Map your concerns (adversities, assets, losses, coping mechanisms, timeframes) against all loss-driven domains upfront, then aggregate overlaps to avoid building duplicate analysis and control mechanisms.

- **Apply the 19 loss-control design principles as a checklist during architecture and design.** Anomaly detection, redundancy, distributed privilege, defense-in-depth, and protective defaults are domain-agnostic protective patterns that work across safety, security, and reliability.

- **Recognize siloism as an organizational anti-pattern.** If safety engineers, security engineers, and reliability engineers are not sharing requirements, architectural decisions, and design solutions, you are paying the cost of LDSE integration without gaining the benefit—use IPTs to break that cycle.

## Anti-patterns

- **Treating loss-driven specialty areas in isolation.** Safety, security, reliability, and resilience are often managed by separate teams with separate processes. This results in redundant requirements, conflicting design solutions, and missed opportunities to address multiple loss concerns with a single architectural pattern.

- **Ignoring loss-driven concerns in standard SE practices.** Traditional lifecycle processes (ISO 15288, INCOSE Handbook) focus primarily on capability delivery. Without augmentation to explicitly address loss-driven attributes in mission analysis, requirements, architecture, and design, loss concerns are under-resourced and late-stage discoveries become expensive.

- **Failing to model loss management scenarios.** If loss scenarios (how adversities interact with system elements to produce loss) are not explicitly captured in model-based systems engineering artifacts, they remain implicit and are vulnerable to gaps in stakeholder communication.

## Key Takeaways

1. **Loss-driven specialty areas share more than they differ.** Resilience, safety, security, reliability, availability, and quality management all address potential losses and share common objectives, requirements, architectural solutions, and analytical techniques. Recognizing this commonality is the foundation of LDSE.

2. **LDSE saves engineering effort while improving comprehensiveness.** By unifying loss-driven processes, you eliminate redundancy, ensure holistic coverage of adversities and weaknesses, reduce non-redundant data artifacts, and identify solutions that address multiple loss concerns simultaneously.

3. **Six systems engineering practices require augmentation for LDSE:** Business/Mission Analysis, Stakeholder Needs and Requirements Definition, System Requirements Definition, Architecture Definition, Design Definition, and Risk Management. Integrate loss management scenarios and loss-driven requirements into each.

4. **Eight core LDSE principles guide system design:** minimize hazards, control unavoidable ones, use proven solutions, enable humans to prevent and recover from loss, seek simplicity, design for evolvability, trace actions to responsible entities, and ensure critical tasks have multiple execution paths.

5. **Nineteen loss-control design techniques operationalize LDSE during architecture and design.** Anomaly detection, defense-in-depth, commensurate protection, protective defaults, distributed privilege, diversity, redundancy, least privilege/functionality/sharing, and protective failure/recovery are domain-agnostic protective patterns.

6. **Model-based systems engineering must expand its information artifacts to capture loss management.** Add adversities as context actors, loss management scenarios as use cases, and model loss management state diagrams, sequence flows, and design features across the lifecycle.

7. **Organizational structure matters.** Use Integrated Product Teams and break down silos to ensure loss-driven specialists share information, collaborate on holistic architectural decisions, and collectively consider the full spectrum of adversities, weaknesses, assets, timeframes, and coping mechanisms.

## Connects To

- **ISO/IEC/IEEE 15288 (Systems and Software Engineering – System and Software Engineering Lifecycle Processes)**: LDSE augments ISO 15288's standard lifecycle processes with explicit loss-driven requirements elicitation, architecture decisions, design decisions, and risk management integration.

- **INCOSE Systems Engineering Handbook**: SEBoK's foundational reference; LDSE extends the Handbook's capability-driven methodology with loss-driven specialty area unification.

- **Risk Management**: Core integrating discipline that sits at the center of LDSE; all loss-driven activities feed risk identification, analysis, and mitigation.

- **System Safety Engineering, System Security Engineering, Reliability, and Resilience Engineering**: The primary loss-driven specialty domains unified under the LDSE umbrella.

- **Model-Based Systems Engineering (MBSE)**: LDSE requires augmented SysML models to explicitly capture loss scenarios, adversities, loss-driven requirements, and protective design features across lifecycle phases.

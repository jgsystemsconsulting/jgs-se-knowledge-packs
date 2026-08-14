# Chapter 8: System & Services Acquisition and Supply Chain Risk Management

## Core Idea
Families 3.16 and 3.17 push CUI protection left into how systems and services are bought, engineered, and sustained through the supply chain. Security engineering principles, unsupported component handling, external service oversight, SCRM planning, acquisition methods, and supplier requirements extend 800-171 beyond the operator’s own perimeter.

## Frameworks Introduced
- **Secure acquisition and engineering**: Apply security engineering principles; manage end-of-life components; control external system services that process CUI.
- **Supply chain risk management (SCRM)**: Plan SCRM, choose acquisition strategies that reduce supply chain risk, and impose requirements/processes on suppliers and partners.

## Key Concepts
- **Security engineering principles (03.16.01)**: Apply systems security engineering principles to the specification, design, development, implementation, and modification of CUI systems.
- **Unsupported system components (03.16.02)**: Replace or provide alternative protections when components are no longer supported by developers, vendors, or manufacturers; justify continued use with documented risk acceptance and compensating controls when replacement is impossible.
- **External system services (03.16.03)**: Require providers to comply with security requirements; define and document oversight/user roles; monitor provider compliance.
- **SCRM plan (03.17.01)**: Develop a plan for managing supply chain risks associated with research, development, design, manufacturing, acquisition, delivery, integration, operations, sustainment, and disposal of systems that process CUI; review and update the plan.
- **Acquisition strategies, tools, and methods (03.17.02)**: Employ acquisition strategies and contractual tools that reduce supply chain risk to CUI systems and system components.
- **Supply chain requirements and processes (03.17.03)**: Establish processes and express requirements that address SCRM for suppliers, developers, system integrators, external service providers, and other partners; enforce and monitor those requirements.

## Mental Models
- If a cloud or MSSP touches CUI, their controls become *your* 800-171 surface — contract and monitor accordingly.
- Unsupported software is a ticking compliance and exploit clock; either replace, isolate with compensating controls, or formally accept risk.
- SCRM is lifecycle-wide: design and disposal matter as much as the purchase order.
- Acquisition language is a control: flow down CUI requirements, right-to-assess, and notification duties in contracts.

## Anti-patterns
- **“The vendor is FedRAMP/ISO, so we’re done”**: External services still need documented requirements, roles, and monitoring against *your* CUI ODPs.
- **Running EOL platforms because migration is hard**: Without compensating controls and acceptance, this fails 03.16.02 intent.
- **SCRM plan that only lists preferred vendors**: Missing processes for anomaly response, component authenticity, and disposal.
- **No flow-down to subcontractors**: Sub-tier suppliers often hold the same CUI without knowing 800-171 applies.

## Key Takeaways
1. Security engineering principles must shape build and modification work on CUI systems, not only operations.
2. Unsupported components require replacement or explicit compensating control + risk acceptance paths.
3. External service providers that handle CUI are in scope for requirement compliance and oversight.
4. An SCRM plan covers the full system life cycle from research through disposal.
5. Acquisition strategies and contractual tools are primary SCRM levers.
6. Supplier requirements need processes to enforce and monitor — paper-only flow-down is insufficient.

## Connects To
- **ch01**: Tailoring assumptions include use of external service providers to meet requirements.
- **ch06**: Risk assessments include supply chain considerations; SSP documents external dependencies.
- **ch02 / ch07**: Technical controls still apply inside acquired or outsourced environments holding CUI.
- **NIST SP 800-161 / CSF GV.SC**: Broader C-SCRM practice frameworks that complement these requirements.

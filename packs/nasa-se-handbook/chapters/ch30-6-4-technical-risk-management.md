# Chapter 30: 6.4 Technical Risk Management

## Core Idea

Technical risk is the potential for performance shortfalls—spanning safety, cost, schedule, and technical domains—and must be managed proactively through two complementary processes: Risk-Informed Decision Making (during design direction-setting) and Continuous Risk Management (during development and implementation).

## Frameworks Introduced

- **Risk-Informed Decision Making (RIDM)**: A decision-making process that uses risk and uncertainty information to select design alternatives and establish baseline performance requirements during system conception and direction-setting.
  - When to use: Early lifecycle phases to inform architecture, design trades, and performance requirements before committing to implementation.

- **Continuous Risk Management (CRM)**: An ongoing process that identifies, assesses, and mitigates individual risks throughout development and implementation to ensure requirements are met and residual risk remains acceptable.
  - When to use: Throughout development and implementation phases to monitor emerging risks, track mitigation progress, and trigger contingency actions.

- **Risk Triplet Characterization**: A three-part model decomposing risk into (1) scenario(s) leading to degraded performance, (2) likelihood(s) of those scenarios, and (3) consequence(s) or severity if scenarios occur.
  - When to use: Systematically articulating and communicating risk statements, enabling quantitative or qualitative assessment of both probability and impact.

## Key Concepts

- **Risk**: The potential for performance shortfalls with respect to explicitly-established requirements in one or more domains: safety, technical, cost, schedule, or institutional support. Characterized as a set of triplets with scenarios, likelihoods, and consequences.

- **Scenario**: A sequence of credible events specifying how a system evolves from its current state to an undesirable future state. Scenarios begin with initiating events and include intermediate events that may have mitigating or exacerbating effects.

- **Technical Risk**: Risk associated with design evolution and system production affecting the ability to meet stakeholder expectations and technical requirements; influenced by design, test, and production processes (process risk) and product nature (product risk).

- **Cost Risk**: Risk that cost estimates and objectives are inaccurate, or that program execution will exceed cost objectives due to failure in handling cost, schedule, or performance risks.

- **Schedule Risk**: Risk that schedule estimates are unrealistic, or that program execution will miss schedule objectives due to failure in handling cost, schedule, or performance risks.

- **Programmatic Risk**: Risk from external actions or inactions outside project control (e.g., ITAR restrictions, partner agreements, congressional direction, OMB directives) that manifest as technical, cost, or schedule impacts.

- **Risk Management Plan**: Developed during Technical Planning; defines how risks will be identified, mitigated, monitored, and controlled throughout the project lifecycle.

- **Trigger Threshold**: The risk level or metric value that initiates mitigation or contingency action plans; risks approaching thresholds receive more frequent monitoring.

- **Residual Risk**: The risk remaining after mitigation or contingency action implementation; monitoring continues until residual risk is deemed acceptable.

- **Risk Mitigation**: Proactive action taken to reduce likelihood or consequence of a risk before it occurs.

- **Contingency Action**: Reactive action plan prepared in advance to address consequences if a risk is realized; executed if the risk occurs.

## Mental Models

- **Think of risk as a portfolio, not isolated issues.** NASA's shift from CRM-only to RIDM+CRM reflects this: RIDM shapes requirements and trades using aggregate risk insights, while CRM tracks individual risks to closure. Both perspectives—systemic and granular—are essential.

- **Use the triplet decomposition to separate "what could go wrong" (scenario), "how likely is it" (likelihood), and "how bad would it be" (consequence).** This separation allows different mitigation strategies: reducing likelihood via design robustness, mitigating consequences via redundancy or early detection, or accepting risk if triplet values are low.

- **Trigger thresholds are decision gates, not alarm bells.** A well-designed threshold system converts qualitative concern into actionable governance, preventing both premature escalation and delayed response.

## Anti-patterns

- **Treating risk management as a compliance checkbox rather than a decision-support process.** Risk management without linkage to design decisions and resource allocation is documentation exercise, not engineering discipline.

- **Confusing risk identification with risk assessment.** Listing risks without evaluating likelihood, consequence, and triplet structure produces noise; assessment prioritizes action.

- **Waiting for a crisis to trigger mitigation.** Reactive contingency-only approaches squander the opportunity to reduce risk early; proactive mitigation during design is more cost-effective.

- **Ignoring programmatic risk as "not engineering."** External constraints (regulatory, contractual, organizational) directly constrain technical feasible space; overlooking them invites late-stage surprises.

## Key Takeaways

1. **Risk is multi-dimensional.** Technical shortfalls are only one domain; cost, schedule, safety, and institutional support risks are equally critical and often interdependent. Isolating technical risk from cost and schedule is artificial.

2. **Integrate risk into decision-making from the start.** RIDM informs design trades and baseline requirements; embedding uncertainty and risk quantification into architecture trades prevents downstream surprises and provides traceability for decisions.

3. **Establish clear monitoring and trigger strategies.** Periodic status reporting on each technical risk at agreed-upon frequency, with escalation thresholds, converts abstract risk statements into operational governance. Risks approaching triggers receive higher monitoring frequency.

4. **Prepare both mitigation and contingency in advance.** Identify stakeholders and organizations responsible for each risk's response before the trigger fires; pre-planned action reduces response time and decision friction.

5. **Document assumptions, rationale, and lessons.** Capture why certain risks were prioritized, what decision alternatives were rejected, and outcomes of mitigation attempts; this record supports future projects and continuous process improvement.

6. **Plan for residual risk.** Even after mitigation, some risk remains acceptable; distinguish between risks you eliminate and risks you manage or accept, and ensure stakeholders understand the residual exposure.

## Connects To

- **ISO/IEC/IEEE 42010 (Systems Architecture)**: Risk management informs architectural decisions and supports traceability of design rationale; residual risk is explicitly communicated in architecture documentation.

- **NPR 8000.4 (Agency Risk Management Procedural Requirements)**: Mandates RIDM+CRM approach; sets NASA-wide policy for risk identification, assessment, and escalation.

- **NASA/SP-2011-3422 (NASA Risk Management Handbook)**: Detailed guidance on RM processes, including techniques for scenario analysis, likelihood and consequence estimation, and mitigation planning.

- **NASA/SP-2010-576 (NASA Risk-Informed Decision Making Handbook)**: Elaborates RIDM methodology for architecture and requirements trades.

- **Technical Planning Process**: Risk Management Plan is an output of technical planning and drives the overall risk governance structure for the program/project.

- **Technical Reviews (Section 6.7.2)**: Configuration and functional audits verify that design mitigation actions have been properly implemented and that residual risk is being managed.

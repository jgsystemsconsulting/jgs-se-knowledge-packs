# Chapter 7: MANAGE Function

## Core Idea
MANAGE allocates risk resources to prioritised risks from MAP and MEASURE, executes risk treatment plans, monitors deployed systems, and communicates about incidents; it closes the risk management loop and enables continual improvement.

## Frameworks Introduced
- **MANAGE Function**: Four category groups (MANAGE 1–4) covering risk prioritisation and response, benefit maximisation and impact minimisation, third-party risk management, and post-deployment monitoring and communication.
  - When to use: Once MAP and MEASURE have produced prioritised risk information; continuously throughout the deployment and operational lifecycle.

## Key Concepts
- **MANAGE 1 (Risk prioritisation and response)**: AI system go/no-go determination; treatment prioritised by impact, likelihood, and available resources; risk response plans (mitigate, transfer, avoid, accept) developed and documented; residual risks documented for downstream acquirers and end users.
- **MANAGE 1.1**: Determination of whether the AI system achieves its intended purposes and whether development or deployment should proceed.
- **MANAGE 1.2**: Treatment of documented AI risks is prioritised based on impact, likelihood, and available resources or methods.
- **MANAGE 1.3**: Responses to high-priority risks are developed and documented; options include mitigating, transferring, avoiding, or accepting.
- **MANAGE 1.4**: Negative residual risks to downstream acquirers and end users are documented.
- **MANAGE 2 (Strategy implementation)**: Resources for risk management are balanced against viable non-AI alternatives; mechanisms sustain deployed system value; unknown risks are responded to when identified; mechanisms exist to supersede, disengage, or deactivate systems with inconsistent performance.
- **MANAGE 2.4**: Mechanisms are in place to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use.
- **MANAGE 3 (Third-party risk management)**: Third-party AI risks and benefits are regularly monitored; pre-trained models used in development are monitored as part of regular system maintenance.
- **MANAGE 4 (Post-deployment monitoring and communication)**: Post-deployment monitoring plans (including user feedback, appeal, override, decommissioning, incident response, change management) are implemented; measurable continual-improvement activities are integrated into updates; incidents and errors are communicated to affected communities.
- **MANAGE 4.3**: Incidents and errors are communicated to relevant AI actors including affected communities; tracking, response, and recovery processes are followed and documented.
- **Risk response options**: Mitigate (reduce likelihood or impact), transfer (shift responsibility), avoid (discontinue the activity), accept (acknowledge and proceed within tolerance).
- **Continual improvement**: Measurable performance improvements or declines identified through consultation with relevant AI actors and field data; integrated into system update cycles.

## Mental Models
- Use the four response options as an explicit decision space: every high-priority risk identified in MAP/MEASURE requires a documented choice among mitigate, transfer, avoid, or accept.
- Use MANAGE 2.4 as an operational kill switch: if a deployed system's performance diverges from intended use, the mechanism to disengage must be in place before deployment, not after the problem emerges.
- Use post-deployment monitoring as a feedback loop back into MAP and MEASURE: field data from MANAGE 4 surfaces emergent risks requiring new measurement cycles.

## Anti-patterns
- **Accepting risk without documentation**: Accepting a risk implicitly (without explicit MANAGE 1.3 documentation) leaves no accountability trail and no basis for future re-evaluation.
- **Neglecting residual risk disclosure**: MANAGE 1.4 requires documenting residual risks for downstream acquirers and end users; omitting this shifts unacknowledged risk onto others.
- **Treating post-deployment as set-and-forget**: MANAGE 4 requires active, ongoing monitoring, incident communication, and continual improvement — not a passive post-launch posture.

## Key Takeaways
1. Begin MANAGE with the go/no-go determination (MANAGE 1.1); this formalises the decision to deploy and creates an accountability record.
2. Document all risk response decisions with rationale; silent acceptance of risk is a governance failure.
3. Residual risk disclosure (MANAGE 1.4) is an obligation to downstream users and acquirers, not optional transparency.
4. Viable non-AI alternatives must be considered (MANAGE 2.1); risk management includes the option that AI is not the right tool.
5. An operational deactivation mechanism (MANAGE 2.4) is a deployment prerequisite; it must be tested, not assumed.
6. Incident communication to affected communities (MANAGE 4.3) is a mandatory practice, not a discretionary transparency gesture.

## Connects To
- **MAP function**: MANAGE consumes MAP's impact characterisation and risk identification as the basis for prioritisation.
- **MEASURE function**: MANAGE uses MEASURE's metrics, benchmarks, and risk tracking outputs to prioritise and calibrate responses.
- **GOVERN function**: GOVERN defines the resource allocation authority, risk tolerance, and accountability structures within which MANAGE operates.
- **NIST RMF SP 800-37**: Parallel risk treatment and continuous monitoring practices in the cybersecurity domain.
- **ISO 31000:2018**: Risk treatment vocabulary (residual risk, risk response) directly used in MANAGE.

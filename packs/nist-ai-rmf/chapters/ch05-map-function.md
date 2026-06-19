# Chapter 5: MAP Function

## Core Idea
MAP establishes the contextual knowledge — about purposes, stakeholders, system capabilities, impacts, and risks — needed to frame risks before they are measured or managed; it enables the go/no-go decision on whether to proceed with an AI system.

## Frameworks Introduced
- **MAP Function**: Five category groups (MAP 1–5) covering context establishment, AI system categorisation, capability and benefit/cost analysis, third-party risk mapping, and societal impact characterisation.
  - When to use: At the start of any AI system initiative, and continuously as context, capabilities, and stakeholders evolve.

## Key Concepts
- **MAP 1 (Context establishment)**: Intended purposes, legal norms, deployment settings, user expectations, risk tolerances, system requirements, and mission alignment are documented; actor competencies and diversity are recorded (subcategories MAP 1.1–1.6).
- **MAP 1.1**: Intended purposes, potentially beneficial uses, context-specific laws, norms, expectations, and prospective deployment settings are understood and documented.
- **MAP 1.5**: Organisational risk tolerances are determined and documented.
- **MAP 2 (AI system categorisation)**: Specific tasks, methods, knowledge limits, human oversight, scientific integrity, and TEVV considerations are defined and documented.
- **MAP 2.2**: AI system knowledge limits and how system output will be overseen by humans are documented to support subsequent decision-making.
- **MAP 3 (Capabilities, goals, benefits, costs)**: Potential benefits and costs — including non-monetary costs from AI errors — are examined relative to organisational risk tolerance; application scope, operator proficiency, and human oversight processes are specified.
- **MAP 3.5**: Processes for human oversight are defined and documented in accordance with GOVERN policies.
- **MAP 4 (Third-party and component risk)**: Legal and IP risks, internal risk controls for AI components including third-party technologies, are mapped and documented.
- **MAP 5 (Societal impact characterisation)**: Likelihood and magnitude of beneficial and harmful impacts — including on individuals not using the system — are documented; feedback from external actors is integrated.
- **Go/no-go decision**: After MAP, the organisation has sufficient contextual knowledge to decide whether to proceed with design, development, or deployment.
- **Context of use**: The specific application setting, user population, legal environment, and societal factors that shape an AI system's risks and benefits.

## Mental Models
- Use MAP as the prerequisite to MEASURE and MANAGE: without the contextual knowledge MAP produces, risk measurement is directionless and risk management is reactive.
- Use diverse, external perspectives in MAP: internal teams alone cannot see all contextual risks; engagement with affected communities, domain experts, and external collaborators is a structural requirement.
- Treat MAP as iterative: re-apply as context, capabilities, risks, and benefits evolve — especially after deployment.

## Anti-patterns
- **Skipping context documentation**: Proceeding directly to model building without MAP 1 creates blind spots about intended purposes, legal constraints, and user populations.
- **Treating MAP as a one-time exercise**: Initial MAP at system inception does not substitute for ongoing re-mapping as deployment context or system capabilities change.
- **Ignoring third-party components in MAP 4**: AI systems built on third-party data, models, or software inherit risks that must be mapped explicitly, not assumed to be managed by the provider.

## Key Takeaways
1. MAP must be completed before MEASURE or MANAGE are meaningful; it is the information-gathering function on which all subsequent risk analysis depends.
2. Document the go/no-go determination after MAP; this creates an explicit accountability record for the decision to proceed.
3. Context of use is dynamic; MAP must be reapplied whenever deployment setting, user population, or system capabilities change.
4. Societal impact (MAP 5) includes people who never interact with the AI system; their potential harms must be characterised.
5. Human oversight processes (MAP 3.5) must be defined at the MAP stage, not retrofitted after deployment.
6. Broad, demographically diverse actor participation in MAP is a structural requirement that improves the quality of all downstream risk activities.

## Connects To
- **GOVERN function**: MAP operates within the policies, risk tolerances, and accountability structures established by GOVERN.
- **MEASURE function**: MAP outputs (identified risks, context, system categorisation) are the direct inputs to MEASURE.
- **MANAGE function**: MAP's impact characterisation and component risk mapping inform MANAGE's prioritisation and response planning.
- **ISO/IEC 42001**: AI management system requirements for context establishment parallel MAP 1.
- **NIST Privacy Framework**: Privacy risk identification in MAP 5 / MAP 4 is informed by Privacy Framework guidance.

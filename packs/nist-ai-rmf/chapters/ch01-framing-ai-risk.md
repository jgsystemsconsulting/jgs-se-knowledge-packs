# Chapter 1: Framing AI Risk

## Core Idea
AI risk is a composite of the probability and magnitude of harm from an AI system's operation; unlike traditional software risk, AI risks are socio-technical, emergent across the lifecycle, and frequently difficult to measure precisely.

## Frameworks Introduced
- **AI Risk Management (general)**: Coordinated activities to direct and control an organisation with regard to AI-specific risk, minimising negative impacts while maximising positive ones.
  - When to use: Any time an organisation designs, develops, deploys, or acquires an AI system.

## Key Concepts
- **Risk**: Composite measure of an event's probability of occurring and the magnitude of the consequences (ISO 31000:2018).
- **Risk tolerance**: The organisation's or AI actor's readiness to bear risk in order to achieve objectives; highly contextual and use-case specific (ISO GUIDE 73).
- **Residual risk**: Risk remaining after risk treatment; directly impacts end users and affected communities (ISO GUIDE 73).
- **Risk prioritisation**: Allocating resources to risks according to severity; highest-risk systems require the most urgent and thorough management.
- **Risk measurement**: Quantitative or qualitative assessment of AI risk; complicated by inscrutability, emergent properties, and third-party dependencies.
- **Inscrutability**: Opacity of AI systems arising from limited explainability, lack of documentation, or inherent uncertainty; complicates risk measurement.
- **Emergent risk**: Risks that arise as AI systems adapt, evolve, or are used beyond their intended scope; may not be present at initial deployment.
- **Third-party risk**: Risk introduced by external data, software, or hardware components whose risk metrics may not align with the deploying organisation's.
- **Socio-technical risk**: Risk arising from the interplay of technical aspects and societal dynamics, including how a system is used, who operates it, and the social context of deployment.

## Mental Models
- Use impact-and-likelihood framing: risk = f(magnitude of harm, likelihood of occurrence); do not conflate inability to measure with low risk.
- Use lifecycle staging: measure risk at each stage (design, development, deployment, operation) because latent risks may increase as systems evolve.
- Use context-first prioritisation: human-facing systems, those trained on sensitive data, or those with direct human impact warrant higher initial prioritisation.

## Anti-patterns
- **Attempting to eliminate all risk**: Counterproductive; leads to inefficient resource allocation and impractical triage. Aim for managed residual risk within tolerance.
- **Treating AI risk in isolation**: AI risks (privacy, security, bias) overlap with enterprise risk; siloed management produces organisational inefficiencies.
- **Assuming unmeasured risk equals low risk**: Inability to measure a risk does not imply it is small; unknown risks still demand tracking.

## Key Takeaways
1. Define risk tolerance explicitly before applying the AI RMF; the framework does not prescribe tolerance levels.
2. Risk measurement must account for third-party components, lifecycle stage, real-world deployment conditions, and human baselines.
3. AI risks are socio-technical; purely technical assessments will miss social and contextual harms.
4. When AI risk is unacceptable (severe harms imminent or occurring), halt development or deployment until risks can be managed.
5. Document residual risks so that downstream acquirers and end users are informed of potential negative impacts.
6. Integrate AI risk management into broader enterprise risk management alongside cybersecurity and privacy.

## Connects To
- **ISO 31000:2018**: Source definition of risk and risk management; AI RMF adapts its vocabulary.
- **OMB Circular A-130:2016**: Basis for the two-factor risk formula (magnitude × likelihood).
- **NIST Cybersecurity Framework / NIST RMF SP 800-37**: Overlapping risk frameworks for security and privacy applicable within AI RMF MAP/MEASURE/MANAGE.
- **ISO 26000:2010 / ISO/IEC TR 24368:2022**: Social responsibility and professional responsibility framing used in the AI RMF's responsible-AI rationale.

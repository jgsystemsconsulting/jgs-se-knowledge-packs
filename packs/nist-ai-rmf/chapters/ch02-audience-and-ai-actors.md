# Chapter 2: Audience and AI Actors

## Core Idea
The AI RMF is intended for all AI actors across the full AI lifecycle and its socio-technical dimensions; effective risk management demands demographically and disciplinarily diverse teams spanning design, development, deployment, operation, and evaluation.

## Frameworks Introduced
- **OECD AI Lifecycle Dimensions**: Five socio-technical dimensions (Application Context, Data and Input, AI Model, Task and Output, People and Planet) organising AI activities for risk governance.
  - When to use: Mapping responsibilities and risk perspectives across a cross-functional AI programme.
- **TEVV (Test, Evaluation, Verification, and Validation)**: Integrated assurance process performed throughout the AI lifecycle by actors separate from front-line developers.
  - When to use: Any stage from design through operation where system trustworthiness must be confirmed or risks tracked.

## Key Concepts
- **AI actor**: Any individual or organisation that plays an active role in the AI system lifecycle, including designers, developers, deployers, operators, evaluators, and affected communities (OECD 2019).
- **AI system**: An engineered or machine-based system that, for a given set of objectives, generates outputs such as predictions, recommendations, or decisions influencing real or virtual environments; operates with varying levels of autonomy (OECD 2019; ISO/IEC 22989:2022).
- **Application Context dimension**: The intended use environment, deployment setting, and contextual norms that shape AI system requirements and risk exposure.
- **AI Model dimension**: The model building, interpretation, training, and validation tasks performed during the AI development phase.
- **People and Planet dimension**: The central dimension representing human rights and broader societal and planetary wellbeing; informs primary AI actors via norms, guidance, and boundary-setting.
- **TEVV actors**: AI actors who examine the AI system, detect and remediate problems, and perform verification and validation tasks; kept separate from builders as a best practice.
- **Interdisciplinary team**: A group with demographic, disciplinary, and experiential diversity; increases the likelihood of surfacing implicit assumptions and emergent risks.

## Mental Models
- Use actor-role mapping before assigning risk responsibilities: different lifecycle phases (Design, Development, Deployment, Operation, TEVV) have distinct actors with distinct risk perspectives.
- Use the People and Planet dimension as a check: affected communities who do not interact with the system are still valid stakeholders and risk informants.
- Use TEVV separation: validators and verifiers should be distinct from builders to avoid conflicts of interest and internal bias.

## Anti-patterns
- **Homogeneous teams**: Uniform backgrounds suppress implicit assumptions, miss cultural or contextual risks, and reduce open idea-sharing.
- **Excluding affected communities**: Treating only direct users as stakeholders misses downstream harms to individuals who never interact with the system.

## Key Takeaways
1. The primary AI RMF audience is AI actors who perform or manage design, development, deployment, evaluation, and use across the lifecycle dimensions.
2. TEVV is a continuous, cross-lifecycle process, not a gate at the end; integrate it from the planning and design stage onward.
3. Diverse, multidisciplinary teams are a structural requirement for effective risk management, not an optional enhancement.
4. Third-party entities (vendors, data providers) are AI actors with shared risk responsibilities even though they are external to the deploying organisation.
5. End users and affected individuals are distinct categories: end users interact with the system; affected individuals may be impacted without any interaction.

## Connects To
- **OECD Framework for Classification of AI Systems (2022)**: Source of the lifecycle-dimension model adapted by NIST.
- **GOVERN 2.1 / GOVERN 3.1**: Subcategories formalising role documentation and team diversity requirements.
- **MAP 1.2**: Subcategory requiring documentation of interdisciplinary actor participation and diversity.
- **ISO/IEC 22989:2022**: Source definition of AI system.

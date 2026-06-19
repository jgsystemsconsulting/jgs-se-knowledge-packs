# Chapter 1: General Provisions — Subject Matter, Scope, Definitions, AI Literacy

## Core Idea
Chapter I establishes the regulatory foundation: what the AI Act is for, who it applies to, what an AI system is, and what 68 key terms mean. It also places a baseline AI literacy obligation on all providers and deployers. The dual purpose is market harmonisation and fundamental-rights protection, not technology suppression.

## Frameworks Introduced
- **Risk-tiered regulatory framework**: The Act structures obligations into four tiers — prohibited practices, high-risk requirements, transparency obligations, and voluntary codes — all defined here by reference.
  - When to use: Use this mental map whenever classifying any AI system to determine which obligations attach.
- **Article 1 dual-objective test**: Every provision should be read against both internal-market harmonisation and high protection of health, safety, and fundamental rights.
  - When to use: When resolving ambiguities in scope or applicability.
- **Article 4 AI literacy obligation**: Providers and deployers must take measures to ensure sufficient AI literacy in staff dealing with AI systems, proportionate to context.
  - When to use: When designing training programmes, onboarding deployers, or auditing operator readiness.

## Key Concepts
- **AI system** (Art 3(1)) — a machine-based system designed to operate with varying levels of autonomy, which may exhibit adaptiveness after deployment and, for explicit or implicit objectives, infers from input how to generate outputs (predictions, content, recommendations, decisions) that can influence physical or virtual environments.
- **Provider** (Art 3(3)) — any natural or legal person that develops or has developed an AI system or GPAI model and places it on the market or puts it into service under their own name or trademark.
- **Deployer** (Art 3(4)) — any natural or legal person using an AI system under their authority, except in the course of a personal non-professional activity.
- **Operator** (Art 3(8)) — umbrella term covering provider, product manufacturer, deployer, authorised representative, importer, or distributor.
- **Intended purpose** (Art 3(12)) — the use for which an AI system is intended by the provider, including specific context and conditions, as specified in documentation, instructions for use, and promotional materials.
- **Reasonably foreseeable misuse** (Art 3(13)) — use not in accordance with intended purpose but resulting from reasonably foreseeable human behaviour or interaction with other systems.
- **Serious incident** (Art 3(49)) — incident or malfunction leading directly or indirectly to death, serious health harm, serious disruption of critical infrastructure, infringement of fundamental rights obligations, or serious harm to property or environment.
- **AI literacy** (Art 3(56)) — skills, knowledge, and understanding allowing providers, deployers, and affected persons to make informed deployments and gain awareness of opportunities, risks, and possible harm.
- **General-purpose AI (GPAI) model** (Art 3(63)) — an AI model trained with large data using self-supervision at scale, displaying significant generality and capable of performing a wide range of distinct tasks regardless of how it is placed on the market.
- **Systemic risk** (Art 3(65)) — a risk specific to high-impact capabilities of GPAI models having significant Union-market impact due to reach or negative effects on public health, safety, security, fundamental rights, or society as a whole.

## Mental Models
- **"Autonomy + adaptiveness + inference = AI system"**: If a machine-based system operates with varying autonomy, may adapt after deployment, and infers outputs from inputs, it is an AI system under Art 3(1). Systems that purely execute hard-coded rules without inference do not qualify.
- **"Who holds the name holds the obligation"**: Provider obligations follow whoever places the system on the market under their own name or trademark, not necessarily whoever built it.
- **"Scope carve-outs stack"**: The exclusions in Art 2 (military/defence, pure R&D before placement, purely personal use, open-source outside prohibited/high-risk categories) are cumulative; check all before concluding inapplicability.

## Anti-patterns
- Treating "deployer" and "provider" as interchangeable: they carry different obligations (Art 16 vs Art 26), and a deployer can become a provider by affixing their trademark (Art 25).
- Assuming open-source release removes all obligations: open-source AI systems remain fully subject to the Act if placed on the market as high-risk or if they fall under Art 5 (prohibited practices) or Art 50 (transparency obligations).
- Using "reasonably foreseeable misuse" to avoid risk assessment: the Act explicitly requires providers to evaluate risks under both intended purpose and foreseeable misuse scenarios (Art 9(2)(b)).

## Key Takeaways
1. The AI system definition is functional (inference + autonomy), not technical; this is intentionally broad.
2. Obligations attach to market actors by role (provider, deployer, importer, distributor), not to the technology itself.
3. Four scope exclusions are most practically significant: military/defence, purely personal non-professional use, pre-market R&D, and qualifying open-source.
4. GDPR and the AI Act coexist: Art 2(7) explicitly preserves GDPR; a DPIA can partially satisfy AI Act obligations (Art 26(9)).
5. AI literacy is a standing obligation, not a one-time training event; it must account for the specific context and affected persons.
6. Provider-deployer split of liability is governed by written agreement on the value chain (Art 25(4)).

## Connects To
- **Chapter II (Art 5)**: The prohibited practices are the first operational use of the scope established here.
- **Chapter III (Art 6-49)**: High-risk classification and requirements draw directly on the definitions in Art 3.
- **Chapter V (Art 51-58)**: GPAI model obligations build on the GPAI model definition in Art 3(63-68).
- **Chapter X (Art 95)**: Voluntary codes reference AI literacy promotion from Art 4 and Art 96.

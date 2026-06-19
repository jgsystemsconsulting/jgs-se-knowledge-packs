# Chapter 8: General-Purpose AI (GPAI) Models — Classification, Obligations, Systemic Risk (Chapter V, Articles 51-58)

## Core Idea
Chapter V introduces a separate regulatory regime for general-purpose AI (GPAI) models — foundation models and large language models that can serve many downstream purposes. All GPAI providers bear baseline obligations (documentation, copyright policy, training data summary). GPAI models classified as having systemic risk face additional obligations including adversarial testing and incident reporting. The 10^25 floating-point operations (FLOPs) training-compute threshold is the presumptive trigger for systemic risk classification.

## Frameworks Introduced
- **Article 51 — Systemic Risk Classification**: A GPAI model is classified as having systemic risk if it has high-impact capabilities (matching or exceeding the most advanced GPAI models), or if the Commission designates it by decision. The rebuttable presumption: cumulative training compute exceeding 10^25 FLOPs.
  - When to use: When a GPAI provider assesses whether their model falls into the systemic risk tier.
- **Article 53 — Baseline obligations for all GPAI providers**: Four obligations: (a) draw up and maintain technical documentation (Annex XI content); (b) provide downstream providers with information enabling them to understand capabilities/limitations and comply with their obligations (Annex XII content); (c) implement a copyright compliance policy including respecting text and data mining rights reservations (Art 4(3) of Directive 2019/790); (d) publish a sufficiently detailed training data summary.
  - When to use: For every GPAI model provider placing a model on the Union market, whether or not systemic risk.
- **Article 55 — Additional obligations for systemic-risk GPAI providers**: Four additional obligations: (a) adversarial testing (red-teaming) per standardised protocols; (b) assess and mitigate systemic risks at Union level; (c) track, document, and report serious incidents and corrective measures without undue delay to AI Office; (d) ensure adequate cybersecurity protection for the model and its physical infrastructure.
  - When to use: For GPAI providers whose model has been classified as systemic-risk (Art 51) or designated by Commission (Art 52(4)).
- **Article 56 — Codes of Practice for GPAI**: The AI Office facilitates codes of practice as the primary compliance pathway for GPAI obligations. Compliance with an approved code creates a presumption of conformity with Art 53 and 55. Harmonised standards, once published, create the same presumption.
  - When to use: As the practical compliance route for GPAI providers until harmonised standards are available.
- **Article 52 — Notification and Designation Procedure**: Providers meeting the 10^25 FLOPs threshold must notify the Commission within two weeks. They may argue their model lacks systemic risk despite meeting the threshold; the Commission may reject those arguments. The Commission may also designate models ex officio or on scientific panel alert.
  - When to use: When assessing notification obligations and the dispute procedure for systemic risk designation.

## Key Concepts
- **General-purpose AI (GPAI) model** (Art 3(63)) — an AI model trained with large amounts of data using self-supervision at scale, displaying significant generality and capable of performing a wide range of distinct tasks, regardless of how it is placed on the market, and integrable into a variety of downstream systems. (Excludes models used only for R&D/prototyping before market placement.)
- **High-impact capabilities** (Art 3(64)) — capabilities matching or exceeding those of the most advanced GPAI models; the qualitative criterion for systemic risk.
- **10^25 FLOPs threshold** (Art 51(2)) — the rebuttable quantitative presumption: cumulative training compute greater than 10^25 floating-point operations creates a presumption of high-impact capabilities. Subject to amendment by delegated act.
- **Systemic risk** (Art 3(65)) — risk specific to high-impact GPAI capabilities with significant Union-market impact due to reach, or reasonably foreseeable negative effects on public health, safety, security, fundamental rights, or society, propagable at scale across the value chain.
- **Open-source GPAI exception** (Art 53(2)) — GPAI models released under open-source licences (free access, usage, modification, and distribution; publicly available weights, architecture, usage information) are exempt from the technical documentation and downstream information obligations in Art 53(1)(a)-(b). This exception does NOT apply to systemic-risk GPAI models.
- **Downstream provider** (Art 3(68)) — a provider of an AI system (including a general-purpose AI system) that integrates a GPAI model, whether self-developed or obtained from another entity.
- **Adversarial testing / red-teaming** (Art 55(1)(a)) — systematic testing of a GPAI model's capabilities and safeguards by simulating adversarial conditions to identify and mitigate systemic risks.

## Mental Models
- **"Two-tier GPAI regime"**: All GPAI providers face baseline obligations (Art 53); systemic-risk GPAI providers face baseline PLUS additional obligations (Art 55). The tier is set by classification under Art 51.
- **"Open-source gets a pass — but not for systemic risk"**: The open-source exception cuts compliance burden significantly, but systemic-risk GPAI models lose this exception; even open-source frontier models must meet all obligations if they have high-impact capabilities.
- **"Codes of practice are the de facto compliance mechanism"**: In the absence of harmonised standards, approved codes of practice are the primary route to presumption of conformity with GPAI obligations.

## Anti-patterns
- Treating all GPAI models as equivalent: the two-tier structure means that a GPT-4-scale model has substantially more obligations than a smaller, lower-capability GPAI model.
- Assuming the FLOPs threshold is fixed: Art 51(3) empowers the Commission to amend the threshold and supplement with benchmarks and indicators as technology evolves; algorithmic efficiency improvements or hardware advances may change the effective classification boundary.
- Conflating GPAI model obligations with high-risk AI system obligations: GPAI model providers face Chapter V obligations; when a GPAI model is integrated into a downstream AI system that is high-risk, the downstream provider faces Chapter III obligations for that system. The two regimes stack.

## Key Takeaways
1. All GPAI model providers: technical documentation, downstream information, copyright policy, training data summary.
2. Systemic-risk GPAI providers additionally: adversarial testing, systemic risk assessment and mitigation, serious incident reporting, cybersecurity.
3. 10^25 FLOPs training compute is the rebuttable presumptive trigger for systemic risk; notification must reach the Commission within two weeks of threshold being met.
4. Open-source GPAI models are exempt from Art 53(1)(a)-(b) documentation obligations unless they have systemic risk.
5. Codes of practice (Art 56) are the primary compliance pathway until harmonised standards arrive; providers who neither follow an approved code nor comply with harmonised standards must demonstrate alternative adequate means of compliance.
6. The Commission has exclusive enforcement jurisdiction over Chapter V (Art 88), exercised through the AI Office.

## Connects To
- **Chapter I (Art 3(63-68))**: GPAI definitions.
- **Chapter VII (Art 64)**: AI Office is the enforcement body for Chapter V.
- **Chapter IX Section 5 (Art 88-94)**: Commission/AI Office enforcement and evaluation powers specific to GPAI.
- **Chapter XII (Art 101)**: GPAI provider fines up to 3% of global annual turnover or EUR 15 million.
- **Annex XI-XII**: Minimum content for GPAI technical documentation and downstream information.

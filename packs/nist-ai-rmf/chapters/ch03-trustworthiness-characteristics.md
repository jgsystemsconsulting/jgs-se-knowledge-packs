# Chapter 3: AI Trustworthiness Characteristics

## Core Idea
Trustworthy AI systems must balance seven interdependent characteristics — valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed — with Valid and Reliable as the necessary foundation for all others.

## Frameworks Introduced
- **Seven Trustworthiness Characteristics (Fig. 4)**: A structured set of socio-technical attributes whose balance defines AI trustworthiness; tradeoffs among them require contextual human judgement.
  - When to use: Evaluating any AI system for deployment readiness or conducting a trustworthiness gap analysis.
- **Three Categories of AI Bias (NIST SP 1270)**: Systemic, computational-and-statistical, and human-cognitive; each can occur without discriminatory intent.
  - When to use: Designing bias management plans or auditing fairness of AI outputs.

## Key Concepts
- **Valid and Reliable**: Validation confirms requirements for intended use are fulfilled (ISO 9000:2015); reliability is the ability to perform as required over a given time interval under given conditions (ISO/IEC TS 5723:2022). The base characteristic; necessary for all others.
- **Accuracy**: Closeness of results to true or accepted values (ISO/IEC TS 5723:2022); must be paired with defined, realistic test sets representative of deployment conditions.
- **Robustness (generalizability)**: Ability to maintain performance under a variety of circumstances, including unanticipated uses; minimises harm when operating outside expected settings (ISO/IEC TS 5723:2022).
- **Safe**: An AI system that does not, under defined conditions, lead to a state in which human life, health, property, or the environment is endangered (ISO/IEC TS 5723:2022).
- **Secure and Resilient**: Secure systems maintain confidentiality, integrity, and availability against attacks; resilient systems withstand adverse events and degrade safely and gracefully.
- **Transparency**: The extent to which information about an AI system and its outputs is available to those interacting with it; enables redress and accountability.
- **Explainability**: A representation of the mechanisms underlying an AI system's operation — answers "how" a decision was made.
- **Interpretability**: The meaning of AI system output in the context of its designed functional purposes — answers "why" a decision has that meaning for the user.
- **Privacy-Enhanced**: AI system design that safeguards human autonomy, identity, and dignity through anonymity, confidentiality, and consent-based data control.
- **Fairness with Bias Managed**: Addressing equality, equity, harmful bias, and discrimination; systems with balanced predictions across groups may still be unfair (e.g., inaccessible to people with disabilities).
- **Systemic bias**: Bias embedded in datasets, organisational practices, or broader societal norms across the AI lifecycle.
- **Computational/statistical bias**: Bias from systematic errors in non-representative samples or algorithmic processes.
- **Human-cognitive bias**: Bias in how individuals or groups perceive, interpret, or act on AI system information.

## Mental Models
- Treat Valid and Reliable as a gate: a system cannot be safe, fair, or explainable if it does not first produce correct, consistent outputs.
- Treat Accountable and Transparent as cross-cutting: it applies to every other characteristic and supports redress, audit, and governance across all of them.
- Navigate tradeoffs explicitly: accuracy vs. interpretability, privacy-enhancing techniques vs. accuracy, fairness vs. predictive performance — each requires a documented contextual judgement.
- Apply the three-question test for explainability/interpretability: "what happened?" (transparency), "how?" (explainability), "why?" (interpretability).

## Anti-patterns
- **Addressing characteristics in isolation**: Optimising one characteristic without considering the others can undermine overall trustworthiness (e.g., highly secure but unfair; accurate but opaque).
- **Confusing demographic balance with fairness**: Systems with balanced predictions may still be inaccessible to people with disabilities or may amplify systemic inequalities.
- **Assuming transparency implies accuracy or fairness**: A transparent system reveals its workings but is not thereby correct, private, or unbiased.

## Key Takeaways
1. All seven characteristics are socio-technical; purely technical measurement is insufficient.
2. Trustworthiness is a spectrum and is only as strong as the weakest characteristic in the specific deployment context.
3. Human judgement must set the specific metrics and threshold values for each characteristic; the framework does not prescribe them.
4. Privacy-enhancing techniques can reduce accuracy under data-sparse conditions; this tradeoff must be explicitly managed.
5. Bias management requires addressing all three categories (systemic, computational, human-cognitive), not just demographic representativeness.
6. Safety risks involving risk of serious injury or death require the most urgent prioritisation and most thorough risk management process.

## Connects To
- **NIST SP 1270**: Detailed treatment of the three categories of AI bias.
- **ISO/IEC TS 5723:2022**: Source definitions for validity, reliability, accuracy, robustness, and safe operation.
- **ISO 9000:2015**: Definition of validation used for the Valid and Reliable characteristic.
- **NIST Privacy Framework**: Companion resource for privacy-enhanced AI design.
- **NIST Cybersecurity Framework**: Applicable guidance for the Secure and Resilient characteristic.
- **MEASURE 2.5–2.11**: Subcategories that operationalise measurement of each trustworthiness characteristic.

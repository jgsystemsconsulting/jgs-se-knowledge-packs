# Chapter 6: MEASURE Function

## Core Idea
MEASURE operationalises AI risk assessment by applying quantitative, qualitative, or mixed-method tools to analyse, benchmark, and monitor the trustworthiness characteristics and social impacts identified in MAP; its outputs provide a traceable evidentiary basis for MANAGE decisions.

## Frameworks Introduced
- **MEASURE Function**: Four category groups (MEASURE 1–4) covering metric selection, trustworthiness evaluation, risk tracking, and measurement efficacy feedback.
  - When to use: Before deployment (to confirm readiness) and continuously in operation (to detect performance drift, emergent risks, and new harms).

## Key Concepts
- **MEASURE 1 (Methods and metrics selection)**: Measurement approaches are selected starting with the most significant risks; risks that cannot be measured are documented; appropriateness and effectiveness of controls are regularly assessed; independent or external assessors are involved.
- **MEASURE 1.1**: Measurement approaches and metrics for risks enumerated in MAP are selected, prioritised by significance; unmeasurable risks are explicitly documented.
- **MEASURE 1.3**: Internal experts who did not serve as front-line developers, and/or independent assessors, are involved in regular assessments.
- **MEASURE 2 (Trustworthiness evaluation)**: Each of the seven trustworthiness characteristics is evaluated through defined subcategories (MEASURE 2.1–2.13); covers TEVV documentation, human subject protections, production monitoring, validity, safety, security, transparency, explainability, privacy, fairness, environmental impact, and TEVV effectiveness.
- **MEASURE 2.5**: Deployed system is demonstrated valid and reliable; generalisability limitations beyond training conditions are documented.
- **MEASURE 2.6**: System is evaluated for safety risks; residual negative risk must not exceed tolerance; system must be able to fail safely.
- **MEASURE 2.11**: Fairness and bias evaluations are conducted and results documented.
- **MEASURE 2.12**: Environmental impact and sustainability of model training and management are assessed.
- **MEASURE 3 (Risk tracking)**: Mechanisms track existing, unanticipated, and emergent risks over time; alternative tracking approaches are used where standard metrics are unavailable; end-user feedback and appeal processes are integrated into evaluation metrics.
- **MEASURE 4 (Measurement feedback)**: Measurement approaches are validated against deployment context through domain expert consultation; measurable performance improvements or declines are identified and documented.
- **TEVV (Test, Evaluation, Verification, and Validation)**: Objective, repeatable, or scalable processes for confirming system trustworthiness; must adhere to scientific, legal, and ethical norms; conducted in an open and transparent process.
- **Uncertainty quantification**: Measurement processes must include measures of uncertainty alongside benchmark comparisons and formalised reporting.

## Mental Models
- Use MEASURE 2.x as a checklist against the seven trustworthiness characteristics: each characteristic has at least one corresponding measurement subcategory.
- Use independent review as a structural safeguard (MEASURE 1.3): internal bias and conflicts of interest reduce measurement validity; separation of assessors from builders mirrors TEVV best practice.
- Use traceable measurement as the basis for MANAGE decisions: where trustworthiness tradeoffs arise, measurement provides the evidentiary record needed for recalibration, mitigation, or system removal.

## Anti-patterns
- **Omitting documentation for unmeasurable risks**: If a risk cannot be measured, MEASURE 1.1 requires it to be explicitly documented — silent omission is not acceptable.
- **Single-point-in-time measurement**: AI systems can drift; ongoing production monitoring (MEASURE 2.4) is required, not just pre-deployment assessment.
- **Conflating lab measurements with deployment risk**: MEASURE 2.3 requires performance demonstrated under conditions similar to the deployment setting; lab-only metrics are insufficient.

## Key Takeaways
1. Start MEASURE with the highest-significance risks from MAP; do not attempt to measure everything at equal depth simultaneously.
2. Involve assessors who did not build the system (MEASURE 1.3); internal-only measurement is a governance risk.
3. Every trustworthiness characteristic (safety, security, fairness, privacy, explainability, etc.) has a corresponding measurement obligation in MEASURE 2.
4. Environmental impact (MEASURE 2.12) is an explicit measurement obligation, not an optional sustainability add-on.
5. End-user feedback and appeal mechanisms (MEASURE 3.3) are measurement infrastructure, not customer service; integrate them into evaluation metrics.
6. Measurement outcomes feed directly into MANAGE; without documented MEASURE outputs, risk prioritisation and response planning lack an evidentiary basis.

## Connects To
- **MAP function**: Identified risks and system categorisation from MAP are the direct inputs to MEASURE 1.1.
- **MANAGE function**: MEASURE outputs (metrics, benchmarks, tracked risks) are used by MANAGE to prioritise and respond to risks.
- **GOVERN function**: GOVERN compliance and evaluation requirements are integrated into MEASURE processes; GOVERN sets the risk tolerance thresholds against which MEASURE 2.6 (safety) is assessed.
- **ISO/IEC TS 5723:2022**: Definitions for validity, reliability, accuracy, robustness underpinning MEASURE 2.5.
- **NIST Cybersecurity Framework**: Security measurement approaches applicable to MEASURE 2.7.
- **NIST Privacy Framework**: Privacy risk measurement applicable to MEASURE 2.10.

# Chapter 2: The System Safety Process & General Requirements

## Core Idea
Section 4 of MIL-STD-882E defines the minimum mandatory requirements for any DoD system safety effort. The centerpiece is an eight-element iterative process (Figure 1) that spans the full life-cycle from concept through disposal. The process is closed-loop: iteration between elements is expected, and risk management does not terminate at fielding.

## Frameworks Introduced

- **Eight-Element System Safety Process**: the normative iterative loop for identifying, assessing, mitigating, and accepting risk.
  - When to use: applies to every defense system from concept through disposal; mandatory when Sections 3 and 4 are invoked.

- **System Safety Design Order of Precedence**: a five-level priority ranking for mitigation selection, used in Element 4.
  - When to use: whenever a hazard cannot be eliminated; the hierarchy must be applied in sequence from most to least effective.

- **Hazard Tracking System (HTS)**: the closed-loop database that records all hazard data, risk assessments, mitigation status, verification records, and formal risk acceptances.
  - When to use: from the first identified hazard through the end of the system's life-cycle; mandatory data element per 4.3.1.d.

## Key Concepts

- **Element 1 — Document the system safety approach**: PM and contractor document the risk management approach, including prescribed and derived requirements (IM, E3, CHMR, etc.), risk acceptance authority definitions, and HTS procedures.
- **Element 2 — Identify and document hazards**: systematic analysis covering hardware, software, human interfaces, operational environment, and entire life-cycle; uses mishap data, legacy lessons learned, health and environmental data.
- **Element 3 — Assess and document risk**: assign severity category (Table I) and probability level (Table II) for each hazard across all system modes; express as a Risk Assessment Code (RAC).
- **Element 4 — Identify and document risk mitigation measures**: select mitigations following the design order of precedence; estimate expected risk reduction; document all options in the HTS.
- **Element 5 — Reduce risk**: implement selected mitigations; evaluate cost, feasibility, and effectiveness through the SE/IPT process; present hazard status at technical reviews (SRR, PDR, CDR).
- **Element 6 — Verify, validate, and document risk reduction**: confirm implementation and effectiveness of mitigations through analysis, testing, demonstration, or inspection; document in HTS.
- **Element 7 — Accept risk and document**: formal risk acceptance by the appropriate authority per DoDI 5000 series before exposing people, equipment, or the environment to known hazards; user representative provides formal concurrence for all Serious and High risks.
- **Element 8 — Manage life-cycle risk**: continues after fielding; incorporates mishap reports, user feedback, configuration changes; any new or higher-risk hazard requires fresh formal acceptance.

## The Design Order of Precedence (Element 4 Detail)

Listed from most to least effective. Apply in this order; document rationale when a higher level is not feasible:

1. **Eliminate hazards through design selection** — remove the hazard by choosing an alternative design or material.
2. **Reduce risk through design alteration** — change the design to reduce severity and/or probability.
3. **Incorporate engineered features or devices** — add active interruption mechanisms or passive protective devices.
4. **Provide warning devices** — install detection and warning systems to alert personnel.
5. **Incorporate signage, procedures, training, and PPE** — lowest priority; for Cat I/II hazards, relying solely on this level should be avoided.

## Mental Models

- **Use the HTS as the single source of truth** when any hazard-related datum is disputed — it holds initial risk, target risk, event risks, mitigations, verification records, and the signed acceptance chain.
- **Use the design order of precedence as a forcing function** when stakeholders default to administrative controls; documented justification for skipping a higher-level option is required.
- **Use technical reviews as hazard-gate events** — the SRR, PDR, CDR, TRR, and PRR are the contractual moments at which hazard status must be presented to program leadership.

## Anti-patterns

- **Treating risk acceptance as a one-time event**: Element 7 explicitly requires re-acceptance after fielding if mishap data or configuration changes reveal higher risk than previously assessed.
- **System safety personnel owning other disciplines' hazard management**: Section 4.2.2 makes clear that system safety personnel are not responsible for hazard management in other SE functional disciplines. Each discipline owns its own risk acceptance.
- **Administrative controls as primary mitigation for Cat I/II hazards**: explicitly cautioned against in 4.3.4.e — "the use of signage, procedures, training, and PPE as the only risk reduction method should be avoided" for Catastrophic or Critical hazards.
- **Optimising mitigations for only one discipline**: 4.2.3 warns that mitigation measures optimised for one discipline may create hazards in others; cross-discipline coordination is mandatory.

## Key Takeaways

1. The 8-element process is iterative, not sequential — feedback loops between elements are normal and expected.
2. The HTS is the legal and contractual record; the Government retains "government purpose rights" over all HTS data.
3. Risk management does not end at fielding; Element 8 requires life-cycle-long vigilance and updated acceptance for any risk elevation.
4. User representative concurrence is legally required for all Serious and High risk acceptance decisions.
5. The design order of precedence is mandatory as a decision framework — skipping levels requires documented rationale.
6. The standard explicitly separates system safety personnel accountability from other SE disciplines; each discipline uses the methodology but manages its own risks.

## Connects To

- **Chapter 3 (Risk Assessment)**: Tables I–III operationalise Elements 3 and 7.
- **Chapter 5 (Task 100 — Management)**: Tasks 101–108 implement Element 1 (documenting the approach) and establish the HTS (Element 2).
- **Chapter 6 (Task 200 — Analysis)**: Tasks 201–210 implement Elements 2 and 3.
- **Chapter 7 (Task 300 — Evaluation)**: Tasks 301–304 implement Elements 5–7.
- **Chapter 8 (Task 400 — Verification)**: Task 401 implements Element 6.

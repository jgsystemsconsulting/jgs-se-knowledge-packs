# Chapter 16: 3.9 Project Phase F: Closeout

## Core Idea
Project Phase F closeout focuses on completing remaining tasks, archiving project data, capturing lessons learned, and transitioning the system to operational support — ensuring a formal, orderly conclusion that preserves institutional knowledge and enables future mission success.

## Frameworks Introduced
- **Compliance Matrix (NPR 7123.1 Appendix H)**: Structured tool for documenting program/project compliance with SE NPR requirements, tailoring rationales, and approved deviations.
  - When to use: Early in project planning and continuously through the lifecycle to manage requirement waivers and ensure stakeholder alignment.
- **NPR 7123.1 Tailoring Process**: Five-gate governance model for seeking relief from SE NPR requirements consistent with program objectives, risk posture, and constraints.
  - When to use: When a requirement is non-applicable, overly burdensome, or can be scaled to better balance implementation cost and project risk.
- **Project Type Classification (Type A–F)**: Six-tier mission taxonomy scaling from very-high-risk human spaceflight (Type A) to low-risk ground-based demonstrations (Type F).
  - When to use: At project inception to baseline documentation rigor, review formality, and SE process customization appropriate to mission complexity and risk tolerance.

## Key Concepts
- **Tailoring**: The process of seeking relief from SE NPR requirements through documented deviations or waivers, consistent with program/project objectives, allowable risk, and constraints.
- **Customization**: Modification of recommended SE practices to accomplish NPR requirements, not requiring waivers; significant customization should be documented in the SEMP.
- **Compliance Matrix**: Living document attached to the SEMP that records the program/project's approach to each NPR requirement (compliant, tailored, or non-applicable) with supporting rationales and approvals.
- **Designated Governing Authority (DGA)**: The approval body (typically Center Director or delegated authority) responsible for approving tailoring waivers and key technical documents in closeout.
- **Life-Cycle Cost Vigilance**: Continuous tracking of present and future costs; budgetary constraints in development that defer costs to operations increase total mission risk.
- **Risk Classification Level**: The baseline profile (per NPR 8705.4) that determines the rigor and extent of allowable tailoring (human-rated systems require stringent assurance; robotic missions allow greater relief).
- **Mission Lifetime**: Duration of operational service; longer-lived systems require stricter NPR adherence to ensure reliability and supportability.
- **Formality Scaling**: Adaptation of review entrance/exit criteria, RID/RFA processes, and audience size to match project scale (formal boards for Type A; tabletop sessions for Type F).

## Mental Models
- **Think of tailoring as "risk-based relief negotiation."** Each NPR requirement imposes assurance cost; tailoring grants relief only where mission risk tolerance and project characteristics justify it. The Compliance Matrix is the negotiated contract.
- **Use the six project types as a mental scaffold for proportionality.** A Type F suborbital demonstrator should require one-tenth the documentation and formality of a Type A human spaceflight program. If your project doesn't fit its assigned type, signal that in tailoring rationales.
- **View lifecycle cost as a debt instrument.** Cutting development budget by deferring work to operations compounds the risk burden and often increases total cost; vigilance via cost-tracking tools prevents this hidden cost growth.
- **Customization is free; tailoring is negotiated.** You can change *how* you implement a requirement (e.g., combine SRR and SDR) without a waiver if the intent of both is met. But if you want to *drop* a required review entirely, you need a waiver and governance approval.

## Anti-patterns
- **Blanket tailoring without risk posture clarity.** Tailoring every requirement equally because the project is "small" ignores which risks the project can actually bear. Without explicit stakeholder agreement on risk tolerance, tailoring lacks legitimacy and courts approval failure or mid-project reinstatement of strict requirements.
- **Ignoring lifecycle cost upstream.** Cutting development documentation and verification to meet a near-term budget cap often pushes high costs and risk to operations. Vigilance via cost-tracking tools and explicit lifecycle cost modeling is required to avoid this "false economy."
- **Customization without documentation.** Claiming "we'll customize our review approach" without recording it in the SEMP or Compliance Matrix creates ambiguity and makes independent assessments impossible. Even non-waiver customization should be explicitly captured.
- **Type misclassification.** Assigning a project to Type E (low-priority, high-risk) when it carries national significance or critical mission dependence invites approval rejection and audit findings. Tailoring criteria should anchor to defensible mission characteristics.
- **Approvals without rationale.** A Compliance Matrix entry that simply says "tailored" without explaining *why* the project can accept reduced assurance for that requirement fails to establish legitimate governance. Rationale must be explicit and traceable.

## Key Takeaways
1. **Tailoring is mandatory for all projects.** NASA policy recognizes that one-size-fits-all SE process is impossible. Every program/project must tailor NPR requirements to its specific objectives, risk, and constraints — and document that tailoring in the Compliance Matrix for governance approval.

2. **Eight factors determine tailoring scope.** Extent of allowable relief depends on mission type, criticality to the Agency Strategic Plan, risk tolerance, national significance, complexity, lifetime, cost, and launch constraints. These factors, taken together, justify the tailoring strategy and provide the basis for governance approval.

3. **Three tailoring approaches protect project flexibility without sacrificing rigor.** (a) Eliminate non-applicable requirements (e.g., contracts chapter for in-house development); (b) eliminate overly burdensome requirements where benefit does not justify cost; (c) scale requirements to match project size and risk (e.g., a Type F project may conduct a tabletop review instead of a formal review board).

4. **Customization of the 17 SE processes and review formality is not tailoring.** You can adjust *how* each process is implemented (rigor, timing, audience, documentation format) without a waiver. Only if you want to *eliminate* a required activity or skip a required review does a waiver apply. Record significant customization in the SEMP and Compliance Matrix for clarity.

5. **Compliance Matrix is the governance instrument.** Attach it to the SEMP. Record each NPR requirement, the program/project's approach (compliant, tailored, or non-applicable), the rationale, the risk owner, and approvals. This living document communicates tailoring to the entire team, allows independent assessors to adjust their criteria, and provides traceability for audit.

6. **Approval governance depends on scope.** If a Center is requesting standard tailoring for all projects at that Center, appendix H.1 is submitted to the NASA Office of Chief Engineer. If an individual program/project seeks waivers, appendix H.2 Compliance Matrix is used; the Center Director or designee approves. In both cases, the rationale and approvals are recorded in the SEMP.

7. **Project-type classification is a starting point, not a rigid assignment.** Table 3.11-1 and 3.11-2 show example tailoring for Types A–F. Many projects have characteristics of multiple types, so tailor by function: allow more customization/relief for simpler, lower-risk aspects; require stricter compliance for complex, high-risk aspects.

## Connects To
- **NPR 7123.1 (NASA Systems Engineering Requirements)**: The primary source of SE NPR requirements that are tailored via the Compliance Matrix; Appendices G and H provide guidance on review criteria and tailoring governance.
- **NPR 8705.4 (Risk Classification for NASA Payloads)**: Establishes baseline risk criteria for payload assignment to project types (human-rated, robotic, suborbital, etc.) that inform tailoring extent.
- **NPR 7120.5, 7150.2, 7120.7, 7120.8 (Governing project management directives)**: Define the lifecycle phases, required reviews, and documentation structure; tailoring of SE requirements must align with the governing directive for the project type.
- **SEMP (Systems Engineering Management Plan)**: The binding document that captures the tailored NPR requirements, customization approaches, risk posture, and governance approvals; Compliance Matrix is attached as evidence.
- **NASA Engineering Network Systems Engineering Community of Practice**: Provides templates for milestone review presentations and access to lessons learned on tailoring across NASA Centers.
- **Life-Cycle Cost Tools**: Project-level cost tracking and modeling (mentioned but not detailed in this section) are essential to the vigilance required to prevent deferring development costs to operations.

---

**Note:** This chapter synthesizes NASA's tailoring and customization framework from NPR 7123.1 guidance and the project-type classification examples provided. It bridges the gap between rigid SE policy and the practical reality that every NASA mission is unique; the Compliance Matrix is the institution's mechanism for asserting principled flexibility while maintaining governance oversight.

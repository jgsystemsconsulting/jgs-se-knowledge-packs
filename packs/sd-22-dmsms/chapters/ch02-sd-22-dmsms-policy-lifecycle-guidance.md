# Chapter — DMSMS Management Policy & Life-Cycle Guidance

## Core Idea

Diminishing manufacturing sources and material shortages (DMSMS) management is not an optional add-on; it is mandated by a layered body of DoD policy and woven into guidance across every phase of a system's life. The governing principle is that DMSMS work should be risk-based, proactive, and continuous — started early (even before development) and carried through to disposal, because defense systems live long while the technologies inside them age fast. This chapter maps the policy stack that requires DMSMS management, then traces how supporting guidance positions DMSMS activities phase by phase, inside systems-engineering and sustainment artifacts, and tailored across the different acquisition pathways.

A central caveat frames everything that follows: this is sustainment/obsolescence territory. The discipline exists because manufacturers stop making parts and materials disappear from the supply base, and those shortages threaten readiness, cost, and schedule long after a system is fielded. The policy and guidance described here are oriented toward preventing, forecasting, and resolving those obsolescence-driven shortages over a system's service life.

## Frameworks Introduced (exact source names, when/how)

The slice introduces a stack of named issuances and artifacts. Each is listed with what it is and how DMSMS attaches to it.

**High-level / cross-cutting policy:**

- **DoDI 4140.01, "DoD Supply Chain Materiel Management Policy"** — historically the home of DMSMS policy. It directs the PM, working through the PSM, to develop, fund, and execute a DMSMS management plan and to run proactive, risk-based management that finds current issues, forecasts future ones, budgets to resolve them, and carries the resolutions out. It also assigns DMSMS responsibilities to senior officials, including Defense Pricing and Contracting, USD(R&E), and DoD Component Heads (who must stand up programs to monitor and mitigate DMSMS and obsolescence risk).
- **DoD Manual (DoDM) 4140.01, Volume 3, "DoD Supply Chain Materiel Management Procedures: Materiel Sourcing"** — directs the Military Departments, MDA, and DLA to establish a standard DMSMS strategy and program that reduces the cost and schedule impact of identified problems and keeps DMSMS from degrading weapon-system readiness. Its Section 9 lays out DMSMS requirements, actions for minimizing impact, and resolution procedures.
- **DoDI 5000.91, "Product Support Management for the Adaptive Acquisition Framework"** — ties DMSMS into the Life-Cycle Sustainment Plan (LCSP), which it names as the primary management reference for support planning from program inception through disposal. A detailed LCSP must cover sustainment risks, supply chain risk management (SCRM), DMSMS risk management with mitigation plans, and engineering/design considerations including DMSMS resilience.
- **DoDI 5000.85, "Major Capability Acquisition"** — the issuance to which DMSMS-relevant general acquisition policy migrated from the former DoDI 5000.02. It frames a rapid, iterative approach intended to avoid technological obsolescence and lean on mature, proven technologies and commercial solutions.

**Stand-alone DMSMS policy (the centerpiece):**

- **DoDI 4245.15, "Diminishing Manufacturing Sources and Material Shortages (DMSMS) Management"** — issued November 5, 2020 as a dedicated, stand-alone DMSMS policy. It establishes risk-based proactive DMSMS management across the life cycle of all DoD items, requires evaluating designs and redesigns for potential DMSMS issues, mandates implementing resolutions to limit cost/schedule/readiness harm, and pushes continuous process improvement enterprise-wide. It assigns responsibilities across a long list of officials (USD(A&S), ASD for Acquisition, ASD(S), Industrial Policy, DCMA, USD(R&E), Component Heads, and the Service/agency directors) and defines procedures for program offices and other DMSMS management performing organizations (DMPOs).
- **DoDM 4245.15** — the companion manual to DoDI 4245.15. It expands the responsibilities and procedures and notably adds the DoD CIO, who must supply guidance on how cyber supply chain risk management affects DMSMS resolution for digital capabilities.

**Engineering policy and SE artifacts:**

- **DoDI 5000.88, "Engineering of Defense Systems"** — establishes the requirement for a Systems Engineering Plan (SEP) for MDAPs and ACAT II/III programs, and frames systems engineering as the disciplined approach spanning specification through retirement.
- **Systems Engineering Plan (SEP) Outline** — its Section 3 documents technical risk; the source recommends folding DMSMS into the SEP so it coordinates with other technical processes, and notes software obsolescence belongs in the software-development approach and feeds severability decisions in an open architecture.
- **Systems Engineering Guidebook** (OUSD(R&E)) — states that a program office should already have a DMSMS management plan and be mitigating obsolescence risk during low-rate and full-rate production. It also defines Systems Engineering Technical Reviews (SETRs) as the event-driven checkpoints where DMSMS posture is assessed.

**Sustainment artifacts and reviews:**

- **Life-Cycle Sustainment Plan (LCSP)** and its **Sample Outline** — the LCSP governs operations-and-support planning from inception to disposal and serves as the repository for product-support decisions; its Section 4.12.1, "Obsolescence Risk Management," is where DMSMS is addressed.
- **Independent/Integrated Logistics Assessment (ILA)** — an assessment of supportability planning, governed for the MCA pathway but recommended for all; the **Independent Logistics Assessment Guidebook** is the reference.
- **Sustainment Review (SR)** — required by **10 U.S.C. 4323**, conducted by each Military Department secretary within five years of a major program's IOC and every five years thereafter, assessing product-support strategy, performance, and O&S costs, and explicitly evaluating the effectiveness of DMSMS and parts-management content.
- Supporting product-support guidebooks: the **Integrated Product Support (IPS) Elements Guidebook**, the **Product Support Manager (PSM) Guidebook** (with its "Obsolescence/DMSMS Mitigation" content), and the **Product Support Business Case Analysis Guidebook** (whose analytic-tools table includes DMSMS/obsolescence tools).

**Acquisition pathway issuances (the Adaptive Acquisition Framework):**

- **DoDI 5000.81 (Urgent Capability Acquisition / UCA)**, **DoDI 5000.80 (Middle Tier of Acquisition / MTA)**, **DoDI 5000.85 (Major Capability Acquisition / MCA)**, **DoDI 5000.75 (Defense Business Systems / DBS)**, **DoDI 5000.87 (Software Acquisition / SWA)**, and **DoDI 5000.74 (Acquisition of Services)** — the six pathways. DMSMS management applies to five of them; the acquisition-of-services pathway is excluded.

## Key Concepts

**The policy hierarchy is layered, not singular.** Before 2020, DMSMS direction lived inside broad supply-chain and acquisition issuances. In November 2020 the Department added a dedicated instruction (DoDI 4245.15) plus its companion manual, while the older high-level policy stayed in force. So a program office answers to both the cross-cutting issuances and the stand-alone DMSMS policy at once, with Component-level policies layered on top — all of which the DMSMS Knowledge Sharing Portal (DKSP) collects in one place.

**Roles run from the deckplate to the OSD level.** The PM and PSM own the program-level duty to plan, fund, and execute DMSMS management. Above them, the policy stack distributes accountability: pricing-and-contracting officials enable timely contractual solutions, the engineering enterprise (USD(R&E)) supplies technical advice, the CIO addresses cyber-supply-chain effects on resolutions, and Component Heads must stand up monitoring-and-mitigation programs.

**Proactive, risk-based monitoring is the operating mode.** Across the policy and the phase guidance, the recurring instruction is to identify current issues, forecast future ones, and resolve them before they bite — using predictive tools, vendor surveys, and ongoing surveillance against the system's bill of materials (BOM). Risk-based means you do not watch everything equally: the proactive watch list concentrates on mission-critical, high-failure-rate, DMSMS-prone items that lack ready commercial substitutes.

**Design-out and preservation are early levers.** Even with only a preliminary parts list, a program can spot obsolete or near-obsolete parts and either design them out before they cause harm or decide what technical data, tooling, and insurance spares to preserve as a hedge. When obsolescence cannot be prevented, a vetted design at least lets the office prepare a cheaper mitigation strategy in advance.

**DMSMS lives inside SE and sustainment ceremonies.** It is not a parallel process. It is documented in the SEP, examined at each SETR (ASR, SRR, SFR, PDR, CDR, PRR), captured in the LCSP, and assessed during ILAs and SRs. The slice provides per-review expectations: planning initiated by ASR; strategy, roles, and contractor data requirements forming through SRR/SFR; the DMP developed by PDR; the DMP formally approved with active monitoring by CDR; and full monitoring, resolution, roadmaps, case management, and metrics by PRR.

**Functional obsolescence is the software-specific failure mode.** For custom software acquired through the SWA pathway, the concern shifts from a part you can no longer buy to software that no longer functions in context — triggered by changes to interfacing hardware/software, changes in policy on the software's use, or newly discovered cybersecurity vulnerabilities. The relationship is bidirectional: newly installed software can render other system elements functionally obsolete.

## Mental Models

**The DMP/DMT engine and its four scoping questions.** Regardless of pathway, every program office should have a DMSMS management team (DMT) executing a DMSMS management plan (DMP) built around a few basic questions: What is the system's expected life cycle? Which items warrant proactive monitoring? How much will the office rely on major suppliers to do DMSMS work? And — folding in supplier capability — can those suppliers actually identify and resolve issues in time and at acceptable cost? The answers decide what stays in-house versus what rides on suppliers, and they shape the contract language, which should be put in place as early as possible.

**Long life vs. short part-life — the squeeze.** The reason DMSMS exists as a discipline is the mismatch between a weapon system's long service life and the shrinking product life of its high-technology components. Extend a system's service life and the squeeze worsens. This model explains why early and continuous attention pays off and why service-life-extension decisions ripple straight into DMSMS planning.

**COTS shifts control to the supplier.** For commercial off-the-shelf assemblies, BOMs are usually unavailable, so the government cannot run deep DMSMS operations and instead leans on suppliers — who often retire obsolescence on their own as good business practice. For non-COTS items, the office typically wants tighter control. This COTS/non-COTS split is the lever for deciding how much DMSMS work the program performs versus oversees.

**Tailoring as a dial set by risk and time horizon.** MCA is the baseline; the other pathways are MCA's processes turned up or down. The dial is set by the system's hardware characteristics, its acquisition/sustainment strategy, how software-heavy it is, and the program's risk tolerance:
- **UCA** assumes a short life tied to a contingency, so DMSMS may be minimal and supplier-reliant; technology roadmaps are precautionary, mainly to confirm commercial viability and prepare for a possible life extension. A disposition analysis about one year into O&S decides terminate, continue, or transition to a program of record.
- **MTA** runs long enough (roughly five years of production plus operation) that obsolescence is expected; technology roadmaps move from precautionary to effectively mandatory because COTS electronics will age out during production and O&S.
- **DBS** is the most software-intensive hardware-associated pathway, closely tracks commercial practice, and minimizes customization; hardware DMSMS may nearly vanish under commercial cloud models, while refresh cycles are informed by technology and product roadmaps.
- **SWA** centers on functional obsolescence of custom software across its planning and execution phases.

**Monitor → assess → resolve, repeated against the BOM.** The recurring sustainment loop in the SETR, ILA, and SR tables is the same shape every time: monitor and survey for issues using predictive tools and vendor surveys against the BOM, assess whether and when an issue must be addressed (and whether to resolve at a higher assembly level), then determine and implement the resolution — all while folding technology roadmaps and refreshment strategies in, and capturing cases and metrics.

## Key Takeaways

- DMSMS management is mandatory and layered: high-level supply-chain and product-support policy (DoDI 4140.01, DoDM 4140.01 Vol. 3, DoDI 5000.91, DoDI 5000.85) plus a stand-alone instruction and manual (DoDI/DoDM 4245.15) issued in November 2020.
- The PM, through the PSM, owns the duty to develop, fund, and execute a DMP and to run proactive, risk-based management; accountability extends up through OSD-level officials and Component Heads.
- Start early and run continuously. Vetting even a preliminary parts list lets a program design out obsolescence, preserve the right data/tooling/spares, and pre-stage cheaper mitigations.
- DMSMS is embedded in existing artifacts and reviews rather than run separately: the SEP, the SETR sequence, the LCSP (Obsolescence Risk Management section), ILAs, and the statutory Sustainment Review under 10 U.S.C. 4323.
- It applies to five of the six pathways (all but Acquisition of Services); MCA is the baseline and the others are tailored by risk, time horizon, software intensity, and COTS reliance.
- For software (SWA), the dominant concern is functional obsolescence driven by interface changes, policy changes, or cybersecurity vulnerabilities — and it can flow in both directions.
- Roadmaps scale with pathway: precautionary for UCA, effectively mandatory for MTA, and central to refresh-cycle planning for DBS.

## Connects To

- **Chapter 1 (DMSMS fundamentals / overview):** this chapter supplies the policy and life-cycle scaffolding behind the foundational definitions; the four scoping questions and the proactive risk-based posture introduced here recur throughout the operational sections.
- **Sections 3–7 of SD-22 (DMSMS operational processes):** the policy and tailoring here point downstream — the pathway tailoring is explicitly described as adjusting the operational processes detailed in those later sections.
- **Appendices B and C of SD-22:** the DMSMS-related questions a program office uses to prepare for SETRs (Appendix B) and for ILAs/SRs (Appendix C) operationalize the review expectations summarized in this chapter.
- **Adaptive Acquisition Framework (DAU):** the six-pathway model and its issuances (DoDI 5000.74/.75/.80/.81/.85/.87) sit at the center of the tailoring discussion and connect to broader acquisition-policy packs.
- **Product-support and SE guidance ecosystem:** the IPS Elements Guidebook, PSM Guidebook, Product Support BCA Guidebook, SEP Outline, and Systems Engineering Guidebook are the connective tissue between DMSMS and the wider sustainment and engineering disciplines.

# Chapter 7 — Implementation Appendices: Assessment Tools, Industry Recommendations, Contracting, Pillar Considerations, and Workforce Development

> Source authority note: This chapter synthesizes the implementation appendices (A through E) of the current DoD guide *Implementing a MOSA in DoD Programs*. This guide is the standing authority and supersedes the 2013 Open Systems Architecture (OSA) guidebook; treat any older OSA-era guidance as historical context, not as the governing reference.

## Core Idea

The body of the guide tells a program *what* a Modular Open Systems Approach is and *why* to pursue it; these appendices supply the practitioner machinery for actually doing it. They answer four operational questions a program management office (PMO) faces once it has committed to MOSA: How do I measure modularity and openness objectively? How do I get industry to deliver it? How do I write it into a contract so it is enforceable and verifiable? And what concrete actions, pillar by pillar, turn the approach into a fielded system? The unifying premise is that modularity and openness are not declared, they are demonstrated — through service-specific assessment tools, traceable metrics, contract clauses tied to deliverable data, and a verification regime that ends in a conformance certification. A closing appendix addresses the human side: a workforce that understands MOSA from both the acquirer and supplier perspective is treated as a precondition for everything else.

## Frameworks Introduced (exact source names, when/how)

The appendices name a specific set of tools, models, statutes, and instructional artifacts. Each entry below gives the source name and how the guide positions it.

- **Program Assessment Rating Tool (PART)** — Appendix A's first assessment tool. It is adapted from the Program Assessment Rating Tool once run by the Office of Management and Budget (OMB), and the Army's MOSA Implementation Guide cites it as that service's assessment instrument. It walks the user through 24 scored questions covering MOSA planning, implementation, self-assessment, and reporting, recording each in four fields: progress/status, extent achieved, rationale narrative, and supporting evidence. It maps results against the Open Systems Joint Task Force's five legacy pillars (Modular Design, Key Interfaces, Open Standards, Conformance, Enabling Environment).

- **Open Architecture Assessment Tool (OAAT)** and its underlying **Open Architecture Assessment Model (OAAM)** — Navy-oriented instruments approved by ASN (RDA). The OAAT scores a weapon system's openness across two dimensions, Business/Programmatic and Technical, each rated 0–4, then plots the result on the OAAM to show current maturity and the path toward greater openness.

- **Key Open Subsystems (KOSS) tool** — developed by NAVAIR to flag which subsystems are most exposed to vendor lock through proprietary interfaces, so a program can target intellectual-property (IP) rights acquisition at the volatile components that matter rather than spending on the rest.

- **Systems Engineering Assessment Model (SEAM)** — an Air Force self-assessment and independent-validation model covering ten standard SE process areas (configuration management; decision analysis; design; manufacturing; project planning; requirements; risk management; transition, fielding, and sustainment; technical management and control; verification and validation). The guide is explicit that SEAM checks whether SE work products exist, not whether the delivered outcome satisfies the customer.

- **MOSA Reference Frameworks in Defense Acquisition Programs (2020)** — cited in Appendix C as the reference describing Government Reference Architectures and their use.

- **Government Reference Architecture (GRA)** — a standardized architecture adopted at subsystem, system, program, or enterprise level to express the Government's desired modularity. Named examples are the Future Airborne Capability Environment (FACE), a government-industry collaboration, and the Ground Combat Systems Common Infrastructure Architecture (GCIA).

- **Statutory anchors** — Appendix C grounds contracting practice in law: 10 U.S.C. 3771 (identifying modular system interfaces and acquiring Government purpose rights in interface technical data), 10 U.S.C. 4401 (defining bolded terms used in the sample contract language), the NDAA FY 2021 Section 804 definition of "desired modularity," and DFARS 252.227 for protecting industry IP. It flags that the enforcement of interface-data rights awaits finalization of DFARS rulemaking case 2021-D005.

- **Contract instruments and their DIDs** — the Open System Management Plan (OSMP, DID DI-MGMT-82099), the Systems Engineering Management Plan (SEMP, DID DI-SESS-81785), and the Digital System Model (DSM, DID DI-SESS-82364). Sample Statement of Work (SOW) language ties deliverables — Contract Data Requirements Lists (CDRLs) backed by Data Item Descriptions (DIDs) — to specific WBS and GRA node levels of indenture.

- **The five OUSD(R&E) MOSA pillars** — Appendix D's organizing framework, developed by OUSD(R&E)-led working groups: Enabling Environment, Modular Design, Designated Interfaces, Consensus-Based Open Standards, and Certifying Conformance. (Note this differs from the older five-pillar set PART uses — see Anti-patterns.)

- **Defense Technical Risk Assessment Methodology, Criteria Volume 6.3 (2020)** — cited as the framework for technical risk assessment supporting Independent Technical Risk Assessments, milestone-readiness decisions, and reviews of SEPs, TEMPs, and Program Protection Plans across all acquisition pathways.

- **Multi-Attribute Utility Theory (MAUT)** — the scoring method OUSD(R&E) recommends for trading off MOSA objectives quantitatively, drawing on the *OUSD(R&E) MOSA Assessment Criteria* (May 2022). The guide notes that although commercial off-the-shelf (COTS) MAUT tools exist, a simple spreadsheet is often the preferred vehicle.

- **FAA COTS Risk Mitigation Guide (2002)** — cited in Appendix B for mitigating the risk that MOSA-driven design changes to existing COTS or platform components trigger costly regression testing or recertification.

- **DAU CLE 019 — Modular Open Systems Approach**, plus the ETM and TST course families and the "Let's Be Modular and Open" webinar series — Appendix E's workforce-development offerings.

## Key Concepts

**Measure what you mean to manage.** Appendix A opens by insisting PMOs measure modularity and openness with purpose-built MOSA metrics and tools, and that the right metric depends on which benefits the primary stakeholder actually wants. There is no single universal openness score; the assessment instrument is chosen to fit the program's MOSA objective and the level (system of systems, system, or below) at which modularity is being applied.

**Business openness and technical openness are distinct axes.** The OAAT formalizes this by scoring Business/Programmatic openness (processes and documentation used to acquire and manage the system) separately from Technical openness (features of the computing environment and application software). The technical axis decomposes into the design tenets of interoperability, maintainability, extensibility, composability, and reusability. A program can be technically modular yet programmatically closed, or vice versa — the two-dimensional rating makes that gap visible.

**Vendor lock is a targeting problem.** The KOSS logic is that not every component is worth buying rights to. Some components turn over or face obsolescence far more often than others, and a sole-source vendor for one of those becomes a de facto monopolist who can charge excess prices and may even deliver inferior solutions versus the open market. KOSS directs IP-rights spending to those high-volatility, lock-prone interfaces and lets a program ignore the rest.

**MOSA requirements flow down by law, then by service, then by program.** Appendix B and C describe a chain: Title 10 U.S.C. statute → DoD-wide implementation → service-specific guidance → PEO-specific guidance → program acquisition office. A MOSA-based SOW should reflect that flow-down, and suppliers must in turn receive modeling conventions — modeling patterns, domain-overlay profiles, interface and analysis definitions, templates and schemas, evaluation/scoring criteria, CDRLs and DIDs, and requirements schemas — so the Government can evaluate and validate a supplier's response.

**Desired modularity is a deliberate cost-benefit choice, not a maximum.** Appendix C frames modularity as a spectrum running from no modularity to near-microscopic modularity. More modularity buys flexibility, supportability, and future savings but can cost technical performance, price, or OEM goodwill. The PMO determines the *desired* level by integrating the SEP, Acquisition Strategy, IP strategy, sustainment strategy, and a cost-benefit analysis — picking a point on the spectrum rather than pushing the slider to the extreme.

**Contract enforceability rides on deliverable data.** The recurring contracting message is that MOSA cannot be implemented without acquiring the interface data and IP rights to back it, per an IP strategy. The mechanism is CDRLs supported by DIDs; omitting them risks both not receiving needed data and, on FAR/DFARS contracts, losing the ability to invoke DFARS data-rights clauses. The sample SOW even constrains the delivered DSM so it cannot alter the GRA's designated modular system interfaces or the HWCIs/CSCIs the Government has marked as modular systems and major system components.

**Non-FAR pathways do not get data rights for free.** A specific caution: Other Transaction Authorities (OTAs) and other non-FAR tools do not automatically carry the DFARS data-rights mechanisms, including rights in interface data — yet the statutory requirement to implement MOSA still applies. Acquisition planners must build equivalent data-requirement and agreement terms by hand.

**Specify modularity before the RFP, not after award.** A best-practice theme across Appendices C and D is front-loading. The OSMP (DI-MGMT-82099) is traditionally received and evaluated only after award; the guide recommends instead requesting a draft or initial OSMP in the proposal so the Government can evaluate how well the offeror's modularity aligns with the Government's pre-stated desired modularity and interfaces. The same "decide before solicitation" logic runs through the pillar guidance.

**The five OUSD(R&E) pillars, operationalized.** Appendix D turns each pillar into concrete actions:
- *Enabling Environment* — the largest set, covering MOSA goals, agile/CI-CD development culture, digital engineering practice under DoDI 5000.97, IP/data-rights strategy, traceability from user requirements into the System Requirements Document and T&E, technical risk management, and recording intent in a MOSA-enabled SEP or Simplified Acquisition Management Plan. It explicitly invokes Conway's Law (1968) — that a system's structure mirrors the communication structure of the organization that builds it — as the rationale for aligning organizational structure with the desired modular architecture.
- *Modular Design* — five sub-functions: scalable reusable self-contained modules; failure isolation so a failed module degrades only its own service; technology-independence with the interface as the only constant; immutable/disposable modules deployable identically everywhere; and least-privilege execution.
- *Designated (Key) Interfaces* — identify interfaces and define their physical, syntactic, semantic, and behavioral boundaries; rank by criticality; create an Interface Management Plan; assign interface ownership; apply unique naming; trace interface requirements; document in ICDs and IRSs; and stand up Interface Control Working Groups (ICWGs) to coordinate.
- *Consensus-Based Open Standards* — prioritize internationally recognized or Government-owned standards; standardize interfaces to the maximum feasible extent; expose services via APIs; align IT standards to the DoD IT Standards Registry (DISR); and use FIPS 140-2-certified encryption at secure interfaces.
- *Certifying Conformance* — establish MOSA Measures of Effectiveness (MOEs) and Measures of Performance (MOPs), use verification checklists, apply the conformance criteria and verification methods of Table D-1, run V&V mechanisms (documentation validation, modularity verification, tool-development verification), and fold MOSA into T&E plans.

**Quantitative scoring via MAUT.** Conformance certification is backed by a numeric method: MAUT handles trade-offs among the pillars, which can be equally weighted or — more often — weighted by service and program need. The benefit/performance score is only half the picture; a complete evaluation pairs it against life-cycle cost in a cost/benefit analysis, an approach OUSD(R&E) validated in a proof-of-concept on an active program.

**Workforce as precondition.** Appendix E treats trained people as foundational. Training must cover MOSA from both business and technical angles, present real implementation examples, and explain MOSA's bearing on IP, data, and data rights. DAU's CLE 019 course (with its six instructional units from MOSA evolution through assessment) is offered as a template, supplemented by ETM and TST courses and the modular-and-open webinar series.

## Mental Models

**Two-axis openness scorecard.** Picture openness as a 2D plot with a business/programmatic axis and a technical axis, each graduated 0–4 (the OAAM rendering). A program is a point on that plane, and improvement is movement toward the upper-right. This guards against the trap of celebrating a clean technical architecture that sits behind closed business practices.

**The volatility-weighted lock map.** Borrowing the KOSS view, imagine the system as a parts list with two dials per component: how often it churns, and how locked-in its supplier is. The components where both dials are high are where Government IP-rights money should go. Everywhere else, conserve resources.

**The statutory funnel.** MOSA obligations pour in at the top from Title 10, narrow through DoD-wide and service guidance, narrow again through PEO guidance, and exit as specific SOW tasking and CDRLs at the bottom. If a program's contract language can't be traced back up this funnel, it isn't grounded.

**Modularity as a dial, not a switch.** Rather than "modular or not," hold the image of a continuous slider from monolithic to near-microscopic granularity, with a cost curve rising as you turn it up and a benefit curve that does not rise forever. The PMO's job is to find the economically optimal setting for *this* system, documented through the integrated SEP/Acquisition Strategy/IP strategy and a cost-benefit analysis.

**Conway's mirror.** Treat the org chart as a draft of the architecture. Because communication structures imprint themselves on the system, a PMO that wants a modular, loosely coupled system must first arrange its own teams and collaboration patterns to match — otherwise the delivered architecture will quietly inherit the seams of the organization.

**Measured-then-acted gets done.** The industry-recommendations refrain — that what is measured, analyzed, and acted upon is what actually happens — is the through-line connecting the assessment tools (Appendix A) to the conformance certification and MAUT scoring (Appendix D). Metrics are not reporting overhead; they are the control loop.

## Anti-patterns

The source names or warns against the following failure modes:

- **Mistaking work-product existence for delivered value.** The guide states plainly that SEAM assesses whether SE work products are present, not whether the customer-facing outcome was achieved. Treating a full document set as proof of a good system is a category error the guide flags.

- **Acquiring data and rights without a MOSA strategy.** Buying technical data and IP rights "without any thought to MOSA," per Appendix C, is possible but tends to raise costs and erode the very benefits MOSA was meant to deliver. The fix is an IP strategy integrated with the Acquisition Strategy.

- **Omitting CDRLs and DIDs.** Leaving deliverable-data requirements out of the contract puts a program at risk of not receiving the data it needs and, on FAR/DFARS contracts, of being unable to invoke DFARS data-rights clauses.

- **Assuming non-FAR vehicles carry data rights automatically.** Using OTAs while assuming DFARS interface-data-rights tools come along for the ride — they do not, even though the MOSA mandate still applies.

- **Forcing MOSA changes onto stable COTS or platform baselines.** When a MOSA implementation leans heavily on off-the-shelf components or complete systems, design changes can trigger substantial regression testing or recertification of the base platform, negating the projected benefit. The guide points to the FAA COTS Risk Mitigation Guide for flexible-requirements, COTS-testing, and configuration-management countermeasures.

- **Deferring modularity definition to post-award OSMP evaluation.** Receiving and judging the OSMP only after contract award is the historical default the guide pushes back on; it recommends evaluating a draft OSMP against pre-stated desired modularity before award.

> Caveat on pillar drift: the appendices carry two different five-pillar lists — the legacy Open Systems Joint Task Force pillars that PART scores against (Modular Design, Key Interfaces, Open Standards, Conformance, Enabling Environment) and the current OUSD(R&E) pillars (Enabling Environment, Modular Design, Designated Interfaces, Consensus-Based Open Standards, Certifying Conformance). They overlap heavily but are not identical; for current programs, the OUSD(R&E) set is the governing framework, consistent with this guide superseding the 2013 OSA guidebook.

## Key Takeaways

1. **Pick the assessment tool to fit the stakeholder's desired benefit and the level of application** — PART (Army), OAAT/OAAM (Navy), KOSS (NAVAIR), and SEAM (Air Force) each serve different needs and the choice is deliberate.
2. **Score business and technical openness separately**, each 0–4, so a programmatically closed-but-technically-modular program is exposed rather than masked.
3. **Target IP-rights acquisition at the volatile, lock-prone interfaces** (the KOSS logic) instead of buying rights everywhere.
4. **Trace MOSA contract language up the statutory funnel** from Title 10 through DoD, service, and PEO guidance to specific SOW tasking and CDRLs.
5. **Treat desired modularity as a cost-benefit-optimized point on a spectrum**, decided through an integrated SEP, Acquisition Strategy, IP strategy, and cost-benefit analysis — not as a maximum.
6. **Anchor enforceability in deliverable data**: CDRLs backed by DIDs, with the DSM constrained so it cannot alter GRA-designated interfaces or designated modular systems and components.
7. **Front-load specification**: state desired modularity and identify modular system interfaces before RFP release, and evaluate a draft OSMP rather than waiting until after award.
8. **Operationalize all five OUSD(R&E) pillars**, ending in a Certify-Conformance regime with MOEs/MOPs, the Table D-1 criteria, V&V mechanisms, and MAUT scoring paired with life-cycle cost.
9. **Remember Conway's Law** — align the organization's communication structure with the intended modular architecture, or the architecture will inherit the org's seams.
10. **Invest in a MOSA-literate workforce** (DAU CLE 019 and the ETM/TST curriculum) as a precondition, covering both business and technical perspectives and MOSA's bearing on IP and data rights.

## Connects To

- **The MOSA pillars and benefits chapters** of this same guide (Section 2.1 and the body), which these appendices operationalize — Appendix D's pillar actions are the execution layer beneath the conceptual pillar treatment.
- **Digital engineering and MBSE practice** — the Digital System Model (DI-SESS-82364), DoDI 5000.97 digital-engineering policy, and the requirement for a scriptable SysML-capable API to interoperate with the GRA. Relevant to MBSE and SysML knowledge packs.
- **DoD acquisition policy and contracting** — the 5000-series instructions, FAR/DFARS data-rights framework, DFARS 252.227, OTAs, and the source-selection/Section L–M structure; ties into acquisition and program-management packs.
- **Technical risk assessment** — the Defense Technical Risk Assessment Methodology (Volume 6.3) and Independent Technical Risk Assessments, linking MOSA conformance to milestone-readiness and SETR reviews (GAO TRA and DoD T&E packs).
- **Workforce and SE curricula** — DAU CLE 019, ETM mission-and-systems-thinking and design-considerations courses, and TST T&E courses, connecting to the DAU SE Guidebook and broader SE-standards landscape.
- **Standards and interoperability** — DISR alignment, FIPS 140-2 encryption, consensus-based open standards, and ICWG governance, which connect to interface-management and open-architecture material elsewhere in the SE canon.

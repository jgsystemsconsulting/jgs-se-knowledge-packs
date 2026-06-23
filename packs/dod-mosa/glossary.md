# DoD MOSA Glossary

Key terms from the OUSD(R&E) *Implementing a MOSA in DoD Programs* guidebook (Feb 2025), alphabetical, with chapter references. Definitions are synthesized in original words, not reproduced from the source.

**10 U.S.C. 4401–4403** — the Title 10 statutory framework that makes MOSA a requirement: §4401 sets the mandate and key definitions for MDAPs, §4402 ties MOSA to capabilities development and weapon-system design, §4403 covers modular-interface availability and MOSA support. (Ch 1)

**Acquisition Strategy** — the program artifact that must state where, why, and how MOSA is applied; it differentiates the major system platform from its major system components and covers IP, data deliverables, and configuration management. (Ch 3, Ch 6)

**Adaptive Acquisition Framework (AAF)** — the umbrella structure organizing the Defense Acquisition System into six pathways; MOSA applies across all of them, varying only in how formally it is mandated. (Ch 6)

**Analysis of Alternatives (AoA) / Economic Analysis** — the comparison of operational effectiveness, suitability, and life-cycle cost across candidate solutions; each option's assessment should describe how MOSA would be realized. (Ch 3)

**API-first design** — the practice of defining a software component's Application Programming Interface before its internals, emphasizing modularity, scalability, and reusability. (Ch 4)

**ASSIST / MOSS** — the defense repository of specifications, standards, handbooks, and data item descriptions (assist.dla.mil); its Modular and Open Standards and Specifications (MOSS) area holds MOSA-specific guidance. (Ch 4)

**Business architecture** — the contracting, legal, and data-rights half of MOSA that must accompany the technical architecture; a clean interface the Government cannot legally exploit is not a MOSA success. (Ch 1)

**Certify Conformance (pillar)** — the fifth OUSD(R&E) pillar: verify and validate that the implementation actually conforms to the selected open interface standards. (Ch 2, Ch 7)

**Conway's Law** — the principle that a system's structure mirrors the communication structure of the organization that builds it; cited as the reason to align team structure with the intended modular architecture. (Ch 7)

**Consensus-Based Open Standards (pillar)** — the fourth OUSD(R&E) pillar: standardize modular interfaces using openly, consensus-developed standards and manage Government-owned interface repositories. (Ch 2, Ch 7)

**COTS (commercial off-the-shelf)** — commercial components whose use under MOSA needs an up-front business case analysis, because a design change can trigger costly regression testing or recertification of the base platform. (Ch 4, Ch 7)

**Data rights** — the IP rights (per DFARS 252.227) that must be sufficient for the Government to use an interface for its intended purpose; without them, architectural modularity cannot be exercised. (Ch 1, Ch 7)

**Desired modularity** — the deliberately chosen point on the modularity spectrum (from none to near-microscopic), set by integrating the SEP, Acquisition Strategy, IP strategy, sustainment strategy, and a cost-benefit analysis — not pushed to a maximum. (Ch 7)

**DFARS** — the Defense Federal Acquisition Regulation Supplement; the regulatory layer that translates the MOSA statute into policy and clauses (e.g. Part 207.106, 227.7203-2, and clauses 252.227-7013/-7015/-7018). (Ch 1)

**DMSMS** — Diminishing Manufacturing Sources and Material Shortages; the obsolescence risk that complicates technology insertion, mitigated by multi-vendor sourcing through open interfaces and by involving DMSMS practitioners early. (Ch 5)

**Employ a Modular Design (pillar)** — the second OUSD(R&E) pillar: identify each component's functionality before the RFP so business and technical objectives drive the partitioning. (Ch 2)

**Enabling Environment (pillar)** — the first OUSD(R&E) pillar: put the requirements, business practices, strategies, and T&E methods in place before design decisions harden. (Ch 2, Ch 7)

**FACE / OMS** — the Future Airborne Capability Environment and Open Mission System: named prescriptive, consensus-based integration standards; FACE is also cited as an example Government Reference Architecture. (Ch 4, Ch 7)

**Government Reference Architecture (GRA)** — a standardized architecture adopted at subsystem, system, program, or enterprise level to express the Government's desired modularity (examples: FACE, GCIA). (Ch 7)

**Interface** — the boundary across which modules exchange data, signals, or commands; the unit of openness — a module is only as open as its interface is clear, standardized, and maintained. (Ch 3)

**Interface Control Document (ICD) / Interface Requirements Specification (IRS)** — the high-value supporting artifacts that capture how standardized interfaces work and how components interact. (Ch 3, Ch 7)

**JCIDS** — the Joint Capabilities Integration and Development System; MOSA should enter its outputs (CBA, the initial-capabilities and capability-development documents) early, per CJCSI 5123.01. (Ch 3)

**Key Open Subsystems (KOSS)** — a NAVAIR tool that flags which subsystems are most exposed to vendor lock so IP-rights spending targets the volatile, lock-prone interfaces. (Ch 7)

**Major system component / interface** — terms from the FY 2017 NDAA naming the severable components and the interfaces between them; the FY 2021 NDAA added *modular system interface*. (Ch 1)

**MAUT (Multi-Attribute Utility Theory)** — the OUSD(R&E)-recommended scoring method for trading off MOSA objectives quantitatively, paired against life-cycle cost in a cost-benefit analysis. (Ch 7)

**MIL-STD-881F** — the mandatory product-oriented Work Breakdown Structure standard for DoDI 5000.02 programs; anchors the MOSA taxonomy for hardware and software. (Ch 4)

**MIL-STD-196G** — the system-naming taxonomy (System, Subsystem, Centers, Centrals, Sets, Group, Units) used to pick consistent levels of modularity. (Ch 4)

**Milestone Decision Authority (MDA)** — the official who, for an MDAP using MOSA, confirms that the EMD and P&D solicitations describe the approach and identify the minimum major system components. (Ch 6)

**Modular Open Systems Approach (MOSA)** — a combined acquisition and design approach pairing a technical and a business architecture around interfaces that conform to widely supported, consensus-based standards, enabling severable components to be added, removed, or swapped. (Ch 1, Ch 2)

**Modular system interface** — the FY 2021 NDAA term for an interface that must either comply with publicly disclosed standards or be delivered with machine-readable documentation per Government requirements. (Ch 1)

**MOSWG / TSWG** — the Modular Open Systems Working Group and the DoD MOSA Technical Standards Working Group: standing governance bodies that lead MOSA guidance, training, and standards identification. (Ch 6)

**OAAT / OAAM** — the Navy Open Architecture Assessment Tool and its underlying model, scoring openness on a Business/Programmatic axis and a Technical axis, each rated 0–4. (Ch 7)

**PART (Program Assessment Rating Tool)** — an Army-cited assessment instrument adapted from an OMB tool; walks through 24 scored questions and maps results against five legacy openness pillars. (Ch 7)

**Profile** — a constraint set that pins down a standard's optional variability so that two implementations of the same standard actually interoperate. (Ch 4)

**Program Capability Document (CDD)** — the capability-requirements artifact (KPPs, KSAs, APAs) that should present MOSA as an enabler for meeting those requirements. (Ch 3)

**SEAM (Systems Engineering Assessment Model)** — an Air Force self-assessment model covering ten SE process areas; it checks whether SE work products exist, not whether the delivered outcome satisfied the customer. (Ch 7)

**Systems Engineering Plan (SEP)** — the plan that defines the MOSA technical approach (applied to the maximum extent practicable), describes the architecture and its modular interfaces, and gives rationale where MOSA is not feasible. (Ch 3)

**Technology refresh / insertion** — the substitution of newer or alternative technology behind stable open interfaces; one of the five MOSA benefit classes and a primary motivation for modularity. (Ch 5)

**WBS as MOSA taxonomy** — the Work Breakdown Structure used as an architectural taxonomy so severable major components and modules can be added, removed, or replaced over the life cycle (Table 3-1). (Ch 4)

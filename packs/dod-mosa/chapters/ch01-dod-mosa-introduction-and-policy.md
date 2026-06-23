# Chapter — Introduction: MOSA Definition, Congressional Direction, and DFARS Policy

> **Source authority note:** This chapter reflects the current OUSD(R&E) SE&A guidebook *Implementing a MOSA in DoD Programs*, which is the present authority and supersedes the older 2013 Open Systems Architecture (OSA) guidebook. Where prior practice and current statute diverge, follow the statutory framework described here.

## Core Idea

A modular open systems approach (MOSA) is no longer just a recommended engineering practice in the U.S. Department of Defense — it is a statutory and regulatory requirement. The guidebook frames MOSA as a combined acquisition and design approach: a paired technical and business architecture that leans on system interfaces conforming to widely supported, consensus-based standards, used wherever such standards exist and fit the need. The intent is a system whose severable components can be added, removed, or swapped incrementally across the life cycle, opening the door to greater efficiency, competition, and innovation.

The chapter's central message is that recent law and DoD policy now *compel* MOSA rather than merely encourage it. What was once an established but discretionary practice has become a baseline expectation, anchored in Title 10 of the U.S. Code and reinforced through the Defense Federal Acquisition Regulation Supplement (DFARS). Programs are expected to integrate technical interface requirements with the contracting mechanisms and legal considerations — particularly data rights — needed to actually realize modularity in practice.

## Frameworks Introduced (exact source names, when/how)

- **Modular Open Systems Approach (MOSA)** — introduced in §1.1 as an acquisition and design approach pairing a technical architecture with a business architecture, both oriented around interfaces compliant with widely supported, consensus-based standards. The guidebook itself focuses on the technical (including programmatic) facet of MOSA.
- **10 U.S.C. 4401–4403** — the governing statutory framework, introduced in §1.2. Section 4401 sets the MOSA requirement and definitions for major defense acquisition programs (MDAPs); §4402 requires MOSA to be addressed during capabilities development and weapon-system design; §4403 covers availability of modular system interfaces and support for MOSA.
- **FY 2017 National Defense Authorization Act (NDAA)** — cited in §1.2 as the law that began updating Title 10 in response to acquisition-agility concerns, directing MOSA in any MDAP reaching Milestone A or B approval after January 1, 2019, and introducing the terms *major system component* and *major system interface*.
- **FY 2021 NDAA, Section 804** — described in §1.2 as amplifying and partly reconceptualizing MOSA, introducing the term *modular system interface* and a stronger emphasis on interface data, interface repositories, and Government-defined modularity requirements.
- **Defense Federal Acquisition Regulation Supplement (DFARS)** — introduced in §1.3 as the regulatory layer that establishes MOSA policy alongside the statute. Specific parts named: **207.106** (use of modular, open architectures to enable competition for upgrades) and **227.7203-2** (considering alternatives to delivering source code and software design details to meet Government needs).
- **DFARS rulemaking case 2021-D005** — named in §1.3 as the vehicle codifying common MOSA terminology, affecting DFARS clauses **252.227-7013, 252.227-7015, and 252.227-7018**, and implementing NDAA sections 804 (FY 2021), 809 (FY 2017), and 815 (FY 2012).
- **DFARS 252.227 (data rights)** — referenced in §1.2 as the basis for ensuring data rights are sufficient to use interfaces for their intended purpose.

## Key Concepts

- **MOSA is both technical and business.** Modularity is not achieved by architecture alone; it requires aligning interface engineering with contracting mechanisms and legal/data-rights considerations so the Government can actually compete, replace, and sustain components.
- **Severable, swappable components.** A MOSA structure is defined by components that can be incrementally added, removed, or replaced across the life cycle — the structural property that delivers efficiency, competition, and innovation.
- **The "maximum extent practicable" mandate.** The FY 2021 NDAA expanded MOSA from MDAPs specifically to *all* defense acquisition programs, qualified by the phrase "to the maximum extent practicable." This is now reflected in 10 U.S.C. 4401, tying MOSA to incremental development and to enhancing competition, innovation, and interoperability.
- **Milestone trigger.** Under the FY 2017 NDAA framing, MOSA applies to MDAPs receiving Milestone A or Milestone B approval after January 1, 2019.
- **Interface compliance and machine-readable documentation.** Title 10 requires a program's modular system interfaces to either comply with publicly disclosed or widely known standards, or be delivered per Government requirements with machine-readable documentation, including functional descriptions adequate to interconnect with publicly disclosed interfaces or with documentation held in Government interface repositories.
- **Interface repositories.** The FY 2021 NDAA added requirements for DoD to stand up MOSA interface repositories and to issue regulations governing authorized access and use of those interfaces — including by non-U.S.-Government parties — to support the statutory objectives.
- **Data rights as an enabler.** Per DFARS 252.227, data rights must be sufficient for the intended use of the interfaces; without adequate rights, the modularity the architecture promises cannot be exercised. DFARS 227.7203-2 specifically points toward weighing alternatives to delivering proprietary source code where technical data or software sufficient for a modular approach will meet the Government's needs.
- **Avoiding proprietary lock-in.** The stated objective is defense systems and components that are modular and readily interoperable — with each other and with new or improved systems — and not hemmed in by proprietary connections.

## Mental Models

- **Statute → regulation → contract chain.** Think of MOSA authority as cascading: 10 U.S.C. 4401–4403 sets the law, the DFARS translates it into acquisition policy and clauses, and the program's RFP and contract language operationalize it. A break anywhere in that chain — especially insufficient data rights — undermines the whole.
- **Modularity as a competition lever.** The recurring theme is that modular interfaces exist to keep the door open for competition and upgrades over the life cycle. If a design choice closes that door (proprietary connection, missing data rights), it works against the statutory intent even if it "works" technically.
- **Two architectures, one system.** Hold the technical architecture and the business architecture in mind simultaneously. A clean interface that the Government cannot legally exploit is not, in MOSA terms, a success.
- **Evolving landscape, monitor continuously.** Treat the statutory and regulatory picture as a moving target. The guidebook explicitly frames the DFARS as still evolving (e.g., renumbering of 10 U.S.C. 2320 to 3771, and 2446a to 4401), so practitioners should track updates rather than assume the citations are static.

## Anti-patterns

The source explicitly cautions on terminology drift:

- **Using non-statutory terms without anchoring them to statute.** Non-statutory terms are not prohibited in contracts or agreements, but if used, they must be tied back to statutory terms so that MOSA efforts and MOSA-compliant systems actually satisfy the legally mandated requirements.
- **Treating "key interface" as if it were a statutory term.** The guidebook calls out *key interface* as having historical and practical value but lacking definition in current law. Not every interface is "key," and not every interface is a *modular system interface*; conflating the two creates compliance gaps. When such legacy terms appear in contracts, they must be defined and explicitly connected to statutory MOSA requirements.

## Key Takeaways

- MOSA has shifted from a long-standing but discretionary DoD practice to a mandated one, driven by statute and DoD policy.
- The governing authority is 10 U.S.C. 4401–4403, with 4401 (requirement and definitions), 4402 (capabilities development and weapon-system design), and 4403 (interface availability and MOSA support).
- The FY 2017 NDAA first directed MOSA for MDAPs at Milestone A/B after January 1, 2019, and introduced *major system component* and *major system interface*; the FY 2021 NDAA Section 804 added *modular system interface*, emphasized interface data and repositories, and expanded the mandate to all acquisition programs to the maximum extent practicable.
- The DFARS reinforces the statute: Part 207.106 promotes modular, open architectures for upgrade competition; Part 227.7203-2 weighs alternatives to delivering proprietary source code; and rulemaking case 2021-D005 codifies common terminology across DFARS clauses 252.227-7013, -7015, and -7018.
- Adequate data rights under DFARS 252.227 are essential — interfaces and their documentation must be usable for the Government's intended purpose, with machine-readable documentation where interfaces are not publicly disclosed.
- Terminology discipline matters: anchor any non-statutory term (such as *key interface*) to the statutory framework, or risk falling short of the legal requirement.

## Connects To

- **Subsequent chapters in this pack** — this introduction sets up the MOSA Overview (the guidebook's Section 2) and the downstream guidance on planning, implementing, and evaluating MOSA, including RFP development and proposal evaluation.
- **Interface repositories and modular system interfaces** — the FY 2021 NDAA repository requirements introduced here feed directly into later treatment of interface definition, machine-readable documentation, and Government access regulations.
- **Data rights and contracting** — the DFARS 252.227 data-rights theme connects to acquisition-strategy and intellectual-property chapters, where the business architecture half of MOSA is operationalized.
- **Broader SE standards landscape** — MOSA's reliance on widely supported, consensus-based interface standards links to the systems-engineering standards and architecture material covered elsewhere in the knowledge-pack collection.

# Chapter — MOSA Requirements Across DoD Acquisition Pathways and Conclusion

> Authority note: This chapter reflects the current DoD MOSA guidance, *Implementing a MOSA in DoD Programs*, which supersedes the 2013 Open Systems Architecture (OSA) guidebook. Where this guide and the older OSA material differ, treat this guide as the governing reference.

## Core Idea

A Modular Open Systems Approach is not an optional add-on reserved for large weapon programs — it is a default expectation that travels across every route a program can take through the defense acquisition system. The governing principle in this slice is a statutory one: program managers are obligated to apply MOSA to the greatest extent practicable, and that obligation holds no matter which acquisition pathway a program runs on. The pathways differ in how *formally* MOSA is mandated and in *why* it matters, but none of them is exempt from the underlying expectation that systems be built to be modular and open.

The chapter closes the guide's argument by stepping back from the pathway-by-pathway detail to a summary judgment: adopting MOSA is a meaningful change in how complex systems are designed, and the payoff — flexibility, interoperability, and sustainability — depends as much on stakeholder commitment and collaboration as on any single technical decision.

## Frameworks Introduced (exact source names, when/how)

- **Adaptive Acquisition Framework (AAF)** — introduced as the structure that organizes the Defense Acquisition System and aims to deliver solutions that are effective, suitable, survivable, sustainable, and affordable to the end user in a timely way. The AAF is the umbrella under which the six pathways sit.
- **The six AAF acquisition pathways**, each governed by its own DoD Instruction:
  - **Urgent Capability Acquisition** — governed by DoDI 5000.81.
  - **Middle Tier of Acquisition** — DoDI 5000.80 (rapid prototyping / rapid fielding).
  - **Major Capability Acquisition** — DoDI 5000.85 (the MCA pathway).
  - **Software Acquisition** — DoDI 5000.87.
  - **Defense Business Systems** — DoDI 5000.75.
  - **Acquisition of Services** — DoDI 5000.74.
- **Title 10, U.S.C. 4401** — cited as the statutory basis requiring PMs to evaluate and implement MOSA to the maximum feasible extent, and the authority under which PMOs must apply MOSA across the other pathways.
- **Major Capability Acquisition (MCA) pathway** — treated in its own section (4.1) as the pathway where MOSA is most fully specified; the guide points to **Figure 4-1** for a summary of the key technical and business requirements that apply here.
- **Modular Open Systems Working Group (MOSWG)** — introduced in the conclusion as the DoD body established to lead MOSA guidance and to build out coursework and training.
- **DoD MOSA Technical Standards Working Group (TSWG)** — named as the partner body that works with the MOSWG to surface common standards and to identify what helps and what hinders MOSA adoption.
- **SE&A MOSA web page** — cited as the DoD's reference point for current MOSA priorities (hosted under the office at cto.mil/sea/mosa).
- **DAU AAF resources** — the guide directs readers to the DAU website for additional MOSA implementation material tied to the framework.

## Key Concepts

- **The statutory floor is "maximum extent practicable."** Across the AAF, the requirement is phrased as applying MOSA as far as is practical or feasible — not "always" and not "never," but a standing obligation to push toward openness unless there is a defensible reason not to.

- **MCA carries the most prescriptive MOSA requirements.** In the Major Capability Acquisition pathway, MOSA is the mechanism for incremental development and for strengthening competition, innovation, and interoperability. Major Defense Acquisition Programs that cleared Milestone A or B after the start of 2019 are required to be designed and developed with MOSA built in.

- **The Acquisition Strategy must locate MOSA concretely.** A program's strategy is expected to spell out where MOSA will be used, why, and how — not leave it as a stated intention.

- **MOSA requirements must flow into the solicitations.** The Milestone Decision Authority for an MDAP using MOSA has to confirm that both solicitations — the RFP for Engineering and Manufacturing Development (EMD) and the RFP for Production and Deployment (P&D) — describe the approach and name the minimum set of major system components to be designed into the system. This is the contractual hand-off point where the approach becomes binding on industry.

- **Pathways without a formal mandate still benefit.** The guide is explicit that every program should adopt MOSA, and it walks the "other pathways" individually:
  - **Urgent Capability (5000.81):** MOSA is not formally required, but using components with modular open interfaces speeds development and fielding while lowering the risk of interface failures with other systems in the field; widely accepted standards add further ease of employment.
  - **Middle Tier (5000.80):** this pathway splits into rapid prototyping and rapid fielding. Rapid prototyping programs are not required to implement MOSA but should where practical, to ease integration with existing systems during technology insertion and refresh. In rapid fielding, mature technologies are pushed out with little development; if those technologies lack modular standardized interfaces, the PM is expected to recognize and actively manage the added integration and operational risk of a less modular system.
  - **Software Acquisition (5000.87):** the guide treats MOSA as especially important here. Software-pathway programs must build architecture strategies that enable a MOSA interoperable with the systems they must work with; PMs must, as far as practical, require that commercial or proprietary software used with government-developed software carries documented open interfaces to permit technology insertion. Programs must use modern, iterative software practices, continuously improve quality, and integrate intellectual-property considerations with their MOSA and other program strategies.
  - **Defense Business Systems (5000.75):** MOSA is not specifically required, but leadership must use COTS and GOTS solutions where practical, and the development and integration of those solutions should be pushed toward maximum openness and modularity.

- **The DoD backs MOSA with standing governance.** Beyond policy text, the department has stood up the MOSWG and the TSWG to lead guidance, build training, and identify the common standards, barriers, and enablers that determine whether MOSA actually takes hold in programs.

## Mental Models

- **MOSA as a default, with pathways as dials, not switches.** Think of MOSA as "on" by default everywhere; each pathway adjusts how hard the requirement is enforced rather than whether it applies. MCA turns the dial to mandatory-and-documented; the software pathway turns it nearly as high; urgent capability and business systems leave it as a strong recommendation — but the dial never reaches zero.

- **The Acquisition Strategy → RFP → design pipeline.** For MCA, MOSA moves through a chain: it is justified and located in the Acquisition Strategy, then described and bounded (minimum major system components) in the EMD and P&D RFPs, then realized in the system design. A break anywhere in that chain means the approach exists on paper but not in the delivered system.

- **Pay now or manage risk later.** The rapid-fielding guidance encodes a trade: skip modular interfaces to field faster, and you inherit downstream integration and operational risk that the PM must then own and manage. Modularity deferred is not modularity avoided — it converts into managed risk.

- **Openness as an enterprise property, not a program property.** The conclusion frames MOSA as a route to a more flexible and responsive *defense enterprise*, achieved by programs working together and leveraging shared resources. The value compounds across programs through common standards, not just within any one system.

## Key Takeaways

- The obligation to apply MOSA to the maximum extent practicable is statutory (10 U.S.C. 4401) and pathway-agnostic — it follows the program regardless of which AAF route is chosen.
- The AAF spans six pathways, each tied to a specific DoDI; MCA (5000.85) is where MOSA requirements are most prescriptive, and software (5000.87) is where the guide stresses MOSA most strongly outside MCA.
- For MDAPs that passed Milestone A or B after January 1, 2019, MOSA design and development is required, must be located in the Acquisition Strategy (where/why/how), and must be carried into the EMD and P&D RFPs with a defined minimum set of major system components.
- Even where MOSA is not formally mandated (urgent capability, business systems, rapid prototyping), the guide's position is unambiguous: adopt it anyway, because the flexibility, interoperability, and lower interface risk are worth it.
- The guide's concluding judgment is that MOSA's success rests on three pillars — modularity, consensus-based standards, and a holistic, forward-looking approach — plus the human factors of commitment and collaboration among stakeholders.
- The DoD has institutionalized MOSA support through the MOSWG and TSWG and points practitioners to the SE&A MOSA web page and DAU AAF resources for current priorities and training.

## Connects To

- **Acquisition Strategy and program planning:** the where/why/how documentation requirement links MOSA directly to the strategy artifacts a PM must produce, tying this chapter to the broader systems-engineering planning discipline.
- **Statutory and policy basis for MOSA:** 10 U.S.C. 4401 and the six DoDIs connect this pathway view to the legal and regulatory foundations covered earlier in the guide, including the rationale for MOSA in MDAPs.
- **MOSA assessment:** the guide moves from pathway requirements into assessing MOSA and assessment tools (Appendix A), connecting "what is required" to "how compliance and maturity are evaluated."
- **Standards and governance bodies:** the MOSWG/TSWG references connect to the consensus-based-standards thread that runs through MOSA — the same standards machinery that downstream packs on open architecture and interoperability rely on.
- **Software and IP strategy:** the 5000.87 requirements link MOSA to intellectual-property management and modern iterative software practice, bridging to acquisition pathways and software-engineering material elsewhere in the knowledge base.

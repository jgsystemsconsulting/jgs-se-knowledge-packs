# Chapter — Agile and the Federal Contracting Process

## Core Idea

Agile delivery depends on carrying lessons from one release into the next and on having the freedom to add staff and resources as contract requirements shift. The same federal procurement machinery built for Waterfall work can be adapted to give Agile programs that freedom. The governing instrument is the Federal Acquisition Regulation (FAR), the codified, uniform set of policies and procedures that executive branch organizations use to acquire goods and services, written to ensure contracts deliver best value to the customer on time. The FAR never names Agile, yet it contains contracting approaches that suit Agile work, and its own guidance (FAR 1.102-4(e)) instructs the acquisition team to treat the absence of a prohibition as permission to innovate using sound business judgment. The chapter's argument is that a contract for an Agile program must strike a deliberate balance: enough structure to reach the mission outcome, enough flexibility to let software requirements evolve within the agreed scope. Tilt too far either way and the program risks disruption and delay. Before committing to an IT contract, an organization should weigh the risks, benefits, and costs, choosing a vehicle based on how much risk it is willing to share with the contractor.

The chapter organizes its guidance into three contracting best practices, each decomposed into supporting actions.

## Frameworks Introduced (exact source names, when/how)

- **Federal Acquisition Regulation (FAR)** — the foundational regulation, introduced at the chapter open as the codification of uniform acquisition policy for executive branch agencies (with noted exceptions such as the FAA and agencies holding separate statutory authority). FAR 1.102-4(e) is quoted to establish the "innovate where not prohibited" stance that frames the whole chapter.
- **Modular contracting** — introduced as the FAR-authorized method (established in 41 U.S.C. § 2308, implemented at FAR 39.103) for satisfying a system need through successive acquisitions of interoperable increments. Presented as the contracting analog to Agile's deliver-in-intervals principle, since a large acquisition can be split into several smaller ones.
- **Simplified acquisition procedures** — cited (FAR 13.500) as a FAR authority for acquiring certain commercial items within set dollar ranges to cut administrative burden.
- **TechFAR handbook** — introduced as the OMB-issued guide that surfaces FAR flexibilities, used in partnership with the **U.S. Digital Services Playbook** and its "plays." Both GSA and OMB are named as authors of guides that help organizations apply FAR flexibility to Agile.
- **Statement of Work (SOW), Performance Work Statement (PWS), and Statement of Objectives (SOO)** — the three solicitation-document types, contrasted in Table 8. The SOO is positioned as the most flexible (broadly defined high-level objectives, not part of the contract, expects the end state to evolve), the SOW as the most prescriptive (high government confidence in the end state, part of the contract, change is disruptive), and the PWS in between (required results in measurable terms, part of the contract, change expected as the offeror innovates).
- **Contract data requirements list (CDRL)** — introduced as the traditional IT contracting deliverable structure, which the chapter argues should be tailored to rely on Agile metrics rather than milestone documentation.
- **Authority to Operate (ATO)** — introduced as the risk-based security authorization process; GAO's own six-step process (based on NIST and FIPS guidance) is described in Agile in Action 4 as an example of folding Agile practices into a process-heavy security gate.
- **Table 9 metric categories** — three categories named for contract oversight: technical management (e.g., technical debt), program management (e.g., lead time), and Agile methods (e.g., feature usage, delivery frequency).
- **Indefinite delivery/indefinite quantity (IDIQ) contracts and Agile blanket purchase agreements (Agile BPA)** — named in the Agile in Action 3 case examples as concrete vehicles agencies used.

## Key Concepts

**Tailoring acquisition planning and contract structure.** The first best practice covers three actions: encourage modular contracting, enable flexibility in contract requirements, and decide whether the contract is for goods or services. The contracting process must be deliberate enough to support regular delivery cadences, and the contracting culture should create a business environment that welcomes small, frequent releases.

**Why modular contracting fits Agile.** Splitting a large acquisition into smaller increments, where each increment performs its principal functions without depending on a later one, reduces risk, speeds capability delivery, and eases adoption of newer technology. Crucially, acquiring one increment must not commit the government to acquiring future ones. The chapter also warns to avoid vendor lock-in by ensuring deliverables are tested and documented so a replacement vendor could continue the work.

**SOW vs. PWS vs. SOO.** Agile programs typically lack the well-defined, detailed requirements that a SOW assumes early in the life cycle. The chapter recommends a PWS (results in clear, measurable, objective terms) or a SOO (broad high-level objectives giving offerors maximum flexibility) instead. A SOO can stand alone or pair with any performance-based contract and may carry the product vision, strategic themes, an initial road map, an initial backlog, and "build iterations." Whichever document is used, the aim is to describe what is to be achieved rather than how — leaving the developers room in their process.

**Contract type follows the goods-versus-services decision.** Almost any contract type can support Agile, but the choice hinges on whether the program is buying end items (e.g., completed features) or services (e.g., the labor of a set number of developers). That single decision drives contract type, contract vehicle, and which oversight data to request. The selected type should maximize the program's ability to continuously deliver working software.

**Inherently governmental functions.** Because the contractor must not perform inherently governmental work, the solicitation should delineate contractor responsibilities, identify which decisions the contractor may make, and keep final disposition decisions with federal employees, preserving government discretion and accountability.

**Oversight through Agile artifacts and metrics.** The second best practice replaces milestone-heavy documentation with data drawn from Agile work. Programs should collect actual data on releases, features, and capabilities and tailor the CDRL to Agile metrics, because the primary deliverable is working code that adds value, not documents. The definition of "done" in a user story should list everything that must be demonstrated before a release. Obtaining data rights (via a technical data package or other means) protects the government if it changes contractors.

**Retrospectives as an oversight input.** The chapter supplies sample retrospective questions and their implications — for example, longer gaps between identifying a need and delivering working software signal greater risk; building a minimum viable product validates needs and enables fast course correction; and working software is the primary measure of progress, with customer satisfaction signaling the program prioritizes early, continuous delivery.

**Aligning reviews with cadence.** In Waterfall, technical reviews act as control gates between sequential phases; in Agile, reviews are face-to-face information-sharing and confidence-building moments that surface problems early. Traditional preliminary and critical design reviews may be replaced by incremental design reviews tied to the release cadence, occurring more often than traditional gates. Reviews not aligned to cadence can impede progress.

**Integrating the program office and developers.** The third best practice covers training program office, acquisition, and contracting personnel; identifying clear roles for oversight; and ensuring everyone knows the contract's scope. Contracting personnel are described as the linchpin enabling a collaborative relationship between empowered teams, program managers, the product owner, and contractors. The FAC-C-DS certification (within the DITAP program) is cited as a training pathway. Distributed teams need collaboration tooling, especially video conferencing, to sustain the frequent feedback Agile requires.

**Role clarity, especially product owner vs. COR vs. contracting officer.** The product owner is accountable for delivering business value by creating, ordering, and maintaining customer-centric backlog items. The contracting officer's representative (COR) is a technical expert who provides day-to-day oversight and judges whether work is technically sufficient for government acceptance. The contracting officer handles contract development, oversight, and administration. The product owner role is a frequent source of confusion because it has no Waterfall equivalent. Both the product owner and COR must be government employees so they are empowered to make day-to-day decisions; the product owner acts as the single government focal point bridging the COR and the contractor.

**Managing change and scope.** Contracting personnel must plan for change during the period of performance. Newly identified work that is still within scope can be added to the backlog and prioritized; work that is higher priority but out of scope may require an out-of-scope contract modification, which raises competition, legal, and appropriations considerations under the FAR. An empowered product owner who prioritizes detailed requirements within the program vision helps keep out-of-scope modifications infrequent and guards against scope creep.

## Mental Models

- **Structure–flexibility balance beam.** Every contracting decision is weighed on a single beam: too rigid and the Agile cadence stalls under long timelines and costly change requests; too loose and mission outcomes go unmet. The goal is enough structure to hit the outcome with enough flexibility to evolve requirements inside the agreed scope.
- **The SOO–PWS–SOW flexibility spectrum.** Picture the three documents on a sliding scale of certainty about the end state. High certainty leans toward a SOW; an evolving end state leans toward a SOO. Match the document to how well the requirements are actually understood at award.
- **Contract as a mirror of the program.** A successful contract reflects the program and can absorb program updates without burdensome paperwork — and reflects learning from prior contracts so the contracting process keeps improving.
- **The "what, not how" lens.** Solicitation documents should state the outcome to be achieved, not the method, leaving developers room to apply their own technical solution.
- **Charge-account contracting.** The Agile BPA is framed as establishing "charge accounts" with qualified contractors to fill anticipated repetitive needs — an experiment in modular contracting that trades fixed vendor pools for a streamlined ordering process.
- **Contract requirements vs. functional requirements.** Hold these as two distinct layers: contract requirements live in the solicitation, while functional requirements decompose over time from high-level capabilities into features. Conflating them risks dropping compliance and security requirements.

## Anti-patterns

- **Self-reporting metrics that invite gaming.** The chapter explicitly warns ("Beware of self-reporting"): velocity is team-specific, not comparable across teams, and easy to inflate by padding story-point estimates, so a rising velocity does not necessarily mean rising productivity or added value.
- **Permanently fixed, pre-established vendor pools.** Drawing on the 18F BPA lessons learned, the source cautions against locking in large, long-duration vendor pools with no ability to onboard or off-board vendors, which can stagnate competition so vendors only compete for larger buys. It likewise warns against relying on open-source prototype software in that context.
- **Reviews and gates misaligned with cadence.** Carrying Waterfall control gates unchanged into an Agile contract can impede progress and cause delays.
- **Confusing or undefined roles.** Failing to distinguish the product owner, COR, and contracting officer, or leaving roles undefined, creates bottlenecks and breaks the rapid feedback channels Agile needs.
- **Disempowered product owner / non-government product owner.** If the product owner is not a government employee or is not empowered, they cannot make day-to-day decisions, which causes development delays and contracting bottlenecks.
- **Untailored CDRLs.** If the contract data requirements list ignores the Agile environment, the program forfeits the chance to collect software-quality data; without Agile metrics, the government lacks the information to hold contractors accountable.

## Key Takeaways

- The FAR does not mention Agile but actively permits it; absence of direction is a license to innovate with sound business judgment (FAR 1.102-4(e)).
- Three best practices anchor Agile contracting: tailor planning and structure to Agile; build oversight on Agile metrics, artifacts, and retrospectives; and integrate the program office with the developers.
- Modular contracting (41 U.S.C. § 2308 / FAR 39.103) is the FAR's closest fit to incremental Agile delivery and should be encouraged.
- Prefer a PWS or SOO over a SOW when requirements are not yet well defined; match the document to the program's actual certainty about the end state.
- The goods-versus-services decision drives contract type, vehicle, and oversight data.
- Oversight should rest on real release/feature data and tailored CDRLs, not predetermined milestone documentation; guard against self-reported, easily inflated metrics like velocity.
- Tie reviews to the Agile cadence; replace heavyweight design-review gates with incremental reviews.
- Define roles crisply — product owner, COR, and contracting officer have distinct duties; the product owner and COR must both be government employees and stay in close communication.
- Plan for change: keep program vision broad enough that emerging features fit the existing scope, reserving out-of-scope modifications for genuine exceptions and their legal/appropriations review.
- ATO is a security gate that Agile teams can streamline by partnering early with security personnel, developing documentation iteratively, and inheriting environment-wide controls.

## Connects To

- **Chapter 2** — the federal adoption challenge of making acquisition strategies and contract structures genuinely support Agile programs.
- **Chapter 3** — long award timelines and costly change requests as major hurdles for frequent-release programs; also the makeup of the development team referenced here.
- **Chapter 5** — the definition of "done" in user stories, reused here as an oversight reference point.
- **Chapter 8** — establishing program-specific Agile metrics; the metric categories in Table 9 point forward to that fuller treatment.
- **Chapter 7** — the immediately following chapter on Agile program monitoring and control, the natural continuation of contract oversight.
- **Appendix II: Key Terms** — referenced for the formal definition of the product owner role.
- **External authorities** — FAR parts 6, 8, 13, 16, 34; 41 U.S.C. § 2308; NIST and FIPS security guidance; OMB/GSA TechFAR handbook and the U.S. Digital Services Playbook; and the FAC-C-DS / DITAP acquisition-training pathway.

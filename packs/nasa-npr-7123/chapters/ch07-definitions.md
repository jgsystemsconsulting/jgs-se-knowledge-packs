# Chapter 7: Appendix A — Definitions

## Core Idea
Appendix A provides the authoritative NASA definitions for the technical and programmatic terms used throughout NPR 7123.1D, establishing precise shared vocabulary that prevents ambiguity in SE requirements, reviews, and documentation; many terms have specific NPR-scoped meanings that differ from general engineering usage.

## Frameworks Introduced
- **Validation vs. Verification Distinction**: Verification answers "Did I build the product right?" (conformance to requirements/specifications); Validation answers "Am I building the right product?" (conformance to stakeholder expectations and ConOps). Both are distinct processes with distinct criteria.
  - When to use: Whenever planning a V&V program; confusing the two leads to products that meet specs but fail in operational use, or vice versa.
- **Deviation vs. Waiver Distinction**: A Deviation is authorised relief *before* the requirement is placed under configuration control; a Waiver is authorised relief *after* configuration control. Timing determines the type.
  - When to use: When seeking relief from any SE requirement; the timing of the request determines which document type to prepare.

## Key Concepts
- **Verification**: Proof of compliance with requirements/specifications; determined by test, analysis, demonstration, or inspection; answers "Did I build the product right?"
- **Validation (product)**: Proof that the product accomplishes its intended purpose based on stakeholder expectations and ConOps; answers "Am I building the right product?"
- **Validation (requirements)**: The continuous process of ensuring requirements are well-formed (clear, unambiguous), complete (consistent with stakeholder needs), consistent (conflict-free), and individually verifiable and traceable.
- **Tailoring**: The process of adjusting or seeking relief from a prescribed requirement; results in deviations (pre-configuration control) or waivers (post-configuration control).
- **Customizing**: Modification of *recommended* SE practices to accomplish SE requirements; does not change what must be done, only how; does not require waivers or deviations.
- **Baseline**: An agreed-to set of requirements, designs, or documents under formal change control; changes must go through an approved monitoring process.
- **Enabling Products**: Life-cycle support products and services (production, test, deployment, training, maintenance, disposal) that facilitate the use of the operational end product; the program/project is responsible for ensuring they exist at each phase.
- **Concept of Operations (ConOps)**: A high-level description of how a system will be used to meet stakeholder expectations, typically time-sequenced; developed early in Pre-Phase A; provides validation criteria.
- **Measure of Effectiveness (MOE)**: A qualitative or non-directly-designable stakeholder-facing measure of product acceptability; typically qualitative; drives validation.
- **Measure of Performance (MOP)**: A quantitative design target; when met, helps ensure the associated MOE is satisfied; typically two or more per MOE; drives design.
- **Technical Performance Measure (TPM)**: Performance measures monitored by comparing current actual achievement against the anticipated plan; selected from MOPs; used for progress tracking and corrective action decisions.
- **Key Decision Point (KDP)**: The event at which the Decision Authority determines program/project readiness to progress to the next life-cycle phase.
- **Leading Indicator**: A subset of TPMs providing forward-looking insight into potential future states; allows management to act before problems are realised; mass and power margins are the two mandated examples.
- **System**: The combination of hardware, software, equipment, facilities, personnel, processes, and procedures that function together to produce a required capability.
- **SE Engine (Systems Engineering Engine)**: The NASA SE model applying 17 technical processes to system products; called an "engine" because the processes drive the technical effort.
- **Recursive**: Repeated application of processes to design next lower layer products or realise next higher layer products within the system structure; also applies across life-cycle phases.
- **Iterative**: Application of a process to the same product or set of products to correct a discovered discrepancy or variation from requirements.
- **Repeatable**: A process characteristic allowing application at any level of the system structure or within any life-cycle phase.
- **Logical Decomposition**: Decomposition of technical requirements by functions, time, and behaviours to determine logical and data architecture models and derived requirements; outputs include functional flow block diagrams, timelines, state and mode diagrams.
- **Product Layer**: A horizontal slice of the product breakdown hierarchy comprising an end product and its associated enabling products; the SE Engine is applied per product layer.
- **Technical Authority (TA)**: Part of NASA's checks-and-balances system; individuals with formally delegated, independently funded authority; three lines: Engineering (ETA), Safety and Mission Assurance (SMA TA), Health and Medical (HMTA).

## Mental Models
- Verification and validation are sequential but distinct: verify first (did we build to spec?), then validate (does it work in the intended environment for the intended purpose?). Neither substitutes for the other.
- MOE → MOP → TPM is a cascade: stakeholder expectations set MOEs; design requirements translate MOEs into MOPs; TPMs are the subset of MOPs actively tracked against plan.
- A "baseline" is not the same as "finished" — baselining puts a document under configuration control so changes are tracked; the document may continue to evolve through controlled updates.

## Key Takeaways
1. Verification = "built right" (specification conformance); Validation = "right thing built" (stakeholder expectation conformance); both are mandatory and distinct.
2. Deviation applies before configuration control; Waiver applies after — timing determines the required document type.
3. MOEs are qualitative validation standards; MOPs are quantitative design targets; TPMs are the monitored subset of MOPs — these three levels of measurement serve distinct purposes.
4. "Recursive, iterative, and repeatable" are precise NPR terms: recursive means applied across product layers; iterative means applied repeatedly to correct a single product; repeatable means applicable at any level or phase.
5. Enabling products are not optional accessories — the program/project is responsible for ensuring enabling products exist at each life-cycle phase.

## Connects To
- **Appendix F (Work Product Maturity Terminology)**: Defines Initial, Preliminary, Baseline, Approve, Update, and Final as used in Chapter 5 review requirements.
- **Chapter 3 (17 Processes)**: Definitions for MOE, MOP, TPM, Logical Decomposition, and Requirements management terms ground the process descriptions.
- **Chapter 5 (Life-Cycle Reviews)**: KDP, Entrance Criteria, Success Criteria, RID, RFA, and Review Trends definitions underpin the review requirements.
- **Chapter 2 (Roles and Responsibilities)**: ETA, Technical Authority, Programmatic Authority, Institutional Authority, Tailoring, Customizing definitions are established here.

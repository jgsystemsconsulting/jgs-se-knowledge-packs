# Chapter 6 — Commercial Launch Safety and System Safety Training

> **Caveat — read this first.** This chapter synthesizes two chapters of the *FAA System Safety Handbook* (December 30, 2000): Chapter 13, the launch-safety "pull-out handbook" written for the commercial space transportation industry, and Chapter 14, on system safety training. The Handbook is a public-domain US Government work, so the underlying ideas are free to reuse — but any third-party *reprint* you may encounter (with added front matter, watermarks, or editorial commentary) is **not** public domain. Cite and quote the FAA original, not a vendor reprint. The training material in particular leans on an outside conference presentation credited in the source; treat the pedagogy as illustrative, and confirm current regulatory citations (the launch-licensing rules and advisory circulars named here date to 2000 and have since been restructured).

## Core Idea

A commercial launch vehicle stores enormous energy to reach orbit, and the accidental release of that energy can be catastrophic both near the pad and far downrange. The FAA's role, exercised through the Office of the Associate Administrator for Commercial Space Transportation (AST), is not to prescribe every design detail but to require the *applicant* to run a disciplined system-safety process that proves their operation poses no unacceptable threat to the public. The license is the gate; system safety engineering is how the applicant earns it. The same logic that runs through the rest of the Handbook — identify hazards, eliminate or control them to acceptable risk across the whole life cycle — is here applied to a domain where the consequence of failure is measured in expected casualties to the uninvolved public.

The second half of the chapter shifts from the rocket to the people. None of the analysis, none of the operational controls, and none of the software discipline matter if the management, engineers, inspectors, and operators carrying out the program have not been trained to do their jobs safely. Chapter 14 therefore treats training as a first-class element of any system safety program and gives the trainer a systematic method — analyze the need, analyze the task, write measurable objectives, deliver to adult learners, and account for how individuals actually learn.

## Frameworks Introduced (exact source names, when/how)

- **Office of the Associate Administrator for Commercial Space Transportation (AST)** — introduced in §13.1–13.2 as the FAA office that carries out the agency's statutory commercial-space responsibility under Title 49 U.S. Code, Subtitle IX (the former Commercial Space Launch Act). AST's mandated mission is to protect public health and safety and the safety of property. It is split into three components: the Associate Administrator's office (AST-1, policy and direction), the Space Systems Development Division (SSDD, technology and air-traffic integration), and the Licensing and Safety Division (LASD, the licensing and compliance arm).

- **The licensing process** — laid out in §13.3 as a set of components: pre-licensing consultation, policy review, payload review, safety evaluation, financial-responsibility determination, and environmental review. Three of these — safety evaluation, financial responsibility, and environmental determination — are where system-safety methodology actually bites.

- **Maximum Probable Loss (MPL) analysis** — introduced in §13.3.2 as the methodology for setting an applicant's financial-responsibility (insurance) requirement. The source is careful: it is maximum *probable* loss, not maximum *possible* loss. MPL works by enumerating accident scenarios, examining the worst for third parties and for government property, and estimating the loss not exceeded at a chosen probability threshold. (The Handbook footnotes that AST's MPL methodology was developed by Futron Corporation.)

- **Facility Damage and Personnel (DAMP) Injury Analysis** — introduced in §13.3.2 as the critical input that feeds MPL. DAMP uses vehicle, trajectory, failure-response, facility, and population data to estimate casualty expectation from inert debris, secondary debris, and impact-explosion overpressure. (Footnoted as developed for AST by Research Triangle Institute.)

- **System Safety Engineering Process** — introduced in §13.4 as the structured application of system-safety principles to find, eliminate, or control hazards across the life cycle, performed by the *vehicle developer/operator*. The source explicitly references MIL-STD-882C as the process basis, including the **System Safety Program Plan (SSPP)**, which describes how safety standards, responsibilities, resources, methods, and milestones are tailored and integrated with the rest of systems engineering.

- **Validation Acceptance Matrix (Table 13-1)** — introduced in §13.4.2 as a sample mapping of candidate critical systems to the mix of analysis, ground test, and flight test that can validate each. Markings distinguish full coverage from partial coverage and flag systems whose hardware *and* software both count.

- **Expected casualty** — introduced in §13.4.8 as the space industry's measure of public risk: the average number of human casualties (fatality or serious injury) expected per mission. The source points to FAA Advisory Circular 431-02 for how the expected-casualty analysis is applied.

- **Systematic Software Safety Process (SSSP)** — introduced in §13.5.2 as the organized, periodic review of safety-critical software and of software tied to safety-critical systems and functions. Its elements are software safety planning, a software safety organization, a software safety team, life-cycle-phase application, phase-independent activities, special provisions, and documentation. Table 13-2 maps safety activities to each life-cycle phase.

- **Software Hazard Criticality (SHC) Matrix** — introduced in §13.5.2 as a risk-grouping matrix analogous to the Hazard Risk Index (HRI), using control categories from MIL-STD-882C crossed with severity (catastrophic / critical / marginal / negligible) to prioritize software design, analysis, and test effort. The source also reproduces the parallel software-level scheme from RTCA DO-178B (levels A through E).

- **System Safety Training method (Chapter 14)** — introduced as a sequence the trainer follows: **Training Needs Analysis → Task Analysis → Learning Objectives → Delivering Effective Training → Learning Styles**. The chapter credits an outside conference presentation as its source and is explicitly a *design* guide, not a delivery or evaluation manual.

## Key Concepts

### Launch licensing and risk

- **Burden of proof sits with the applicant.** It is the applicant's job to show they understand every hazard and risk their operation poses and how they will mitigate it — through safety devices, protective systems, warning devices, or special procedures. LASD's job is to verify that the demonstration is adequate and valid.

- **Quantitative vs. qualitative analyses.** The quantitative work focuses on the reliability of critical safety systems and on the hazards of the hardware and the risk those pose to people and property near the pad, along the flight path, and on orbit. The tools named most often are fault trees (FTA) and FMEA, together with Poisson-distribution calculations of collision risk for over-flight and on-orbit cases. The qualitative work instead examines the *organization*: safety policies, communications, personnel qualifications, and internal/external interfaces.

- **Five evaluation tests.** LASD checks whether the applicant has (1) identified all energy and toxic sources and controlled their accidental release, (2) evaluated safety-critical aspects and accident-risk factors, (3) identified hazardous events and assessed cause, effect, and frequency, (4) implemented elimination/prevention/mitigation to bring risk to acceptable levels, and (5) specified how those controls can be verified and validated.

- **Financial responsibility, three ways.** A licensee can meet the required amount by holding sufficient financial reserves, placing the amount in escrow, or buying liability insurance — the last being the common and preferred route. If a launch leaves no government property at risk (e.g., from a private licensed range), no government-property requirement is issued.

- **Environmental determination.** Because licensing a launch or launch site is a major Federal action, NEPA (1969, as amended) requires AST to weigh environmental consequences and to review the applicant's Environmental Assessments and Environmental Impact Statements.

### Safety-critical systems and their validation

- **Definition of safety-critical.** Any system or subsystem is safety-critical when a failure of its performance or reliability could endanger public health, the public, or property. Whether a given system is critical can depend on flight path and on the vehicle's ability to reach populated areas — so each system must be analyzed for each mission phase, from ground operations through reentry and landing.

- **A worked candidate list.** The source enumerates examples that hazard analysis (PHA and others) may flag: main structure, thermal protection, propulsion and propellant tanks, power, guidance/navigation/control and critical avionics, health monitoring, the Flight Safety System, ground-based flight-safety systems, and — depending on concept — pilot and life-support systems.

- **Three validation legs: analysis, ground test, flight test.** Analysis can be the *primary* validation only where the flight regime cannot be simulated by test and there is sound technical justification. Qualification tests are deliberately run beyond expected environments — the source notes ELV Flight Safety Systems are qualified to roughly twice the expected environment — to prove design margin. A well-defined test plan plus a credible test report can substitute for direct FAA observation.

- **Flight test catches the unknown unknowns.** The source is blunt that analysis and ground test, however necessary, do not surface every safety issue in a new system; flight test exists to verify performance, validate the design, find deficiencies, and expose unrecognized interactions. Post-flight comparison of predicted vs. actual data is the crucial validation tool, and the chapter walks the data to monitor through each flight phase (launch, staging/separation, booster turn-around and flyback, ascent, descent/de-orbit).

- **Similarity is allowed but bounded.** Performance and reliability data can lean on flight history of comparable systems, but a candidate qualified "by similarity" must be only a minor variation of the already-qualified item, and the reference item's experienced environments must be at least as severe. The source cites EWR 127-1 for this rule.

- **Operational controls trade against design.** What counts as safety-critical depends on the scope of operations. Rather than redesign a vehicle to remove a limitation, an operator may instead constrain operations — through launch-commit criteria, abort capability, weather limits, airspace coordination, landing-site surveillance, and limits on over-flight of populated areas. As confidence in the system grows through demonstration, some constraints (e.g., over-flight restrictions) may be relaxed.

### Software safety

- **Software fails differently.** Having no physical existence, software never wears, fractures, or decays the way hardware does. Its problems are *errors* — coding mistakes, misread requirements, specification oversights, or failures to anticipate a hazardous set of conditions. Because software has far more execution paths than hardware, exhaustive path testing is infeasible, and there is no mature, uniform way to assign reliability numbers to it. Ultimately, software system safety aims to locate and strip out the unintended hazardous behavior built into the system.

- **Defect classes that become hazards.** Software is defective if it does not execute, executes at the wrong time or out of sequence, or executes but produces wrong information. It becomes hazardous when those defects sit inside safety-critical functions — the source lists examples including ignition control, flight control, navigation, monitoring, hazard sensing, energy control, fault detection, interrupt processing, autonomous control, safety-information display, and safety-critical computation.

- **Organize for independence.** A software safety organization should have centralized authority dedicated to safety, genuine independence (to prevent bias in sensitive hazard calls), and high enough status to act with visibility. Ultimate accountability rests with the applicant/operator's top management.

- **Phase-mapped analyses.** Table 13-2 sequences the analyses: a Preliminary Software Hazard Analysis (PSHA) at concept/requirements, an architectural-design hazard analysis (SSADHA) at PDR, a detailed-design hazard analysis (SSDDHA) at CDR, an implementation hazard analysis at TRR, integration testing and a final software-system hazard analysis at acceptance, and an Operating and Support Hazard Analysis (O&SHA) in operations. Phase-independent activities (from NASA Standard 8719.13A) run throughout: tracing safety requirements, tracking discrepancies and changes, and conducting safety reviews.

- **A long list of design rules.** The source gives concrete design and development guidance — a defined safe state per operational phase, reverting to safe state on detected failure, isolating safety-critical functions (ideally on a standalone computer), single deterministic execution paths for safety-critical functions, integrity checks at power-up and during reconfiguration, graceful degradation on power loss, error logging, positive feedback on safety-critical actions, distinguishable safety-critical alerts, and rigorous configuration control through a Software Configuration Control Board with version control and the ability to restore prior revisions.

- **Cited external standards.** The chapter points outward repeatedly: MIL-STD-882C and RTCA DO-178B for software control categories and levels; the IEEE Standard for Software Safety Plans and UK Defence Standard 00-55 (Annexes B and E, including the software safety "case") for planning and documentation models; NASA Standard 8719.13A and Guidebook GB-1740.13-96; ISO 9000-3 for software quality; and the Joint Software System Safety Committee handbook plus EWR 127-1 for generic software safety provisions.

### Training as a system safety element

- **Training is required, not optional.** Management, safety working groups, inspectors, controllers, technicians, and engineers all need training appropriate to their role; training also serves as an *administrative control* to bring risk to acceptable levels.

- **Needs analysis comes first.** A training needs analysis studies the organization to find how training can improve safety, effectiveness, efficiency, and legal compliance. The source's explanation for why the *same* course can succeed once and fall flat the next time is that no two groups share the same prior knowledge, motivation, and background — so the trainer must assess and adapt. Audience analysis (education, duties, prior training, tenure, climate, norms) and problem analysis (is the gap really one of skill, or of motivation/environment?) feed this.

- **Task analysis.** Before objectives, the trainer lists the sequential steps of the job skill. Not every step needs training, but seeing the whole task lets trainer and trainee identify the steps that do — and lets even an expert trainer surface "common sense" steps they might otherwise skip. The trainer can observe the task, interview incumbents, or perform it themselves, then validate the inventory with the people who actually do the job, watching for drift between written procedure and real practice.

- **Learning objectives have four parts.** Every objective is written from the *trainee's* viewpoint and built from target audience, behavior, condition, and standard. The behavior must be observable and measurable — vague verbs like "know," "understand," or "cover" are out; concrete verbs (measure, repair, demonstrate) are in. The condition states the constraints under which the behavior is *tested* (not how it was taught), and the standard sets the minimum acceptable performance (a percentage, a time limit, a tolerance).

- **Domains of learning.** Behaviors fall into cognitive, psychomotor, and affective domains. Cognitive behaviors ladder from knowledge (rote recall) → comprehension (interpret) → application (routine practice) → problem-solving (non-routine analysis, synthesis, evaluation). The same verb can sit at different levels depending on whether the activity is routine — so the trainer must use judgment, not a fixed verb list.

## Mental Models

- **Energy is the hazard; the license is the proof.** Frame every launch-safety decision around the energy that must be released to reach orbit and the public that energy could harm if released the wrong way. The license is simply the point at which the applicant has proven they control that energy to an acceptable expected-casualty level.

- **Probable, not possible.** MPL deliberately sets financial responsibility against *probable* maximum loss at a probability threshold, not the worst imaginable outcome. Carry this distinction into any risk-financing conversation: insuring against the truly maximum *possible* loss of a launch is neither how the system works nor how it is meant to work.

- **Three legs hold up the validation stool.** Analysis, ground test, and flight test each cover what the others cannot. Analysis is cheap and broad but blind to unknown interactions; ground test exercises hardware under stress but on the ground; flight test is the only place "unknown unknowns" reliably surface. Lean on all three in proportion to what the flight regime lets you simulate.

- **Software has more doors than you can lock.** Because software has far more paths than hardware and no mature reliability model, you cannot test your way to safety. Design for it: isolate safety-critical functions, give them a single deterministic path, define safe states, and check integrity continuously.

- **Walk the SHC matrix.** Locate each software function by its *control category* (how directly its failure leads to a hazard, and whether independent intervention exists) crossed with the *severity* of the consequence. The cell tells you how much analysis and test the function earns. If you cannot place a function on the matrix, you do not yet understand its safety role.

- **Train the group, not just the person.** Behavioral norms beat classroom instruction. If supervisors and old-timers break the rule, new hires "learn" to break it too, whatever the training said. Treat management support and organizational norms as more powerful than any single session, and recruit supervisors as ongoing reinforcers ("coaches"), not one-time attendees.

- **Objectives are testable promises.** A learning objective you cannot observe and measure is not an objective — it is a wish. If you can't state the behavior, the test condition, and the passing standard, you cannot tell whether the training worked.

## Anti-patterns

The source names these training pitfalls directly:

- **Skipping the needs analysis.** Trainers who don't analyze the group's needs find the same course unpredictably succeeds and fails, because they never accounted for differences in prior knowledge, motivation, and background.

- **Accepting unrealistic expectations.** Trying to train a large group with wildly varied need-to-know in one session, scheduling training at a hostile time with no compensation, or — most seriously — being asked to downplay dangers, encourage shortcuts, or overlook hazards. The source warns that deliberately misinforming trainees can create liability, and that a trainer may have to walk away rather than compromise standards.

- **Starting at the wrong level.** Assuming trainees have mastered prerequisites and pitching too high (a "disaster"), or pitching so low that experienced participants are bored.

- **Vague objectives.** Writing objectives around words like "know," "learn," or "understand" that cannot be observed or measured — so you cannot tell whether learning occurred.

- **Treating adults like children.** Approaching the trainer-learner relationship as teacher-to-child: condescending tone, reprimanding people in front of peers, schoolteacher body language. Adults want to know why a thing matters and how to apply it, and they recognize bad training when they see it.

- **Teaching to the trainer's own style.** Designing the session around how the *trainer* learns best (hand out a manual because the trainer reads well; throw people in unguided because the trainer experiments well) rather than around the learners' varied styles. Instructional media should be chosen to help the learner, not for the instructor's convenience.

## Key Takeaways

1. **AST licenses, the applicant proves.** The FAA does not dictate launch-vehicle design; it requires the developer/operator to run a system-safety process (per MIL-STD-882C, anchored by an SSPP) and demonstrate acceptable public risk to earn a license.
2. **Public risk is measured as expected casualty** — average human casualties per mission — and additional mitigation is required when the analysis shows risk is too high.
3. **Financial responsibility rests on MPL + DAMP**: enumerate accident scenarios, estimate probable (not possible) loss, and feed the casualty/damage estimate that sets the insurance requirement.
4. **Validate critical systems on three legs** — analysis, ground test, flight test — using qualification beyond expected environments, the Validation Acceptance Matrix, and post-flight predicted-vs-actual comparison; flight test is where unknown interactions surface.
5. **Software safety is design, not test-coverage.** Because software has unbounded paths and no mature reliability model, control it with isolation, safe states, deterministic paths, the SSSP's phase-mapped analyses, and the SHC matrix for prioritization.
6. **Training is a system safety element.** Run needs analysis → task analysis → measurable learning objectives → adult-oriented delivery → learning-style accommodation; and remember organizational norms outweigh any single session.

## Connects To

- **Earlier chapters of this pack** — the launch chapter applies the same hazard-identification and risk-acceptance discipline (PHA/SSHA, FMEA, FTA, the HRI) that the Handbook establishes generally; here it is specialized to expected casualty and licensing.
- **`dau-se-guidebook` pack** — MIL-STD-882C, the SSPP, and the review milestones (SRR/PDR/CDR/TRR) named in §13.5 line up with the defense SE review and configuration-baseline discipline; the SHC matrix mirrors the technical-risk grouping used there.
- **`nasa-*` packs** — the chapter explicitly draws on NASA Standard 8719.13A and Guidebook GB-1740.13-96 for software safety activities and phase-independent tasks; useful for cross-referencing NASA's software-safety doctrine.
- **`faa-sem` pack** — the FAA Systems Engineering Manual frames the agency's general SE process; this chapter is the commercial-space-safety application of that same agency's safety thinking.
- **RTCA DO-178B / airborne software assurance** — the DO-178B levels (A–E) reproduced in §13.5 connect this material to civil aviation software certification practice.
- **Training and competency frameworks** — Chapter 14's needs/task/objective method is a general instructional-design pattern; it pairs with any SE competency or workforce-development model that asks "what must this person be able to *do*."

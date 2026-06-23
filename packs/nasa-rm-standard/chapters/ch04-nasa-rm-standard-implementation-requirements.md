# Chapter — Implementation Requirements: Planning, Evaluation & Review

## Core Idea

NASA-STD-8729.1A is an **objectives-driven R&M framework**: rather than mandating a fixed list of analyses, it requires a project or program to plan, document, and demonstrate how it will meet reliability and maintainability *objectives and strategies*. Section 5 is where that philosophy becomes binding action. It splits into two halves. **Planning and Implementation (5.1)** governs how an organization sets up its R&M work — by embedding requirements into the project's existing safety and mission-assurance plan and specifying what that work will produce. **Evaluation and Review (5.2)** governs how that work is later judged at formal decision gates. The thread connecting both halves is *evidence*: a project does not satisfy the standard by performing activities, but by producing artifacts that show the objectives were addressed and the residual technical risk is acceptable to the relevant authority.

A second defining feature of this slice is its governance structure. Authority over whether the plan is adequate, and whether independent evaluation actually happened, rests with the **SMA Technical Authority** — a role distinct from the project team itself. The standard therefore institutionalizes a separation between those who do the R&M work and those who concur that it is sufficient.

## Frameworks Introduced (exact source names, when/how)

- **SMA Plan (per NPR 7120.5)** — Introduced in 5.1.1 as the home for R&M requirements. The standard does not create a new standalone R&M plan; it requires the project to establish and implement R&M requirements *inside* the Safety and Mission Assurance Plan that NPR 7120.5 already mandates. The SMA Plan is expected to address the objectives and strategies of the standard's Appendix A and the tables of Appendix B.
- **Appendix A (objectives and strategies)** — Referenced in 5.1.1 as the catalog of R&M objectives and strategies the SMA Plan should address.
- **Appendix B (tables of strategy implementation)** — Referenced repeatedly across 5.1.2 as the authority on *minimum scope*. The plan's scoping of each activity (5.1.2.d) and its evidentiary methods (5.1.2.e) are both calibrated against these tables, with deviations permitted only as documented alternatives.
- **FMEA — Failure Modes and Effects Analysis** — Named in 5.1.2.b and 5.1.2.c as an example of the kind of effective R&M activity that the plan's referenced objectives, requirements, and design/process standards are meant to enable.
- **CIL — Critical Items List** — Named in 5.1.2.c as a development output enabled by applying the design and process standards that affect system reliability.
- **MMOD (micrometeoroid and orbital debris)** — Listed in 5.1.2.a as one of the sources from which R&M criteria may be derived, alongside safety, mission success, and sustainment.
- **SMA Technical Authority** — The concurrence and verification role invoked in 5.1.3, 5.2.1, 5.2.2, and 5.2.3. It is the body that must agree the plan is sufficient, that confirms independent evaluation was carried out, and that concurs in the evidence presented at gates.
- **Milestone reviews and readiness reviews** — The two distinct review types defined in 5.2.2 and 5.2.3, each with its own evidentiary bar.

## Key Concepts

- **Plan by reference, not by restatement (5.1.2).** The R&M requirements and plan are expected to *specify and/or reference* the other program or project plans, documents, or models that carry the relevant detail. The standard treats the plan as a coordinating index that points to criteria, functional and performance requirements, applicable design and process standards, schedules, and organizational interfaces — rather than duplicating them.
- **Ten dimensions a plan must cover (5.1.2.a–j).** The plan's referenced material spans: derived R&M criteria; functional/performance objectives that enable quantitative reliability models and FMEA; applicable design and process standards enabling FMEA and CIL development; the scope of each activity against Appendix B minimums; the products serving as evidence (and any alternative evidentiary methods); cases where R&M products serve as design-requirement verification; a deliverables schedule tied to design, developmental, and operational milestones; the organizations and interfaces (such as risk management) executing the work; the independent-evaluation strategy where applicable; and lessons learned, best practices, and system heritage across the life cycle.
- **Evidence-and-products orientation.** Several sub-clauses (5.1.2.e, 5.1.2.f, 5.2.2) treat R&M *products* as the currency of compliance. The plan must name which products serve as evidence for each strategy, flag where products double as design-requirement verification, and the project must later present those products as proof at reviews.
- **Concurrence on sufficiency (5.1.3).** Before the work proceeds, the project must obtain the SMA Technical Authority's agreement that the requirements and plan — or any later update — are sufficient to address the objectives and strategies, scaled to the mission class.
- **Resource accountability (5.1.4).** The plan must name, in an appropriate planning document, which organizations supply the personnel, funding, tools, and other resources required to satisfy the R&M plan. Planning is not complete until ownership of the means is assigned.
- **Two review bars (5.2.2 vs 5.2.3).** At *milestone* reviews the project must show, with SMA Technical Authority concurrence, that objectives and strategies were adequately addressed consistent with the plan, that R&M products are at appropriate maturity and meet applicable standards, and that related technical risks are identified and acceptable. At *readiness* reviews the bar shifts toward operational fitness: confirm objectives and strategies were adequately addressed, and that the *residual* risks are acceptable. Maturity and standards-conformance dominate the earlier gate; residual-risk acceptance dominates the later one.
- **Independent evaluation as a verified obligation (5.1.2.i, 5.2.1).** Where applicable, the plan must lay out how R&M products and activities will be independently evaluated, scaled to the minimum scope of strategy implementation. Independence is not optional self-assertion: 5.2.1 makes the SMA Technical Authority responsible for verifying that the independent-evaluation strategy was actually implemented.

## Mental Models

- **The plan as a contract, the reviews as its enforcement.** Section 5.1 writes the promise — what will be done, to what scope, producing what evidence, on what schedule, with whose resources. Section 5.2 collects on it. Reading the two sections together shows the standard as a closed loop: every commitment scoped in 5.1.2 becomes a thing the project must show evidence for in 5.2.2 and 5.2.3.
- **Scope is a dial set by mission class and Appendix B, not by the practitioner.** The repeated phrase "commensurate with the minimum scope" (5.1.2.d, 5.1.2.i) and "commensurate with the mission class" (5.1.3) frames R&M rigor as a tailorable but floor-bounded quantity. Appendix B sets the floor; mission class sets where on the dial you land; the practitioner documents the choice and any alternative.
- **Two pairs of eyes, structurally enforced.** The doer (project/program) and the concurrer (SMA Technical Authority) are deliberately different roles. This is the writer/verifier split made organizational: the project produces the plan and the evidence; the Technical Authority concurs on sufficiency and verifies independence happened.
- **Maturity climbs as the gates progress.** The evidentiary language sharpens from milestone reviews (products at *appropriate maturity*, technical risks *acceptable*) to readiness reviews (*residual* risks acceptable). The model is a ratchet: each gate demands a higher-confidence statement about a smaller remaining unknown.
- **R&M is interdisciplinary by design, not by the R&M team alone (5.1.1).** The standard explicitly anticipates that some objective-relevant activities are performed outside the R&M discipline by programs or projects beyond a single practitioner's control. The mental model is coordination of interfaces among stakeholders, with the R&M plan ensuring nothing relevant falls between the disciplines.

## Anti-patterns

The source does not name anti-patterns in this slice. (5.1.1 does flag a structural hazard it requires projects to guard against — that objective-relevant activities may be performed by parties outside the R&M discipline, so projects *shall* coordinate the appropriate interfaces among stakeholders — but it frames this as a coordination requirement rather than naming a failure mode.)

## Key Takeaways

- R&M requirements live inside the **SMA Plan required by NPR 7120.5**, addressing the objectives and strategies of Appendix A and the tables of Appendix B — there is no separate freestanding R&M plan.
- The plan **references rather than restates**: it points to the criteria, requirements, standards, schedules, evidence products, and organizational interfaces detailed in other documents and models (5.1.2.a–j).
- **Appendix B sets the minimum scope** for each activity and for the evidentiary methods; alternatives to the referenced evidence are permitted but must be documented (5.1.2.d, 5.1.2.e).
- The **SMA Technical Authority must concur** that the plan is sufficient *before* the work proceeds and at every gate, and must **verify that independent evaluation was actually implemented** (5.1.3, 5.2.1).
- **Resources must be owned**: the plan names which organizations provide personnel, funding, tools, and other resources (5.1.4).
- **Milestone reviews** test adequacy-against-plan, product maturity, standards conformance, and acceptable technical risk; **readiness reviews** test adequacy and acceptable *residual* risk (5.2.2, 5.2.3).
- Compliance is demonstrated through **products presented as evidence**, including products that serve double duty as design-requirement verification (5.1.2.e, 5.1.2.f, 5.2.2).

## Connects To

- **NPR 7120.5 (NASA program/project management) and the SMA Plan** — the host document into which 5.1.1 inserts R&M requirements; this chapter cannot be applied without it.
- **Appendix A and Appendix B of this standard** — the objectives/strategies catalog and the minimum-scope tables that every scoping and evidentiary decision in 5.1.2 is calibrated against; a downstream chapter on those appendices closes the loop.
- **FMEA and CIL methods** — the concrete reliability analyses (5.1.2.b, 5.1.2.c) that the planning clauses exist to enable; connects to any analysis-technique chapter in the pack.
- **Systems Engineering / interdisciplinary integration** — 5.1.1's call for an interdisciplinary approach and coordinated interfaces ties R&M planning to the broader SE lifecycle and to risk management (named explicitly in 5.1.2.h).
- **Milestone- and readiness-review gates of the broader lifecycle** — 5.2's review types map onto NASA's lifecycle decision gates, connecting R&M evidence to program-level go/no-go decisions.
- **Independent evaluation / SMA Technical Authority governance** — the separation-of-roles principle in 5.1.3, 5.2.1, and the concurrence clauses connects to the wider mission-assurance authority structure across the standard.

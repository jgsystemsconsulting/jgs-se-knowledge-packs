# Chapter — V&V Approach in the AMS Lifecycle: Service Analysis, Strategic Planning, and Concept & Requirements Definition

> **Caveat — read this first.** This pack is the FAA's *verification-and-validation* companion to its Acquisition Management System (AMS), not a general SE methodology. It assumes you already know the AMS lifecycle (covered in the FAA SEM pack) and tells you specifically *what gets V&V'd, against which criteria, by whom, and before which decision point*. This chapter covers only the front of that lifecycle — the two earliest phases plus the research activity that feeds them. Where the source quotes process maturity language from CMMI v1.2 (SEI), this chapter paraphrases it; nothing here is a verbatim lift of CMMI text.

## Core Idea

The guideline organizes V&V around the **AMS lifecycle** rather than around a generic V-model. The whole acquisition is segmented into named phases, and V&V is not a one-time gate at the end — it runs continuously across every phase, with the *emphasis* shifting as the program matures. What stays constant is the toolkit (the same families of techniques verify and validate work products everywhere); what changes from phase to phase is *which* artifacts are under examination and *which* independent stakeholders own the review.

The unifying logic is that every critical work product, product component, and product — including the very criteria used to judge other items — is itself subject to systematic V&V by the program disciplines, throughout the lifecycle. Each functional discipline plans, performs, and reports its own V&V using the integrated processes its parent organization maintains. The job of this front-end chapter is to make that discipline concrete for the earliest decisions, where the program is still defining the problem rather than building the solution.

A second organizing idea is that V&V at the front of the lifecycle is fundamentally about *de-risking decisions on paper*. The earliest artifacts are planning and requirements documents, and getting them wrong is cheap to fix now and expensive to fix later. So the V&V effort concentrates on a small set of management documents and analyses whose quality determines whether the program is even ready to advance to the next gate.

## Frameworks Introduced (exact source names, when/how)

- **The AMS Lifecycle (five phases).** Introduced at the top of Section 3 as the spine of the entire approach. In order, the phases run: SASP (*Service Analysis & Strategic Planning*) → CRD (*Concept & Requirements Definition*) → IA (*Investment Analysis*) → SI (*Solution Implementation*) → ISM (*In-Service Management*). This chapter addresses the first two; later chapters carry the rest.

- **Research for Service Analysis (RSA).** Named as a *separate activity* — not a phase — that runs before and/or during the early phases. Its purpose is to mature and validate emerging concepts and technologies as candidates for investment and deployment in the National Airspace System (NAS), and to feed information into SASP, CRD, IA, and the opening of SI. Critically, the source states that RSA shares the *same* independent stakeholders and reviewers as those four lifecycle stages — its V&V is not a separate governance track.

- **Figure 3 — AMS Lifecycle Primary V&V Activities.** Cited as the visual that shows where the *primary emphasis* of V&V falls between major decision points. The source is explicit that the figure shows emphasis only; both verification and validation occur throughout, and the *complete* minimum set of required activities lives in Tables 1–6, not the figure.

- **The five early-lifecycle management documents.** The guideline names five documents required to support the critical early decision points, each subjected to formal, structured V&V:
  1. **Acquisition Program Baseline (APB)** — for an investment program segment, it fixes the baselines for schedule, cost, and performance.
  2. **Program Requirements Document (PRD)** — sets the operational framework and the performance requirements the program must meet.
  3. **Business Case** — captures the business-case analysis results and supplies the quantitative, analytical basis for the investment decision.
  4. **Implementation Strategy and Planning Document (ISPD)** — lays out the overall implementation strategy and plan.
  5. **Program Management Plan (PMP)** — describes how the service team will run the program to execute the ISPD's strategy.

- **Appendix B checklists (PRD, APB, ISPD, PMP).** Introduced as four checklists, one per document, that enumerate the key elements requiring verification or validation. For each element, the author must record the method used and the artifact produced. The framing is that these checklists give document authors a *structure* so the documents reliably carry the information approving authorities need to make lifecycle decisions. (The Business Case is handled separately — see below.)

- **Business Case Evaluation and Assessment Guideline / Independent Evaluation Review (IER).** The office of *Investment Planning & Analysis* owns V&V of the Business Case, per the AFI Business Case Evaluation and Assessment Guideline. Their **Independent Evaluation Review (IER)** is the artifact that satisfies the documentation and reporting requirements for Business Case V&V — i.e., the Business Case is routed through a dedicated review rather than the Appendix B checklist set.

- **Table 1 — V&V in Service Analysis & Strategic Planning.** The structured map for SASP. Each phase table lists four columns: the major decision point, the minimum work products to be V&V'd at that point, the criteria each work product is checked against, and the stakeholder responsible. The source flags that Table 1's content reflects AMS policy at publication, and that more detailed, current SASP guidelines and templates should be consulted.

- **Table 2 — V&V in Concept and Requirements Definition.** The same four-column structure for CRD, with the same caveat that detailed phase guidance and templates exist and supersede the table for current practice.

## Key Concepts

**Phase-by-phase ownership, common toolkit.** The V&V *techniques* (peer reviews, audits, analyses, checklists, testing, demonstrations, simulations, and the like) are shared infrastructure available in every phase. What is phase-specific is the *subject matter* under V&V and the *responsible reviewers*. This is why the guideline can be terse about methods in Section 3 — it spends its detail on the per-phase tables instead.

**Everything is V&V'd, including the criteria.** A subtle but load-bearing point: the items used *as* V&V criteria are themselves V&V'd. Criteria are not assumed-correct yardsticks handed down from above; they are work products that earn trust through the same systematic review as the things they measure.

**Decision points are the unit of organization.** Each phase table is anchored on a *decision point*, and the work products listed are the minimum that must clear V&V *before* that decision is made. The early-lifecycle decision points named here are the **Concept and Requirements Definition Readiness Decision** (the gate at the end of SASP) and the **Investment Analysis Readiness Decision** (the gate at the end of CRD). V&V exists to make those gates trustworthy.

**SASP — deciding what capability the agency needs.** Service Analysis & Strategic Planning is the process for determining the capabilities the agency must have, now and later, to meet its goals and serve its customers. Its results are captured as the *"as-is"* and *"to-be"* states of the **Enterprise Architecture (EA)**, plus the roadmaps that connect them; the responsible Line of Business folds these into business plans and operating plans. The output is the information needed to decide which service shortfalls or service-improvement ideas get admitted into the agency's strategic-planning documents.

**The three SASP V&V targets.** During SASP, the primary V&V emphasis falls on three artifacts: the **ISS Risk Factors Assessment**, the plan for **Concept & Requirements Definition**, and the **Preliminary Shortfall Analysis**. Table 1 ties each of these to its responsible stakeholder and to its validation and verification criteria. Notably, the *validation* criteria for these planning artifacts are largely the agency's strategic and architectural reference set — the EA, the NextGen Implementation Plan, the NAS Segment Implementation Plan, FAA Strategic Initiatives, the NARP (where applicable), and the NAS ConOps — while *verification* criteria are the procedural references (the SASP/CRD Guidelines, shortfall-analysis guidance and templates, and AMS Policy).

**Security enters at the very front.** Even at SASP, the **ISS Risk Factors Assessment** is in scope, validated against the **FIPS-199 Security Categorization Table** and verified against the **Information Security Guidance for System Acquisition (ISGSA)**, with AMS Policy as a verification reference. Information-system security is treated as a first-phase concern, not a late add-on.

**CRD — turning a need into preliminary requirements.** Concept & Requirements Definition takes the priority operational needs that sit in the EA and turns them into *preliminary* requirements, paired with a solution **Concept of Operations** for the capability being sought. CRD also quantifies the service shortfall in enough detail to support realistic preliminary requirements and a first estimate of costs and benefits, and it identifies the most promising alternative solutions — one of which must be the alternative already in the EA.

**The CRD V&V emphasis.** During CRD, the primary focus is *validation* of: the preliminary program requirements; the concept of use; the EA products and amendments; the **Preliminary ISS Assessment**; the plan for initial Investment Analysis; and the shortfall analysis — all aimed at confirming the existing or planned product genuinely addresses the mission need. Table 2 decomposes these into per-work-product criteria.

**Stakeholder breadth widens at CRD.** In SASP the responsible parties are dominated by the Lines of Business (Mission Support) / Service Team (NAS), with Investment Planning & Analysis and the Advanced Concepts and Technology Development Office appearing on the readiness decision. By CRD, **ANG Engineering Services** joins as a co-responsible reviewer on most work products, and the **Enterprise Architecture Control Board (NAS and Mission Support)** owns verification of the EA products and amendments. The deeper the program goes, the more engineering and architecture-governance bodies are pulled into the V&V.

**Criteria reuse across phases.** The same strategic/architectural artifacts (EA, NextGen Implementation Plan, NAS Segment Implementation Plan, NAS Requirements Documents, FAA Strategic Initiatives) recur as validation criteria for many CRD work products. The verification side adds engineering-specific references such as the **Program Requirements Document template**, the **System Engineering Manual**, and the **NAS Integrated Systems Engineering Framework**. The Initial Investment Analysis Plan and Preliminary ISS Assessment carry the security thread forward (again FIPS-199 for validation, ISGSA for verification).

## Mental Models

- **V&V as a continuous current, not a final gate.** Picture verification and validation as flowing through the entire lifecycle, with Figure 3 marking only where the current runs strongest between decision points. If you reach for "the V&V phase," you've mis-modeled it — there isn't one. There are V&V *activities in every phase*, and the tables, not the figure, define the minimum set.

- **The maturity ratchet, seen from the V&V side.** The companion SEM pack frames the lifecycle as a maturity ratchet; this pack shows what that ratchet costs in assurance. The *same* anchor artifacts (EA, shortfall analysis, ConOps, requirements) reappear phase after phase, but each reappearance is re-V&V'd at higher resolution and against a growing criteria set. Validate the preliminary version against strategy in SASP; re-validate the sharpened version against strategy *plus* engineering references in CRD.

- **Criteria are evidence, not axioms.** Because the items used as V&V criteria are themselves V&V'd, treat every yardstick in the tables as a work product that earned its place. If a criterion is stale or wrong, the assurance it confers is illusory — which is exactly why the source repeatedly cautions that detailed, current phase guidance supersedes the published tables.

- **Decision-readiness is the real product of front-end V&V.** The deliverable at each early gate is not the document itself but the *justified confidence* that the document is good enough for the approving authority to decide on. The Appendix B checklists exist to manufacture that confidence by forcing each key element to name its method and its evidentiary artifact.

- **Two governance tracks for one program.** Most early artifacts run through the Appendix B / Tables 1–2 machinery owned by Lines of Business, engineering, and architecture bodies. The Business Case runs through a *parallel* track owned by Investment Planning & Analysis and closed out by the IER. Hold both tracks in view — a program is not V&V-complete at a decision point until both have reported.

- **Security and architecture are front-loaded, not bolted on.** ISS assessments and EA alignment appear in the *first* phase and intensify in the second. Model information security and enterprise-architecture conformance as constraints present from day one, validated against FIPS-199 / ISGSA and the EA respectively, rather than as downstream compliance checks.

## Anti-patterns

The guideline is written as positive, prescriptive guidance and does not present a labeled catalogue of named anti-patterns. The closest it comes are cautions stated directly in the slice:

- **Reading Figure 3 as the definition of required V&V.** The source explicitly warns that the figure shows only the *primary emphasis* between decision points; treating it as the complete activity set — instead of consulting Tables 1–6 — would under-scope a program's V&V.
- **Treating the published phase tables as current authority.** Both Table 1 and Table 2 carry footnotes stating their content reflects AMS policy *as of publication* and that detailed, current phase guidelines and templates exist and should be reviewed. Relying on the tables alone, without checking for superseding guidance, is flagged as a mistake.
- **Skipping front-end paperwork V&V to "save time."** The whole front-end emphasis on V&V'ing planning and requirements documents before the readiness decisions implies the inverse failure: advancing to a gate on un-verified, un-validated documents that the approving authority then cannot soundly decide on.

## Key Takeaways

- The approach is organized by the **AMS lifecycle** — SASP, CRD, IA, SI, ISM — with V&V running across every phase and only its *emphasis* shifting; this chapter covers the front two phases plus the **RSA** activity that feeds them.
- **RSA** is a non-phase activity that matures and validates concepts/technologies for the NAS and shares the *same* independent stakeholders and reviewers as SASP, CRD, IA, and early SI.
- Five early management documents — **APB, PRD, Business Case, ISPD, PMP** — anchor the critical early decisions and get formal, structured V&V; **Appendix B** supplies checklists for PRD, APB, ISPD, and PMP, while the **Business Case** is V&V'd separately by Investment Planning & Analysis and closed out by the **IER**.
- **Every** critical work product — *including the criteria used to judge others* — is systematically V&V'd; criteria are earned evidence, not assumed-correct yardsticks.
- **SASP** decides what capability the agency needs, captured as the EA's *as-is*/*to-be* states and roadmaps; its three primary V&V targets are the **ISS Risk Factors Assessment**, the **Concept & Requirements Definition Plan**, and the **Preliminary Shortfall Analysis**.
- **CRD** turns EA-resident needs into *preliminary* requirements and a solution ConOps, quantifies the shortfall, and identifies promising alternatives (one of which must be the EA's); its V&V emphasis is validation of the preliminary requirements, concept of use, EA products/amendments, shortfall analysis, initial IA plan, and **Preliminary ISS Assessment**.
- Stakeholder breadth **widens** from SASP to CRD — **ANG Engineering Services** and the **Enterprise Architecture Control Board** join the Lines of Business / Service Team — and information security (**FIPS-199**, **ISGSA**) plus EA conformance are front-loaded into the earliest phases.
- The published phase tables (Tables 1–2) are **snapshots of policy at publication**; detailed current phase guidance and templates take precedence.

## Connects To

- **FAA Systems Engineering Manual (sibling pack).** The SEM defines the AMS lifecycle, its decision points, and the requirements-maturation ratchet (pPR → iPR → fPR); this pack is the *assurance overlay* on that same skeleton. Read the SEM's "what happens in each phase" against this pack's "what gets V&V'd, against what, by whom" for a complete front-end picture.
- **Later chapters of this pack.** This chapter handles SASP and CRD; subsequent chapters extend the same Table-driven, decision-point-anchored V&V treatment into Investment Analysis, Solution Implementation, and In-Service Management — and to RSA, which threads through all of them.
- **CMMI v1.2 (SEI) — paraphrased.** The guideline draws on CMMI process-maturity concepts for its V&V framing; this pack treats those ideas in paraphrase only. For the canonical maturity-model treatment of Verification and Validation as process areas, go to the CMMI source directly.
- **NASA NPR 7123.1 / NASA SE Handbook and the DAU SE Guidebook (sibling packs).** The AMS readiness decisions are the civil-agency analogue of NASA KDPs and DoD milestone decisions; the "V&V the planning and requirements documents before the gate" pattern is shared government-acquisition DNA. The criteria sets differ, but the decision-readiness logic is the same.
- **Enterprise architecture and information-security packs.** SASP/CRD lean heavily on the EA (as-is/to-be states, roadmaps, EA Control Board governance) and on information-security references (FIPS-199 categorization, ISGSA). Any pack covering enterprise architecture or system-acquisition security connects here as the *source* of the criteria this pack validates against.
- **ISO/IEC/IEEE 15288 and the SEBoK (sibling packs).** The phase structure and the verification/validation distinction map onto the broader SE canon; use 15288 and the SEBoK to translate FAA-specific phase and artifact names back into vendor-neutral SE vocabulary.

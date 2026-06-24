# Chapter 1 — Introduction: V&V Terms, Definitions, and Philosophy

> **Caveat — read this first.** This pack is the FAA's *verification and validation* companion to its acquisition doctrine, not a standalone V&V theory. It assumes the FAA Acquisition Management System (AMS) lifecycle and the FAA Acquisition Management Policy as its surrounding scaffolding, and it borrows its core verb-definitions from the Carnegie Mellon Software Engineering Institute's CMMI for Development, Version 1.2 (2006). Wherever this chapter restates those CMMI definitions, it does so in paraphrase — the originals are a copyrighted SEI model and should be cited, not copied. Treat this as the FAA dialect of a widely shared V&V grammar, wrapped around one agency's decision-point machinery.

## Core Idea

V&V, as this guidelines document frames it, is a *disciplined, lifecycle-long assessment* applied to selected products together with the work products and product components that lead up to them. Its purpose is twofold and durable: to confirm that a quality product is actually being built, and to confirm that the thing being built satisfies the operational requirements and service needs that justified it. The document is not a procedure manual so much as agency-wide guidance — it defines the vocabulary, shows how V&V is accomplished, and walks the application of V&V through each phase of the AMS lifecycle.

The central premise is that verification and validation are *complementary but distinct*, and that their relative weight shifts as a program matures. Early on, when the mission definition, operational concept, and requirements are still soft, validation against needs dominates. Later, as the product and its components solidify, verification against specifications carries more of the load. The ordering and emphasis of "did we build it right" versus "did we build the right thing" is therefore not fixed; it tracks the maturity of the mission definition, the concept, the requirements, and the product itself.

The third organizing premise is that V&V exists *to serve decisions*. Senior management commits to or kills an investment initiative at formal milestones — the AMS decision points — and the entire value of V&V is that it makes the information feeding those decisions accurate and dependable, so that each transition through the lifecycle rests on knowledge and acceptable risk rather than optimism.

## Frameworks Introduced (exact source names, when/how)

- **FAA AMS Lifecycle V&V Guidelines (Version 3.0, dated April 2017)** — the document itself. Section 1 establishes its scope: provide general guidance for applying V&V policy across the AMS lifecycle by defining terminology, illustrating how V&V is accomplished, and describing its application in each lifecycle phase. It is explicitly a living document, updated as better practices and lessons emerge, with the current version hosted on the FAA Acquisition System Toolset (FAST).

- **FAA Acquisition Management System (AMS)** — named throughout Section 1 as the lifecycle this guidance wraps around. The AMS lifecycle (defined in the FAA Acquisition Management Policy) is the sequence of phases and decision points against which V&V is scheduled and reported.

- **FAA Acquisition Management Policy** — cited as the authority that defines the AMS lifecycle the guidelines apply across.

- **Capability Maturity Model Integration (CMMI) for Development, Version 1.2** — published by the Carnegie Mellon Software Engineering Institute (SEI) in August 2006 — the cited source for the formal definitions of verification and validation. The document states its V&V definitions are consistent with CMMI and characterizes CMMI as an internationally recognized development-and-acquisition model that the Government Accountability Office (GAO) relies on when conducting its quality audits and process assessments. *(Paraphrased throughout this pack; never quoted verbatim.)*

- **Enterprise Architecture (EA)** — introduced in Section 1.3 as a *major V&V source criterion*. The EA sets out the operational and technical framework covering every FAA capital asset, laying out the current and target architectures plus the transition strategy that bridges them. It is itself subject to V&V under these guidelines, and it is the premise against which critical work products — needs, requirements, concepts of use, strategies — are verified and validated. The EA also helps size and scope investments by complexity (interface counts, stakeholders impacted, and the like).

- **Quality Assurance (QA)** — named in the Section 1.2.2 note as a *complementary but separate* process. The document draws an explicit boundary: V&V confirms requirements are met, the project stays aimed at user/mission needs, and risk is managed; QA confirms that the established processes were followed in producing the product.

- **Supporting EA-anchored artifacts** — the Section 1.3 discussion names the FAA Strategic Initiatives, the National Airspace System (NAS) Requirements Documents, the NAS Segment Implementation Plan (NSIP), and the EA infrastructure roadmaps as the planning structure the EA supports and integrates.

## Key Concepts

**The three objects of V&V: work product, product component, product.** The document defines a deliberate hierarchy and applies V&V to all three:

1. **Work product** — anything that represents, defines, or directs the final product. The document's enumerated examples span designs, descriptions, specifications, documents, processes and procedures, models and simulations, prototypes, and contracts. These are the early-lifecycle artifacts (for instance, the solution concept of operations and the program requirements document) that steer development.
2. **Product component** — a lower-level part, element, or module that gets integrated upward to form the product. There can be multiple nested levels of components.
3. **Product** — the delivered end item, whether a system, a service, a facility, or an operational change, destined for a customer or end user.

V&V flows up this hierarchy: work products are verified and validated first, then components as they become available and before integration, then the final product before it is accepted into the operational environment. The same item may be put through V&V more than once across its life if it is modified or if additional levels of assurance are required.

**Verification — "built right."** Paraphrasing the cited CMMI definition: verification confirms that the selected work products meet the requirements specified for them, spanning both the delivered end product (a system, a service, or an operational change) and the intermediate artifacts, each checked against whatever requirements apply. The document stresses that verification is *inherently incremental* — it runs throughout development, beginning at the initial requirements, carrying through each successive change, and concluding once the finished end product itself has been verified.

**Validation — "the right thing."** Again paraphrasing CMMI: validation confirms that a finished product, or one of its components, will deliver its intended purpose and meet user needs once it sits in the environment it was built for. The validation methods reach not only the end product and its components but also a chosen subset of work products — and those chosen should be the ones that most reliably forecast how well the finished item will meet its purpose and the users' needs. Validation can address any facet of the product across any of its intended settings — operation, training, manufacturing, maintenance, or support.

**Who performs V&V, and on whose work.** V&V is performed on both government and contractor work products, components, and products, and the obligation to perform it falls on both government and contractor organizations. It is not delegated to one side.

**V&V is required, both parties, both directions.** Because work products feed forward — each verified-and-validated artifact becomes the baseline for V&V of the next — neglecting V&V early corrupts everything that inherits from it.

**V&V as a decision-and-risk instrument.** Across the AMS lifecycle, V&V is positioned as a systematic activity that improves a program's efficiency and effectiveness, supports decision-making, and manages risk. At each decision point, senior management needs verified and validated work products that report the genuine progress and status of the service or product, so the milestone choice rests on accurate, dependable information.

**The EA as both source criterion and feedback recipient.** The Enterprise Architecture serves as the yardstick for verifying and validating critical work products — needs, requirements, concepts of use, strategies — and it closes the loop: the EA is itself revised and sharpened from whatever results and knowledge V&V yields.

## Mental Models

- **"Built right" vs. "right thing built."** The compact mnemonic the document leads with: verification asks whether the product was built right against its specifications; validation asks whether the right product was built to fulfill its intended use. Carry both questions through every artifact — a specification can be flawless against its template (verifies) and still satisfy the wrong need (fails validation).

- **The verify-against-requirements, validate-against-needs pair.** The document's worked example crystallizes the split: a system specification is *verified* by checking it against the mandated standards and templates that govern its content and format, and *validated* against the needs captured in the higher-level program requirements document (the specification that expresses mission needs as operational requirements). Verification looks down at the spec; validation looks up at the need.

- **The relay baton.** Each work product, once verified and validated, becomes the basis for the V&V of the *next* work product or of the final product. This puts disproportionate weight on the artifacts created earliest — gap analyses, solution concept-of-operations documents, requirements documents — because every downstream verification inherits their correctness. Validate the front of the chain hardest; that is where "the right product" is decided.

- **Shifting center of gravity.** Because the relative significance of verification and validation moves with the state of the mission definition, concept, requirements, and product, the right model is a sliding balance, not a fixed split. Expect validation-heavy effort while needs and concepts are still forming, and verification-heavy effort as the design and product harden.

- **V&V as the EA's mirror.** The Enterprise Architecture supplies the criteria V&V judges against *and* absorbs what V&V learns. Think of it as a two-way membrane: top-down it constrains and grounds critical work products in the agency's operational/technical framework; bottom-up it is refined by the evidence V&V generates.

- **V&V ≠ QA.** Keep the two processes mentally separate even when they run together. V&V is product-and-outcome focused — are requirements met, is the program still aimed at the mission, is risk under control. QA is process-focused — were the established procedures actually followed. Conflating them is a category error; they answer different questions.

## Anti-patterns

The guidelines document is written as positive guidance and does not present a labeled catalogue of named anti-patterns, so this section is intentionally restrained. The nearest things to cautions stated in this slice are framed as distinctions to respect rather than named failure modes:

- **Collapsing V&V into QA (or vice versa).** The Section 1.2.2 note exists precisely to prevent treating "the process was followed" (QA) as if it were evidence that "requirements are met and the mission is served" (V&V). They are complementary, not interchangeable.
- **Under-validating early work products.** Because the front-of-lifecycle artifacts (gap analyses, ConOps, requirements documents) seed every later verification, the document's emphasis implies that failing to validate them — confirming they capture the *right* needs — propagates the wrong product forward undetected.

## Key Takeaways

- The pack is the FAA's agency-wide V&V guidance (Version 3.0, April 2017), defining terminology, showing how V&V is done, and mapping it onto every phase of the AMS lifecycle; it is a living document hosted on FAST.
- **Verification = built right** (work products meet specified requirements, incrementally, end product included); **Validation = right thing built** (the finished product or component will deliver its purpose and satisfy users once in its operating environment). Both definitions are drawn — and here paraphrased — from CMMI for Development v1.2 (SEI, 2006).
- V&V applies to a three-level hierarchy — **work product → product component → product** — and flows upward: artifacts first, components before integration, the final product before operational acceptance. Any item may undergo V&V more than once.
- Both **government and contractor** organizations are required to perform V&V, on both parties' work products, components, and products.
- The relative **emphasis of verification vs. validation shifts** with the maturity of the mission definition, concept, requirements, and product — it is a sliding balance, not a fixed rule.
- The **Enterprise Architecture** is a major V&V source criterion (the basis for V&V'ing needs, requirements, concepts of use, and strategies) and is itself refined by V&V results — a closed loop.
- V&V exists **to support decisions and manage risk**: it makes the information feeding each AMS decision point accurate and dependable, so transitions rest on knowledge and acceptable risk.
- **V&V and QA are complementary, not the same**: V&V targets requirements/mission/risk; QA targets adherence to established processes.

## Connects To

- **FAA Systems Engineering Manual (SEM) (sibling pack).** The SEM wraps SE around the same AMS lifecycle and the same decision points; this V&V pack is the assurance discipline that carries SE products cleanly through those gates. Read the SEM's requirements-maturity ratchet (pPR → iPR → fPR) alongside this chapter's "validate the early work products hardest" emphasis — they describe the same front-loaded risk.
- **CMMI for Development (SEI).** The verification and validation definitions trace directly to CMMI v1.2; any pack grounded in CMMI process areas (verification, validation, the generic/specific practices) shares this pack's vocabulary and is the upstream source for it.
- **GAO assurance and audit guidance (GAO-aligned sibling packs).** The document explicitly notes that GAO leans on CMMI when it audits quality and assesses processes, linking this V&V framing to the GAO cost/schedule/TRA assurance traditions.
- **NASA NPR 7123.1 / NASA SE Handbook (sibling packs).** NASA's verification-vs-validation distinction and its gate-by-gate evidence model are the civil-space analogue of the FAA's decision-point V&V; the AMS decision points are the FAA counterpart to NASA Key Decision Points.
- **Enterprise Architecture / DoDAF-style frameworks (sibling packs).** The EA's role here as both source criterion for V&V and recipient of V&V feedback connects to any pack treating architecture as the authoritative reference baseline against which requirements and concepts are checked.
- **Downstream chapters of this pack.** This chapter sets up Section 2 (V&V implementation guidance — planning, performing, reporting, decision support) and Section 3 (key work products, product components, and products with their responsible stakeholders at each AMS decision point and phase), both of which operationalize the terms and philosophy defined here.

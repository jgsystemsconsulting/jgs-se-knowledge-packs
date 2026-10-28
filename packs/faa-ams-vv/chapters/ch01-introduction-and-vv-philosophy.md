Sources: FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0 (January 2023), printed pages 1-7 (Section 1, including 1.3.1 V-Model Implementation and 1.3.2 Agile Acquisition/Shift-Left Principles in V&V).

# Chapter 1: Introduction and the V&V Philosophy

> Foundational chapter. This covers the guideline's scope, terminology, and philosophy of verification and validation (V&V) as a lifecycle-wide, decision-support discipline rather than an end-stage test. The core verification and validation definitions trace to CMMI for Development, Version 1.2 (SEI, August 2006) and are paraphrased here, never copied.

## Core Idea

The guideline applies V&V policy across the FAA Acquisition Management System (AMS) lifecycle. Its stated job is threefold: define the terms, show how V&V is actually accomplished, and describe what gets V&V'd in each AMS phase. Planning, performing, and reporting guidance rounds this out, all in service of decision support.

V&V itself is a disciplined approach for assessing a product together with its product components and work products across the life of a system, service, enterprise capability, facility, or operational change. The point is that a quality product gets built and that the built thing satisfies operational requirements and service needs. The guideline is explicit that the order and the relative weight of verification versus validation can shift over the lifecycle as mission definition, operational concept, requirements, development, and the product itself mature.

Both government and contractor organizations are required to perform V&V, and it is performed on both parties' work. Any work product, component, or product may also be subject to V&V more than once if it is modified, or if additional levels of V&V are required.

## Frameworks Introduced

### The three-tier object hierarchy

V&V attaches to three kinds of object, and the guideline defines each (defined terms kept short):

1. **Work product.** Anything that represents, defines, or directs the final product: documents, processes, procedures, designs, descriptions, specifications, simulations, models, prototypes, contracts.
2. **Product component.** A lower-level element integrated upward to produce the product, and there may be multiple levels of components.
3. **Product.** The final or end system, service, enterprise capability, facility, or operational change, delivered to the customer or end user.

The early AMS phases generate work products (a solution concept of operations, a program requirements document) that define and direct everything downstream. Components are V&V'd before integration. The final product is V&V'd before acceptance into the operational environment.

### Verification versus validation

Verification confirms that selected work products meet specified requirements, across the product and intermediate work products. It is inherently incremental: it begins with the initial requirements and continues through every subsequent change until the completed product is verified.

Validation confirms that the product, or an end product component, will fulfill its intended purpose and user needs when placed in its intended environment. Validation methods get applied to the product, its components, and selected work products, and the selection favors the best predictors of how well the product will satisfy purpose and user needs. Validation can cover all aspects of the product in its intended environments: operation, training, manufacturing, maintenance, and support services.

Both concepts rest on CMMI for Development, Version 1.2 (Carnegie Mellon Software Engineering Institute, August 2006), the footnote the guideline prints on page 3. The guideline notes that CMMI is a best-practices model the Government Accountability Office uses as a basis for quality audits. The formal definitions under that footnote are paraphrased here and never copied. The same footnote draws the QA boundary: V&V and Quality Assurance are complementary but different. V&V targets whether requirements are met, whether the project serves user and mission needs, and whether risk is managed. QA targets whether the established processes for producing the product were followed.

## Mental Models

**The EA source criterion and feedback loop.** The Enterprise Architecture (EA) is a major V&V source criterion and is itself subject to V&V under the guideline. The EA defines the operational and technical framework for every FAA capital asset: current and target architectures plus the transition strategy between them. V&V of critical work products and products is premised on the EA, and the EA supports FAA Strategic Initiatives, NAS Requirements Documents, and the NAS Segment Implementation Plan. The EA is also used to size and scope investments (interface counts, stakeholders impacted), and it is updated and refined from the knowledge V&V produces. A closed loop: architecture grounds criteria, criteria ground checks, checks feed architecture.

**Verify down, validate up.** A generic flow: current work products, components, and products are verified against requirements and validated against needs, both identified in previous work products, components, and products. A system specification, for example, is verified against the standards and templates that define its content and format, and validated against the needs captured in the program requirements document. Each verified-and-validated work product then becomes the basis for V&V of future ones. That is why the guideline stresses early artifacts (gap analyses, solution ConOps, requirements documents): they must be validated so the right product gets built.

**The V-Model as AMS overlay.** Section 1.3.1 uses the V-Model (Figure 3) to show V&V running through every AMS phase. The left side of the V covers work products: concepts of operation, requirements, specifications, architectural design. The primary V&V purpose there is strategic planning support, making sure key decisions rest on thoroughly vetted documentation; loopback arrows signify V&V against criteria in previous work products. The right side covers test and evaluation of systems, services, and capabilities through development and implementation, confirming that what comes out of the left side is effective and suitable for FAA operations. The middle of the V is cross-referencing: left-side activities should stay conscious of future integration needs; right-side activities must remember the driving operational concepts and requirements that originated on the left.

**Agile acquisition and shift-left.** Section 1.3.2 lets programs apply Agile principles: small batches of work, fast learning cycles, and multiple rapid deliveries of incremental capability. Work products are treated as fluid and continually maturing, so program offices, engineering, users, developers, and V&V/T&E stakeholders work across disciplines, iteratively defining, prototyping, and changing scope and requirements. An operational tester may collaborate with developers from the concepts-of-operations and requirements phase onward, through all of T&E.

Shift-Left is the companion practice: find and prevent defects early, because major defects are known to be introduced early in acquisition but surface late, cost more, and resist fixing. Moving tasks left creates opportunities to V&V work products as soon as possible, with testers engaged on program office teams early in the lifecycle. Early-and-often V&V reduces the chance of deficiencies in fielded systems and lets acquisition start sooner on an acceptable level of immature concepts and requirements. Figure 3's own caption calls this out: shift-left V&V with evolving and maturing system and service capabilities in the NAS.

## Key Takeaways

- V&V spans the whole AMS lifecycle, on both government and contractor work, and repeats whenever an item is modified.
- Three tiers: work product, product component, product. V&V flows up the hierarchy.
- Verification asks whether the thing was built right; validation asks whether the right thing was built. Both questions, every item.
- The definitions trace to CMMI for Development v1.2 (SEI, August 2006); this pack paraphrases them.
- V&V is not QA: V&V chases requirements, mission, and risk; QA chases process adherence.
- The EA both grounds V&V criteria and absorbs V&V results.
- Shift-left: engage testers early, V&V early and often, because defects born early cost most late.

## Connects To

- `ch02` turns the philosophy into implementation mechanics: planning elements, independence, method catalogs, reporting, decision support.
- `ch03` and `ch04` walk the AMS lifecycle phase by phase, naming what gets V&V'd at each decision point.

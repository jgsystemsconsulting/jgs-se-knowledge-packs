# Chapter 1 — Scope, CM Fundamentals & Definitions

> **Version note:** This pack is built from the current **MIL-HDBK-61B** (the 2020 release, cataloged with Change 1). It is *not* the superseded 2001 MIL-HDBK-61A(SE). Where older guidance differs, follow 61B and its EIA-649 referenced suite.

## Core Idea

MIL-HDBK-61B is a DoD *guidance* document — explicitly advisory, not a citable requirement — that explains how program managers, systems engineers, logistics managers, and others responsible for Configuration Management (CM) should plan, perform, and contract for CM across a defense system's life cycle, spanning both acquisition and sustainment. The handbook does not invent its own CM rules; instead it points the practitioner to the adopted commercial standard suite (the EIA-649 family) and adds the DoD-specific implementation and tailoring layer on top. CM's central purpose is to keep a product's performance, functional, and physical attributes consistent with its requirements, design, and operational information throughout the product's life — so that everyone working with the product is operating from correct, current, traceable information.

## Frameworks Introduced (exact source names, when/how)

The slice introduces the governing standards landscape and the operative CM structure:

- **SAE EIA-649 (Configuration Management Standard)** — the commercial CM standard DoD has adopted as its baseline; named as the source of CM principles and of the many alias terms used across different industries. Listed both in the practitioner "toolkit" (§1.1.1) and in Non-Government publications (§2.3).
- **SAE EIA-649-1 (Configuration Management Requirements for Defense Contracts)** — the defense-contract requirements companion to EIA-649; the handbook provides recommendations for *tailoring* its requirements when placing them on contract. Also the terminology source for the handbook's definitions.
- **GEIA-HB-649 (Configuration Management Standard Implementation Guide)** — the implementation guide rounding out the three-item toolkit the handbook says a DoD configuration manager needs to interpret MIL-HDBK-61 fully.
- **GEIA-859 (Data Management)** and **IEEE 828 (Configuration Management in Systems and Software Engineering)** — referenced supporting non-Government publications.
- **ISO 9000, ISO 10007 (Guidelines for CM), and ISO/IEC/IEEE 12207** — international standards forming part of the referenced document base.
- **The five CM functions (§1.1.2)** — the operative process framework introduced here. The handbook organizes CM into five activities: planning the CM program; identifying the configuration; controlling changes to it; accounting for its status; and verifying and auditing it. Those five, together with the underlying CM principles, form a deliberately flexible implementation structure; the handbook stresses that the practitioner decides the appropriate *level* of implementation per configuration item.
- **Government framing documents (§2.2)** — DoDI 5000.02 (Operation of the Defense Acquisition System), MIL-STD-961, MIL-STD-31000 (Technical Data Packages), DoD 5010.12-M, and FAR Parts 7 and 46 — situate CM within DoD acquisition policy and contracting.

## Key Concepts

**CM as a management process.** Configuration Management is defined as a management process for establishing and maintaining consistency between a product's performance, functional, and physical attributes and its requirements, design, and operational information across its life. The configuration manager is the person responsible for ensuring that process runs successfully for a given system or item.

**Configuration and baselines.** A *configuration* is the collection of an item's descriptive and governing characteristics — expressible in functional terms (what it must do) and physical terms (what it is and consists of when built). A *configuration baseline* is an agreed description of a product's attributes at a point in time that serves as the reference for managing change; it is captured in approved, released, revision-controlled documentation. The slice names the three baseline tiers that recur throughout CM: the **Functional Baseline (FBL)**, **Allocated Baseline (ABL)**, and **Product Baseline (PBL)**, each with its corresponding configuration documentation (FCD, ACD, PCD).

**Configuration Item (CI).** The unit of CM. A CI bundles hardware and/or software that has been picked out for CM and is handled as one managed entity — the part of a configuration that delivers an end-use capability and can be pinned to a unique identity at a defined reference point. HWCI and CSCI are the hardware and computer-software specializations.

**The five functions, briefly:**
- *Configuration Identification* selects the product attributes, organizes and states associated information, assigns unique identifiers, releases CIs and their documentation, and establishes baselines.
- *Configuration Control / Change Management* is the systematic process ensuring that changes to released documentation are identified, documented, impact-assessed, approved at the right authority level, incorporated, and verified.
- *Configuration Status Accounting (CSA)* formalizes recording and reporting of established configuration information, the status of proposed changes, and the implementation of approved changes — keeping the record current, accurate, and retrievable.
- *Configuration Verification and Audit* confirms the actual product against required attributes (FCA verifies functional achievement against the FCD/ACD; PCA verifies the as-built item against its design documentation and finalizes the product baseline).

**Change classification.** Engineering changes are classified as *Major (Class I)* — affecting approved functional/allocated/product requirements, or touching cost, warranties, or contract milestones — versus *Minor (Class II)*, which is any approved-documentation change that is not Class I. Changes flow through an **Engineering Change Proposal (ECP)**, are dispositioned by a **Configuration Control Board (CCB)**, and the decision is recorded in a **CCB Directive (CCBD)**. A **Notice of Revision (NOR)** captures documentation revisions required after ECP approval; a **Request for Variance (RFV)** is how a supplier requests a temporary, bounded departure from product definition without revising it.

**Authority and roles.** The **Current Document Change Authority (CDCA)** is the activity currently responsible for a document's content and the sole approver of changes to it. The **tasking activity** (buyer) imposes requirements via contract or tasking directive; the **performing activity** (seller, contractor or Government) executes them.

**Nonconformance vocabulary.** *Nonconformance* is a unit's failure to meet a specified requirement; a *defect* is any nonconformance of a characteristic. *Rework* fully eliminates a nonconformance (restoring full conformance); *repair* only reduces it (the characteristic still does not fully conform). *Retrofit* incorporates approved new design or software code into already-delivered, accepted products, guided by a *retrofit instruction*.

**Interchangeability.** An *interchangeable item* is functionally and physically equivalent to another and can substitute without selection for fit/performance and without altering adjoining products (except adjustment); a *replacement item* is interchangeable but needs additional operations such as drilling, reaming, or shimming to install.

**Form, fit, function, interface.** *Form* is the physical envelope (shape, size, mass, and — for software — language and media); *fit* is the ability to interface or interconnect with another item; *function* is the action an item is designed to perform. An *interface* is the set of characteristics required at a common boundary between systems, managed through *interface control* and, where a design cycle warrants, an *Interface Control Working Group (ICWG)*.

**Digital-era terms.** Reflecting 61B's modernization, the definitions include *digital artifact*, *digital engineering*, and *digital twin* (an integrated, multiphysics, probabilistic simulation of an as-built system, enabled by the digital thread, that mirrors and predicts its physical twin over life). These signal that CM increasingly governs model- and data-based product definition, not just drawings.

## Mental Models

**CM is the product's single source of truth.** Think of CM as the discipline that guarantees a one-to-one correspondence between *the physical/digital thing*, *the documents that define it*, and *the requirements it must satisfy*. Every benefit the handbook lists collapses to this: defined attributes, documented configuration, labeled-and-correlated products, evaluated changes, managed change activity, retrievable information, and verified configuration.

**Adopt-and-tailor, don't reinvent.** The handbook is a *bridge*, not a rulebook: DoD adopted EIA-649 commercially, and 61B's job is to translate that commercial standard into DoD practice and to advise how to tailor EIA-649-1 onto a contract. When you need depth on *what* CM requires, go to the EIA-649 suite; when you need *how* DoD applies and tailors it, stay in 61B.

**Guidance vs. requirement.** 61B cannot be cited as a contractual requirement — it is advisory. Contractual teeth come from EIA-649-1 (tailored) and the citing acquisition documents. Treat 61B as the interpretive companion that tells you how to wield those requirements, not as the source of obligation itself.

**Functional → Allocated → Product.** The baseline progression is a maturation ladder: the FBL fixes system-level functional/performance requirements; the ABL allocates those across CIs (with each CI's performance stated in its item performance specification); the PBL captures the detailed, as-built product definition (initially set per-CI at CDR, finalized and validated at PCA). Reading any CM activity through "which baseline am I touching?" keeps change impact analysis honest.

**Terminology is intentionally non-rigid.** Because acquisition streamlining favors commercial and industry practice, the handbook explicitly declines to enforce one canonical CM vocabulary; EIA-649 catalogs the common aliases. The mental model: anchor on the *concept and its definition*, expect local industry terms to vary, and map them rather than fighting them.

## Key Takeaways

1. **MIL-HDBK-61B is guidance, not a requirement** — it advises how to plan, perform, and contract for CM, but cannot itself be cited as a contractual obligation.
2. **DoD has adopted the EIA-649 suite as its CM baseline**; the configuration manager's working toolkit is SAE EIA-649, SAE EIA-649-1, and GEIA-HB-649, with 61B supplying DoD-specific application and tailoring advice.
3. **CM is one management process expressed through five functions** — Planning, Identification, Control/Change Management, Status Accounting, and Verification & Audit — applied at a practitioner-chosen level to each CI.
4. **The definition of CM is consistency**: keeping a product's performance, functional, and physical attributes aligned with its requirements, design, and operational information across the full life.
5. **Three baselines structure the work** — Functional (FBL), Allocated (ABL), and Product (PBL) — each with corresponding configuration documentation, maturing from system requirements through CI allocation to as-built definition.
6. **Change is classified and governed**: Class I (Major) vs. Class II (Minor) changes flow through the ECP → CCB → CCBD path, with CDCA owning document-change authority and NOR/RFV handling revisions and variances.
7. **The cost case for CM is asymmetric**: its investment is small relative to the cost, schedule, and technical risk of ad hoc change management, mismatched support assets, and — at the extreme — catastrophic loss of equipment or life.
8. **61B is digitally aware**: definitions now include digital artifact, digital engineering, and digital twin, anchoring CM to model- and data-based product definition.

## Anti-patterns

The source frames these as the consequences of absent or ineffective CM (§1.1.3) rather than labeling them with anti-pattern names, but it explicitly calls them out:

- **Ad hoc, erratic change management** — managing change without a defined process, which the handbook ties to costly, avoidable errors.
- **Treating CM purely as a cost-driver** — discounting the small CM investment while ignoring or underestimating the compensating benefits and the cost, schedule, and technical risk of inadequate or delayed CM.
- **Incorrect part installation or replacement** and **equipment/maintenance-instruction mismatches** — failure modes that arise when configuration information is not kept correct and current, leading to failures, down-time, and inflated maintenance cost.

## Connects To

- **Chapter 2+ (the five CM functions in depth)** — Configuration Identification, Control/Change Management, Status Accounting, and Verification & Audit each get full treatment downstream; this chapter supplies their definitions and the baseline/CI vocabulary they all rely on.
- **SAE EIA-649 / EIA-649-1 / GEIA-HB-649** — the adopted standard suite this handbook tailors and references; consult these for the authoritative *requirements* behind 61B's guidance.
- **DoDI 5000.02 and the DoD acquisition life cycle** — the policy frame within which CM's acquisition-and-sustainment scope sits.
- **MIL-STD-961 / MIL-STD-31000 (Technical Data Packages)** — the specification and TDP standards that give configuration documentation its format and content.
- **MOSA (Modular Open Systems Approach)** — defined in this slice as an integrated business/technical strategy using modular design and consensus-based interface standards; a strategic driver for how CIs and interfaces are configured and controlled.
- **MIL-STD-882 (System Safety)** — adjacent DoD process standard; CM's verified-configuration guarantee underpins the integrity of safety-critical baselines and change control.

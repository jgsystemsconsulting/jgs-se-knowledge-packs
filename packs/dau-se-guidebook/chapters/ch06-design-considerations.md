# Chapter 6: Design Considerations (24)

## Core Idea
Design considerations are the cross-cutting concerns the SE process must **balance into** the design — not bolt on afterward. The Guidebook details **24** of them, each with statutory/regulatory drivers and a place in the SEP and the technical processes. They are addressed continuously through Architecture Design and Implementation and assessed at reviews.

## Frameworks Introduced
- **The 24 design considerations** — a structured checklist of specialty-engineering and compliance concerns to be planned in the SEP and integrated across the life cycle.
  - When to use: during Technical Planning (to plan their treatment) and Architecture Design/Implementation (to engineer them in); each maps to its own deeper specialty source.
- **"Engineer in, don't bolt on"** — every consideration is cheapest and most effective when designed in early, traded against cost/schedule/performance like any other requirement.
  - When to use: from the earliest design decisions; retrofitting safety, security, supportability, or HSI late is costly and often infeasible.

## Key Concepts — the considerations (grouped)
- **Dependability / specialty engineering**:
  - **Reliability & Maintainability (R&M) engineering** — foundational R&M activities across phases; reliability growth, maintainability, availability.
  - **System Safety** — the system safety process, **software system safety**, **ESOH** (Environment, Safety, Occupational Health), **hazard tracking system**, SS in the SE process and program documents, SS risk management, hazardous materials, safety release for testing, safety confirmation.
  - **Survivability** — the system's ability to avoid/withstand hostile environments.
  - **Supportability** — designing for sustainment; ties to the LCSP and product support.
- **Mission/operational**:
  - **Human Systems Integration (HSI)** — integrate human capabilities/limitations into design (manpower, personnel, training, human factors, safety, habitability, survivability).
  - **Interoperability and Dependencies** — work within the joint/SoS environment.
  - **Intelligence (Life Cycle Mission Data Plan)** — intelligence mission data needs across the life cycle.
  - **Spectrum Management** — electromagnetic spectrum supportability across phases.
  - **Operational Energy** — energy demand as a design and sustainment driver.
- **Security & integrity**:
  - **System Security Engineering** — protect the system and its critical program information/components against threats across the life cycle (ties to the Program Protection Plan).
  - **Anti-Counterfeiting** and **Critical Safety Item (CSI)** management.
- **Producibility & life cycle**:
  - **Manufacturing & Quality** — manufacturing management program, quality management, producibility, assessing **manufacturing readiness** (MRLs) and risk, industrial capabilities.
  - **Diminishing Manufacturing Sources and Material Shortages (DMSMS)**.
  - **Corrosion Prevention and Control**; **Packaging, Handling, Storage & Transportation (PHS&T)**; **Demilitarization and Disposal**; **Insensitive Munitions**; **Item Unique Identification (IUID)**.
- **Openness & efficiency**:
  - **Modular Design** / **MOSA**; **Standardization**; **Commercial-Off-The-Shelf (COTS)**.
  - **Affordability — SE Trade-Off Analyses**; **Value engineering**.
  - **Accessibility (Section 508 compliance)**.

## Mental Models
- A design consideration is a *requirement source*, not paperwork: each one generates design requirements, trades, and verification activities that compete for the same cost/schedule/performance budget.
- Cost of late integration rises sharply: safety, security, HSI, and supportability designed in at architecture cost a fraction of what they cost retrofitted after CDR.
- Manufacturing readiness parallels technology readiness: assess MRLs at defined points just as you assess TRLs — a producible design is part of "done," not an afterthought.
- The SEP is where considerations get governed: if a consideration matters to the program, its treatment, owner, and review evidence belong in the SEP (e.g., ESOH information in the SEP).

## Anti-patterns
- **Bolt-on safety/security/HSI**: deferring these to late phases, where they become expensive change requests or unfixable.
- **Ignoring producibility until production**: a verified design that cannot be manufactured affordably at rate.
- **Treating the 24 as a one-time checklist**: ticking them at one review instead of carrying owned, evidenced treatment through the life cycle.
- **No data-rights / MOSA strategy**: foreclosing future competition and upgrades by accepting closed interfaces and lost data rights.

## Key Takeaways
1. The Guidebook details **24 design considerations** to be planned in the SEP and engineered into the design — not added later.
2. They span dependability (R&M, system safety/ESOH, survivability, supportability), mission (HSI, interoperability, spectrum, energy), security (system security engineering, anti-counterfeiting, CSI), producibility (manufacturing & quality, MRLs, DMSMS), and openness/efficiency (MOSA, standardization, COTS, affordability, Section 508).
3. **Engineer in, don't bolt on** — early integration is far cheaper than retrofit.
4. **Manufacturing readiness (MRLs)** is assessed at defined points, in parallel with TRLs.
5. Each consideration generates requirements/trades that compete for the cost/schedule/performance budget and is governed through the SEP.

## Connects To
- **ch05 (Technical Processes)**: design considerations are balanced within Architecture Design and Implementation.
- **ch04 (Technical Management Processes)**: Technical Planning plans their treatment; Risk Management tracks consideration-driven risks.
- **ch01 / SEP**: the SEP documents how each relevant consideration is addressed (e.g., ESOH info in the SEP).
- **`mil-std-882` pack**: the DoD System Safety standard underpinning the System Safety consideration.
- **`nasa-hsi` pack**: deeper HSI domain treatment.
- **NIST RMF / Program Protection Plan**: deeper system security engineering / cybersecurity treatment.

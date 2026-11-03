# Chapter: Design Considerations

## Core Idea

Design considerations are factors that shape system design, characteristics, or behavior. Some are mandated by law or regulation; others come from long practice. They are not optional decoration. The PM, systems engineer, and software engineer address and document them so end-user capability is designed in, and so trades stay explicit. The September 2026 edition keeps 24 considerations in one section. This pack names each with its job in our words. It does not reproduce checklist or statutory tables cell by cell.

## Frameworks Introduced

- **Integrated design-consideration set** treated as coupled variables, not stovepipes.
- **SEP design-considerations table intent** (relevance and trade role), without copying table cells.
- **Twenty-four named considerations** (7.1 through 7.24) as the working vocabulary.

## Key Concepts

- **Two jobs for the set.** (1) Translate end-user capability into interrelated design specifications. (2) Enable trades among considerations under cost and schedule constraints.
- **Integrated view.** Each item is discrete, but programs treat them as an interacting set so one specialty does not silently defeat another.
- **Relevance filter.** Not every item is equally critical on every program. All should be examined for relevancy; Service, Center, platform, or domain may add more.
- **7.1 Accessibility (Section 508).** Design information and communications technology so qualified users with disabilities can use it, unless a documented exception applies.
- **7.2 Affordability and SE trade-off analyses.** Keep cost and mission effectiveness in the same trade space across the life cycle.
- **7.3 Anti-Counterfeiting.** Prevent and detect counterfeit parts in the supply chain and design.
- **7.4 Commercial-Off-the-Shelf (COTS).** Use commercial items deliberately, with known limits on change, support, and data rights.
- **7.5 Corrosion Prevention and Control.** Design and material choices that limit corrosion across the life cycle.
- **7.6 Critical Safety Item.** Identify and control items whose failure can have catastrophic safety consequences.
- **7.7 Demilitarization and Disposal.** Plan end-of-life demilitarization and disposal while design is still flexible.
- **7.8 DMSMS.** Manage loss of sources and material shortages so supportability survives market change.
- **7.9 Human Systems Integration (HSI).** Integrate human capabilities and limitations into design across HSI domains.
- **7.10 Insensitive Munitions.** Reduce munition vulnerability to unintended stimuli where applicable.
- **7.11 Intelligence (Life Cycle Mission Data Plan).** Plan intelligence mission data needs across the life cycle.
- **7.12 Interoperability and Dependencies.** Design for required exchanges and dependencies with other systems.
- **7.13 Item Unique Identification.** Identify items uniquely for tracking, accountability, and support.
- **7.14 Manufacturing and Quality.** Design for producibility and embed quality into manufacturing planning.
- **7.15 Modular Design.** Structure the design so modules can be developed, replaced, and upgraded with controlled interfaces.
- **7.16 Operational Energy.** Account for energy use and supply as a design and mission constraint.
- **7.17 Packaging, Handling, Storage, and Transportation (PHS&T).** Design so the system survives and remains usable through PHS&T environments.
- **7.18 Reliability and Maintainability Engineering.** Set and achieve R&M characteristics that meet operational availability needs.
- **7.19 Spectrum Management.** Ensure electromagnetic spectrum needs and constraints are designed in.
- **7.20 Standardization.** Prefer standard parts, interfaces, and processes where they reduce risk and cost.
- **7.21 Supportability.** Design for maintenance, supply, and product support so the fielded system stays usable.
- **7.22 Survivability.** Design to survive threat and environmental conditions relevant to the mission.
- **7.23 System Safety.** Identify, assess, and mitigate hazards across the life cycle.
- **7.24 System Security Engineering.** Engineer protection against security threats, including cyber, as a design job.

## Mental Models

- **Design-in, do not inspect-in.** Late add-on of safety, security, or supportability is expensive and weak.
- **Coupled trades.** Improving one consideration can harm another; record the trade.
- **Relevance, then depth.** Screen all 24; deep-dive the drivers for this system.
- **SEP is the ledger.** Relevant considerations and their trade role belong in the SE approach or SEP.

## Key Takeaways

- Examine all 24 considerations for relevancy; document the drivers in the SEP.
- Treat the set as integrated variables under affordability and mission effectiveness.
- Name statutory and policy drivers when they apply; do not paste table cells from this pack.
- Pull specialty engineering in early enough to change architecture, not only paperwork.
- Use modular design, MOSA thinking, R&M, safety, and security as standing design jobs where relevant.

## Connects To

- ch02 for system-level context that makes interoperability and dependencies real.
- ch03 for MOSA and digital practices that change how modular and secure design runs.
- ch06 for SEP and technical planning that record the considerations table intent.
- ch07 for architecture, implementation, and verification processes that carry the design in.

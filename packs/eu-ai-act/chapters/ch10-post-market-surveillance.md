# Chapter 10: EU Database, Post-Market Monitoring, Market Surveillance, and Incident Reporting (Chapters VIII-IX, Articles 71-87)

## Core Idea
Chapters VIII and IX establish the post-placement oversight infrastructure: the EU database as the public registry for high-risk AI systems; provider-run post-market monitoring systems feeding data back into risk management; mandatory serious incident reporting; and a market surveillance regime modelled on EU product-safety law (Regulation 2019/1020) but adapted for AI. Affected persons also gain a right to explanation and a right to complain.

## Frameworks Introduced
- **Article 71 — EU Database for High-Risk AI Systems**: The Commission sets up and maintains a public EU database. Providers and authorised representatives enter system data (Annex VIII Section A/B); public-authority deployers enter their use data (Annex VIII Section C). The database is publicly accessible, user-friendly, and machine-readable. The Commission is controller. A non-public section covers real-world testing registrations (Art 60).
  - When to use: To register high-risk AI systems before placement (mandatory under Art 49); to check whether a system has been registered before deploying as a public authority.
- **Article 72 — Post-Market Monitoring (PMM) System**: Providers must establish a PMM system that actively and systematically collects, documents, and analyses relevant performance data throughout the system's lifetime, enabling continuous compliance evaluation. The PMM plan is part of technical documentation (Annex IV). For products covered by Annex I legislation, the PMM may be integrated with existing sector requirements.
  - When to use: When designing the operational maintenance regime for a high-risk AI system after deployment; PMM data feeds back into the Art 9 Risk Management System.
- **Article 73 — Serious Incident Reporting**: Providers must report serious incidents to market surveillance authorities of the Member State where the incident occurred, without undue delay and within set timeframes: immediately for incidents leading to death or serious health harm where there is a reasonable causal relationship; within two working days where there is immediate risk of death or health harm; within 15 days for other serious incidents. Deployers must inform providers (and if unreachable, directly inform authorities).
  - When to use: When a high-risk AI system causes or contributes to a death, serious health harm, fundamental rights infringement, critical infrastructure disruption, or serious property/environmental harm.
- **Article 74-79 — Market Surveillance Powers**: Market surveillance authorities have powers to access documentation, test AI systems, order corrective actions, withdraw or recall systems, and impose temporary restrictions. For AI systems with suspected serious risk, authorities can restrict use immediately and notify the Commission via the RAPEX/ICSMS-equivalent. The Commission and AI Office can conduct Union safeguard procedures (Art 81) when a Member State measure is contested by another Member State or found inconsistent.
  - When to use: When an authority identifies a non-compliant high-risk AI system post-placement, or when cross-border market actions are required.
- **Article 85-86 — Remedies**: Any person may lodge a complaint with a market surveillance authority (Art 85). Affected persons subject to decisions based on Annex III high-risk AI outputs (except area 2 — critical infrastructure) have a right to obtain clear and meaningful explanations of the AI system's role in the decision and the main elements of the decision taken (Art 86).
  - When to use: Art 85 for affected persons and competitors seeking regulatory action; Art 86 for individuals seeking to understand AI-driven decisions affecting their rights.

## Key Concepts
- **Post-market monitoring plan** — documented plan (part of Annex IV technical documentation) specifying how the provider will collect and analyse performance data; Commission template due by 2 February 2026.
- **Serious incident** (Art 3(49)) — incident or malfunction leading directly or indirectly to: death; serious health harm; serious and irreversible disruption of critical infrastructure; infringement of fundamental rights obligations; or serious harm to property or environment.
- **Serious incident reporting timelines** (Art 73) — death/serious health harm with causal relationship: immediately; immediate risk of death/health harm: within 2 working days; other serious incidents: within 15 days. Single market surveillance authority notified (where incident occurred); that authority coordinates with others via RAPEX.
- **Right to explanation** (Art 86) — affected persons have a right to a clear and meaningful explanation of the AI system's role in a decision and its main elements, where that decision has legal or similarly significant adverse effects on health, safety, or fundamental rights. Applies to all Annex III categories except area 2 (critical infrastructure).
- **Confidentiality of information** (Art 78) — market surveillance authorities must treat obtained information confidentially, protecting trade secrets, intellectual property, and personal data. This applies throughout surveillance and enforcement activities.

## Mental Models
- **"PMM feeds RMS": The lifecycle loop**: Post-market monitoring (Art 72) gathers data -> serious incidents trigger reporting (Art 73) -> RMS is updated (Art 9(2)(c)) -> risk measures are adapted -> updated system documentation. This closed loop is the operational core of AI governance post-deployment.
- **"Complaint + explanation = affected person toolkit"**: Art 85 gives any person standing to complain to market surveillance; Art 86 gives individuals subject to AI decisions the right to understand how the AI contributed. Together they are the citizen-facing enforcement interface.

## Anti-patterns
- Treating post-market monitoring as optional or passive: Art 72 requires active and systematic data collection; passive log-keeping alone is insufficient.
- Missing the 2-working-day reporting window: serious incidents posing an immediate risk of death or health harm must be reported within 2 working days, not the general 15-day window. Providers must have triage protocols ready.
- Assuming right to explanation is unlimited: Art 86 does not apply to critical infrastructure AI (Annex III area 2), and does not apply where exceptions exist under Union or national law (Art 86(2)).

## Key Takeaways
1. EU database is the mandatory pre-placement registry; public-authority deployers must verify registration before use.
2. PMM is a continuous provider obligation; it is not satisfied by the initial conformity assessment alone.
3. Serious incident reporting has three distinct timeframes depending on severity; internal triage and reporting protocols must be operationalised before deployment.
4. Market surveillance authorities have broad investigative and corrective powers, including immediate restriction of use for serious-risk systems.
5. Affected persons have a complaint right (Art 85) and a right to explanation (Art 86) for non-critical-infrastructure Annex III AI decisions.
6. GPAI provider enforcement is handled exclusively by the AI Office/Commission (Art 88), not national market surveillance authorities.

## Connects To
- **Chapter III Section 2 (Art 9)**: PMM data feeds back into the risk management system.
- **Chapter III Section 3 (Art 17)**: QMS must include PMM system setup and serious incident reporting procedures.
- **Chapter VII (Art 64-70)**: AI Office and national competent authorities conduct surveillance.
- **Chapter IX Section 5 (Art 88-94)**: Parallel GPAI-specific enforcement by AI Office.

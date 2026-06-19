# Chapter 5: Obligations of Providers, Deployers, Importers, Distributors and Value-Chain Responsibility (Chapter III Section 3, Articles 16-27)

## Core Idea
Section 3 translates the technical requirements of Section 2 into role-specific legal obligations distributed across the full AI value chain. The fundamental principle is that whoever brings a high-risk AI system to market or uses it must bear obligations proportional to their role and ability to influence compliance. Responsibility can transfer when parties make substantial modifications or rebrand systems.

## Frameworks Introduced
- **Article 16 — Provider obligations checklist**: Twelve enumerated obligations including QMS, technical documentation, conformity assessment, EU declaration of conformity, CE marking, registration, corrective actions, and accessibility compliance.
  - When to use: As a compliance checklist for any entity acting as provider of a high-risk AI system.
- **Article 17 — Quality Management System (QMS)**: Providers must maintain a documented QMS covering regulatory compliance strategy, design control, development procedures, examination/validation, technical specifications, data management, risk management (Art 9), post-market monitoring (Art 72), serious incident reporting (Art 73), authority communications, record-keeping, resource management, and accountability framework. Financial institutions may satisfy this via existing internal governance requirements.
  - When to use: When designing provider compliance infrastructure; QMS is the organisational backbone analogous to ISO 9001 but AI-specific.
- **Article 25 — Value-chain responsibility transfer**: A distributor, importer, deployer, or other third party becomes a provider (and assumes full provider obligations) if they: (a) affix their name/trademark; (b) make a substantial modification; or (c) change the intended purpose such that the system becomes high-risk. The original provider is released from obligations but must cooperate and provide technical access.
  - When to use: Whenever a party is rebranding, modifying, or repurposing an AI system they did not originally develop.
- **Article 26 — Deployer obligations**: Deployers must follow instructions for use, assign qualified human oversight persons, maintain logs for at least 6 months, inform workers, register in EU database if a public authority, notify providers and market surveillance of serious incidents, and notify affected persons of AI system use in decisions affecting them.
  - When to use: As a compliance checklist for all entities deploying high-risk AI systems.
- **Article 27 — Fundamental Rights Impact Assessment (FRIA)**: Public authorities and private entities providing public services deploying Annex III systems (except area 2) must perform a FRIA before first use, covering: process description, frequency and period of use, categories of affected persons, specific risks per category, human oversight implementation, and risk materialisation measures. Results must be notified to the market surveillance authority. A FRIA may complement but does not replace a GDPR DPIA.
  - When to use: For all public and public-service deployers of high-risk AI before they put systems into service.

## Key Concepts
- **Documentation retention period** (Art 18) — providers must retain technical documentation, QMS documentation, notified body decisions, and EU declaration of conformity for 10 years after placement or putting into service.
- **Automatic log retention** (Art 19) — providers must retain automatically generated logs for at least 6 months (unless sector law specifies otherwise); logs under deployer control must also be kept for at least 6 months (Art 26(6)).
- **Authorised representative** (Art 22) — a Union-established mandatee for non-Union providers of high-risk AI systems; must verify documentation, retain copies for 10 years, cooperate with authorities, and can terminate the mandate if the provider acts contrary to obligations.
- **Importer obligations** (Art 23) — importers must verify conformity assessment, technical documentation, CE marking, EU declaration of conformity, and authorised representative appointment before placement; must retain certificates and documentation for 10 years.
- **Distributor obligations** (Art 24) — distributors must verify CE marking, EU declaration of conformity, and that provider/importer obligations have been met before making a system available; must inform provider/importer of non-compliance risks.
- **Substantial modification** (Art 3(23)) — a change after placement that was not foreseen in the initial conformity assessment AND affects compliance with Section 2 requirements or changes the intended purpose. A party making such a modification becomes a provider.
- **Post-remote biometric identification deployer obligations** (Art 26(10)) — deployers using post-remote RBIS for criminal investigations must obtain prior judicial/administrative authorisation (within 48 hours in urgent cases), document each use in police files, and submit annual reports.

## Mental Models
- **"Name it, own it"**: Affixing your name or trademark to a high-risk AI system makes you its provider in law, regardless of who built the underlying technology.
- **"Modification threshold = conformity assessment re-trigger"**: Any post-market change that was unforeseen AND affects compliance requirements or changes intended purpose is "substantial" and restarts the provider liability chain.
- **"Public deployer = extra obligations"**: Public authorities and entities providing public services face the FRIA obligation (Art 27), worker notification obligation (Art 26(7)), and mandatory EU database registration (Art 26(8)) in addition to standard deployer obligations.

## Anti-patterns
- Assuming a white-label arrangement transfers all risk: Art 25(4) requires a written agreement specifying what information, capabilities, and technical access the original provider will give the new provider; contracts cannot override statutory obligations.
- Neglecting the deployer's obligation to notify workers: Art 26(7) requires informing workers' representatives and affected workers before putting a workplace high-risk AI system into use, in accordance with applicable industrial relations law.
- Treating the FRIA as identical to a DPIA: a FRIA is broader, covering all fundamental rights categories beyond data protection, and must be conducted by deployers (not providers); a DPIA can complement but not substitute for a FRIA (Art 27(4)).

## Key Takeaways
1. Provider obligations are comprehensive (12 items in Art 16) and require a QMS with 13 mandatory components.
2. All parties in the supply chain — importers, distributors, deployers — carry specific obligations; ignorance of a product's high-risk status is not a defence.
3. Responsibility can transfer to downstream parties who modify, rebrand, or repurpose systems; original providers must cooperate but are released from ongoing obligations.
4. Deployers retain logs for at least 6 months; providers retain documentation for 10 years.
5. Public-body and public-service deployers must complete a FRIA before deployment and notify market surveillance of results.
6. Written value-chain agreements (Art 25(4)) are legally required where third parties supply components, tools, or services integrated into high-risk AI.

## Connects To
- **Chapter III Section 2 (Art 8-15)**: Requirements that providers, deployers, and others must implement.
- **Chapter III Section 4 (Art 28-47)**: Conformity assessment, notified bodies, and certification that providers must undergo.
- **Chapter IX Section 2 (Art 73-79)**: Market surveillance authorities oversee fulfilment of these obligations.
- **Chapter XII (Art 99(4))**: Non-compliance with Art 16, 22, 23, 24, or 26 carries fines up to EUR 15 million or 3% of turnover.

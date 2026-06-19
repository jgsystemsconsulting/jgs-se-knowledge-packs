# Chapter 6: Conformity Assessment, Notified Bodies, CE Marking, and Registration (Chapter III Sections 4-5, Articles 28-49)

## Core Idea
Sections 4 and 5 establish the market-entry gate for high-risk AI systems: a conformity assessment process that is either provider-conducted (internal) or third-party (notified body), followed by an EU declaration of conformity, CE marking, and registration in the EU database. The sections also create the notified body accreditation infrastructure and set up the EU database as the public registry for high-risk AI.

## Frameworks Introduced
- **Article 43 — Conformity Assessment Procedure**: Two routes: (A) for Annex III systems not covered by Route A product legislation — providers may conduct internal assessment against Section 2 requirements, or use a notified body; (B) for Annex I Route A product systems — conformity assessment follows the procedures set out in applicable Union harmonisation legislation, supplemented by Section 2 requirements. Third-party assessment by a notified body is required where the system uses techniques not based on training data that is not derived from prior human labelling, or for biometric identification systems.
  - When to use: To determine whether a provider can self-assess or must engage a notified body.
- **Article 28-36 — Notifying Authorities and Notified Bodies**: Each Member State must designate a notifying authority to assess, designate, and monitor notified bodies. Notified bodies must be independent, impartial, financially viable, and have documented procedures. Notified bodies may be subcontracted but remain responsible. The Commission maintains an online database of notified bodies (NANDO equivalent for AI).
  - When to use: When selecting a third-party conformity assessment body or when a Member State is setting up its notification infrastructure.
- **Article 47 — EU Declaration of Conformity (DoC)**: Providers must draw up a DoC stating that the high-risk AI system complies with this Regulation. The DoC must contain the elements in Annex V. One DoC may cover multiple AI systems. The DoC must be kept for 10 years.
  - When to use: When preparing market placement documentation.
- **Article 48 — CE Marking**: The CE marking must be affixed to the high-risk AI system or its packaging/documentation before market placement. For products covered by Annex I legislation, CE marking follows those sectoral rules.
  - When to use: As the final market-readiness indicator; affixing CE marking without completing conformity assessment is a specific infringement.
- **Article 49 — Registration**: Providers must register high-risk AI systems in the EU database (Art 71) before placement. Deployers who are public authorities must verify registration and not use unregistered systems. Providers who assess their Annex III system as not-high-risk must also register (Art 6(4)).
  - When to use: As the last step before a high-risk AI system goes to market.
- **Article 40-41 — Harmonised Standards and Common Specifications**: AI systems compliant with harmonised standards published in the Official Journal are presumed to conform with corresponding Section 2 requirements. Where no harmonised standard exists, the Commission may issue common specifications by implementing act.
  - When to use: When building technical compliance evidence; harmonised standard compliance is the primary presumption-of-conformity pathway.
- **Articles 57-60 — AI Regulatory Sandboxes and Real-World Testing**: Member States must establish at least one AI regulatory sandbox by 2 August 2026. Sandboxes allow development, training, validation, and testing of innovative AI systems under regulatory supervision for a limited time. Data protection rules apply within sandboxes. Real-world testing outside sandboxes is also permitted under strict conditions (Art 60).
  - When to use: When a startup or innovator wants to test high-risk AI before full market placement without incurring all conformity costs upfront.

## Key Concepts
- **Notified body** (Art 3(22)) — a conformity assessment body designated by a Member State notifying authority and included in the NANDO-equivalent EU database; has exclusive third-party certification authority for high-risk AI systems.
- **Certificate of conformity** (Art 44) — issued by notified body after successful conformity assessment; maximum validity 5 years; subject to regular update; must be withdrawn if conditions are no longer met.
- **Harmonised standard** (Art 3(27)) — a standard adopted by CEN, CENELEC, or ETSI at the Commission's request and published in the Official Journal; compliance creates a presumption of conformity with the corresponding requirements.
- **Common specification** (Art 3(28)) — a set of technical specifications issued by the Commission where no harmonised standard exists or where it does not fully cover Section 2 requirements; compliance creates a presumption of conformity.
- **AI regulatory sandbox** (Art 3(55)) — a controlled framework set up by a competent authority offering providers the possibility to develop, train, validate and test innovative AI systems in real-world conditions under regulatory supervision under a sandbox plan.
- **Substantial modification post-certification** — a substantial modification to a high-risk AI system invalidates the existing conformity assessment; a new assessment is required, and the notified body that issued the original certificate must be informed.

## Mental Models
- **"Presumption staircase"**: Harmonised standard compliance -> presumption of conformity. Common specification compliance -> presumption of conformity. Neither available -> provider must demonstrate compliance by other means acceptable to the notified body or authority.
- **"Self-assess or third-party based on technique and area"**: Most Annex III systems can self-assess; biometric identification and systems with non-training-data-based techniques require a notified body. Route A product legislation may require third-party assessment under that legislation's rules.

## Anti-patterns
- Assuming all high-risk AI requires a notified body: Art 43 allows internal conformity assessment for most Annex III systems; third-party assessment is mandatory only for specific cases (biometric identification systems in Annex III point 1(a) and certain special-purpose systems).
- Treating CE marking as self-certification: CE marking must be affixed only after completing the applicable conformity assessment procedure and drawing up a DoC; premature affixing is a specific infringement attracting fines.
- Neglecting post-market documentation maintenance: conformity assessment is point-in-time, but technical documentation and the RMS must continue to be maintained and updated throughout the system's lifecycle.

## Key Takeaways
1. Two conformity assessment routes: internal assessment (most Annex III systems) or notified body (biometric identification systems, certain product sectors, or provider's choice).
2. Harmonised standards create presumption of conformity; they are the primary compliance-efficiency tool.
3. CE marking is the market-readiness symbol; the DoC is the underlying legal statement; both are required.
4. EU database registration is mandatory before placement; public-authority deployers must verify registration before use.
5. AI regulatory sandboxes are required in each Member State by August 2026; they allow pre-compliance innovation with regulatory supervision.
6. Notified body certificates expire after five years and must be renewed or withdrawn if conditions change.

## Connects To
- **Chapter III Section 2 (Art 8-15)**: The requirements that conformity assessment verifies.
- **Chapter III Section 3 (Art 16)**: Provider obligation to conduct conformity assessment and draw up DoC is listed in Art 16(f-g).
- **Chapter VIII (Art 71)**: The EU database in which providers register.
- **Chapter IX (Art 74-79)**: Market surveillance authorities can verify conformity assessment after placement.

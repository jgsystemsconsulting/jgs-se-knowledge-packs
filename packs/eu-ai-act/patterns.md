# EU AI Act Patterns and Techniques

Practical when/how/trade-offs blocks for applying the EU AI Act's frameworks to real-world AI development and deployment.

---

## Pattern 1: AI System Classification Gate

**When to use**: Before any compliance planning, to determine which tier of obligations applies.

**How**:
1. Check Art 5: does the system fall under any of the eight prohibited practice categories? If yes, stop — no compliance pathway.
2. Check Art 6(1) Route A: is this an AI system intended as a safety component, OR is it itself a product, covered by Annex I sector legislation? AND does that product require third-party conformity assessment? If both yes → high-risk.
3. Check Art 6(2) Route B: does the system fall within an Annex III use-case area? If yes, check Art 6(3) de minimis carve-out (narrow procedural task / improves prior human activity / detects patterns without replacing assessment / preparatory task). If carve-out applies AND no profiling → not high-risk (but must document and register per Art 6(4)).
4. Check Art 50: does the system interact with humans, generate synthetic content, or recognise emotions/biometric categories? If yes → transparency obligations apply regardless of high-risk status.
5. Check Chapter V: is the system a GPAI model? If yes → Chapter V obligations apply regardless of high-risk status.

**Trade-offs**: Classification is self-assessed by providers but subject to market surveillance audit; documenting the classification decision (Art 6(4)) reduces legal exposure if the classification is later disputed.

---

## Pattern 2: Risk Management System (RMS) Lifecycle Design

**When to use**: When designing the compliance infrastructure for a high-risk AI system.

**How**:
1. At design phase: identify and analyse known and reasonably foreseeable risks (Art 9(2)(a)).
2. During development: estimate and evaluate risks under intended purpose and foreseeable misuse (Art 9(2)(b)); apply risk mitigation measures integrated into design.
3. Before placement: test against pre-defined metrics and probabilistic thresholds (Art 9(6-8)); document residual risk as acceptable.
4. Post-placement: integrate post-market monitoring data (Art 72) into RMS step (c) (Art 9(2)(c)); update mitigation measures as needed.
5. Incident response: trigger serious incident reporting (Art 73); investigate root cause; update RMS.

**Trade-offs**: Continuous lifecycle management requires operational investment; integrating RMS with existing ISO 31000 or IEC 62443 risk frameworks reduces duplication and may satisfy Art 9(10) combination-with-existing-law provisions.

---

## Pattern 3: Data Governance Compliance for Training Data

**When to use**: When preparing training, validation, and testing data sets for a high-risk AI system.

**How**:
1. Document design choices and data origin (Art 10(2)(a-b)).
2. Record preparation operations: annotation, labelling, cleaning, enrichment (Art 10(2)(c)).
3. State assumptions about what the data measures and represents (Art 10(2)(d)).
4. Assess availability, quantity, and suitability (Art 10(2)(e)).
5. Examine for biases that could affect health, safety, or cause prohibited discrimination (Art 10(2)(f)); implement detection and mitigation measures (Art 10(2)(g)).
6. Identify data gaps and remediation paths (Art 10(2)(h)).
7. For bias correction only: special-category personal data may be processed if all six conditions in Art 10(5) are met (last resort, pseudonymised, access controlled, not transferred, deleted after use, logged).

**Trade-offs**: The six-condition gate for special-category bias data processing is strict; synthetic or anonymised data must first be shown insufficient before resorting to special-category data (Art 10(5)(a)).

---

## Pattern 4: Conformity Assessment Route Selection

**When to use**: When a provider of a high-risk AI system is deciding whether to self-assess or engage a notified body.

**How**:
- If the system is a safety component of an Annex I product sector (Route A): follow the conformity assessment procedure under that sector's legislation. A notified body is often required under those sector laws.
- If the system is an Annex III system (Route B):
  - Is it an RBIS (Annex III area 1(a), remote biometric identification)? → Notified body required.
  - Is it a system using techniques NOT based on data-trained models (e.g. rule-based expert systems in Annex III areas)? → Notified body may be required; check applicable implementing acts.
  - All other Annex III systems → internal conformity assessment is permitted.
- Regardless of route: draw up EU Declaration of Conformity (Annex V), affix CE marking, register in EU database.

**Trade-offs**: Internal assessment is faster and cheaper but carries more legal risk if challenged post-placement; notified body certification creates a stronger presumption of conformity but requires preparation time (6-18 months typical) and ongoing certification fees.

---

## Pattern 5: Provider-to-Deployer Information Package

**When to use**: When a provider prepares the package to hand to deployers of a high-risk AI system.

**How**: The instructions for use (Art 13(3)) must cover at minimum:
1. Provider identity and contact details.
2. Intended purpose and capabilities.
3. Accuracy metrics, known limitations, foreseeable circumstances affecting performance.
4. Known foreseeable misuse risks to health, safety, or fundamental rights.
5. Explainability capabilities (if any).
6. Performance per specific person/group categories (where applicable).
7. Input data specifications and training/validation data characteristics.
8. Human oversight measures the deployer must implement (Art 14).
9. Computational and hardware requirements; expected lifetime; maintenance needs.
10. Log collection, storage, and interpretation guidance.

**Trade-offs**: Insufficient instructions for use can shift liability back to the provider if deployer misuse was foreseeable; over-specification can impose unrealistic deployer constraints; balance requires understanding the deployer's operating context.

---

## Pattern 6: Deployer Pre-Deployment Checklist

**When to use**: When an organisation is about to put a high-risk AI system into service.

**How**:
1. Verify the system is registered in the EU database (Art 49 / Art 26(8) for public authorities).
2. Review instructions for use; confirm all human oversight persons are assigned and trained.
3. For public-body or public-service deployers: complete the FRIA (Art 27) and notify market surveillance of results.
4. Inform workers' representatives and affected workers (Art 26(7)).
5. Establish log retention procedures (minimum 6 months, Art 26(6)).
6. Establish serious incident notification protocols (Art 26(5)).
7. Ensure input data is relevant and sufficiently representative (Art 26(4)).
8. Implement procedures for informing affected persons of AI use in decisions about them (Art 26(11)).

**Trade-offs**: FRIA scope is broad and requires structured process; integrating it with an existing GDPR DPIA (permitted under Art 27(4)) reduces duplication but FRIA covers rights beyond data protection.

---

## Pattern 7: Value-Chain Responsibility Assessment

**When to use**: When a non-provider party (distributor, importer, deployer) modifies or rebrands a high-risk AI system.

**How**:
1. Does the party affix its own name or trademark? → Becomes provider (Art 25(1)(a)).
2. Does the party make a substantial modification (Art 3(23))? → Becomes provider (Art 25(1)(b)); original provider must cooperate and provide technical access.
3. Does the party change the intended purpose such that a non-high-risk system becomes high-risk (Art 6)? → Becomes provider (Art 25(1)(c)).
4. If none of the above: party retains its original role obligations (Art 23 for importers, Art 24 for distributors).
5. Document all value-chain agreements in writing (Art 25(4)), specifying information, capabilities, and technical access the original provider will supply.

**Trade-offs**: White-labelling is a frequent trigger for provider liability transfer; the original provider can limit this by explicitly stating the system must not be converted to a high-risk application (Art 25(2) last sentence).

---

## Pattern 8: GPAI Systemic Risk Self-Assessment

**When to use**: When a GPAI model provider is approaching or has exceeded the 10^25 FLOPs training-compute threshold.

**How**:
1. Calculate cumulative training compute; compare to 10^25 FLOPs threshold (Art 51(2)).
2. If threshold met: notify Commission within 2 weeks (Art 52(1)).
3. May argue model does not in fact present systemic risk despite meeting the threshold, by submitting substantiated arguments at the time of notification (Art 52(2)).
4. Commission may accept (no systemic risk designation) or reject (model classified as systemic risk, Art 52(3)).
5. Commission may also designate ex officio or on scientific panel qualified alert (Art 52(4)); provider may request reassessment no earlier than 6 months after designation (Art 52(5)).
6. If systemic risk is confirmed: implement Art 55 obligations (adversarial testing, risk assessment and mitigation, incident reporting, cybersecurity).

**Trade-offs**: Proactive notification builds regulatory goodwill; attempts to avoid notification are more expensive if discovered post-hoc (up to 3% global turnover fine). The 10^25 FLOPs threshold will evolve by delegated act.

---

## Pattern 9: Serious Incident Triage and Reporting

**When to use**: When a high-risk AI system produces an output that has caused or may have caused harm.

**How**:
1. Identify the incident category:
   - Category A: death or serious health harm with reasonable causal relationship → report immediately to market surveillance authority of the Member State where the incident occurred.
   - Category B: immediate risk of death or serious health harm → report within 2 working days.
   - Category C: other serious incidents (critical infrastructure, fundamental rights, property/environment) → report within 15 days.
2. Simultaneously: investigate root cause; implement corrective actions (Art 20).
3. Deployer reports to provider first; if provider is unreachable, deployer reports directly (Art 26(5)).
4. For GPAI model serious incidents: provider reports to AI Office (Art 55(1)(c)).
5. Update RMS and PMM plan post-investigation.

**Trade-offs**: Speed of reporting is mandatory; thorough investigation takes time. Best practice is to file an initial notification immediately with known facts, followed by a supplementary report with full investigation findings.

---

## Pattern 10: Transparency Obligation Matrix (Art 50)

**When to use**: When determining disclosure obligations for AI systems regardless of high-risk classification.

**How**: Apply all four tests:
1. Does the system interact directly with natural persons? → Provider must build in disclosure that this is an AI system (unless obvious). Deployer must implement it.
2. Does the system generate synthetic audio, image, video, or text? → Provider must ensure outputs are machine-readably labelled as AI-generated.
3. Does the system perform emotion recognition or biometric categorisation? → Deployer must inform persons exposed.
4. Does the deployer use AI to generate or manipulate image/audio/video constituting a deep fake? → Deployer must disclose. Does the deployer publish AI-generated text on public-interest matters? → Deployer must disclose (unless human editorial control + responsibility applies).

**Trade-offs**: Machine-readable labelling (Art 50(2)) requires technical implementation at generation time; retrofitting to existing models is complex. Content watermarking standards are still evolving; codes of practice (Art 50(7)) will provide technical guidance.

---

## Pattern 11: AI Regulatory Sandbox Entry Strategy

**When to use**: When a startup or innovator needs to develop and test a potentially high-risk AI system before full commercial deployment.

**How**:
1. Apply to the relevant national competent authority's AI regulatory sandbox (Art 57; Member States required to establish at least one by 2 August 2026).
2. Agree a sandbox plan covering objectives, conditions, timeframe, methodology, and requirements (Art 3(54)).
3. Within the sandbox: develop, train, validate, and test the system under regulatory supervision, including in real-world conditions if approved.
4. Data protection obligations remain fully in force during sandbox activities.
5. At sandbox exit: determine conformity assessment route; complete required assessments; register in EU database before market placement.

**Trade-offs**: Sandbox participation provides regulatory access and reduced market-entry risk but does not guarantee market authorisation; sandbox findings may result in redesign requirements. SME-specific provisions under Art 57 provide additional support and guidance.

---

## Pattern 12: Open-Source GPAI Compliance Strategy

**When to use**: When a provider is releasing a GPAI model under an open-source licence.

**How**:
1. Confirm the model meets the open-source definition: freely accessible, modifiable, and distributable; weights, architecture, and usage information publicly available.
2. If confirmed open-source and model is NOT systemic risk: exempt from Art 53(1)(a) technical documentation and Art 53(1)(b) downstream information obligations. Other obligations (copyright policy, training data summary) still apply.
3. If the open-source model IS systemic risk (10^25 FLOPs threshold met or Commission designation): all Art 53 and Art 55 obligations apply; the open-source exemption is lost.
4. Authorised representative obligations (Art 54) are also waived for qualifying open-source non-systemic-risk models.

**Trade-offs**: Open-source release eliminates documentation obligations but not systemic risk obligations; frontier open-source models (e.g. those matching leading closed-source capabilities) will still face the full obligation set. Community integration by downstream providers does not exempt those downstream providers from their own high-risk AI system obligations.

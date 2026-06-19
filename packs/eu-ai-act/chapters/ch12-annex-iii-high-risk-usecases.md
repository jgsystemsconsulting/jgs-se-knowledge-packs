# Chapter 12: Annex III — High-Risk AI Use Cases Reference

## Core Idea
Annex III is the exhaustive list of use-case areas that trigger high-risk classification under Art 6(2). It covers eight domains where AI systems are deemed to pose significant risks to health, safety, or fundamental rights by virtue of the nature of their deployment context, the vulnerability of affected persons, or the consequential weight of their outputs. This annex is a living document: the Commission may expand or contract it by delegated act under Art 7.

## Frameworks Introduced
- **Eight-area taxonomy**: The eight areas of Annex III are: (1) Biometrics; (2) Critical infrastructure; (3) Education and vocational training; (4) Employment, workers' management and access to self-employment; (5) Access to and enjoyment of essential private and public services and benefits; (6) Law enforcement; (7) Migration, asylum and border control management; (8) Administration of justice and democratic processes.
  - When to use: As the primary reference for determining whether a specific AI deployment falls under the high-risk classification and therefore the full Chapter III compliance burden.

## Key Concepts by Area

**Area 1 — Biometrics** (permitted under relevant Union/national law):
- Remote biometric identification systems (excluding one-to-one biometric verification).
- AI for biometric categorisation based on sensitive/protected attributes inferred from biometric data.
- Emotion recognition systems.

**Area 2 — Critical Infrastructure**:
- AI used as safety components in management/operation of critical digital infrastructure, road traffic, water/gas/heating/electricity supply.

**Area 3 — Education and Vocational Training**:
- Determining access/admission or assigning persons to educational/vocational training institutions at all levels.
- Evaluating learning outcomes, including where outcomes are used to steer the learning process.
- Assessing appropriate education level for an individual.
- Monitoring and detecting prohibited behaviour of students during tests (exam proctoring).

**Area 4 — Employment, Workers' Management and Access to Self-Employment**:
- Recruitment and selection: targeted job adverts, analysing/filtering job applications, evaluating candidates.
- Decisions affecting terms of work-related relationships, promotion, termination, task allocation based on individual behaviour or personal traits, performance monitoring and evaluation.

**Area 5 — Essential Private and Public Services and Benefits**:
- AI used by public authorities (or on their behalf) to evaluate eligibility for essential public assistance including healthcare benefits (grant, reduce, revoke, reclaim).
- Creditworthiness evaluation or credit scoring (excluding financial fraud detection).
- Risk assessment and pricing for life and health insurance.
- Evaluation and classification of emergency calls or dispatch/prioritisation of emergency first-response services (police, firefighters, medical aid, patient triage).

**Area 6 — Law Enforcement** (permitted under Union/national law):
- Assessing risk of a natural person becoming a victim of criminal offences.
- Polygraphs and similar tools used by law enforcement.
- Evaluating reliability of evidence in criminal investigation/prosecution.
- Assessing risk of a person offending or reoffending (not solely based on profiling).
- Profiling of natural persons in the course of criminal detection, investigation, or prosecution.

**Area 7 — Migration, Asylum and Border Control** (permitted under Union/national law):
- Polygraphs and similar tools used by competent authorities.
- Assessing security risk, irregular migration risk, or health risk posed by persons entering Member State territory.
- Assisting examination of asylum, visa, or residence permit applications including reliability of evidence.
- Detecting, recognising, or identifying natural persons in migration/asylum/border context (excluding travel document verification).

**Area 8 — Administration of Justice and Democratic Processes**:
- Assisting judicial authorities in researching/interpreting facts and law, or applying law to facts, or for alternative dispute resolution.
- AI for influencing election/referendum outcomes or voting behaviour of natural persons (excluding administrative/logistical campaign tools).

## Mental Models
- **"Power asymmetry as a trigger"**: Most Annex III areas share a common feature: the AI system operates in a context where the affected person is in a position of dependence or vulnerability relative to the deployer (public benefits claimant, job applicant, asylum seeker, defendant). This asymmetry is the policy rationale for elevated scrutiny.
- **"Decision weight as a trigger"**: High-risk use cases tend to produce outputs that directly or indirectly determine access to essential resources (employment, education, credit, healthcare, asylum, liberty) or expose persons to legal consequences. The weight of the output justifies the compliance burden.

## Anti-patterns
- Treating Annex III as static: Art 7 gives the Commission a standing delegated-act power to add, modify, or remove use cases. Compliance assessments must consider the current version of Annex III, not the version at the time of initial deployment.
- Assuming non-listed adjacent AI is safe: a system used to prepare for an Annex III task (preparatory task) may qualify under the de minimis carve-out (Art 6(3)(d)) as not high-risk, but must still be documented and registered (Art 6(4)).
- Ignoring the "solely on profiling" qualifier in area 6(d): recidivism prediction AI that incorporates objective evidence alongside profiling is NOT caught by the prohibition in Art 5(1)(d) but IS caught by Annex III area 6(d) as a high-risk system requiring full Chapter III compliance.

## Key Takeaways
1. Eight areas, each with specific sub-categories; the sub-category level determines whether a particular AI deployment is high-risk.
2. Areas 1, 6, and 7 include explicit qualifiers ("in so far as their use is permitted under relevant Union or national law"), reflecting that some deployments in these areas may be unlawful under other Union/national law entirely.
3. Area 8 includes election influence AI — a late addition reflecting democratic integrity concerns.
4. Creditworthiness scoring and insurance pricing AI are in Area 5; financial fraud detection AI is explicitly excluded from the creditworthiness sub-category.
5. Emergency dispatch triage AI (Area 5(d)) is high-risk, reflecting life-or-death decision contexts.
6. The de minimis carve-out (Art 6(3)) can exclude a system from high-risk classification even within an Annex III area, but documentation and registration obligations remain.

## Connects To
- **Chapter III Section 1 (Art 6-7)**: Annex III is the operative list for Route B high-risk classification.
- **Chapter III Section 2 (Art 8-15)**: All high-risk requirements apply to Annex III systems that are not carved out.
- **Chapter II (Art 5)**: Some Annex III area 1 (biometrics) and area 6 (law enforcement) sub-categories are also subject to the absolute prohibition on real-time RBIS in public spaces.
- **Chapter VII (Art 66)**: The Board advises on potential Annex III amendments; Art 7 delegated acts are how the Commission acts on Board recommendations.

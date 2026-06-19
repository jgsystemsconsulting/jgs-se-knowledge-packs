# Chapter 3: High-Risk AI Classification (Chapter III Section 1, Articles 6-7 + Annex III)

## Core Idea
An AI system is high-risk if it satisfies one of two routes: (1) it is a safety component of a product subject to Union harmonisation legislation AND that product requires third-party conformity assessment (Art 6(1)); or (2) it falls within one of the eight use-case areas listed in Annex III (Art 6(2)), unless it satisfies a narrow de minimis carve-out. High-risk classification is the gateway to the full set of requirements in Section 2.

## Frameworks Introduced
- **Article 6 two-route classification test**: Route A (product safety route) — Annex I sector + third-party conformity assessment required. Route B (Annex III route) — listed use-case area. Both routes can be satisfied independently.
  - When to use: As the primary classification decision tree for any AI product or system.
- **Article 6(3) de minimis carve-out**: An Annex III system is NOT high-risk if it (a) performs a narrow procedural task, (b) improves the result of a previously completed human activity, (c) detects decision-making patterns without influencing prior human assessment, or (d) performs a preparatory task to an Annex III assessment. Exception: if the system performs profiling, it is always high-risk regardless.
  - When to use: To check whether an Annex III-area system can be documented as not high-risk (Art 6(4) documentation obligation still applies).
- **Article 7 dynamic amendment power**: The Commission can add, modify, or remove use-case areas from Annex III by delegated act, using criteria including autonomy level, scale of harm, vulnerability of affected persons, and corrigibility of outputs.
  - When to use: When assessing future-facing compliance roadmaps for AI systems near but not yet in Annex III.
- **Annex III eight-area high-risk taxonomy**: The enumerated list of use-case areas triggering high-risk classification.
  - When to use: As the go-to reference for Annex III classification decisions.

## Key Concepts
- **Safety component** (Art 3(14)) — a component of a product or AI system that fulfils a safety function for that product or system, or whose failure would endanger health and safety of persons or property.
- **Annex I Route A sectors** — products covered by Union harmonisation legislation where third-party conformity assessment is required (machinery, toys, radio equipment, pressure equipment, recreational craft, cableways, PPE, gas appliances, medical devices, in vitro diagnostics, motor vehicles, aviation, agriculture, rail, maritime, etc.).
- **Annex III eight areas**: (1) Biometrics (RBIS, biometric categorisation, emotion recognition); (2) Critical infrastructure safety components; (3) Education and vocational training (admissions, evaluation, monitoring during exams); (4) Employment (recruitment, performance management, task allocation, termination); (5) Essential private/public services (creditworthiness, insurance pricing, benefit eligibility, emergency dispatch); (6) Law enforcement (victim risk assessment, evidence reliability, recidivism prediction, profiling); (7) Migration, asylum, border control (risk assessment, asylum examination, border detection); (8) Administration of justice and democratic processes (judicial decision support, election/referendum influence).
- **Profiling exception within de minimis carve-out** — Art 6(3) carve-out does not apply if the Annex III system performs profiling of natural persons; such systems are always high-risk.
- **Documentation requirement for non-high-risk Annex III claims** (Art 6(4)) — a provider who considers their Annex III system is not high-risk must document the assessment before placement and register in the EU database under Art 49(2).

## Mental Models
- **"Route A = sector + third-party test"**: For products, ask (a) does Annex I cover this product sector? and (b) does applicable sector law require third-party conformity assessment? Both yes = high-risk regardless of Annex III.
- **"Route B = use-case area + not de minimis"**: Ask (a) does the system fall within an Annex III area? and (b) does it fail all four de minimis conditions AND is it not a profiling system? Both yes = high-risk.
- **"Profiling always wins"**: Even if a system passes all four de minimis conditions, profiling of natural persons makes it high-risk. This is a hard override.

## Anti-patterns
- Treating Annex III as a complete list with no evolution: Art 7 expressly empowers the Commission to expand or contract Annex III by delegated act based on evidence of harm.
- Assuming the de minimis carve-out is self-executing: the provider must document the non-high-risk assessment (Art 6(4)) and register in the EU database — the carve-out is not automatic exemption from all obligations.
- Confusing Route A and Route B: a system can be high-risk under Route A (product safety component) even if its specific use case is not in Annex III.

## Key Takeaways
1. Two independent routes to high-risk classification — product safety (Route A) and use-case list (Route B, Annex III).
2. Annex III covers eight areas; election influence AI and judicial decision support AI are included.
3. De minimis carve-out in Art 6(3) is narrow: four conditions, any of which can exclude high-risk status, but profiling overrides all.
4. Providers claiming de minimis must still document and register (Art 6(4)) — they are not entirely outside the Act.
5. Commission guidelines on practical implementation of Art 6 were due by 2 February 2026.
6. Annex III is a living document: the Commission's Art 7 delegated-act power means classification may change over time.

## Connects To
- **Chapter III Section 2 (Art 8-15)**: High-risk classification is the gateway to all technical requirements.
- **Chapter III Section 3 (Art 16-27)**: Obligations attach by role once a system is classified as high-risk.
- **Annex I**: Union harmonisation legislation whose sectors trigger Route A high-risk.
- **Chapter XII (Art 99)**: Non-compliance with high-risk requirements carries fines up to EUR 15 million or 3% of turnover.

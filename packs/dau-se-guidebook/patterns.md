# Patterns: DoD Systems Engineering Guidebook (September 2026)

Reusable When / How / Trade-offs patterns from the September 2026 edition.

## Pattern: Pathway-tailored SE approach

- **When:** Any AAF pathway program standing up technical planning.
- **How:** Write an SE approach (and SEP when required) that names process depth, review set, digital/data approach, and design-consideration drivers. Scale to risk and need for speed.
- **Trade-offs:** More rigor slows delivery; less rigor hides integration and safety risk. Record the choice.

## Pattern: Knowledge-gated reviews

- **When:** Planning ASR through PCA (or the pathway subset).
- **How:** Define entrance and exit logic first. Hold the event when evidence exists. Track actions to close.
- **Trade-offs:** Calendar pressure versus decision quality. Sliding a gate without evidence only moves risk downstream.

## Pattern: Digital authoritative baseline

- **When:** Program adopts DE/MBSE under SE modernization.
- **How:** Mature models with metadata, manage them under configuration control as an authoritative source of truth, and show model evidence in reviews and the TDP.
- **Trade-offs:** Tooling and skill cost versus document churn and late discovery. Models without control become a second shadow baseline.

## Pattern: Agile inside the SE V

- **When:** Software-heavy or iterative subsystem development.
- **How:** Run Agile/DevSecOps iterations for delivery speed, reserve capacity for technical debt, and map iteration evidence into SRR/PDR/CDR-class baseline questions.
- **Trade-offs:** Iteration speed versus baseline stability. Skipping baseline confirmation creates integration debt.

## Pattern: Integrated design-consideration trades

- **When:** Architecture and preliminary design trades open.
- **How:** Screen all 24 considerations for relevancy. Put drivers in the SEP. Trade affordability, R&M, safety, security, MOSA/modularity, and supportability together.
- **Trade-offs:** Optimizing one specialty in isolation creates stovepipe failure modes.

## Pattern: Technical data and interface control

- **When:** Multiple developers, FoS/SoS context, or long sustainment tail.
- **How:** Stand up interface management (often with an ICWG) and technical data management with explicit data-rights strategy.
- **Trade-offs:** Up-front data and interface work versus lock-in and unsupportable fielded systems.

## Pattern: SoS depth outside this pack

- **When:** Program is deeply coupled to an SoS or FoS.
- **How:** Keep enterprise dependency framing from Section 2, then use the updated SoS guide for SoS practice moved out of this edition.
- **Trade-offs:** Staying only inside this pack under-serves SoS engineering after the content move.

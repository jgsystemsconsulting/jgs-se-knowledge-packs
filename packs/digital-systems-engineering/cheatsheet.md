# Digital Systems Engineering Cheatsheet

Decision rules and quick-reference tables distilled from *Towards Digital Engineering*
(Huang et al., arXiv:2002.11672, 2020). Judgment and selection guidance — see `glossary.md`
for definitions and the chapters for full reasoning.

## Digitize vs. Digitalize (the core distinction)
- **Digitized** = converted analog→digital, possibly computerized, but NOT yet in standard form with operating metadata. Loose-format image; scanned book.
- **Digitalized** = standard machine-accessible representation + unique identifier + standard metadata, all uniquely bound. Standardized photo with camera/time/place metadata; eBook with cross-reader + rights metadata.
- Rule: if a machine can't operate on or interoperate over it automatically, it's digitized, not digitalized.

## The four-part digitalization test
1. Standard, machine-accessible representation (well-defined semantics)
2. Unique identifier assigned and kept
3. Standard metadata enabling automated machine operation
4. Identifier + metadata uniquely bound to the item (digital signatures, blockchain)
- Miss any one → not digitalized.

## Digital augmentation = the three parts of a digitalized artifact
| Component | What it is | For physical objects |
|---|---|---|
| Digital representation | Standard, machine-accessible form | Digital twin → picture → text description |
| Unique identifier | Uniquely associated, for traceability/accountability | Barcode, RFID |
| Metadata | Standard semantics, enables automation | Properties of object + of representation |

## Digitalized-model metadata (richer than ordinary artifacts)
Generic attributes · inputs/outputs/parameters · provenance · utilization guide · security properties · machine-processible access-control policies.
- Models get the heaviest schema because digital representation of the system of interest is the central theme of DE.

## The five DES goals as a dependency stack (read bottom-up)
| Layer | Goal | Role |
|---|---|---|
| Top (driver) | G3 — End-to-end digital enterprise | Driving force; issues new requirements downward |
| Middle | G1 — Formalized model lifecycle | The *fundamental* goal; builds on G2 |
| Middle | G2 — Authoritative Source of Truth | Builds on G4; feeds G1 |
| Foundation | G4 — Transformed IT infrastructure | IT basis |
| Foundation | G5 — Transformed culture & workforce | Human/organizational base |
- Rule: don't pursue an upper goal until its lower layers exist. Skipping a layer leaves the upper ones unsupported.

## The four-level DSE framework (read top-down as a realization chain)
| Level | Question | Content |
|---|---|---|
| 1 Vision | Why | Needs analysis; goals/advantages of engineering in the digital age |
| 2 Strategy | What moves | Transform practice · transform workforce/education · transform infrastructure · embrace innovative tech |
| 3 Action | What work | Digitalize artifacts · operate on them · run lifecycle activities with them · build innovative applications |
| 4 Foundation | What enables it | Digitalization foundations · digital trust · cybersecurity · big data & ML |
- A problem placed too high without its foundation has nothing to stand on.

## Six operations on digitalized artifacts (Action level)
Creation · Curation · Qualification · Governance · Sharing · Utilization.
- Cross these against the five lifecycle stages (Concept, Development, Production, Utilization/Support, Retirement) — a research/engineering issue appears in *every* cell.

## Centralized vs. distributed — the recurring dial
| Domain | Centralized (near-term efficient) | Distributed (long-run resilient) |
|---|---|---|
| Standardization | One official issued standard | Crowdsourced evolutionary ontologies; most-used converges |
| Trust | Single AST | Digital signatures, distributed certification, evidence-based, blockchain |
| Access control | Single policy regime | Heterogeneous policies reconciled by integration frameworks |
- Centralization wins on near-term speed but concentrates risk (single point of failure, wrong-direction lock-in, stifled innovation if set too early).
- Distribution hedges those risks at the cost of near-term efficiency (e.g., costly ontology mapping).
- Hybrid sits between: decentralized AST hierarchies/meshes (like PKIs).

## Access-control paradigm by operating world
| World | Paradigm | Basis |
|---|---|---|
| Military / government | MAC / Multilevel Security | Bell-LaPadula |
| Business | RBAC | Sandhu et al. |
| General, attribute-driven | ABAC | XACML policy language |
- Enduring tension: need-to-know vs. need-to-share; reconcile with trust-integration frameworks.

## Provenance maturity ladder
Data Provenance (where/why in data workflows) → Knowledge Provenance (origin/validity of knowledge) → Open Provenance Model (standardized) → PROV (ontology usable for engineering artifacts).
- Where a capability sits on the ladder tells you how far it can be trusted for engineering artifacts.

## Reproducibility ladder (imported from science)
Reproducibility (same procedures, same data) → Replicability (same procedures, different data) → Generalizability (results hold in different contexts).
- Each rung is harder; engineering loses a rung's worth of stability whenever tacit human know-how disappears.

## Five enabling-technology clusters (a portfolio, not a silver bullet)
| Cluster | Stage of an artifact's life-of-trust it owns |
|---|---|
| AI & Machine Learning (central) | Produced — automation, digital representation, model-building |
| Ontologies & Semantics | Made meaningful & shareable across boundaries |
| Provenance modeling | Given lineage — value, integrity, reproducibility |
| Trust management | Protected & adjudicated — access control, trust judgment |
| Computing infrastructure (HPC/cloud/big data) | Stored & computed over at scale |
- Wrong question: "which technology enables DE?" Right question: "is every cluster covered?"

## Tells & smells
- "We went digital" but a machine can't operate on the artifact automatically → digitized, not digitalized.
- An AST model with no recorded provenance → just data, not a reusable accountable asset.
- A DE program investing in modeling (G1) with no repository (G2), IT (G4), or prepared workforce (G5) → upper layer with no foundation.
- Standardizing an emerging field too early via one fixed standard → risk of wrong-direction lock-in and stifled innovation.
- Treating DSE and MBSE as rivals → they're complementary: MBSE drives document→model-centric; DSE adds digitalization, identification, big data, digital trust.
- The "five Vs" of big data in the connected environment: volume, velocity, variety, veracity, *views*.

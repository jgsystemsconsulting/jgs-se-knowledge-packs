# Digital Systems Engineering Patterns & Techniques

Concrete techniques drawn from *Towards Digital Engineering* (Huang et al., arXiv:2002.11672,
2020). The source is a vision paper, so these are conceptual practices and analytical moves it
proposes — not step-by-step procedures. Each entry gives when to reach for it, how the source
frames it, and the trade-offs it names.

## Digitalize, Don't Just Digitize
**When to use**: Whenever someone claims an artifact is "digital" and you need to know what a machine can actually do with it.
**How**: Apply the four-part test — (1) standard, machine-accessible representation with well-defined semantics; (2) a unique identifier assigned and kept; (3) standard metadata enabling automated machine operation; (4) identifier and metadata uniquely bound to the item (e.g., via digital signatures or blockchain). Miss any part and you have a digitized, not a digitalized, artifact.
**Trade-offs**: Full digitalization costs effort up front (standard form, semantics, metadata); but a merely digitized artifact cannot participate in automated, cross-machine workflows — the gate every downstream capability passes through.

## Locate an Artifact on the Digitalization Spectrum
**When to use**: To set realistic expectations for automation before committing to a "digital xxx" capability.
**How**: Rate the artifact on four dials — representation fidelity, semantic depth, form compatibility, metadata richness. Those four predict how much automated machine operation and interoperation is possible.
**Trade-offs**: Treating digitalization as binary over-promises; the vague phrase "digital xxx" can sit anywhere on the continuum, so naming the dials prevents disappointment at integration time.

## Attach a Digital Augmentation to Every Artifact
**When to use**: When you need any artifact (model, dataset, product, part, service, process) to be machine-processable and traceable.
**How**: Wrap the artifact in three components — a digital representation (standard, machine-accessible form; for a digital object this *is* the object, for a physical object it ranges from a digital twin down to a picture or text), a uniquely associated identifier (barcode/RFID for physical things), and associated standard-semantics metadata covering the artifact's and the representation's properties.
**Trade-offs**: Adds authoring and maintenance overhead per artifact; without it, artifacts can't be operated on automatically or traced across organizations and lifecycle phases.

## Give Models the Richer Metadata Schema
**When to use**: When the artifact being digitalized is a model — the most important artifact class for digital engineering.
**How**: Beyond the generic digital-augmentation metadata, capture: generic attributes; inputs/outputs/parameters; provenance; a utilization guide; security properties; and machine-processible access-control policies. Build toward a "model of models" using knowledge representation to express the properties of and relations among model types.
**Trade-offs**: The schema is heavier than for ordinary artifacts; justified because digital representation of the system of interest is the central theme of digital engineering.

## Choose Centralized Standards vs. Distributed Ontologies by Time Horizon
**When to use**: When deciding how shared digital representation, semantics, and vocabulary get standardized.
**How**: Reach for an officially issued (centralized) standard when you need short-term efficiency and central coordination. Reach for distributed, crowdsourced ontologies when you want long-term evolvability and collective intelligence — working groups build new ontology parts on reused parts, and the most-used version converges into a de facto standard that an authority can later issue as official.
**Trade-offs**: Centralized standards are efficient short-term but risk a single point of failure, a wrong-direction commitment, and stifled innovation if set too early. Ontologies are less efficient short-term (mapping is often needed and costly) but harness collective intelligence and allow micro-level revision.

## Match the Access-Control Paradigm to the Operating World
**When to use**: When the Authoritative Source of Truth must serve entities running different access-control regimes.
**How**: Government/military leans MAC (Bell-LaPadula / Multilevel Security); business leans RBAC; general, attribute-driven policy needs lean ABAC expressed in XACML. Use trust-integration frameworks to reconcile the paradigms and balance "need-to-know" against "need-to-share."
**Trade-offs**: No single paradigm fits all; the enduring tension is need-to-know vs. need-to-share, now compounded by cybersecurity threats and IP/competitive concerns.

## Use Provenance as the Basis for Reuse and Reproducibility
**When to use**: Before reusing a model or data artifact pulled from a shared repository.
**How**: Require recorded provenance so traceability can underwrite a trustworthiness judgment; trace dependency relationships among artifacts to support reproducibility and replicability. Locate the capability on the maturity ladder — Data Provenance (where/why in data workflows) → Knowledge Provenance (origin/validity of knowledge) → Open Provenance Model (standardized) → PROV (an ontology usable for engineering artifacts).
**Trade-offs**: Without provenance a model in the AST is just data; with it the model becomes a reusable, accountable asset — but longer, cross-organizational provenance chains weaken the trust they carry.

## Read the Five Goals as a Load-Bearing Stack
**When to use**: When planning or auditing a digital-engineering transformation program against the DES.
**How**: Order the five DES goals as dependencies, not a flat checklist — Goal 5 (workforce/culture) and Goal 4 (IT) are the foundations; Goal 2 (AST) builds on Goal 4 and feeds Goal 1 (formalized model lifecycle); Goal 3 (digital enterprise) sits on top as the driving force whose pursuit of new technology issues fresh requirements downward.
**Trade-offs**: Skipping a lower layer leaves upper goals without support — you cannot pursue formalized modeling without a repository, IT foundation, and prepared workforce beneath it.

## Place a Research or Engineering Problem in the Four-Level Framework
**When to use**: To locate any digital-systems-engineering problem at the right altitude and see its dependencies.
**How**: Map the problem to Vision (why), Strategy (what moves), Action (what work), or Foundation (what makes it possible). At the Action level, use the operation × lifecycle matrix — model operations (creation, curation, qualification, governance, sharing, utilization) crossed against the five lifecycle stages — to enumerate research issues systematically; an issue appears in every cell.
**Trade-offs**: A problem placed too high without its foundation has nothing to stand on; a foundation built without a vision solves nothing in particular.

## Tune the Centralization Dial Deliberately Across Domains
**When to use**: When facing standardization, trust, or access-control design under a connected, multi-party environment.
**How**: Recognize these as the same dial in different domains. Turn toward centralization for near-term speed and efficiency; turn toward distribution to hedge single points of failure and long-run misdirection. The source's meta-principle: preserve diversity through evolution, drawn equally from biological populations and technological approaches.
**Trade-offs**: Over-centralizing concentrates risk and can lock in a wrong direction; over-distributing sacrifices near-term efficiency. Hybrid mechanisms (e.g., decentralized hierarchies/meshes of ASTs, like PKIs) sit between the poles.

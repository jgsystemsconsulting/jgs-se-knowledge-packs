# Digital Systems Engineering Glossary

Key terms from *Towards Digital Engineering: The Advent of Digital Systems Engineering*
(Huang et al., arXiv:2002.11672, 2020). Definitions paraphrase the source; chapter refs point
to where the term is developed.

**Access Control** — Mechanisms governing which entities may use a stored artifact; the source names MAC, RBAC, and ABAC as paradigms the Authoritative Source of Truth must reconcile (Ch 3, Ch 4).

**ABAC (Attribute-Based Access Control)** — The more recent access-control paradigm allowing general, attribute-driven policies, expressed via the XACML standardized policy language (Servos & Osborn, 2017) (Ch 4).

**Action Level** — Level 3 of the four-level framework: the concrete work of digitalizing artifacts, operating on them, running lifecycle activities with them, and building innovative applications (Ch 6).

**Artificial General Intelligence (AGI)** — The swing of AI back from domain-focused systems toward general intelligence, framed as paving the way for a new generation of intelligent engineering systems (Ch 4).

**Authoritative Source of Truth (AST)** — A shared, governed repository hosting standardized models, data, and artifacts; the central hub of the DoD Digital Engineering Strategy. Captures provenance, maintains traceability, and propagates updates to dependent entities (Ch 1, Ch 2, Ch 3, Ch 4, Ch 6).

**Big Data** — Data of unprecedented volume, variety, quality range, and streaming velocity flooding every connected engineering process; both an asset (quality, cost) and a burden (processing, integration, sharing) (Ch 3, Ch 4, Ch 6).

**Blockchain** — A technology for verifying data integrity and supporting distributed digital trust; named as essential to system security and one route to unique binding of identifier and metadata (Ch 4, Ch 5, Ch 6).

**Centralized vs. Distributed** — The recurring tension across standardization, trust, and access control: centralization is faster and more efficient near-term but concentrates risk; distribution hedges single points of failure and long-run misdirection (Ch 3, Ch 5, Ch 6).

**Computing Infrastructure** — The HPC / cloud / big-data cluster supplying scalable, elastic, ubiquitous compute; a hard dependency for digital engineering, not a convenience (Ch 4, Ch 6).

**Cyber-Physical-Social Smart Systems (CPS3)** — The class of innovative systems the Internet of Things enables (Huang, Seck, & Gheorghe, 2016) (Ch 1).

**Data-Intensive Systems Engineering** — A proposed approach centering trustworthy AI systems, ML models, and algorithms for knowledge discovery from large data, with goals of reliable performance, explainability, safety, security, resilience, and scientific-computing integrity (Ch 6, Ch 7).

**Digital Augmentation** — The machine-processable wrapper attached to a digitalized artifact, made of three parts: a digital representation, a uniquely associated identifier, and associated metadata (Ch 5, Ch 6).

**Digital Engineering (DE)** — The digital transformation of engineering to leverage digital technologies; the destination toward which digital transformation of engineering is heading (Ch 1, Ch 5).

**Digital Engineering Strategy (DES)** — The US DoD's 2018 strategy to build a digital enterprise, quickly absorb innovation, and connect formal models across boundaries through an Authoritative Source of Truth (Ch 1, Ch 2, Ch 3).

**Digital Systems Engineering (DSE)** — The emerging academic field developing the theory, methods, models, and tools that bring digital technologies into systems engineering to support digital engineering practice (Ch 1, Ch 6, Ch 7).

**Digital Twin** — A full digital representation of a physical object; the richest end of the digital-representation range for physical artifacts (Glaessgen & Stargel, 2012) (Ch 1, Ch 5).

**Digitalization** — Giving an item a standard, machine-accessible representation, a unique identifier, and standard metadata, all uniquely bound together (the four-part definition); goes beyond mere digitization (Ch 5, Ch 6, Ch 7).

**Digitalized Artifact** — An artifact plus its digital augmentation (representation + identifier + metadata); the schema for any artifact, digital or physical, once digitalized (Ch 5, Ch 6).

**Digitalized Model** — A specialization of the digitalized artifact for models, with a richer metadata schema: generic attributes, I/O and parameters, provenance, utilization guide, security properties, and machine-processible access-control policies (Ch 5).

**Digitize** — Conversion from analog to digital form (Gartner); a digitized item may be computerized but is not yet in standard form with the metadata that lets machines operate on it automatically (Ch 5).

**Foundation Level** — Level 4 of the four-level framework: enabling technologies and foundational research — digitalization foundations, digital trust mechanisms, cybersecurity, and big data & ML (Ch 6).

**Fourth Paradigm** — Jim Gray's vision of data-intensive science as the fourth scientific paradigm after the empirical, theoretical, and computational; invoked to argue data can yield insight theory alone cannot (Ch 1).

**Generalizability** — Per the NSF definition adopted by the paper: applicability of results to different contexts; the top rung above reproducibility and replicability (Ch 3).

**Industry 4.0** — The fourth industrial revolution driven by industrial IoT and smart cyber-physical systems; a label for digital transformation in industry (GTAI, 2014; Schwab, 2017) (Ch 1, Ch 6).

**Internet of Things (IoT)** — The fast-growing network of connected things reshaping how systems are conceived and operated; an enabler of lifecycle-wide traceability (Atzori, Iera, & Morabito, 2010) (Ch 1).

**Knowledge Provenance (KP)** — Determining the origin and validity of knowledge by modeling information sources, dependencies, and trust structures (Fox & Huang, 2003) (Ch 4).

**Knowledge Representation & Reasoning (KR&R)** — The AI machinery, grounded in formal logic, for representing artifacts (especially models) with well-defined semantics; a foundation for digitalization (Ch 5, Ch 6).

**MAC (Mandatory Access Control) / Multilevel Security** — Access-control paradigm based on the Bell-LaPadula model, framed as serving military and government entities (Bell & LaPadula, 1973) (Ch 3, Ch 4).

**MBSE (Model-Based Systems Engineering)** — The formalized application of modeling to support SE from conceptual design through the lifecycle; moves SE from document-centric to model-centric. DSE's complementary partner discipline, not a rival (INCOSE, 2007) (Ch 6).

**Model of Models** — Using knowledge representation to explicitly capture the properties of, and logical relations among, different model types; groundwork for the ontologies expressing models' digital augmentations (Ch 5, Ch 7).

**Ontology** — A formal, explicit specification of a shared conceptualization (Gruber, 1993); the conceptual hinge letting models be shared and integrated across boundaries, and a distributed, evolutionary route to standardization (Ch 4, Ch 5, Ch 6).

**Open Provenance Model (OPM)** — A milestone provenance standard arising from eScience and scientific-workflow research; further developed into the PROV ontology (Moreau et al., 2011) (Ch 4).

**PROV Ontology** — The W3C development of the Open Provenance Model, positioned as able to model provenance for engineering artifacts (W3C, 2013) (Ch 4).

**Provenance** — Recorded lineage of an artifact (its where/why, dependencies, validity); the basis for judging value and integrity, and the enabler of model reproducibility and replicability (Ch 2, Ch 4, Ch 7).

**RBAC (Role-Based Access Control)** — The business-world access-control paradigm (Sandhu et al., 1996) (Ch 3, Ch 4).

**Reinforcement Learning** — ML illustrated by AlphaGo; invoked for continuous improvement of a system's operational performance (Silver et al., 2018; Sutton & Barto, 2018) (Ch 4).

**Replicability** — Per the NSF definition: same procedures applied to different data; the middle rung of the reproducibility ladder (Ch 3).

**Reproducibility** — Per the NSF definition: same procedures applied to the same data; the bottom rung, imported from the science reproducibility crisis as a warning to engineering (Ch 3).

**Scientific Computing Integrity (SCI)** — High confidence that scientific data has an understood process, provenance, and correctness; can be compromised by attack or by faults in equipment, software, networks, or people (DOE ASCR; Peisert, Cybenko & Jajodia, 2015) (Ch 3, Ch 4).

**Strategy Level** — Level 2 of the four-level framework: four strategic moves — transform practice, transform workforce/education, transform infrastructure, embrace innovative technologies in operations (Ch 6).

**Trust Management** — The cluster supplying the access and trust mechanisms (centralized, decentralized, distributed, hybrid) that make an Authoritative Source of Truth defensible (Ch 4, Ch 6).

**Unique Identification** — Assigning and binding a unique identifier to an artifact; the foundation for traceability and accountability across information, material, causality, and fault chains (Ch 5, Ch 6, Ch 7).

**Vision Level** — Level 1 of the four-level framework: a clear, general vision of engineering in the digital age, reached via needs analysis and the goals/advantages to pursue (Ch 6).

**XACML** — The eXtensible Access Control Markup Language standardized policy language used to express ABAC policies (OASIS, 2013) (Ch 4).

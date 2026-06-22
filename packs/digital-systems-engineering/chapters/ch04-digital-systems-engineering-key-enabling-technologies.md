# Chapter — Key Enabling Technologies

> Source: Huang, Gheorghe, Handley, et al., *Towards Digital Engineering — The Advent of Digital Systems Engineering*, arXiv:2002.11672 (preprint of the paper in press at *Int. J. System of Systems Engineering*). This chapter is grounded only in the arXiv preprint, Section 4 (not the paywalled journal version). The paper is thin (~28 pp); this section is a deliberately brief, illustrative survey rather than a comprehensive technology review — the authors note that space prevents an exhaustive treatment and instead sketch several clusters.

## Core Idea

Digital engineering does not run on a single breakthrough technology; it is carried by several distinct *clusters* of enabling technology that each solve a different part of the problem of producing, sharing, trusting, and computing over digital engineering artifacts at scale. The paper organizes the landscape into five clusters: an AI & machine-learning cluster (treated as the central, foundational one), an ontologies-and-semantics cluster, a provenance-modeling cluster, a trust-management cluster, and a computing-infrastructure cluster spanning HPC, cloud, and big data. The through-line is that each cluster answers a question the others cannot: AI/ML supplies automation and model-building intelligence; ontologies supply shared meaning so models cross boundaries; provenance supplies the lineage needed to judge an artifact's value and integrity; trust management supplies the access and trust mechanisms that make an authoritative source of truth defensible; and the computing infrastructure supplies the scalable, elastic, ubiquitous compute the rest depend on. Treating these as a portfolio — rather than betting on one — is the chapter's organizing principle.

## Frameworks Introduced (exact source names, when/how)

The slice cites a number of named technologies, models, standards, and reference works. These are surfaced here with the role the paper assigns each — not as endorsements, but as the literature anchors the authors use to ground each cluster.

- **US national AI research and development strategy** (attributed to US NSTC, 2016 and 2019) — invoked to show national-level investment driving AI's broad societal impact, framing why AI/ML is the central cluster.
- **One Hundred Year Study on Artificial Intelligence (AI100)** (Stanford, 2016) — cited as a panoramic account of AI's history and trajectory.
- **Machine learning** (LeCun, Bengio, & Hinton, 2015) — the foundational reference for the ML strand of the cluster.
- **Big Data technologies** — named instances: Apache Spark's TensorFlowOnSpark and Apache Hadoop Submarine, positioned as the means to build system models from large data gathered across a digitalized, connected lifecycle.
- **Reinforcement learning** (Silver et al., 2018; Sutton & Barto, 2018) — illustrated by AlphaGo defeating the world's top Go player; the paper's point is continuous improvement of a system's operational performance.
- **Artificial general intelligence** (Adams et al., 2012) — cited as the swing back from domain-focused AI toward general intelligence, framed as paving the way for a new generation of intelligent engineering systems.
- **Gruber's ontology definition** (Gruber, 1993; also Studer, Benjamins, & Fensel, 1998) — supplies the working definition of an ontology as a formal, explicit specification of a shared conceptualization, anchoring the semantics cluster.
- **Semantic web / ontology engineering references** (Baclawski et al., 2018; Fritzsche et al., 2017) — cited as related AI subfields focused on formalizing semantics and knowledge sharing.
- **Enterprise modeling and enterprise integration research** (Chen, Doumeingts, & Vernadat, 2008; Fox & Huang, 2005; Goranson, 2002) — invoked as a body of work since the 1990s supporting model sharing across boundaries.
- **Data Provenance** (Buneman, Khanna, & Tan, 2001) — credited as the first proposal of the term, addressing the *where* and *why* questions in complex data workflows.
- **Knowledge Provenance (KP)** (Fox & Huang, 2003) — addresses determining the origin and validity of knowledge by modeling information sources, dependencies, and trust structures.
- **Open Provenance Model** (Moreau et al., 2011) — described as a milestone arising from provenance research in eScience and scientific workflows.
- **PROV ontology** (W3C Provenance Working Group, 2013) — the further development of the Open Provenance Model; positioned as able to model provenance for engineering artifacts. The integrity argument is anchored to Berners-Lee, Hall, Hendler, Shadbolt, & Weitzner (2006).
- **Bell-LaPadula model** (Bell & LaPadula, 1973) — the basis for Mandatory Access Control (MAC) / Multilevel Security, framed as serving military and government entities.
- **Role-Based Access Control (RBAC)** (Sandhu et al., 1996) — framed as the business-world paradigm.
- **Attribute-Based Access Control (ABAC)** (Servos & Osborn, 2017) — the more recent paradigm allowing more general, attribute-driven policies, expressed via the **XACML** standardized policy language (OASIS, 2013).
- **Trust-integration frameworks** — three works are cited together (Jin et al., 2012; and two by Huang and colleagues in 2012) as proposals for integrating different access models and balancing "need-to-know" against "need-to-share."
- **Computational trust research** (Cho, Chan, & Adali, 2015; Huang, 2018; Huang & Nicol, 2009; Marsh, 1994; Huang & Nicol, 2013) — cited as enabling trust mechanisms ranging from centralized (standards and certifications) to distributed (evidence-based, distributed attribute certifications).
- **Blockchain** (Wang et al., 2019) — named as a recent technology for verifying data integrity, framed as essential to system security.
- **Cloud computing / HPC / Big Data infrastructure references** (Armbrust et al., 2010; ASCR, 2016; NIST, 2018; Asch et al., 2018; Keahey & Parashar, 2014) — anchor the computing-infrastructure cluster, including the extreme-scale-computing-as-competitive-advantage argument and the emerging trend of blending cloud into scientific HPC.

## Key Concepts

- **The five clusters as a division of labor.** AI/ML (automation, digital representation, model-building, intelligent reasoning/control/scheduling/planning/decision-making); ontologies and semantics (semantic representation of model properties and relations, cross-boundary model sharing and integration, digital representation of enterprise concepts and processes); provenance (representing and maintaining artifact lineage, tracing dependencies, supporting reproducibility and replicability, aiding trustworthiness evaluation); trust management (building an authoritative source of truth, access control over stored artifacts, trust judgment of models); and computing infrastructure (scalable, elastic, timely, ubiquitous storage/management/query/processing/mining/analysis plus large-scale cross-boundary collaboration).
- **AI/ML as the foundational cluster.** The paper singles out AI/ML as central — it is what makes continuing automation in digital engineering possible and what underwrites the digital representation and model-building the other clusters operate on.
- **The trajectory of AI: general → domain-focused → general again.** The slice frames AI as having traveled from a general ambition to domain-focused systems and now swinging back toward artificial general intelligence, which it ties to a coming generation of intelligent engineering systems.
- **Ontology as shared meaning.** Gruber's definition — a formal, explicit specification of a shared conceptualization — is the conceptual hinge that lets models be shared and integrated across enterprise, discipline, and lifecycle-stage boundaries.
- **Provenance as the basis for value and integrity.** Provenance information is positioned as critical to judging an artifact's value and integrity; the *Data Provenance → Knowledge Provenance → Open Provenance Model → PROV* lineage shows the concept maturing from data workflows toward something usable for engineering artifacts.
- **Access control as a spectrum matched to context.** MAC/Multilevel Security for military and government, RBAC for business, ABAC for more general attribute-driven policy — the paper presents these not as competitors but as paradigms fit to different needs, unified by frameworks that balance need-to-know against need-to-share.
- **The "right data, right person, right use, right time" goal.** Trust management exists so that each consumer receives exactly the data they need, fit to their intended use, delivered when it is required — the chapter's compact statement of what an authoritative source of truth must achieve.
- **Compute as a dependency multiplier.** Digital engineering is framed as depending on computing infrastructure far more than traditional engineering, with extreme-scale computing treated as a core capability for competitive advantage.

## Mental Models

- **Portfolio, not silver bullet.** Read the enabling technologies as a portfolio of clusters, each covering a gap the others leave open. Asking "which technology enables digital engineering?" is the wrong question; the right one is "is every cluster covered?"
- **The artifact's lifecycle of trust.** An engineering artifact is *produced* (AI/ML), *made meaningful and shareable* (ontologies), *given lineage* (provenance), *protected and adjudicated* (trust management), and *stored and computed over at scale* (infrastructure). Each cluster owns one stage of an artifact's journey from creation to trustworthy reuse.
- **Provenance maturity ladder.** Data Provenance answers *where/why* in data workflows; Knowledge Provenance extends to *origin and validity of knowledge*; the Open Provenance Model standardizes it; PROV makes it an ontology usable for engineering. Locating a capability on this ladder tells you how far it can be trusted for engineering artifacts.
- **Access control as a fit-to-context choice.** Pick the paradigm by the world you operate in — government/military leans MAC, business leans RBAC, general policy needs lean ABAC/XACML — and use integration frameworks to reconcile the tension between sharing and restricting.

## Key Takeaways

- Digital engineering is enabled by five technology clusters, with AI & machine learning treated as the central, foundational one.
- The other four clusters each close a specific gap: shared meaning (ontologies/semantics), artifact lineage (provenance), defensible trust and access (trust management), and scalable compute (HPC/cloud/big data).
- Provenance is the basis for judging an artifact's value, integrity, reproducibility, and trustworthiness, and the paper traces a clear lineage of the concept up to the PROV ontology.
- Trust management aims to get each consumer the data they need, fit to their intended use and delivered when required, drawing on a spectrum of access-control paradigms (MAC, RBAC, ABAC) plus blockchain for integrity verification.
- Computing infrastructure is a hard dependency, not a convenience: digital engineering leans on extreme-scale, cloud, HPC, and big-data capabilities far more than traditional engineering does.
- The treatment is deliberately brief and illustrative; it names anchor references per cluster rather than offering a comprehensive review.

## Connects To

- **Authoritative Source of Truth (AST):** the trust-management cluster exists to build and protect the AST referenced elsewhere in the paper — access control and trust judgment are how an AST stays authoritative.
- **Provenance and unique identification:** the provenance cluster underpins the paper's core claims about traceability, accountability, reproducibility, and replicability of digital artifacts across the lifecycle.
- **Digital representation and model-building:** the AI/ML cluster supplies the digital representation and machine-learned models that the paper's broader vision of digitalized artifacts depends on.
- **Cross-boundary sharing:** the ontologies/semantics cluster operationalizes the paper's goal of model and information sharing across enterprises, disciplines, and lifecycle stages.
- **Computing infrastructure as foundation layer:** the HPC/cloud/big-data cluster maps to the foundation layer in the paper's four-level picture (vision, strategy, action, foundation).

# Chapter — Challenges in Digital Engineering

> Source: Huang et al., "Towards Digital Engineering — The Advent of Digital Systems Engineering" (arXiv preprint 2002.11672; *Int. J. System of Systems Engineering*, in press). This chapter is grounded **only** in the open-access arXiv PDF, not the paywalled journal version. Section 3, "Challenges."

## Core Idea

Digital engineering transformation is not blocked by a single obstacle but by a constellation of them. The authors lay out eight named challenges that any organization pursuing digital engineering has to confront, framed against three reference points: the goals being targeted, the digital transformations that are actually needed, and the state of current engineering practice. The recurring tension running through the list is between **centralized** approaches — which the authors repeatedly judge faster and more effective in the near term — and **distributed/evolutionary** approaches, which protect against single points of failure and long-run wrong turns. Most of the named challenges are not purely technical; several are governance, trust, workforce, and institutional problems that surface precisely because engineering work is now expected to be shared as models and data across organizational and national boundaries.

## Frameworks Introduced (exact source names, when/how)

The Challenges section is organized as a numbered enumeration. The eight named challenges, as the source titles them:

- **Challenge 1: Big Data issues in digital engineering** — introduced to flag that every engineering process in a connected environment will be flooded with data of unprecedented size, varied form and quality, and high streaming velocity.
- **Challenge 2: Centralized standardization vs. distributed evolutionary standardization** — introduced around how shared digital representation, semantics, and vocabulary get standardized, contrasting a single fixed standard against crowdsourced, evolving ontologies.
- **Challenge 3: Centralized vs. distributed mechanisms of trust** — introduced to question whether a single authoritative trust mechanism can absorb trust signals from a globally distributed supply chain.
- **Challenge 4: Balancing access and control in AST** — introduced to examine how the Authoritative Source of Truth can reconcile competing access-control regimes and the need to protect intellectual property.
- **Challenge 5: Scientific Computing Integrity of digital models** — introduced to carry the integrity concern from extreme-scale scientific computing into engineering model reuse.
- **Challenge 6: Reproducibility and Replicability** — introduced to import the reproducibility crisis from research science into engineering practice.
- **Challenge 7: Practical difficulties in producing products' digital counterparts** — introduced to name the production-side burden of generating models, supporting data, and knowledge alongside the product itself.
- **Challenge 8: Insufficient knowledge in the workforce** — introduced to flag the gap between the skills digital engineering demands and what the existing workforce and training pipelines supply.

Supporting frameworks and reference concepts named in the slice:

- **DoD Digital Engineering Strategy (DES)** — cited as leaning toward centralized standardization and as the origin of the aim to put the correct data into the hands of whoever needs it, for its intended use, at the moment it is required.
- **Authoritative Source of Truth (AST)** — treated as a centralized trust and access mechanism that underwrites model credibility, accuracy, reusability, safety, and security.
- **Access-control models** — the source names **MAC** (Bell & LaPadula, 1973), **RBAC** (Sandhu et al., 1996), **ABAC** (Servos & Osborn, 2017), and combinations of these, as the heterogeneous policies AST must interoperate with.
- **Scientific Computing Integrity (SCI)** — attributed to DOE ASCR (Advanced Scientific Computing Research) via Peisert, Cybenko & Jajodia (2015); defined as high confidence that scientific data has an understood process, provenance, and correctness.
- **NSF definitions of reproducibility / replicability / generalizability** (NSF_SBE_AC, 2015) — adopted by the paper as its working vocabulary, with reproducibility framed as same procedures + same data, replicability as same procedures + different data, and generalizability as applicability to different contexts.

## Key Concepts

**Big Data as a double-edged input.** The connected engineering environment pulls data from upstream processes, partners, the lifecycle of the system of interest, prior and similar systems, interacting external systems, the operating environment, the supply chain and manufacturing, and stakeholders. The upside is better quality and lower time and cost; the downside is the burden of processing, managing, mining, analyzing, integrating, and sharing that data and the associated models fast enough to be useful.

**Two ways to standardize.** A centralized scheme fixes one digital representation that the whole community adopts. A distributed evolutionary scheme grows ontologies through fine-grained crowdsourcing — working groups build new ontology parts on top of useful parts borrowed from others, and the most-used parts converge into a de facto standard. The authors note the centralized path is generally more efficient and effective in the current context and near term, but it carries a single point of failure and the risk of committing to a wrong direction over the long run. Standardizing too early in an emerging field can also stifle innovation, and partners abroad may bring incompatible standards of their own.

**Trust has the same centralized/distributed split.** AST is read as a centralized trust mechanism — fast and effective — but modern supply chains are long and complicated, with components arriving from allies and trading partners. Folding distributed trust into a centralized authoritative source is an open problem.

**Access control is a decades-old balancing act.** AST must serve many entities that each run different access-control models and policies. The enduring tension is between "need-to-know" and "need-to-share," now compounded by cybersecurity threats and owners' concerns over intellectual property and competitive position.

**Integrity and provenance of reused models.** Because models and data stream into AST from many entities and get reused downstream, their integrity matters. SCI can be compromised by malicious attacks or by faults in equipment, software, networks, engineers, or workers. Long, complex workflows, supply chains, and provenance chains make guaranteeing integrity extremely hard.

**Reproducibility imported from science.** The paper anchors its concern with a research-world crisis — a Nature collection on irreproducible research, a retraction by a Nobel laureate over reproducibility, and a survey in which more than seventy percent of researchers reported failing to reproduce another scientist's experiments. Engineering adds its own twist: techniques, skills, and tacit know-how live in human teams and can be lost.

**Digital counterparts as a production burden.** Enterprises must now ship not just the product and its conventional documentation but also its models, the data backing those models, and associated knowledge. That raises the bar on credibility, repeatability, interpretability, interoperability, IP protection, security, cost, and workforce readiness.

**Workforce gap.** The knowledge and skills digital engineering requires exceed those of the traditional workforce and traditional education and training, making it hard to retrain a large, professionally diverse population through on-the-job training and academic programs.

## Mental Models

**The centralization dial.** Three separate challenges (standardization, trust, and to a degree access control) are the same dial set in different domains: turn toward centralization for near-term speed and efficiency; turn toward distribution to hedge against single points of failure and long-run misdirection. The authors' meta-point is that diversity must be preserved through evolution — a principle they draw equally from biological populations and technological approaches.

**Data flows in, integrity flows downstream.** Models and data enter AST and are reused later, so any integrity defect introduced early propagates forward. Provenance is the chain you have to trust, and the longer and more cross-organizational it gets, the weaker that trust becomes.

**The reproducibility ladder.** Reproducibility (same procedures, same data) → replicability (same procedures, different data) → generalizability (results hold in different contexts). Each rung is harder than the last, and engineering loses a rung's worth of stability whenever tacit human know-how disappears.

**Product plus shadow.** Every deliverable now casts a digital shadow — its models, data, and knowledge — and the shadow has to meet its own quality, security, and IP standards alongside the physical or software artifact.

## Key Takeaways

- The barrier to digital engineering is plural: eight distinct, named challenges, several of them organizational rather than technical.
- A single tension — centralized vs. distributed — recurs across standardization, trust, and access control; centralization wins on near-term efficiency but concentrates risk.
- AST is the load-bearing construct for both trust and access, and it inherits hard problems: distributed supply-chain trust, heterogeneous access-control policies, IP protection, and the need-to-know vs. need-to-share balance.
- Integrity (SCI) and reproducibility are imported, evidence-backed concerns — the reproducibility crisis in science is offered as a direct warning to engineering, sharpened by the loss of tacit human knowledge.
- Producing high-quality digital counterparts and growing a capable workforce are first-order practical obstacles, not afterthoughts.
- Beyond the eight, the authors leave open research questions on enterprise culture, human-machine interaction, team collaboration, transparency-driven trust, and new risk categories.

## Connects To

- **Authoritative Source of Truth and the DoD Digital Engineering Strategy** — Challenges 3 and 4 build directly on the AST and DES constructs that the pack's earlier material on digital engineering goals introduces.
- **MBSE and shared-model practice** — the standardization, integrity, and digital-counterpart challenges all assume models are the primary shared artifact, linking to model-based systems engineering canon (see the SEBoK knowledge base on MBSE and traceability).
- **Access-control literature** — MAC, RBAC, and ABAC connect this chapter to security engineering foundations (cf. the NIST systems-security-engineering pack on protecting models and data).
- **Scientific computing and provenance** — SCI (DOE ASCR) ties the chapter to data-integrity and provenance concerns that recur in any digital-thread discussion.
- **Open research agenda** — the closing questions on culture, human-machine interaction, collaboration, transparency, and risk feed forward into the pack's treatment of digital engineering as an evolving research field rather than a settled practice.

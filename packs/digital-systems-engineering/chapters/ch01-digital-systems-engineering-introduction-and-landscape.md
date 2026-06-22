# Chapter — Introduction and the Digital Engineering Landscape

> Source caveat: this chapter is grounded only in the openly available arXiv preprint of the paper (Section 1, "Introduction"), not the paywalled journal version. The paper is short (~28 pp), so this pack stays deliberately thin and does not over-claim beyond what the introduction supports.

## Core Idea

Engineering is undergoing a broad digital transformation, and a new field is crystallizing at the intersection of that transformation and systems engineering: **digital systems engineering**. The paper frames this field as the body of knowledge and technology needed to support digital engineering practice. The motivation is concrete: traditional engineering and acquisition methods struggle with complex modern systems because the work flows linearly, leans heavily on documents, and traps information in disconnected silos, which makes systems slow to change and hard to sustain when the operational environment shifts quickly and unpredictably. The introduction positions digital systems engineering as the converging research response to those pain points — an effort to fold digital technologies into systems engineering so practice can keep pace with a rapidly digitalizing world.

## Frameworks Introduced (exact source names, when/how)

- **Digital Engineering Strategy (DES)** — attributed to the US Department of Defense (US DoD, 2018). The introduction names it as the DoD's launched response to the problems of traditional engineering and acquisition. Its stated aim is to build a digital enterprise and quickly absorb technological innovation by digitally representing the system of interest, and by developing, using, integrating, and curating formal models that span organizational boundaries and lifecycle activities. The chapter later in the paper (Section 2) is dedicated to the goals of this strategy.
- **Authoritative Source of Truth** — introduced as a named element of the DES: a central platform and repository that serves as the shared point for collaborating, communicating, and exchanging data and models.
- **Digital Engineering (the broader movement)** — described as the digital transformation of engineering, emerging worldwide under several labels. The source explicitly ties these labels together: **Industry 4.0** (GTAI, 2014), and **digital manufacturing / smart manufacturing** (White House, 2012, 2018), among others.
- **The Fourth Paradigm (data-intensive science)** — credited to Jim Gray's vision, as captured in Hey, Tansley, & Tolle (2009). It is presented as the fourth scientific paradigm following the empirical, theoretical, and computational paradigms, and is invoked to motivate why data (observations of a system) can yield insight that theory alone cannot.
- **Cyber-Physical-Social Smart Systems (CPS3)** — named (Huang, Seck, & Gheorghe, 2016) as the class of innovative systems the Internet of Things is enabling.

## Key Concepts

- **Why traditional engineering falls short.** The introduction lists the specific failure modes that digital engineering is meant to fix: a linear engineering process applied to complex systems, document-heavy and stove-piped information flow, and the resulting difficulty of changing and sustaining systems in volatile, uncertain operating environments.
- **The shifting landscape of engineering systems.** The fast growth of the **Internet of Things (IoT)** (Atzori, Iera, & Morabito, 2010; IEEE, 2015) is reshaping how systems are conceived and operated. The source highlights **Industrial IoT (IIoT)** and industrial smart cyber-physical systems as the path toward the fourth industrial revolution (Schwab, 2017), shorthanded as Industry 4.0.
- **Lifecycle traceability via digital technology.** Combining IoT with Big Data, AI, and Machine Learning makes it possible to trace a system's "fingerprints" or "footprints" — the running changes in its status, components, and behavior — across the entire lifecycle. The same approach lets the operating environment be observed, recorded, and mined to inform design, testing, manufacturing, operations, maintenance, support, reuse, recycling, and risk analysis, in service of trustworthy and resilient systems.
- **Digital transformation as the wider context.** The paper defines digital transformation as the pervasive spread of digital technologies through engineering, business, and many societal processes, touching nearly every part of human activity. Digital engineering is cast as that transformation expressing itself specifically in the field of engineering.
- **The enabling-technology stack.** The introduction names a broad set of technologies that digital engineering draws on. Among them: smart cyber-physical systems and IoT; the data-and-learning trio of big data, AI, and ML; robotics; the immersive pair of augmented reality (AR) and virtual reality (VR); the **digital twin** (Glaessgen & Stargel, 2012; Tao et al., 2018); additive/3D printing; and digital-trust mechanisms including blockchain (Nakamoto, 2008; among others). Digital manufacturing is offered as a striking example of digital engineering in action.
- **Data-intensive thinking.** Under the data-intensive paradigm, the core activities become capturing data, curating it, discovering knowledge from it, and publishing it. The argument is that a theory is only an abstraction of what is already known and is therefore inherently limited, whereas fresh observations of a system can open new understanding and even seed new theory. This vision is credited with inspiring data-intensive research across science and engineering and with driving the rise of Data Science (NIST, 2015).

## Mental Models

- **Model-based over document-based.** The DES vision the introduction quotes pushes toward an integrated, digital, model-based approach in place of document-centric workflows. The mental shift is from documents-as-artifacts to formal models as the shared, living representation of the system.
- **Single source of truth as the hub.** Treat the Authoritative Source of Truth as the central spoke through which collaboration, communication, and data/model sharing pass, rather than letting truth scatter across stove-piped tools and teams.
- **Theory has limits; data extends them.** The fourth-paradigm framing is a mental model for when to lean on observation: because theory only abstracts known knowledge, the observations a digitally instrumented system produces are a route to new insight and potential breakthroughs.
- **The system leaves a digital trail.** Picture every system as continuously emitting fingerprints across its lifecycle — captured through IoT and mined with AI/ML — so that design and sustainment decisions can draw on the real behavior of the system and its environment, not just on up-front assumptions.

## Key Takeaways

- Digital systems engineering is the emerging field that brings digital technologies into systems engineering to support digital engineering practice; this paper is an exploration of that area.
- The DoD's Digital Engineering Strategy (US DoD, 2018) is the anchoring driver in the introduction, built on formal models spanning boundaries and lifecycle, and on an Authoritative Source of Truth as the central repository.
- The shift is away from linear, document-heavy, siloed processes and toward an integrated, digital, model-based approach.
- IoT, Big Data, AI, and ML enable lifecycle-wide traceability of both the system and its environment, supporting trustworthiness and resilience.
- The paper's roadmap (per the introduction): Section 2 covers DES goals, Section 3 the challenges, Section 4 enabling technologies, Section 5 the framework of digital systems engineering plus core concepts across four levels (vision, strategy, action, and foundation with enabling technologies), and Section 6 the conclusion and further research.

## Connects To

- **The DES goals chapter (Section 2 of the source):** this introduction sets up the strategy whose goals are unpacked next.
- **The challenges chapter (Section 3):** the failure modes named here (linear, document-intensive, stove-piped) preview the obstacles to achieving DES goals.
- **The enabling-technologies chapter (Section 4):** the named stack — IoT, big data, AI/ML, digital twin, blockchain, VR/AR, 3D printing — is the input to that discussion.
- **The digital-systems-engineering framework chapter (Section 5):** the four-level structure (vision, strategy, action, foundation) and the small set of core concepts are introduced here only by forward reference.
- **MBSE and SE-canon packs (e.g. the SEBoK pack):** the model-based, single-source-of-truth themes connect directly to established systems-engineering practice on models, lifecycle processes, and traceability.

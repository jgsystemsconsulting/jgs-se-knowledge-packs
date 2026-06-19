# Chapter 6: Task Section 200 — Analysis Tasks

## Core Idea
The 200-series tasks are the analytical engine of MIL-STD-882E. They progress from early, broad-scope hazard listing (Task 201 PHL) through progressively more detailed analyses at concept (Task 202 PHA), requirements (Task 203 SRHA), subsystem (Task 204 SSHA), system-integration (Task 205 SHA), and operational (Task 206 O&SHA) levels, with specialised analyses for health (Task 207 HHA), functional failure (Task 208 FHA), system-of-systems emergence (Task 209 SoSHA), and environmental impact (Task 210 EHA). Results flow into the HTS at every stage.

## Frameworks Introduced

- **Task 201 — Preliminary Hazard List (PHL)**: earliest hazard identification; compiles a list of potential hazards from legacy/similar system data shortly after materiel solution analysis begins.
  - When to use: at programme start, before engineering design begins; establishes initial hazard scope.

- **Task 202 — Preliminary Hazard Analysis (PHA)**: first formal risk assessment; assigns initial RACs to PHL hazards using best available data; identifies potential mitigation measures using the design order of precedence.
  - When to use: during concept/technology development; output feeds SSPP and early design decisions.

- **Task 203 — System Requirements Hazard Analysis (SRHA)**: identifies applicable design requirements to eliminate hazards or reduce risks; flows these requirements into system specifications, hardware/software specs, and test plans; assesses compliance at design reviews.
  - When to use: spans all life-cycle phases and modes; begins at requirements definition and continues through CDR and beyond.

- **Task 204 — Subsystem Hazard Analysis (SSHA)**: verifies subsystem compliance with requirements; identifies previously unidentified hazards at the component level; considers human as a component; covers COTS/GOTS/NDI/GFE; includes software contribution when software is developed separately.
  - When to use: during detailed design and development, typically at Engineering and Manufacturing Development (EMD) phase.

- **Task 205 — System Hazard Analysis (SHA)**: analyses hazards at the integrated system level, including all subsystem interfaces and software/human interfaces; examines independent, dependent, and simultaneous events; evaluates common cause failures and degradation scenarios.
  - When to use: begins during EMD after SSHA outputs are available; updated following design changes.

- **Task 206 — Operating and Support Hazard Analysis (O&SHA)**: examines hazards introduced by operational and support activities and procedures, including maintenance, storage, transport, and disposal; begins during EMD; treats the human as an element of the total system.
  - When to use: when operational and support procedures are defined enough for analysis; typically mid-to-late EMD through Operations and Support.

- **Task 207 — Health Hazard Analysis (HHA)**: evaluates human health hazards from chemical, physical, biological, ergonomic, and radiation (ionising and non-ionising) stressors; includes HAZMAT evaluation, ergonomics evaluation, and operational environment characterisation.
  - When to use: whenever the system involves materials, emissions, noise, vibration, or radiation with potential health consequences to operators or maintainers.

- **Task 208 — Functional Hazard Analysis (FHA)**: identifies and classifies system functions and the safety consequences of functional failure or malfunction; identifies SCFs, SCIs, SRFs, and SRIs; maps functions to hardware, software, and human interface design architecture; assigns SCC and SwCI to SSSFs.
  - When to use: as early as possible in the SE process; the upstream trigger for software system safety (Section 4.4); best performed before subsystem design is fixed.

- **Task 209 — System-of-Systems Hazard Analysis (SoSHA)**: identifies unique SoS hazards that emerge from interactions between constituent systems; provides traceability to SoS architecture locations, interfaces, data, and stakeholders; verifies and validates recommended mitigations.
  - When to use: whenever the system operates as part of a SoS; required re-evaluation of legacy system SCCs at SoS functional and physical interfaces.

- **Task 210 — Environmental Hazard Analysis (EHA)**: identifies and manages environmental hazards across the full life-cycle; supports NEPA and EO 12114 requirements; integrates environmental hazards into the SE process as early as possible.
  - When to use: programmes with environmental impact potential (HAZMAT, noise, emissions, pollutants, demilitarisation and disposal); start as early as possible because early design decisions have greatest environmental leverage.

## Key Concepts

- **Analysis hierarchy**: PHL → PHA → SRHA → SSHA → SHA → O&SHA is the logical progression; each stage builds on the previous without replacing it.
- **Human as a system component**: Tasks 204, 205, 206, and 209 explicitly require that humans be analysed as components within the system or SoS, receiving inputs and initiating outputs.
- **COTS/GOTS/NDI/GFE inclusion**: every analysis task explicitly includes COTS, GOTS, NDI, and GFE hardware and software as items to be analysed; inherited items do not inherit safety.
- **Software integration across analysis tasks**: each analysis task (SSHA, SHA, O&SHA, FHA) requires the contractor to monitor and incorporate software development outputs at each phase when software is developed separately.
- **FHA as the software safety trigger**: Task 208 is the mechanism by which SCFs, SCIs, SRFs, SRIs, and SSSFs are formally identified and SCC/SwCI assignments are made; it feeds directly into Task 102/103 SSPP/HMP software sections.
- **HTS as central repository**: all analysis results are captured in the HTS; analysis reports reference the HTS rather than stand-alone documents where applicable.
- **Health hazard stressor categories**: chemical (toxicity, flammability, carcinogenicity), physical (acoustical energy, vibration, acceleration, blast, thermal), biological (bacteria, viruses, fungi, mould), ergonomic (non-neutral postures, load-bearing stress, repetitive motion, cognitive demands), non-ionising radiation (RF/laser), ionising radiation.

## Mental Models

- **"PHA sets the floor, SHA sets the ceiling"** — the PHA establishes initial risk baselines that carry forward; the SHA at the integrated system level is where those baselines are confirmed, updated, or new interface-emergent hazards are discovered.
- **"FHA first, SSHA/SHA second"** — the FHA identifies what functions are safety-significant and how they are allocated to hardware/software/human; without FHA outputs, SSHA and SHA analyses are missing their safety requirements context.
- **"O&SHA is the operator's advocate"** — while design analyses (SSHA, SHA) focus on the system, the O&SHA explicitly examines what happens when humans interact with the system in real operational and maintenance contexts, including human error pathways.

## Anti-patterns

- **Treating PHA as a one-time deliverable**: the PHA must be updated as design evolves; it is a living assessment, not a gate document.
- **Omitting software from subsystem and system hazard analyses**: Tasks 204 and 205 explicitly require software to be included, even when developed by separate contractors; coordination with the software team and PM is mandatory when software hazard mitigations require action from the software developer.
- **Starting the EHA late**: Task 210 notes that early design decisions made without environmental consideration may result in impacts that "cannot be easily designed out"; cost of mitigation rises steeply after detailed design is frozen.

## Key Takeaways

1. The 200-series analysis tasks form a progressive hierarchy from concept to operations; each task is selectively applicable to programme phases (see Appendix A Table A-I).
2. The FHA (Task 208) is the critical gateway between system-level hazard analysis and software system safety — it must be initiated as early as possible to enable software architecture decisions.
3. Every analysis task explicitly includes COTS, GOTS, NDI, and GFE; the "not-invented-here" items do not inherit safety compliance from their source programmes.
4. The SoSHA (Task 209) specifically targets emergent hazards that arise from system interactions, not from any constituent system alone — it fills a gap that single-system analyses cannot address.
5. HHA (Task 207) covers a broad stressor landscape; its ergonomics and operational environment sub-sections are often under-resourced in hardware-focused programmes.
6. All analysis task results populate the HTS and feed directly into the evaluation tasks (Task 300 SAR/HMAR) and verification tasks (Task 401).

## Connects To

- **Chapter 4 (Software Safety)**: FHA (Task 208) provides the SCC/SwCI inputs that drive the SSCM and LOR task requirements in Section 4.4.
- **Chapter 5 (Task 100 Management)**: analysis results feed HTS records maintained under Tasks 101 and 106.
- **Chapter 7 (Task 300 Evaluation)**: SAR and HMAR aggregate analysis results to provide programme-level hazard status summaries.
- **FMECA (MIL-STD-1629)**: complementary analysis technique often used within SSHA and SHA to characterise component failure modes.
- **Fault Tree Analysis (FTA)**: top-down deductive technique referenced as an analytical tool within MIL-STD-882E analysis tasks; widely used for SHA and software safety analyses.

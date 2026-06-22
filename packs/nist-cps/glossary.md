# NIST CPS Framework Glossary

Key terms from the NIST Framework for Cyber-Physical Systems (SP 1500-201/202/203), alphabetical, with chapter references. Definitions are synthesized in original wording, not reproduced from the source.

**Accurate Time Interval (Accurate TI)** — a deterministic TI whose timescale is traceable to an international standard (UTC or TAI); use where spatial extent or regulation demands a globally referenced clock. (Ch 6)

**Activity / Artifact** — a generic unit of engineering work inside a facet, and the concrete technical output it produces; activities may be tailored into per-aspect groups. (Ch 2)

**Adaptor** — a standard interface inserted into a data flow so that everything upstream becomes interoperable per a canonical model; sited for maximum effect at least cost. (Ch 5)

**Allan Variance family (AVAR/MVAR/TVAR; ADEV/MDEV/TDEV)** — clock-stability measures computed from a time-error sequence as functions of observation interval; the modified forms separate noise types AVAR cannot. (Ch 8)

**Archival vs. real-time data** — data recording past observations for later use versus data that steers the environment and has only limited temporal validity (it can expire in transit). (Ch 5)

**Aspect** — a grouping of conceptually related stakeholder concerns; the Framework defines nine (functional, business, human, trustworthiness, timing, data, boundaries, composition, lifecycle). (Ch 2)

**Assurance case** — the set of assurance judgments (claims, evidence, argumentation, estimate of confidence) showing a realized CPS satisfies its model. (Ch 2, Ch 3)

**Bounded Time Interval (Bounded TI)** — a timing constraint that stays under a stated maximum (sometimes above a minimum); the weakest TI class, for deadline-driven behavior. (Ch 6)

**Canonical data model** — a shared common model that disparate semantic models map to, cutting required transformations from roughly n(n−1) toward n. (Ch 5)

**Co-design** — considering hardware and software (or physical, analog, and cyber elements) jointly so cyber/physical trade-offs are informed; allocating requirements across element types for an optimal cost/benefit/risk balance. (Ch 1, Ch 4)

**Composition of concerns** — when several concerns apply at once, the combined requirement is the set union of the properties each demands; commutative and associative. (Ch 2)

**Concern** — an interest in the system mattering to one or more stakeholders; the fundamental driver of the methodology. Concerns are not orthogonal. (Ch 2)

**CPS (cyber-physical system)** — a smart system of interacting physical and computational components that senses, computes, and actuates under timing constraints, joining the IT and OT worlds. (Ch 1)

**CPS Framework** — the central artifact: a shared vocabulary, a structure (domains/facets/aspects/concerns), and an analysis methodology for studying, designing, and evolving CPS. (Ch 1, Ch 2)

**CPS Network Manager (CNM) / Centralized User Configuration (CUC)** — the node that manages and monitors per-node state across time domains and computes transmission schedules and gate events guaranteeing bounded latency. (Ch 6, Ch 8)

**CPS Time Domain** — a logical grouping of CPS nodes and bridges sharing a timing master and a primary (locally synchronized) timescale; the master must avoid time discontinuities during time-sensitive transfer. (Ch 6)

**Cross-property risk management** — the integrated successor to siloed security: reasoning about safety, security, privacy, reliability, and resilience together across the lifecycle. (Ch 4)

**Data interoperability** — the degree to which systems can exchange data *and* interpret it; scoped to three dimensions — syntactical, semantic, contextual. (Ch 5)

**Data slip** — loss or repetition of a data block when a network element's receive and internal clocks differ enough to overflow/underflow a buffer; sized by MTIE. (Ch 8)

**Deterministic Time Interval (Deterministic TI)** — a TI held within a stated error of an application target on a system-local timescale; for repeatable precise timing relative to the system's own clock. (Ch 6)

**Digital Object (DO) Architecture / ITU-T X.1255** — an integration foundation representing metadata and other information as digital entities with persistent identifiers; the Handle system manages original and derived data. (Ch 5)

**Emergent behavior** — behavior arising from the interaction of many subsystems that no single subsystem exhibits; can be detrimental (a traffic jam) or desirable (a balanced smart grid). (Ch 1)

**Epoch / rate** — a timescale's time-zero origin and the speed at which time advances (the definition of the second, realized via cesium energy levels). (Ch 6, Ch 8)

**Facet** — an engineering view bundling activities and artifacts; the three are conceptualization, realization, and assurance. (Ch 2)

**Fog computing** — moving computation to where the data lives (rather than data to the cloud) to meet latency or trust constraints. (Ch 5)

**Free composability** — the ability to combine components into systems dynamically, even modifying the architecture at runtime; timing composability is the hard case. (Ch 1)

**GNSS jamming vs. spoofing** — denial of the navigation signal by radiated energy versus injection of counterfeit/recorded signals; spoofing is more dangerous because it yields confident, wrong time. (Ch 6, Ch 8)

**Holdover** — riding through a brief loss of a global time source on a strong monotonic local clock (e.g., a high-stability rubidium oscillator) rather than introducing a time discontinuity. (Ch 6, Ch 8)

**Information-Centric Networking (ICN)** — an architecture routing uniquely named, self-securing data by name rather than by address, with native in-network caching. (Ch 5)

**Integrity monitoring (of time)** — guarding a time reference via three elements — time-to-alarm, integrity risk, and alarm limit — paired with the detect/alarm/fail-over triad. (Ch 8)

**Maximum Time Interval Error (MTIE)** — the largest peak-to-peak phase deviation of a clock from its reference over any window of a given length; directly sizes buffers and predicts slips. (Ch 8)

**On-time marker + accompanying data** — the physical signal that marks *when* time is correct, separate from the date/time-of-day carried as noise-tolerant data. (Ch 6)

**Orphaned device / orphaned code / throwaway system** — a device no firm supports, unused code still resident, or a disposable system left in place past its lifespan; each a standing risk that can be co-opted. (Ch 4)

**Primitive (simple) requirement** — a generalized atomic requirement statement mapped to a use-case step and a requirement category; seeded from EPRI IntelliGrid and broadened for CPS. (Ch 7)

**Property** — a concrete assertion addressing a concern (requirement, design element, test, or judgment); spans the whole lifecycle and is the unit of work. (Ch 2)

**Reciprocity assumption** — in two-way time transfer, the assumption that path delay is equal in each direction; its breakdown (asymmetry) is the root of most timing error and the most dangerous spoofing. (Ch 8)

**Reliability vs. resilience** — reliability handles *risk* (known outcome distributions, fault tolerance); resilience handles *uncertainty* (unknown distributions, threat tolerance). (Ch 4)

**Risk budget** — a common resource every trustworthiness property can draw on (not a fixed per-property share); cyber components tend to consume the largest share. (Ch 4)

**Scale / level** — a measuring dimension (spatial, temporal, quantitative, analytical) along which data is examined, and a single unit of analysis sitting on that scale. (Ch 5)

**Semantic / syntactical / contextual interoperability** — agreeing on meaning, on structure/format, and on the business rules for use; the three data-interoperability dimensions. (Ch 5)

**System of systems (SoS)** — a CPS spanning multiple purposes and time/data domains; forces translation or accommodation between domains. (Ch 1)

**Temporal determinism** — identical or near-identical timing behavior given identical input, identical initial state, and no external interference; distinct from functional determinism. (Ch 6)

**Time-correctness by design** — specifying timing as a hardware-independent abstraction so tooling can verify (or generate) an implementation that survives hardware/software upgrades. (Ch 6)

**Time interval (TI)** — the elapsed time between two instants on one common timescale; CPS timing requirements are expressed as bounds on TIs between significant events. (Ch 6)

**Time-triggered architecture** — a controller initiating a fixed, periodic sense–compute–actuate cycle, with inter-node communication scheduled against a common timescale. (Ch 6)

**Trust chain to actuation** — trusted actuation depends on trusted decisions, on trusted analytics, on trusted data; a break anywhere upstream propagates to the physical world. (Ch 5)

**Trustworthiness** — the demonstrable likelihood a system performs its designed behavior under any conditions, evidenced by safety, security, privacy, reliability, and resilience. (Ch 1, Ch 4)

**Type A / Type B uncertainty** — statistical (jitter/PDV) versus deterministic-bias (path asymmetry) uncertainty, per the BIPM method; Type B cannot be revealed by measurement spread alone. (Ch 6)

**Use case (CPS Example vs. specific use case)** — a multi-system/multi-actor scenario summary versus a single-actor/single-system interaction with step-level requirements. (Ch 7)

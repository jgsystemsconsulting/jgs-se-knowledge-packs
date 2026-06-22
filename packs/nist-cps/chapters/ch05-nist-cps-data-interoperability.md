# Chapter — Data Interoperability in Cyber-Physical Systems

## Core Idea

Data interoperability is the degree to which systems and devices can both exchange data and actually interpret it. The report's starting premise is that an exchange only delivers value if the receiving side understands what arrived, so the work centers on *how far* a recipient can understand the data rather than on whether the bits merely moved. This is treated as a subset of the larger interoperability problem — physical connectivity and protocol compatibility matter too — but Section 3 of Volume 2 deliberately narrows to the data dimensions: syntactical, semantic, and contextual.

The CPS angle sharpens the stakes. A CPS is described as a set of cooperating computational elements that observe and steer physical things, so understanding the data passed among independent computing elements is at least as important here as in any other data-management domain — because misunderstood data can drive a wrong actuation in the physical world. The report separates two broad classes of CPS-relevant data: archival data, which records past observations for later use, and real-time data, which controls the environment and has only limited temporal validity. The traffic-light state is given as the canonical real-time example: a value that was valid when placed in a queue may already be invalid when it is taken out, because the progression of time can invalidate it.

A recurring structural idea is that data crosses *boundaries* — ownership boundaries, scales, and levels. A *scale*, in the report's terms, is a measuring dimension — spatial, temporal, quantitative, or analytical — along which data is examined; a *level* is one unit of analysis sitting on such a scale (for the temporal scale, levels are timeframes tied to rates, durations, or frequencies). Because each domain naturally defines its own semantics and exchange protocols, both humans and machines struggle once data moves across these domain and ownership boundaries. The stated goal of the data aspect is to supply a sound description and standards base that simplifies understanding cross-domain data interactions.

## Frameworks Introduced (exact source names, when/how)

The report is explicit that it cites references as *exemplary rather than prescriptive*, and that it samples standards to illustrate the scope of problems rather than to mandate solutions. The following are named in the slice, with the role each plays:

- **Three dimensions of data interoperability — syntactical, semantic, contextual** (Section 3.1.1). Syntactical interoperability fixes the structure and format so bits and bytes move without altering meaning, ensuring exchanges are interpretable at the individual field level. Semantic interoperability adds a shared, common interpretation so authorized parties can actually use the exchanged information independent of the syntax that carried it. Contextual interoperability layers on business rules — validation, authorization, and the where/when/how/why of the receiver's intended use.

- **Canonical data models and adaptors** (Section 3.1.2). A set of common canonical models mapped to disparate semantic models is offered as the way to cut integration cost. The key quantitative claim: canonical models reduce the number of required transformations from roughly n(n−1) down to n, because pairwise bilateral mappings otherwise explode as systems are added. Adaptors are standard interfaces inserted at any point in the data flow so that everything upstream becomes interoperable per the canonical model; they should be sited for maximum effect at minimum cost.

- **Recommendation ITU-T X.1255** (approved September 2013; Sections 3.2.1.1 and 3.2.2). Defines a digital entity data model giving a uniform way to represent metadata records — and other information — as digital entities, with the identifier acting as a single point of reference. Cited as a comprehensive data-integration foundation alongside the **Digital Object (DO) Architecture**.

- **Digital Object (DO) Architecture** (Section 3.2.2). Paired with X.1255 as an architectural foundation letting mobile programs, applications, services, and devices exchange information about the location and provenance of data; its **Handle system** is named as a place to manage original and derived data as related objects.

- **OPC Unified Architecture (OPC UA)** (Section 3.2.1.2). A federation protocol; SCADA systems using OPC UA are given as the example of combining data into a common structured dataset reachable via web services.

- **ISO/IEC/IEEE P21451-1-4, also called Sensei-IoT** (Section 3.2.1.3). A common transport language with built-in security, expressing data in XML via IoT extensions (XEPs) to **XMPP**, securing transport with **TLS**, and using trust engagement (every device registered before participating). Described as among the first Semantic Web 3.0 standards aimed at IoT complexity.

- **RDF, OWL, and SPARQL** (Section 3.2.2.2). The linked-data stack: RDF and OWL as languages for describing data and metadata, SPARQL as the protocol and query language for merging (via endpoints) and querying. Noted as already used to integrate industrial data in electric power, oil drilling, and manufacturing shop floors.

- **Information-Centric Networking (ICN), via the IETF/IRTF ICNRG working group** (Section 3.2.2.2). Proposes uniquely named data as a core principle: data routed by name rather than address, self-securing through signing at creation, with native in-network caching.

- **Fair Information Practice Principles (FIPPs)** and **privacy engineering** (Section 3.2.4.2). FIPPs are positioned as the baseline input to a broader privacy-engineering methodology that NIST is exploring to build privacy-preserving controls directly into systems rather than relying on paper policy. **OAuth, OpenID Connect, and User-Managed Access (UMA)**, plus **Personal Data Stores (PDS)**, are named as mechanisms for explicit user control over information release.

- **The data/information/semantic model distinction** (Section 3.2.5.1), drawn from an Ed Barkmeyer presentation to the Ontolog Forum (2007) and RFC 3444. Data models relate data to data (structure and type); information models relate things to things and to information about them (for human comprehension); semantic models (often ontologies) are information models meant for machine "comprehension" and reasoning. **UML** (software-engineering/data-modeling lineage) and **OWL** (AI/knowledge-representation lineage) are contrasted as complementary, not rival.

- **NISO three metadata types — structural, descriptive, administrative** (Section 3.2.5.3), with rights-management and preservation metadata called out as administrative subsets. Bagley's 1968 coinage of "metadata" as data about data anchors the discussion.

- **ISO data-quality stack** (Section 3.2.8): ISO/IEC 2382-1 (information vs. data definitions), ISO 9000 (quality as conformance to requirements), ISO 8000 (quality data = references a syntax, is semantically explicit, meets stated requirements — hence portable), ISO 22745-30 and 22745-40 (stating and exchanging requirements via an open technical dictionary), and ISO 8000-120 (provenance required at the data-element level, identifying the providing organization plus extraction date/time).

- **Four data-service patterns** (Section 3.2.9): request-reply in two flavors — service-oriented (strongly typed, presented via **WSDL**/**SOAP**) and data/resource-oriented (navigable, CRUD-style, presented via **REST**); unidirectional/event-driven signals; and publish-subscribe (with a broker either as a separate middleman or built into each publishing node).

- **ANSI C12.19** (Section 3.2.13). A North American automated-meter-reading standard whose "Event Logger" function chains secure hashes and timestamped event records so any device state can be re-created by replaying the logged changes in order — the report's worked example of configuration assurance via data interoperability.

> Caveat honored per pack instructions: this slice contains permission-licensed third-party figures (notably the chemical-plant network topology used by permission of chemicalprocessing.com, and other vendor/standards-body diagrams such as the data-fusion, double-blind, and common-data-services illustrations). Those figures are not reproduced or depended upon here; their content is conveyed in prose drawn from the surrounding text. Consistent with the pack instructions, the two externally licensed figures of the Beecham/ETSI type are dropped, and this material is bundled as one pack alongside the rest of the Volume 1/2 content.

## Key Concepts

- **Data fusion has no single definition — and that is itself a hazard.** The report surveys several authoritative definitions, each shaped by its author's domain: the DoD Joint Directors of Laboratories workshop (multi-level association and correlation of single- and multi-source data for refined position, identity, and threat assessment); Hall and Llinas (combining multiple sources for improved accuracy and more specific inferences than any single source); Bizer, Heath, and Berners-Lee (integrating multiple representations of the same real-world object into one clean representation); and Castanedo's three categories — data association, state estimation, and decision fusion. The takeaway is that the diversity of definitions complicates design for engineers who must choose one.

- **The air-traffic-control fusion example.** A radar reports bearing and slant range relative to its known antenna position (the primary return), while an aircraft's IFF transponder sends altitude together with an identification code as a secondary return; the display system continuously merges primary and secondary data to keep aircraft safely separated. It grounds the fusion concept in a safety-critical CPS that combines two sensor types.

- **Identification is weak today and must scale enormously.** Many systems offer no identity beyond a tag name; IP and MAC addresses are insufficient to positively establish device type, owner, operator, or trustworthiness. The report states that solutions must scale to trillions of devices, and notes emerging approaches — QR-code identifiers, IPv6/6LoWPAN unique identifiers — that remain years from widespread, large-scale use because of backhaul and protocol-diversity problems.

- **Coupling follows role.** In manufacturing, controller-to-actuator relationships are tightly coupled with tightly constrained read/write access; the same control system may expose measurement data to outside clients in a loosely coupled relationship. Coupling tightness is thus a function of the parties' respective roles in the CPS.

- **The hierarchical plant problem.** Manufacturing networks are layered, with the lowest layers specialized for production functions; that equipment has a long lifecycle, is expensive to take offline, and is rarely replaced, leaving a diverse mix of types, eras, and technologies. Raw data must flow upward to the enterprise network, and the challenge is doing so without harming determinism, availability, security, and robustness.

- **Actors, roles, permissions (governance of interaction).** For data-driven interaction between dependent and independent CPS, the report defines four actor categories (Data Managers; Operations Staff; Governance, Risk, and Compliance staff; and devices/subsystems acting on behalf of personnel), the roles each holds, and an enumerated permission set (define/initiate/monitor interaction points; view/modify data; create workflows; import/export data). A non-modifiable, non-deletable audit trail is required so that any failure or compromise can be reconstructed.

- **The shipping-container worked example.** Securing the millions of containers entering US ports is presented end-to-end — RFID item/pallet tags, GPS tracking, tamper-reporting digital seals, gas-chromatograph/mass-spectrometer screening, and central repositories that alarm on deviation — and is explicitly broken into smaller, independently useful phases rather than attempted as one "boil the ocean" project. It also shows compliance with named programs (CSI, C-TPAT, and related CBP standards).

- **Privacy is structurally hard in pervasive CPS.** Data are produced in greater volume from more sources, storage is moving to third-party clouds through chains of brokers and aggregators, and data leakage is a side effect of collection (appliance data revealing whether someone is home). The report notes the irony that imposing access controls can *decrease* privacy by stockpiling authenticating information across more administrators. The advanced utility grid (synchrophasors, heat and vibration sensors) is the privacy example, where a user can barely locate every collection point that tracks them.

- **Privacy-by-derivation and metadata minimization.** Releasing a derived claim rather than a raw value limits disclosure — proving "over 17" instead of a full birth date — and even the metadata should minimize ("a valid DMV asserted it," not "the Virginia DMV asserted it") to avoid unnecessary leakage. Cryptographic profiles with zero-knowledge assertions and double/triple-blind schemes aim for anonymity, unlinkability, and unobservability, though the report stresses the required cryptography is not yet in common use and the broker in such schemes is both powerful and a prime attack target.

- **Identifiers: unique, persistent, resolvable — and not brittle.** A digital entity referenced outside its local domain needs a unique identifier that resolves to current state (location, access conditions) while the identifier itself stays constant. Baking changeable attributes (location, ownership) into the identifier string makes it brittle and tempts unjustifiable assumptions. Two classes are distinguished: traceable/navigable identifiers, and untraceable ones such as UUIDs used when anonymity is needed. "Same entity?" is always answered relative to *same for what purpose*.

- **Volume and velocity reshape the problem.** High volume forces policies on whether/where to store, when to expire, and how to migrate data, and a separation between the registries that describe data and the physical repositories that hold it. Bandwidth mismatches force transformation (transcoding, sub-sampling, aggregation, compression), after which derived data must stay linked to its origin and carry forward the original's policies; attribute-based encryption (ABE) is offered as a way to embed access policy in the data so movement alone does not defeat control. Velocity (time-sensitive or control-loop data) drives **Fog computing** — moving functions to the data rather than data to the cloud — and motivates Time-Sensitive Networking (TSN) and Time-Coordinated Computing (TCC) to manage end-to-end timing.

- **Timestamps are a discipline, not an afterthought.** The report enumerates issues: oscillator short-term stability and the size/weight/power/cost trade-off of better clocks, quantization error, deterministic offset from stable-but-inaccurate oscillators, traceability to a common reference timescale (UTC or TAI) for cross-node correlation, accounting for missing data, and reconciling differing timestamp formats and clock granularities (e.g., 40 MHz vs. 250 MHz). It then lists the parameters a timestamp should carry — nominal data rate, a missing-data indicator, sufficient significant digits, stochastic and deterministic uncertainty, traceability accuracy and reference scale, a format-resolution formalism, and possibly a validity/expiration period.

- **Security framed as confidentiality, integrity, availability — with a CPS twist.** Confidentiality needs protection at rest and in transit (encryption only as strong as algorithm, key exchange, and key storage). Integrity needs authentication, authorization, and cryptographic integrity checks (digital signatures), because ordinary CRC/checksum/hash methods only catch accidental errors — an attacker can simply recompute them. Availability is singled out as the priority for control-systems engineers (an unavailable system during chemical mixing or power events can cause physical harm), in contrast to IT engineers who tend to weight confidentiality and integrity first.

- **Trust chains to actuation.** Because the physical world is actuated from data, trusted actuation depends on trusted decisions, which depend on trusted analytics, which depend on trusted data — and data interoperability is meaningless if data are not transmitted, used, and stored securely.

## Mental Models

- **The three-layer interoperability ladder.** Picture syntactic → semantic → contextual as rungs: move the bytes intact, agree on what they mean, then agree on the rules for using them. Physical connectivity sits below the bottom rung. Climbing higher reduces the complexity and risk of the exchange.

- **The n vs. n(n−1) hub.** Without a canonical model, every pair of systems needs its own bilateral translator and the count grows quadratically; insert a shared canonical model and translators collapse to one per system. This is the spoke-and-hub argument for why canonical models and well-placed adaptors pay off.

- **Adaptor as a "make-interoperable" valve in the pipe.** A standard interface dropped into the data flow renders everything upstream interoperable per the canonical model. Place these valves where they buy the most interoperability for the least cost.

- **Data as a first-class, named, self-securing entity.** Stop treating data as a second-class thing reachable only by "secure the server, then guard access to the server." Instead give the datum a persistent identifier and (in the ICN view) sign it at creation so it routes by name and secures itself — decoupling identity and trust from location and channel.

- **Keep the data still, move the computation.** When data is too big, too fast, or legally immovable, ship the analytics (as executables) to where the data lives. Fog computing is the architectural expression of this inversion, useful for both latency and trust-sensitive data such as certain healthcare records.

- **Metadata is a role, not a kind.** Whether a value is "data" or "metadata" depends on its relationship to other data and can flip across the lifecycle — a sensor's make/model is metadata to a control app but data to an asset-management app. Model metadata as a relationship, and remember access rights are themselves metadata.

- **The double-blind broker as a single point of power.** In privacy-preserving identity schemes, the broker that sits between identity provider and relying party can see everything unless cryptography prevents it — so picture it simultaneously as the privacy guarantor and the highest-value attack target, and design accordingly.

- **Trust as a chain that ends in the physical world.** Read backward from the actuator: every physical action rests on a decision, on analytics, on data, on the device that produced it. A break anywhere upstream propagates to a possibly dangerous physical outcome.

## Anti-patterns

- **Clean-slate solutions that ignore legacy.** The report states plainly that legacy CPS have to be accommodated in any interoperability scenario, and it calls clean-slate designs that disregard that legacy unacceptable. Redesigning applications onto a new semantic model is often infeasible.

- **Baking changeable attributes into identifiers.** Encoding location or ownership into the identifier string itself yields a brittle identifier and invites both people and software to assume things about the entity that may be unwarranted; changeable attributes belong in the resolved record, not the name.

- **Favoring one modeling approach as universally best.** The report warns against comparing modeling approaches and preferring one in general; doing so ignores legacy systems and the fact that different situations and viewpoints need different approaches (UML and OWL each fit their own community).

- **Treating data entities as second-class.** A paradigm that hardens the server and then gates access to it — while leaving the data itself without continuous, credentialed identity — is named as the root of many data-sharing and management challenges; PKI credentialing that cannot interoperate across trust domains is a specific weakness.

- **Relying on non-cryptographic integrity checks against attackers.** CRC, checksums, and plain hashes protect only against accidental modification; an attacker can recompute them after tampering, which is why cryptographic signatures are required.

- **Relying solely on user management (or paper policy) for privacy.** Individuals are not always positioned to mitigate every privacy risk, so approaches must include controls that do not depend solely on user management, engineered into executable systems rather than left to manual policy.

## Key Takeaways

- Data interoperability is about *understanding*, not just transport; the report scopes it to three data dimensions — syntactical, semantic, contextual — atop the physical connectivity that enables movement.
- CPS data splits into archival and real-time, and real-time data can expire in transit, so timing validity is intrinsic to correctness.
- Canonical models plus strategically placed adaptors are the report's headline complexity-reduction tactic, cutting transformations from n(n−1) toward n and rendering upstream data interoperable.
- Identity and meaning are reached by mutual agreement — there is no global authority — so the technical community must solve them while balancing communication cost, safety risk, security needs, and interface versioning.
- Standards are sampled as exemplary, not prescriptive: X.1255 and the DO Architecture for comprehensive integration; OPC UA, Sensei-IoT/P21451-1-4, RDF/OWL/SPARQL, and ICN for federation, semantics, and naming.
- Governance of dependent/independent CPS interaction requires unambiguous definitions of actors, roles, and permissions, anchored by immutable audit trails.
- Privacy must be engineered in (FIPPs as baseline, OAuth/OIDC/UMA, PDS, zero-knowledge and blind schemes), with derivation and metadata minimization limiting disclosure — but the needed cryptography is acknowledged as not yet common.
- Volume and velocity force transformation-with-lineage, policy-bound data (e.g., ABE), and moving computation to data (Fog), while timestamps demand explicit, traceable, uncertainty-bearing parameters.
- Security reduces to confidentiality/integrity/availability, with availability prioritized in control systems, and the whole trust chain terminating in physical actuation — making secure data a precondition for meaningful interoperability.
- Configuration and safety assurance rely on verifiable software hashes and immutable, replayable change logs (the ANSI C12.19 Event Logger pattern).

## Connects To

- **Chapter 1 / Volume 1 (the CPS Framework and SoS)** — the SoS composability introduced there reappears here as the boundary-crossing problem: when data leaves a CPS interface, new SoS behaviors can emerge, and the quality of interface handling (sender identity, data identity/integrity, time sensitivity, semantics, authorization) is the test of whether a CPS can join an SoS.
- **Timing and Synchronization** — the timestamp parameters, UTC/TAI traceability, and TSN/TCC efforts in Section 3.2.7 and 3.2.12 are the data-side counterpart to the Framework's treatment of timing as a first-class architectural concern.
- **Cybersecurity and Privacy aspect** — Sections 3.2.4 and 3.2.11 carry the trustworthiness concern into data terms: confidentiality/integrity/availability, authentication/authorization, signatures, and privacy engineering.
- **The Assurance Facet (NIST SP 1500-201)** — explicitly cross-referenced in Section 3.2.13, where assurance cases and configuration verification depend on data interoperability mechanisms such as secure hashes and event logs.
- **Provenance and data quality (ISO 8000 family)** — links interoperability to whether data can be trusted and reused, requiring element-level provenance and concept dictionaries.
- **A future CPS Framework User's Guide** — named as the place where more specific best-practice procedures (e.g., which component types to protect in which CPS) should eventually live, signaling that this report is foundational rather than exhaustive.

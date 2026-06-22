# Chapter — Related Standards and Applying the Framework (Emergency Response Use Case)

## Core Idea

The CPS Framework does not stand alone. Volume 1 closes by situating the
Framework inside a crowded landscape of architecture, IoT, timing, and security
standards efforts, and then by walking a single end-to-end example — an
emergency-response dispatch scenario — through the three facets to show the
mechanics of analysis in motion. The two halves answer two different questions.
The standards survey answers "how does this Framework relate to everything else
that touches cyber-physical and IoT systems?" The worked use case answers "what
does it actually look like to pick up the Framework and use it on a real
problem?" Critically, the use case is deliberately constrained: the authors warn
that the narrow scope sacrifices real insight into emergency response in exchange
for a clear demonstration of method. The point is to teach the Framework's
moving parts, not to design a dispatch system. The chapter therefore reads as a
bridge between the abstract meta-model and concrete practice, with the explicit
caveat that what follows is a "shallow" pass, not a complete analysis.

## Frameworks Introduced (exact source names, when/how)

The standards survey (Section 2.5) names related efforts and explains where each
sits relative to CPS. It is presented as a partial list of relevant standards,
organizations, and working groups — not an exhaustive map.

- **IoT Architectural Reference Model (IoT ARM)** — produced by the European
  Lighthouse Integrated Project "Internet of Things – Architecture" (IoT-A)
  across 2010 to 2013. Introduced top-down architectural principles and design
  guidelines, with the aim of a shared language that lets vertical domain "silos"
  interoperate. The survey stresses that IoT-A deliberately scopes itself apart
  from CPS: in its terminology, cyber-physical systems are treated as the IoT
  devices and IoT resources beneath the service layers, and architecting those
  devices is out of the IoT ARM's scope.
- **IEEE P2413 working group** — formed in 2014 to advance cross-domain
  interaction, system interoperability, and functional compatibility in IoT. It
  defines an IoT architectural framework with shared abstractions and vocabulary,
  and emphasizes a blueprint for data abstraction plus a four-part quality set
  spanning protection, security, privacy, and safety.
- A shared-traits note ties IoT ARM and IEEE P2413 together: both conform to the
  **ISO/IEC/IEEE 42010** architecture-description standard, both draw functional
  inspiration from the **OSI reference model**, and both explicitly treat
  architecture divergence as a major concern. The survey frames finding the
  similarities and differences between IoT-scoped work and CPS as a task that
  helps readers tell the two apart and build CPS-specific architectures that can
  still be compatible with IoT services.
- **OneM2M** — positioned as an interoperability enabler spanning the whole CPS,
  M2M, and IoT ecosystem. It develops technical specifications and reports for a
  common IoT service layer realizable through an embedded API, so devices in the
  field can connect to application servers regardless of the sector or industry
  solution already in place.
- **Cybersecurity Research Alliance (CSRA)** — an industry-led non-profit
  consortium driving cybersecurity R&D strategy through government–industry–
  academia partnership.
- **CPS Voluntary Organization** (supported by the National Science Foundation) —
  an online venue for collaboration among CPS professionals across academia,
  government, and industry.
- **NITRD CPS Senior Steering Committee** — coordinates programs, budgets, and
  policy recommendations for federal CPS research and development, including
  joint program planning and strategy across member agencies.
- **NIST Privacy Engineering** — guidance aimed at reducing privacy risk and
  helping organizations make deliberate decisions about controls in information
  systems; the survey flags that it targets government-agency privacy practice
  and may not suffice for the private sector.
- A cluster of **timing and time-sensitive-networking standards** is introduced
  under the theme of making time integral to networks: **IEEE 802.1** (its Time
  Sensitive Networking, or TSN, task group, enabling determinism in wired LANs
  through synchronized clocks), **IEEE 1588** (the Precision Time Protocol, PTP),
  **IEEE 802.11** (Timing Measurement and Fine Timing Measurement protocols for
  WiFi synchronization), the **IETF** (planning to extend the IEEE building
  blocks to routable wide-area networks), the **ITU-T** (which applied 1588 work
  to telecom networks), and the **IETF 6TISCH** task group with **RFC 7554** (a
  time-slotted model over IEEE 802.15.4 for low-power personal-area networks).
- **AVnu Alliance** — builds an interoperable ecosystem for precise-timing,
  low-latency applications using open standards such as TSN, and runs
  interoperability tests and certification for products needing bounded latency,
  reserved bandwidth, and synchronized time.
- **Industrial Internet Consortium (IIC)** — assembles organizations and
  technologies to accelerate the Industrial Internet through best practices,
  testbeds, reference architecture and frameworks, standards influence, and
  shared security approaches.
- **National Security Telecommunications Advisory Committee (NSTAC)** — convenes
  industry chief executives to advise the President on assuring vital
  telecommunications through any crisis and maintaining a resilient national
  communications posture.
- **The Open Group Open Platform 3.0 / IoT Work Group** — IoT standards intended
  to do for connected things what HTML/HTTP did for the web, so equipment can be
  monitored and integrated across its lifecycle for safety, maintenance, and
  energy efficiency gains.

The worked example (Appendix C) then exercises the **CPS Framework itself** — its
three facets (conceptualization, realization, assurance), its facet activities,
and its aspects-and-concerns structure — as the framework under application.

> Note on figures: per the pack's licensing caveat, the two third-party figures
> in the source that were reproduced under permission (the Beecham and ETSI
> illustrations) are intentionally omitted here. Only NIST's own framework content
> is carried forward, consistent with the pack's public-domain basis.

## Key Concepts

**Scoping CPS against IoT.** The recurring move in the survey is boundary-drawing.
IoT-A and IEEE P2413 are architecture frameworks for IoT that treat CPS as the
device-and-resource substrate underneath their service layers. The Framework's
value, in this framing, is to let an engineer build a CPS-specific architecture
that remains compatible with IoT services rather than being subsumed by them.

**Time as a first-class network property.** A large share of the survey is devoted
to standards that make synchronized, deterministic timing a built-in capability
of networks — wired (IEEE 802.1 TSN, IEEE 1588 PTP), wireless (IEEE 802.11
timing-measurement protocols, IEEE 802.15.4 / 6TISCH), and wide-area (IETF and
ITU-T extensions). This foreshadows why the use case treats timing as one of its
core aspects.

**Tailoring before analysis.** The use case begins by deciding what kind of
analysis to run. Using the Framework's own tailoring guidance, the team selected
a **waterfall** process, a **shallow** depth, and a **system-of-systems** scope
(Table 8). It then marked the relevant application domains (Table 9): cities,
consumer, emergency response, infrastructure, and transportation. Tailoring is an
explicit, recorded decision, not an implicit default.

**Facet-by-facet activity selection.** Each facet is pared down to only the
activities the exercise needs. Conceptualization kept three activities — Mission
and Business Case Development, Functional Decomposition, and Requirements
Analysis (Table 10). Realization kept a single activity, Design, and even that
was limited to resolving two properties surfaced during conceptualization (Table
11). Assurance kept two — Identify Assurance Objectives and Define Assurance
Strategy (Table 12). The aspects were likewise trimmed: Functional, Human,
Trustworthiness, Timing, Data, Boundaries, and Composition were kept in; Business
and Lifecycle were largely profiled out (Table 13).

**Properties as the unit of work.** The conceptualization facet's artifact is the
CPS Model, expressed as a set of properties. The exercise tags each with a
mnemonic — a business case property, a use-case property, an assumptions
property, a success-metric property — and carries them forward. The injured-person
scenario is decomposed into systems (smart phone, E-911 with dispatch, ambulance
with smart GPS, traffic control system, GPS system) and a step-by-step
data-exchange table (Table 14) capturing who sends what to whom across the cell
and enterprise networks.

**Requirements as an aspect/concern grid.** Requirements analysis (Table 15) is
organized by walking every retained aspect against its subsidiary concerns and
recording the properties that fall out of each cell. Functional concerns yield
actuation, communication, controllability, sensing, and performance properties.
Trustworthiness yields privacy, resilience, safety, and security properties —
including a combined-reliability target (for example, 95% confidence the
ambulance arrives in time), failover to a second ambulance, tamper protection,
and message-integrity validation. Timing yields a logical event ordering, latency
bounds (text delivered in under ten seconds, enterprise-network latency under one
second), and a common UTC time scale. Cells with nothing to record are marked
`N/A`.

**Design/test pairs in realization.** Realization (Tables 16) produced two
example design-and-test pairs, one for the functional/performance property
("ambulance arrives within target time") and one for the composition/adaptability
property ("work with different cell phone technologies"). Each design carries a
hypothetical test plan with numbered test IDs and pass thresholds — for instance,
verifying SMS propagation under ten seconds over a thousand messages, GPS
acquisition under sixty seconds, and a roughly six-minute target response time
built from a chain of per-step timing budgets.

**Assurance as argued judgment.** Assurance (Section C.8) returns to the two
fully-exercised properties and treats their assurance as the objective. The
strategy reuses the realization design and test artifacts and frames a leaf-level
argument: successful execution of the test, traced back through the design to the
property, is taken as sufficient grounds to conclude the property is met. The
source writes this as a leaf assurance function relating the property, its design,
and its test.

## Mental Models

**The Framework as a meta-model you instantiate.** Volume 1's summary calls the
CPS Framework an abstract framework or meta-model for understanding and deriving
domain-specific CPS architectures. The right mental model is a template you
specialize: start from the full Domains/Facets/Activities/Aspects/Concerns
structure, then tailor it down to the slice your problem needs before you analyze
anything.

**The three-facet pipeline.** Properties are discovered and modeled in
conceptualization, implemented and deployed in realization, and verified and
validated in assurance. A property's lifecycle is the through-line: the same
"ambulance arrives within target time" property is born as a requirement, given a
design and a test, and finally argued to be assured. Watching one property travel
all three facets is the cleanest way to internalize how they connect.

**Aspect-by-concern sweep as a checklist generator.** Rather than brainstorming
requirements freely, the grid forces a disciplined sweep: every retained aspect ×
every concern is a cell that either holds a property or is explicitly `N/A`.
Empty cells are a deliberate record that the question was asked and found
irrelevant — not that it was forgotten.

**Shallow-by-design.** The exercise is an honest demonstration, not a finished
analysis. The authors repeatedly signal the limits: scope was constrained, depth
is shallow, only two properties were carried through all three facets, and
several aspects were profiled out. The mental model is "minimum viable pass to
show the mechanics," which is itself a legitimate, named use of the Framework.

## Key Takeaways

- The CPS Framework is positioned as complementary to, and scope-distinct from,
  major IoT architecture efforts (IoT ARM, IEEE P2413, OneM2M) and from a broad
  ecosystem of timing, security, and industrial-internet standards.
- IoT frameworks generally treat CPS as the device-and-resource layer beneath
  their services; the Framework's job is to let engineers architect that layer in
  a way that still interoperates with IoT.
- Deterministic, synchronized time is a heavily standardized concern (IEEE 802.1
  TSN, IEEE 1588 PTP, IEEE 802.11, 6TISCH/RFC 7554), which is why timing is a
  core aspect of CPS analysis.
- Applying the Framework starts with explicit tailoring decisions: process type,
  analysis depth, scope, relevant domains, and which facet activities, aspects,
  and concerns to keep.
- Conceptualization produces a CPS Model expressed as properties, derived by
  sweeping each aspect against its concerns; realization attaches designs and
  tests to selected properties; assurance argues that passing those tests, traced
  to the design, justifies concluding the property is met.
- The emergency-response example is intentionally shallow — it demonstrates
  method, and only two properties are carried fully through all three facets — so
  its conclusions about dispatch are illustrative, not authoritative.

## Connects To

- **The three facets and aspects/concerns model** introduced earlier in Volume 1:
  this chapter is the applied counterpart, instantiating that structure on a
  concrete scenario.
- **Architecture-description practice** via ISO/IEC/IEEE 42010, which both IoT ARM
  and IEEE P2413 conform to and which underpins the Framework's view/viewpoint
  vocabulary.
- **System-of-systems engineering**: the use case is explicitly scoped as a
  system of systems, linking the Framework to SoS analysis where independent
  systems (phone, E-911, ambulance, traffic control, GPS) interoperate toward a
  shared mission.
- **Assurance-case reasoning**: the leaf-argument approach in Section C.8 connects
  to broader assurance-argument and verification-and-validation practice, where
  evidence is traced to claims.
- **Timing and synchronization engineering**: the survey's timing standards and
  the use case's latency and common-time-scale requirements connect to precision-
  timing and time-sensitive-networking work elsewhere in the CPS body of
  knowledge.

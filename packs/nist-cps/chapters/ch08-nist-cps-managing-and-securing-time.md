# Chapter — Managing and Securing Time: Networks, Resilience, and Requirements

## Core Idea

Volume 3 of the CPS Framework — the Timing Annex (NIST SP 1500-203) — takes the
timing aspect that earlier volumes named as a core CPS concern and turns it into
working engineering material. It supplements the Timing subgroup report in Volume
2, which was produced by Subgroup 4 (Timing and Synchronization) together with the
NIST-led TAACCS group (Time Aware Applications, Computers and Communications
Systems). The annex moves through four linked ideas. First, it lays a metrological
foundation: what a clock signal actually is, how clock error is modeled, and how
clock quality is measured. Second, it shows how networks and operating systems are
made *time-aware* so that synchronized, bounded-latency behavior can be engineered
rather than hoped for. Third — and this is the center of gravity — it makes the
case that time is a security target in its own right, catalogs how time can be
compromised (jamming, spoofing, network attacks) and defended, and surveys backup
sources for when the dominant source, GNSS, fails. Fourth, it grounds all of this
in a table of real CPS timing requirements spanning the critical-infrastructure
sectors. The throughline is that in a cyber-physical system, an instant in time
is not free infrastructure you can assume — it is a measured, distributed,
attackable quantity that has to be designed for, monitored, and recovered.

## Frameworks Introduced (exact source names, when/how)

The annex names a substantial set of standards, organizations, and metrics. They
fall into three groups: time-aware networking standards, security extensions, and
backup/alternative time sources.

**Standards that make networks time-aware (Section 2.1).** The annex lists these
as the standards (and standards suites) relevant to building time-awareness into
networks:

- **IEEE 1588** — a layered architecture for propagating time that supports clock
  synchronization across heterogeneous networks, including wireless. It specifies
  media-independent options and the mapping onto media-dependent options that live
  in network-specific standards. It is the Precision Time Protocol (PTP).
- **IEEE 802.1AS** — an Ethernet-specific profile of IEEE 1588 that adds
  guarantees on synchronization accuracy. The annex notes that IEEE 802.3bf
  (2011) once supplied the accurate transmit/receive timing indications 802.1AS
  needed, but has since been superseded.
- **IEEE 802.1Q** — provides time-sensitive data-transfer mechanisms that let
  time-sensitive and best-effort traffic share one Ethernet network without
  breaking the bounded-latency guarantees of the time-sensitive streams. It
  includes hardware time-aware scheduling — per-port time-aware gates and
  time-based shapers — that yields the lowest-latency options needed for control
  applications. The annex notes the IEEE 802.1Qbv specification in this context.
- **IEEE 802.1CB** — seamless-redundancy options that raise the reliability of
  Ethernet data transfer.
- **IEEE 802.11-2016** — the Wi-Fi standards family; IEEE 802.11v-2011 adds a
  timing-measurement capability and a mapping function to IEEE 1588, and IEEE
  802.11ak is cited as enabling future time-sensitive stream support over Wi-Fi.
- **ITU-T G.8261 (Y.1361)** — timing and synchronization aspects in packet
  networks.
- **ITU-T G.8262** — timing characteristics of the Synchronous Ethernet equipment
  slave clock (EEC).
- **ITU-T G.8265 (Y.1365)** — architecture and requirements for packet-based
  *frequency* delivery.
- **ITU-T G.8275 (Y.1369)** — architecture and requirements for packet-based
  *time and phase* delivery.

The annex also names supporting bodies: the **Wi-Fi Alliance (WFA)** and **Avnu
Alliance** as consortia testing implementation and interoperability, and the
**IETF Deterministic Networking (DetNet)** working group as the effort to bring
time and time-sensitive transfer into wide-area networks.

**Clock-quality metrics and reference recommendations.** The metrology sections
introduce the standard toolkit for quantifying clock error and stability:

- **ITU-T Rec. G.8260** — cited as the source for how to estimate constant time
  error (the average of an initial run of the time-error sequence), with a linear-
  regression fallback (per Appendix II of ITU-T G.823) when a frequency offset is
  present.
- **Allan Variance (AVAR / ADEV), Modified Allan Variance (MVAR / MDEV), and
  Time Variance (TVAR / TDEV)** — stability measures computed from the time-error
  sequence as functions of the observation interval τ; the deviations are simply
  the square roots of the variances. MVAR/TVAR can separate white and flicker
  phase modulation, which AVAR cannot.
- **Maximum Time Interval Error (MTIE)** — the largest peak-to-peak phase
  deviation between a clock and its reference over any window of a given duration;
  presented as the metric for sizing buffers (the related MRTIE compares two
  clocks when neither is treated as ideal).

**Security extensions and protocols (Section 3.6).** The annex surveys the
state-of-the-art mechanisms for protecting time communication:

- **NTP** with its **Autokey** extension and symmetric-key authentication — guards
  against packet modification and replay and offers endpoint authentication via
  digital certificates. The annex flags Autokey's weaknesses repeatedly (a short
  effective key length, a flawed trusted-certificate scheme) and recommends that
  only symmetric-key authentication be used. The IETF NTP Working Group's revised
  network time security work is noted as in progress.
- **IEEE 1588 Annex K** — an experimental extension providing group source
  authentication, message integrity, and replay protection via a replay counter,
  with trust established by a challenge-response three-way handshake over pre-
  shared keys; the annex catalogs its known gaps (outdated HMAC-SHA1-96, costly
  HMAC-SHA256-128, header fields left uncovered).
- **IPsec** — a Layer-3 suite (transport or tunnel mode) using Authentication
  Header (AH) and Encapsulating Security Payload (ESP); it gives end-to-end
  integrity protection but impacts achievable accuracy.
- **MACsec** — Layer-2 link-level security (IEEE 802.1AE for crypto, IEEE 802.1X
  for session/key management) using a hop-by-hop encrypt/validate-and-re-encrypt
  approach that lets transparent clocks modify packets in transit.

**Backup and alternative time sources (Section 3.3).** Named alternatives to GPS
include other **GNSS constellations** (China's Compass/BeiDou, Russia's GLONASS,
the EU's Galileo); **dedicated wide-area networks** running PTP over OTN or
SONET/SDH; **Synchronous Ethernet (SyncE) with PTP**, including CERN's sub-
nanosecond **White Rabbit** variant whose technology is being folded into a high-
accuracy option of IEEE 1588; NIST's **WWVB** (60 kHz LF) and **WWV/WWVH** (HF)
radio broadcasts, discussed for holdover and Assisted Partial Timing Support
(APTS); and **eLORAN**, a modernized LORAN-C presented as a near-unjammable,
hard-to-spoof terrestrial option.

> Note on figures: per the pack's licensing caveat, third-party figures
> reproduced only under permission are omitted. In this material that includes the
> electric-substation synchronization architecture diagram adapted from Tournier
> et al. (© 2009 IEEE, used with permission); its content is described in text
> here rather than reproduced. The Beecham and ETSI permission-licensed figures
> referenced for the pack as a whole likewise carry forward only as NIST's own
> public-domain prose, not as images.

## Key Concepts

**A clock is a frequency device, and "time" is an artificial construct.** The
annex is explicit that every network element has a clock subsystem built around an
oscillator; the most basic free-run, while better ones discipline a local
oscillator against an external reference and inherit its characteristics. Because
a clock is fundamentally a frequency source, even the best clocks exhibit a random
walk in phase and drift apart from each other without bound. "Time" itself is a
label attached to a counted sequence of pulses relative to a chosen origin —
meaning time of day must be *transferred* from a standard, and accuracy as a
wall-clock means traceability to UTC or TAI. The SI second is defined via cesium
energy levels and realized by the BIPM; UTC is discontinuous because of leap
seconds (kept within 0.9 s of astronomical UT1), and any real-time UTC/TAI signal
is only a prediction since both are post-processed scales.

**The clock-error model: three deterministic terms plus five noise types.** Clock
behavior is modeled as a phase/time-error signal x(t) with a constant offset x0, an
initial frequency offset y0, a linear frequency drift D (common in rubidium
standards and quartz crystals), and a random remainder. That random part is
captured by five power-law noise types — white and flicker phase modulation, white
(random-walk phase) and flicker frequency modulation, and random-walk frequency —
each dominating in a different Fourier-frequency band. This model underpins the
metrics: AVAR/MVAR/TVAR as functions of observation interval τ reveal which noise
process dominates, and the τ-domain variances follow their own power laws.

**Time error, TIE, and why MTIE sizes buffers.** Time error is the deviation of a
real clock's edges from the ideal; time interval error (TIE) measures it over an
interval. A second, more damaging error class than a bit error is a *data slip*:
when a network element's receive clock and internal clock differ, its buffer
overflows or underflows and a whole block of data is lost or repeated. MTIE is the
practical lever here — if MTIE(τ) stays below the buffer size B, overflow/underflow
is avoided over intervals up to τ; equivalently, MTIE(τ) tells you the buffer size
needed to meet a slip specification. Better synchronization means fewer slips.

**Two-way time transfer rests on a reciprocity assumption.** In packet-based
exchange (NTP or PTP), a slave aligns to a master using four timestamps across a
message in each direction. With two equations and three unknowns, the slave can
only solve for its offset by *assuming the delay is equal in both directions*. The
annex enumerates the error sources that break this: actual path asymmetry (which
maps directly into a constant time error and can only be removed if known),
imprecise timestamps (best taken at the physical layer to avoid OS and interrupt
jitter), packet delay variation (PDV) in the network, low update rate (accuracy
improves only as the square root of update rate under white PDV), and instability
of the slave's local clock over the measurement window.

**Time-awareness is a layered problem in networks *and* operating systems.** On
the network side, a Centralized Network Manager (CNM) / Centralized Network
Controller gathers performance metrics — bridge, propagation, and forwarding
delays — computes topology, and generates a transmission schedule with bridge gate
and shaper events so each time-sensitive stream gets guaranteed latency and
reserved queues for zero-congestion loss. Latency is measured empirically by
time-stamping a test stream at each bridge's ingress and egress. On the OS side,
the same determinism problem recurs as a request for accurate time traverses OS
layers: a monolithic main-loop OS makes time trivially accessible but is often too
simple; multi-threaded, microkernel (message-passing), and virtual-machine
architectures add flexibility at the cost of non-deterministic latency through
each layer. The annex notes that accurately accounting for OS-layer residence time
would need very low-latency hardware support not present in current systems, and
that hypervisor-hosted virtual networks would need a virtualized timing protocol
(e.g., emulating a PTP-aware switch) to extend hardware timing into VMs.

**Time is a security surface, attacked at the source and on the wire.** At the
*source*, GNSS is the dominant timing source and is easy to disrupt: its signals
arrive from roughly 20,000 km up and are weak enough that low-cost commercial gear
can jam them, and meaconing/spoofing can feed a receiver a counterfeit signal. The
annex distinguishes *denial* (jamming, or space weather) from *spoofing*: denial
usually just stops synchrophasors, whereas spoofing can drive automated control or
human operators to take harmful actions on false premises. On the *network*, the
annex formalizes a threat vocabulary — unsecured/secured/hybrid networks; internal
vs. external attackers; man-in-the-middle, injector, DoS/DDoS — and lays out
attack primitives (interception, interruption, insertion, modification). Drawing
on Mizrahi's analysis of secured PTP networks, it tabulates external and internal
attacks against secured time networks (packet-delay manipulation, time-protocol
DoS, cryptographic-performance attacks, rogue master, replay/spoofing) with impacts
and candidate countermeasures.

**Defense in depth for time.** Countermeasures span cryptographic hygiene and
architecture. The annex recommends 128–256-bit symmetric keys, AES-based message
authentication (e.g., CMAC), key rotation/freshness and perfect forward secrecy,
authenticating the packet header (not just the time-protocol payload), and
deterministic crypto latency to avoid degrading accuracy. Architecturally it
contrasts hop-by-hop integrity (MACsec — lets transparent clocks update the
correction field) with end-to-end integrity (IPsec — safer but accuracy-limiting),
and proposes scalable key management based on certificate authorities issuing
combined X.509 identity and attribute certificates, with OCSP/stapling and ECDH for
forward secrecy. Because legitimate-but-compromised insiders defeat authentication,
it adds **trusted platform attestation** (building on Trusted Computing Group work),
**network and host intrusion detection systems (NIDS/HIDS)**, a **delay-threshold**
detector for delay manipulation, and **clock-drift correction** that uses time-
series prediction to keep slaves synchronized through a DoS attack.

**Resilience through holdover, integrity monitoring, and source diversity.** When
the source fails, a high-stability extended-holdover oscillator (e.g., a high-
stability rubidium holding one microsecond for about a day) lets a network ride out
a GNSS outage; a redundant grandmaster plus diverse, redundant network paths (ring
protocols such as RSTP, MRP, HSR) preserves synchronization. The annex frames
**integrity monitoring** of the time reference with three elements — time-to-alarm,
integrity risk, and alarm limit — and frames secure-timing mitigation as a triad:
*detect* jamming/spoofing at the affected device, *alarm* the operator, and *fail
over* to an equally precise trusted backup. It notes that anti-jamming products
meeting all three exist commercially today, but civilian anti-spoofing products do
not yet.

**Requirements are sector-specific and span twelve orders of magnitude.** The
closing use-case table makes the diversity concrete: requirements range from
better than one part in 10^11 frequency accuracy for the mobile-communications
evolution from 4G to 5G, through sub-100-ns UTC for emergency-services real-time
communications, to phase/latency targets measured in milliseconds for patient-care
devices, remote surgery, robotics, vehicle-to-vehicle signaling, and smart
buildings. Some listed cases are flagged as still-unsolved timing problems.

## Mental Models

**Time as a measured, attackable supply chain — not free infrastructure.** The
cleanest framing the annex supports is to treat an accurate instant the way you
treat any critical supply: it has a *source* (GNSS or a national lab), a *transfer
path* (the network and OS layers that carry it), a *quality spec* (the AVAR/MTIE
family), *failure modes* (jamming, spoofing, slips, PDV), and a *continuity plan*
(holdover, backups, failover). Every link in that chain can be measured and every
link can be attacked.

**Frequency first, time second.** Because a clock is fundamentally a frequency
device, the model separates aligning *rate* (syntonization, achievable one-way and
requiring only a constant transfer delay) from aligning *time of day*
(synchronization, requiring two-way exchange and the reciprocity assumption).
Holding this distinction explains why SyncE (physical-layer frequency) is deployed
*with* PTP (time/phase) rather than instead of it.

**The reciprocity assumption is the load-bearing wall.** Two-way transfer works
only because you assume equal delay each way. Most network-side timing error and
the most dangerous spoofing attacks are, at root, deliberate or accidental
*asymmetry* — a man-in-the-middle that adds delay in one direction, an unmodeled
path difference. Watching where reciprocity holds and where it breaks is the single
most useful lens for both accuracy engineering and threat analysis.

**Denial vs. spoofing is the security decision boundary.** The annex repeatedly
contrasts the two: denial degrades to a known-safe fallback (manual operation,
holdover), while spoofing is the genuinely dangerous case because it produces
confident, wrong time that drives bad automated action. Designing for "what if the
time is *wrong* rather than *missing*" is the harder, more important problem.

**Tailor the timing requirement to the sector, then to the application.** The
use-case table is a reminder that there is no single CPS timing number. The right
mental move is to locate your application in its sector band — frequency for
telecom, UTC/phase for the grid, bounded latency for medical and vehicular control
— and read the accuracy class (down to nanoseconds, up to a second) from the
application, not from a default.

## Anti-patterns

The source does not present a formally labeled "anti-patterns" list, but it
explicitly names several practices and conditions as unsafe or inadequate, which
function as anti-patterns:

- **Relying on NTP Autokey for authentication.** The annex states Autokey's
  effective key length is only 32 bits (exploitable by the "cookie-snatching"
  attack) and its trusted-certificate scheme is flawed and unusable as a template;
  it concludes only symmetric-key authentication should be used.
- **Using outdated message-authentication algorithms.** IEEE 1588 Annex K's
  HMAC-SHA1-96 is called out as no longer considered safe.
- **Authenticating only the time-protocol payload.** Omitting the source/
  destination header from the authenticated code (as Annex K does) leaves the
  protocol open to MitM-style attacks.
- **Deploying GPS-based synchrophasors in automated control without secure
  timing.** Commercial PMUs/synchrophasors possess none of the three secure-timing
  elements, so using them in automated control puts the grid at risk; a
  demonstrated 10-degree timing walk-off can trip large generators offline.
- **Taking timestamps above the physical layer.** Values not captured at the
  physical layer are corrupted by variable OS and interrupt-handling delay,
  degrading two-way transfer accuracy.
- **Assuming a single timing source is enough.** The annex frames sole reliance on
  vulnerable GPS receivers — without holdover, backups, or path/source diversity —
  as the condition that makes pervasive time loss possible.

## Key Takeaways

- The Timing Annex (NIST SP 1500-203) operationalizes the CPS Framework's timing
  aspect: it supplies the metrology, the time-aware networking and OS picture, the
  security/resilience treatment, and a sector-by-sector requirements table.
- A clock is a frequency device and "time" is an artificial, transferred label;
  even ideal clocks random-walk apart, so traceability to UTC/TAI and active time
  transfer are unavoidable.
- Clock quality is engineered through a standard toolkit — the clock-error model
  (x0, y0, D plus five power-law noises), the AVAR/MVAR/TVAR (ADEV/MDEV/TDEV)
  family, and MTIE, which directly sizes buffers and predicts data slips.
- Networks and operating systems are made time-aware by layered standards
  (IEEE 1588/PTP, 802.1AS, 802.1Q/TSN, 802.1CB, 802.11, ITU-T G.826x/827x) plus
  centralized schedule generation; OS and VM layers add non-determinism that must
  be bounded.
- Time is a first-class security target. GNSS is easy to jam and spoof; spoofing is
  more dangerous than denial because it yields confident wrong time. Network-level
  threats and defenses (NTP, IEEE 1588 Annex K, IPsec, MACsec; NIDS/HIDS, trusted
  platform attestation, delay thresholds, clock-drift correction) are cataloged
  against secured-network threat models.
- Resilience comes from holdover oscillators, integrity monitoring (time-to-alarm,
  integrity risk, alarm limit), the detect/alarm/fail-over triad, source diversity
  (other GNSS, dedicated WANs, SyncE+PTP/White Rabbit, WWVB/WWV, eLORAN), and
  redundant ring topologies.
- CPS timing requirements are sector- and application-specific, spanning from one
  part in 10^11 frequency accuracy down to nanoseconds and up to a second, with
  some use cases still unsolved.

## Connects To

- **The timing aspect and trustworthiness concern of the CPS Framework** (Volumes
  1–2): this annex is the deep-dive companion that turns those named concerns into
  measurable, defendable engineering.
- **Time-sensitive networking and precision-timing standards** introduced in the
  Volume 1 standards survey (IEEE 802.1 TSN, IEEE 1588 PTP, IEEE 802.11 timing
  measurement, IETF DetNet, ITU-T telecom timing): the annex specifies how those
  building blocks are profiled, scheduled, and secured.
- **Critical-infrastructure resilience and the CIKR sectors**: the GPS-anomaly and
  space-weather impact tables, holdover requirements, and the requirements use-case
  table all map timing directly onto the sixteen critical-infrastructure sectors.
- **Cyber-physical security engineering**: the threat-model vocabulary (internal/
  external attackers, MitM, DoS, injector) and defenses (IPsec, MACsec, attestation,
  intrusion detection) connect timing to general network-security and zero-trust
  practice.
- **Metrology and signal analysis**: the clock-error model, power-law noise types,
  and Allan-family variances connect the CPS Framework to the broader frequency-
  and-time metrology body of knowledge maintained by NIST and the BIPM.
- **Power-systems and grid SE**: the synchrophasor/PMU tripping scenario and the
  digital-substation automation case connect timing security to wide-area grid
  monitoring, protection, and SCADA situational awareness.

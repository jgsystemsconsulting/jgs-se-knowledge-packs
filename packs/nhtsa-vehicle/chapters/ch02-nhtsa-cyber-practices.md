# Chapter 2: Cybersecurity Best Practices for Modern Vehicles (2022 Guidance)

> Source: NHTSA Cybersecurity Best Practices for the Safety of Modern Vehicles (Updated 2022, final); extract pages 1–7, 9–12, 15–17, 19–24 (pages 8, 13, 14, and 18 omitted by third-party screen).

## Core Idea

NHTSA's 2022 update is **non-binding, voluntary guidance**. It is not a Federal Motor Vehicle Safety Standard, not a mandate, and not a conformity scheme. Manufacturers and equipment makers are encouraged to review it and decide whether and how to apply the practices to their own systems. The document treats vehicles as cyber-physical systems whose cybersecurity weaknesses can become safety problems, and it frames a risk-based set of organizational and technical practices that industry can maintain as the threat landscape moves.

The 2022 release notes emphasize a readability reorganization, alignment checks against recent industry standards named by title (including ISO/SAE 21434), enumerated recommendations, clearer coverage of the vehicle development lifecycle, and continued expectation that industry self-certifies and self-audits its cybersecurity work. This chapter follows the document's own section structure rather than imposing an external maturity model.

## Purpose, Scope, and Audience

**Purpose.** Update NHTSA's voluntary guidance so organizations building or integrating vehicle electronics and software can strengthen product cybersecurity with a durable, refreshable process base.

**Scope.** Cybersecurity issues for motor vehicles and motor vehicle equipment, including software. The audience is broad: high- and low-volume vehicle and equipment designers, suppliers, manufacturers, modifiers, and alterers. The security of the assembled vehicle is only as strong as the weakest contributor in that chain.

**Relationship to other instruments.** The guidance points readers toward industry resources by name, including ISO/SAE 21434 and Auto-ISAC best-practice material, without turning those instruments into federal requirements inside this document. Detail on those third-party standards belongs outside this pack; see `functional-safety-signpost` for ISO/SAE 21434 orientation and `automotive-signpost` for related UNECE cybersecurity type-approval landscape (for example UNECE R155), without any claim here about what those documents require.

## General Best Practices (document section 4)

The heart of the guidance is a set of enumerated general practices. Themes below match the document's headings.

### Leadership priority on product cybersecurity

Leadership is expected to set corporate cybersecurity priorities and foster a culture that can handle rising vehicle and equipment cyber risk. Emphasis from leadership down through staff signals that cybersecurity risk is managed seriously and helps the organization prioritize cybersecurity work throughout product development.

### General approach and vehicle development process

The document opens its general practices with a layered posture: assume some vehicle systems can be compromised, reduce the chance an attack succeeds, and limit harm when access is gained. It points industry at NIST's Cybersecurity Framework functions (Identify, Protect, Detect, Respond, Recover) as a way to build that layered approach, with risk-based focus on safety-critical vehicle control systems, elimination of risk sources where feasible, field detection and response, designed-in recovery, and industry lesson-sharing (including Auto-ISAC participation).

Under the vehicle-development heading, kept-page practices cover:

- **Sensor vulnerability risks.** Treat manipulation of sensor inputs (not only classical software exploits) as in-scope for modern vehicles, including automated and driver-assistance features that trust perception data.
- **Removal or mitigation of safety-critical risks.** Prefer eliminating or reducing safety-critical cyber risk in design; residual risk should be conscious, not accidental.
- **Protections / layered defenses.** Use layered protections matched to assessed risk so a single failed control does not open the safety-relevant path; communicate clear cybersecurity expectations to suppliers that support those protections.
- **Inventory and management of hardware and software assets.** Know what hardware and software is on each vehicle build, including third-party and open-source components, with enough detail to map newly published vulnerabilities to fielded fleets and to retain a history of version updates over the vehicle life.
- **Cybersecurity testing and vulnerability identification.** Evaluate off-the-shelf and open-source components against known vulnerabilities; run product cybersecurity testing (including penetration testing) with qualified testers separate from the developers; document each vulnerability's disposition.
- **Monitoring, containment, and remediation.** Establish rapid incident detection and remediation that can protect occupants and nearby road users and move the vehicle toward a minimal risk condition when a cyberattack is detected.
- **Data, documentation, and information sharing.** Capture attack-relevant data; document design choices and analyses under version control; share appropriately through Auto-ISAC and comparable mechanisms.
- **Continuous risk monitoring and assessment.** Revisit risk as systems, connectivity, and the threat landscape change after start of production.
- **Industry best practices.** Follow secure software development practice, stay current with named industry and government guidance sources, and take part in automotive standards and Auto-ISAC best-practice work as new risks appear.

### Information sharing

NHTSA recounts the policy push that led industry to stand up Auto-ISAC and continues to treat timely sharing of threat and vulnerability information as a core community practice. Membership is encouraged; non-members are still pointed at sharing pathways rather than hoarding safety-relevant cyber findings.

### Security vulnerability reporting program

Industry members should make it easy for the security research community and the public to report information to them. The guidance calls for each organization to create its own vulnerability reporting policies and mechanisms so those reports can help find cybersecurity weaknesses.

### Organizational incident response process

Detailed incident-response planning text on the screened-out pages is not used here. From kept pages, the same safety outcome is already in the general and development practices: timely detection and rapid response to field cyber incidents, designed-in recovery, rapid detection and remediation capabilities, and transition toward a minimal risk condition when a cyberattack is found, plus collection and industry sharing of attack-relevant information.

### Self-auditing

Industry is encouraged to consider organizational and product cybersecurity audits on an annual cadence. Public versions of audit reports are described as useful for stakeholders and consumers when organizations choose to release them. (Process-management documentation detail that sat only on screened-out pages is omitted.)

## Aftermarket devices and serviceability (document sections 6–7)

**Vehicle manufacturers** should account for consumer-owned and aftermarket devices that connect through the interfaces the manufacturer provides, apply reasonable protections against the risks those devices introduce, and authenticate third-party connections with appropriately limited access.

**Aftermarket device manufacturers** connect into cyber-physical systems that can affect safety of life, across vehicle types with uneven vehicle-side defenses. The guidance tells them to put strong cybersecurity protections on their own products rather than assuming the vehicle will absorb the risk.

**Serviceability.** Vehicles remain on the road for years and need maintenance and repair. Industry should plan for serviceability by owners and third parties, and should provide strong cybersecurity protections that do not unduly block alternative repair channels the owner authorizes. Cybersecurity is not a license to lock out service; serviceability is not a license to weaken cyber controls.

## Technical Best Practices (document section 8)

Section 8 shifts from organizational process to concrete technical expectations. Kept-page themes:

### Developer and debugging access on production devices

Production vehicles should not leave developer or debugging interfaces exposed in ways that let an attacker gain privileged control. Close or tightly control those paths before vehicles leave the factory posture.

### Cryptographic techniques and credentials

Cryptography ages with computing capability. Techniques should stay current and non-obsolescent for the intended application; implementation quality matters as much as algorithm choice. Credentials that grant elevated access to vehicle platforms (passwords, certificates, keys) should be protected from unauthorized disclosure or modification. A credential taken from one vehicle should not unlock other vehicles. For diagnostic access in particular, global symmetric keys and ad-hoc cryptographic techniques should be minimized.

### Vehicle diagnostic functionality

Diagnostic features support repair but can be abused against vehicle systems. Limit diagnostics to the vehicle operating mode that serves the feature's purpose, and design them so misuse outside that purpose has minimal dangerous effect (for example, constraining which brakes can be disabled, at what speed, and for how long).

### Event logs (fleet trend review)

Where logs can be aggregated across vehicles, review them periodically for cyberattack trends. (Subsections on diagnostic tools and vehicle internal communications that sat only on a screened-out page are omitted.)

### Wireless paths into vehicles

Wireless interfaces expand remote attack surface. Practices emphasize:

- Knowing and minimizing wireless attack paths.
- Segmentation and isolation so a compromised wireless domain cannot freely reach safety-critical controllers.
- Closing unnecessary network ports, protocols, and services on production vehicles; limiting services that must remain.
- Hardening communication to back-end servers and avoiding designs that let an attacker rewrite routing rules or pivot from connectivity modules into deeper vehicle networks.

### Software updates and over-the-air updates

Update mechanisms are both a remediation channel and an attack channel. Authenticate and integrity-protect updates; limit firmware rollback or downgrade attacks that reintroduce known weak software; treat cloud and backend components that stage updates as part of the same trust problem. Over-the-air paths need the same care as local update paths, with attention to how an attacker might abuse the pipeline.

## What This Chapter Does Not Do

- It does not quote ISO/SAE 21434, UNECE regulations, or other third-party standards, even where the source footnotes discuss them.
- It does not add a maturity model, capability level, or certification ladder the NHTSA document does not define.
- It does not convert voluntary practices into "shall" regulation language.

For UNECE cybersecurity type-approval context use `automotive-signpost`. For ISO/SAE 21434 orientation use `functional-safety-signpost`. This chapter states only what NHTSA's guidance itself urges.

## Key Takeaways

1. The 2022 document is **voluntary guidance**, not a regulation and not a mandate; application is a manufacturer decision.
2. Leadership priority, a development process that includes cybersecurity, inventory of hardware/software assets, testing, monitoring, sharing, vulnerability intake, incident response, and self-audit form the **organizational** spine.
3. Technical practices stress closing debug paths, current cryptography and per-vehicle credentials, constrained diagnostics, fleet log trend review, segmented wireless architectures, and **authenticated, anti-rollback** software updates including OTA.
4. Auto-ISAC-style **information sharing** and **vulnerability reporting policies/mechanisms** are first-class expectations, not optional extras.
5. Third-party standards named in the source are pointers only; this pack does not reproduce them. Continue at `automotive-signpost` and `functional-safety-signpost`.

## Connects To

- **ch01 (introduction):** pack scope, refusals, and the guidance-vs-regulation boundary.
- **ch03 (ADS vision):** ADS 2.0's separate "Vehicle Cybersecurity" safety element, which points industry at robust product development and sharing without replacing this chapter.
- **`functional-safety-signpost`:** ISO/SAE 21434 and related cybersecurity-engineering standards named but not quoted here.
- **`automotive-signpost`:** UNECE R155 and related automotive regulatory landscape named but not quoted here.
- **FMVSS chapters (ch04, ch06):** vehicle-level performance standards; they do not define cybersecurity process.

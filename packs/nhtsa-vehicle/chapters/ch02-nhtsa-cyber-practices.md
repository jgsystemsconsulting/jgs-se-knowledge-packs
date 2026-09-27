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

Leadership is expected to treat product cybersecurity as an explicit priority, resource it, and set culture so cybersecurity enters design early rather than as a late gate. Without that signal, development teams lack cover to trade schedule or features for safety-relevant cyber work.

### Vehicle development process with explicit cybersecurity considerations

The document expects cybersecurity to be built into the vehicle development process, not bolted on after architecture lock. Practices under this heading (drawn from kept pages) cover:

- **Process and risk assessment.** Define how cybersecurity work runs inside product development; assess risk so safety-critical exposures are visible before release decisions.
- **Sensor vulnerability risks.** Treat manipulation of sensor inputs (not only classical software exploits) as in-scope for modern vehicles, including automated and driver-assistance features that trust perception data.
- **Removal or mitigation of safety-critical risks.** Prefer eliminating or reducing safety-critical cyber risk in design; residual risk should be conscious, not accidental.
- **Protections / layered defenses.** Use layered protections so a single failed control does not open the safety-relevant path.
- **Inventory and management of hardware and software assets.** Know what hardware and software is on each vehicle build, including third-party and open-source components, with enough detail to map newly published vulnerabilities to fielded fleets and to retain a history of version updates over the vehicle life.
- **Cybersecurity testing and vulnerability identification.** Test for vulnerabilities with methods appropriate to the architecture; identify weaknesses before and after integration.
- **Monitoring, containment, and remediation.** Plan how issues found in the field are detected, contained, and fixed.
- **Data, documentation, and information sharing.** Capture attack and incident-relevant data; document analyses; share appropriately through industry channels such as Auto-ISAC and comparable mechanisms.
- **Continuous risk monitoring and assessment.** Revisit risk as systems, connectivity, and the threat landscape change after start of production.
- **Industry best practices.** Stay aligned with evolving industry practice rather than freezing a one-time checklist.

### Information sharing

NHTSA recounts the policy push that led industry to stand up Auto-ISAC and continues to treat timely sharing of threat and vulnerability information as a core community practice. Membership is encouraged; non-members are still pointed at sharing pathways rather than hoarding safety-relevant cyber findings.

### Security vulnerability reporting program

Organizations that design or manufacture vehicle systems are expected to give external researchers a clear, confidential path to report vulnerabilities, with policies that make responsible disclosure workable.

### Organizational incident response process

Not every attack can be predicted. The guidance expects a prepared incident-response capability: roles, communication paths, containment and recovery actions, and reporting of incidents, exploits, and vulnerabilities to Auto-ISAC promptly, with parallel attention to appropriate government reporting channels where applicable. Exercises and readiness checks belong with the process, not only paper plans.

### Self-auditing

The document pushes documented process management and periodic review. Industry is encouraged to run organizational and product cybersecurity audits on a recurring cadence (the text discusses annual consideration). Public-facing summaries of audit posture are described as useful for stakeholders and consumers when organizations choose to release them. The guidance encourages thorough work-product discipline; it does not itself define a third-party certification scheme.

## Who Must Act (document sections 5–7)

**Vehicle manufacturers** carry end-to-end responsibility for the cybersecurity of the vehicle as delivered and supported, including supplier-provided content they integrate.

**Aftermarket device manufacturers** sit on interfaces that touch many vehicle types with uneven vehicle-side defenses. The guidance tells them to put strong cybersecurity protections on their own products rather than assuming the vehicle will absorb the risk.

**Serviceability.** Vehicles remain in service for years. Service channels, dealer tools, and maintenance paths are part of the cybersecurity surface. Convenience of repair must be weighed against opening privileged operations to attackers who reverse engineer service paths.

## Technical Best Practices (document section 8)

Section 8 shifts from organizational process to concrete technical expectations. Kept-page themes:

### Developer and debugging access on production devices

Production vehicles should not leave developer or debugging interfaces exposed in ways that let an attacker gain privileged control. Close or tightly control those paths before vehicles leave the factory posture.

### Cryptographic techniques and credentials

Cryptography ages. Algorithms, key lengths, and credential handling should stay current for the intended lifetime and use case. Prefer designs that avoid global secrets shared across large vehicle populations when public-key approaches fit the problem. Protect keys and credentials in storage and in use.

### Vehicle diagnostic functionality

Diagnostic services are powerful by design. Limit what an unauthenticated or weakly authenticated party can do through diagnostic interfaces, especially operations that reflash software or move actuators.

### Diagnostic tools, internal communications, and event logs

(Tooling and in-vehicle network topics continue across the screened pages; synthesis from adjacent kept content and later subsections.) Treat diagnostic tools as sensitive assets whose credentials and capabilities can be reverse engineered. Internal vehicle messaging that carries control or safety-relevant state needs integrity and authenticity protections appropriate to the harm of spoofed messages. Event logs that support forensics and fleet trend detection should be retained and reviewed so repeated attack patterns surface.

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
3. Technical practices stress closing debug paths, current cryptography, constrained diagnostics, protected internal messaging, segmented wireless architectures, and **authenticated, anti-rollback** software updates including OTA.
4. Auto-ISAC-style **information sharing** and researcher-facing **vulnerability reporting** are first-class expectations, not optional extras.
5. Third-party standards named in the source are pointers only; this pack does not reproduce them. Continue at `automotive-signpost` and `functional-safety-signpost`.

## Connects To

- **ch01 (introduction):** pack scope, refusals, and the guidance-vs-regulation boundary.
- **ch03 (ADS vision):** ADS 2.0's separate "Vehicle Cybersecurity" safety element, which points industry at robust product development and sharing without replacing this chapter.
- **`functional-safety-signpost`:** ISO/SAE 21434 and related cybersecurity-engineering standards named but not quoted here.
- **`automotive-signpost`:** UNECE R155 and related automotive regulatory landscape named but not quoted here.
- **FMVSS chapters (ch04, ch06):** vehicle-level performance standards; they do not define cybersecurity process.

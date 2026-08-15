# Chapter 4: DETECT, RESPOND, and RECOVER Goals

## Core Idea
CPG 2.0 keeps DETECT/RESPOND/RECOVER intentionally tight: detect malicious code and adverse events, communicate and report incidents, and execute recovery plans. These goals assume PROTECT logging/backups and GOVERN IR planning already exist.

## Frameworks Introduced
- **DETECT (4.x)**: Malicious code detection and adverse event identification.
- **RESPOND (5.x)**: Incident communication and reporting procedures.
- **RECOVER (6.x)**: Incident recovery plan execution.

## Key Concepts
- **4.A Establish malicious code detection**: Deploy capabilities that identify malware/hostile code early across relevant IT/OT hosts and paths.
- **4.B Identify adverse events**: Correlate signals so organizations recognize incidents and precursor activity, not only signature hits.
- **5.A Establish incident communication procedures**: Predefine who is told what, when, and how during incidents (internal and external stakeholders).
- **5.B Establish incident reporting procedures**: Include reporting paths to appropriate authorities/partners (CISA and others as applicable) with usable triggers and content expectations.
- **6.A Execute incident recovery plan**: Practice and perform recovery so operations return safely — tied to backup/restore ability under PROTECT (3.O) and IR plans under GOVERN (1.C).

## Mental Models
- Detection without adverse-event analysis produces alert piles, not incidents.
- Response communications are a control equal to technical containment — especially for critical infrastructure public-safety impacts.
- Recovery execution is the proof that backups, topologies, and authorities were real.
- Keep this Function set thin on purpose: CPGs prioritize baseline readiness, not a full SOC maturity model.

## Anti-patterns
- **AV only on IT laptops, nothing on jump hosts or engineering workstations**: Incomplete 4.A coverage for OT-adjacent paths.
- **No playbook for who calls the regulator, customer, or CISA**: 5.A/5.B failures create legal and trust damage.
- **Recovery plan never executed under time pressure**: 6.A is about execution ability, not document presence.
- **Detect tools without log retention (3.Q)**: Investigations die immediately.

## Key Takeaways
1. DETECT goals focus on malware detection and recognizing adverse events.
2. RESPOND goals emphasize communication and reporting procedures, not deep forensic method.
3. RECOVER centers on executing the recovery plan successfully.
4. These goals lean on GOVERN IR plans and PROTECT logging/backups.
5. Critical infrastructure entities should pre-stage external reporting contacts and templates.
6. Thin goal counts here are intentional prioritization, not a claim that advanced detection is unnecessary later.

## Connects To
- **ch02**: IR plans (1.C) and topology (2.E) that response needs.
- **ch03**: Logging (3.Q) and backups (3.O) enabling detect/recover.
- **ch05**: Sector/OT communication constraints during response.
- **nist-800-61**: Deeper IR life-cycle and CSF Community Profile guidance.

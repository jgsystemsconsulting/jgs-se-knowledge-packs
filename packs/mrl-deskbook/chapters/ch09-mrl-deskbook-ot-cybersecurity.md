# Chapter: Operational Technology Cybersecurity in MRL Assessments

## Core Idea

Appendix D adds operational-technology cybersecurity screening to manufacturing assessments. Shop-floor networks and equipment are attack surfaces. Software-borne disruption can halt operations or degrade product quality without obvious detection. Version 2025 therefore folds OT protection questions into the MRL thread structure. This chapter is screening guidance inside a manufacturing assessment. It is not a deep cybersecurity audit method.

## Frameworks Introduced

### OT versus neighboring technology classes

Operational technology covers programmable systems and devices that sense or change the physical world: industrial control, building management, fire control, physical access mechanisms, numerical control machines, automated inspection gear, and related sensors. The deskbook points readers to NIST SP 800-37 for the formal OT definition. Name that publication. Do not rebuild its text here.

OT is distinct from:

- General information technology
- Platform information technology or mission data environments
- Enterprise management information systems

OT assets often sit outside the tightest IT department control and outside ordinary IT audit scope. That is why manufacturing assessments must ask about them explicitly.

### Scope inside MRL work

The MRL Working Group placed cybersecurity criteria across multiple threads in the matrix. The manufacturing-assessment scope stays limited to OT protections. It does not expand the MRL Assessment into a full enterprise cyber certification exercise such as a complete Cybersecurity Maturity Model Certification campaign.

### Screening posture

Manufacturing subject-matter experts ask fundamental questions:

- Has the organization considered OT cybersecurity for manufacturing systems?
- Are basic, common-sense controls present?
- Where are major gaps or risks in OT protection?

Experts are not expected to perform highly technical cyber evaluations unaided. When discussion turns deeply technical, pull in a cybersecurity specialist. Top-level controls that a manufacturing SME can recognize still belong in the assessment conversation.

### Federal and non-federal system notes

Deskbook discussion distinguishes environments that meet federal system criteria from non-federal manufacturing environments. Screening still seeks policy, procedure, training, and education signals, plus practical control evidence on the floor. Classification of the system boundary changes who owns which policy set. It does not remove the need to ask whether OT is protected.

## Key Concepts

- **Screening, not audit.** Goal is major-gap detection for manufacturing risk, not certification.
- **Thread integration.** OT cybersecurity appears inside manufacturing management and related thread structure rather than as a free-floating cyber chapter detached from producibility.
- **SME boundary.** Manufacturing assessors handle common-sense control questions; cyber specialists handle deep technical follow-up.
- **Quality and disruption link.** OT compromise is a manufacturing risk because it can stop lines or corrupt process quality.

## Mental Models

**Physical-world computers.** If the box drives a machine, sensor, or access mechanism on the floor, treat it as OT until proven otherwise.

**Ask early, escalate late.** Start with presence of policy, training, basic segmentation and access discipline, and incident awareness. Escalate to specialists when answers require packet-level or control-system forensics skill.

**Manufacturing residual risk.** Record OT gaps the same way other thread gaps feed MMPs and decision reviews.

## Key Takeaways

- Version 2025 includes OT cybersecurity screening inside MRL Assessments.
- Scope is operational technology on the manufacturing floor, not a full IT or mission-cyber audit.
- Manufacturing SMEs ask basic control and gap questions; specialists join when needed.
- NIST SP 800-37 is named for the OT definition; its text is not quoted here.
- Findings feed ordinary manufacturing risk and maturation handling.

## Connects To

- `ch02-mrl-deskbook-scale-threads-and-trl.md` hosts Manufacturing Management and related thread structure where OT criteria appear.
- `ch04-mrl-deskbook-conducting-assessments.md` is when screening questions get asked on site.
- `ch05-mrl-deskbook-maturation-plans-and-risk.md` absorbs OT gaps that need mitigation.
- `ch08-mrl-deskbook-adapting-criteria.md` may change intensity of OT questions by environment.

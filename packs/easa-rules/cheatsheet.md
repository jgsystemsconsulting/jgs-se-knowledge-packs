# Cheatsheet: easa-rules

Decision rules for EASA airborne software and AEH means-of-compliance questions. Each rule names the chapter that owns the detail; the paywalled industry standards are named only, and `avionics-signpost` carries the designations and purchase points.

## Which document governs my question? → ch01

Decision tree:

- Software means of compliance → AMC 20-115D: scope and replacement ch02, assurance framing and legacy paths ch03, tool pointer and GM practices ch04.
- AEH means of compliance → AMC 20-152A: scope and DAL bounds ch05, the added objectives ch06.
- Multi-core → AMC 20-193, name-only pointer; not covered in this release.
- Both sides at once (joint planning seam) → ch07.
- An FAA question goes to `faa-8110-49`, not this pack.
- A DO or ED clause question is designation only: `avionics-signpost` names the standard.
- Neither AMC is mandatory law: AltMoC exists with equivalent safety and EASA approval on a product or ETSO article basis. (ch01, ch02, ch05)
- Which decision issued which AMC: ED Decision 2017/020/R (Amendment 14) carries AMC 20-115D; ED Decision 2020/010/R (Amendment 19) carries AMC 20-152A; both consolidated in EAR Amendment 23. (ch01)

## Is AMC 20-115D the door, and what did replacing 115C change? → ch02

- Applicability: applicants, DAHs, and developers of software installed on type-certified aircraft, engines, and propellers, or used in ETSO articles. (ch02)
- ETSO software shares the door with product certification; no separate ETSO-only means exists. (ch02)
- AMC 20-115D replaces and cancels AMC 20-115C (12 September 2013); the recognised basis moves to ED-12C/DO-178C plus supplements. (ch02)
- "ED-12C/DO-178C" already folds in ED-215/DO-330 and the technique supplements as applicable; ED-94C/DO-248C are supporting, not primary. (ch02)
- Hardware is out of this AMC; that door is AMC 20-152A. (ch02)

## Am I on B-era processes, and can I stay? → ch03

- Six section 5 criteria gate continued ED-12B/DO-178B process use on new development; fail any one and the project upgrades to ED-12C/DO-178C. (ch03)
- The criteria: no known process deficiencies, prior certified use at an equal or higher software level, EASA-accepted technique embeddings, accepted PDI or configuration-data processes, unchanged plans and environment, and no intent to declare C-era satisfaction. (ch03)
- Under C-era processes: satisfy every applicable objective for the software level, produce the life cycle data, submit the liaison data, and honour any CS-specific level-mapping AMC over the generic mapping. (ch03)
- Technique supplements are never stand-alone: the PSAC states the joint application, objective by objective. (ch03)
- Legacy modify/reuse runs usage history and the Table 1 level check first; unacceptable intersections force a baseline upgrade through the C-era change path and ED-215/DO-330. (ch03)
- Modification means CIA, and CIA results are summarised in the PSAC or SAS. (ch03)
- Staying on a pre-C edition for modifications is a deliberate non-claim: every 9.b.7 condition holds and no C-era satisfaction is declared. (ch03)
- Equivalence declared after a baseline upgrade never extends to unmodified tools. (ch03)
- FLS add-ons: corruption and partial-load protection at the FLS level, a verifiable loaded part number, and inhibit of inadvertent field loading in cruise and other safety-critical phases. (ch03)
- UMS: the modifiable portion is developed at a software level at least as high as the level assigned to that software. (ch03)

## What do paragraph 10 and GM1 to GM3 add? → ch04

- Tool qualification points at ED-12C/DO-178C section 12.2 and ED-215/DO-330; the AMC adds legacy-tool specialisation, not a second tool standard. (ch04)
- AMC Table 2 maps B-era development-tool and verification-tool types, by software level, onto TQL-1 through TQL-5; certification decisions use the official table. (ch04)
- Development tools keep B-era processes only where the old level meets the required TQL; TQL-4 verification tools requalify under ED-215/DO-330. (ch04)
- A tool declared as satisfying ED-215/DO-330 does not make the legacy software C-era-equivalent; software equivalence does not bless untouched tools. (ch04)
- GM1: CIA is a structured impact story across eight change item classes, not a list of edited files. (ch04)
- GM2: data coupling analysis and control coupling analysis are different analyses with different purposes; both are required, and both are earned by design-phase interface and dependency specification. (ch04)
- GM3: identify foreseeable error sources and specify protection in requirements; at Levels A and B prefer runtime protection over static analysis or probabilistic argument alone. (ch04)

## Does AMC 20-152A apply to my hardware? → ch05

- Applicability: AEH on type-certified aircraft, engines, and propellers, including ETSO article developers. (ch05)
- Coverage is DAL-bounded: AEH contributing to DAL A, B, or C; DAL C takes only a limited objective set, with the restriction written into each objective's own text. (ch05)
- DAL D: use of the AMC is not required; the appendix clarifications remain available as optional support for showing intended function. (ch05)
- The AMC recognises ED-80/DO-254 and then adds AMC-owned objectives for custom devices including COTS IP, COTS devices, and CBAs. (ch05)
- SEE is outside the AMC; CRI practice and CM-AS-004 are the name-only pointers, and the PHAC may still record SEE considerations. (ch05)
- The PHAC (or a related planning document) records the process and activities against the objectives and is submitted for certification. (ch05)

## Which objective rack applies? → ch06

- Custom device first: CD-1 records DAL, simple/complex classification, and the simple justification in the PHAC before anything else. (ch06)
- Simple is earned by verifiability: full deterministic test-and-analysis coverage under all foreseeable conditions with no anomalous behaviour; a bag of simple blocks can still be complex. (ch06)
- Complex path: ED-80/DO-254 plus sections 5.5 to 5.11. Simple path: CD-2's reduced process, with the 5.5.2.4-5.5.2.5 verification clarifications still in force. (ch06)
- CD-8 at DAL A/B: abnormal and boundary conditions and expected behaviour become requirements. CD-9: planned HDL coverage criteria for elemental analysis, with gaps justified and unreachable items complemented. (ch06)
- Tools: CD-10 independent output assessment sized to the objectives the tool serves; CD-11 credible history data, never a stand-alone design-tool story. (ch06)
- PDH reuse (CD-12): modification, function/use/classification change, or environment change each break prior credit until a Section 11.1 assessment. (ch06)
- COTS IP: IP-1 selection and IP-2 provider/data assessment gate the work; IP-3 fills provider gaps; IP-4 verifies the IP, the IP after your design steps, and the integration; IP-7 meets Appendix B at DAL A/B, with safety-specific analysis as the named alternative when coverage cannot reach the IP. (ch06)
- COTS devices: COTS-1 classifies complexity before section 6.4; COTS-2 ECMP; COTS-4 microcode either manufacturer-qualified or your own means of compliance; COTS-5 errata; COTS-6 failure modes into system safety; COTS-7 usage and interfaces with unused functions isolated; COTS-8 critical-configuration-setting mitigation at DAL A/B. (ch06)
- CBAs hosting complex custom or complex COTS devices: CBA-1 requires requirements capture, validation, verification, configuration management, and flow-down. (ch06)

## How do the two sides meet in one workflow? → ch07

- PSAC-class documents carry the software spine (objectives, supplement application, CIA/SAS closeout); the PHAC carries the hardware spine; both are AMC-pointed roles, not paywalled templates. (ch07)
- A TQP joins when a qualified tool uses supplement techniques, for tool qualification levels 1 through 4. (ch07)
- The seam is the HW/SW interface: intended function, HW/SW and HW/HW interface data, and unused COTS function control at DAL A/B with verified deactivation where available. (ch07)
- Related planning documents are allowed; what matters is that process and activities against the claimed objectives are written and submitted. (ch07)
- Open problems are a hygiene stream beside the plans; AMC 20-189 is the name-only pointer. (ch07)

## Quick anchors

| Need | Answer | Chapter |
|------|--------|---------|
| Which AMC governs? | Software 20-115D; AEH 20-152A; multi-core 20-193 name-only | ch01 |
| Is the AMC mandatory? | No; AltMoC with equivalent safety and EASA approval | ch01, ch02, ch05 |
| What replaced 115C? | AMC 20-115D, basis moved to ED-12C/DO-178C | ch02 |
| B-era reuse test | Six section 5 criteria; any failure upgrades | ch03 |
| CIA summary home | PSAC or SAS | ch03, ch07 |
| Legacy tool TQL | AMC Table 2 maps B-era types to TQL-1 through TQL-5 | ch04 |
| DAL D hardware | AMC use not required; clarifications optional | ch05 |
| Simple custom device claim | CD-1 justification in the PHAC, or it is complex | ch06 |
| COTS IP entry gates | IP-1 selection; IP-2 assessment | ch06 |
| Board with complex parts | CBA-1 process with requirement flow-down | ch06 |
| Where the plans meet | PSAC and TQP software spine; PHAC hardware spine | ch07 |
| FAA twin | `faa-8110-49`, not this pack | ch01 |
| Paywalled standard | `avionics-signpost` names it; no text here | ch01 |

## Tells & smells

| Smell | Likely gap | Chapter |
|-------|------------|---------|
| AMC treated as mandatory law | AltMoC exists under stated conditions | ch01, ch02, ch05 |
| Hardware answered from 115D, or software from 152A | Wrong door | ch02, ch05 |
| Objective tables pasted from ED/DO documents | Paywalled; name only, not reproduced | ch01, ch03, ch06 |
| B-era processes kept while declaring C-era satisfaction | Section 5 criterion forbids the combination | ch03 |
| CIA listing only edited source files | GM1 expects eight item classes | ch04 |
| Full objective stack applied at DAL C by default | Limited set; restriction sits in the objective text | ch05 |
| Device called simple with no CD-1 justification | Classification is evidence-based | ch06 |
| Provider marketing used as IP verification | IP-2 and IP-4 gates unmet | ch06 |
| PHAC never submitted | Objectives need a planned process on record | ch05, ch07 |

## What this pack is not

- Not mandatory law: both AMCs are acceptable means, not the only means; AltMoC exists. (ch01, ch02, ch05)
- Not the standards: ED-12C/DO-178C, ED-80/DO-254, and the supplement set are name only, not reproduced; `avionics-signpost` names and locates them. (ch01)
- Not the FAA side: FAA questions belong to `faa-8110-49`; the two AMC sections state their own harmonisation with the FAA ACs, nothing more. (ch01, ch03)
- Not multi-core: AMC 20-193 is a name-only pointer in this release. (ch01)
- Not the official AMC and not advice: reconstructed notes pinned to Amendment 23 as consolidated in the June 2023 EAR; check the EASA document library before relying on a single point. (ch01, ch05)

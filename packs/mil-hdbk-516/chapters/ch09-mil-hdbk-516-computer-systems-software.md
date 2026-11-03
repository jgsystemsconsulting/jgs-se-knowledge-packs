# Chapter: Computer systems and software

## Core Idea

Section 15 sets AW verification criteria for computer systems and software (CS&S) used in air systems. Criteria apply to CS&S that support execution and integrity of safety-critical functions (SCFs). Some criteria also reach CS&S that are not themselves SCF but can affect them.

Topics include scope and applicability, multicore processing environments, definitions and terminology, modification considerations, section assumptions, how CS&S methodology compares to other handbook methods, numbering of standards and MoCs, and artificial intelligence considerations. The foreword notes that section 15 was not fully rewritten to every D style objective; users still apply its criteria as published.

## Frameworks Introduced

### SCF-centered applicability

Start from safety-critical functions. Identify CS&S that implement or can affect those functions, then select criteria and MoCs.

### Architecture, process, and qualification

Cover system processing architecture; design and functional integration of architecture elements; hardware elements; software development processes; software architecture and design; and software qualification and installation.

### Multicore and AI as first-class concerns

Multicore environments and AI elements introduce timing, partitioning, and assurance challenges that traditional single-thread assumptions miss. Address them explicitly when the design uses them.

### Modification path

Software and computing changes reopen CS&S criteria even when the airframe is unchanged. Treat DMS and form-fit-function updates as AW-relevant.

## Key Concepts

- **CS&S.** Computing hardware, software, and firmware in the air system context.
- **SCF support.** Criteria intensity follows contribution to safety-critical behavior.
- **Processing architecture.** Partitioning, resource sharing, and integrity of the computing suite.
- **Software qualification and installation.** Evidence that the correct, qualified load is what flies.
- **AI elements.** When present, assess their effect on traditional AW methods and evidence.

## Mental Models

- **Function first, then code.** Map SCFs before arguing process maturity alone.
- **Hosted software is not free.** Avionics and VCF chapters own the function; this chapter owns computing assurance.
- **Incomplete style rewrite is not a skip.** Foreword caveats do not delete section 15 criteria.

## Key Takeaways

- Section 15 is the CS&S AW criteria set focused on SCF support.
- Cover architecture, hardware elements, development process, design, and qualification/installation.
- Call out multicore and AI when the design includes them.
- Reassess on software modification and DMS-driven computing changes.

## Connects To

- ch04 for VCF software paths
- ch07 and ch08 for displays, AR electronics, and avionics hosts
- ch02 for SE integration of software requirements and verification

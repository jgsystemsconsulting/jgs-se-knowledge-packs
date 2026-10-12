# Chapter 13 - Design-Level Error Handling

Sources: S4 AC 00-69, Best Practices for Airborne Software Development Assurance Using EUROCAE ED-12( ) and RTCA DO-178( ) (2017-07-21), section 3.3, lines 80-122 of `sources/text/S4.txt`. Best practices, not guidance, and not an acceptable means of compliance. Complements ED-12C/DO-178C (and ED-12B/DO-178B) sections 6.3.2-6.3.4, including 6.3.4.f; optional formal-methods route named as ED-216/DO-333. Designations only; those sections are not quoted here.

## Core Idea

AC 00-69 section 3.3 pushes foreseeable software error sources up to design-level handling. The AC is best practices, complementary to ED-12C/DO-178C, not guidance and not an acceptable means of compliance. ED-12C/DO-178C section 6.3.4.f (named only) already flags error sources that need focused source-code review. The AC's practice is stronger upstream: identify foreseeable error sources, pair each with mitigation, and specify protection mechanisms in high-level or low-level requirements, including verification of the handling mechanisms. For software levels A and B, prefer runtime protection mechanisms; probabilistic arguments or static analysis alone may not be enough. Formal methods under ED-216/DO-333 may improve runtime-error detection.

## Frameworks Introduced

- **Source-code review is necessary; design-level handling is the recommended reinforcement.** The standard's code-review focus on certain error sources remains; the AC adds design-time identification, mitigation, and requirements-level protection so foreseeable unintended behavior is handled before code review is the last net.

- **Four-step practice loop.** (1) Identify foreseeable error sources. (2) Identify mitigation for each source. (3) Specify protection mechanisms in software requirements (HLR or LLR), including how handling is verified. (4) At levels A and B, give serious consideration to runtime protection mechanisms; the same runtime mechanisms can be good practice at other levels.

- **Optional formal-methods assist.** ED-216/DO-333 may enhance detection of runtime errors. Named only; this chapter does not unpack the supplement.

## Key Concepts

### Foreseeable error sources (section 3.3.2.1)

Original summary of the sources the AC names (not a paste):

| Category | Examples the AC groups together |
|---|---|
| Runtime exceptions and arithmetic/resource errors | Fixed or floating-point arithmetic overflow; stack or heap overflow; division by zero; counter and timer overrun or wrap-around |
| Data, memory, and timing integrity | Data or memory corruption; timing issues from lack of partitioning; improper interrupt management; improper cache management |
| Unpredictable execution features | Dynamic allocation; out-of-order execution; resource contention |

These are foreseeable classes to drive design and requirements work, not an exhaustive hazard list for every project. Partitioning, interrupts, and cache appear because weak management there produces corruption and timing faults even when application logic looks clean. Dynamic allocation, out-of-order execution, and contention appear because they make execution order and resource availability harder to predict.

### Mitigation and requirements specification (sections 3.3.2.2-3.3.2.3)

For each foreseeable source:

1. Identify the associated mitigation.
2. Specify protection mechanisms in software requirements (high-level or low-level), including specification and verification of the handling mechanisms.

Mitigation that exists only in a design comment or in tribal knowledge does not meet the practice. The requirements set should state what is protected, how, and how verification will show the handler works.

### Runtime protection by software level (section 3.3.2.4)

| Software level | AC posture on runtime protection |
|---|---|
| A and B | Recommended to incorporate runtime protection mechanisms; reliance on probabilistic approaches or static analyses alone may not be adequate |
| Other levels | Runtime mechanisms may still be good practice |

"Recommended" here is best-practice language inside AC 00-69, not a new objective table. Projects at A and B that lean only on static analysis or probability arguments are off the AC's advice even if code review still occurs.

### Formal methods option (section 3.3.3)

Use of formal methods according to ED-216/DO-333 may enhance runtime-error detection. The AC presents this as an optional enhancement path, not a mandatory technique for every project.

### Designation-only standards map

| Designation | Role in this chapter |
|---|---|
| ED-12C/DO-178C sections 6.3.2, 6.3.3, 6.3.4 | Complementary industry references the AC points at |
| ED-12C/DO-178C section 6.3.4.f | Named locus for error sources that need focused source-code review |
| ED-216/DO-333 | Optional formal-methods supplement path for stronger runtime-error detection |

No clause text, no objective lists, and no reconstructed order material belong in pack notes.

## Mental Models

- Code review catches residual error sources; design-level requirements decide which sources are allowed to reach code without a handler.
- Runtime protection is a safety net with a level-sensitive strength recommendation (strongest wording at A and B), not a substitute for correct requirements and design.
- Static analysis and probabilistic reasoning help; at A and B the AC still wants runtime mechanisms in the conversation.
- Best practices complement the means of compliance. Citing AC 00-69 does not replace ED-12C/DO-178C section 6.3 evidence.

## Anti-patterns

- **Waiting for source-code review to discover overflow, wrap-around, or division-by-zero paths that design could have named.** Section 3.3.1 recommends design-level handling on top of the code-review focus.
- **Error source list without per-source mitigation.** Section 3.3.2.2 pairs every source with a mitigation.
- **Handlers described only in code comments, never in HLR/LLR.** Section 3.3.2.3 wants protection mechanisms in software requirements, with verification of handling included.
- **Level A/B reliance on static analysis or probability alone for these sources.** Section 3.3.2.4 recommends runtime protection at A and B.
- **Assuming partitioning, interrupt design, or cache policy are pure hardware concerns.** The AC lists them among software error sources tied to corruption and timing.
- **Treating dynamic allocation or contention as late performance tuning.** Section 3.3.2.1.3 groups them with features that make execution unpredictable enough to handle at design level.
- **Using AC 00-69 as the means of compliance for verification of reviews and analyses.** It is best practices only.

## Key Takeaways

1. AC 00-69 section 3.3 is best-practice material for design-level error handling; complementary to ED-12C/DO-178C sections 6.3.2-6.3.4 (including 6.3.4.f), not guidance and not an AMC.

2. Identify foreseeable sources across runtime exceptions, memory and timing integrity (partitioning, interrupts, cache), and unpredictable-execution features (dynamic allocation, out-of-order execution, contention).

3. For each source, identify mitigation and specify protection mechanisms in high-level or low-level requirements, including verification of the handlers.

4. At software levels A and B, incorporate runtime protection mechanisms; do not rely on probabilistic approaches or static analyses alone. Runtime mechanisms remain good practice at other levels.

5. ED-216/DO-333 is an optional formal-methods route that may improve runtime-error detection; designation only.

## Connects To

- **ch11** - CIA on architecture and code changes should re-open the foreseeable-error and runtime-protection story.
- **ch12** - interface and dependency design practices that interact with partitioning and control-flow assumptions.
- **ch05** - DO-178C recognition and verification/life-cycle data frame that still carries the section 6.3 evidence.
- **ch06** - legacy modify path and supplement use (including formal methods when DO-333 applies).
- **ch02** - reviews that will look for requirements-level handlers, not only code-level defensiveness.

# Chapter 2: System-Level Considerations

## Core Idea
Before and around the per-element SE processes, programs must reason at the **system level**: how SE applies to systems of systems, how digital engineering and modern techniques (mission, software, value, sustainability engineering) change practice, how to organize engineering resources and roles, and how the Systems Engineer shapes the contract through the RFP.

## Frameworks Introduced
- **Systems of Systems (SoS) typology** — four types: **virtual**, **collaborative**, **acknowledged**, **directed** — distinguished by management authority, funding, and the degree of central control over the constituent systems.
  - When to use: when the "system" is actually a set of independently managed/operated systems that must interoperate; it changes who controls interfaces and requirements.
- **Digital Engineering (DE)** — securely connect people, processes, data, and capabilities across an end-to-end digital enterprise, using authoritative models throughout the life cycle to represent the system of interest.
  - When to use: as the program's analysis backbone; it changes *how* reviews and analyses are conducted, not *what* must be done.
- **Modular Open Systems Approach (MOSA)** — design with severable modules and open interfaces/standards, to the maximum extent practicable.
  - When to use: when evolvability, competition, and avoiding vendor lock matter (i.e., almost always); MOSA and data-rights analysis go together.

## Key Concepts
- **Comparing systems and SoS**: SoS differ from single systems in management/operational independence of constituents, evolutionary development, emergent behavior, and geographic distribution — which complicates interface control and requirements authority.
- **DE goal set**: DoD's Digital Engineering Strategy goals (e.g., formalize model use across the life cycle, provide an authoritative source of truth, incorporate technological innovation, establish supporting infrastructure/environments, transform culture/workforce).
- **Mission engineering**: analysis of how systems combine to achieve mission outcomes — feeds requirements and trade space upstream of system SE.
- **Software engineering & DevSecOps**: continuous integration / continuous deployment practice integrated into the SE effort; software is a first-class system element.
- **Value engineering & sustainability analysis**: structured techniques to improve value (function per cost) and to assess life-cycle environmental and resource impacts.
- **Engineering resources**: roles and responsibilities (PM, Systems Engineer, Lead Software Engineer), stakeholders, **Integrated Product Teams (IPTs)** (including the SE WIPT), automated tools, and SE **certifications**.
- **SE role in contracting**: the Systems Engineer shapes the **RFP** technical content — the SOW/PWS, technical requirements, data deliverables (CDRLs/DIDs), evaluation criteria, and required technical reviews — so that the contract obligates the right SE activities and products.

## Mental Models
- "What is the system?" is the first SoS question: if constituents have their own PMs, budgets, and missions, you are doing SoS SE and you do **not** fully control their requirements or interfaces — you negotiate them.
- DE is a force multiplier on the *how*: a good digital ecosystem (authoritative source of truth + static/dynamic models) makes reviews and trade-space exploration faster and more iterative, but it does not remove any required review.
- The contract is where SE intent becomes enforceable: if a review, product, or data item is not in the RFP/contract, the program cannot reliably get it later.

## Anti-patterns
- **Running SoS as if it were a single system**: assuming central authority over constituent requirements/interfaces that the program does not actually have.
- **"Digital engineering" as a tool purchase**: buying modeling tools without an authoritative source of truth, data strategy, or workforce change — DE is an enterprise practice, not a license.
- **Leaving SE out of the RFP**: discovering at execution that required technical reviews, data deliverables, or MOSA/data-rights provisions were never put on contract.

## Key Takeaways
1. Identify the **SoS type** (virtual / collaborative / acknowledged / directed) — it determines your real authority over requirements and interfaces.
2. **Digital Engineering** changes *how* SE analyses and reviews are done, not *what* is required; its value depends on an authoritative source of truth and models across the life cycle.
3. Apply **MOSA** to the maximum extent practicable, paired with a data-rights analysis, for evolvability and competition.
4. Organize engineering through **IPTs** (incl. the SE WIPT) with clear roles for the PM, Systems Engineer, and Lead Software Engineer.
5. The Systems Engineer shapes the **RFP** so the contract obligates the right SE activities, reviews, and data deliverables.

## Connects To
- **ch04 (Technical Management Processes)**: Technical Planning resources these teams; Configuration/Data/Interface Management are central to SoS and DE.
- **ch03 (Technical Reviews & Audits)**: DE changes how reviews are conducted; the RFP puts required reviews on contract.
- **ch06 (Design Considerations)**: MOSA, modular design, and interoperability are also design considerations.
- **`dodaf` pack**: architecture frameworks/viewpoints used to model SoS and capability.
- **DoDI 5000.88 / Engineering of Defense Systems Guidebook**: pathway-specific SoS and DE guidance.

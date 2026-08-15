# Chapter 5: IT/OT Implementation, Prioritization, and Using CPGs

## Core Idea
CPG 2.0 treats IT and OT as a shared goal set while recognizing OT’s reliability-first design history and weaker built-in security. Effective adoption means prioritizing goals against real threats and resource constraints, translating outcomes into concrete actions for both enterprise and industrial environments, and using CPGs to drive investment conversations.

## Frameworks Introduced
- **Universal goal set over siloed IT/OT lists**: 2.0 folds former OT-only items into cross-cutting goals.
- **Prioritized subset model**: Implement highest-yield goals first; expand toward fuller CSF programs later.
- **Executive communication pattern**: Outcome language supports board-level resourcing and benchmarking.

## Key Concepts
- **Why OT is special but not separate**: OT/ICS often prioritize availability and safety; many systems lack modern auth, patching, or encryption. CPGs still expect segmentation, credential hygiene, remote-access hardening, inventories, and recovery paths that respect process safety.
- **IT/OT boundary controls**: Segmentation (3.I), authorized devices (3.R), internet-facing hardening (3.S), and MSP oversight (1.E) are frequent OT-relevant control points.
- **Identity in mixed estates**: Default passwords and shared engineering accounts are chronic OT issues addressed by 3.A–3.H; apply carefully to avoid unsafe lockouts — use staged changes and out-of-band recovery.
- **Logging and monitoring realism**: Collect what you can without breaking control loops; prioritize jump hosts, historians, firewalls, and remote access paths when endpoint agents are impossible.
- **Prioritization method**: Use CISA/partner threat observations and your sector’s risk profile; do not treat the document order as a blind sequence if ransomware-ready backups (3.O) and MFA (3.F) are open gaps.
- **Benchmarking and investment**: Score current vs target goal attainment (often via CSET or internal trackers); express gaps as risk reduction per dollar for governing bodies.
- **Sector-specific goals (SSGs)**: Some sectors publish additional goals beyond the cross-sector set — CPGs are the common floor, not the ceiling.
- **Slick-sheet role**: Short-form overview for awareness and alignment; the full report carries complete outcome/action text for implementation.

## Mental Models
- Start with identity, remote access, segmentation, backups, and logging — they unlock both IT ransomware resilience and OT remote-threat reduction.
- Translate each outcome into an owner, system list, and evidence artifact before buying tools.
- Safety override: never “secure” an OT process in a way that creates uncontrolled shutdown risk; engineer changes with operations.
- CPGs answer “where to start,” not “when you are done.”

## Anti-patterns
- **Separate incompatible IT and OT checklists that duplicate 2.0 merges**: Reintroduces the fragmentation 2.0 removed.
- **Agent-everywhere mandate on fragile controllers**: Prefer boundary and jump-host controls when native agents are unsafe.
- **Board slides with red/yellow/green and no owners**: Benchmarking without accountability fails GOVERN intent.
- **Waiting for perfect inventory before any MFA/backup work**: Parallelize critical PROTECT goals with IDENTIFY maturation.

## Key Takeaways
1. CPG 2.0 uses one goal set spanning IT and OT rather than siloed OT-only catalogs.
2. OT constraints change *how* you implement, not *whether* foundational outcomes apply.
3. Prioritize against threat and resource reality; identity, segmentation, backups, and logging are frequent first wins.
4. Use outcome language to justify investment and track progress with governing bodies.
5. Sector-specific goals may extend the cross-sector floor.
6. Pair the short overview (slick sheet) with the full report when executing.

## Connects To
- **ch01**: 2.0 consolidation rationale.
- **ch02–ch04**: Goal details being implemented.
- **nist-csf**: Broader program beyond the CPG subset.
- **doe-sem / SE packs**: Engineering change discipline when modifying operational systems.

# Chapter 6: Appendices as a Map — When to Open Which Annex

## Core Idea
The body of IS-GPS-200 is the interface contract; the appendices carry most of the *normative payload*. Learn the map. Do not transcribe Apps II–IV (no PRN/Gold-code tables, no CNAV/LNAV bit fields). Open the official IS when a decoder, simulator, or waiver actually needs those bits.

## Frameworks Introduced
- **Appendix I — Letters of Exception**: SV- or manufacturer-specific qualified non-compliances. Read first when a vehicle “doesn’t match the shall.” Scope, applicable docs, then the letters themselves.
- **Appendix II — LNAV D(t) for PRN 1–32**: data characteristics, 30-second frame / 5-subframe structure, TLM/HOW, subframe 1 clock/health/IODC, 2–3 ephemeris, 4–5 almanac/UTC/iono/NMCT, timing relationships, parity. Starts ~p.78.
- **Appendix III — CNAV DC(t)**: typed messages (10/11 ephemeris & health; 30–37 clock-plus; 12/31/37 almanacs; 32 EOP; 33 UTC; 13/14/34 differentials; 35 GGTO; 15/36 text; 40 integrity support), timing, parity. Starts ~p.141.
- **Appendix IV — LNAV D(t) for PRN 33–63**: same family as App II, upper PRN neighborhood (data IDs, SV IDs, health/almanac slots that differ). Starts ~p.212.
- **§6 notes as a mini-appendix in the body**: acronyms, definitions (URA, CEI, reserved/invalid), extra PRN sequences, operational protocols. Some “tables in §6” are still identification payload — treat like annexes.

## Key Concepts
- **Why split II and IV**: upper PRNs were redesignated as the constellation grew. Keeping two annexes avoids breaking every PRN 1–32 decoder when 33–63 semantics diverge.
- **Figures 20-1 / 30-x / 40-1 are the bit maps**: eleven-sheet LNAV frames, per-type CNAV layouts. They are why this pack stops at the map — overlap risk and agent-context waste.
- **When to open which**:
  - Exception against a shall → App I
  - Civil/legacy nav decoder for PRN ≤32 → App II
  - L2 CNAV decoder / ISM → App III
  - Upper-PRN LNAV → App IV
  - Code-phase assignment / expanded PRN → body tables 3-I* and §6.3.6 (still not copied here)
  - Preparation process, VRTM, IRD vs ICD outline → leave this pack; use `faa-std-025`
- **What this pack will never be**: IS-GPS-705J (L5), IS-GPS-800J (L1C), ICD-GPS-153 (request-only), or a searched-for IS-300 (does not exist on the public list).

## Mental Models
- Annexes are *normative attachments*, not optional background.
- A map is sufficient for Interface Management competency; a dump is a second, different product.
- If the question is “how do I write my program’s ICD,” you are in the wrong pack (`faa-std-025`). If the question is “how does a real IS stash its bits,” you are here.

## Anti-patterns
- **Copying Gold-code taps, first-N chips, or convolutional polynomials into notes.**
- **Implementing CNAV from memory of message-type numbers only.**
- **Assuming App IV is a verbatim clone of App II.**
- **Building `packs/is-gps-705j`, `is-gps-800j`, `icd-gps-153`, or `gps-is-200n`.**

## Key Takeaways
1. Use this chapter as a routing table, not as a substitute for the annexes.
2. App I qualifies shalls; II/IV hold LNAV; III holds CNAV.
3. Bit maps and PRN tables stay in the official IS.
4. §6 extra-PRN material is annex-like — still not transcribed.
5. Complementary pack: `faa-std-025` for preparation rules.
6. One public L1/L2 exemplar is enough; do not ingest the rest of the GPS ICD family here.

## Connects To
- **ch01**: How IRNs and exceptions enter the baseline.
- **ch02–ch05**: Body clauses that point at these annexes.
- **faa-std-025**: Writing the next ICD so *its* annexes are equally navigable.

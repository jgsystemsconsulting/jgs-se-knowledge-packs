# FAA HF-STD-001B Cheatsheet

Fast-reference decision rules, selection tables, and tells-and-smells distilled from the standard. Numbers are design limits the standard states; trace any figure back to its chapter and cited source before treating it as binding.

## Signal classes (the alert family)
| Class | Meaning | Action |
|---|---|---|
| **Warning** | Hazardous condition; risk of injury, loss of life, equipment damage, or service interruption | Immediate action |
| **Caution** | Condition needs attention; possible equipment damage | Attention, not immediate action |
| **Advisory** | Safe/normal configuration or routine information | None / awareness |
| **Alert** | Demands immediate action or flags a significant update | Per the alerted condition |

## Reserved color-coding (displays, indicators, CHI)
| Color | Reserved meaning |
|---|---|
| **Flashing red** | Emergency needing immediate action to prevent injury/damage |
| **Red** | No-go / inoperative / error / failure / malfunction |
| **Yellow** | Marginal condition; caution; recheck |
| **Green** | In-tolerance / ready / satisfactory / proceed |
| **White** | Neutral; alternatives without operability or safety implication |
| **Blue** | Advisory only |

Rules: one meaning per color; redundant with another code; honor pre-existing user-community meanings; avoid dominant wavelengths above 650 nm; avoid blue/green/violet coding for aging users.

## Coding channel capacities (CHI, ch06)
- Brightness levels: ≤3 (separated by 2:1 ratios)
- Sizes: ≤3 · Line widths: ≤3 · Line angles: ≤11
- Shapes: ideally 5, not normally over 15
- Colors: ≤4 on one alphanumeric screen, ≤7 across a related set
- Flashing: 2–5 Hz, ≥50% on-interval, on a small area, never on the text the user must read

## Distinct auditory signals a person can handle (ch05)
- Absolute identification: cap at **4** (4–7 learnable quickly; up to 9 only with regular exposure)
- Relative discrimination: cap at **12**

## Warning-signal physics (ch05)
- Frequency: 200–5,000 Hz (preferably 500–3,000); <1,000 Hz to carry ≥300 m; <500 Hz to pass obstacles/partitions
- Loudness: ≥10 dB(A) over ambient; ceiling 115 dB(A) emergency / 90 dB(A) other
- Intermittent and modulated (1–8 beeps/s, or warble 1–3 cycles/s)
- Two-element timing: 0.5 s alert, then essential info in the first 2 s of the action signal

## Display legibility (ch04, ch06)
- Angular character size: ≥10 min-arc non-critical, ≥16 critical, 20–24 preferred — at longest viewing distance
- Contrast: >3:1 (7:1 preferred), no lower than 2:1 at peak ambient
- Pixel density: ≥90 dpi reading, ≥100 dpi complex symbols
- Control-reach cap: eye-to-display ≤635 mm (5th-percentile female reach); min viewing distance 330 mm
- Screen density ceiling: ~60% filled positions

## Keyboard envelope (ch08, ANSI 1988)
- Key strike width ~12–15 mm; horizontal spacing 16–19 mm; vertical 18–21 mm
- Depression force 0.25–1.5 N (0.5–0.6 N preferred); slope 0–25° (under 15° preferred)
- Numeric keypad: 1–9 in 3×3, 0 centered below; alphanumeric: QWERTY

## Anthropometric percentile selection (ch01, ch08, ch09)
| Dimension type | Percentile |
|---|---|
| Clearance / body passage | 95th-male (99th for heavy or life-threatening passages) |
| Limiting reach / strength | 5th-female (1st for critical escape) |
| Adjustable dimensions | 5th-to-95th |
| Critical life support | 1st-to-99th |
| **Never** | the 50th percentile / mean as a design criterion |

## Mutually-exclusive choice control sizing (ch07)
- ≤6 options → radio buttons · ≤10 → menu · >10 → scrolling menu
- Per-menu options: 3–10 · Hierarchical depth: ≤4 selections · Cascade: ≤1 level

## Response-time / feedback ladder (ch07)
- Acknowledge every action instantly
- "Working" indication past 2 s · inform of delay past 15 s · countdown past 60 s · positive completion signal for long waits

## Fastener preference order (ch03, ease of maintenance)
Quick fastening/releasing → latches/catches → captive fasteners → screws → nuts and bolts (last)

## Handling limits (ch03)
- One-person carry: 16 kg · two-person: 19 kg/person (distances ≤10 m)
- Reach into a lift: ≤635 mm · multi-person lift scales as X + 0.75(N−1)X
- Lifting eyes/jacking points: units >68 kg · weight/crew labels: >13.6 kg or multi-lifter

## Electrical / hazard limits (ch09)
- Shock hazard treated at ≥30 V · sensation ~1–2 mA · let-go ~16–20 mA · fibrillation 51–100 mA
- Interlocks: bypassable 70–500 V; non-bypassable >500 V or RF/microwave >300 KHz; auto-reset on cover replacement
- Touch burn onset: 45°C skin · CO cap: 50 ppm · hearing conservation at 85 dBA 8-hr TWA
- Interlock ≠ lockout/tagout; lockout and tagout used together

## Tells & smells (anti-patterns to catch in review)
- A critical condition signalled **only** by an absence (dark light, dimmed-off display, missing indication)
- **Color alone** carrying information, or color used where the target color is shared by other items
- **Technology-centered automation** — automating because the capability exists, not because it helps
- **Silent automation / silent slow processing** — state change or delay with no feedback
- **Mode errors** from inadequate feedback on which mode is active; more modes than needed
- Sound used for **normal conditions**, overused, startling, or resembling real operational sounds
- A flood of component failures reported on total system failure (should consolidate to the top-level fault)
- **Enter key** used to confirm a destructive action; Delete adjacent to Save
- Flash/refresh in the **15–20 Hz seizure band**
- Maintenance access from **underneath/inside** rather than above/outside; riveted access panels; stacked or blocking units
- **Interlock as the sole de-energizing means** (violates OSHA lockout/tagout)
- Anthropometric sins: designing to the **50th percentile**, treating one percentile as universal across dimensions, **summing** like-percentiles across body segments, using single-joint data for adjacent joints
- A standard treated as a **guarantee of good design** — it cannot replace human-factors expertise or representative-user testing
- **Unskilled tailoring** — worse than coarse tailoring; an accurate high-level cut beats an inaccurate detailed one

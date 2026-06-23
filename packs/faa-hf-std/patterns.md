# FAA HF-STD-001B Patterns & Techniques

Reusable human-factors design techniques drawn from HF-STD-001B, each framed as *When to use / How / Trade-offs*. These are the moves an engineer applies when specifying or evaluating an FAA-domain interface, console, alarm, or piece of maintainable equipment.

## 1. Quantify a qualitative requirement
- **When**: any time a requirement reads "legible", "reachable", "easy", or "safe" and a reviewer could argue about whether it is met.
- **How**: convert the adjective into a measurable limit the standard supplies — angular character size in minutes of arc, viewing distance in millimetres, illumination in footcandles, contrast ratios, control force in newtons, lift weight in kilograms, flash rate in hertz. Specify against the worst-case condition, not the nominal one.
- **Trade-offs**: numbers are testable and contractible but can over-constrain a novel design; keep the source citation so the figure can be re-derived or relaxed during tailoring.

## 2. Two-layer error handling (resistance + tolerance)
- **When**: designing any task where operator error is plausible and consequential.
- **How**: first make the error hard to commit (simplicity, clear information, electronic checklists — *resistance*); then assume errors still happen and limit their damage (monitoring, confirmation, undo — *tolerance*). Apply both layers, not one.
- **Trade-offs**: resistance can add steps that slow expert users; tolerance adds monitoring and recovery machinery. The two are complements, never substitutes.

## 3. Match automation authority to task risk
- **When**: deciding how much autonomy to grant an automated function.
- **How**: place the function on the levels-of-automation ladder (from full autonomy down to no assistance). For higher-uncertainty, higher-risk tasks, cap authority at "suggest a preferred alternative" and keep the operator in command with a guaranteed manual override and graceful degradation.
- **Trade-offs**: lower authority preserves situation awareness and recoverability but spends operator workload; higher authority cuts workload but risks complacency, skill decay, and un-recoverable dependence.

## 4. Audio as a redundant pointer, not the message
- **When**: designing any non-verbal auditory alert.
- **How**: put the meaning in a visual indication that defines the condition, and let the sound direct attention to that display. In high-illumination areas, provide both channels. Reserve voice for cases where coded meanings are too many or directions too complex.
- **Trade-offs**: redundancy costs a display element and a sound source, but a sound alone is easily masked, ignored, or misattributed; the pairing survives a single-channel failure.

## 5. Hit the salience window
- **When**: setting the physics of a warning signal.
- **How**: keep frequency in 200–5,000 Hz (preferably 500–3,000), at least 10 dB(A) over ambient, intermittent and modulated, distinct from background and from other signals — but capped (115 dB(A) emergency, 90 dB(A) otherwise) and never so startling it blocks the response. Limit distinct signals to four for absolute identification.
- **Trade-offs**: a louder, more numerous signal set raises detection but spends operator trust; every confusable or unnecessary alarm erodes the credibility of the whole system.

## 6. Design maintainability in by decomposition
- **When**: architecting any piece of equipment that will be inspected, tested, or repaired.
- **How**: break the unit into independent, interchangeable, replaceable modules with ready access; reuse existing items that meet the criteria before designing new ones; design for the worst combination of context (continuous operation + protective clothing + outdoor + lowest-skill maintainer).
- **Trade-offs**: modularization can raise unit count and interface complexity, but it yields access, fault isolation, lower skill demand, and faster mean-time-to-repair.

## 7. Poka-yoke the assembly
- **When**: any installation or connection that could be done wrong with harmful effect.
- **How**: make the wrong action physically impossible — alignment pins and tracks, asymmetric covers, physically incompatible connectors across functions, and distinct fasteners where types are mixed. Enforce the rule that non-interchangeable items must not be physically interchangeable.
- **Trade-offs**: keying and incompatibility add tooling and part variety; the payoff is the elimination of a whole class of mis-assembly errors.

## 8. The "absence is not a signal" rule
- **When**: using a light, indicator, or display to communicate a critical state.
- **How**: never let a dark bulb, a dimmed-to-off display, or a missing indication be the sole carrier of a critical condition — failure looks identical to "nothing wrong". Provide redundant lamps with a test means, and never allow a display to dim indistinguishably from off.
- **Trade-offs**: redundant lamps and test circuits add cost; without them a failed indicator silently hides a hazard.

## 9. Bind the control to its indicator
- **When**: laying out any control and the indicator that reports its effect.
- **How**: make the relationship immediately apparent through proximity, grouping, coding, and labeling; place the control below the indicator so neither it nor the hand obscures the readout; standardize direction-of-movement (clockwise/up/right = increase); give feedback the user perceives as instantaneous.
- **Trade-offs**: tight binding constrains panel layout but removes the ambiguity where operator error is born.

## 10. Coding as a constrained vocabulary
- **When**: assigning meaning through color, brightness, shape, size, line, texture, or flashing.
- **How**: respect the per-channel capacity caps (≈three brightness levels, three sizes, four colors per screen, eleven line angles, ≤fifteen shapes); make color redundant with another code; honor reserved color meanings (red = no-go, yellow = caution, green = go, flashing red = emergency); never overwrite an established user-community meaning.
- **Trade-offs**: redundant coding uses more channels per item, but color-only coding fails for color-deficient users and degrades search at high display density.

## 11. Choose the interaction type first
- **When**: at the start of any interactive-interface design.
- **How**: pick the interaction style (question-answer, form-filling, menu, function key, command language, query language, constrained natural language, direct manipulation) against the triad of task requirements, system characteristics, and user training — before designing the screen.
- **Trade-offs**: command languages serve trained frequent users but punish novices; menus serve constrained choices but slow high-volume expert entry. Serve both ends of the trained/untrained axis where possible.

## 12. Feedback graded to delay
- **When**: any operation that may take perceptible time.
- **How**: acknowledge every action instantly; show a "working" indication past 2 seconds; warn the user when a delay will exceed 15 seconds; count down past 60 seconds; give a positive completion signal for long waits. Bound response-time variability within the standard's percentage bands.
- **Trade-offs**: progress machinery adds implementation work, but the model assumes uncertainty (not delay itself) is what frustrates the operator.

## 13. Fence destructive actions
- **When**: any control entry that could change or lose stored data.
- **How**: require explicit notification of the consequence and a confirming action that is *not* the Enter key; separate opposing actions (Delete not adjacent to Save); never make a destructive button the default; layer recoverability (Back, Cancel, Undo, Redo, Restart, Suspend).
- **Trade-offs**: confirmation adds a step to legitimate destructive operations; the alternative is silent, unrecoverable data loss from a reflexive keystroke.

## 14. Consequence-scaled percentile selection
- **When**: setting any anthropometric dimension.
- **How**: pick the percentile by what failure costs — clearance and body passage to the 95th-percentile male (or 99th for heavy/life-threatening passages), limiting reach and strength to the 5th-percentile female (or 1st for critical escape), and general adjustability across the 5th-to-95th band, with critical life support spanning 1st-to-99th.
- **Trade-offs**: extreme percentiles widen accommodation but cost space and adjustability range; a single mid-percentile cut silently excludes large parts of the population.

## 15. Reduce and rebuild borrowed human data
- **When**: applying strength or reach figures inherited from a source standard.
- **How**: never design to a maximum — strength data collected from young military men at full exertion is stepped down (e.g. control forces to 80% of the 5th-percentile male, then by fixed ratios for female users), and static reach numbers are rebuilt into task-specific envelopes adjusted for grasp, torso movement, seat angle, and clothing.
- **Trade-offs**: conservative reduction lowers achievable performance specs but ensures the weakest likely operator can still work the system.

## 16. Tailor early, detailed, and by an expert
- **When**: applying the standard to a real program under cost and schedule pressure.
- **How**: treat tailoring as more than include/exclude — adjust requirement strength (shall ↔ should), assess verifiability and objectiveness, derive requirements, and flag those likely to become inapplicable. Do it early and in detail, by someone skilled in human factors.
- **Trade-offs**: a careful tailored list looks heavier in review than "impose the whole chapter", but a whole chapter actually imposes strictly more; surplus requirements are cheap to delete later, missing ones expensive to add.

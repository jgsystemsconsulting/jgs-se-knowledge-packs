# Patterns — MIL-HDBK-338B

## 1. Spec to Allocate to Predict Loop
- **When:** Starting or resetting a reliability program on an electronic system.
- **How:** Write quantitative requirements with environment; build allocation tree; maintain a living prediction model.
- **Trade-offs:** Upfront modeling cost vs late discovery that architecture cannot meet the number.

## 2. Derating Before Redundancy
- **When:** Reliability shortfall appears in early prediction.
- **How:** Reduce electrical/thermal stress and tighten parts control before adding parallel hardware.
- **Trade-offs:** Possible performance margin reduction vs logistics/coverage complexity of redundancy.

## 3. Dual-Analysis Pair (FMEA + FTA)
- **When:** Safety- or mission-critical functions.
- **How:** Bottom-up FMEA/FMECA for breadth; top-down FTA on critical top events for combinations/common cause.
- **Trade-offs:** Analysis effort vs blind spots of using only one direction.

## 4. FRACAS with Teeth
- **When:** Integration, growth test, or field returns.
- **How:** Mandatory root cause, corrective action owner, and verify-fix; feed modes back into FMEA/prediction.
- **Trade-offs:** Process overhead vs repeating the same escapes.

## 5. Growth vs Demonstration Choice
- **When:** Planning reliability test money.
- **How:** Use growth while design can still change; demonstration when configuration is frozen.
- **Trade-offs:** Schedule for fixes vs false confidence from a single demonstration shot.

## 6. Testability Entry Criteria
- **When:** Design reviews before layout/packaging freeze.
- **How:** Require detection/isolation coverage targets tied to FMEA-critical modes; include BIT/probe access.
- **Trade-offs:** Early DFT features vs board area/firmware cost.

## 7. Environment-Linked Prediction
- **When:** Predictions disagree with field data.
- **How:** Rebuild stress profiles from real environments; refresh derating and part failure rates.
- **Trade-offs:** Data collection effort vs comforting but wrong lab assumptions.

## 8. COTS/NDI Risk Gate
- **When:** Inserting commercial items into military electronic systems.
- **How:** Explicit selection criteria, delta assurance, and system-level modeling of unknown failure modes.
- **Trade-offs:** Cost/schedule gains vs assurance gaps.

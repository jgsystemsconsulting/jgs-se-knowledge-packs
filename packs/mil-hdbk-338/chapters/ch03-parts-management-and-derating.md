# Chapter 3: Parts Management and Derating

## Core Idea
Section 7 opens reliability design guidance with parts management and derating — high-leverage early choices. Manufacturing process maturity, screening, application stress, and operation below rated limits set inherent failure rates used in later models.

## Frameworks Introduced
- **Parts management**: Selecting, qualifying, and controlling parts with attention to process maturity and application.
- **Electronic derating**: Operating below rated electrical/thermal stress to reduce failure rates.
- **Mechanical/structural derating**: Stress-margin thinking for non-electronic elements where the handbook addresses them.

## Key Concepts
- Parts management covers selection, qualification, and application control.
- Manufacturer process maturity strongly influences field failure rates.
- Electronic derating lowers electrical and thermal stress below ratings.
- Derating criteria should track the actual mission environments.
- Inherent reliability is largely set once parts and stresses freeze.

## Mental Models
- Inherent reliability is largely fixed once parts list and stresses freeze.
- Derating trades capability for life; it is not free performance.
- Maker process capability often dominates field results more than paper ratings.

## Anti-patterns
- **Catalog max as design target**: Designing to absolute maximum ratings.
- **One derating table for all missions**: Ignoring thermal, radiation, or dormant environments.
- **Parts list without stress review**: Approved parts never checked in actual circuits.

## Key Takeaways
1. Invest in parts management before exotic redundancy.
2. Derate electronics with documented stress criteria tied to environment.
3. Treat manufacturer quality/volume as a reliability input.
4. Feed actual stresses into prediction (ch02).
5. Revisit derating when packaging or cooling changes.

## Connects To
- **ch04** for circuit techniques that assume managed parts.
- **ch02** for derated rates in predictions.
- **ch05** for environmental stresses driving derating.

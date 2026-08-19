---
phase: 8-agent-enablement-surface
reviewed: 2026-08-17T00:35:00Z
depth: deep
scope: impl (diff d821099..ab42f7a)
files_reviewed: 4
files_reviewed_list:
  - tooling/check_capability_map.py
  - docs/capability-pack-map.json
  - docs/capability-pack-map.md
  - docs/capability-map-CONTRACT.md
findings:
  critical: 0
  blocker: 0
  major: 1
  minor: 3
  info: 3
  total: 7
status: issues_found
verdict: PASS_WITH_NOTES
---

# Phase 8 Impl Review (diff scope: d821099, dc35907, 1c32f59, ab42f7a)

**Verdict:** PASS_WITH_NOTES

No blockers. The committed artifacts are verified correct; the findings below are
gate-hardening gaps and doc nits, none of which affect the shipped map data.

## What Was Adversarially Verified (evidence, not assertions)

The gate was loaded as a module and run against 12 corrupted map copies (temp files;
the real map never touched). Results:

| Corruption injected | Gate response | Fired? |
|---|---|---|
| Remove all `federal-bca` entries | `staleness: pack on disk not in map` + chapter-set on_disk_only=6 + OBM threshold | YES |
| Rename one chapter to `ch99-renamed.md` | chapter-set both directions + `existence: chapter missing` | YES |
| Strip C5 to 2 entries | `threshold: 'Interface Management & ICIDs' has 2 entries, need >=3` | YES |
| Duplicate one entry | `uniqueness: 1 duplicate (pack, chapter) pair(s)` | YES |
| `schema_version: "2"` (string) | `envelope: schema_version must be 2, got '2'` | YES |
| v1 keyless envelope | 3 named envelope failures | YES |
| Top-level JSON list | `envelope: top-level JSON must be an object` + cascades | YES |
| Bad JSON syntax (`{"clusters": [`) | clean `FAIL: JSON decode error` line, exit 1, no traceback | YES |
| Missing map file | `FAIL: map file missing`, exit 1 | YES |
| `schema_version: 2.0` (float) | **rc=0 PASS** | NO — see MA-01/MI-01 |
| Duplicate cluster name (rename cluster 1 to an existing name) | **rc=0 PASS** | NO — see MA-01 |
| Non-UTF-8 bytes (`\xff\xfe...`) | **uncaught UnicodeDecodeError traceback** | NO — see MI-02 |

Additional verified facts:

- Fresh runs: `python tooling/check_capability_map.py` exit=0 twice, byte-identical
  output (idempotent); `python tooling/check_release.py` exit=0.
- Envelope: top-level keys `['schema_version','map_version','generated_on','clusters']`;
  `schema_version` is int 2; `map_version == "1.18.0"`; `generated_on == "2026-08-17"`
  (matches machine date at commit time, 2026-08-17T00:21Z).
- Coverage: 61/61 chapter-bearing packs on disk mapped, 0 missing, 0 stale;
  chapter-set equality exact (52 new chapters all present); all 6 new support-file
  rows resolve at pack root.
- Backward compat proven entry-by-entry vs `d821099^`: all 570 pre-existing
  (cluster, pack, chapter, note) rows identical, cluster order/names identical,
  old top-level was keyless `{"clusters"}` — v1 `data["clusters"]` consumers keep
  working; 58 rows added (52 chapters + 6 support).
- md/JSON sync: all 32 summary-table counts AND all 32 per-cluster section row
  counts match the JSON exactly; totals 628/628.
- Entry shape: every one of 628 entries has exactly `{pack, chapter, note}` keys,
  no empty notes; all 32 cluster names unique (in the committed file).
- CONTRACT doc accuracy: schema example, field table, versioning, deprecation,
  refresh path, and threshold table all match the actual JSON and the gate's
  `THRESHOLDS` dict (>=1/>=3/>=3/>=2, name-keyed).
- Classification spot-check (8 chapters, 6 packs, 8 clusters): mil-std-40051 ch01
  (C25), federal-bca ch02 (C15), faa-std-025 ch04 (C5), faa-std-025 ch05 (C3),
  mil-std-881f ch07 (C17), dote ch03 (C8), dod-vva ch06 (C32), dafman ch06 (C6) —
  all 8 defensible against actual chapter content; secondary fits noted per the
  rules of construction.
- Red-run evidence pasted in `d821099` commit body (36 issues, 0 existence failures),
  matching the plan's predicted red shape.

## Narrative Findings (AI reviewer)

### MA-01: Gate silently accepts duplicate cluster names (counts dict last-wins)

**Severity:** MAJOR
**File:** `tooling/check_capability_map.py:95` (`counts[name] = len(chapters)`)
**Issue:** Cluster names are the stable identity the whole v2 contract keys on
(FR-2.1: name -> list of {pack, chapter}), and the CONTRACT doc calls
`clusters[].name` "Stable cluster identity" — but the gate never asserts name
uniqueness. `counts` is keyed by name, so when two clusters share a name the last
one silently overwrites the first: printed counts and threshold asserts evaluate
only the last duplicate. Verified: renaming cluster 1 ("Systems Thinking &
Fundamentals") to "Opportunity/Benefit Management" in a copy yields rc=0 PASS —
one cluster vanishes and the two merge for consumers, undetected (T-8-01 gap).
The committed map has 32 unique names, so this is a validation blind spot, not a
shipped-data defect.
**Fix:**
```python
seen_names: set[str] = set()
...
if name in seen_names:
    fail(errs, f"clusters: duplicate cluster name: {name!r}")
seen_names.add(name)
counts[name] = len(chapters)
```

### MI-01: `schema_version` type not enforced — float `2.0` passes

**Severity:** MINOR
**File:** `tooling/check_capability_map.py:61-65`
**Issue:** The check is `schema != 2` (numeric equality); JSON `2.0` parses to
Python float and `2.0 == 2` is True, so a float schema_version passes the gate
while the CONTRACT declares the field as int and instructs consumers to check
`schema_version == 2` — a strict consumer could reject gate-passed data.
**Fix:** `if not isinstance(schema, int) or isinstance(schema, bool) or schema != 2:`

### MI-02: Non-UTF-8 map file crashes with a bare traceback

**Severity:** MINOR
**File:** `tooling/check_capability_map.py:50-55`
**Issue:** Only `json.JSONDecodeError` is caught. A map file with invalid UTF-8
bytes raises `UnicodeDecodeError` (a `ValueError` subclass, not a
`JSONDecodeError`) during `json.load(fh)` — verified: uncaught traceback. The
process still exits non-zero via the interpreter (fails closed), but this violates
the plan's T-8-04 mitigation and the Task 1 done-criterion ("fails cleanly on
malformed JSON") for the encoding-corruption path — a realistic Windows-editor
corruption mode.
**Fix:** `except (json.JSONDecodeError, UnicodeDecodeError) as exc:`

### MI-03: `map_version` / `generated_on` unvalidated vs contract types

**Severity:** MINOR
**File:** `tooling/check_capability_map.py:67-73`
**Issue:** Both fields are checked only for presence/non-empty (deliberate for
`generated_on` per the research's no-freshness-assert rule), but the CONTRACT
declares semver (`"1.18.0"`) and ISO date (`YYYY-MM-DD`). A typo like `"1.18O.0"`
or `"2026-8-17"` passes the gate while violating the published contract —
gate/contract divergence.
**Fix:** minimal shape asserts: `re.fullmatch(r"\d+\.\d+\.\d+", map_version)` and
`re.fullmatch(r"\d{4}-\d{2}-\d{2}", generated_on)` (still no freshness check).

### IN-01: CONTRACT refresh path references "cluster 30" in a name-keyed contract

**Severity:** INFO
**File:** `docs/capability-map-CONTRACT.md:72`
**Issue:** "process definitions → cluster 30" uses a numeric label while the JSON
names carry no numbers and the contract itself says identity is name-keyed. The
number only exists in the md human summary headings.
**Fix:** Say "Standards, Tailoring & Process Models" instead of "cluster 30".

### IN-02: mil-std-881f single-cluster but no support-file rows

**Severity:** INFO
**File:** `docs/capability-pack-map.json` (cluster "Technical Planning & Work Breakdown")
**Issue:** mil-std-881f is 7/7 chapters in one cluster yet has no
`glossary.md/patterns.md/cheatsheet.md (support file)` rows, while mil-std-40051
and federal-bca (also single-cluster) do. Permitted by the rule ("included only
for essentially single-cluster" — necessary, not sufficient) and pre-named in the
plan, but the asymmetry is unexplained in the map; a one-line rationale would
prevent future rule drift.
**Fix:** Note the rationale in the md rules-of-construction or 8-01-SUMMARY.

### IN-03: "Regeneration byte-identical" idempotence evidence is not tool-reproducible

**Severity:** INFO
**File:** `.planning/phases/8-agent-enablement-surface/8-01-SUMMARY.md:124`
**Issue:** SC-1(b) no-diff evidence came from re-running the agent classification
pass — no script exists to reproduce it; only the gate-output determinism (SC-1a)
is tool-verifiable. The summary labels the two readings honestly, so this is
acceptable; Phase 9 wiring should treat the gate as the operational check.
**Fix:** None required; optionally record (b) as agent-attested, not gate-evidenced.

---

**Verdict rationale:** 0 blockers / 1 major. The major is a gate hardening gap
against a corruption mode the committed map does not exhibit; every must-have
truth in 8-01-PLAN.md was independently re-verified true. PASS_WITH_NOTES.

_Reviewed: 2026-08-17T00:35:00Z_
_Reviewer: ZCode (gsd-code-reviewer)_
_Depth: deep (diff scope)_

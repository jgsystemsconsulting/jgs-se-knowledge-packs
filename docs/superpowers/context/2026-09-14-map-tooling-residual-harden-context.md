# Context: map-tooling-residual-harden (2026-09-14)

## Context brief

**Primary question**: Close the three residual map-tooling holes left after Phase 21 (WR-01 cluster_names, WR-02 rules-vs-map date, WR-03 md freshness) in one stdlib-only slice.

**Sub-questions**:
1. Current data flow: rules + overrides -> generate_map -> JSON + optional render_md; --check; check_release replay.
2. Exact code for each WR hole (quoted, with live line refs).
3. Date-field semantics (`generated_on` on rules and map; local `disk_on`).
4. How byte-stable / object-stable replay is proven today.
5. Package constraints + design choices the spec must settle per WR.

**Success criteria**: SC1 data flow; SC2 WR quotes; SC3 date fields; SC4 replay proof; SC5 design constraints.

**Out of scope** (packages.md P7): version trio / CHANGELOG / tag / gh release; CONTRACT rewrite (done in Phase 21); GAP.md ledger refresh (P8); pack content or new packs; CI changes (P4/P5); no `validate.yml` repo-Python step.

**Budget**: single-pass context gate.

**Workspace baseline**: HEAD `35c5e3adb34974fa9933232343c064d39f7fdfa9` on `main`.

**Parent-verified package facts** (packages.md P7): Phase 21 closed pack/chapter/note path guards and folded generator `--check` into `check_release`; residuals WR-01/02/03 sit on generator, md render, and release-replay; one slice closes them; stdlib-only.

## Findings

Grades: CORROBORATED 9, SINGLE-SOURCE 6, CONFLICTED 0, STALE 2 (IMPL_REVIEW / package line refs drifted after later check_release growth).

| # | Claim | Grade |
|---|-------|-------|
| 1 | `generate_map` accepts any non-empty string cluster_names; no `\|`/CR/LF reject | CORROBORATED |
| 2 | `render_md` injects `cluster['name']` unescaped at Summary row and `##` heading | CORROBORATED |
| 3 | pack/chapter/note already reject CR/LF; pack/chapter/note escape `\|` in render | CORROBORATED |
| 4 | `check_rules` cluster_names shape matches generator (non-empty strings only) | CORROBORATED |
| 5 | map-replay reads map `generated_on` into local `disk_on` and feeds it to `--check` | CORROBORATED |
| 6 | `check_rules` fidelity compares map_version, cluster names, keys, is_support; not dates | CORROBORATED |
| 7 | `--check` compares JSON objects only; returns before any md work | CORROBORATED |
| 8 | No check_release step compares capability-pack-map.md | CORROBORATED |
| 9 | RR-B-30 packs.html is the existing render-and-compare precedent | CORROBORATED |
| 10 | Both rules and map carry `generated_on: "2026-08-27"` today (agree live) | CORROBORATED |
| 11 | There is no on-disk field named `disk_on`; only the check_release local | SINGLE-SOURCE |
| 12 | IMPL_REVIEW cites check_release.py:264-273; live replay is ~L308-343 | STALE |
| 13 | Package evidence cites check_release.py:284-285; live `disk_on` is L321 | STALE |
| 14 | P7 in_scope/out_scope as ledger; stdlib-only already true | CORROBORATED |
| 15 | Fail tags already in use: `[map]`, `[map-replay]`, `[classification-rules]`, `[rr-b-30]` | SINGLE-SOURCE |

## Current data flow

```
docs/classification-rules.json     (schema 1; map_version; generated_on; cluster_names; assignments)
docs/capability-pack-map-note-overrides.json  (schema 1; notes[644])
        |
        v
generate_capability_map.generate_map(rules, overrides, generated_on_cli)
        |
        +--> docs/capability-pack-map.json   (schema 2; map_version; generated_on; clusters[])
        |
        +--> [optional --sync-md]
               render_md(built, header_prefix from on-disk md up to "## Summary")
               --> docs/capability-pack-map.md  (human header kept; Summary + cluster tables rewritten)
```

**CLI modes** (`tooling/generate_capability_map.py`):

| Mode | Behavior |
|------|----------|
| `--generated-on DATE` (required always) | Build map; write JSON. No wall-clock default. |
| `+ --sync-md` | Also rewrite md Summary/tables. Illegal with `--check`. |
| `+ --check` | Build in memory; load on-disk JSON; `built != disk` object compare; write nothing. |

**check_release local/trusted chain** (map-related only):

| Step | Tag | Tool | Role |
|------|-----|------|------|
| 5e | `[map]` | `check_capability_map.main()` | Live map envelope, pack/chapter existence, thresholds |
| 5f | `[classification-rules]` | `check_classification_rules.main()` | Rules shape + live-chapter coverage + rules-vs-map fidelity |
| 5g | `[map-replay]` | `generate_capability_map.main(["--generated-on", disk_on, "--check"])` | Generator replay vs on-disk JSON |

CI (`.github/workflows/validate.yml`) never executes repo Python. P7 must not add a validate.yml repo-Python step.

## Exact current state (quoted)

### WR-01 — cluster_names unvalidated / unescaped

**Validation today** (`generate_capability_map.py` L77-83): non-empty strings only.

```python
cluster_names = rules.get("cluster_names")
if (
    not isinstance(cluster_names, list)
    or not cluster_names
    or not all(isinstance(n, str) and n for n in cluster_names)
):
    raise ValueError("rules cluster_names must be a non-empty list of strings")
```

**Contrast**: pack/chapter already reject CR/LF (L121-124); notes reject CR/LF on pack/chapter/note (L168-173). No equivalent on cluster_names.

**Mirror in check_rules** (`check_classification_rules.py` L91-97): same non-empty-string shape; no pipe/CR/LF reject.

**Render hole** (`generate_capability_map.py` L257-265, L270-273):

```python
for i, cluster in enumerate(clusters, start=1):
    n = len(cluster["chapters"])
    total += n
    lines.append(f"| {i}. {cluster['name']} | {n} |")
# ...
for i, cluster in enumerate(clusters, start=1):
    lines.append(f"## {i}. {cluster['name']}")
# ...
pack = _deslop(ch["pack"]).replace("|", "\\|")
chapter = _deslop(ch["chapter"]).replace("|", "\\|")
note = _deslop(ch["note"]).replace("|", "\\|")
```

`cluster['name']` is not `_deslop`'d and not pipe-escaped. IMPL_REVIEW verified live: name `A|B` or `X\nINJECTED` passes generate_map and check_rules; md table/heading breaks; gates stay green because nothing validates the md.

### WR-02 — map-replay date truth source is the map itself

**check_release 5g** (live L308-336; local name `disk_on`):

```python
map_obj = json.loads(map_path.read_text(encoding="utf-8"))
# ...
disk_on = map_obj.get("generated_on")
if not isinstance(disk_on, str) or not disk_on:
    fail(errs, "[map-replay] capability-pack-map.json missing generated_on")
else:
    rc = generate_capability_map.main(
        ["--generated-on", disk_on, "--check"]
    )
```

By construction, the date fed to the generator equals the map envelope date, so replay cannot fail on date drift.

**check_rules fidelity** (L238-277 region): compares `schema_version`, `map_version`, ordered `cluster_names` vs `clusters[].name`, signpost list, (pack, chapter) key-sets, per-row cluster and is_support. **Does not** compare `rules.generated_on` to `live.generated_on`. Shape-check only validates each file's own `generated_on` against `YYYY-MM-DD` (rules L63-67; map via check_capability_map L83-89).

### WR-03 — capability-pack-map.md has no freshness gate

**`--check` path** (`generate_capability_map.py` L332-349):

```python
if args.check:
    try:
        disk = _load_json(MAP_PATH, "map")
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1
    if built != disk:
        print("FAIL: generated map does not match on-disk capability-pack-map.json")
        # ... envelope key diffs ...
        return 1
    print("PASS: generated map matches on-disk capability-pack-map.json")
    return 0
```

Returns before any md read. `--sync-md` is optional write-only. check_release has no md step for this artifact.

**Precedent**: RR-B-30 packs.html (`check_release.py` L206-221) renders fresh and compares `fresh != ph`.

## Date-field semantics

| Symbol | Where | Owner / meaning |
|--------|-------|-----------------|
| `generated_on` | `docs/classification-rules.json` envelope | Rules authoring date (YYYY-MM-DD). Shape-checked by `check_classification_rules`. Live value: `2026-08-27`. |
| `generated_on` | `docs/capability-pack-map.json` envelope | Map envelope date written by generator from `--generated-on` CLI. Shape-checked by `check_capability_map`. Live value: `2026-08-27`. |
| `disk_on` | local var only in `check_release` 5g | `map_obj.get("generated_on")`; fed back into generator `--check`. Not a JSON field. |
| `--generated-on` | generator CLI (required) | Sole write-path date input. No wall-clock default. Validated `YYYY-MM-DD` + real calendar date. |

There is no separate `disk_on` field on disk. Content fidelity (membership, cluster assignment, notes) is gated independently of the date. Date drift is metadata-only today and currently ungated across rules vs map.

## How the repo proves replay today

1. **JSON object equality, not raw bytes**: `--check` builds `built = generate_map(...)`, loads `disk` via `json.load`, then `built != disk`. Order-sensitive because generator emits insertion-ordered clusters matching `cluster_names` and dumps with `json.dumps(..., indent=2, ensure_ascii=False) + "\n"` (`dumps_map`).
2. **Date is an input, not derived**: caller must pass `--generated-on`; check_release chooses the map's own date, so envelope date always matches under 5g.
3. **Write path is deterministic given inputs**: same rules + overrides + generated_on -> same object -> same pretty JSON text under `dumps_map`.
4. **md is not in the replay loop**: header prefix is taken from the live md file (text before `## Summary`); body is pure function of `map_obj`. Without a compare step, stale body after JSON-only regen is invisible.
5. **Sibling checkers do not import the generator** (H-07): check_capability_map and check_classification_rules load JSON independently. Replay is the only path that re-executes generate_map.

## Package constraints

From packages.md P7 + live tooling:

- **in_scope**: reject `|` / CR / LF in `cluster_names` in `generate_map` and `check_rules`; escape names in `render_md`; cross-check rules `generated_on` vs live map (or feed rules date into map-replay); extend `--check` (or check_release) to compare rendered md to on-disk `capability-pack-map.md`.
- **out_scope**: website YAML (P1 done); version trio / CHANGELOG / tag / gh release; CONTRACT rewrite; GAP.md (P8); pack content / new packs; CI changes (P4/P5).
- **Hard**: stdlib-only; no `validate.yml` repo-Python step; generator must not import sibling checkers.
- **Fail-closed idioms**: keep existing tags (`[map-replay]`, `[classification-rules]`, generator `FAIL:` / `PASS:` prints). New messages should name the field and side (rules vs map, generated vs disk) the way envelope diffs already do.

## Design considerations the spec must settle

### WR-01 (cluster_names)

1. **Validation points**: both `generate_map` (raises `ValueError`, named field) and `check_rules` (appends envelope error). Mirror pack/chapter/note style: reject if `"|" in n or "\n" in n or "\r" in n`.
2. **Escape mechanism**: defense in depth in `render_md`: at minimum `.replace("|", "\\|")` on the name used in the Summary cell; heading line is not a table cell but CR/LF must already be rejected upstream so a multi-line heading cannot appear. Optional `_deslop` for consistency with pack/chapter/note (live names have no em dash today).
3. **Do not** invent a new cluster-name schema field; keep the existing `cluster_names: list[str]` shape.

### WR-02 (date cross-check)

1. **Option A (fidelity home)**: in `check_rules` fidelity block, fail when `live.get("generated_on") != generated_on` (rules). Natural: fidelity already owns rules-vs-map agreement (`map_version`, names, keys).
2. **Option B (replay home)**: load rules `generated_on` in check_release 5g and pass that to `--check` instead of `disk_on`. Then date mismatch fails via existing envelope diff print in `--check`.
3. **Option C**: both. Redundant but belt-and-suspenders; ponytail prefers one home.
4. Spec should pick **one primary home**. IMPL_REVIEW recommends fidelity as the more natural home; package allows either.
5. Do not add a second date field. Keep the single name `generated_on` on both files.

### WR-03 (md freshness)

1. **Option A (`--check` owns it)**: after JSON match, if `MD_PATH` missing fail; else `render_md(built, _split_md_header(existing))` and compare to full on-disk text; fail on mismatch. Automatically covered by check_release 5g.
2. **Option B (check_release owns it)**: new step beside 5g, modeled on RR-B-30 packs.html. Duplicates render call unless it reuses generator helpers.
3. Prefer **Option A**: one tool, one freshness definition, 5g stays the single map-replay entry. Keep write path (`--sync-md`) unchanged.
4. Missing `## Summary` must stay fail-closed (existing `_split_md_header` behavior).
5. Compare full md text (header prefix + rendered body), not body alone, so accidental header edits that break the split still surface; header is preserved verbatim from disk on write, so a clean tree compares equal.

### Cross-cutting

1. No CI edits. Local/trusted only.
2. No pack content, CONTRACT, CHANGELOG, version trio, tag.
3. Keep generator free of checker imports.
4. Failure UX: generator keeps `FAIL:` / `PASS:` lines; check_release keeps `[map-replay]` wrapper. If fidelity gains the date check, message shape `fidelity: rules generated_on {a!r} != live map {b!r}`.
5. Tests: repo has no pytest mandate for this slice; optional assert-style probes ok if already used nearby; do not add frameworks.

## Synthesis

SC1-SC5 covered. All three WR holes exist as described on current main. Spec must (1) add cluster_name reject + escape, (2) pick date cross-check home (fidelity vs replay feed), (3) add md render-compare preferably inside `--check`. Minimum fix is three small edits on the same generator/checker/release surfaces Phase 21 already owns.

## Evidence index

| Loc | Kind |
|-----|------|
| tooling/generate_capability_map.py:54-227 | code (generate_map) |
| tooling/generate_capability_map.py:77-83 | code (WR-01 validation hole) |
| tooling/generate_capability_map.py:245-276 | code (render_md; WR-01 escape hole L260,265) |
| tooling/generate_capability_map.py:287-370 | code (CLI; WR-03 --check L332-349) |
| tooling/check_release.py:286-343 | code (5e/5f/5g; WR-02 disk_on L321-329) |
| tooling/check_release.py:206-221 | code (RR-B-30 packs.html precedent) |
| tooling/check_classification_rules.py:63-67 | code (rules generated_on shape) |
| tooling/check_classification_rules.py:91-97 | code (WR-01 check_rules hole) |
| tooling/check_classification_rules.py:218-277 | code (fidelity; no date compare) |
| tooling/check_capability_map.py:83-89 | code (map generated_on shape) |
| docs/classification-rules.json | data (generated_on, cluster_names) |
| docs/capability-pack-map.json | data (generated_on, clusters[].name) |
| docs/capability-pack-map.md | data (Summary table cells) |
| .planning/phases/21-.../21-IMPL_REVIEW.md:76-92 | doc (WR-01/02/03) |
| docs/superpowers/packages/2026-09-14-jgs-se-knowledge-packs-packages.md P7 | doc (in/out scope) |

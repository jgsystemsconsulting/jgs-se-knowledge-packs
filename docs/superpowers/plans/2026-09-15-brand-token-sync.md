# Brand Token Sync (P13) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `docs/index.html` the single source of truth for the brand token block (four `@font-face` rules plus the `:root` variables), have the packs-page generator copy that block verbatim at render time, and lock the parity with a CI-covered `[brand-tokens]` assertion; the dead `--ink-4` token is deleted on the way.

**Architecture:** Explicit `/* BRAND-TOKENS:BEGIN ... :END */` marker comments wrap the token block in `docs/index.html`. `tooling/gen_packs_page.py` extracts the exclusive interior with `brand_tokens()` and splices it into the template through a literal placeholder, so the f-string never sees single-brace CSS. The `[html-assets]` self-containment check in `tooling/check_release.py` gains an inline extract-and-substring assertion (`[brand-tokens]`) that is mirrored in the `.github/workflows/validate.yml` heredoc, with byte parity pinned in `tooling/test_ci_gate.py` (`HTML_ASSET_PAIR`), the same three-file twin pattern P12 used.

**Tech Stack:** Python 3 stdlib only (repo tooling convention), GitHub Actions inline python3 heredocs, plain HTML/CSS. No new dependencies, no CSS parsing, no test framework (assert-based probes).

**Spec:** docs/superpowers/specs/2026-09-15-brand-token-sync.md

**Research:** research: skipped (in-repo CSS token sync; no external API)

## Global Constraints

- `docs/index.html` is the single source of truth for brand tokens. Edit there first.
- `docs/packs.html` is generated output; never hand-edit it (RR-B-00). Regenerate with `python tooling/gen_packs_page.py` and commit both sides of a token change.
- No new colors, no new font families, no CDN. The only value change in this package is deleting `--ink-4`.
- The marker contract is the **exclusive interior**: the text between the BEGIN line and the END line, neither marker comment line included. Exactly one BEGIN and one END, BEGIN before END; missing, duplicated, reversed, or unbalanced markers are errors.
- `brand_tokens()` raises a plain `ValueError` (an `Exception`), never `sys.exit`/`SystemExit`, so importers (`check_release.py` rr-b-30) see a normal exception. Only the CLI `__main__` path catches it, prints to stderr, and exits nonzero.
- CI never executes checkout repo code: the gate's brand-token extract is inlined in `check_release.py` and again in the `validate.yml` heredoc. Do not import `gen_packs_page` from CI surfaces.
- The three surfaces (`gen_packs_page.py`, `check_release.py`, `validate.yml` heredoc) duplicate the extraction algorithm by convention, exactly like the existing html-assets twin; `test_ci_gate.py` pins the marker literals byte-for-byte.
- Masthead and footer chrome stay hand-mirrored between the two sources (only DOC-ID and REV differ legitimately); this package adds a one-line mirror note, no lock.
- All tooling stays stdlib-only; emitted copy stays em-dash-free (RR-B-28); commands run from the repo root with `python` on Windows Git Bash.

## Codebase context

- `docs/index.html:25-41`: the `Self-hosted brand fonts` comment (stays outside the contract), the four `@font-face` rules (lines 27-30), a blank line (31), and the `:root` block (32-41) containing `--ink-4:#1e2024` on line 33. `<style>` opens at line 24.
- `docs/index.html:106-112`: the masthead block (`<!-- §00 Masthead -->` then `<div class="mast">`).
- `tooling/gen_packs_page.py:18`: `ROOT = Path(__file__).resolve().parent.parent` (the root resolution pattern `brand_tokens()` reuses). Lines 93-106: the hardcoded `@font-face` x4 plus `:root` block inside the `render()` f-string, braces doubled. Lines 151-156: the template masthead. Lines 224-225: `if __name__ == "__main__": raise SystemExit(main())`.
- `tooling/check_release.py:365-376`: check 12 (`[html-assets]`), the per-page scan loop the `[brand-tokens]` assertion extends. Check 5c (`rr-b-30`, lines 346-363) imports `gen_packs_page` and calls `render()`; it already wraps that call in `try/except Exception`.
- `.github/workflows/validate.yml:132-243`: the pinned step `HTML self-containment` with its `python3 - <<'PY' ... PY` heredoc (10-space body indentation).
- `tooling/test_ci_gate.py:61-78`: `HTML_ASSET_PAIR`, the byte-parity pin list. Lines 218-226: `HTML_CLEAN_PAGE`, the positive fixture page. Lines 362-377: the html-assets negative demos and the `html-clean-ok` positive demo. Lines 379-384: real-tree positive runs of every pinned heredoc.
- `var(--ink-4)` appears in zero CSS rules on either page; the token is defined three times and used never (verified 2026-09-15).

---

### Task 1: Markers, dead-token deletion, and mast mirror note in docs/index.html

**Files:**
- Modify: `docs/index.html` (style block lines 24-41, masthead line 106-107)

**Interfaces:**
- Consumes: nothing.
- Produces: the marker lines `/* BRAND-TOKENS:BEGIN (single source; tooling/gen_packs_page.py copies this verbatim) */` and `/* BRAND-TOKENS:END */` around the exclusive token slice that Task 2 extracts and Task 3 asserts against. The slice is the four `@font-face` rules, the blank line, and the `:root` block with `--ink-4` removed.

**Model:** flash

- [ ] **Step 1: Run the failing marker check**

```bash
python - <<'PY'
from pathlib import Path
t = Path("docs/index.html").read_text(encoding="utf-8")
lines = t.splitlines()
b = [i for i, ln in enumerate(lines) if ln.startswith("/* BRAND-TOKENS:BEGIN")]
e = [i for i, ln in enumerate(lines) if ln.startswith("/* BRAND-TOKENS:END")]
assert len(b) == 1 and len(e) == 1 and b[0] < e[0], f"markers wrong: BEGIN={b} END={e}"
assert "--ink-4" not in t, "--ink-4 still present"
assert "hand-mirrored in tooling/gen_packs_page.py" in t, "mast mirror note missing"
print("index.html brand contract OK")
PY
```

Expected: `AssertionError: markers wrong: BEGIN=[] END=[]`

- [ ] **Step 2: Wrap the token block in markers**

In `docs/index.html`, insert one line immediately before the first `@font-face` (after the existing two-line `Self-hosted brand fonts` comment, which stays outside the contract) and one line immediately after the `:root` closing brace. The `:root` block lines are shown here in full with the marker lines added; the only other change is Step 3.

```css
/* BRAND-TOKENS:BEGIN (single source; tooling/gen_packs_page.py copies this verbatim) */
@font-face{font-family:'JetBrains Mono';src:url('fonts/JetBrainsMono-Regular.woff2') format('woff2');font-weight:400;font-display:swap}
@font-face{font-family:'JetBrains Mono';src:url('fonts/JetBrainsMono-Bold.woff2') format('woff2');font-weight:700;font-display:swap}
@font-face{font-family:'Inter';src:url('fonts/Inter-Regular.woff2') format('woff2');font-weight:400;font-display:swap}
@font-face{font-family:'Inter';src:url('fonts/Inter-SemiBold.woff2') format('woff2');font-weight:600;font-display:swap}

:root{
  --ink:#0a0a0b; --ink-2:#111113; --ink-3:#16171a;
  --line:#2a2d33; --line-2:#3a3e46;
  --mute:#6b7078; --mute-2:#8b9099;
  --text:#c7ccd3; --text-hi:#e8ebf0;
  --paper:#f4f2ec; --paper-ink:#0a0a0b;
  --mono:'JetBrains Mono',ui-monospace,'SFMono-Regular',Menlo,Consolas,monospace;
  --sans:'Inter',ui-sans-serif,system-ui,sans-serif;
  --pad-x:clamp(24px,4vw,80px); --pad-section:clamp(48px,6vw,96px);
}
/* BRAND-TOKENS:END */
```

- [ ] **Step 3: Delete the dead --ink-4 token**

In the `:root` first line inside the markers, change

```css
  --ink:#0a0a0b; --ink-2:#111113; --ink-3:#16171a; --ink-4:#1e2024;
```

to

```css
  --ink:#0a0a0b; --ink-2:#111113; --ink-3:#16171a;
```

Nothing else in the block changes. (Done in the block shown in Step 2 if applied as one edit.)

- [ ] **Step 4: Add the mast mirror note**

Above `<div class="mast"><div class="wrap">` (directly under `<!-- §00 Masthead -->`), insert exactly one line:

```html
<!-- Masthead and footer chrome stay hand-mirrored in tooling/gen_packs_page.py; only the BRAND-TOKENS block auto-syncs. -->
```

- [ ] **Step 5: Rerun the check and the unused-token grep**

Run: the same heredoc as Step 1.
Expected: `index.html brand contract OK`

Run: `grep -n "ink-4" docs/index.html`
Expected: no output, exit 1.

Run: `python -c "import pathlib; t = pathlib.Path('docs/index.html').read_text(encoding='utf-8'); i = t.index('BRAND-TOKENS:BEGIN'); print('slice head:', t[t.index(chr(10), i)+1:t.index(chr(10), i)+40])"`
Expected: `slice head: @font-face{font-family:'JetBrains Mono';src:url('fonts/JetBrainsM` (confirms the exclusive interior starts at the first `@font-face`, not the marker).

- [ ] **Step 6: Commit**

```bash
git add docs/index.html
git commit -m "feat: BRAND-TOKENS markers in index.html, drop dead --ink-4 (P13)"
```

---

### Task 2: brand_tokens() extraction and splice in the generator, regenerate packs.html

**Files:**
- Modify: `tooling/gen_packs_page.py` (module docstring line 4-12, template lines 92-106, template masthead line 151, `__main__` lines 224-225)
- Modify (generated): `docs/packs.html` (regenerated, never hand-edited)

**Interfaces:**
- Consumes: the marker lines and exclusive slice from Task 1.
- Produces: `gen_packs_page.BRAND_BEGIN` and `gen_packs_page.BRAND_END` (string constants `"/* BRAND-TOKENS:BEGIN"` and `"/* BRAND-TOKENS:END"`), `gen_packs_page.slice_brand_tokens(text: str) -> str` (pure, raises `ValueError`), `gen_packs_page.brand_tokens() -> str` (reads `docs/index.html`, wraps the slice), and `render(rows, ver)` now splicing the slice into the page. Task 3's gate deliberately does not import these; it inlines its own copy.

**Model:** flash

- [ ] **Step 1: Write the failing slice demo**

```bash
python - <<'PY'
import sys
sys.path.insert(0, "tooling")
import gen_packs_page as g
toks = g.brand_tokens()
assert toks.startswith("@font-face"), repr(toks[:60])
assert ":root{" in toks and "--ink-4" not in toks
assert "BRAND-TOKENS" not in toks, "marker lines must stay outside the slice"
src = open("docs/index.html", encoding="utf-8").read()
lines = src.splitlines()
no_begin = "\n".join(l for l in lines if not l.startswith(g.BRAND_BEGIN))
no_end = "\n".join(l for l in lines if not l.startswith(g.BRAND_END))
dup = src.replace(g.BRAND_END, g.BRAND_END + "\n" + g.BRAND_END, 1)
# BEGIN line moved after the END line: count passes (1/1), order check must fire
kept = [l for l in lines if not l.startswith(g.BRAND_BEGIN)]
reversed_ = "\n".join(kept + [l for l in lines if l.startswith(g.BRAND_BEGIN)])
for label, bad in (("no-begin", no_begin), ("no-end", no_end),
                   ("duplicate", dup), ("reversed", reversed_)):
    try:
        g.slice_brand_tokens(bad)
    except ValueError:
        pass
    else:
        raise AssertionError(f"{label}: expected ValueError")
print("brand slice demos OK")
PY
```

Expected: `ImportError: cannot import name 'gen_packs_page'` is not possible (module exists), so the first failure is `AttributeError: module 'gen_packs_page' has no attribute 'brand_tokens'`.

- [ ] **Step 2: Add the constants and the two functions**

In `tooling/gen_packs_page.py`, directly after the `version()` function (before `REPO = ...`), add:

```python
BRAND_BEGIN = "/* BRAND-TOKENS:BEGIN"
BRAND_END = "/* BRAND-TOKENS:END"
BRAND_PLACEHOLDER = "__BRAND_TOKENS__"


def slice_brand_tokens(text: str) -> str:
    """Exclusive interior between the BRAND-TOKENS BEGIN and END marker lines.

    docs/index.html is the single source of truth for brand tokens (P13); the
    BEGIN and END comment lines themselves are not part of the slice. Raises
    ValueError (a plain Exception, never SystemExit) on missing, duplicated,
    reversed, or unbalanced markers so importers of brand_tokens()/render()
    (tooling/check_release.py rr-b-30) see a normal exception.
    """
    lines = text.splitlines()
    begins = [i for i, ln in enumerate(lines) if ln.startswith(BRAND_BEGIN)]
    ends = [i for i, ln in enumerate(lines) if ln.startswith(BRAND_END)]
    if len(begins) != 1 or len(ends) != 1:
        raise ValueError(
            f"expected exactly one BRAND-TOKENS BEGIN and one END marker line, "
            f"found {len(begins)} BEGIN / {len(ends)} END"
        )
    if begins[0] >= ends[0]:
        raise ValueError("BRAND-TOKENS:BEGIN must precede BRAND-TOKENS:END")
    return "\n".join(lines[begins[0] + 1:ends[0]])


def brand_tokens() -> str:
    """The brand-token block copied verbatim from docs/index.html."""
    index = ROOT / "docs" / "index.html"
    return slice_brand_tokens(index.read_text(encoding="utf-8"))
```

Also append one sentence to the module docstring (after the sentence ending "Regenerate after any pack/SKILLS.md change so it cannot drift (RR-B-00)."):

```
Brand tokens (fonts plus :root) are not stored here: they are extracted from the
BRAND-TOKENS marker block in docs/index.html at render time (P13).
```

- [ ] **Step 3: Replace the hardcoded template block with the placeholder**

In the `render()` f-string, delete the twelve lines from the first `@font-face` through the `:root` closing braces (currently lines 93-106, all with doubled braces) and put the placeholder in their place. The top of the template `<style>` becomes:

```python
<style>
__BRAND_TOKENS__
*{{box-sizing:border-box}}
```

The placeholder is a bare literal inside the f-string (no braces), so nothing needs escaping; the single-brace CSS arrives already formatted via `replace`.

- [ ] **Step 4: Splice the slice in render() and harden the CLI**

`render()` currently ends with `return f"""<!doctype html>` and closes the template with `"""`. Make two edits with Edit on the file (the ellipsis below stands for the existing template body; do not retype it, the template stays byte-identical apart from the Step 3 placeholder swap and the mast note below):

Change the opening line

```python
    return f"""<!doctype html>
```

to

```python
    html_out = f"""<!doctype html>
```

and change the closing

```python
</body>
</html>
"""
```

to

```python
</body>
</html>
"""

    return html_out.replace(BRAND_PLACEHOLDER, brand_tokens())
```

Add the mast mirror note inside the template, directly above `<div class="mast"><div class="wrap">` (currently line 151):

```html
<!-- Masthead and footer chrome stay hand-mirrored in docs/index.html; only the BRAND-TOKENS block auto-syncs. -->
```

Replace the `__main__` block (currently lines 224-225) with:

```python
if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        print(
            "restore exactly one BRAND-TOKENS:BEGIN and one BRAND-TOKENS:END "
            "marker line in docs/index.html, then rerun",
            file=sys.stderr,
        )
        raise SystemExit(1) from e
```

(`SystemExit(0)` raised by a successful `main()` is not a `ValueError`, so the success path is untouched.)

- [ ] **Step 5: Rerun the slice demo**

Run: the same heredoc as Step 1.
Expected: `brand slice demos OK`

- [ ] **Step 6: Regenerate packs.html and inspect the diff**

Run: `python tooling/gen_packs_page.py`
Expected: `wrote docs\packs.html (14 packs)` (count is whatever `SKILLS.md` holds today; the point is success with no traceback).

Run: `git diff --stat docs/packs.html && git diff docs/packs.html | head -60`
Expected diff, and nothing else:
- the four `@font-face` lines and the `:root` block replaced by the extracted slice (same `@font-face` text, a blank line inserted before `:root`, and the `--ink-4:#1e2024;` fragment gone);
- one added HTML comment line above `<div class="mast">` (the mast mirror note).

- [ ] **Step 7: Freshness and release gate**

Run: `python tooling/check_release.py`
Expected: `RELEASE CHECK: PASS (v<current version> @ <short sha>)`. This exercises rr-b-30, which imports `render()` and now goes through `brand_tokens()`; `[brand-tokens]` does not exist yet (Task 3).

- [ ] **Step 8: Commit**

```bash
git add tooling/gen_packs_page.py docs/packs.html
git commit -m "feat: generator extracts brand tokens from index.html markers (P13)"
```

---

### Task 3: [brand-tokens] parity assertion in the gate, CI twin, and probe pins

**Files:**
- Modify: `tooling/check_release.py` (module constants near `FIRST_PARTY_HOSTS` line 108, new function after `scan_html_external_assets` line 233, check 12 after line 376, docstring item 12)
- Modify: `.github/workflows/validate.yml` (heredoc under `HTML self-containment`, lines 231-242; coverage-map comment line 20)
- Modify: `tooling/test_ci_gate.py` (`HTML_ASSET_PAIR` lines 61-78, module docstring lines 22-24, `HTML_CLEAN_PAGE` lines 218-226, html-assets demos lines 362-377)

**Interfaces:**
- Consumes: marker literals `"/* BRAND-TOKENS:BEGIN"` / `"/* BRAND-TOKENS:END"` from Task 2 (duplicated, not imported, in `check_release.py` and the heredoc); the regenerated `docs/packs.html` from Task 2 for real-tree runs.
- Produces: `[brand-tokens]` failure tag in both gate surfaces with the message naming the fix (`rerun tooling/gen_packs_page.py`); `HTML_ASSET_PAIR` entries `"/* BRAND-TOKENS:BEGIN"` and `"/* BRAND-TOKENS:END"` pinning both surfaces; `HTML_CLEAN_PAGE` fixture carrying a minimal marker block.

**Model:** standard

- [ ] **Step 1: Extend the probe first (the failing test)**

In `tooling/test_ci_gate.py`:

1. Append two entries to `HTML_ASSET_PAIR` (after the `meta twitter:image:src` entry):

```python
    ("brand-tokens BEGIN marker", '"/* BRAND-TOKENS:BEGIN"'),
    ("brand-tokens END marker", '"/* BRAND-TOKENS:END"'),
```

2. Extend the module docstring sentence (lines 22-24) from "and the meta image tokens must appear verbatim in both check_release.py and validate.yml (HTML_ASSET_PAIR)" to "and the meta image tokens plus the BRAND-TOKENS marker literals (P13) must appear verbatim in both check_release.py and validate.yml (HTML_ASSET_PAIR)".

3. Add a minimal marker block to `HTML_CLEAN_PAGE` so the positive fixture satisfies the coming assertion:

```python
HTML_CLEAN_PAGE = (
    '<!doctype html>\n'
    '<link rel="icon" href="data:image/svg+xml,%3Csvg '
    "xmlns='http://www.w3.org/2000/svg'%3E\">\n"
    '<link rel="canonical" href="https://jgsystemsconsulting.github.io/jgs-se-knowledge-packs/">\n'
    '<img src="https://github.com/jgs-se/asset/raw/main/og.png" alt="hero">\n'
    "<style>@font-face{src:url('fonts/Inter-Regular.woff2')}\n"
    '@import "css/site.css";</style>\n'
    "<style>/* BRAND-TOKENS:BEGIN (single source; tooling/gen_packs_page.py copies this verbatim) */\n"
    ":root{--ink:#0a0a0b;--paper:#f4f2ec}\n"
    "/* BRAND-TOKENS:END */</style>\n"
)
```

4. Add a shared slice constant right below it:

```python
BRAND_SLICE = ":root{--ink:#0a0a0b;--paper:#f4f2ec}\n"
```

5. Update the `html-clean-ok` demo to ship a `packs.html` carrying the same exclusive slice, and add two brand-tokens negative demos after it:

```python
        # html-assets: data URI, relative fonts/@import, and allowlisted hosts pass;
        # brand-token parity holds when packs.html carries the index.html slice
        demo_ok({"docs/index.html": HTML_CLEAN_PAGE,
                 "docs/packs.html": "<style>\n" + BRAND_SLICE + "</style>\n"},
                "HTML self-containment", "html-clean-ok")
        # brand-tokens: a hand-edited hex in the packs.html copy fails
        demo({"docs/index.html": HTML_CLEAN_PAGE,
              "docs/packs.html": "<style>:root{--ink:#0b0b0c;--paper:#f4f2ec}</style>\n"},
             "HTML self-containment",
             "[brand-tokens] docs/packs.html does not carry the index.html brand "
             "token block verbatim", "html-brand-drift")
        # brand-tokens: missing markers fail [brand-tokens], not a crash
        demo({"docs/index.html":
              "<!doctype html>\n<style>:root{--ink:#0a0a0b}</style>\n"},
             "HTML self-containment",
             "[brand-tokens] expected exactly one BRAND-TOKENS BEGIN",
             "html-brand-markers-missing")
```

(The two pre-existing negative demos `html-external-img` and `html-protocol-relative` keep their trees unchanged; they will now also print a `[brand-tokens]` line, which is harmless because `demo()` only asserts its expected substring and a nonzero exit.)

Run: `python tooling/test_ci_gate.py`
Expected: `AssertionError` from the parity loop: `... 'brand-tokens BEGIN marker' missing from check_release.py`.

- [ ] **Step 2: Add the extract and the assertion to check_release.py**

1. After the `FIRST_PARTY_HOSTS` assignment (line 108), add:

```python
# P13 brand-token markers; the same literals are pinned in test_ci_gate.HTML_ASSET_PAIR.
BRAND_BEGIN = "/* BRAND-TOKENS:BEGIN"
BRAND_END = "/* BRAND-TOKENS:END"
```

2. After `scan_html_external_assets` (after its `return found`), add the inlined extract. Same algorithm as `gen_packs_page.slice_brand_tokens`, duplicated by twin convention; the gate never imports generator code for CI-mirrored checks.

```python
def slice_brand_tokens(text: str) -> str:
    """Exclusive interior between the BRAND-TOKENS BEGIN and END marker lines
    in docs/index.html. Same algorithm as gen_packs_page.slice_brand_tokens,
    inlined by twin convention (this gate never imports generator code);
    raises ValueError on missing, duplicated, reversed, or unbalanced markers.
    """
    lines = text.splitlines()
    begins = [i for i, ln in enumerate(lines) if ln.startswith(BRAND_BEGIN)]
    ends = [i for i, ln in enumerate(lines) if ln.startswith(BRAND_END)]
    if len(begins) != 1 or len(ends) != 1:
        raise ValueError(
            f"docs/index.html: expected exactly one BRAND-TOKENS BEGIN and one END "
            f"marker line, found {len(begins)} BEGIN / {len(ends)} END"
        )
    if begins[0] >= ends[0]:
        raise ValueError(
            "docs/index.html: BRAND-TOKENS:BEGIN must precede BRAND-TOKENS:END"
        )
    return "\n".join(lines[begins[0] + 1:ends[0]])
```

3. In `main()`, immediately after the check 12 per-page loop (the `fail(errs, f"[html-assets] external asset in ...")` loop) and before `# 6. SKILLS.md entry count`, insert check 12b:

```python
    # 12b. brand-token parity (P13): the exclusive BRAND-TOKENS slice extracted
    #     from docs/index.html must appear verbatim in docs/packs.html. A miss
    #     means the generated page is stale against the token source of truth.
    try:
        index_html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        packs_text = (ROOT / "docs" / "packs.html").read_text(encoding="utf-8")
        brand_block = slice_brand_tokens(index_html)
        if brand_block not in packs_text:
            fail(errs, "[brand-tokens] docs/packs.html does not carry the index.html "
                       "brand token block verbatim; rerun tooling/gen_packs_page.py")
    except ValueError as e:
        fail(errs, f"[brand-tokens] {e}")
    except OSError as e:
        fail(errs, f"[brand-tokens] cannot read page: {e}")
```

(The broad `except Exception` around check 5c's `render()` call already absorbs a `ValueError` from `brand_tokens()` on a marker-broken tree, so no `SystemExit` can escape rr-b-30 either.)

4. In the module docstring, extend item 12: after "zero pages fails closed." append:

```
     Plus brand-token parity ([brand-tokens], P13): the exclusive BRAND-TOKENS
     slice extracted from docs/index.html must appear verbatim in
     docs/packs.html.
```

- [ ] **Step 3: Mirror the assertion in the CI heredoc**

In `.github/workflows/validate.yml`, inside the `HTML self-containment` heredoc, insert between the per-page `for page in pages:` loop and `if not fails:` (keep the 10-space body indentation exactly):

```python
          # P13 brand-token parity: the exclusive BRAND-TOKENS slice extracted
          # from docs/index.html must appear verbatim in docs/packs.html.
          # Marker literals are pinned by tooling/test_ci_gate.py HTML_ASSET_PAIR.
          BRAND_BEGIN = "/* BRAND-TOKENS:BEGIN"
          BRAND_END = "/* BRAND-TOKENS:END"

          def slice_brand_tokens(text: str) -> str:
              lines = text.splitlines()
              begins = [i for i, ln in enumerate(lines) if ln.startswith(BRAND_BEGIN)]
              ends = [i for i, ln in enumerate(lines) if ln.startswith(BRAND_END)]
              if len(begins) != 1 or len(ends) != 1:
                  raise ValueError(
                      f"expected exactly one BRAND-TOKENS BEGIN and one END marker line, "
                      f"found {len(begins)} BEGIN / {len(ends)} END"
                  )
              if begins[0] >= ends[0]:
                  raise ValueError("BRAND-TOKENS:BEGIN must precede BRAND-TOKENS:END")
              return "\n".join(lines[begins[0] + 1:ends[0]])

          try:
              index_html = pathlib.Path("docs/index.html").read_text(encoding="utf-8")
              packs_text = pathlib.Path("docs/packs.html").read_text(encoding="utf-8")
              brand_block = slice_brand_tokens(index_html)
              if brand_block not in packs_text:
                  print("::error::[brand-tokens] docs/packs.html does not carry the "
                        "index.html brand token block verbatim; rerun "
                        "tooling/gen_packs_page.py")
                  fails += 1
              elif not fails:
                  print("[brand-tokens] index.html brand block present in packs.html")
          except ValueError as e:
              print(f"::error::[brand-tokens] {e}")
              fails += 1
          except OSError as e:
              print(f"::error::[brand-tokens] cannot read page: {e}")
              fails += 1
```

Also update the coverage-map comment in the workflow header (line 20) from

```
#   HTML self-containment                      twins check_release 12 [html-assets] (literal twin (hosts + regex pins))
```

to

```
#   HTML self-containment                      twins check_release 12 [html-assets] (literal twin (hosts + regex pins)) plus [brand-tokens] (P13)
```

- [ ] **Step 4: Run the probe**

Run: `python tooling/test_ci_gate.py`
Expected: `ci-gate probe: OK (parity, extraction, negative demos, positive runs)`. The real-tree positive run of `HTML self-containment` executes the extended heredoc against the actual `docs/` (markers from Task 1, regenerated packs.html from Task 2), so this also proves the live parity.

- [ ] **Step 5: Run the release gate**

Run: `python tooling/check_release.py`
Expected: `RELEASE CHECK: PASS (v<version> @ <sha>)` with no `[brand-tokens]` line.

- [ ] **Step 6: Commit**

```bash
git add tooling/check_release.py .github/workflows/validate.yml tooling/test_ci_gate.py
git commit -m "feat: [brand-tokens] parity assertion in gate and CI twin with probe pins (P13)"
```

---

### Task 4: Full verification pass from the spec

**Files:**
- Modify: nothing durable. Steps 3-5 mutate tracked files and restore them from the commits made in Tasks 1-3.

**Interfaces:**
- Consumes: everything shipped in Tasks 1-3.
- Produces: the verification evidence the spec requires before this package is called done.

**Model:** flash

Run every command from the repo root. All four commands below come from spec Verification items 1, 2, 4, and 5; items 3 and 6 are Steps 3-6 and 8.

- [ ] **Step 1: Generator idempotence and diff shape**

Run: `python tooling/gen_packs_page.py && git diff --stat`
Expected: regeneration succeeds and `git diff` is empty (Tasks 1-3 already committed the correct generated page; rerunning changes nothing).

- [ ] **Step 2: Clean-tree release gate**

Run: `python tooling/check_release.py`
Expected: `RELEASE CHECK: PASS (v<version> @ <sha>)`.

- [ ] **Step 3: Negative demo, stale packs.html (spec 3, first half)**

```bash
python - <<'PY'
from pathlib import Path
p = Path("docs/packs.html")
t = p.read_text(encoding="utf-8")
p.write_text(t.replace("--ink:#0a0a0b", "--ink:#0b0b0c", 1), encoding="utf-8")
PY
python tooling/check_release.py; echo "exit=$?"
```

Expected: `RELEASE CHECK: FAIL` with a line `[brand-tokens] docs/packs.html does not carry the index.html brand token block verbatim; rerun tooling/gen_packs_page.py` and `exit=1`. Restore by rerunning the generator, exactly as the failure message says:

```bash
python tooling/gen_packs_page.py
git diff --stat
```

Expected: diff empty again.

- [ ] **Step 4: Negative demo, missing markers (spec 3, second half)**

```bash
python - <<'PY'
from pathlib import Path
p = Path("docs/index.html")
lines = [l for l in p.read_text(encoding="utf-8").splitlines()
         if not l.startswith("/* BRAND-TOKENS:BEGIN")
         and not l.startswith("/* BRAND-TOKENS:END")]
p.write_text("\n".join(lines) + "\n", encoding="utf-8")
PY
python tooling/gen_packs_page.py; echo "gen-exit=$?"
python tooling/check_release.py; echo "gate-exit=$?"
```

Expected: `gen-exit=1` with `ERROR: expected exactly one BRAND-TOKENS BEGIN and one END marker line, found 0 BEGIN / 0 END` on stderr and no traceback. The gate exits 1 having completed its full sweep (`RELEASE CHECK: FAIL` summary printed): a `[brand-tokens] docs/index.html: expected exactly one BRAND-TOKENS BEGIN ...` line is present, and no `SystemExit`/traceback aborts the run mid-check.

Restore, then verify restoration:

```bash
git checkout -- docs/index.html
python tooling/gen_packs_page.py
python tooling/test_ci_gate.py
```

Expected: probe prints `ci-gate probe: OK ...` again.

- [ ] **Step 5: Negative demo, unbalanced markers (BEGIN without END)**

```bash
python - <<'PY'
from pathlib import Path
p = Path("docs/index.html")
lines = [l for l in p.read_text(encoding="utf-8").splitlines()
         if not l.startswith("/* BRAND-TOKENS:END")]
p.write_text("\n".join(lines) + "\n", encoding="utf-8")
PY
python tooling/gen_packs_page.py; echo "gen-exit=$?"
python tooling/check_release.py; echo "gate-exit=$?"
git checkout -- docs/index.html
python tooling/gen_packs_page.py
```

Expected: same failure mode as Step 4 (`found 1 BEGIN / 0 END`), never a splice of the rest of the file; both exits are 1; after restore the generator succeeds.

- [ ] **Step 6: Probe with the extended pair pin and fixtures**

Run: `python tooling/test_ci_gate.py`
Expected: `ci-gate probe: OK (parity, extraction, negative demos, positive runs)`.

- [ ] **Step 7: Dead token gone everywhere**

Run: `grep -rn "ink-4" docs/index.html docs/packs.html tooling/gen_packs_page.py`
Expected: no output, exit 1.

- [ ] **Step 8: Visual check (spec 6)**

Open `docs/index.html` and `docs/packs.html` in a local browser. Expected: both pages render identically to before; the only content delta anywhere is the removed dead token (invisible) and the added HTML comments (invisible). This is a human or Playwright spot check; if automation is preferred, compare the computed `:root` style of `<html>` on both pages for equality and for absence of `--ink-4`.

- [ ] **Step 9: Confirm clean tree**

Run: `git status --porcelain`
Expected: empty. No commit is needed in this task; every negative demo was restored and the committed state is the deliverable.

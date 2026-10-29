<!--
Copyright (c) 2026 JG Systems Consulting Ltd. MIT License (see LICENSE).
SPDX-License-Identifier: MIT
-->

# Source Freshness

The catalogue's 74 live content packs were each built from one upstream document.
A content pack may pin more than one PDF when the publisher ships the document
in parts (see the build rules in [PACK-SPEC.md](PACK-SPEC.md)). The watchlist
stays one entry per live catalog pack, not one entry per PDF. Those documents
get revised, and a pack does not notice on its own. This watch checks, monthly,
whether the revision a pack was built from is still the revision the publisher
offers.

## What it checks

`docs/source-watchlist.json` holds one entry per live catalog pack: the slug, the
publisher, the document identifier, the revision last recorded as observed
upstream, the date of that observation, and an optional hint. It carries no URLs.
Source URLs are not stored in tracked files; the monthly run finds the publisher's
current page by web search at run time.

The check compares the recorded revision string with the revision identifier the
publisher states. It does not parse dates out of the version string, and it does
not guess. A date-only difference inside an otherwise identical revision
identifier counts as no change.

## Cadence and where the output goes

The run is monthly. Reports land at `.zcode/source-watch/YYYY-MM-DD.md`, which is
gitignored, and they accumulate. Each report lists drift findings, unknowns, packs
whose recorded revision is ahead of what the pack was built from, and three
report-only glances: live link health, the README version badge against
`RELEASE-INFO.txt`, and the status of `planned[]` entries.

## The watch never edits a pack

A drift finding is information for the maintainer. Rebuilding a pack stays a human
decision, made from the report. The automation writes no tracked file except
through `tooling/check_source_watch.py --record`, which updates the watchlist's
bookkeeping and nothing else. The pack's `PACK.yaml` keeps the revision the pack
was built from.

## Recording a revision by hand

A source that stays unknown across runs needs a person to look it up. Once the
revision is confirmed, record it:

```bash
python tooling/check_source_watch.py --record <slug> "<revision>" <YYYY-MM-DD>
```

There is no accept-stale option. An entry left with an empty `last_checked` fails
the release gate's source-watch check (check 18 in `tooling/check_release.py`,
listed at line 60, called at lines 1313-1321). The check is local only and is not
mirrored into CI. That is the point: a tag cut over an unwatched catalogue should
be blocked locally.

`python tooling/check_source_watch.py` validates the watchlist and reports. It
never writes and it never fetches anything.

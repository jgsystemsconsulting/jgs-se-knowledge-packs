import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import eval as ev  # noqa: E402


def agg(slug="nasa-risk", status="PASS"):
    return {"slug": slug, "status": status,
            "verdicts": {"a": "PASS", "b": "FAIL"},
            "dispositions": {"a": "NONE", "b": "QUARANTINE"},
            "trend": {"a": 5.0, "b": 0.0},
            "canary_load_bearing": True}


class TestReport(unittest.TestCase):
    def test_report_shows_denominator(self):
        md = ev.render_report([agg()], suite="INCOMPLETE", total_packs=13,
                              judge_model="claude-x", bank_sha="abc123")
        self.assertIn("1/13", md)
        self.assertIn("INCOMPLETE", md)

    def test_report_lists_failures_first(self):
        # Two packs: one FAIL, one PASS. The FAIL pack's heading must appear before the
        # PASS pack's heading. (Do NOT assert on a bare letter like "b" — it matches the
        # 'b' in a bank_sha and passes vacuously.)
        fail_pack = agg(slug="pack-fail", status="FAIL")
        pass_pack = agg(slug="pack-pass", status="PASS")
        pass_pack["verdicts"] = {"a": "PASS"}
        pass_pack["dispositions"] = {"a": "NONE"}
        pass_pack["trend"] = {"a": 5.0}
        md = ev.render_report([pass_pack, fail_pack], suite="FAIL", total_packs=13,
                              judge_model="claude-x", bank_sha="0000000")
        self.assertLess(md.index("### pack-fail"), md.index("### pack-pass"))
        self.assertIn("FAIL", md)

    def test_quarantine_digest_has_no_source_quotations(self):
        recs = [{"id": "b", "canary": False,
                 "answer": "SECRET SOURCE TEXT THAT MUST NOT LEAK",
                 "judge": {"faithfulness": 2, "routing": 5, "completeness": 5,
                           "triggering": None, "unmapped_claims": ["foo"],
                           "must_not_include_hits": ["bad"], "must_use_terms_missing": []}}]
        digest = ev.render_quarantine("nasa-risk", recs)
        self.assertIn("b", digest)
        self.assertIn("QUARANTINE", digest)
        self.assertNotIn("SECRET SOURCE TEXT", digest)

    def test_quarantine_digest_empty_when_nothing_to_review(self):
        recs = [{"id": "a", "canary": False, "answer": "x",
                 "judge": {"faithfulness": 5, "routing": 5, "completeness": 5,
                           "triggering": None, "unmapped_claims": [],
                           "must_not_include_hits": [], "must_use_terms_missing": []}}]
        self.assertEqual(ev.render_quarantine("nasa-risk", recs).strip(), "")

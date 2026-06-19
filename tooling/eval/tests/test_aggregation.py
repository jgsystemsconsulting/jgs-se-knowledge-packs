import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import eval as ev  # noqa: E402


def rec(qid, verdict="PASS", canary=False):
    j = {"faithfulness": 5, "routing": 5, "completeness": 5, "triggering": None,
         "unmapped_claims": [], "must_not_include_hits": [], "must_use_terms_missing": []}
    if verdict == "FAIL":
        j["completeness"] = 2
    return {"id": qid, "canary": canary, "judge": j}


class TestAggregation(unittest.TestCase):
    def test_all_pass_complete_bank_is_pass(self):
        agg = ev.aggregate("nasa-risk", "complete", [rec("a"), rec("b")])
        self.assertEqual(agg["status"], "PASS")

    def test_a_fail_makes_bank_fail(self):
        agg = ev.aggregate("nasa-risk", "complete", [rec("a"), rec("b", "FAIL")])
        self.assertEqual(agg["status"], "FAIL")

    def test_seed_status_forces_incomplete(self):
        agg = ev.aggregate("demo", "seed", [rec("a")])
        self.assertEqual(agg["status"], "INCOMPLETE")

    def test_partial_pack_coverage_is_incomplete_at_suite_level(self):
        suite = ev.suite_status([
            {"status": "PASS"}, {"status": "PASS"}], total_packs=13)
        self.assertEqual(suite, "INCOMPLETE")

    def test_full_coverage_all_pass_is_pass(self):
        suite = ev.suite_status([{"status": "PASS"}] * 13, total_packs=13)
        self.assertEqual(suite, "PASS")

    def test_any_fail_makes_suite_fail_even_if_complete(self):
        suite = ev.suite_status([{"status": "PASS"}] * 12 + [{"status": "FAIL"}], total_packs=13)
        self.assertEqual(suite, "FAIL")

    def test_canary_load_bearing_only_at_five(self):
        self.assertFalse(ev.canary_is_load_bearing([rec("a", canary=True)] * 4))
        self.assertTrue(ev.canary_is_load_bearing([rec(str(i), canary=True) for i in range(5)]))

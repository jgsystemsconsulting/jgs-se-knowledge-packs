import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import eval as ev  # noqa: E402


def scored_record(**judge):
    base = {"faithfulness": 5, "routing": 5, "completeness": 5,
            "triggering": None, "unmapped_claims": [],
            "must_not_include_hits": [], "must_use_terms_missing": []}
    base.update(judge)
    return {"id": "q", "judge": base}


class TestScoring(unittest.TestCase):
    def test_all_fives_passes(self):
        self.assertEqual(ev.gate_verdict(scored_record()), "PASS")

    def test_faithfulness_2_fails(self):
        self.assertEqual(ev.gate_verdict(scored_record(faithfulness=2)), "FAIL")

    def test_routing_2_fails(self):
        self.assertEqual(ev.gate_verdict(scored_record(routing=2)), "FAIL")

    def test_completeness_2_fails(self):
        self.assertEqual(ev.gate_verdict(scored_record(completeness=2)), "FAIL")

    def test_trigger_fail_fails(self):
        r = {"id": "t", "judge": {"faithfulness": None, "routing": None,
             "completeness": None, "triggering": "FAIL"}}
        self.assertEqual(ev.gate_verdict(r), "FAIL")

    def test_trigger_pass_passes(self):
        r = {"id": "t", "judge": {"faithfulness": None, "routing": None,
             "completeness": None, "triggering": "PASS"}}
        self.assertEqual(ev.gate_verdict(r), "PASS")

    def test_must_not_include_hit_is_faithfulness_fail(self):
        r = scored_record(faithfulness=2, must_not_include_hits=["bad claim"])
        self.assertEqual(ev.gate_verdict(r), "FAIL")

    def test_trend_scalar_zero_on_gated_fail(self):
        self.assertEqual(ev.trend_scalar(scored_record(completeness=2)), 0.0)

    def test_trend_scalar_is_mean_when_passing(self):
        self.assertAlmostEqual(
            ev.trend_scalar(scored_record(faithfulness=4, routing=5, completeness=3)),
            (4 + 5 + 3) / 3)

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


class TestQuarantine(unittest.TestCase):
    def _rec(self, **judge):
        base = {"faithfulness": 5, "routing": 5, "completeness": 5, "triggering": None,
                "unmapped_claims": [], "must_not_include_hits": [], "must_use_terms_missing": []}
        base.update(judge)
        return {"id": "q", "judge": base}

    def test_faithfulness_fail_quarantines(self):
        self.assertEqual(ev.disposition(self._rec(faithfulness=2)), "QUARANTINE")

    def test_must_not_include_hit_quarantines(self):
        self.assertEqual(
            ev.disposition(self._rec(faithfulness=2, must_not_include_hits=["x"])), "QUARANTINE")

    def test_strong_answer_with_term_miss_is_anchor_review(self):
        self.assertEqual(
            ev.disposition(self._rec(faithfulness=5, must_use_terms_missing=["RIDM"])),
            "ANCHOR_REVIEW")

    def test_clean_pass_needs_no_review(self):
        self.assertEqual(ev.disposition(self._rec()), "NONE")

    def test_routing_only_fail_is_not_quarantine(self):
        self.assertEqual(ev.disposition(self._rec(routing=2)), "NONE")


class TestAttestation(unittest.TestCase):
    """Headline guarantees (faithfulness scored only vs human anchors; loaded-file list
    withheld from the faithfulness pass) are driver-enforced; eval.py can't verify the wall
    but refuses records that don't attest to it."""

    def _rec(self, judge_method="anchors-only", faithfulness_saw_loaded_files=False):
        return {"id": "q", "judge_method": judge_method,
                "faithfulness_saw_loaded_files": faithfulness_saw_loaded_files,
                "judge": {"faithfulness": 5, "routing": 5, "completeness": 5, "triggering": None,
                          "unmapped_claims": [], "must_not_include_hits": [],
                          "must_use_terms_missing": []}}

    def test_well_attested_record_is_trusted(self):
        self.assertEqual(ev.attestation_errors(self._rec()), [])

    def test_missing_method_is_flagged(self):
        r = self._rec(); del r["judge_method"]
        self.assertTrue(ev.attestation_errors(r))

    def test_wrong_method_is_flagged(self):
        self.assertTrue(ev.attestation_errors(self._rec(judge_method="trust-me")))

    def test_faithfulness_saw_loaded_files_is_flagged(self):
        self.assertTrue(ev.attestation_errors(self._rec(faithfulness_saw_loaded_files=True)))

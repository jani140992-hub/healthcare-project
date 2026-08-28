"""
Unit Tests for Epidemiological Surveillance & LACE Readmission Risk.
"""

import unittest
from carepulse.analytics.surveillance import EpidemiologicalSurveillanceService

class TestAnalyticsSubsystem(unittest.TestCase):
    def test_lace_readmission_index_calculation(self):
        # Low risk: 1 day stay, elective (0), 0 comorbidities, 0 ED visits
        low_res = EpidemiologicalSurveillanceService.calculate_lace_index(
            length_of_stay_days=1,
            is_acute_emergency_admission=False,
            charlson_comorbidity_score=0,
            emergency_visits_past_6_months=0
        )
        self.assertEqual(low_res.lace_score, 1)
        self.assertEqual(low_res.risk_category, "low")

        # High risk: 5 day stay (6 pts), acute (3 pts), 3 comorbidities (3 pts), 2 ED visits (2 pts) = 14
        high_res = EpidemiologicalSurveillanceService.calculate_lace_index(
            length_of_stay_days=5,
            is_acute_emergency_admission=True,
            charlson_comorbidity_score=3,
            emergency_visits_past_6_months=2
        )
        self.assertEqual(high_res.lace_score, 14)
        self.assertEqual(high_res.risk_category, "high")
        self.assertGreater(high_res.probability_of_readmission_pct, 20.0)

if __name__ == '__main__':
    unittest.main()

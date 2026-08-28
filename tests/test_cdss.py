"""
Unit Tests for Clinical Decision Support System (CDSS).
"""

import unittest
from carepulse.cdss.ddi_engine import DDIEngine, SeverityLevel
from carepulse.cdss.allergy_checker import AllergyChecker
from carepulse.cdss.early_warning import EarlyWarningSystem
from carepulse.cdss.dose_calculator import DoseCalculator
from carepulse.cdss.guideline_rules import ClinicalGuidelineEngine

class TestCDSSSubsystem(unittest.TestCase):
    def setUp(self):
        self.ddi_engine = DDIEngine()
        self.allergy_checker = AllergyChecker()
        self.ews = EarlyWarningSystem()
        self.dose_calc = DoseCalculator()
        self.guidelines = ClinicalGuidelineEngine()

    def test_ddi_major_interaction_detection(self):
        active_meds = ["warfarin 5mg", "lisinopril 10mg", "ibuprofen 400mg"]
        alerts = self.ddi_engine.check_medication_list(active_meds)
        self.assertGreaterEqual(len(alerts), 1)

        warfarin_nsaid = next((a for a in alerts if "warfarin" in a.drug1 and "ibuprofen" in a.drug2), None)
        self.assertIsNotNone(warfarin_nsaid)
        self.assertEqual(warfarin_nsaid.severity, SeverityLevel.MAJOR)

    def test_ddi_contraindicated_pair(self):
        pair_alert = self.ddi_engine.check_pair("simvastatin 40mg", "clarithromycin 500mg")
        self.assertIsNotNone(pair_alert)
        self.assertEqual(pair_alert.severity, SeverityLevel.CONTRAINDICATED)

    def test_allergy_contraindication_cross_reactivity(self):
        # Penicillin allergy vs amoxicillin (direct)
        direct_alerts = self.allergy_checker.check_drug_against_allergies("Amoxicillin 500mg", ["Penicillin"])
        self.assertGreaterEqual(len(direct_alerts), 1)
        self.assertEqual(direct_alerts[0].risk_level, "contraindicated")

        # Aspirin allergy vs Ibuprofen (cross-reactivity NSAID)
        aspirin_alerts = self.allergy_checker.check_drug_against_allergies("Ibuprofen 400mg", ["Aspirin"])
        self.assertGreaterEqual(len(aspirin_alerts), 1)

    def test_qsofa_and_sepsis_risk(self):
        # Unstable patient: RR 24, SBP 88, Altered mental status = qSOFA 3
        qsofa = self.ews.calculate_qsofa(respiratory_rate=24, systolic_bp=88, altered_mental_status=True)
        self.assertEqual(qsofa, 3)

        sepsis_eval = self.ews.evaluate_sepsis_risk(
            respiratory_rate=24,
            systolic_bp=88,
            heart_rate=125,
            temperature_c=39.2,
            altered_mental_status=True,
            suspected_infection=True
        )
        self.assertTrue(sepsis_eval.is_sepsis_screen_positive)
        self.assertEqual(sepsis_eval.risk_tier, "critical")
        self.assertIn("EMERGENCY: Suspected Sepsis", sepsis_eval.clinical_recommendation)

    def test_pediatric_dose_calculator(self):
        # Amoxicillin: 40 mg/kg/day divided TID, child weight 15 kg -> 600 mg/day, 200 mg TID
        res = self.dose_calc.calculate_pediatric_dose(
            weight_kg=15.0,
            mg_per_kg_per_day=40.0,
            doses_per_day=3,
            adult_max_single_dose_mg=875.0,
            adult_max_daily_dose_mg=2000.0
        )
        self.assertEqual(res.recommended_dose_mg, 200.0)
        self.assertFalse(res.is_capped_at_adult_max)

        # Huge weight cap test: 80 kg child, 40 mg/kg/day = 3200 mg/day (exceeds adult max 2000 mg)
        capped_res = self.dose_calc.calculate_pediatric_dose(
            weight_kg=80.0,
            mg_per_kg_per_day=40.0,
            doses_per_day=2,
            adult_max_single_dose_mg=1000.0,
            adult_max_daily_dose_mg=2000.0
        )
        self.assertTrue(capped_res.is_capped_at_adult_max)
        self.assertEqual(capped_res.recommended_dose_mg, 1000.0)

    def test_renal_clearance_adjustment(self):
        # Cockcroft-Gault: 70 yo female, 60kg, Cr 2.0 mg/dL
        crcl = self.dose_calc.calculate_creatinine_clearance(
            age_years=70,
            weight_kg=60.0,
            serum_creatinine_mg_dl=2.0,
            is_female=True
        )
        self.assertAlmostEqual(crcl, 24.8, delta=0.5)

        # Ciprofloxacin adjustment for CrCl < 30
        adj = self.dose_calc.adjust_for_renal_function("Ciprofloxacin", 500.0, crcl)
        self.assertEqual(adj["adjusted_dose_mg"], 250.0)

    def test_clinical_guidelines_diabetes_and_hypertension(self):
        dm_recs = self.guidelines.evaluate_diabetes_care(
            age=52,
            hba1c=9.2,
            has_diabetes=True,
            has_ascvd=False,
            on_statin=False,
            urine_microalbumin_checked_past_year=False,
            eye_exam_past_year=False
        )
        self.assertGreaterEqual(len(dm_recs), 3)

        htn_recs = self.guidelines.evaluate_hypertension(154.0, 96.0)
        self.assertEqual(len(htn_recs), 1)
        self.assertIn("Stage 2 Hypertension", htn_recs[0].finding)

if __name__ == '__main__':
    unittest.main()

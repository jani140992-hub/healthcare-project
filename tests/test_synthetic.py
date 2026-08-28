"""
Unit Tests for Synthetic Patient and Cohort Generator.
"""

import unittest
import os
import tempfile
from carepulse.database import DatabaseEngine
from carepulse.synthetic.generator import SyntheticPatientGenerator
from carepulse.synthetic.cohort_builder import CohortBuilder
from carepulse.auth.service import AuthService
from carepulse.auth.models import Role

class TestSyntheticSubsystem(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.temp_db.close()
        self.db = DatabaseEngine(db_path=self.temp_db.name)
        
        # Pre-populate required providers to satisfy foreign key constraints
        self.auth_svc = AuthService(self.db)
        self.auth_svc.register_user(
            username="doc_primary_001",
            email="primary@carepulse.org",
            password="StrongPass123!Secure",
            first_name="Primary",
            last_name="CareDoc",
            role=Role.ATTENDING_PHYSICIAN
        )
        self.auth_svc.register_user(
            username="nurse_triage_001",
            email="triage@carepulse.org",
            password="StrongPass123!Secure",
            first_name="Triage",
            last_name="Nurse",
            role=Role.REGISTERED_NURSE
        )

        self.generator = SyntheticPatientGenerator(self.db)
        self.cohort_builder = CohortBuilder(self.db)

    def tearDown(self):
        try:
            os.unlink(self.temp_db.name)
        except Exception:
            pass

    def test_single_patient_generation_with_chronic_conditions(self):
        pat = self.generator.generate_patient(has_diabetes=True, has_hypertension=True)
        self.assertIsNotNone(pat)
        self.assertTrue(pat.id.startswith("pat_"))

        # Verify conditions were registered
        conds = self.db.execute_query("SELECT * FROM conditions WHERE patient_id = ?", (pat.id,))
        self.assertEqual(len(conds), 2)
        icd_codes = [c["icd10_code"] for c in conds]
        self.assertIn("E11.9", icd_codes)
        self.assertIn("I10", icd_codes)

        # Verify prescriptions were ordered
        prescriptions = self.db.execute_query("SELECT * FROM prescriptions WHERE patient_id = ?", (pat.id,))
        self.assertEqual(len(prescriptions), 2)

    def test_cohort_builder_generation(self):
        cohort = self.cohort_builder.build_cohort(total_patients=5, diabetes_prevalence=0.4, hypertension_prevalence=0.6)
        self.assertEqual(len(cohort), 5)

if __name__ == '__main__':
    unittest.main()

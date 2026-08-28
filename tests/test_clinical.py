"""
Unit Tests for CarePulse Clinical Subsystem.
"""

import unittest
import os
import tempfile
from carepulse.database import DatabaseEngine
from carepulse.clinical.patient import PatientService
from carepulse.clinical.encounter import EncounterService
from carepulse.clinical.vitals import VitalsService
from carepulse.clinical.conditions import ConditionService
from carepulse.clinical.allergies import AllergyService
from carepulse.clinical.notes import ClinicalNotesService
from carepulse.clinical.cpoe import CPOEService

class TestClinicalSubsystem(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.temp_db.close()
        self.db = DatabaseEngine(db_path=self.temp_db.name)
        
        self.patient_svc = PatientService(self.db)
        self.encounter_svc = EncounterService(self.db)
        self.vitals_svc = VitalsService(self.db)
        self.condition_svc = ConditionService(self.db)
        self.allergy_svc = AllergyService(self.db)
        self.notes_svc = ClinicalNotesService(self.db)
        self.cpoe_svc = CPOEService(self.db)

        from carepulse.auth.service import AuthService
        from carepulse.auth.models import Role
        self.auth_svc = AuthService(self.db)
        self.doc_user = self.auth_svc.register_user(
            username="test_dr_001",
            email="dr.smith@carepulse.org",
            password="StrongPass123!Secure",
            first_name="Doctor",
            last_name="Smith",
            role=Role.ATTENDING_PHYSICIAN
        )

    def tearDown(self):
        try:
            os.unlink(self.temp_db.name)
        except Exception:
            pass

    def test_patient_registration_and_retrieval(self):
        pat = self.patient_svc.register_patient(
            first_name="Alice",
            last_name="Johnson",
            date_of_birth="1985-04-12",
            gender="female",
            actor_id="test_doctor",
            actor_role="attending_physician",
            phone="555-0199",
            email="alice.j@example.com"
        )
        self.assertTrue(pat.id.startswith("pat_"))
        self.assertTrue(pat.mrn.startswith("MRN-"))
        self.assertEqual(pat.full_name, "Alice Johnson")
        self.assertGreater(pat.age, 30)

        # Retrieve
        fetched = self.patient_svc.get_patient(pat.id, actor_id="test_doctor", actor_role="attending_physician")
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.first_name, "Alice")
        self.assertEqual(fetched.mrn, pat.mrn)

    def test_patient_search(self):
        self.patient_svc.register_patient("Robert", "Smith", "1970-01-01", "male", "doc", "doctor")
        self.patient_svc.register_patient("Roberta", "Williams", "1980-02-02", "female", "doc", "doctor")

        results = self.patient_svc.search_patients("Robert", "doc", "doctor")
        self.assertGreaterEqual(len(results), 2)

    def test_encounter_lifecycle(self):
        pat = self.patient_svc.register_patient("Test", "Patient", "1990-01-01", "male", "doc", "doctor")
        enc = self.encounter_svc.start_encounter(
            patient_id=pat.id,
            provider_id=self.doc_user.id,
            encounter_type="inpatient",
            actor_id="doc",
            actor_role="attending_physician",
            reason_description="Acute abdominal pain"
        )
        self.assertEqual(enc.status, "in-progress")

        completed = self.encounter_svc.complete_encounter(
            enc.id, actor_id="doc", actor_role="attending_physician", discharge_disposition="home"
        )
        self.assertTrue(completed)

        enc_list = self.encounter_svc.get_patient_encounters(pat.id, "doc", "attending_physician")
        self.assertEqual(len(enc_list), 1)
        self.assertEqual(enc_list[0].status, "completed")

    def test_vital_signs_and_calculations(self):
        pat = self.patient_svc.register_patient("John", "Doe", "1965-06-15", "male", "doc", "doctor")
        vitals = self.vitals_svc.record_vitals(
            patient_id=pat.id,
            recorded_by="nurse_001",
            actor_role="registered_nurse",
            systolic_bp=150.0,
            diastolic_bp=95.0,
            heart_rate=88.0,
            respiratory_rate=18.0,
            body_temperature=37.2,
            oxygen_saturation=97.0,
            height_cm=180.0,
            weight_kg=85.0
        )
        # MAP = (2 * 95 + 150) / 3 = 340 / 3 = 113.3
        self.assertAlmostEqual(vitals.mean_arterial_pressure, 113.3, delta=0.5)
        # BMI = 85 / (1.8^2) = 26.23
        self.assertAlmostEqual(vitals.bmi, 26.23, delta=0.2)
        self.assertEqual(vitals.bmi_category, "Overweight")

    def test_clinical_conditions_and_allergies(self):
        pat = self.patient_svc.register_patient("Sarah", "Connor", "1984-05-12", "female", "doc", "doctor")
        cond = self.condition_svc.add_condition(
            patient_id=pat.id,
            icd10_code="E11.9",
            description="Type 2 diabetes mellitus",
            category="chronic-problem",
            clinical_status="active",
            recorded_by="doc_001",
            actor_role="attending_physician"
        )
        self.assertEqual(cond.icd10_code, "E11.9")

        conds = self.condition_svc.get_patient_conditions(pat.id, "doc_001", "attending_physician")
        self.assertEqual(len(conds), 1)

        alg = self.allergy_svc.record_allergy(
            patient_id=pat.id,
            substance="Penicillin",
            category="medication",
            criticality="high",
            recorded_by="nurse_001",
            actor_role="registered_nurse",
            reaction="Anaphylaxis"
        )
        self.assertEqual(alg.substance, "Penicillin")
        algs = self.allergy_svc.get_patient_allergies(pat.id, "doc_001", "attending_physician")
        self.assertEqual(len(algs), 1)

    def test_soap_notes_and_signing(self):
        pat = self.patient_svc.register_patient("Bruce", "Wayne", "1975-02-19", "male", "doc", "doctor")
        enc = self.encounter_svc.start_encounter(pat.id, self.doc_user.id, "ambulatory", "doc", "doctor")
        
        note = self.notes_svc.create_soap_note(
            patient_id=pat.id,
            encounter_id=enc.id,
            author_id=self.doc_user.id,
            actor_role="attending_physician",
            subjective="Patient reports mild headache.",
            objective="BP 120/80, HR 72, Afebrile.",
            assessment="Tension headache.",
            plan="Rest, hydration, OTC acetaminophen PRN."
        )
        self.assertFalse(note.signed)

        signed = self.notes_svc.sign_note(note.id, "doc_001", "attending_physician")
        self.assertTrue(signed)

        # Signing again should raise ValueError
        with self.assertRaises(ValueError):
            self.notes_svc.sign_note(note.id, "doc_001", "attending_physician")

if __name__ == '__main__':
    unittest.main()

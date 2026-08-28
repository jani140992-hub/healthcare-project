"""
Unit Tests for HL7 FHIR R4 Serialization & Validation.
"""

import unittest
from carepulse.clinical.patient import PatientRecord
from carepulse.clinical.encounter import EncounterRecord
from carepulse.clinical.vitals import VitalSignsRecord
from carepulse.fhir.serializers import FHIRSerializer
from carepulse.fhir.validator import FHIRValidator

class TestFHIRSubsystem(unittest.TestCase):
    def test_patient_to_fhir_serialization(self):
        patient = PatientRecord(
            id="pat_12345",
            mrn="MRN-00123456",
            first_name="Jane",
            last_name="Doe",
            date_of_birth="1992-08-14",
            gender="female",
            phone="555-1234",
            email="jane.doe@example.com",
            address_street="100 Main St",
            address_city="Boston",
            address_state="MA",
            address_postal_code="02115"
        )
        fhir_json = FHIRSerializer.patient_to_fhir(patient)

        self.assertEqual(fhir_json["resourceType"], "Patient")
        self.assertEqual(fhir_json["id"], "pat_12345")
        self.assertEqual(fhir_json["gender"], "female")
        self.assertEqual(fhir_json["name"][0]["family"], "Doe")

        # Validate with FHIRValidator
        is_valid, issues = FHIRValidator.validate_resource(fhir_json)
        self.assertTrue(is_valid, f"Validation issues: {issues}")

    def test_vitals_to_fhir_observations(self):
        vitals = VitalSignsRecord(
            id="vit_987",
            patient_id="pat_12345",
            recorded_at="2026-08-28T10:00:00Z",
            recorded_by="nurse_1",
            systolic_bp=120.0,
            diastolic_bp=80.0,
            heart_rate=72.0,
            oxygen_saturation=99.0
        )
        obs_list = FHIRSerializer.vitals_to_fhir_observations(vitals)
        self.assertGreaterEqual(len(obs_list), 3)

        for obs in obs_list:
            is_valid, issues = FHIRValidator.validate_resource(obs)
            self.assertTrue(is_valid, f"Obs validation failed: {issues}")

    def test_fhir_bundle_creation(self):
        resources = [
            {"resourceType": "Patient", "id": "p1", "gender": "male"},
            {"resourceType": "Patient", "id": "p2", "gender": "female"}
        ]
        bundle = FHIRSerializer.create_bundle(resources)
        self.assertEqual(bundle["resourceType"], "Bundle")
        self.assertEqual(bundle["total"], 2)
        self.assertEqual(len(bundle["entry"]), 2)

    def test_fhir_validator_rejects_malformed_resources(self):
        invalid_patient = {"resourceType": "Patient"} # Missing id
        is_valid, issues = FHIRValidator.validate_resource(invalid_patient)
        self.assertFalse(is_valid)
        self.assertTrue(any("id" in issue for issue in issues))

        unknown_resource = {"resourceType": "FakeResource", "id": "f1"}
        is_valid, issues = FHIRValidator.validate_resource(unknown_resource)
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()

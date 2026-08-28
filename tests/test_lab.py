"""
Unit Tests for Laboratory Information Subsystem (LIS).
"""

import unittest
import os
import tempfile
from carepulse.database import DatabaseEngine
from carepulse.clinical.patient import PatientService
from carepulse.clinical.cpoe import CPOEService
from carepulse.lab.orders import LabOrderService
from carepulse.lab.specimens import SpecimenService
from carepulse.lab.analyzers import AnalyzerInterface
from carepulse.lab.results import LabResultService
from carepulse.auth.service import AuthService
from carepulse.auth.models import Role

class TestLabSubsystem(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.temp_db.close()
        self.db = DatabaseEngine(db_path=self.temp_db.name)

        self.patient_svc = PatientService(self.db)
        self.cpoe_svc = CPOEService(self.db)
        self.order_svc = LabOrderService(self.db)
        self.specimen_svc = SpecimenService()
        self.result_svc = LabResultService(self.db)
        self.auth_svc = AuthService(self.db)

        self.doc = self.auth_svc.register_user("dr_jones", "jones@med.org", "Pass123!Secure", "Indy", "Jones", Role.ATTENDING_PHYSICIAN)
        self.tech = self.auth_svc.register_user("tech_clark", "clark@med.org", "Pass123!Secure", "Clark", "Kent", Role.LAB_TECHNICIAN)

    def tearDown(self):
        try:
            os.unlink(self.temp_db.name)
        except Exception:
            pass

    def test_specimen_accessioning_and_rejection(self):
        spc = self.specimen_svc.accession_specimen(
            patient_id="pat_123",
            lab_order_id="ord_456",
            specimen_type="blood",
            collector_id=self.tech.id,
            container_type="Lavender Top (EDTA)"
        )
        self.assertEqual(spc.status, "collected")
        self.assertTrue(spc.accession_number.startswith("ACC-"))

        # Inspect and accept
        self.specimen_svc.inspect_specimen(spc.specimen_id, is_acceptable=True)
        self.assertEqual(spc.status, "received_in_lab")

        # Reject another specimen
        spc2 = self.specimen_svc.accession_specimen("pat_999", "ord_777", "blood", self.tech.id, "Red Top")
        self.specimen_svc.inspect_specimen(spc2.specimen_id, is_acceptable=False, rejection_reason="Grossly hemolyzed")
        self.assertEqual(spc2.status, "rejected")
        self.assertEqual(spc2.rejection_reason, "Grossly hemolyzed")

    def test_analyzer_simulation(self):
        cbc_results = AnalyzerInterface.run_complete_blood_count("BARCODE-12345")
        self.assertEqual(len(cbc_results), 5)
        wbc = next(r for r in cbc_results if r.test_code == "6690-2")
        self.assertGreater(wbc.numeric_value, 0.0)

    def test_panic_value_flagging(self):
        pat = self.patient_svc.register_patient("Clark", "Griswold", "1960-12-25", "male", "admin", "admin")
        order = self.cpoe_svc.place_lab_order(
            patient_id=pat.id,
            provider_id=self.doc.id,
            actor_role="attending_physician",
            loinc_code="2823-3",
            test_name="Potassium",
            specimen_type="serum"
        )

        # Critical High Potassium (e.g. 6.8 mmol/L - normal 3.5 - 5.2, crit > 6.2)
        res = self.result_svc.record_result(
            lab_order_id=order.order_id,
            patient_id=pat.id,
            loinc_code="2823-3",
            analyte_name="Potassium",
            numeric_value=6.8,
            unit="mmol/L",
            reference_low=3.5,
            reference_high=5.2,
            critical_low=2.8,
            critical_high=6.2,
            reporter_id=self.tech.id,
            reporter_role="lab_technician"
        )
        self.assertEqual(res.abnormal_flag, "critical_high")

if __name__ == '__main__':
    unittest.main()

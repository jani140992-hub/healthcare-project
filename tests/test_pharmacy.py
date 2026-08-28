"""
Unit Tests for Pharmacy Inventory and Dispensing BCMA Subsystem.
"""

import unittest
import os
import tempfile
from carepulse.database import DatabaseEngine
from carepulse.clinical.patient import PatientService
from carepulse.clinical.cpoe import CPOEService
from carepulse.pharmacy.inventory import PharmacyInventoryService, MedicationInventoryItem
from carepulse.pharmacy.dispensing import DispensingService
from carepulse.pharmacy.prescription import PrescriptionService
from carepulse.auth.service import AuthService
from carepulse.auth.models import Role

class TestPharmacySubsystem(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.temp_db.close()
        self.db = DatabaseEngine(db_path=self.temp_db.name)

        self.patient_svc = PatientService(self.db)
        self.cpoe_svc = CPOEService(self.db)
        self.inv_svc = PharmacyInventoryService()
        self.dispense_svc = DispensingService(self.db)
        self.rx_svc = PrescriptionService(self.db)
        self.auth_svc = AuthService(self.db)

        self.doc = self.auth_svc.register_user("dr_house", "house@med.org", "SafePass123!#", "Greg", "House", Role.ATTENDING_PHYSICIAN)
        self.pharm = self.auth_svc.register_user("pharm_wilson", "wilson@med.org", "SafePass123!#", "James", "Wilson", Role.CLINICAL_PHARMACIST)

    def tearDown(self):
        try:
            os.unlink(self.temp_db.name)
        except Exception:
            pass

    def test_pharmacy_inventory_stock_and_expiry(self):
        item = MedicationInventoryItem(
            item_id="item_01",
            ndc="00069-4200-30",
            drug_name="Atorvastatin Calcium",
            strength="20 mg",
            dosage_form="Oral Tablet",
            lot_number="LOT-2026A",
            expiration_date="2027-12-31",
            quantity_on_hand=500,
            reorder_threshold=100
        )
        self.inv_svc.add_or_update_stock(item)

        self.assertTrue(self.inv_svc.check_stock_availability("00069-4200-30", 250))
        self.assertFalse(self.inv_svc.check_stock_availability("00069-4200-30", 600))

        deducted = self.inv_svc.deduct_stock("item_01", 100)
        self.assertTrue(deducted)
        self.assertEqual(item.quantity_on_hand, 400)

    def test_bcma_dispensing_five_rights_verification(self):
        pat = self.patient_svc.register_patient("Tony", "Stark", "1970-05-29", "male", "admin", "admin")
        order = self.cpoe_svc.place_medication_order(
            patient_id=pat.id,
            prescriber_id=self.doc.id,
            actor_role="attending_physician",
            rxnorm_code="860975",
            drug_name="Metformin 500 MG",
            dosage_form="tablet",
            strength="500 mg",
            dose_amount=500.0,
            dose_unit="mg",
            route="oral",
            frequency="BID",
            duration_days=30,
            quantity=60
        )

        # Successful 5-rights dispense
        res = self.dispense_svc.verify_and_dispense(
            prescription_id=order.order_id,
            scanned_patient_mrn=pat.mrn,
            scanned_barcode_ndc="860975",
            scanned_dose_amount=500.0,
            scanned_route="oral",
            pharmacist_id=self.pharm.id,
            pharmacist_role="clinical_pharmacist",
            lot_number="MET-2026-X",
            expiration_date="2027-06-30",
            quantity_to_dispense=60
        )
        self.assertTrue(res.is_approved)
        self.assertTrue(res.five_rights_verified)
        self.assertIsNotNone(res.dispense_id)

        # Mismatched dose error test
        bad_dose_res = self.dispense_svc.verify_and_dispense(
            prescription_id=order.order_id,
            scanned_patient_mrn=pat.mrn,
            scanned_barcode_ndc="860975",
            scanned_dose_amount=1000.0, # Mismatch!
            scanned_route="oral",
            pharmacist_id=self.pharm.id,
            pharmacist_role="clinical_pharmacist",
            lot_number="MET-2026-X",
            expiration_date="2027-06-30",
            quantity_to_dispense=60
        )
        self.assertFalse(bad_dose_res.is_approved)
        self.assertIn("Dose Mismatch", bad_dose_res.errors[0])

if __name__ == '__main__':
    unittest.main()

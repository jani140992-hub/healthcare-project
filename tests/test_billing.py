"""
Unit Tests for Revenue Cycle & Billing Subsystem (EDI 837P, EDI 835, Fee Schedule).
"""

import unittest
import os
import tempfile
from carepulse.database import DatabaseEngine
from carepulse.clinical.patient import PatientService
from carepulse.billing.fee_schedule import FeeScheduleService
from carepulse.billing.claims_837 import Claims837Generator, InsuranceClaim, ServiceLine
from carepulse.billing.remittance_835 import Remittance835Parser
from carepulse.billing.invoicing import BillingInvoicingService

class TestBillingSubsystem(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.temp_db.close()
        self.db = DatabaseEngine(db_path=self.temp_db.name)

        self.patient_svc = PatientService(self.db)
        self.fee_svc = FeeScheduleService()
        self.invoice_svc = BillingInvoicingService(self.db)

    def tearDown(self):
        try:
            os.unlink(self.temp_db.name)
        except Exception:
            pass

    def test_fee_schedule_and_rvu_calculation(self):
        charge = self.fee_svc.get_charge("99214")
        self.assertIsNotNone(charge)
        self.assertEqual(charge.code, "99214")
        self.assertEqual(charge.total_rvu, 3.58)

        reimbursement = self.fee_svc.calculate_rvu_reimbursement("99214", conversion_factor=32.7442)
        self.assertAlmostEqual(reimbursement, 117.22, delta=0.5)

    def test_edi_837p_claim_generation(self):
        claim = InsuranceClaim(
            claim_id="CLM100234",
            patient_id="pat_001",
            patient_name="John Doe",
            patient_dob="1980-05-15",
            patient_gender="male",
            subscriber_id="SUB998877",
            payer_id="BLUECROSS01",
            payer_name="Blue Cross Blue Shield",
            provider_npi="1234567890",
            provider_tax_id="123456789",
            diagnosis_codes=["I10", "E11.9"],
            service_lines=[
                ServiceLine(1, "99214", 195.00, 1, "2026-08-28"),
                ServiceLine(2, "80053", 45.00, 1, "2026-08-28")
            ],
            total_claim_charge=240.00
        )
        edi_text = Claims837Generator.generate_edi_837p(claim)
        self.assertIn("ISA*", edi_text)
        self.assertIn("GS*HC*", edi_text)
        self.assertIn("ST*837*", edi_text)
        self.assertIn("CLM*CLM100234*240.00", edi_text)
        self.assertIn("SV1*HC:99214*195.00", edi_text)
        self.assertIn("SE*", edi_text)
        self.assertIn("IEA*", edi_text)

    def test_edi_835_remittance_parsing(self):
        mock_835 = (
            "ISA*00* *00* *ZZ*PAYER *ZZ*CAREPULSE *260828*1000*^*00501*000000001*0*P*:~"
            "GS*HP*PAYER*CAREPULSE*20260828*1000*1*X*005010X221A1~"
            "ST*835*0001~"
            "N1*PR*AETNA HEALTH~"
            "TRN*1*CHECK123456*1999999999~"
            "CLP*CLM100234*1*240.00*180.00*20.00*12*PAYERREF100~"
            "CAS*CO*45*40.00~"
            "CAS*PR*1*20.00~"
            "SE*8*0001~"
            "GE*1*1~"
            "IEA*1*000000001~"
        )
        parsed = Remittance835Parser.parse_mock_835_string(mock_835)
        self.assertEqual(len(parsed), 1)
        remit = parsed[0]
        self.assertEqual(remit.claim_id, "CLM100234")
        self.assertEqual(remit.billed_amount, 240.00)
        self.assertEqual(remit.paid_amount, 180.00)
        self.assertEqual(remit.patient_responsibility, 20.00)
        self.assertEqual(remit.contractual_allowance, 40.00)
        self.assertEqual(len(remit.adjustments), 2)

    def test_patient_invoicing_and_payments(self):
        pat = self.patient_svc.register_patient("Arthur", "Dent", "1978-03-11", "male", "admin", "admin")
        inv = self.invoice_svc.generate_invoice(
            patient_id=pat.id,
            total_charges=200.0,
            insurance_covered=150.0,
            patient_copay=50.0
        )
        self.assertEqual(inv.patient_balance, 50.0)

        # Make partial payment
        paid_partial = self.invoice_svc.record_patient_payment(inv.id, 25.0)
        self.assertTrue(paid_partial)

        # Check balance
        row = self.db.execute_single("SELECT patient_balance, status FROM billing_invoices WHERE id = ?", (inv.id,))
        self.assertEqual(row["patient_balance"], 25.0)
        self.assertEqual(row["status"], "partial_payment")

        # Pay remainder
        paid_full = self.invoice_svc.record_patient_payment(inv.id, 25.0)
        self.assertTrue(paid_full)
        row2 = self.db.execute_single("SELECT patient_balance, status FROM billing_invoices WHERE id = ?", (inv.id,))
        self.assertEqual(row2["patient_balance"], 0.0)
        self.assertEqual(row2["status"], "paid")

if __name__ == '__main__':
    unittest.main()

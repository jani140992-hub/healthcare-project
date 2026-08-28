"""
Patient Invoicing, Copays, and Balance Ledger Management.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import uuid
from datetime import datetime, timezone, timedelta
from carepulse.database import get_db

@dataclass
class InvoiceRecord:
    id: str
    invoice_number: str
    patient_id: str
    encounter_id: Optional[str]
    total_charges: float
    insurance_covered: float
    patient_copay: float
    patient_balance: float
    status: str
    issue_date: str
    due_date: str

class BillingInvoicingService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()

    def generate_invoice(
        self,
        patient_id: str,
        total_charges: float,
        encounter_id: Optional[str] = None,
        insurance_covered: float = 0.0,
        patient_copay: float = 25.0,
        payer_id: Optional[str] = None,
        payer_name: Optional[str] = None,
        insurance_policy_number: Optional[str] = None
    ) -> InvoiceRecord:
        invoice_id = f"inv_{uuid.uuid4().hex[:12]}"
        inv_number = f"INV-{datetime.now(timezone.utc).strftime('%Y%m')}-{uuid.uuid4().hex[:6].upper()}"
        now = datetime.now(timezone.utc).date()
        due = now + timedelta(days=30)
        patient_balance = max(0.0, total_charges - insurance_covered)

        sql = """
        INSERT INTO billing_invoices (
            id, invoice_number, patient_id, encounter_id,
            insurance_policy_number, payer_id, payer_name,
            total_charges, insurance_covered, patient_copay,
            patient_balance, status, issue_date, due_date, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'submitted', ?, ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                invoice_id, inv_number, patient_id, encounter_id,
                insurance_policy_number, payer_id, payer_name,
                total_charges, insurance_covered, patient_copay,
                patient_balance, now.isoformat(), due.isoformat(), now.isoformat()
            )
        )

        return InvoiceRecord(
            id=invoice_id,
            invoice_number=inv_number,
            patient_id=patient_id,
            encounter_id=encounter_id,
            total_charges=total_charges,
            insurance_covered=insurance_covered,
            patient_copay=patient_copay,
            patient_balance=patient_balance,
            status="submitted",
            issue_date=now.isoformat(),
            due_date=due.isoformat()
        )

    def record_patient_payment(self, invoice_id: str, amount_paid: float) -> bool:
        row = self.db.execute_single("SELECT patient_balance FROM billing_invoices WHERE id = ?", (invoice_id,))
        if not row:
            return False

        new_bal = max(0.0, row["patient_balance"] - amount_paid)
        status = "paid" if new_bal == 0.0 else "partial_payment"
        sql = "UPDATE billing_invoices SET patient_balance = ?, status = ? WHERE id = ?"
        self.db.execute_insert(sql, (new_bal, status, invoice_id))
        return True

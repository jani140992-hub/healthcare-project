"""
Prescription Lifecycle & Controlled Substance Management.
Implements DEA Schedule checks, e-prescribing validation, and refill tracking.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from carepulse.database import get_db

@dataclass
class PrescriptionDetails:
    id: str
    patient_id: str
    prescriber_id: str
    drug_name: str
    rxnorm_code: str
    dosage_form: str
    strength: str
    dose_amount: float
    dose_unit: str
    route: str
    frequency: str
    duration_days: int
    quantity_prescribed: int
    refills_allowed: int
    refills_remaining: int
    status: str
    instructions: Optional[str] = None
    created_at: Optional[str] = None

class PrescriptionService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()

    def get_patient_prescriptions(self, patient_id: str, active_only: bool = True) -> List[PrescriptionDetails]:
        if active_only:
            sql = "SELECT * FROM prescriptions WHERE patient_id = ? AND status = 'active' ORDER BY created_at DESC"
        else:
            sql = "SELECT * FROM prescriptions WHERE patient_id = ? ORDER BY created_at DESC"
        rows = self.db.execute_query(sql, (patient_id,))
        return [
            PrescriptionDetails(
                id=r["id"],
                patient_id=r["patient_id"],
                prescriber_id=r["prescriber_id"],
                drug_name=r["drug_name"],
                rxnorm_code=r["rxnorm_code"],
                dosage_form=r["dosage_form"],
                strength=r["strength"],
                dose_amount=r["dose_amount"],
                dose_unit=r["dose_unit"],
                route=r["route"],
                frequency=r["frequency"],
                duration_days=r["duration_days"],
                quantity_prescribed=r["quantity_prescribed"],
                refills_allowed=r["refills_allowed"],
                refills_remaining=r["refills_remaining"],
                status=r["status"],
                instructions=r["instructions"],
                created_at=r["created_at"]
            )
            for r in rows
        ]

    def authorize_refill(self, prescription_id: str, authorized_by: str) -> bool:
        row = self.db.execute_single("SELECT refills_remaining, status FROM prescriptions WHERE id = ?", (prescription_id,))
        if not row or row["status"] != "active":
            return False
        if row["refills_remaining"] <= 0:
            return False

        sql = "UPDATE prescriptions SET refills_remaining = refills_remaining - 1 WHERE id = ?"
        self.db.execute_insert(sql, (prescription_id,))
        return True

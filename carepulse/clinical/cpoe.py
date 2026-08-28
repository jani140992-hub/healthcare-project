"""
Computerized Physician Order Entry (CPOE) Subsystem.
Centralizes clinical orders across Medications, Laboratory, and Diagnostic Imaging.
"""

import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from carepulse.database import get_db
from carepulse.auth.audit import HIPAALogger, AuditAction

@dataclass
class OrderRecord:
    order_id: str
    order_type: str  # medication, lab, radiology
    patient_id: str
    encounter_id: Optional[str]
    ordering_provider_id: str
    item_code: str
    item_name: str
    priority: str
    status: str
    order_date: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

class CPOEService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()
        self.audit_logger = HIPAALogger(self.db)

    def place_medication_order(
        self,
        patient_id: str,
        prescriber_id: str,
        actor_role: str,
        rxnorm_code: str,
        drug_name: str,
        dosage_form: str,
        strength: str,
        dose_amount: float,
        dose_unit: str,
        route: str,
        frequency: str,
        duration_days: int,
        quantity: int,
        encounter_id: Optional[str] = None,
        instructions: Optional[str] = None
    ) -> OrderRecord:
        order_id = f"rx_{uuid.uuid4().hex[:12]}"
        now = datetime.now(timezone.utc).isoformat()

        sql = """
        INSERT INTO prescriptions (
            id, patient_id, encounter_id, prescriber_id, rxnorm_code,
            drug_name, dosage_form, strength, dose_amount, dose_unit,
            route, frequency, duration_days, quantity_prescribed,
            status, instructions, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'active', ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                order_id, patient_id, encounter_id, prescriber_id, rxnorm_code,
                drug_name, dosage_form, strength, dose_amount, dose_unit,
                route, frequency, duration_days, quantity, instructions, now
            )
        )

        self.audit_logger.log_event(
            actor_id=prescriber_id,
            actor_role=actor_role,
            action=AuditAction.ORDER_SUBMITTED,
            resource_type="MedicationRequest",
            resource_id=order_id,
            patient_id=patient_id,
            details={"drug": drug_name, "quantity": quantity}
        )

        return OrderRecord(
            order_id=order_id,
            order_type="medication",
            patient_id=patient_id,
            encounter_id=encounter_id,
            ordering_provider_id=prescriber_id,
            item_code=rxnorm_code,
            item_name=drug_name,
            priority="routine",
            status="active",
            order_date=now
        )

    def place_lab_order(
        self,
        patient_id: str,
        provider_id: str,
        actor_role: str,
        loinc_code: str,
        test_name: str,
        specimen_type: str,
        priority: str = "routine",
        encounter_id: Optional[str] = None
    ) -> OrderRecord:
        order_id = f"lab_{uuid.uuid4().hex[:12]}"
        now = datetime.now(timezone.utc).isoformat()

        sql = """
        INSERT INTO lab_orders (
            id, patient_id, encounter_id, ordering_provider_id,
            loinc_code, test_name, specimen_type, priority,
            status, order_date
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'ordered', ?)
        """
        self.db.execute_insert(
            sql,
            (
                order_id, patient_id, encounter_id, provider_id,
                loinc_code, test_name, specimen_type, priority.lower(), now
            )
        )

        self.audit_logger.log_event(
            actor_id=provider_id,
            actor_role=actor_role,
            action=AuditAction.ORDER_SUBMITTED,
            resource_type="ServiceRequest/Lab",
            resource_id=order_id,
            patient_id=patient_id,
            details={"test": test_name, "loinc": loinc_code}
        )

        return OrderRecord(
            order_id=order_id,
            order_type="lab",
            patient_id=patient_id,
            encounter_id=encounter_id,
            ordering_provider_id=provider_id,
            item_code=loinc_code,
            item_name=test_name,
            priority=priority,
            status="ordered",
            order_date=now
        )

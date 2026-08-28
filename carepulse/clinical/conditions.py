"""
Clinical Problem List & Condition Registry.
Tracks acute diagnoses, chronic illnesses, and medical history with ICD-10-CM classification.
"""

import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from carepulse.database import get_db
from carepulse.auth.audit import HIPAALogger, AuditAction

@dataclass
class ConditionRecord:
    id: str
    patient_id: str
    icd10_code: str
    description: str
    category: str
    clinical_status: str
    recorded_by: str
    encounter_id: Optional[str] = None
    snomed_code: Optional[str] = None
    verification_status: Optional[str] = "confirmed"
    severity: Optional[str] = "moderate"
    onset_date: Optional[str] = None
    abatement_date: Optional[str] = None
    created_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

class ConditionService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()
        self.audit_logger = HIPAALogger(self.db)

    def add_condition(
        self,
        patient_id: str,
        icd10_code: str,
        description: str,
        category: str,
        clinical_status: str,
        recorded_by: str,
        actor_role: str,
        encounter_id: Optional[str] = None,
        snomed_code: Optional[str] = None,
        severity: Optional[str] = "moderate",
        onset_date: Optional[str] = None
    ) -> ConditionRecord:
        cond_id = f"con_{uuid.uuid4().hex[:12]}"
        now = datetime.now(timezone.utc).isoformat()

        sql = """
        INSERT INTO conditions (
            id, patient_id, encounter_id, icd10_code, snomed_code,
            description, category, clinical_status, verification_status,
            severity, onset_date, recorded_by, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'confirmed', ?, ?, ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                cond_id, patient_id, encounter_id, icd10_code.upper().strip(),
                snomed_code, description.strip(), category.lower(),
                clinical_status.lower(), severity.lower(), onset_date or now[:10],
                recorded_by, now
            )
        )

        self.audit_logger.log_event(
            actor_id=recorded_by,
            actor_role=actor_role,
            action=AuditAction.PHI_CREATE,
            resource_type="Condition",
            resource_id=cond_id,
            patient_id=patient_id,
            details={"icd10": icd10_code, "status": clinical_status}
        )

        return ConditionRecord(
            id=cond_id,
            patient_id=patient_id,
            encounter_id=encounter_id,
            icd10_code=icd10_code.upper().strip(),
            snomed_code=snomed_code,
            description=description.strip(),
            category=category.lower(),
            clinical_status=clinical_status.lower(),
            verification_status="confirmed",
            severity=severity.lower(),
            onset_date=onset_date or now[:10],
            recorded_by=recorded_by,
            created_at=now
        )

    def get_patient_conditions(
        self,
        patient_id: str,
        actor_id: str,
        actor_role: str,
        active_only: bool = True
    ) -> List[ConditionRecord]:
        if active_only:
            sql = "SELECT * FROM conditions WHERE patient_id = ? AND clinical_status = 'active' ORDER BY created_at DESC"
        else:
            sql = "SELECT * FROM conditions WHERE patient_id = ? ORDER BY created_at DESC"
        rows = self.db.execute_query(sql, (patient_id,))

        self.audit_logger.log_event(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.PHI_READ,
            resource_type="ConditionList",
            resource_id=patient_id,
            patient_id=patient_id,
            details={"active_only": active_only, "count": len(rows)}
        )

        return [
            ConditionRecord(
                id=r["id"],
                patient_id=r["patient_id"],
                encounter_id=r["encounter_id"],
                icd10_code=r["icd10_code"],
                snomed_code=r["snomed_code"],
                description=r["description"],
                category=r["category"],
                clinical_status=r["clinical_status"],
                verification_status=r["verification_status"],
                severity=r["severity"],
                onset_date=r["onset_date"],
                abatement_date=r["abatement_date"],
                recorded_by=r["recorded_by"],
                created_at=r["created_at"]
            )
            for r in rows
        ]

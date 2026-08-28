"""
Allergy & Adverse Reaction Management Subsystem.
Tracks medication, food, and environmental hypersensitivities with severity classifications.
"""

import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from carepulse.database import get_db
from carepulse.auth.audit import HIPAALogger, AuditAction

@dataclass
class AllergyRecord:
    id: str
    patient_id: str
    substance: str
    category: str
    criticality: str
    clinical_status: str
    recorded_by: str
    substance_code: Optional[str] = None
    reaction_manifestation: Optional[str] = None
    severity: Optional[str] = "moderate"
    onset_date: Optional[str] = None
    created_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

class AllergyService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()
        self.audit_logger = HIPAALogger(self.db)

    def record_allergy(
        self,
        patient_id: str,
        substance: str,
        category: str,
        criticality: str,
        recorded_by: str,
        actor_role: str,
        substance_code: Optional[str] = None,
        reaction: Optional[str] = None,
        severity: Optional[str] = "moderate",
        onset_date: Optional[str] = None
    ) -> AllergyRecord:
        allergy_id = f"alg_{uuid.uuid4().hex[:12]}"
        now = datetime.now(timezone.utc).isoformat()

        sql = """
        INSERT INTO allergies (
            id, patient_id, substance, substance_code, category,
            criticality, clinical_status, reaction_manifestation,
            severity, onset_date, recorded_by, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, 'active', ?, ?, ?, ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                allergy_id, patient_id, substance.strip(), substance_code,
                category.lower(), criticality.lower(), reaction,
                severity.lower(), onset_date or now[:10], recorded_by, now
            )
        )

        self.audit_logger.log_event(
            actor_id=recorded_by,
            actor_role=actor_role,
            action=AuditAction.PHI_CREATE,
            resource_type="AllergyIntolerance",
            resource_id=allergy_id,
            patient_id=patient_id,
            details={"substance": substance, "criticality": criticality}
        )

        return AllergyRecord(
            id=allergy_id,
            patient_id=patient_id,
            substance=substance.strip(),
            substance_code=substance_code,
            category=category.lower(),
            criticality=criticality.lower(),
            clinical_status="active",
            reaction_manifestation=reaction,
            severity=severity.lower(),
            onset_date=onset_date or now[:10],
            recorded_by=recorded_by,
            created_at=now
        )

    def get_patient_allergies(
        self,
        patient_id: str,
        actor_id: str,
        actor_role: str
    ) -> List[AllergyRecord]:
        sql = "SELECT * FROM allergies WHERE patient_id = ? AND clinical_status = 'active'"
        rows = self.db.execute_query(sql, (patient_id,))

        self.audit_logger.log_event(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.PHI_READ,
            resource_type="AllergyIntoleranceList",
            resource_id=patient_id,
            patient_id=patient_id,
            details={"count": len(rows)}
        )

        return [
            AllergyRecord(
                id=r["id"],
                patient_id=r["patient_id"],
                substance=r["substance"],
                substance_code=r["substance_code"],
                category=r["category"],
                criticality=r["criticality"],
                clinical_status=r["clinical_status"],
                reaction_manifestation=r["reaction_manifestation"],
                severity=r["severity"],
                onset_date=r["onset_date"],
                recorded_by=r["recorded_by"],
                created_at=r["created_at"]
            )
            for r in rows
        ]

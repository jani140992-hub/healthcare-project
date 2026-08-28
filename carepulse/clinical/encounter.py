"""
Clinical Encounter Lifecycle Management.
Supports Inpatient, Outpatient, Emergency, Ambulatory, and Telehealth Encounters.
"""

import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from carepulse.database import get_db
from carepulse.auth.audit import HIPAALogger, AuditAction

@dataclass
class EncounterRecord:
    id: str
    patient_id: str
    provider_id: str
    encounter_type: str
    status: str
    start_time: str
    class_code: Optional[str] = None
    priority: Optional[str] = "routine"
    service_type: Optional[str] = "general_medicine"
    end_time: Optional[str] = None
    reason_code: Optional[str] = None
    reason_description: Optional[str] = None
    discharge_disposition: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

class EncounterService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()
        self.audit_logger = HIPAALogger(self.db)

    def start_encounter(
        self,
        patient_id: str,
        provider_id: str,
        encounter_type: str,
        actor_id: str,
        actor_role: str,
        priority: str = "routine",
        service_type: str = "general_medicine",
        reason_code: Optional[str] = None,
        reason_description: Optional[str] = None
    ) -> EncounterRecord:
        encounter_id = f"enc_{uuid.uuid4().hex[:12]}"
        now = datetime.now(timezone.utc).isoformat()
        valid_types = ["inpatient", "outpatient", "emergency", "ambulatory", "virtual"]
        if encounter_type.lower() not in valid_types:
            raise ValueError(f"Invalid encounter type '{encounter_type}'. Must be one of: {valid_types}")

        sql = """
        INSERT INTO encounters (
            id, patient_id, provider_id, encounter_type, status,
            priority, service_type, start_time, reason_code,
            reason_description, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                encounter_id, patient_id, provider_id, encounter_type.lower(),
                "in-progress", priority, service_type, now,
                reason_code, reason_description, now, now
            )
        )

        self.audit_logger.log_event(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.PHI_CREATE,
            resource_type="Encounter",
            resource_id=encounter_id,
            patient_id=patient_id,
            details={"type": encounter_type, "provider_id": provider_id}
        )

        return EncounterRecord(
            id=encounter_id,
            patient_id=patient_id,
            provider_id=provider_id,
            encounter_type=encounter_type.lower(),
            status="in-progress",
            priority=priority,
            service_type=service_type,
            start_time=now,
            reason_code=reason_code,
            reason_description=reason_description,
            created_at=now,
            updated_at=now
        )

    def complete_encounter(
        self,
        encounter_id: str,
        actor_id: str,
        actor_role: str,
        discharge_disposition: Optional[str] = "home"
    ) -> bool:
        now = datetime.now(timezone.utc).isoformat()
        query = "SELECT patient_id FROM encounters WHERE id = ?"
        row = self.db.execute_single(query, (encounter_id,))
        if not row:
            return False

        sql = """
        UPDATE encounters
        SET status = 'completed', end_time = ?, discharge_disposition = ?, updated_at = ?
        WHERE id = ?
        """
        self.db.execute_insert(sql, (now, discharge_disposition, now, encounter_id))

        self.audit_logger.log_event(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.PHI_UPDATE,
            resource_type="Encounter",
            resource_id=encounter_id,
            patient_id=row["patient_id"],
            details={"action": "discharge", "disposition": discharge_disposition}
        )
        return True

    def get_patient_encounters(
        self,
        patient_id: str,
        actor_id: str,
        actor_role: str
    ) -> List[EncounterRecord]:
        sql = "SELECT * FROM encounters WHERE patient_id = ? ORDER BY start_time DESC"
        rows = self.db.execute_query(sql, (patient_id,))

        self.audit_logger.log_event(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.PHI_READ,
            resource_type="EncounterList",
            resource_id=patient_id,
            patient_id=patient_id,
            details={"count": len(rows)}
        )

        return [
            EncounterRecord(
                id=r["id"],
                patient_id=r["patient_id"],
                provider_id=r["provider_id"],
                encounter_type=r["encounter_type"],
                status=r["status"],
                class_code=r["class_code"],
                priority=r["priority"],
                service_type=r["service_type"],
                start_time=r["start_time"],
                end_time=r["end_time"],
                reason_code=r["reason_code"],
                reason_description=r["reason_description"],
                discharge_disposition=r["discharge_disposition"],
                created_at=r["created_at"],
                updated_at=r["updated_at"]
            )
            for r in rows
        ]

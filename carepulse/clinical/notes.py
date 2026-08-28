"""
Clinical Documentation & Electronic Signatures.
Manages SOAP (Subjective, Objective, Assessment, Plan) Notes, Progress Notes, and Consultation Reports.
"""

import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from carepulse.database import get_db
from carepulse.auth.audit import HIPAALogger, AuditAction

@dataclass
class ClinicalNoteRecord:
    id: str
    patient_id: str
    encounter_id: str
    author_id: str
    note_type: str
    subjective: Optional[str] = None
    objective: Optional[str] = None
    assessment: Optional[str] = None
    plan: Optional[str] = None
    signed: bool = False
    signed_by: Optional[str] = None
    signed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

class ClinicalNotesService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()
        self.audit_logger = HIPAALogger(self.db)

    def create_soap_note(
        self,
        patient_id: str,
        encounter_id: str,
        author_id: str,
        actor_role: str,
        subjective: str,
        objective: str,
        assessment: str,
        plan: str,
        note_type: str = "soap"
    ) -> ClinicalNoteRecord:
        note_id = f"not_{uuid.uuid4().hex[:12]}"
        now = datetime.now(timezone.utc).isoformat()

        sql = """
        INSERT INTO clinical_notes (
            id, patient_id, encounter_id, author_id, note_type,
            subjective, objective, assessment, plan, signed,
            created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                note_id, patient_id, encounter_id, author_id, note_type.lower(),
                subjective, objective, assessment, plan, now, now
            )
        )

        self.audit_logger.log_event(
            actor_id=author_id,
            actor_role=actor_role,
            action=AuditAction.PHI_CREATE,
            resource_type="DocumentReference/Note",
            resource_id=note_id,
            patient_id=patient_id,
            details={"type": note_type, "encounter_id": encounter_id}
        )

        return ClinicalNoteRecord(
            id=note_id,
            patient_id=patient_id,
            encounter_id=encounter_id,
            author_id=author_id,
            note_type=note_type.lower(),
            subjective=subjective,
            objective=objective,
            assessment=assessment,
            plan=plan,
            signed=False,
            created_at=now,
            updated_at=now
        )

    def sign_note(
        self,
        note_id: str,
        signer_id: str,
        signer_role: str
    ) -> bool:
        now = datetime.now(timezone.utc).isoformat()
        row = self.db.execute_single("SELECT patient_id, signed FROM clinical_notes WHERE id = ?", (note_id,))
        if not row:
            return False
        if row["signed"]:
            raise ValueError("Note has already been signed and locked against further edits")

        sql = """
        UPDATE clinical_notes
        SET signed = 1, signed_by = ?, signed_at = ?, updated_at = ?
        WHERE id = ?
        """
        self.db.execute_insert(sql, (signer_id, now, now, note_id))

        self.audit_logger.log_event(
            actor_id=signer_id,
            actor_role=signer_role,
            action=AuditAction.PHI_UPDATE,
            resource_type="DocumentReference/Note",
            resource_id=note_id,
            patient_id=row["patient_id"],
            details={"action": "electronic_signature", "signed_at": now}
        )
        return True

    def get_notes_for_encounter(
        self,
        encounter_id: str,
        actor_id: str,
        actor_role: str
    ) -> List[ClinicalNoteRecord]:
        sql = "SELECT * FROM clinical_notes WHERE encounter_id = ? ORDER BY created_at ASC"
        rows = self.db.execute_query(sql, (encounter_id,))

        return [
            ClinicalNoteRecord(
                id=r["id"],
                patient_id=r["patient_id"],
                encounter_id=r["encounter_id"],
                author_id=r["author_id"],
                note_type=r["note_type"],
                subjective=r["subjective"],
                objective=r["objective"],
                assessment=r["assessment"],
                plan=r["plan"],
                signed=bool(r["signed"]),
                signed_by=r["signed_by"],
                signed_at=r["signed_at"],
                created_at=r["created_at"],
                updated_at=r["updated_at"]
            )
            for r in rows
        ]

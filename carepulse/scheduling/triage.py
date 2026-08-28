"""
Emergency Department Triage & Acuity Leveling.
Implements the 5-level Emergency Severity Index (ESI) algorithm:
- Level 1: Resuscitation (Immediate life-saving intervention needed)
- Level 2: Emergent (High risk, confused/lethargic/disoriented, severe pain/distress)
- Level 3: Urgent (Requires 2 or more projected resources, vitals stable)
- Level 4: Less Urgent (Requires 1 projected resource)
- Level 5: Non-Urgent (Requires 0 projected resources)
"""

from dataclasses import dataclass
from typing import Optional, List, Dict
import uuid
from datetime import datetime, timezone
from carepulse.database import get_db

@dataclass
class EmergencyTriageRecord:
    id: str
    patient_id: str
    triage_nurse_id: str
    esi_level: int
    chief_complaint: str
    arrival_mode: str
    triage_time: str
    pain_scale: Optional[int]
    mental_status: Optional[str]
    notes: Optional[str]

class TriageService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()

    @staticmethod
    def determine_esi_level(
        requires_immediate_life_support: bool,
        is_high_risk_or_confused: bool,
        estimated_resources: int,
        vitals_in_danger_zone: bool = False
    ) -> int:
        if requires_immediate_life_support:
            return 1
        if is_high_risk_or_confused:
            return 2
        if estimated_resources >= 2:
            if vitals_in_danger_zone:
                return 2  # Step 4 vital sign danger zone up-triage
            return 3
        if estimated_resources == 1:
            return 4
        return 5

    def triage_patient(
        self,
        patient_id: str,
        nurse_id: str,
        chief_complaint: str,
        arrival_mode: str,
        requires_immediate_life_support: bool = False,
        is_high_risk: bool = False,
        estimated_resources: int = 2,
        pain_scale: Optional[int] = 0,
        mental_status: str = "Alert",
        notes: Optional[str] = None
    ) -> EmergencyTriageRecord:
        triage_id = f"trg_{uuid.uuid4().hex[:12]}"
        now = datetime.now(timezone.utc).isoformat()
        esi = self.determine_esi_level(requires_immediate_life_support, is_high_risk, estimated_resources)

        sql = """
        INSERT INTO emergency_triage (
            id, patient_id, triage_nurse_id, esi_level, chief_complaint,
            arrival_mode, triage_time, pain_scale, mental_status, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                triage_id, patient_id, nurse_id, esi, chief_complaint,
                arrival_mode, now, pain_scale, mental_status, notes
            )
        )

        return EmergencyTriageRecord(
            id=triage_id,
            patient_id=patient_id,
            triage_nurse_id=nurse_id,
            esi_level=esi,
            chief_complaint=chief_complaint,
            arrival_mode=arrival_mode,
            triage_time=now,
            pain_scale=pain_scale,
            mental_status=mental_status,
            notes=notes
        )

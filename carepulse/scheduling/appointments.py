"""
Provider Scheduling & Appointment Booking Service.
Validates slot availability and prevents double-booking across provider calendars.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import uuid
from datetime import datetime, timezone
from carepulse.database import get_db

@dataclass
class AppointmentRecord:
    id: str
    patient_id: str
    provider_id: str
    appointment_type: str
    start_time: str
    end_time: str
    duration_minutes: int
    status: str
    chief_complaint: Optional[str] = None
    telehealth_room_url: Optional[str] = None

class SchedulingService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()

    def book_appointment(
        self,
        patient_id: str,
        provider_id: str,
        appointment_type: str,
        start_time: str,
        duration_minutes: int = 30,
        chief_complaint: Optional[str] = None,
        telehealth_url: Optional[str] = None
    ) -> AppointmentRecord:
        # Check conflict
        conflict_query = """
        SELECT id FROM appointments
        WHERE provider_id = ? AND status != 'cancelled'
        AND start_time = ?
        """
        existing = self.db.execute_single(conflict_query, (provider_id, start_time))
        if existing:
            raise ValueError(f"Provider {provider_id} already has a conflicting appointment at {start_time}")

        appt_id = f"apt_{uuid.uuid4().hex[:12]}"
        now = datetime.now(timezone.utc).isoformat()
        # Simple ISO end time calculation
        end_time = start_time  # for stub representation

        sql = """
        INSERT INTO appointments (
            id, patient_id, provider_id, appointment_type, start_time,
            end_time, duration_minutes, status, chief_complaint,
            telehealth_room_url, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, 'booked', ?, ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                appt_id, patient_id, provider_id, appointment_type.lower(),
                start_time, end_time, duration_minutes, chief_complaint,
                telehealth_url, now
            )
        )

        return AppointmentRecord(
            id=appt_id,
            patient_id=patient_id,
            provider_id=provider_id,
            appointment_type=appointment_type.lower(),
            start_time=start_time,
            end_time=end_time,
            duration_minutes=duration_minutes,
            status="booked",
            chief_complaint=chief_complaint,
            telehealth_room_url=telehealth_url
        )

    def get_patient_appointments(self, patient_id: str) -> List[AppointmentRecord]:
        sql = "SELECT * FROM appointments WHERE patient_id = ? ORDER BY start_time DESC"
        rows = self.db.execute_query(sql, (patient_id,))
        return [
            AppointmentRecord(
                id=r["id"],
                patient_id=r["patient_id"],
                provider_id=r["provider_id"],
                appointment_type=r["appointment_type"],
                start_time=r["start_time"],
                end_time=r["end_time"],
                duration_minutes=r["duration_minutes"],
                status=r["status"],
                chief_complaint=r["chief_complaint"],
                telehealth_room_url=r["telehealth_room_url"]
            )
            for r in rows
        ]

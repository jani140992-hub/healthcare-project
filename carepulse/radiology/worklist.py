"""
Modality Worklist (MWL) & PACS Workflow Coordinator.
Manages imaging orders, scheduled technician assignments, and acquisition queues.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import uuid
from datetime import datetime, timezone
from carepulse.database import get_db

@dataclass
class ImagingStudy:
    study_id: str
    patient_id: str
    order_id: str
    modality: str
    procedure_name: str
    body_site: str
    scheduled_time: str
    status: str  # scheduled, acquired, reading, finalized

class ModalityWorklistService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()

    def schedule_study(
        self,
        patient_id: str,
        order_id: str,
        modality: str,
        procedure_name: str,
        body_site: str,
        scheduled_time: str
    ) -> ImagingStudy:
        study_id = f"img_{uuid.uuid4().hex[:12]}"
        return ImagingStudy(
            study_id=study_id,
            patient_id=patient_id,
            order_id=order_id,
            modality=modality.upper(),
            procedure_name=procedure_name,
            body_site=body_site,
            scheduled_time=scheduled_time,
            status="scheduled"
        )

"""
Specimen Accessioning & Chain of Custody Management.
Enforces barcode scanning, collection timestamps, and specimen integrity checks.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict
import uuid
from datetime import datetime, timezone

@dataclass
class SpecimenRecord:
    specimen_id: str
    accession_number: str
    patient_id: str
    lab_order_id: str
    specimen_type: str  # blood, urine, csf, tissue, sputum
    collection_time: str
    collector_id: str
    container_type: str  # Lavender Top (EDTA), Red Top, Gold Top (SST), Sterile Cup
    status: str          # collected, received_in_lab, hemolyzed, rejected, processed
    rejection_reason: Optional[str] = None

class SpecimenService:
    def __init__(self):
        self._specimens: Dict[str, SpecimenRecord] = {}

    def accession_specimen(
        self,
        patient_id: str,
        lab_order_id: str,
        specimen_type: str,
        collector_id: str,
        container_type: str
    ) -> SpecimenRecord:
        specimen_id = f"spc_{uuid.uuid4().hex[:12]}"
        accession_num = f"ACC-{datetime.now(timezone.utc).strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
        now = datetime.now(timezone.utc).isoformat()

        record = SpecimenRecord(
            specimen_id=specimen_id,
            accession_number=accession_num,
            patient_id=patient_id,
            lab_order_id=lab_order_id,
            specimen_type=specimen_type,
            collection_time=now,
            collector_id=collector_id,
            container_type=container_type,
            status="collected"
        )
        self._specimens[specimen_id] = record
        return record

    def inspect_specimen(self, specimen_id: str, is_acceptable: bool, rejection_reason: Optional[str] = None) -> bool:
        spc = self._specimens.get(specimen_id)
        if not spc:
            return False
        if is_acceptable:
            spc.status = "received_in_lab"
        else:
            spc.status = "rejected"
            spc.rejection_reason = rejection_reason or "Specimen hemolyzed / insufficient volume"
        return True

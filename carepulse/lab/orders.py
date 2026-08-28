"""
Laboratory Order Lifecycle Management.
Tracks LOINC laboratory test requisitions from ordering to specimen accessioning.
"""

from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from carepulse.database import get_db

@dataclass
class LabOrderRecord:
    id: str
    patient_id: str
    ordering_provider_id: str
    loinc_code: str
    test_name: str
    specimen_type: str
    priority: str
    status: str
    order_date: str
    encounter_id: Optional[str] = None
    panel_name: Optional[str] = None
    collected_date: Optional[str] = None

class LabOrderService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()

    def get_orders_by_patient(self, patient_id: str) -> List[LabOrderRecord]:
        sql = "SELECT * FROM lab_orders WHERE patient_id = ? ORDER BY order_date DESC"
        rows = self.db.execute_query(sql, (patient_id,))
        return [
            LabOrderRecord(
                id=r["id"],
                patient_id=r["patient_id"],
                encounter_id=r["encounter_id"],
                ordering_provider_id=r["ordering_provider_id"],
                loinc_code=r["loinc_code"],
                test_name=r["test_name"],
                panel_name=r["panel_name"],
                specimen_type=r["specimen_type"],
                priority=r["priority"],
                status=r["status"],
                order_date=r["order_date"],
                collected_date=r["collected_date"]
            )
            for r in rows
        ]

    def update_order_status(self, order_id: str, new_status: str) -> bool:
        sql = "UPDATE lab_orders SET status = ? WHERE id = ?"
        self.db.execute_insert(sql, (new_status.lower(), order_id))
        return True

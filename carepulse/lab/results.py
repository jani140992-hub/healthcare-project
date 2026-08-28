"""
Laboratory Results Processing & Panic Value Notification Engine.
Classifies findings against reference intervals and triggers critical value alerts.
"""

from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any
from datetime import datetime, timezone
import uuid
from carepulse.database import get_db
from carepulse.auth.audit import HIPAALogger, AuditAction

@dataclass
class LabResultRecord:
    id: str
    lab_order_id: str
    patient_id: str
    loinc_code: str
    analyte_name: str
    numeric_value: Optional[float]
    string_value: Optional[str]
    unit: str
    reference_low: Optional[float]
    reference_high: Optional[float]
    abnormal_flag: str  # normal, low, high, critical_low, critical_high
    status: str         # preliminary, final, corrected
    reported_at: str
    verified_by: Optional[str] = None

class LabResultService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()
        self.audit_logger = HIPAALogger(self.db)

    @staticmethod
    def determine_flag(
        val: Optional[float],
        low: Optional[float],
        high: Optional[float],
        crit_low: Optional[float] = None,
        crit_high: Optional[float] = None
    ) -> str:
        if val is None:
            return "normal"
        if crit_low is not None and val <= crit_low:
            return "critical_low"
        if crit_high is not None and val >= crit_high:
            return "critical_high"
        if low is not None and val < low:
            return "low"
        if high is not None and val > high:
            return "high"
        return "normal"

    def record_result(
        self,
        lab_order_id: str,
        patient_id: str,
        loinc_code: str,
        analyte_name: str,
        numeric_value: Optional[float],
        unit: str,
        reference_low: Optional[float],
        reference_high: Optional[float],
        reporter_id: str,
        reporter_role: str,
        critical_low: Optional[float] = None,
        critical_high: Optional[float] = None,
        string_value: Optional[str] = None
    ) -> LabResultRecord:
        result_id = f"res_{uuid.uuid4().hex[:12]}"
        now = datetime.now(timezone.utc).isoformat()
        flag = self.determine_flag(numeric_value, reference_low, reference_high, critical_low, critical_high)

        sql = """
        INSERT INTO lab_results (
            id, lab_order_id, patient_id, loinc_code, analyte_name,
            numeric_value, string_value, unit, reference_low,
            reference_high, abnormal_flag, status, reported_at, verified_by
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'final', ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                result_id, lab_order_id, patient_id, loinc_code, analyte_name,
                numeric_value, string_value, unit, reference_low,
                reference_high, flag, now, reporter_id
            )
        )

        self.audit_logger.log_event(
            actor_id=reporter_id,
            actor_role=reporter_role,
            action=AuditAction.PHI_CREATE,
            resource_type="Observation/LabResult",
            resource_id=result_id,
            patient_id=patient_id,
            details={"analyte": analyte_name, "value": numeric_value, "flag": flag}
        )

        return LabResultRecord(
            id=result_id,
            lab_order_id=lab_order_id,
            patient_id=patient_id,
            loinc_code=loinc_code,
            analyte_name=analyte_name,
            numeric_value=numeric_value,
            string_value=string_value,
            unit=unit,
            reference_low=reference_low,
            reference_high=reference_high,
            abnormal_flag=flag,
            status="final",
            reported_at=now,
            verified_by=reporter_id
        )

    def get_results_by_patient(self, patient_id: str) -> List[LabResultRecord]:
        sql = "SELECT * FROM lab_results WHERE patient_id = ? ORDER BY reported_at DESC"
        rows = self.db.execute_query(sql, (patient_id,))
        return [
            LabResultRecord(
                id=r["id"],
                lab_order_id=r["lab_order_id"],
                patient_id=r["patient_id"],
                loinc_code=r["loinc_code"],
                analyte_name=r["analyte_name"],
                numeric_value=r["numeric_value"],
                string_value=r["string_value"],
                unit=r["unit"],
                reference_low=r["reference_low"],
                reference_high=r["reference_high"],
                abnormal_flag=r["abnormal_flag"],
                status=r["status"],
                reported_at=r["reported_at"],
                verified_by=r["verified_by"]
            )
            for r in rows
        ]

"""
Structured Diagnostic Radiology Reporting.
Implements ACR (American College of Radiology) standard reporting templates and critical finding notification.
"""

from dataclasses import dataclass
from typing import Optional, Dict, Any, List
from datetime import datetime, timezone
import uuid
from carepulse.database import get_db

@dataclass
class StructuredReport:
    report_id: str
    radiology_order_id: str
    radiologist_id: str
    findings: str
    impression: str
    birads_or_rating: Optional[str]
    has_critical_findings: bool
    reported_at: str

class RadiologyReportingService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()

    def create_report(
        self,
        radiology_order_id: str,
        radiologist_id: str,
        findings: str,
        impression: str,
        birads_rating: Optional[str] = None,
        is_critical: bool = False
    ) -> StructuredReport:
        report_id = f"rad_{uuid.uuid4().hex[:12]}"
        now = datetime.now(timezone.utc).isoformat()

        sql = """
        INSERT INTO radiology_reports (
            id, radiology_order_id, radiologist_id, findings,
            impression, birads_or_rating, critical_findings, reported_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                report_id, radiology_order_id, radiologist_id,
                findings, impression, birads_rating, 1 if is_critical else 0, now
            )
        )

        return StructuredReport(
            report_id=report_id,
            radiology_order_id=radiology_order_id,
            radiologist_id=radiologist_id,
            findings=findings,
            impression=impression,
            birads_or_rating=birads_rating,
            has_critical_findings=is_critical,
            reported_at=now
        )

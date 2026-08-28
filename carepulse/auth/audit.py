"""
HIPAA Title II Audit Logging Engine (45 CFR § 164.312(b)).
Maintains an immutable, cryptographically chained (SHA-256) audit trail of all PHI access.
"""

import hashlib
import json
import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Optional, Dict, Any, List, Tuple
from carepulse.database import get_db

class AuditAction(str, Enum):
    PHI_READ = "PHI_READ"
    PHI_CREATE = "PHI_CREATE"
    PHI_UPDATE = "PHI_UPDATE"
    PHI_DELETE = "PHI_DELETE"
    PHI_EXPORT = "PHI_EXPORT"
    LOGIN_SUCCESS = "LOGIN_SUCCESS"
    LOGIN_FAILURE = "LOGIN_FAILURE"
    LOGOUT = "LOGOUT"
    PASSWORD_CHANGE = "PASSWORD_CHANGE"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    ORDER_SUBMITTED = "ORDER_SUBMITTED"
    PRESCRIPTION_FILLED = "PRESCRIPTION_FILLED"

class HIPAALogger:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()

    def _get_latest_hash(self) -> str:
        query = "SELECT entry_hash FROM hipaa_audit_log ORDER BY id DESC LIMIT 1"
        row = self.db.execute_single(query)
        if row and row.get("entry_hash"):
            return row["entry_hash"]
        return "GENESIS_HASH_CAREPULSE_EHR_SYSTEM_2026"

    def _compute_hash(self, prev_hash: str, payload_str: str) -> str:
        hasher = hashlib.sha256()
        hasher.update(prev_hash.encode("utf-8"))
        hasher.update(payload_str.encode("utf-8"))
        return hasher.hexdigest()

    def log_event(
        self,
        actor_id: str,
        actor_role: str,
        action: AuditAction,
        resource_type: str,
        resource_id: str,
        patient_id: Optional[str] = None,
        ip_address: Optional[str] = "127.0.0.1",
        details: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Appends an immutable audit log entry linked to the previous entry hash.
        """
        log_id = f"aud_{uuid.uuid4().hex[:12]}"
        timestamp = datetime.now(timezone.utc).isoformat()
        details_str = json.dumps(details or {}, sort_keys=True)
        prev_hash = self._get_latest_hash()

        record_content = f"{log_id}:{timestamp}:{actor_id}:{actor_role}:{action.value}:{resource_type}:{resource_id}:{patient_id or ''}:{ip_address or ''}:{details_str}"
        entry_hash = self._compute_hash(prev_hash, record_content)

        sql = """
        INSERT INTO hipaa_audit_log (
            log_id, timestamp, actor_id, actor_role, action,
            resource_type, resource_id, patient_id, ip_address,
            details, previous_hash, entry_hash
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                log_id, timestamp, actor_id, actor_role, action.value,
                resource_type, resource_id, patient_id, ip_address,
                details_str, prev_hash, entry_hash
            )
        )
        return log_id

    def verify_integrity(self) -> Tuple[bool, Optional[str]]:
        """
        Verifies the cryptographic integrity of the entire audit chain.
        Returns (is_valid, error_description).
        """
        query = "SELECT * FROM hipaa_audit_log ORDER BY id ASC"
        rows = self.db.execute_query(query)
        if not rows:
            return True, None

        expected_prev_hash = "GENESIS_HASH_CAREPULSE_EHR_SYSTEM_2026"
        for row in rows:
            if row["previous_hash"] != expected_prev_hash:
                return False, f"Broken chain at log_id {row['log_id']}: previous hash mismatch"

            record_content = (
                f"{row['log_id']}:{row['timestamp']}:{row['actor_id']}:{row['actor_role']}:"
                f"{row['action']}:{row['resource_type']}:{row['resource_id']}:"
                f"{row['patient_id'] or ''}:{row['ip_address'] or ''}:{row['details']}"
            )
            recalculated = self._compute_hash(expected_prev_hash, record_content)
            if recalculated != row["entry_hash"]:
                return False, f"Tampered entry detected at log_id {row['log_id']}: computed {recalculated} != stored {row['entry_hash']}"

            expected_prev_hash = row["entry_hash"]

        return True, None

    def get_recent_logs(self, limit: int = 100, patient_id: Optional[str] = None) -> List[Dict[str, Any]]:
        if patient_id:
            sql = "SELECT * FROM hipaa_audit_log WHERE patient_id = ? ORDER BY id DESC LIMIT ?"
            return self.db.execute_query(sql, (patient_id, limit))
        sql = "SELECT * FROM hipaa_audit_log ORDER BY id DESC LIMIT ?"
        return self.db.execute_query(sql, (limit,))

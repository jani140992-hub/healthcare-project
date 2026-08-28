"""
Authentication & User Identity Service.
Implements PBKDF2-HMAC-SHA256 secure password hashing, JWT generation,
and brute-force lockout protection compliant with HIPAA § 164.308(a)(5)(ii)(D).
"""

import os
import hmac
import hashlib
import base64
import json
import time
import uuid
from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, Any, Tuple
from carepulse.database import get_db
from carepulse.config import get_config
from carepulse.auth.models import User, Role
from carepulse.auth.audit import HIPAALogger, AuditAction

class AuthService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()
        self.config = get_config()
        self.audit_logger = HIPAALogger(self.db)

    def _hash_password(self, password: str, salt: Optional[str] = None) -> Tuple[str, str]:
        if salt is None:
            salt = os.urandom(16).hex()
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        )
        return key.hex(), salt

    def _verify_password(self, password: str, salt: str, expected_hash: str) -> bool:
        key, _ = self._hash_password(password, salt)
        return hmac.compare_digest(key, expected_hash)

    def _create_jwt(self, payload: Dict[str, Any]) -> str:
        header = {"alg": "HS256", "typ": "JWT"}
        header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")
        payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
        signature_base = f"{header_b64}.{payload_b64}".encode()
        secret = self.config.security.secret_key.encode()
        signature = hmac.new(secret, signature_base, hashlib.sha256).digest()
        sig_b64 = base64.urlsafe_b64encode(signature).decode().rstrip("=")
        return f"{header_b64}.{payload_b64}.{sig_b64}"

    def decode_jwt(self, token: str) -> Optional[Dict[str, Any]]:
        parts = token.split(".")
        if len(parts) != 3:
            return None
        header_b64, payload_b64, sig_b64 = parts
        try:
            signature_base = f"{header_b64}.{payload_b64}".encode()
            secret = self.config.security.secret_key.encode()
            expected_sig = hmac.new(secret, signature_base, hashlib.sha256).digest()
            actual_sig = base64.urlsafe_b64decode(sig_b64 + "==")
            if not hmac.compare_digest(expected_sig, actual_sig):
                return None
            payload_json = base64.urlsafe_b64decode(payload_b64 + "==").decode()
            payload = json.loads(payload_json)
            # Check expiry
            if payload.get("exp") and time.time() > payload["exp"]:
                return None
            return payload
        except Exception:
            return None

    def register_user(
        self,
        username: str,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        role: Role,
        department: Optional[str] = None,
        npi_number: Optional[str] = None,
        dea_number: Optional[str] = None
    ) -> User:
        user_id = f"usr_{uuid.uuid4().hex[:12]}"
        password_hash, salt = self._hash_password(password)
        now = datetime.now(timezone.utc).isoformat()

        sql = """
        INSERT INTO users (
            id, username, email, password_hash, salt, first_name,
            last_name, role, department, npi_number, dea_number,
            created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                user_id, username.lower().strip(), email.lower().strip(),
                password_hash, salt, first_name, last_name, role.value,
                department, npi_number, dea_number, now, now
            )
        )
        return User(
            id=user_id,
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role,
            department=department,
            npi_number=npi_number,
            dea_number=dea_number,
            created_at=now,
            updated_at=now
        )

    def authenticate(self, username: str, password: str, ip_address: str = "127.0.0.1") -> Optional[Tuple[User, str]]:
        query = "SELECT * FROM users WHERE username = ? OR email = ?"
        row = self.db.execute_single(query, (username.lower().strip(), username.lower().strip()))
        if not row:
            self.audit_logger.log_event(
                actor_id="anonymous",
                actor_role="unknown",
                action=AuditAction.LOGIN_FAILURE,
                resource_type="auth",
                resource_id="login",
                ip_address=ip_address,
                details={"reason": "User not found", "attempted_username": username}
            )
            return None

        user_id = row["id"]
        # Check lockout
        if row["locked_until"]:
            try:
                locked_until_dt = datetime.fromisoformat(row["locked_until"])
                if datetime.now(timezone.utc) < locked_until_dt:
                    return None
            except Exception:
                pass

        if not self._verify_password(password, row["salt"], row["password_hash"]):
            failed = row["failed_login_attempts"] + 1
            locked_until = None
            if failed >= self.config.security.max_login_attempts:
                lock_delta = timedelta(minutes=self.config.security.lockout_duration_minutes)
                locked_until = (datetime.now(timezone.utc) + lock_delta).isoformat()

            self.db.execute_insert(
                "UPDATE users SET failed_login_attempts = ?, locked_until = ? WHERE id = ?",
                (failed, locked_until, user_id)
            )
            self.audit_logger.log_event(
                actor_id=user_id,
                actor_role=row["role"],
                action=AuditAction.LOGIN_FAILURE,
                resource_type="auth",
                resource_id=user_id,
                ip_address=ip_address,
                details={"failed_attempts": failed, "locked": locked_until is not None}
            )
            return None

        # Reset failed attempts on success
        self.db.execute_insert(
            "UPDATE users SET failed_login_attempts = 0, locked_until = NULL WHERE id = ?",
            (user_id,)
        )

        user = User(
            id=row["id"],
            username=row["username"],
            email=row["email"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            role=Role(row["role"]),
            department=row["department"],
            npi_number=row["npi_number"],
            dea_number=row["dea_number"],
            is_active=bool(row["is_active"])
        )

        exp = int(time.time()) + (self.config.security.jwt_expiration_minutes * 60)
        token_payload = {
            "sub": user.id,
            "username": user.username,
            "role": user.role.value,
            "exp": exp,
            "iat": int(time.time())
        }
        token = self._create_jwt(token_payload)

        self.audit_logger.log_event(
            actor_id=user.id,
            actor_role=user.role.value,
            action=AuditAction.LOGIN_SUCCESS,
            resource_type="auth",
            resource_id=user.id,
            ip_address=ip_address,
            details={"token_expires": exp}
        )
        return user, token

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        query = "SELECT * FROM users WHERE id = ?"
        row = self.db.execute_single(query, (user_id,))
        if not row:
            return None
        return User(
            id=row["id"],
            username=row["username"],
            email=row["email"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            role=Role(row["role"]),
            department=row["department"],
            npi_number=row["npi_number"],
            dea_number=row["dea_number"],
            is_active=bool(row["is_active"]),
            created_at=row["created_at"],
            updated_at=row["updated_at"]
        )

"""
Master Patient Index (MPI) and Patient Demographics Management.
Compliant with USCDI v3 and FHIR R4 Patient Resource requirements.
"""

import uuid
import re
import hashlib
from dataclasses import dataclass, asdict
from datetime import datetime, timezone, date
from typing import Optional, List, Dict, Any
from carepulse.database import get_db
from carepulse.auth.audit import HIPAALogger, AuditAction

@dataclass
class PatientRecord:
    id: str
    mrn: str
    first_name: str
    last_name: str
    date_of_birth: str
    gender: str
    middle_name: Optional[str] = None
    ssn_hash: Optional[str] = None
    blood_type: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address_street: Optional[str] = None
    address_city: Optional[str] = None
    address_state: Optional[str] = None
    address_postal_code: Optional[str] = None
    address_country: Optional[str] = "USA"
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    emergency_contact_relation: Optional[str] = None
    primary_care_provider_id: Optional[str] = None
    is_deceased: bool = False
    deceased_datetime: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    @property
    def full_name(self) -> str:
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self) -> int:
        try:
            born = datetime.strptime(self.date_of_birth, "%Y-%m-%d").date()
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        except Exception:
            return 0

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["full_name"] = self.full_name
        d["age"] = self.age
        # Never expose raw ssn_hash in clinical serialization
        d.pop("ssn_hash", None)
        return d

class PatientService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()
        self.audit_logger = HIPAALogger(self.db)

    def _generate_mrn(self) -> str:
        """
        Generates a unique 9-digit Medical Record Number with Luhn-like check.
        """
        raw_num = f"{uuid.uuid4().int % 100000000:08d}"
        checksum = sum(int(digit) * (2 if idx % 2 == 0 else 1) for idx, digit in enumerate(raw_num)) % 10
        return f"MRN-{raw_num}{checksum}"

    def register_patient(
        self,
        first_name: str,
        last_name: str,
        date_of_birth: str,
        gender: str,
        actor_id: str,
        actor_role: str,
        middle_name: Optional[str] = None,
        ssn: Optional[str] = None,
        blood_type: Optional[str] = None,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        address_street: Optional[str] = None,
        address_city: Optional[str] = None,
        address_state: Optional[str] = None,
        address_postal_code: Optional[str] = None,
        emergency_name: Optional[str] = None,
        emergency_phone: Optional[str] = None,
        emergency_relation: Optional[str] = None,
        pcp_id: Optional[str] = None
    ) -> PatientRecord:
        # Validate Date of Birth (YYYY-MM-DD)
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_of_birth):
            raise ValueError(f"Invalid date of birth format: {date_of_birth}. Expected YYYY-MM-DD")

        # Validate Gender according to HL7 AdministrativeGender
        normalized_gender = gender.lower()
        if normalized_gender not in ["male", "female", "other", "unknown"]:
            raise ValueError(f"Invalid gender: {gender}. Must be male, female, other, or unknown")

        patient_id = f"pat_{uuid.uuid4().hex[:12]}"
        mrn = self._generate_mrn()
        ssn_hash = hashlib.sha256(ssn.strip().encode()).hexdigest() if ssn else None
        now = datetime.now(timezone.utc).isoformat()

        sql = """
        INSERT INTO patients (
            id, mrn, ssn_hash, first_name, middle_name, last_name,
            date_of_birth, gender, blood_type, phone, email,
            address_street, address_city, address_state, address_postal_code,
            address_country, emergency_contact_name, emergency_contact_phone,
            emergency_contact_relation, primary_care_provider_id,
            is_deceased, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                patient_id, mrn, ssn_hash, first_name.strip(), middle_name.strip() if middle_name else None,
                last_name.strip(), date_of_birth, normalized_gender, blood_type,
                phone, email, address_street, address_city, address_state, address_postal_code,
                "USA", emergency_name, emergency_phone, emergency_relation, pcp_id, now, now
            )
        )

        self.audit_logger.log_event(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.PHI_CREATE,
            resource_type="Patient",
            resource_id=patient_id,
            patient_id=patient_id,
            details={"mrn": mrn, "name": f"{first_name} {last_name}"}
        )

        return PatientRecord(
            id=patient_id,
            mrn=mrn,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=normalized_gender,
            ssn_hash=ssn_hash,
            blood_type=blood_type,
            phone=phone,
            email=email,
            address_street=address_street,
            address_city=address_city,
            address_state=address_state,
            address_postal_code=address_postal_code,
            emergency_contact_name=emergency_name,
            emergency_contact_phone=emergency_phone,
            emergency_contact_relation=emergency_relation,
            primary_care_provider_id=pcp_id,
            created_at=now,
            updated_at=now
        )

    def get_patient(self, patient_id: str, actor_id: str, actor_role: str) -> Optional[PatientRecord]:
        query = "SELECT * FROM patients WHERE id = ? OR mrn = ?"
        row = self.db.execute_single(query, (patient_id, patient_id))
        if not row:
            return None

        self.audit_logger.log_event(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.PHI_READ,
            resource_type="Patient",
            resource_id=row["id"],
            patient_id=row["id"],
            details={"mrn": row["mrn"]}
        )

        return self._row_to_record(row)

    def search_patients(
        self,
        query_str: str,
        actor_id: str,
        actor_role: str,
        limit: int = 50
    ) -> List[PatientRecord]:
        q = f"%{query_str.strip()}%"
        sql = """
        SELECT * FROM patients
        WHERE first_name LIKE ? OR last_name LIKE ? OR mrn LIKE ? OR phone LIKE ? OR email LIKE ?
        ORDER BY last_name ASC, first_name ASC LIMIT ?
        """
        rows = self.db.execute_query(sql, (q, q, q, q, q, limit))

        self.audit_logger.log_event(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.PHI_READ,
            resource_type="PatientList",
            resource_id="search",
            details={"query": query_str, "results_count": len(rows)}
        )

        return [self._row_to_record(row) for row in rows]

    def _row_to_record(self, row: Dict[str, Any]) -> PatientRecord:
        return PatientRecord(
            id=row["id"],
            mrn=row["mrn"],
            first_name=row["first_name"],
            middle_name=row["middle_name"],
            last_name=row["last_name"],
            date_of_birth=row["date_of_birth"],
            gender=row["gender"],
            blood_type=row["blood_type"],
            phone=row["phone"],
            email=row["email"],
            address_street=row["address_street"],
            address_city=row["address_city"],
            address_state=row["address_state"],
            address_postal_code=row["address_postal_code"],
            address_country=row["address_country"],
            emergency_contact_name=row["emergency_contact_name"],
            emergency_contact_phone=row["emergency_contact_phone"],
            emergency_contact_relation=row["emergency_contact_relation"],
            primary_care_provider_id=row["primary_care_provider_id"],
            is_deceased=bool(row["is_deceased"]),
            deceased_datetime=row["deceased_datetime"],
            created_at=row["created_at"],
            updated_at=row["updated_at"]
        )

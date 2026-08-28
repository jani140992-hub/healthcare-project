"""
User, Role, and Security Models for CarePulse Healthcare System.
Includes Role-Based Access Control (RBAC) definitions matching HIPAA security rules.
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

class Role(str, Enum):
    SYSTEM_ADMIN = "system_admin"
    ATTENDING_PHYSICIAN = "attending_physician"
    RESIDENT_PHYSICIAN = "resident_physician"
    NURSE_PRACTITIONER = "nurse_practitioner"
    REGISTERED_NURSE = "registered_nurse"
    CLINICAL_PHARMACIST = "clinical_pharmacist"
    LAB_TECHNICIAN = "lab_technician"
    RADIOLOGIST = "radiologist"
    BILLING_SPECIALIST = "billing_specialist"
    MEDICAL_RECORDS_CLERK = "medical_records_clerk"
    PATIENT = "patient"

class Permission(str, Enum):
    # Patient PHI Access
    PATIENT_READ = "patient:read"
    PATIENT_WRITE = "patient:write"
    PATIENT_DELETE = "patient:delete"
    PATIENT_EXPORT = "patient:export"
    
    # Clinical Encounters & Notes
    ENCOUNTER_READ = "encounter:read"
    ENCOUNTER_WRITE = "encounter:write"
    CLINICAL_NOTE_SIGN = "clinical_note:sign"
    
    # Orders & Prescriptions
    CPOE_ORDER = "cpoe:order"
    PRESCRIPTION_WRITE = "prescription:write"
    PRESCRIPTION_DISPENSE = "prescription:dispense"
    
    # Laboratory & Diagnostics
    LAB_ORDER = "lab:order"
    LAB_ENTER_RESULTS = "lab:enter_results"
    LAB_VERIFY_RESULTS = "lab:verify_results"
    
    # Radiology & Imaging
    RADIOLOGY_ORDER = "radiology:order"
    RADIOLOGY_REPORT = "radiology:report"
    
    # Financial & Billing
    BILLING_READ = "billing:read"
    BILLING_SUBMIT_CLAIM = "billing:submit_claim"
    
    # Audit & Security Administration
    AUDIT_LOG_READ = "audit:read"
    USER_MANAGE = "user:manage"
    SYSTEM_CONFIG = "system:config"

# RBAC Matrix mapping Roles to Permissions
ROLE_PERMISSIONS: dict[Role, list[Permission]] = {
    Role.SYSTEM_ADMIN: [
        Permission.PATIENT_READ,
        Permission.AUDIT_LOG_READ,
        Permission.USER_MANAGE,
        Permission.SYSTEM_CONFIG,
    ],
    Role.ATTENDING_PHYSICIAN: [
        Permission.PATIENT_READ,
        Permission.PATIENT_WRITE,
        Permission.ENCOUNTER_READ,
        Permission.ENCOUNTER_WRITE,
        Permission.CLINICAL_NOTE_SIGN,
        Permission.CPOE_ORDER,
        Permission.PRESCRIPTION_WRITE,
        Permission.LAB_ORDER,
        Permission.RADIOLOGY_ORDER,
        Permission.AUDIT_LOG_READ,
    ],
    Role.RESIDENT_PHYSICIAN: [
        Permission.PATIENT_READ,
        Permission.PATIENT_WRITE,
        Permission.ENCOUNTER_READ,
        Permission.ENCOUNTER_WRITE,
        Permission.CPOE_ORDER,
        Permission.PRESCRIPTION_WRITE,
        Permission.LAB_ORDER,
        Permission.RADIOLOGY_ORDER,
    ],
    Role.NURSE_PRACTITIONER: [
        Permission.PATIENT_READ,
        Permission.PATIENT_WRITE,
        Permission.ENCOUNTER_READ,
        Permission.ENCOUNTER_WRITE,
        Permission.CLINICAL_NOTE_SIGN,
        Permission.CPOE_ORDER,
        Permission.PRESCRIPTION_WRITE,
        Permission.LAB_ORDER,
    ],
    Role.REGISTERED_NURSE: [
        Permission.PATIENT_READ,
        Permission.PATIENT_WRITE,
        Permission.ENCOUNTER_READ,
        Permission.ENCOUNTER_WRITE,
        Permission.LAB_ORDER,
    ],
    Role.CLINICAL_PHARMACIST: [
        Permission.PATIENT_READ,
        Permission.ENCOUNTER_READ,
        Permission.PRESCRIPTION_DISPENSE,
    ],
    Role.LAB_TECHNICIAN: [
        Permission.PATIENT_READ,
        Permission.LAB_ENTER_RESULTS,
        Permission.LAB_VERIFY_RESULTS,
    ],
    Role.RADIOLOGIST: [
        Permission.PATIENT_READ,
        Permission.RADIOLOGY_REPORT,
    ],
    Role.BILLING_SPECIALIST: [
        Permission.PATIENT_READ,
        Permission.BILLING_READ,
        Permission.BILLING_SUBMIT_CLAIM,
    ],
    Role.MEDICAL_RECORDS_CLERK: [
        Permission.PATIENT_READ,
        Permission.PATIENT_WRITE,
    ],
    Role.PATIENT: [
        Permission.PATIENT_READ,
        Permission.ENCOUNTER_READ,
        Permission.BILLING_READ,
    ],
}

@dataclass
class User:
    id: str
    username: str
    email: str
    first_name: str
    last_name: str
    role: Role
    department: Optional[str] = None
    npi_number: Optional[str] = None
    dea_number: Optional[str] = None
    is_active: bool = True
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def has_permission(self, permission: Permission) -> bool:
        allowed = ROLE_PERMISSIONS.get(self.role, [])
        return permission in allowed

@dataclass
class AuthToken:
    access_token: str
    token_type: str = "Bearer"
    expires_in_seconds: int = 3600
    user_id: str = ""
    role: str = ""

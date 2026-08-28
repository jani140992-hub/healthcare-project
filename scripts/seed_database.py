"""
Database Seeding Script for CarePulse Healthcare System.
Populates an initial clinic database with clinical departments, providers, sample patients, and clinical records.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from carepulse.database import get_db
from carepulse.auth.service import AuthService
from carepulse.auth.models import Role
from carepulse.synthetic.cohort_builder import CohortBuilder

def seed():
    print("[*] Initializing CarePulse Database...")
    db = get_db()
    auth_svc = AuthService(db)

    print("[*] Creating administrative and clinical staff accounts...")
    admin = auth_svc.register_user(
        username="admin",
        email="admin@carepulse.org",
        password="AdminSecure2026!",
        first_name="Hospital",
        last_name="Administrator",
        role=Role.SYSTEM_ADMIN,
        department="Information Technology"
    )

    doc = auth_svc.register_user(
        username="dr.smith",
        email="dr.smith@carepulse.org",
        password="PhysicianPass2026!",
        first_name="Sarah",
        last_name="Smith",
        role=Role.ATTENDING_PHYSICIAN,
        department="Internal Medicine",
        npi_number="1892837465",
        dea_number="BS1928374"
    )

    nurse = auth_svc.register_user(
        username="nurse.patel",
        email="nurse.patel@carepulse.org",
        password="NursePass2026!",
        first_name="Priya",
        last_name="Patel",
        role=Role.REGISTERED_NURSE,
        department="Inpatient Medical/Surgical"
    )

    pharmacist = auth_svc.register_user(
        username="pharm.chen",
        email="pharm.chen@carepulse.org",
        password="PharmPass2026!",
        first_name="David",
        last_name="Chen",
        role=Role.CLINICAL_PHARMACIST,
        department="Central Pharmacy"
    )

    print(f"[OK] Created users: admin ({admin.id}), dr.smith ({doc.id}), nurse.patel ({nurse.id}), pharm.chen ({pharmacist.id})")

    print("[*] Generating synthetic patient cohort (20 patients with longitudinal records)...")
    cohort_builder = CohortBuilder(db)
    patients = cohort_builder.build_cohort(total_patients=20, diabetes_prevalence=0.3, hypertension_prevalence=0.4)
    print(f"[OK] Successfully registered {len(patients)} synthetic patients with associated clinical history.")

    # Integrity verification
    is_valid, err = auth_svc.audit_logger.verify_integrity()
    if is_valid:
        print("[OK] Cryptographic HIPAA audit chain verified (100% tamper-evident integrity).")
    else:
        print(f"[!] Audit chain check warning: {err}")

    print("\n[OK] Database seeding completed successfully!")

if __name__ == '__main__':
    seed()

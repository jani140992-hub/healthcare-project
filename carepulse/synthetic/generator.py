"""
Longitudinal Synthetic Patient History Generator.
Generates comprehensive clinical records with correlated vitals, medications, diagnoses, and lab results.
"""

import random
import uuid
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, List
from carepulse.clinical.patient import PatientService, PatientRecord
from carepulse.clinical.encounter import EncounterService
from carepulse.clinical.vitals import VitalsService
from carepulse.clinical.conditions import ConditionService
from carepulse.clinical.cpoe import CPOEService
from carepulse.synthetic.disease_models import ChronicDiseaseModel

FIRST_NAMES_MALE = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles"]
FIRST_NAMES_FEMALE = ["Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
CITIES = ["Boston", "New York", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

class SyntheticPatientGenerator:
    def __init__(self, db_engine=None):
        self.patient_svc = PatientService(db_engine)
        self.encounter_svc = EncounterService(db_engine)
        self.vitals_svc = VitalsService(db_engine)
        self.condition_svc = ConditionService(db_engine)
        self.cpoe_svc = CPOEService(db_engine)

    def generate_patient(self, has_diabetes: bool = False, has_hypertension: bool = False) -> PatientRecord:
        gender = random.choice(["male", "female"])
        first_name = random.choice(FIRST_NAMES_MALE if gender == "male" else FIRST_NAMES_FEMALE)
        last_name = random.choice(LAST_NAMES)
        birth_year = random.randint(1950, 2005)
        dob = f"{birth_year}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"

        pat = self.patient_svc.register_patient(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=dob,
            gender=gender,
            actor_id="synthetic_engine",
            actor_role="system_admin",
            blood_type=random.choice(["A+", "O+", "B+", "AB+", "A-", "O-"]),
            phone=f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            email=f"{first_name.lower()}.{last_name.lower()}@example-health.org",
            address_street=f"{random.randint(100, 999)} Maple Ave",
            address_city=random.choice(CITIES),
            address_state="MA",
            address_postal_code=f"{random.randint(10000, 99999)}"
        )

        # Ensure provider exists for foreign keys
        doc_row = self.patient_svc.db.execute_single("SELECT id FROM users WHERE role = 'attending_physician' LIMIT 1")
        if doc_row:
            provider_id = doc_row["id"]
        else:
            provider_id = "usr_sys_doc_001"
            self.patient_svc.db.execute_insert(
                "INSERT OR IGNORE INTO users (id, username, email, password_hash, salt, first_name, last_name, role, created_at, updated_at) "
                "VALUES (?, 'sys_doc', 'doc@carepulse.org', 'x', 'x', 'Default', 'Doctor', 'attending_physician', datetime('now'), datetime('now'))",
                (provider_id,)
            )

        # Baseline Encounter
        enc = self.encounter_svc.start_encounter(
            patient_id=pat.id,
            provider_id=provider_id,
            encounter_type="ambulatory",
            actor_id="synthetic_engine",
            actor_role="system_admin",
            reason_description="Annual comprehensive wellness exam"
        )

        # Baseline Vitals
        sbp = 145.0 if has_hypertension else random.uniform(115.0, 128.0)
        dbp = 92.0 if has_hypertension else random.uniform(70.0, 82.0)
        hr = random.uniform(64.0, 84.0)
        rr = random.uniform(14.0, 18.0)
        temp = random.uniform(36.5, 37.1)
        h_cm = random.uniform(160.0, 185.0)
        w_kg = random.uniform(65.0, 95.0)

        self.vitals_svc.record_vitals(
            patient_id=pat.id,
            recorded_by="nurse_triage_001",
            actor_role="registered_nurse",
            encounter_id=enc.id,
            systolic_bp=sbp,
            diastolic_bp=dbp,
            heart_rate=hr,
            respiratory_rate=rr,
            body_temperature=temp,
            oxygen_saturation=98.0,
            height_cm=h_cm,
            weight_kg=w_kg
        )

        # Conditions and Meds
        if has_diabetes:
            dm = ChronicDiseaseModel.DIABETES_TYPE_2
            self.condition_svc.add_condition(
                patient_id=pat.id,
                icd10_code=dm.icd10_code,
                description=dm.disease_name,
                category="chronic-problem",
                clinical_status="active",
                recorded_by="doc_primary_001",
                actor_role="attending_physician",
                encounter_id=enc.id
            )
            self.cpoe_svc.place_medication_order(
                patient_id=pat.id,
                prescriber_id=provider_id,
                actor_role="attending_physician",
                rxnorm_code="860975",
                drug_name="Metformin Hydrochloride 500 MG Oral Tablet",
                dosage_form="tablet",
                strength="500 mg",
                dose_amount=500.0,
                dose_unit="mg",
                route="oral",
                frequency="BID",
                duration_days=90,
                quantity=180,
                encounter_id=enc.id
            )

        if has_hypertension:
            htn = ChronicDiseaseModel.ESSENTIAL_HYPERTENSION
            self.condition_svc.add_condition(
                patient_id=pat.id,
                icd10_code=htn.icd10_code,
                description=htn.disease_name,
                category="chronic-problem",
                clinical_status="active",
                recorded_by="doc_primary_001",
                actor_role="attending_physician",
                encounter_id=enc.id
            )
            self.cpoe_svc.place_medication_order(
                patient_id=pat.id,
                prescriber_id=provider_id,
                actor_role="attending_physician",
                rxnorm_code="314076",
                drug_name="Lisinopril 10 MG Oral Tablet",
                dosage_form="tablet",
                strength="10 mg",
                dose_amount=10.0,
                dose_unit="mg",
                route="oral",
                frequency="once daily",
                duration_days=90,
                quantity=90,
                encounter_id=enc.id
            )

        self.encounter_svc.complete_encounter(enc.id, actor_id=provider_id, actor_role="attending_physician")
        return pat

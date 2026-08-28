"""
Database Engine & Persistence Layer for CarePulse.
Provides schema definition, migration management, connection pooling,
and standard query execution for SQLite and SQL-compatible engines.
"""

import sqlite3
import os
import json
import logging
from typing import Any, Dict, List, Optional, Tuple
from contextlib import contextmanager
from carepulse.config import get_config

logger = logging.getLogger(__name__)

SCHEMA_SQL = """
-- HIPAA Audit Log (Immutable, Hash Chained)
CREATE TABLE IF NOT EXISTS hipaa_audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_id TEXT UNIQUE NOT NULL,
    timestamp TEXT NOT NULL,
    actor_id TEXT NOT NULL,
    actor_role TEXT NOT NULL,
    action TEXT NOT NULL,
    resource_type TEXT NOT NULL,
    resource_id TEXT NOT NULL,
    patient_id TEXT,
    ip_address TEXT,
    details TEXT,
    previous_hash TEXT,
    entry_hash TEXT NOT NULL
);

-- Users & Credentials
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    role TEXT NOT NULL,
    department TEXT,
    npi_number TEXT,
    dea_number TEXT,
    is_active INTEGER DEFAULT 1,
    mfa_secret TEXT,
    failed_login_attempts INTEGER DEFAULT 0,
    locked_until TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

-- Patients (Master Patient Index)
CREATE TABLE IF NOT EXISTS patients (
    id TEXT PRIMARY KEY,
    mrn TEXT UNIQUE NOT NULL,
    ssn_hash TEXT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    date_of_birth TEXT NOT NULL,
    gender TEXT NOT NULL,
    blood_type TEXT,
    phone TEXT,
    email TEXT,
    address_street TEXT,
    address_city TEXT,
    address_state TEXT,
    address_postal_code TEXT,
    address_country TEXT,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT,
    emergency_contact_relation TEXT,
    primary_care_provider_id TEXT,
    is_deceased INTEGER DEFAULT 0,
    deceased_datetime TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

-- Clinical Encounters
CREATE TABLE IF NOT EXISTS encounters (
    id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    provider_id TEXT NOT NULL,
    encounter_type TEXT NOT NULL, -- inpatient, outpatient, emergency, ambulatory, virtual
    status TEXT NOT NULL,         -- planned, in-progress, completed, cancelled
    class_code TEXT,
    priority TEXT,
    service_type TEXT,
    start_time TEXT NOT NULL,
    end_time TEXT,
    reason_code TEXT,
    reason_description TEXT,
    discharge_disposition TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES patients(id),
    FOREIGN KEY(provider_id) REFERENCES users(id)
);

-- Vital Signs Observations
CREATE TABLE IF NOT EXISTS vital_signs (
    id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    encounter_id TEXT,
    recorded_at TEXT NOT NULL,
    recorded_by TEXT NOT NULL,
    systolic_bp REAL,
    diastolic_bp REAL,
    heart_rate REAL,
    respiratory_rate REAL,
    body_temperature REAL,
    oxygen_saturation REAL,
    height_cm REAL,
    weight_kg REAL,
    bmi REAL,
    pain_score INTEGER,
    early_warning_score INTEGER,
    score_interpretation TEXT,
    notes TEXT,
    FOREIGN KEY(patient_id) REFERENCES patients(id),
    FOREIGN KEY(encounter_id) REFERENCES encounters(id)
);

-- Patient Conditions / Diagnoses (Problem List)
CREATE TABLE IF NOT EXISTS conditions (
    id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    encounter_id TEXT,
    icd10_code TEXT NOT NULL,
    snomed_code TEXT,
    description TEXT NOT NULL,
    category TEXT NOT NULL,       -- encounter-diagnosis, chronic-problem, health-concern
    clinical_status TEXT NOT NULL,-- active, recurrence, relapse, remission, resolved
    verification_status TEXT,     -- provisional, confirmed, refuted
    severity TEXT,                -- mild, moderate, severe
    onset_date TEXT,
    abatement_date TEXT,
    recorded_by TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES patients(id)
);

-- Allergies & Adverse Reactions
CREATE TABLE IF NOT EXISTS allergies (
    id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    substance TEXT NOT NULL,
    substance_code TEXT,
    category TEXT NOT NULL,       -- medication, food, environment, biologic
    criticality TEXT NOT NULL,    -- low, high, unable-to-assess
    clinical_status TEXT NOT NULL,-- active, inactive, resolved
    reaction_manifestation TEXT,
    severity TEXT,                -- mild, moderate, severe
    onset_date TEXT,
    recorded_by TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES patients(id)
);

-- Clinical Notes (SOAP, Progress, Discharge)
CREATE TABLE IF NOT EXISTS clinical_notes (
    id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    encounter_id TEXT NOT NULL,
    author_id TEXT NOT NULL,
    note_type TEXT NOT NULL,      -- soap, progress, consult, discharge_summary, operative
    subjective TEXT,
    objective TEXT,
    assessment TEXT,
    plan TEXT,
    signed INTEGER DEFAULT 0,
    signed_by TEXT,
    signed_at TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES patients(id),
    FOREIGN KEY(encounter_id) REFERENCES encounters(id)
);

-- Prescriptions & Medication Orders
CREATE TABLE IF NOT EXISTS prescriptions (
    id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    encounter_id TEXT,
    prescriber_id TEXT NOT NULL,
    rxnorm_code TEXT NOT NULL,
    drug_name TEXT NOT NULL,
    dosage_form TEXT NOT NULL,
    strength TEXT NOT NULL,
    dose_amount REAL NOT NULL,
    dose_unit TEXT NOT NULL,
    route TEXT NOT NULL,          -- oral, intravenous, subcutaneous, topical, inhalation
    frequency TEXT NOT NULL,      -- once daily, BID, TID, QID, PRN
    duration_days INTEGER NOT NULL,
    quantity_prescribed INTEGER NOT NULL,
    refills_allowed INTEGER DEFAULT 0,
    refills_remaining INTEGER DEFAULT 0,
    status TEXT NOT NULL,         -- active, completed, cancelled, on-hold
    instructions TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES patients(id),
    FOREIGN KEY(prescriber_id) REFERENCES users(id)
);

-- Medication Dispensing Records
CREATE TABLE IF NOT EXISTS medication_dispense (
    id TEXT PRIMARY KEY,
    prescription_id TEXT NOT NULL,
    patient_id TEXT NOT NULL,
    pharmacist_id TEXT NOT NULL,
    lot_number TEXT NOT NULL,
    expiration_date TEXT NOT NULL,
    quantity_dispensed INTEGER NOT NULL,
    days_supply INTEGER NOT NULL,
    dispense_date TEXT NOT NULL,
    status TEXT NOT NULL,         -- completed, preparation, in-progress
    notes TEXT,
    FOREIGN KEY(prescription_id) REFERENCES prescriptions(id),
    FOREIGN KEY(patient_id) REFERENCES patients(id)
);

-- Laboratory Orders
CREATE TABLE IF NOT EXISTS lab_orders (
    id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    encounter_id TEXT,
    ordering_provider_id TEXT NOT NULL,
    loinc_code TEXT NOT NULL,
    test_name TEXT NOT NULL,
    panel_name TEXT,
    specimen_type TEXT NOT NULL,  -- whole blood, serum, plasma, urine, swab, csf
    priority TEXT NOT NULL,       -- stat, urgent, routine
    status TEXT NOT NULL,         -- ordered, collected, processing, completed, cancelled
    order_date TEXT NOT NULL,
    collected_date TEXT,
    FOREIGN KEY(patient_id) REFERENCES patients(id),
    FOREIGN KEY(ordering_provider_id) REFERENCES users(id)
);

-- Laboratory Results
CREATE TABLE IF NOT EXISTS lab_results (
    id TEXT PRIMARY KEY,
    lab_order_id TEXT NOT NULL,
    patient_id TEXT NOT NULL,
    loinc_code TEXT NOT NULL,
    analyte_name TEXT NOT NULL,
    numeric_value REAL,
    string_value TEXT,
    unit TEXT,
    reference_low REAL,
    reference_high REAL,
    abnormal_flag TEXT,           -- normal, low, high, critical_low, critical_high
    status TEXT NOT NULL,         -- preliminary, final, corrected, cancelled
    reported_at TEXT NOT NULL,
    verified_by TEXT,
    FOREIGN KEY(lab_order_id) REFERENCES lab_orders(id),
    FOREIGN KEY(patient_id) REFERENCES patients(id)
);

-- Radiology & Diagnostic Imaging Orders
CREATE TABLE IF NOT EXISTS radiology_orders (
    id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    encounter_id TEXT,
    ordering_provider_id TEXT NOT NULL,
    modality TEXT NOT NULL,       -- CT, MRI, XR, US, NM, PET
    body_site TEXT NOT NULL,
    procedure_name TEXT NOT NULL,
    indication TEXT,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,         -- ordered, scheduled, acquired, read, completed
    order_date TEXT NOT NULL,
    completed_date TEXT,
    FOREIGN KEY(patient_id) REFERENCES patients(id)
);

-- Radiology Reports
CREATE TABLE IF NOT EXISTS radiology_reports (
    id TEXT PRIMARY KEY,
    radiology_order_id TEXT NOT NULL,
    radiologist_id TEXT NOT NULL,
    findings TEXT NOT NULL,
    impression TEXT NOT NULL,
    birads_or_rating TEXT,
    critical_findings INTEGER DEFAULT 0,
    reported_at TEXT NOT NULL,
    FOREIGN KEY(radiology_order_id) REFERENCES radiology_orders(id),
    FOREIGN KEY(radiologist_id) REFERENCES users(id)
);

-- Appointments & Scheduling
CREATE TABLE IF NOT EXISTS appointments (
    id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    provider_id TEXT NOT NULL,
    appointment_type TEXT NOT NULL, -- routine, follow_up, specialist, telehealth, urgent
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    duration_minutes INTEGER NOT NULL,
    status TEXT NOT NULL,           -- booked, checked_in, in_progress, completed, no_show, cancelled
    cancellation_reason TEXT,
    chief_complaint TEXT,
    telehealth_room_url TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES patients(id),
    FOREIGN KEY(provider_id) REFERENCES users(id)
);

-- Emergency Triage
CREATE TABLE IF NOT EXISTS emergency_triage (
    id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    triage_nurse_id TEXT NOT NULL,
    esi_level INTEGER NOT NULL,      -- ESI 1 (Resuscitation) to 5 (Non-urgent)
    chief_complaint TEXT NOT NULL,
    arrival_mode TEXT NOT NULL,      -- ambulance, walk_in, air_medical, police
    triage_time TEXT NOT NULL,
    pain_scale INTEGER,
    mental_status TEXT,              -- alert, verbal, pain, unresponsive
    notes TEXT,
    FOREIGN KEY(patient_id) REFERENCES patients(id)
);

-- Billing Invoices & Claims
CREATE TABLE IF NOT EXISTS billing_invoices (
    id TEXT PRIMARY KEY,
    invoice_number TEXT UNIQUE NOT NULL,
    patient_id TEXT NOT NULL,
    encounter_id TEXT,
    insurance_policy_number TEXT,
    payer_id TEXT,
    payer_name TEXT,
    total_charges REAL NOT NULL,
    insurance_covered REAL DEFAULT 0.0,
    patient_copay REAL DEFAULT 0.0,
    patient_balance REAL NOT NULL,
    status TEXT NOT NULL,           -- draft, submitted, pending_adjudication, paid, denied
    issue_date TEXT NOT NULL,
    due_date TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES patients(id)
);

-- Billing Line Items (CPT / HCPCS)
CREATE TABLE IF NOT EXISTS billing_line_items (
    id TEXT PRIMARY KEY,
    invoice_id TEXT NOT NULL,
    cpt_code TEXT NOT NULL,
    description TEXT NOT NULL,
    units INTEGER NOT NULL DEFAULT 1,
    unit_price REAL NOT NULL,
    total_price REAL NOT NULL,
    FOREIGN KEY(invoice_id) REFERENCES billing_invoices(id)
);
"""

class DatabaseEngine:
    def __init__(self, db_path: Optional[str] = None):
        if db_path is None:
            config = get_config()
            self.db_path = config.database.sqlite_path
        else:
            self.db_path = db_path
        self._ensure_schema()

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    @contextmanager
    def transaction(self):
        conn = self.get_connection()
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            logger.error(f"Database transaction rolled back due to: {e}")
            raise
        finally:
            conn.close()

    def _ensure_schema(self):
        with self.transaction() as conn:
            conn.executescript(SCHEMA_SQL)

    def execute_query(self, query: str, params: Tuple[Any, ...] = ()) -> List[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def execute_insert(self, query: str, params: Tuple[Any, ...] = ()) -> int:
        with self.transaction() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.rowcount

    def execute_single(self, query: str, params: Tuple[Any, ...] = ()) -> Optional[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            row = cursor.fetchone()
            return dict(row) if row else None

_engine_instance: Optional[DatabaseEngine] = None

def get_db(db_path: Optional[str] = None) -> DatabaseEngine:
    global _engine_instance
    if _engine_instance is None or db_path is not None:
        _engine_instance = DatabaseEngine(db_path=db_path)
    return _engine_instance

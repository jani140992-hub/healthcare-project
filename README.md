# CarePulse Enterprise Healthcare Information System (HIS / EHR)

[![CI/CD Pipeline](https://github.com/jani140992-hub/healthcare-project/actions/workflows/ci.yml/badge.svg)](https://github.com/jani140992-hub/healthcare-project/actions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Standards](https://img.shields.io/badge/standards-HL7%20FHIR%20R4%20%7C%20ICD--10%20%7C%20LOINC%20%7C%20RxNorm-green.svg)](#standards-compliance)
[![Security](https://img.shields.io/badge/compliance-HIPAA%20Title%20II%20%28Audit%20Chained%29-red.svg)](#hipaa-security--cryptographic-audit-trail)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](#build)
[![License](https://img.shields.io/badge/license-Proprietary-red.svg)](#license)

CarePulse is a comprehensive, production-grade Healthcare Information System (HIS) and Electronic Health Record (EHR) platform built in Python. Designed for hospital clinical workflows, regulatory standards, interoperability protocols, and clinical decision support.

---

## Overview

CarePulse integrates hospital operations across twelve core clinical and administrative domains:
- **Master Patient Index (MPI)**: Patient registration, deterministic MRN, and identity management.
- **Clinical EHR Core**: Inpatient/outpatient encounters, vital signs (MAP, BMI), SOAP notes, and CPOE order entry.
- **HL7 FHIR R4 Standard**: Native resources (`Patient`, `Observation`, `Encounter`, `Condition`, `Bundle`), serializers, and validators.
- **Clinical Decision Support (CDSS)**: Drug-Drug Interactions (DDI), allergy cross-reactivity, qSOFA/MEWS sepsis screening, pediatric and renal dosing.
- **Medical Ontologies**: ICD-10-CM, LOINC observation panels, RxNorm formularies, and SNOMED-CT taxonomies.
- **Pharmacy & BCMA**: Medication inventory, expiration lot control, and 5-rights barcode verification.
- **Laboratory LIS & Radiology**: Specimen tracking, panic flags, and DICOM 3.0 image viewing presets.
- **Revenue Cycle & Billing**: CPT fee schedules, ANSI ASC X12 EDI 837P claims, and EDI 835 remittance parsing.
- **Telehealth & Scheduling**: Multi-provider calendars, ESI 1-5 emergency triage, and WebRTC video consult signaling.
- **HIPAA Security & Audit**: RBAC access controls, PBKDF2 password security, and immutable SHA-256 chained audit logs.

---

## Dependencies

The system requires Python 3.10 or newer.

### Production Dependencies
- `fastapi` >= 0.110.0
- `uvicorn[standard]` >= 0.28.0
- `pydantic` >= 2.6.0
- `sqlalchemy` >= 2.0.28
- `cryptography` >= 42.0.0

### Development & Testing Dependencies
- `pytest` >= 8.0.0
- `pytest-asyncio` >= 0.23.0

Package manifests and locked dependency trees are tracked via `requirements.txt`, `pyproject.toml`, `poetry.lock`, `package.json`, and `package-lock.json`.

---

## Installation

### 1. Clone the Repository
```bash
git clone git@github.com:jani140992-hub/healthcare-project.git
cd healthcare-project
```

### 2. Create and Activate Virtual Environment
On Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
On Windows:
```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
Or using Poetry:
```bash
poetry install
```

---

## Build

### Local Package Build
To build the Python distribution package wheel and source archive:
```bash
python setup.py build
python -m pip install -e .
```

### Container Build (Docker)
Build the production container image using Docker:
```bash
docker build -t carepulse-ehr:2.4.0 .
```

---

## Run

### Option A: Direct Python Server
1. Seed the database with clinical staff accounts and synthetic patient cohorts:
```bash
python scripts/seed_database.py
```
2. Start the unified EHR server and Web Portal:
```bash
python scripts/run_server.py
```
Open **http://127.0.0.1:8000** in your browser.

### Option B: Docker Compose
Launch the containerized stack:
```bash
docker-compose up --build -d
```
Access the application at `http://localhost:8000`.

---

## Usage

### Interactive Web Portal
Navigate to `http://127.0.0.1:8000` to access the Single-Page EHR Dashboard:
- **Hospital Overview**: View clinical census, bed occupancy, and audit integrity.
- **Patient Directory**: Search patients by name or MRN, view vital trajectories and conditions.
- **Clinical Decision Support (CDSS)**: Run Drug-Drug Interaction screening and calculate Sepsis qSOFA/MEWS scores.
- **FHIR R4 Explorer**: Query and inspect standard HL7 FHIR resources.
- **HIPAA Audit Chain**: Inspect the cryptographic hash chain and verify tamper-evident integrity.

### REST API Endpoints

#### System Health Check
```bash
curl -X GET http://127.0.0.1:8000/health
```

#### Staff Authentication (JWT)
```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "dr.smith", "password": "PhysicianPass2026!"}'
```

#### Real-Time Drug-Drug Interaction Screening
```bash
curl -X POST http://127.0.0.1:8000/api/v1/cdss/ddi-check \
  -H "Content-Type: application/json" \
  -d '{"drugs": ["warfarin 5mg", "ibuprofen 400mg"]}'
```

#### Sepsis Early Warning Evaluation
```bash
curl -X POST http://127.0.0.1:8000/api/v1/cdss/sepsis \
  -H "Content-Type: application/json" \
  -d '{"respiratory_rate": 24, "systolic_bp": 90, "heart_rate": 120, "temperature_c": 39.2, "altered_mental_status": true, "suspected_infection": true}'
```

#### Retrieve FHIR Patient Resource
```bash
curl -X GET http://127.0.0.1:8000/api/v1/fhir/Patient
```

---

## Testing

Run the automated test suite covering all clinical, security, and interoperability modules:
```bash
python -m unittest discover tests
```

To verify lines of code:
```bash
python scripts/count_loc.py
```

---

## License

PROPRIETARY AND CONFIDENTIAL.
Copyright (c) 2026 CarePulse Health Technologies. All Rights Reserved.
Commercial proprietary software. Unauthorized reproduction or redistribution is strictly prohibited.

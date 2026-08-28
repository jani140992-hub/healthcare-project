"""
Clinical API Route Handlers.
Exposes endpoints for Patient registration, Encounters, Vitals, Conditions, and Orders.
"""

from typing import Dict, Any, List
from carepulse.clinical.patient import PatientService
from carepulse.clinical.encounter import EncounterService
from carepulse.clinical.vitals import VitalsService
from carepulse.clinical.conditions import ConditionService
from carepulse.clinical.allergies import AllergyService
from carepulse.clinical.cpoe import CPOEService

class ClinicalAPIController:
    def __init__(self, db_engine=None):
        self.patients = PatientService(db_engine)
        self.encounters = EncounterService(db_engine)
        self.vitals = VitalsService(db_engine)
        self.conditions = ConditionService(db_engine)
        self.allergies = AllergyService(db_engine)
        self.cpoe = CPOEService(db_engine)

    def register_patient_endpoint(self, payload: Dict[str, Any], actor_id: str, actor_role: str) -> Dict[str, Any]:
        pat = self.patients.register_patient(
            first_name=payload["first_name"],
            last_name=payload["last_name"],
            date_of_birth=payload["date_of_birth"],
            gender=payload["gender"],
            actor_id=actor_id,
            actor_role=actor_role,
            middle_name=payload.get("middle_name"),
            phone=payload.get("phone"),
            email=payload.get("email"),
            blood_type=payload.get("blood_type")
        )
        return {"status": "success", "data": pat.to_dict()}

    def record_vitals_endpoint(self, payload: Dict[str, Any], actor_id: str, actor_role: str) -> Dict[str, Any]:
        rec = self.vitals.record_vitals(
            patient_id=payload["patient_id"],
            recorded_by=actor_id,
            actor_role=actor_role,
            encounter_id=payload.get("encounter_id"),
            systolic_bp=payload.get("systolic_bp"),
            diastolic_bp=payload.get("diastolic_bp"),
            heart_rate=payload.get("heart_rate"),
            respiratory_rate=payload.get("respiratory_rate"),
            body_temperature=payload.get("body_temperature"),
            oxygen_saturation=payload.get("oxygen_saturation"),
            height_cm=payload.get("height_cm"),
            weight_kg=payload.get("weight_kg")
        )
        return {"status": "success", "data": rec.to_dict()}

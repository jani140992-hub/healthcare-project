"""
FHIR RESTful Server & Endpoint Handler.
Supports standard FHIR operations: read, search, vread, and history.
"""

from typing import Dict, Any, Optional, List
from carepulse.clinical.patient import PatientService
from carepulse.clinical.encounter import EncounterService
from carepulse.clinical.vitals import VitalsService
from carepulse.fhir.serializers import FHIRSerializer
from carepulse.fhir.validator import FHIRValidator, FHIRValidationError

class FHIRServer:
    def __init__(self, db_engine=None):
        self.patient_service = PatientService(db_engine)
        self.encounter_service = EncounterService(db_engine)
        self.vitals_service = VitalsService(db_engine)

    def get_patient(self, patient_id: str, actor_id: str = "fhir_client") -> Optional[Dict[str, Any]]:
        pat = self.patient_service.get_patient(patient_id, actor_id=actor_id, actor_role="system")
        if not pat:
            return None
        fhir_pat = FHIRSerializer.patient_to_fhir(pat)
        valid, issues = FHIRValidator.validate_resource(fhir_pat)
        if not valid:
            raise FHIRValidationError(issues)
        return fhir_pat

    def search_patient(self, name: Optional[str] = None, actor_id: str = "fhir_client") -> Dict[str, Any]:
        results = []
        if name:
            patients = self.patient_service.search_patients(name, actor_id=actor_id, actor_role="system")
            results = [FHIRSerializer.patient_to_fhir(p) for p in patients]
        return FHIRSerializer.create_bundle(results)

    def get_patient_observations(self, patient_id: str, actor_id: str = "fhir_client") -> Dict[str, Any]:
        vitals_list = self.vitals_service.get_patient_vitals_history(patient_id, actor_id=actor_id, actor_role="system")
        all_obs = []
        for v in vitals_list:
            all_obs.extend(FHIRSerializer.vitals_to_fhir_observations(v))
        return FHIRSerializer.create_bundle(all_obs)

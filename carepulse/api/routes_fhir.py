"""
FHIR R4 RESTful API Route Handlers.
Exposes standard HL7 FHIR endpoints for Patient and Observation resources.
"""

from typing import Dict, Any, Optional
from carepulse.fhir.server import FHIRServer

class FHIRAPIController:
    def __init__(self, db_engine=None):
        self.fhir_server = FHIRServer(db_engine)

    def handle_get_patient(self, patient_id: str) -> Optional[Dict[str, Any]]:
        return self.fhir_server.get_patient(patient_id)

    def handle_search_patient(self, name: Optional[str] = None) -> Dict[str, Any]:
        return self.fhir_server.search_patient(name)

    def handle_get_observations(self, patient_id: str) -> Dict[str, Any]:
        return self.fhir_server.get_patient_observations(patient_id)

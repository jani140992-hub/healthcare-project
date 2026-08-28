"""
HL7 Fast Healthcare Interoperability Resources (FHIR R4) Implementation.
Provides models, validation, serialization, and RESTful resource operations.
"""

from carepulse.fhir.resources import (
    FHIRResource,
    FHIRPatient,
    FHIREncounter,
    FHIRObservation,
    FHIRCondition,
    FHIRMedicationRequest,
    FHIRDiagnosticReport,
    FHIRBundle,
)
from carepulse.fhir.serializers import FHIRSerializer
from carepulse.fhir.validator import FHIRValidator
from carepulse.fhir.server import FHIRServer

__all__ = [
    "FHIRResource",
    "FHIRPatient",
    "FHIREncounter",
    "FHIRObservation",
    "FHIRCondition",
    "FHIRMedicationRequest",
    "FHIRDiagnosticReport",
    "FHIRBundle",
    "FHIRSerializer",
    "FHIRValidator",
    "FHIRServer",
]

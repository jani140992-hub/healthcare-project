"""
Clinical Management Subsystem.
Encompasses Patient Demographics, Encounters, Vitals, Conditions, Allergies, SOAP notes, and CPOE.
"""

from carepulse.clinical.patient import PatientService, PatientRecord
from carepulse.clinical.encounter import EncounterService, EncounterRecord
from carepulse.clinical.vitals import VitalsService, VitalSignsRecord
from carepulse.clinical.conditions import ConditionService, ConditionRecord
from carepulse.clinical.allergies import AllergyService, AllergyRecord
from carepulse.clinical.notes import ClinicalNotesService, ClinicalNoteRecord
from carepulse.clinical.cpoe import CPOEService, OrderRecord

__all__ = [
    "PatientService",
    "PatientRecord",
    "EncounterService",
    "EncounterRecord",
    "VitalsService",
    "VitalSignsRecord",
    "ConditionService",
    "ConditionRecord",
    "AllergyService",
    "AllergyRecord",
    "ClinicalNotesService",
    "ClinicalNoteRecord",
    "CPOEService",
    "OrderRecord",
]

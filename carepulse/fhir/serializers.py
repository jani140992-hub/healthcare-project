"""
FHIR R4 JSON Serializers & Parsers.
Converts internal EHR domain models to compliant FHIR JSON schemas and vice versa.
"""

import json
from dataclasses import asdict
from typing import Dict, Any, List, Optional
from carepulse.fhir.resources import (
    FHIRPatient, FHIREncounter, FHIRObservation, FHIRCondition,
    FHIRMedicationRequest, FHIRDiagnosticReport, FHIRBundle,
    CodeableConcept, Coding, Quantity, Reference
)
from carepulse.clinical.patient import PatientRecord
from carepulse.clinical.encounter import EncounterRecord
from carepulse.clinical.vitals import VitalSignsRecord
from carepulse.clinical.conditions import ConditionRecord

class FHIRSerializer:
    @staticmethod
    def patient_to_fhir(p: PatientRecord, base_url: str = "http://localhost:8000/api/v1/fhir") -> Dict[str, Any]:
        return {
            "resourceType": "Patient",
            "id": p.id,
            "identifier": [
                {
                    "use": "usual",
                    "type": {
                        "coding": [{
                            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                            "code": "MR",
                            "display": "Medical Record Number"
                        }]
                    },
                    "system": "urn:carepulse:mrn",
                    "value": p.mrn
                }
            ],
            "active": not p.is_deceased,
            "name": [
                {
                    "use": "official",
                    "family": p.last_name,
                    "given": [p.first_name] + ([p.middle_name] if p.middle_name else [])
                }
            ],
            "telecom": [
                {"system": "phone", "value": p.phone, "use": "home"} if p.phone else None,
                {"system": "email", "value": p.email, "use": "home"} if p.email else None,
            ],
            "gender": p.gender,
            "birthDate": p.date_of_birth,
            "address": [
                {
                    "line": [p.address_street] if p.address_street else [],
                    "city": p.address_city,
                    "state": p.address_state,
                    "postalCode": p.address_postal_code,
                    "country": p.address_country or "USA"
                }
            ]
        }

    @staticmethod
    def encounter_to_fhir(e: EncounterRecord) -> Dict[str, Any]:
        return {
            "resourceType": "Encounter",
            "id": e.id,
            "status": e.status,
            "class": {
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                "code": e.encounter_type.upper()[:3],
                "display": e.encounter_type.capitalize()
            },
            "subject": {
                "reference": f"Patient/{e.patient_id}"
            },
            "period": {
                "start": e.start_time,
                "end": e.end_time
            },
            "reasonCode": [
                {
                    "coding": [
                        {
                            "system": "http://hl7.org/fhir/sid/icd-10-cm",
                            "code": e.reason_code or "R69",
                            "display": e.reason_description or "Illness, unspecified"
                        }
                    ]
                }
            ] if e.reason_code or e.reason_description else []
        }

    @staticmethod
    def vitals_to_fhir_observations(v: VitalSignsRecord) -> List[Dict[str, Any]]:
        observations = []
        patient_ref = {"reference": f"Patient/{v.patient_id}"}
        effective_time = v.recorded_at

        # Blood pressure panel
        if v.systolic_bp is not None and v.diastolic_bp is not None:
            bp_obs = {
                "resourceType": "Observation",
                "id": f"{v.id}-bp",
                "status": "final",
                "category": [{
                    "coding": [{
                        "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                        "code": "vital-signs",
                        "display": "Vital Signs"
                    }]
                }],
                "code": {
                    "coding": [{
                        "system": "http://loinc.org",
                        "code": "85354-9",
                        "display": "Blood pressure panel with all children optional"
                    }]
                },
                "subject": patient_ref,
                "effectiveDateTime": effective_time,
                "component": [
                    {
                        "code": {
                            "coding": [{"system": "http://loinc.org", "code": "8480-6", "display": "Systolic blood pressure"}]
                        },
                        "valueQuantity": {"value": v.systolic_bp, "unit": "mmHg", "system": "http://unitsofmeasure.org", "code": "mm[Hg]"}
                    },
                    {
                        "code": {
                            "coding": [{"system": "http://loinc.org", "code": "8462-4", "display": "Diastolic blood pressure"}]
                        },
                        "valueQuantity": {"value": v.diastolic_bp, "unit": "mmHg", "system": "http://unitsofmeasure.org", "code": "mm[Hg]"}
                    }
                ]
            }
            observations.append(bp_obs)

        # Heart Rate
        if v.heart_rate is not None:
            observations.append({
                "resourceType": "Observation",
                "id": f"{v.id}-hr",
                "status": "final",
                "category": [{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category", "code": "vital-signs"}]}],
                "code": {"coding": [{"system": "http://loinc.org", "code": "8867-4", "display": "Heart rate"}]},
                "subject": patient_ref,
                "effectiveDateTime": effective_time,
                "valueQuantity": {"value": v.heart_rate, "unit": "/min", "system": "http://unitsofmeasure.org", "code": "/min"}
            })

        # SpO2
        if v.oxygen_saturation is not None:
            observations.append({
                "resourceType": "Observation",
                "id": f"{v.id}-spo2",
                "status": "final",
                "category": [{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category", "code": "vital-signs"}]}],
                "code": {"coding": [{"system": "http://loinc.org", "code": "2708-6", "display": "Oxygen saturation in Arterial blood by Pulse oximetry"}]},
                "subject": patient_ref,
                "effectiveDateTime": effective_time,
                "valueQuantity": {"value": v.oxygen_saturation, "unit": "%", "system": "http://unitsofmeasure.org", "code": "%"}
            })

        return observations

    @staticmethod
    def create_bundle(resources: List[Dict[str, Any]], bundle_type: str = "searchset") -> Dict[str, Any]:
        return {
            "resourceType": "Bundle",
            "type": bundle_type,
            "total": len(resources),
            "entry": [
                {
                    "fullUrl": f"urn:uuid:{res.get('id', 'item')}",
                    "resource": res
                }
                for res in resources
            ]
        }

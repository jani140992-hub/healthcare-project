"""
FHIR R4 Structural & Profile Validation Engine.
Validates required resource attributes, cardinality, and data type invariants.
"""

from typing import Dict, Any, List, Tuple

class FHIRValidationError(Exception):
    def __init__(self, issues: List[str]):
        super().__init__(f"FHIR Validation Failed: {'; '.join(issues)}")
        self.issues = issues

class FHIRValidator:
    REQUIRED_FIELDS = {
        "Patient": ["resourceType", "id"],
        "Observation": ["resourceType", "id", "status", "code"],
        "Encounter": ["resourceType", "id", "status", "class"],
        "Condition": ["resourceType", "id", "clinicalStatus", "code"],
        "MedicationRequest": ["resourceType", "id", "status", "intent", "subject"],
        "DiagnosticReport": ["resourceType", "id", "status", "code"],
        "Bundle": ["resourceType", "type", "entry"],
    }

    VALID_GENDERS = {"male", "female", "other", "unknown"}
    VALID_OBS_STATUSES = {"registered", "preliminary", "final", "amended", "corrected", "cancelled", "entered-in-error", "unknown"}
    VALID_ENC_STATUSES = {"planned", "arrived", "triaged", "in-progress", "onleave", "finished", "cancelled", "entered-in-error", "unknown"}

    @classmethod
    def validate_resource(cls, resource: Dict[str, Any]) -> Tuple[bool, List[str]]:
        issues = []
        if not isinstance(resource, dict):
            return False, ["Resource root must be a JSON object"]

        res_type = resource.get("resourceType")
        if not res_type:
            return False, ["Missing required property 'resourceType'"]

        expected_reqs = cls.REQUIRED_FIELDS.get(res_type)
        if not expected_reqs:
            issues.append(f"Unrecognized or unsupported FHIR resourceType: {res_type}")
            return False, issues

        for req in expected_reqs:
            if req not in resource or resource[req] is None:
                issues.append(f"Missing required field '{req}' for resource {res_type}")

        # Specific type validations
        if res_type == "Patient":
            gender = resource.get("gender")
            if gender and gender not in cls.VALID_GENDERS:
                issues.append(f"Invalid Patient.gender '{gender}'. Must be one of: {cls.VALID_GENDERS}")

        elif res_type == "Observation":
            status = resource.get("status")
            if status and status not in cls.VALID_OBS_STATUSES:
                issues.append(f"Invalid Observation.status '{status}'. Must be one of: {cls.VALID_OBS_STATUSES}")

        elif res_type == "Encounter":
            status = resource.get("status")
            if status and status not in cls.VALID_ENC_STATUSES:
                issues.append(f"Invalid Encounter.status '{status}'. Must be one of: {cls.VALID_ENC_STATUSES}")

        return len(issues) == 0, issues

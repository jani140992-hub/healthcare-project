"""
HL7 FHIR R4 Standard Data Classes.
Implements the core FHIR resources with standard field structures, codings, and value quantities.
"""

from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any

@dataclass
class Coding:
    system: str
    code: str
    display: str

@dataclass
class CodeableConcept:
    coding: List[Coding] = field(default_factory=list)
    text: Optional[str] = None

@dataclass
class Quantity:
    value: float
    unit: str
    system: Optional[str] = "http://unitsofmeasure.org"
    code: Optional[str] = None

@dataclass
class Reference:
    reference: str
    display: Optional[str] = None

@dataclass
class FHIRResource:
    resourceType: str
    id: str

@dataclass
class FHIRPatient(FHIRResource):
    active: bool = True
    name: List[Dict[str, Any]] = field(default_factory=list)
    telecom: List[Dict[str, Any]] = field(default_factory=list)
    gender: str = "unknown"
    birthDate: Optional[str] = None
    address: List[Dict[str, Any]] = field(default_factory=list)
    identifier: List[Dict[str, Any]] = field(default_factory=list)

    def __post_init__(self):
        self.resourceType = "Patient"

@dataclass
class FHIREncounter(FHIRResource):
    status: str = "in-progress"  # planned, arrived, triaged, in-progress, finished, cancelled
    class_coding: Optional[Coding] = None
    subject: Optional[Reference] = None
    participant: List[Dict[str, Any]] = field(default_factory=list)
    period: Dict[str, Optional[str]] = field(default_factory=dict)
    reasonCode: List[CodeableConcept] = field(default_factory=list)

    def __post_init__(self):
        self.resourceType = "Encounter"

@dataclass
class FHIRObservation(FHIRResource):
    status: str = "final"       # registered, preliminary, final, amended
    category: List[CodeableConcept] = field(default_factory=list)
    code: Optional[CodeableConcept] = None
    subject: Optional[Reference] = None
    encounter: Optional[Reference] = None
    effectiveDateTime: Optional[str] = None
    valueQuantity: Optional[Quantity] = None
    valueString: Optional[str] = None
    interpretation: List[CodeableConcept] = field(default_factory=list)

    def __post_init__(self):
        self.resourceType = "Observation"

@dataclass
class FHIRCondition(FHIRResource):
    clinicalStatus: Optional[CodeableConcept] = None
    verificationStatus: Optional[CodeableConcept] = None
    category: List[CodeableConcept] = field(default_factory=list)
    severity: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    subject: Optional[Reference] = None
    onsetDateTime: Optional[str] = None
    recordedDate: Optional[str] = None

    def __post_init__(self):
        self.resourceType = "Condition"

@dataclass
class FHIRMedicationRequest(FHIRResource):
    status: str = "active"
    intent: str = "order"
    medicationCodeableConcept: Optional[CodeableConcept] = None
    subject: Optional[Reference] = None
    authoredOn: Optional[str] = None
    requester: Optional[Reference] = None
    dosageInstruction: List[Dict[str, Any]] = field(default_factory=list)

    def __post_init__(self):
        self.resourceType = "MedicationRequest"

@dataclass
class FHIRDiagnosticReport(FHIRResource):
    status: str = "final"
    code: Optional[CodeableConcept] = None
    subject: Optional[Reference] = None
    effectiveDateTime: Optional[str] = None
    result: List[Reference] = field(default_factory=list)
    conclusion: Optional[str] = None

    def __post_init__(self):
        self.resourceType = "DiagnosticReport"

@dataclass
class BundleEntry:
    fullUrl: str
    resource: Dict[str, Any]

@dataclass
class FHIRBundle(FHIRResource):
    type: str = "searchset"     # document, message, transaction, transaction-response, searchset
    total: int = 0
    entry: List[Dict[str, Any]] = field(default_factory=list)

    def __post_init__(self):
        self.resourceType = "Bundle"

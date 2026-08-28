"""
Chronic Disease Natural History & Progression Models.
Simulates clinical biomarker trajectories for Diabetes, Hypertension, and CKD over 10-year timelines.
"""

from dataclasses import dataclass
from typing import List, Dict, Tuple
import random

@dataclass
class DiseaseTrajectory:
    disease_name: str
    icd10_code: str
    baseline_age_onset: int
    progression_rate: float
    typical_medications: List[Tuple[str, str, str]] # (Name, RxNorm, Dose)
    typical_lab_markers: List[Tuple[str, float, float]] # (Name, baseline, yearly_delta)

class ChronicDiseaseModel:
    DIABETES_TYPE_2 = DiseaseTrajectory(
        disease_name="Type 2 Diabetes Mellitus without complications",
        icd10_code="E11.9",
        baseline_age_onset=48,
        progression_rate=0.08,
        typical_medications=[
            ("Metformin 500mg", "860975", "500 mg BID"),
            ("Glipizide 5mg", "310489", "5 mg daily"),
            ("Empagliflozin 10mg", "1545653", "10 mg daily")
        ],
        typical_lab_markers=[
            ("Hemoglobin A1c", 6.8, 0.25),
            ("Fasting Blood Glucose", 135.0, 5.0)
        ]
    )

    ESSENTIAL_HYPERTENSION = DiseaseTrajectory(
        disease_name="Essential (primary) hypertension",
        icd10_code="I10",
        baseline_age_onset=42,
        progression_rate=0.05,
        typical_medications=[
            ("Lisinopril 10mg", "314076", "10 mg daily"),
            ("Amlodipine 5mg", "197361", "5 mg daily"),
            ("Hydrochlorothiazide 25mg", "310798", "25 mg daily")
        ],
        typical_lab_markers=[
            ("Systolic Blood Pressure", 138.0, 1.8),
            ("Diastolic Blood Pressure", 88.0, 0.9)
        ]
    )

    CHRONIC_KIDNEY_DISEASE_STAGE_3 = DiseaseTrajectory(
        disease_name="Chronic kidney disease, stage 3 (moderate)",
        icd10_code="N18.3",
        baseline_age_onset=58,
        progression_rate=0.12,
        typical_medications=[
            ("Losartan 50mg", "311354", "50 mg daily"),
            ("Furosemide 40mg", "310429", "40 mg daily")
        ],
        typical_lab_markers=[
            ("Serum Creatinine", 1.6, 0.15),
            ("eGFR", 45.0, -3.0)
        ]
    )

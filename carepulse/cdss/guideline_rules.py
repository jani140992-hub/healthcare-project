"""
Clinical Practice Guidelines & Evidence-Based Recommendation Engine.
Automates ADA Diabetes Standards of Care, ACC/AHA Hypertension Guidelines, and USPSTF Preventive Screenings.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Any

@dataclass
class GuidelineRecommendation:
    category: str
    guideline_source: str
    strength_of_recommendation: str  # Class I, Class IIa, USPSTF Grade A, Grade B
    finding: str
    recommended_action: str
    rationale: str

class ClinicalGuidelineEngine:
    @staticmethod
    def evaluate_diabetes_care(
        age: int,
        hba1c: Optional[float],
        has_diabetes: bool,
        has_ascvd: bool,
        on_statin: bool = False,
        urine_microalbumin_checked_past_year: bool = False,
        eye_exam_past_year: bool = False
    ) -> List[GuidelineRecommendation]:
        recs = []
        if not has_diabetes:
            return recs

        # Glycemic Control Target
        if hba1c is not None:
            if hba1c > 8.0:
                recs.append(GuidelineRecommendation(
                    category="Glycemic Management",
                    guideline_source="ADA Standards of Care in Diabetes",
                    strength_of_recommendation="Class I (Level A)",
                    finding=f"Current HbA1c of {hba1c}% exceeds general target (< 7.0%)",
                    recommended_action="Intensify antihyperglycemic regimen (consider adding SGLT2i or GLP-1 RA if ASCVD/CKD present); provide diabetes self-management education",
                    rationale="Stringent glycemic control early in disease course prevents microvascular complications (nephropathy, retinopathy, neuropathy)"
                ))

        # Statin Therapy
        if age >= 40 and not on_statin:
            recs.append(GuidelineRecommendation(
                category="Cardiovascular Risk Reduction",
                guideline_source="ADA / ACC / AHA Consensus",
                strength_of_recommendation="Class I (Level A)",
                finding="Patient age >= 40 with diabetes not currently prescribed statin therapy",
                recommended_action="Initiate moderate-to-high intensity statin therapy (e.g., Atorvastatin 20-40mg daily)",
                rationale="Diabetes is a cardiovascular risk equivalent; statins significantly reduce major adverse cardiac events (MACE)"
            ))

        # Nephropathy Screening
        if not urine_microalbumin_checked_past_year:
            recs.append(GuidelineRecommendation(
                category="Microvascular Screening",
                guideline_source="ADA Standards of Care",
                strength_of_recommendation="Class I (Level B)",
                finding="Urine albumin-to-creatinine ratio (uACR) not documented in the past 12 months",
                recommended_action="Order spot urine microalbumin-to-creatinine ratio",
                rationale="Early detection of diabetic kidney disease allows intervention with ACEi/ARB and SGLT2 inhibitors to halt progression to ESRD"
            ))

        # Diabetic Retinopathy Screening
        if not eye_exam_past_year:
            recs.append(GuidelineRecommendation(
                category="Microvascular Screening",
                guideline_source="ADA Standards of Care",
                strength_of_recommendation="Class I (Level B)",
                finding="Dilated retinal eye exam not documented within the past 12 months",
                recommended_action="Refer to ophthalmology/optometry for annual dilated fundoscopic examination",
                rationale="Diabetic retinopathy is a leading cause of preventable adult blindness; early photocoagulation or anti-VEGF prevents vision loss"
            ))

        return recs

    @staticmethod
    def evaluate_hypertension(
        systolic_bp: float,
        diastolic_bp: float,
        has_hypertension_diagnosis: bool = False
    ) -> List[GuidelineRecommendation]:
        recs = []
        
        # 2017 ACC/AHA Blood Pressure Categories
        if systolic_bp >= 140 or diastolic_bp >= 90:
            stage = "Stage 2 Hypertension"
            action = "Initiate prompt pharmacotherapy with two first-line agents of different classes (e.g., CCB + ACEi/ARB or Thiazide) and recommend lifestyle modifications; re-evaluate in 1 month"
            rec_str = "Class I (Level A)"
        elif (130 <= systolic_bp <= 139) or (80 <= diastolic_bp <= 89):
            stage = "Stage 1 Hypertension"
            action = "Assess 10-year ASCVD risk score. If ASCVD >= 10%, initiate single antihypertensive agent; if < 10%, recommend aggressive lifestyle modifications and recheck in 3-6 months"
            rec_str = "Class I (Level B-R)"
        elif (120 <= systolic_bp <= 129) and (diastolic_bp < 80):
            stage = "Elevated Blood Pressure"
            action = "Recommend nonpharmacological interventions (DASH diet, sodium reduction < 1500mg/day, regular physical activity, weight loss); re-evaluate in 3-6 months"
            rec_str = "Class I (Level B-NR)"
        else:
            stage = "Normal Blood Pressure"
            action = "Maintain healthy lifestyle; screen annually"
            rec_str = "Standard Protocol"

        if stage != "Normal Blood Pressure":
            recs.append(GuidelineRecommendation(
                category="Cardiovascular Prevention",
                guideline_source="2017 ACC/AHA/AAPA/ABC/ACPM/AGS/APhA/ASH/ASPC/NMA/PCNA Guideline",
                strength_of_recommendation=rec_str,
                finding=f"Blood pressure of {systolic_bp}/{diastolic_bp} mmHg classified as {stage}",
                recommended_action=action,
                rationale="Tight blood pressure control significantly reduces risk of stroke, myocardial infarction, heart failure, and renal failure"
            ))

        return recs

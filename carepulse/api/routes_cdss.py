"""
Clinical Decision Support API Controllers.
Provides endpoints for checking drug interactions, allergy contraindications, and early warning scores.
"""

from typing import Dict, Any, List
from carepulse.cdss.ddi_engine import DDIEngine
from carepulse.cdss.allergy_checker import AllergyChecker
from carepulse.cdss.early_warning import EarlyWarningSystem
from carepulse.cdss.dose_calculator import DoseCalculator

class CDSSAPIController:
    def __init__(self):
        self.ddi = DDIEngine()
        self.allergy = AllergyChecker()
        self.early_warning = EarlyWarningSystem()
        self.dose = DoseCalculator()

    def check_drug_interactions(self, drug_list: List[str]) -> List[Dict[str, str]]:
        alerts = self.ddi.check_medication_list(drug_list)
        return [a.to_dict() for a in alerts]

    def evaluate_sepsis(self, vitals_payload: Dict[str, Any]) -> Dict[str, Any]:
        assessment = self.early_warning.evaluate_sepsis_risk(
            respiratory_rate=vitals_payload.get("respiratory_rate"),
            systolic_bp=vitals_payload.get("systolic_bp"),
            heart_rate=vitals_payload.get("heart_rate"),
            temperature_c=vitals_payload.get("temperature_c"),
            altered_mental_status=vitals_payload.get("altered_mental_status", False),
            suspected_infection=vitals_payload.get("suspected_infection", False)
        )
        return {
            "qsofa_score": assessment.qsofa_score,
            "mews_score": assessment.mews_score,
            "is_sepsis_screen_positive": assessment.is_sepsis_screen_positive,
            "risk_tier": assessment.risk_tier,
            "clinical_recommendation": assessment.clinical_recommendation
        }

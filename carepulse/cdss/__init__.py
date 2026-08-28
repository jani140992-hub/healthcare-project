"""
Clinical Decision Support System (CDSS).
Provides rule evaluation for Drug-Drug Interactions (DDI), Allergy Contraindications,
Early Warning Deterioration Scoring, Pediatric Dosing, and Clinical Practice Guidelines.
"""

from carepulse.cdss.ddi_engine import DDIEngine, InteractionAlert, SeverityLevel
from carepulse.cdss.allergy_checker import AllergyChecker, AllergyContraindicationAlert
from carepulse.cdss.early_warning import EarlyWarningSystem, SepsisRiskAssessment
from carepulse.cdss.dose_calculator import DoseCalculator, PediatricDoseResult
from carepulse.cdss.guideline_rules import ClinicalGuidelineEngine, GuidelineRecommendation

__all__ = [
    "DDIEngine",
    "InteractionAlert",
    "SeverityLevel",
    "AllergyChecker",
    "AllergyContraindicationAlert",
    "EarlyWarningSystem",
    "SepsisRiskAssessment",
    "DoseCalculator",
    "PediatricDoseResult",
    "ClinicalGuidelineEngine",
    "GuidelineRecommendation",
]

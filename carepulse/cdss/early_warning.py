"""
Early Warning Scores & Sepsis Risk Assessment Engine.
Calculates quick SOFA (qSOFA), Modified Early Warning Score (MEWS), and Sepsis-3 screening criteria.
"""

from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class SepsisRiskAssessment:
    qsofa_score: int
    mews_score: int
    is_sepsis_screen_positive: bool
    risk_tier: str  # low, moderate, high, critical
    clinical_recommendation: str

class EarlyWarningSystem:
    @staticmethod
    def calculate_qsofa(
        respiratory_rate: Optional[float],
        systolic_bp: Optional[float],
        altered_mental_status: bool
    ) -> int:
        """
        Quick Sequential Organ Failure Assessment (qSOFA).
        Criteria:
        1. Respiratory rate >= 22 breaths/min (1 pt)
        2. Altered mental status / GCS < 15 (1 pt)
        3. Systolic blood pressure <= 100 mmHg (1 pt)
        """
        score = 0
        if respiratory_rate is not None and respiratory_rate >= 22:
            score += 1
        if systolic_bp is not None and systolic_bp <= 100:
            score += 1
        if altered_mental_status:
            score += 1
        return score

    @staticmethod
    def calculate_mews(
        systolic_bp: Optional[float],
        heart_rate: Optional[float],
        respiratory_rate: Optional[float],
        temperature_c: Optional[float],
        avpu_level: str = "Alert"  # Alert, Voice, Pain, Unresponsive
    ) -> int:
        """
        Modified Early Warning Score (MEWS).
        """
        score = 0

        # Systolic BP
        if systolic_bp is not None:
            if systolic_bp <= 70:
                score += 3
            elif 71 <= systolic_bp <= 80:
                score += 2
            elif 81 <= systolic_bp <= 100:
                score += 1
            elif 101 <= systolic_bp <= 199:
                score += 0
            elif systolic_bp >= 200:
                score += 2

        # Heart Rate
        if heart_rate is not None:
            if heart_rate <= 40:
                score += 2
            elif 41 <= heart_rate <= 50:
                score += 1
            elif 51 <= heart_rate <= 100:
                score += 0
            elif 101 <= heart_rate <= 110:
                score += 1
            elif 111 <= heart_rate <= 129:
                score += 2
            elif heart_rate >= 130:
                score += 3

        # Respiratory Rate
        if respiratory_rate is not None:
            if respiratory_rate < 9:
                score += 2
            elif 9 <= respiratory_rate <= 14:
                score += 0
            elif 15 <= respiratory_rate <= 20:
                score += 1
            elif 21 <= respiratory_rate <= 29:
                score += 2
            elif respiratory_rate >= 30:
                score += 3

        # Temperature
        if temperature_c is not None:
            if temperature_c < 35.0:
                score += 2
            elif 35.0 <= temperature_c <= 38.4:
                score += 0
            elif temperature_c >= 38.5:
                score += 2

        # AVPU consciousness
        level = avpu_level.lower()
        if level == "voice":
            score += 1
        elif level == "pain":
            score += 2
        elif level == "unresponsive":
            score += 3

        return score

    @classmethod
    def evaluate_sepsis_risk(
        cls,
        respiratory_rate: Optional[float],
        systolic_bp: Optional[float],
        heart_rate: Optional[float],
        temperature_c: Optional[float],
        altered_mental_status: bool = False,
        suspected_infection: bool = False
    ) -> SepsisRiskAssessment:
        qsofa = cls.calculate_qsofa(respiratory_rate, systolic_bp, altered_mental_status)
        avpu = "Voice" if altered_mental_status else "Alert"
        mews = cls.calculate_mews(systolic_bp, heart_rate, respiratory_rate, temperature_c, avpu)

        is_positive = (qsofa >= 2 or mews >= 4) and suspected_infection

        if qsofa >= 2 and suspected_infection:
            tier = "critical"
            rec = "EMERGENCY: Suspected Sepsis with high risk of in-hospital mortality. Initiate Sepsis Bundle immediately: Blood cultures, IV broad-spectrum antibiotics within 1 hour, IV crystalloids (30 mL/kg for MAP < 65 or lactate >= 4), order serum lactate."
        elif mews >= 4:
            tier = "high"
            rec = "HIGH ALERT: Significant physiologic deterioration detected (MEWS >= 4). Urgent physician evaluation required within 15 minutes. Consider rapid response team activation."
        elif qsofa == 1 or mews >= 2:
            tier = "moderate"
            rec = "MODERATE RISK: Increased frequency of vitals monitoring (q1h). Re-assess clinical status and check for developing infection."
        else:
            tier = "low"
            rec = "STABLE: Standard ward monitoring protocol."

        return SepsisRiskAssessment(
            qsofa_score=qsofa,
            mews_score=mews,
            is_sepsis_screen_positive=is_positive,
            risk_tier=tier,
            clinical_recommendation=rec
        )

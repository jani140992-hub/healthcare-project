"""
Epidemiological Surveillance & Quality Measures Engine.
Implements syndromic infectious outbreak clustering and LACE 30-day hospital readmission risk index.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
from carepulse.database import get_db

@dataclass
class OutbreakAlert:
    syndrome_name: str
    case_count: int
    threshold: int
    severity: str  # alert, epidemic_warning, monitor
    affected_zip_codes: List[str]
    recommendation: str

@dataclass
class LACEReadmissionRisk:
    patient_id: str
    lace_score: int
    risk_category: str  # low, moderate, high
    probability_of_readmission_pct: float
    factors: Dict[str, int]

class EpidemiologicalSurveillanceService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()

    @staticmethod
    def calculate_lace_index(
        length_of_stay_days: int,
        is_acute_emergency_admission: bool,
        charlson_comorbidity_score: int,
        emergency_visits_past_6_months: int
    ) -> LACEReadmissionRisk:
        """
        LACE index for predicting 30-day readmission in hospital patients:
        - L (Length of stay): 0 to 7 pts
        - A (Acuity of admission): 3 pts if acute/emergency, 0 if elective
        - C (Charlson comorbidity): 0 to 5 pts
        - E (Emergency visits prior 6 mo): 0 to 4 pts
        Total Score range: 0 - 19
        """
        # L
        l_score = min(7, length_of_stay_days if length_of_stay_days < 4 else (length_of_stay_days + 1 if length_of_stay_days < 7 else 7))
        # A
        a_score = 3 if is_acute_emergency_admission else 0
        # C
        c_score = min(5, charlson_comorbidity_score)
        # E
        e_score = min(4, emergency_visits_past_6_months)

        total_score = l_score + a_score + c_score + e_score

        if total_score >= 10:
            category = "high"
            prob = min(45.0, 15.0 + (total_score - 10) * 3.5)
        elif 5 <= total_score <= 9:
            category = "moderate"
            prob = 8.0 + (total_score - 5) * 1.4
        else:
            category = "low"
            prob = 2.5 + total_score * 0.9

        return LACEReadmissionRisk(
            patient_id="unspecified",
            lace_score=total_score,
            risk_category=category,
            probability_of_readmission_pct=round(prob, 1),
            factors={"L": l_score, "A": a_score, "C": c_score, "E": e_score}
        )

    def scan_for_infectious_syndromes(self, syndrome_name: str, threshold: int = 5) -> Optional[OutbreakAlert]:
        """
        Scans recent diagnosis problem lists for potential outbreak clusters.
        """
        sql = """
        SELECT COUNT(*) as count, GROUP_CONCAT(pat.address_postal_code) as zips
        FROM conditions c
        JOIN patients pat ON c.patient_id = pat.id
        WHERE c.description LIKE ?
        """
        row = self.db.execute_single(sql, (f"%{syndrome_name}%",))
        if not row:
            return None

        count = row.get("count", 0)
        if count >= threshold:
            raw_zips = row.get("zips") or ""
            unique_zips = list(set([z.strip() for z in raw_zips.split(",") if z.strip()]))
            return OutbreakAlert(
                syndrome_name=syndrome_name,
                case_count=count,
                threshold=threshold,
                severity="epidemic_warning" if count >= (threshold * 2) else "alert",
                affected_zip_codes=unique_zips,
                recommendation=f"Notify Department of Public Health; implement isolation protocols for {syndrome_name} presentations."
            )
        return None

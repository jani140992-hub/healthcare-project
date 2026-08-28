"""
Vital Signs & Clinical Observations Management.
Calculates MAP (Mean Arterial Pressure), BMI, pediatric percentiles,
and integrates with critical alert early warning triggers.
"""

import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any, Tuple
from carepulse.database import get_db
from carepulse.auth.audit import HIPAALogger, AuditAction

@dataclass
class VitalSignsRecord:
    id: str
    patient_id: str
    recorded_at: str
    recorded_by: str
    encounter_id: Optional[str] = None
    systolic_bp: Optional[float] = None
    diastolic_bp: Optional[float] = None
    heart_rate: Optional[float] = None
    respiratory_rate: Optional[float] = None
    body_temperature: Optional[float] = None  # in Celsius
    oxygen_saturation: Optional[float] = None # in percentage
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    bmi: Optional[float] = None
    pain_score: Optional[int] = None           # 0 to 10
    early_warning_score: Optional[int] = None
    score_interpretation: Optional[str] = None
    notes: Optional[str] = None

    @property
    def mean_arterial_pressure(self) -> Optional[float]:
        """
        Calculates MAP: (2 * Diastolic + Systolic) / 3
        """
        if self.systolic_bp is not None and self.diastolic_bp is not None:
            return round((2 * self.diastolic_bp + self.systolic_bp) / 3.0, 1)
        return None

    @property
    def bmi_category(self) -> Optional[str]:
        if self.bmi is None:
            return None
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25.0:
            return "Normal weight"
        elif 25.0 <= self.bmi < 30.0:
            return "Overweight"
        elif 30.0 <= self.bmi < 35.0:
            return "Obesity Class I"
        elif 35.0 <= self.bmi < 40.0:
            return "Obesity Class II"
        else:
            return "Obesity Class III (Severe/Morbid)"

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["map"] = self.mean_arterial_pressure
        d["bmi_category"] = self.bmi_category
        return d

class VitalsService:
    def __init__(self, db_engine=None):
        self.db = db_engine or get_db()
        self.audit_logger = HIPAALogger(self.db)

    @staticmethod
    def calculate_bmi(height_cm: Optional[float], weight_kg: Optional[float]) -> Optional[float]:
        if height_cm and weight_kg and height_cm > 0:
            height_m = height_cm / 100.0
            return round(weight_kg / (height_m * height_m), 2)
        return None

    @staticmethod
    def calculate_news2_score(
        rr: Optional[float],
        spo2: Optional[float],
        temp: Optional[float],
        sbp: Optional[float],
        hr: Optional[float]
    ) -> Tuple[int, str]:
        """
        National Early Warning Score 2 (NEWS2) calculation standard.
        """
        score = 0
        
        # Respiratory Rate
        if rr is not None:
            if rr <= 8:
                score += 3
            elif 9 <= rr <= 11:
                score += 1
            elif 12 <= rr <= 20:
                score += 0
            elif 21 <= rr <= 24:
                score += 2
            elif rr >= 25:
                score += 3

        # SpO2 (Scale 1)
        if spo2 is not None:
            if spo2 <= 91:
                score += 3
            elif 92 <= spo2 <= 93:
                score += 2
            elif 94 <= spo2 <= 95:
                score += 1

        # Temperature
        if temp is not None:
            if temp <= 35.0:
                score += 3
            elif 35.1 <= temp <= 36.0:
                score += 1
            elif 36.1 <= temp <= 38.0:
                score += 0
            elif 38.1 <= temp <= 39.0:
                score += 1
            elif temp >= 39.1:
                score += 2

        # Systolic BP
        if sbp is not None:
            if sbp <= 90:
                score += 3
            elif 91 <= sbp <= 100:
                score += 2
            elif 101 <= sbp <= 110:
                score += 1
            elif 111 <= sbp <= 219:
                score += 0
            elif sbp >= 220:
                score += 3

        # Heart Rate
        if hr is not None:
            if hr <= 40:
                score += 3
            elif 41 <= hr <= 50:
                score += 1
            elif 51 <= hr <= 90:
                score += 0
            elif 91 <= hr <= 110:
                score += 1
            elif 111 <= hr <= 130:
                score += 2
            elif hr >= 131:
                score += 3

        # Clinical interpretation
        if score == 0:
            interp = "Low clinical risk: Ward-based monitoring"
        elif 1 <= score <= 4:
            interp = "Low-medium clinical risk: Prompt assessment by competent registered nurse"
        elif 5 <= score <= 6:
            interp = "Medium clinical risk: Urgent review by clinician with acute care competency"
        else:
            interp = "High clinical risk: Emergency assessment by clinical team with critical care competencies"

        return score, interp

    def record_vitals(
        self,
        patient_id: str,
        recorded_by: str,
        actor_role: str,
        encounter_id: Optional[str] = None,
        systolic_bp: Optional[float] = None,
        diastolic_bp: Optional[float] = None,
        heart_rate: Optional[float] = None,
        respiratory_rate: Optional[float] = None,
        body_temperature: Optional[float] = None,
        oxygen_saturation: Optional[float] = None,
        height_cm: Optional[float] = None,
        weight_kg: Optional[float] = None,
        pain_score: Optional[int] = None,
        notes: Optional[str] = None
    ) -> VitalSignsRecord:
        vitals_id = f"vit_{uuid.uuid4().hex[:12]}"
        now = datetime.now(timezone.utc).isoformat()
        bmi = self.calculate_bmi(height_cm, weight_kg)
        score, interp = self.calculate_news2_score(
            respiratory_rate, oxygen_saturation, body_temperature, systolic_bp, heart_rate
        )

        sql = """
        INSERT INTO vital_signs (
            id, patient_id, encounter_id, recorded_at, recorded_by,
            systolic_bp, diastolic_bp, heart_rate, respiratory_rate,
            body_temperature, oxygen_saturation, height_cm, weight_kg,
            bmi, pain_score, early_warning_score, score_interpretation, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.db.execute_insert(
            sql,
            (
                vitals_id, patient_id, encounter_id, now, recorded_by,
                systolic_bp, diastolic_bp, heart_rate, respiratory_rate,
                body_temperature, oxygen_saturation, height_cm, weight_kg,
                bmi, pain_score, score, interp, notes
            )
        )

        self.audit_logger.log_event(
            actor_id=recorded_by,
            actor_role=actor_role,
            action=AuditAction.PHI_CREATE,
            resource_type="Observation/Vitals",
            resource_id=vitals_id,
            patient_id=patient_id,
            details={"news2_score": score, "hr": heart_rate, "bp": f"{systolic_bp}/{diastolic_bp}"}
        )

        return VitalSignsRecord(
            id=vitals_id,
            patient_id=patient_id,
            encounter_id=encounter_id,
            recorded_at=now,
            recorded_by=recorded_by,
            systolic_bp=systolic_bp,
            diastolic_bp=diastolic_bp,
            heart_rate=heart_rate,
            respiratory_rate=respiratory_rate,
            body_temperature=body_temperature,
            oxygen_saturation=oxygen_saturation,
            height_cm=height_cm,
            weight_kg=weight_kg,
            bmi=bmi,
            pain_score=pain_score,
            early_warning_score=score,
            score_interpretation=interp,
            notes=notes
        )

    def get_patient_vitals_history(
        self,
        patient_id: str,
        actor_id: str,
        actor_role: str,
        limit: int = 50
    ) -> List[VitalSignsRecord]:
        sql = "SELECT * FROM vital_signs WHERE patient_id = ? ORDER BY recorded_at DESC LIMIT ?"
        rows = self.db.execute_query(sql, (patient_id, limit))

        self.audit_logger.log_event(
            actor_id=actor_id,
            actor_role=actor_role,
            action=AuditAction.PHI_READ,
            resource_type="ObservationList/Vitals",
            resource_id=patient_id,
            patient_id=patient_id,
            details={"count": len(rows)}
        )

        return [
            VitalSignsRecord(
                id=r["id"],
                patient_id=r["patient_id"],
                encounter_id=r["encounter_id"],
                recorded_at=r["recorded_at"],
                recorded_by=r["recorded_by"],
                systolic_bp=r["systolic_bp"],
                diastolic_bp=r["diastolic_bp"],
                heart_rate=r["heart_rate"],
                respiratory_rate=r["respiratory_rate"],
                body_temperature=r["body_temperature"],
                oxygen_saturation=r["oxygen_saturation"],
                height_cm=r["height_cm"],
                weight_kg=r["weight_kg"],
                bmi=r["bmi"],
                pain_score=r["pain_score"],
                early_warning_score=r["early_warning_score"],
                score_interpretation=r["score_interpretation"],
                notes=r["notes"]
            )
            for r in rows
        ]

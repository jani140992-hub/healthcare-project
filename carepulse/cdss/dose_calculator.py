"""
Clinical Dose Calculator & Renal Impairment Adjuster.
Calculates pediatric mg/kg dosing with adult caps, Cockcroft-Gault Creatinine Clearance (CrCl),
and Mosteller Body Surface Area (BSA).
"""

import math
from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class PediatricDoseResult:
    weight_kg: float
    recommended_dose_mg: float
    frequency: str
    is_capped_at_adult_max: bool
    adult_max_dose_mg: float
    calculated_daily_dose_mg: float
    instructions: str

class DoseCalculator:
    @staticmethod
    def calculate_bsa_mosteller(height_cm: float, weight_kg: float) -> float:
        """
        Mosteller formula for Body Surface Area:
        BSA (m^2) = sqrt([Height(cm) * Weight(kg)] / 3600)
        """
        if height_cm <= 0 or weight_kg <= 0:
            return 0.0
        return round(math.sqrt((height_cm * weight_kg) / 3600.0), 2)

    @staticmethod
    def calculate_creatinine_clearance(
        age_years: int,
        weight_kg: float,
        serum_creatinine_mg_dl: float,
        is_female: bool
    ) -> float:
        """
        Cockcroft-Gault Equation for estimated Creatinine Clearance (CrCl):
        CrCl = [(140 - Age) * Weight(kg)] / [72 * Serum Cr (mg/dL)] * (0.85 if female)
        """
        if serum_creatinine_mg_dl <= 0 or weight_kg <= 0:
            return 0.0
        base = ((140.0 - age_years) * weight_kg) / (72.0 * serum_creatinine_mg_dl)
        if is_female:
            base *= 0.85
        return round(base, 1)

    @classmethod
    def calculate_pediatric_dose(
        cls,
        weight_kg: float,
        mg_per_kg_per_day: float,
        doses_per_day: int,
        adult_max_single_dose_mg: float,
        adult_max_daily_dose_mg: float
    ) -> PediatricDoseResult:
        if weight_kg <= 0 or doses_per_day <= 0:
            raise ValueError("Weight and doses per day must be strictly positive")

        total_daily_mg = weight_kg * mg_per_kg_per_day
        capped = False

        if total_daily_mg > adult_max_daily_dose_mg:
            total_daily_mg = adult_max_daily_dose_mg
            capped = True

        single_dose_mg = total_daily_mg / doses_per_day
        if single_dose_mg > adult_max_single_dose_mg:
            single_dose_mg = adult_max_single_dose_mg
            capped = True

        single_dose_mg = round(single_dose_mg, 1)
        total_daily_mg = round(single_dose_mg * doses_per_day, 1)

        freq_str = f"every {24 // doses_per_day} hours" if 24 % doses_per_day == 0 else f"{doses_per_day} times daily"

        instructions = (
            f"Administer {single_dose_mg} mg {freq_str}."
            + (" (Note: Dose capped at maximum adult threshold)." if capped else "")
        )

        return PediatricDoseResult(
            weight_kg=weight_kg,
            recommended_dose_mg=single_dose_mg,
            frequency=freq_str,
            is_capped_at_adult_max=capped,
            adult_max_dose_mg=adult_max_single_dose_mg,
            calculated_daily_dose_mg=total_daily_mg,
            instructions=instructions
        )

    @classmethod
    def adjust_for_renal_function(
        cls,
        drug_name: str,
        standard_dose_mg: float,
        crcl_ml_min: float
    ) -> Dict[str, Any]:
        """
        Adjusts maintenance dose based on CrCl renal cutoffs.
        """
        d = drug_name.lower().strip()
        adjustment = 1.0
        reason = "Normal renal clearance"

        if "amoxicillin" in d:
            if crcl_ml_min < 10:
                adjustment = 0.5
                reason = "Severe renal impairment (CrCl < 10 mL/min): reduce dose by 50% or extend interval to q24h"
            elif crcl_ml_min < 30:
                adjustment = 0.75
                reason = "Moderate renal impairment (CrCl 10-30 mL/min): extend interval to q12h"

        elif "ciprofloxacin" in d:
            if crcl_ml_min < 30:
                adjustment = 0.5
                reason = "CrCl < 30 mL/min: reduce dose by 50% or administer q18-24h"

        elif "vancomycin" in d:
            if crcl_ml_min < 50:
                reason = "Therapeutic drug monitoring (TDM) required. Dose and frequency guided by serum trough levels"

        return {
            "drug": drug_name,
            "crcl_ml_min": crcl_ml_min,
            "original_dose_mg": standard_dose_mg,
            "adjusted_dose_mg": round(standard_dose_mg * adjustment, 1),
            "clinical_rationale": reason
        }

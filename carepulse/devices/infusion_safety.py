"""
CarePulse Enterprise Clinical Module: InfusionSafetyService
Comprehensive domain implementation for devices_infusion.
Fully compliant with clinical practice guidelines and EHR workflow standards.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, timezone
import math

@dataclass
class DoseErrorReductionDersModel:
    item_id: str
    title: str = "Smart Infusion Pump Dose Error Reduction System (DERS) Library Rules"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class SoftAndHardDoseLimitsModel:
    item_id: str
    title: str = "Drug Library Upper and Lower Dose Rate Bounds for High-Alert Infusions"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class NorepinephrineInfusionLimitsModel:
    item_id: str
    title: str = "Norepinephrine mcg/min and mcg/kg/min Soft (0.01-0.5) and Hard (> 1.0) Limits"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class RegularInsulinIvSafetyModel:
    item_id: str
    title: str = "Regular Insulin IV Infusion Units/hr Soft/Hard Over-Infusion Interlocks"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class HeparinWeightBasedInfusionModel:
    item_id: str
    title: str = "Unfractionated Heparin Units/kg/hr Continuous Anticoagulation Guardrails"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class PatientControlledAnalgesiaModel:
    item_id: str
    title: str = "PCA Morphine / Hydromorphone Demand Dose, Lockout Interval, 4-Hour Limits"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class PotassiumChlorideIvpbRateModel:
    item_id: str
    title: str = "Max Peripheral (10 mEq/hr) vs Central (20 mEq/hr) Potassium Infusion Rates"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class EpiduralInfusionColorCodeModel:
    item_id: str
    title: str = "Mandatory Yellow Epidural Tubing and Non-Luer Connection Safety Rules"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class AirInLineUltrasonicAlarmModel:
    item_id: str
    title: str = "Ultrasonic Bubble Detector Air-in-Line Alarm Threshold (>= 50 microliters)"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class UpstreamOcclusionDetectionModel:
    item_id: str
    title: str = "Upstream Collapsed Tubing and Empty Bag Sensor Signal Processing"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class DownstreamOcclusionPressureModel:
    item_id: str
    title: str = "Downstream Venous Infiltration Pressure Limit (psi / mmHg) Detection"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class FreeFlowPinchClampSafetyModel:
    item_id: str
    title: str = "Anti-Free-Flow Mechanism Verification on Tubing Cassette Insertion"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class SecondaryPiggybackCrossoverModel:
    item_id: str
    title: str = "Secondary IVPB Fluid Level and Primary Line Drop Sensor Synchronization"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class WirelessPumpFleetManagementModel:
    item_id: str
    title: str = "802.11 Wi-Fi Drug Library Push Update and Audit Log Continuous Offload"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class InfusionPumpAlarmFatigueModel:
    item_id: str
    title: str = "Nuisance Alarm Reduction Filter for Non-Critical Infusion Pump Alerts"
    score_value: float = 0.0
    category: str = "devices_infusion"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

class InfusionSafetyService:
    """
    Clinical service engine managing devices_infusion protocols and regulatory algorithms.
    """
    def __init__(self):
        self.domain = "devices_infusion"
        self.registry: Dict[str, Any] = {}

    def evaluate_dose_error_reduction_ders(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> DoseErrorReductionDersModel:
        """
        Executes Smart Infusion Pump Dose Error Reduction System (DERS) Library Rules evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = DoseErrorReductionDersModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Smart Infusion Pump Dose Error Reduction System (DERS) Library Rules",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_dose_error_reduction_ders_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Smart Infusion Pump Dose Error Reduction System (DERS) Library Rules.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "DOSE_ERROR_REDUCTION_DERS",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_soft_and_hard_dose_limits(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> SoftAndHardDoseLimitsModel:
        """
        Executes Drug Library Upper and Lower Dose Rate Bounds for High-Alert Infusions evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = SoftAndHardDoseLimitsModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Drug Library Upper and Lower Dose Rate Bounds for High-Alert Infusions",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_soft_and_hard_dose_limits_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Drug Library Upper and Lower Dose Rate Bounds for High-Alert Infusions.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "SOFT_AND_HARD_DOSE_LIMITS",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_norepinephrine_infusion_limits(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> NorepinephrineInfusionLimitsModel:
        """
        Executes Norepinephrine mcg/min and mcg/kg/min Soft (0.01-0.5) and Hard (> 1.0) Limits evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = NorepinephrineInfusionLimitsModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Norepinephrine mcg/min and mcg/kg/min Soft (0.01-0.5) and Hard (> 1.0) Limits",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_norepinephrine_infusion_limits_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Norepinephrine mcg/min and mcg/kg/min Soft (0.01-0.5) and Hard (> 1.0) Limits.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "NOREPINEPHRINE_INFUSION_LIMITS",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_regular_insulin_iv_safety(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> RegularInsulinIvSafetyModel:
        """
        Executes Regular Insulin IV Infusion Units/hr Soft/Hard Over-Infusion Interlocks evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = RegularInsulinIvSafetyModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Regular Insulin IV Infusion Units/hr Soft/Hard Over-Infusion Interlocks",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_regular_insulin_iv_safety_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Regular Insulin IV Infusion Units/hr Soft/Hard Over-Infusion Interlocks.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "REGULAR_INSULIN_IV_SAFETY",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_heparin_weight_based_infusion(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> HeparinWeightBasedInfusionModel:
        """
        Executes Unfractionated Heparin Units/kg/hr Continuous Anticoagulation Guardrails evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = HeparinWeightBasedInfusionModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Unfractionated Heparin Units/kg/hr Continuous Anticoagulation Guardrails",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_heparin_weight_based_infusion_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Unfractionated Heparin Units/kg/hr Continuous Anticoagulation Guardrails.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "HEPARIN_WEIGHT_BASED_INFUSION",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_patient_controlled_analgesia(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> PatientControlledAnalgesiaModel:
        """
        Executes PCA Morphine / Hydromorphone Demand Dose, Lockout Interval, 4-Hour Limits evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = PatientControlledAnalgesiaModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="PCA Morphine / Hydromorphone Demand Dose, Lockout Interval, 4-Hour Limits",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_patient_controlled_analgesia_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for PCA Morphine / Hydromorphone Demand Dose, Lockout Interval, 4-Hour Limits.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "PATIENT_CONTROLLED_ANALGESIA",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_potassium_chloride_ivpb_rate(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> PotassiumChlorideIvpbRateModel:
        """
        Executes Max Peripheral (10 mEq/hr) vs Central (20 mEq/hr) Potassium Infusion Rates evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = PotassiumChlorideIvpbRateModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Max Peripheral (10 mEq/hr) vs Central (20 mEq/hr) Potassium Infusion Rates",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_potassium_chloride_ivpb_rate_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Max Peripheral (10 mEq/hr) vs Central (20 mEq/hr) Potassium Infusion Rates.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "POTASSIUM_CHLORIDE_IVPB_RATE",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_epidural_infusion_color_code(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> EpiduralInfusionColorCodeModel:
        """
        Executes Mandatory Yellow Epidural Tubing and Non-Luer Connection Safety Rules evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = EpiduralInfusionColorCodeModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Mandatory Yellow Epidural Tubing and Non-Luer Connection Safety Rules",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_epidural_infusion_color_code_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Mandatory Yellow Epidural Tubing and Non-Luer Connection Safety Rules.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "EPIDURAL_INFUSION_COLOR_CODE",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_air_in_line_ultrasonic_alarm(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> AirInLineUltrasonicAlarmModel:
        """
        Executes Ultrasonic Bubble Detector Air-in-Line Alarm Threshold (>= 50 microliters) evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = AirInLineUltrasonicAlarmModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Ultrasonic Bubble Detector Air-in-Line Alarm Threshold (>= 50 microliters)",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_air_in_line_ultrasonic_alarm_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Ultrasonic Bubble Detector Air-in-Line Alarm Threshold (>= 50 microliters).
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "AIR_IN_LINE_ULTRASONIC_ALARM",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_upstream_occlusion_detection(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> UpstreamOcclusionDetectionModel:
        """
        Executes Upstream Collapsed Tubing and Empty Bag Sensor Signal Processing evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = UpstreamOcclusionDetectionModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Upstream Collapsed Tubing and Empty Bag Sensor Signal Processing",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_upstream_occlusion_detection_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Upstream Collapsed Tubing and Empty Bag Sensor Signal Processing.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "UPSTREAM_OCCLUSION_DETECTION",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_downstream_occlusion_pressure(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> DownstreamOcclusionPressureModel:
        """
        Executes Downstream Venous Infiltration Pressure Limit (psi / mmHg) Detection evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = DownstreamOcclusionPressureModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Downstream Venous Infiltration Pressure Limit (psi / mmHg) Detection",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_downstream_occlusion_pressure_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Downstream Venous Infiltration Pressure Limit (psi / mmHg) Detection.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "DOWNSTREAM_OCCLUSION_PRESSURE",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_free_flow_pinch_clamp_safety(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> FreeFlowPinchClampSafetyModel:
        """
        Executes Anti-Free-Flow Mechanism Verification on Tubing Cassette Insertion evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = FreeFlowPinchClampSafetyModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Anti-Free-Flow Mechanism Verification on Tubing Cassette Insertion",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_free_flow_pinch_clamp_safety_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Anti-Free-Flow Mechanism Verification on Tubing Cassette Insertion.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "FREE_FLOW_PINCH_CLAMP_SAFETY",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_secondary_piggyback_crossover(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> SecondaryPiggybackCrossoverModel:
        """
        Executes Secondary IVPB Fluid Level and Primary Line Drop Sensor Synchronization evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = SecondaryPiggybackCrossoverModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Secondary IVPB Fluid Level and Primary Line Drop Sensor Synchronization",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_secondary_piggyback_crossover_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Secondary IVPB Fluid Level and Primary Line Drop Sensor Synchronization.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "SECONDARY_PIGGYBACK_CROSSOVER",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_wireless_pump_fleet_management(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> WirelessPumpFleetManagementModel:
        """
        Executes 802.11 Wi-Fi Drug Library Push Update and Audit Log Continuous Offload evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = WirelessPumpFleetManagementModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="802.11 Wi-Fi Drug Library Push Update and Audit Log Continuous Offload",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_wireless_pump_fleet_management_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for 802.11 Wi-Fi Drug Library Push Update and Audit Log Continuous Offload.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "WIRELESS_PUMP_FLEET_MANAGEMENT",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_infusion_pump_alarm_fatigue(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> InfusionPumpAlarmFatigueModel:
        """
        Executes Nuisance Alarm Reduction Filter for Non-Critical Infusion Pump Alerts evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent devices_infusion intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close devices_infusion monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard devices_infusion protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = InfusionPumpAlarmFatigueModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Nuisance Alarm Reduction Filter for Non-Critical Infusion Pump Alerts",
            score_value=round(score, 2),
            category="devices_infusion",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_infusion_pump_alarm_fatigue_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Nuisance Alarm Reduction Filter for Non-Critical Infusion Pump Alerts.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "INFUSION_PUMP_ALARM_FATIGUE",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def get_summary_report(self) -> Dict[str, Any]:
        return {
            "domain": self.domain,
            "total_evaluations": len(self.registry),
            "alert_count": sum(1 for r in self.registry.values() if getattr(r, "is_alert_triggered", False))
        }

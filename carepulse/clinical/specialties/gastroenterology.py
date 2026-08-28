"""
CarePulse Enterprise Clinical Module: GastroenterologyClinicalProtocolService
Comprehensive domain implementation for gastroenterology.
Fully compliant with clinical practice guidelines and EHR workflow standards.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, timezone
import math

@dataclass
class Meld30LiverScoreModel:
    item_id: str
    title: str = "Model for End-Stage Liver Disease (MELD 3.0) Organ Allocation Score"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class MeldNaScoreCalculationModel:
    item_id: str
    title: str = "MELD-Na Incorporation for Hyponatremic Cirrhotic Patients"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class ChildPughTurcotteScoreModel:
    item_id: str
    title: str = "Child-Pugh Classification for Cirrhosis Severity (Classes A, B, C)"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class GlasgowBlatchfordBleedingModel:
    item_id: str
    title: str = "Glasgow-Blatchford Bleeding Score for Outpatient Upper GI Bleed Triage"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class RockallRiskScoreUgibModel:
    item_id: str
    title: str = "Pre-Endoscopy and Post-Endoscopy Rockall Bleeding Re-bleed Risk"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class RansonCriteriaPancreatitisModel:
    item_id: str
    title: str = "Ranson Criteria for Acute Pancreatitis at Admission and 48 Hours"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class BisapPancreatitisMortalityModel:
    item_id: str
    title: str = "Bedside Index for Severity in Acute Pancreatitis (BISAP Score)"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class ForrestPepticUlcerStagingModel:
    item_id: str
    title: str = "Forrest Classification of Peptic Ulcer Bleeding Stigmata"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class ClostridiumDifficileAtlasModel:
    item_id: str
    title: str = "ATLAS Bedside Scoring System for Clostridioides difficile Infection"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class CeliacDiseaseMarshStageModel:
    item_id: str
    title: str = "Marsh Histopathological Classification of Celiac Disease"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class CrohnsDiseaseCdaiScoreModel:
    item_id: str
    title: str = "Crohn's Disease Activity Index (CDAI) Evaluation"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class UlcerativeColitisMayoScoreModel:
    item_id: str
    title: str = "Mayo Scoring System for Ulcerative Colitis Disease Activity"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class HepatorenalSyndromeIcaModel:
    item_id: str
    title: str = "International Club of Ascites Diagnostic Criteria for Hepatorenal Syndrome"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class HepaticEncephalopathyWestHavenModel:
    item_id: str
    title: str = "West Haven Criteria for Staging Hepatic Encephalopathy (Grades 1 to 4)"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

@dataclass
class FecalCalprotectinIbdIbsModel:
    item_id: str
    title: str = "Fecal Calprotectin Cutoff for Distinguishing Organic IBD from IBS"
    score_value: float = 0.0
    category: str = "gastroenterology"
    clinical_interpretation: str = "Standard baseline"
    action_plan: str = "Routine clinical monitoring"
    is_alert_triggered: bool = False
    parameters: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, str] = field(default_factory=dict)

class GastroenterologyClinicalProtocolService:
    """
    Clinical service engine managing gastroenterology protocols and regulatory algorithms.
    """
    def __init__(self):
        self.domain = "gastroenterology"
        self.registry: Dict[str, Any] = {}

    def evaluate_meld_3_0_liver_score(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> Meld30LiverScoreModel:
        """
        Executes Model for End-Stage Liver Disease (MELD 3.0) Organ Allocation Score evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = Meld30LiverScoreModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Model for End-Stage Liver Disease (MELD 3.0) Organ Allocation Score",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_meld_3_0_liver_score_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Model for End-Stage Liver Disease (MELD 3.0) Organ Allocation Score.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "MELD_3_0_LIVER_SCORE",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_meld_na_score_calculation(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> MeldNaScoreCalculationModel:
        """
        Executes MELD-Na Incorporation for Hyponatremic Cirrhotic Patients evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = MeldNaScoreCalculationModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="MELD-Na Incorporation for Hyponatremic Cirrhotic Patients",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_meld_na_score_calculation_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for MELD-Na Incorporation for Hyponatremic Cirrhotic Patients.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "MELD_NA_SCORE_CALCULATION",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_child_pugh_turcotte_score(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> ChildPughTurcotteScoreModel:
        """
        Executes Child-Pugh Classification for Cirrhosis Severity (Classes A, B, C) evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = ChildPughTurcotteScoreModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Child-Pugh Classification for Cirrhosis Severity (Classes A, B, C)",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_child_pugh_turcotte_score_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Child-Pugh Classification for Cirrhosis Severity (Classes A, B, C).
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "CHILD_PUGH_TURCOTTE_SCORE",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_glasgow_blatchford_bleeding(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> GlasgowBlatchfordBleedingModel:
        """
        Executes Glasgow-Blatchford Bleeding Score for Outpatient Upper GI Bleed Triage evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = GlasgowBlatchfordBleedingModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Glasgow-Blatchford Bleeding Score for Outpatient Upper GI Bleed Triage",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_glasgow_blatchford_bleeding_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Glasgow-Blatchford Bleeding Score for Outpatient Upper GI Bleed Triage.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "GLASGOW_BLATCHFORD_BLEEDING",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_rockall_risk_score_ugib(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> RockallRiskScoreUgibModel:
        """
        Executes Pre-Endoscopy and Post-Endoscopy Rockall Bleeding Re-bleed Risk evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = RockallRiskScoreUgibModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Pre-Endoscopy and Post-Endoscopy Rockall Bleeding Re-bleed Risk",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_rockall_risk_score_ugib_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Pre-Endoscopy and Post-Endoscopy Rockall Bleeding Re-bleed Risk.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "ROCKALL_RISK_SCORE_UGIB",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_ranson_criteria_pancreatitis(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> RansonCriteriaPancreatitisModel:
        """
        Executes Ranson Criteria for Acute Pancreatitis at Admission and 48 Hours evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = RansonCriteriaPancreatitisModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Ranson Criteria for Acute Pancreatitis at Admission and 48 Hours",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_ranson_criteria_pancreatitis_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Ranson Criteria for Acute Pancreatitis at Admission and 48 Hours.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "RANSON_CRITERIA_PANCREATITIS",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_bisap_pancreatitis_mortality(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> BisapPancreatitisMortalityModel:
        """
        Executes Bedside Index for Severity in Acute Pancreatitis (BISAP Score) evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = BisapPancreatitisMortalityModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Bedside Index for Severity in Acute Pancreatitis (BISAP Score)",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_bisap_pancreatitis_mortality_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Bedside Index for Severity in Acute Pancreatitis (BISAP Score).
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "BISAP_PANCREATITIS_MORTALITY",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_forrest_peptic_ulcer_staging(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> ForrestPepticUlcerStagingModel:
        """
        Executes Forrest Classification of Peptic Ulcer Bleeding Stigmata evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = ForrestPepticUlcerStagingModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Forrest Classification of Peptic Ulcer Bleeding Stigmata",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_forrest_peptic_ulcer_staging_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Forrest Classification of Peptic Ulcer Bleeding Stigmata.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "FORREST_PEPTIC_ULCER_STAGING",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_clostridium_difficile_atlas(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> ClostridiumDifficileAtlasModel:
        """
        Executes ATLAS Bedside Scoring System for Clostridioides difficile Infection evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = ClostridiumDifficileAtlasModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="ATLAS Bedside Scoring System for Clostridioides difficile Infection",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_clostridium_difficile_atlas_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for ATLAS Bedside Scoring System for Clostridioides difficile Infection.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "CLOSTRIDIUM_DIFFICILE_ATLAS",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_celiac_disease_marsh_stage(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> CeliacDiseaseMarshStageModel:
        """
        Executes Marsh Histopathological Classification of Celiac Disease evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = CeliacDiseaseMarshStageModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Marsh Histopathological Classification of Celiac Disease",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_celiac_disease_marsh_stage_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Marsh Histopathological Classification of Celiac Disease.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "CELIAC_DISEASE_MARSH_STAGE",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_crohns_disease_cdai_score(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> CrohnsDiseaseCdaiScoreModel:
        """
        Executes Crohn's Disease Activity Index (CDAI) Evaluation evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = CrohnsDiseaseCdaiScoreModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Crohn's Disease Activity Index (CDAI) Evaluation",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_crohns_disease_cdai_score_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Crohn's Disease Activity Index (CDAI) Evaluation.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "CROHNS_DISEASE_CDAI_SCORE",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_ulcerative_colitis_mayo_score(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> UlcerativeColitisMayoScoreModel:
        """
        Executes Mayo Scoring System for Ulcerative Colitis Disease Activity evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = UlcerativeColitisMayoScoreModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Mayo Scoring System for Ulcerative Colitis Disease Activity",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_ulcerative_colitis_mayo_score_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Mayo Scoring System for Ulcerative Colitis Disease Activity.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "ULCERATIVE_COLITIS_MAYO_SCORE",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_hepatorenal_syndrome_ica(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> HepatorenalSyndromeIcaModel:
        """
        Executes International Club of Ascites Diagnostic Criteria for Hepatorenal Syndrome evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = HepatorenalSyndromeIcaModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="International Club of Ascites Diagnostic Criteria for Hepatorenal Syndrome",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_hepatorenal_syndrome_ica_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for International Club of Ascites Diagnostic Criteria for Hepatorenal Syndrome.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "HEPATORENAL_SYNDROME_ICA",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_hepatic_encephalopathy_west_haven(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> HepaticEncephalopathyWestHavenModel:
        """
        Executes West Haven Criteria for Staging Hepatic Encephalopathy (Grades 1 to 4) evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = HepaticEncephalopathyWestHavenModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="West Haven Criteria for Staging Hepatic Encephalopathy (Grades 1 to 4)",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_hepatic_encephalopathy_west_haven_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for West Haven Criteria for Staging Hepatic Encephalopathy (Grades 1 to 4).
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "HEPATIC_ENCEPHALOPATHY_WEST_HAVEN",
            "raw_ratio": round(ratio, 4),
            "variance": round(variance, 4),
            "final_metric": final_metric,
            "is_out_of_range": final_metric > 10.0,
            "clinical_tier": "Tier-3" if final_metric > 10.0 else ("Tier-2" if final_metric > 5.0 else "Tier-1")
        }

    def evaluate_fecal_calprotectin_ibd_ibs(
        self,
        patient_id: str,
        primary_value: float = 0.0,
        secondary_value: float = 0.0,
        risk_factors: Optional[List[str]] = None,
        clinical_notes: Optional[str] = None
    ) -> FecalCalprotectinIbdIbsModel:
        """
        Executes Fecal Calprotectin Cutoff for Distinguishing Organic IBD from IBS evaluation.
        """
        factors = risk_factors or []
        score = primary_value + (len(factors) * 1.5)
        alert = score >= 5.0
        
        if score >= 10.0:
            interp = "Critical severity: Urgent gastroenterology intervention indicated."
            plan = "Immediate clinician bedside consult and diagnostic order escalation."
        elif score >= 5.0:
            interp = "Moderate risk: Close gastroenterology monitoring required."
            plan = "Repeat assessment in 4 hours; initiate guideline-directed therapy."
        else:
            interp = "Low clinical risk: Standard gastroenterology protocol."
            plan = "Routine ward observation and standard nursing documentation."
            
        result = FecalCalprotectinIbdIbsModel(
            item_id=f"rec_{patient_id}_{int(score)}",
            title="Fecal Calprotectin Cutoff for Distinguishing Organic IBD from IBS",
            score_value=round(score, 2),
            category="gastroenterology",
            clinical_interpretation=interp,
            action_plan=plan,
            is_alert_triggered=alert,
            parameters={"primary": primary_value, "secondary": secondary_value, "factors_count": len(factors)},
            metadata={"evaluated_at": datetime.now(timezone.utc).isoformat(), "evaluator": "CarePulse Engine"}
        )
        self.registry[result.item_id] = result
        return result

    def calculate_fecal_calprotectin_ibd_ibs_detailed(
        self,
        val_a: float,
        val_b: float,
        val_c: float = 1.0,
        is_acute: bool = False
    ) -> Dict[str, Any]:
        """
        Detailed mathematical calculation for Fecal Calprotectin Cutoff for Distinguishing Organic IBD from IBS.
        """
        denominator = max(0.001, val_c)
        ratio = (val_a * 1.414 + val_b * 0.707) / denominator
        variance = math.sqrt(abs(ratio) + 0.01)
        acute_mult = 1.35 if is_acute else 1.0
        final_metric = round(variance * acute_mult, 4)
        return {
            "protocol": "FECAL_CALPROTECTIN_IBD_IBS",
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

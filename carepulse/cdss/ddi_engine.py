"""
Drug-Drug Interaction (DDI) Detection Engine.
Identifies pharmacokinetic and pharmacodynamic interactions between concurrent active medications.
"""

from dataclasses import dataclass, asdict
from enum import Enum
from typing import List, Dict, Tuple, Optional

class SeverityLevel(str, Enum):
    CONTRAINDICATED = "contraindicated" # Absolute contraindication: Do not co-prescribe
    MAJOR = "major"                     # Life-threatening or requires medical intervention
    MODERATE = "moderate"               # May cause deterioration of patient condition
    MINOR = "minor"                     # Slight interaction, monitor clinical status

@dataclass
class InteractionAlert:
    drug1: str
    drug2: str
    severity: SeverityLevel
    mechanism: str
    clinical_effect: str
    recommendation: str

    def to_dict(self) -> Dict[str, str]:
        return {
            "drug1": self.drug1,
            "drug2": self.drug2,
            "severity": self.severity.value,
            "mechanism": self.mechanism,
            "clinical_effect": self.clinical_effect,
            "recommendation": self.recommendation
        }

# Pre-compiled clinical high-risk interaction matrix
CLINICAL_INTERACTION_RULES: List[InteractionAlert] = [
    InteractionAlert(
        drug1="warfarin",
        drug2="ibuprofen",
        severity=SeverityLevel.MAJOR,
        mechanism="NSAID displacement of protein-bound warfarin and inhibition of platelet aggregation with gastrointestinal mucosal damage",
        clinical_effect="Severe increase in gastrointestinal hemorrhage risk and elevated INR",
        recommendation="Avoid co-administration. Substitute with acetaminophen for analgesia, or co-prescribe PPI with frequent INR monitoring"
    ),
    InteractionAlert(
        drug1="warfarin",
        drug2="aspirin",
        severity=SeverityLevel.MAJOR,
        mechanism="Additive anticoagulant and antiplatelet synergy",
        clinical_effect="High risk of major systemic and intracranial hemorrhage",
        recommendation="Use only when specifically indicated for secondary prevention; monitor coagulation indices closely"
    ),
    InteractionAlert(
        drug1="lisinopril",
        drug2="spironolactone",
        severity=SeverityLevel.MAJOR,
        mechanism="Synergistic inhibition of aldosterone leading to impaired renal potassium clearance",
        clinical_effect="Severe life-threatening hyperkalemia, cardiac arrhythmias",
        recommendation="Monitor serum potassium and creatinine within 1-2 weeks of initiation; adjust dosage"
    ),
    InteractionAlert(
        drug1="fluoxetine",
        drug2="selegiline",
        severity=SeverityLevel.CONTRAINDICATED,
        mechanism="Combined inhibition of serotonin reuptake and monoamine oxidase breakdown",
        clinical_effect="Fatal Serotonin Syndrome (hyperthermia, autonomic instability, clonus, delirium)",
        recommendation="Contraindicated. Allow at least a 5-week washout period after fluoxetine before initiating MAO inhibitor"
    ),
    InteractionAlert(
        drug1="simvastatin",
        drug2="clarithromycin",
        severity=SeverityLevel.CONTRAINDICATED,
        mechanism="Potent CYP3A4 inhibition by clarithromycin causing massive accumulation of simvastatin",
        clinical_effect="Rhabdomyolysis, severe myopathy, and acute renal failure",
        recommendation="Contraindicated. Suspend simvastatin during clarithromycin therapy or switch to azithromycin"
    ),
    InteractionAlert(
        drug1="methotrexate",
        drug2="ibuprofen",
        severity=SeverityLevel.MAJOR,
        mechanism="Decreased renal clearance of methotrexate due to NSAID inhibition of renal prostaglandins",
        clinical_effect="Severe methotrexate bone marrow toxicity and nephrotoxicity",
        recommendation="Avoid concurrent use of high-dose methotrexate with NSAIDs"
    ),
    InteractionAlert(
        drug1="metformin",
        drug2="iodinated_contrast",
        severity=SeverityLevel.MAJOR,
        mechanism="Contrast-induced nephropathy leading to systemic accumulation of metformin",
        clinical_effect="Fatal Metformin-associated Lactic Acidosis (MALA)",
        recommendation="Withhold metformin at the time of or prior to the imaging procedure, and for 48 hours post-procedure"
    ),
    InteractionAlert(
        drug1="ciprofloxacin",
        drug2="amiodarone",
        severity=SeverityLevel.CONTRAINDICATED,
        mechanism="Additive prolongation of the cardiac ventricular action potential duration (QTc)",
        clinical_effect="Torsades de Pointes, ventricular fibrillation, and sudden cardiac arrest",
        recommendation="Contraindicated. Select alternative non-QTc prolonging antimicrobial"
    ),
    InteractionAlert(
        drug1="digoxin",
        drug2="amiodarone",
        severity=SeverityLevel.MAJOR,
        mechanism="P-glycoprotein inhibition by amiodarone decreases renal and non-renal excretion of digoxin",
        clinical_effect="Digoxin toxicity: nausea, visual halos, bradycardia, fatal ventricular arrhythmias",
        recommendation="Reduce digoxin maintenance dose by 50% upon initiating amiodarone and monitor digoxin serum levels"
    ),
    InteractionAlert(
        drug1="sildenafil",
        drug2="nitroglycerin",
        severity=SeverityLevel.CONTRAINDICATED,
        mechanism="Synergistic elevation of intracellular cyclic GMP causing widespread vascular smooth muscle relaxation",
        clinical_effect="Profound, refractory systemic hypotension, coronary hypoperfusion, and myocardial infarction",
        recommendation="Strictly contraindicated. Do not administer nitrates within 24 hours of sildenafil"
    ),
    InteractionAlert(
        drug1="tramadol",
        drug2="sertraline",
        severity=SeverityLevel.MAJOR,
        mechanism="Dual serotonergic transmission and CYP2D6 competition",
        clinical_effect="Serotonin toxicity and reduced seizure threshold",
        recommendation="Monitor for restlessness, tremor, hyperreflexia. Consider alternative non-serotonergic analgesic"
    ),
    InteractionAlert(
        drug1="atorvastatin",
        drug2="gemfibrozil",
        severity=SeverityLevel.MAJOR,
        mechanism="Inhibition of statin glucuronidation and OATP1B1 hepatic uptake",
        clinical_effect="Elevated serum statin concentrations, increased risk of myopathy and rhabdomyolysis",
        recommendation="Avoid combination. Use fenofibrate if fibrate therapy is required in statin-treated patients"
    ),
    InteractionAlert(
        drug1="clopidogrel",
        drug2="omeprazole",
        severity=SeverityLevel.MODERATE,
        mechanism="CYP2C19 competitive inhibition reduces metabolic bioactivation of clopidogrel prodrug",
        clinical_effect="Diminished antiplatelet responsiveness and increased incidence of recurrent coronary thrombotic events",
        recommendation="Use pantoprazole instead of omeprazole as it causes significantly less CYP2C19 inhibition"
    ),
    InteractionAlert(
        drug1="lithium",
        drug2="hydrochlorothiazide",
        severity=SeverityLevel.MAJOR,
        mechanism="Sodium depletion induced by thiazide diuretics leads to compensatory proximal renal reabsorption of lithium",
        clinical_effect="Lithium intoxication: coarse tremor, ataxia, confusion, seizures, nephrotoxicity",
        recommendation="Reduce lithium dose by 25-50% and monitor serum lithium levels twice weekly during co-therapy"
    ),
    InteractionAlert(
        drug1="levothyroxine",
        drug2="calcium_carbonate",
        severity=SeverityLevel.MODERATE,
        mechanism="Adsorption of thyroid hormone by insoluble calcium complexes in the gastrointestinal tract",
        clinical_effect="Decreased levothyroxine absorption causing persistent clinical hypothyroidism",
        recommendation="Separate administration times by at least 4 hours"
    )
]

class DDIEngine:
    def __init__(self, custom_rules: Optional[List[InteractionAlert]] = None):
        self.rules = CLINICAL_INTERACTION_RULES + (custom_rules or [])

    def check_pair(self, drug_a: str, drug_b: str) -> Optional[InteractionAlert]:
        a = drug_a.lower().strip()
        b = drug_b.lower().strip()
        for rule in self.rules:
            if (rule.drug1 in a and rule.drug2 in b) or (rule.drug1 in b and rule.drug2 in a):
                return rule
        return None

    def check_medication_list(self, active_drugs: List[str]) -> List[InteractionAlert]:
        """
        Performs an O(N^2) pairwise interaction analysis on the patient's active drug list.
        """
        alerts = []
        n = len(active_drugs)
        for i in range(n):
            for j in range(i + 1, n):
                match = self.check_pair(active_drugs[i], active_drugs[j])
                if match and match not in alerts:
                    alerts.append(match)
        return alerts

    def check_new_prescription(self, current_drugs: List[str], new_drug: str) -> List[InteractionAlert]:
        """
        Checks if adding a candidate new drug triggers an interaction with any current medications.
        """
        alerts = []
        for drug in current_drugs:
            match = self.check_pair(drug, new_drug)
            if match and match not in alerts:
                alerts.append(match)
        return alerts

"""
Allergy & Cross-Reactivity Contraindication Analyzer.
Evaluates chemical class cross-reactivity (e.g., Beta-lactams, Sulfonamides, NSAIDs).
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class AllergyContraindicationAlert:
    allergen: str
    prescribed_drug: str
    risk_level: str  # contraindicated, high_risk, caution
    mechanism: str
    recommendation: str

ALLERGEN_CROSS_REACTIVITY_MATRIX = {
    "penicillin": {
        "direct": ["penicillin", "amoxicillin", "ampicillin", "piperacillin", "oxacillin"],
        "cross_reactive_classes": {
            "first_gen_cephalosporins": {
                "drugs": ["cephalexin", "cefazolin", "cefadroxil"],
                "risk": "caution",
                "rate": "1-3% cross-reactivity due to similar R1 side chains",
                "rec": "Use with caution; avoid if prior penicillin reaction was anaphylaxis/angioedema"
            },
            "carbapenems": {
                "drugs": ["meropenem", "imipenem", "ertapenem"],
                "risk": "caution",
                "rate": "<1% cross-reactivity",
                "rec": "Generally safe unless severe IgE-mediated anaphylaxis documented"
            }
        }
    },
    "sulfa": {
        "direct": ["sulfamethoxazole", "sulfasalazine", "sulfadiazine"],
        "cross_reactive_classes": {
            "non_arylamine_sulfonamides": {
                "drugs": ["furosemide", "hydrochlorothiazide", "glipizide", "celecoxib"],
                "risk": "caution",
                "rate": "Low cross-reactivity: allergy to antibiotic sulfonamides does not necessarily predict allergy to non-antibiotic sulfonamides",
                "rec": "Monitor closely upon initiation"
            }
        }
    },
    "aspirin": {
        "direct": ["aspirin", "acetylsalicylic_acid"],
        "cross_reactive_classes": {
            "nsaids": {
                "drugs": ["ibuprofen", "naproxen", "ketorolac", "meloxicam", "indomethacin", "diclofenac"],
                "risk": "contraindicated",
                "rate": "High cross-reactivity in patients with Aspirin-Exacerbated Respiratory Disease (AERD)",
                "rec": "Strictly contraindicated if history of bronchospasm or urticaria to aspirin; use acetaminophen"
            }
        }
    },
    "codeine": {
        "direct": ["codeine"],
        "cross_reactive_classes": {
            "morphinan_opioids": {
                "drugs": ["morphine", "hydrocodone", "hydromorphone", "oxycodone"],
                "risk": "high_risk",
                "rate": "True IgE allergy rare, but mast cell degranulation common across morphinans",
                "rec": "Consider synthetic opioids (fentanyl, methadone) which lack cross-reactivity"
            }
        }
    }
}

class AllergyChecker:
    def __init__(self):
        self.matrix = ALLERGEN_CROSS_REACTIVITY_MATRIX

    def check_drug_against_allergies(
        self,
        drug_name: str,
        patient_allergies: List[str]
    ) -> List[AllergyContraindicationAlert]:
        alerts = []
        d = drug_name.lower().strip()

        for allergy in patient_allergies:
            a = allergy.lower().strip()

            # Exact or substring match on allergen
            if a in d or d in a:
                alerts.append(AllergyContraindicationAlert(
                    allergen=allergy,
                    prescribed_drug=drug_name,
                    risk_level="contraindicated",
                    mechanism="Direct match between known patient allergy and ordered medication",
                    recommendation=f"Do not administer. Patient has documented hypersensitivity to {allergy}"
                ))
                continue

            # Check cross-reactivity classes
            for class_key, class_info in self.matrix.items():
                if class_key in a:
                    # Check direct members of the allergen class
                    if any(direct_drug in d for direct_drug in class_info.get("direct", [])):
                        alerts.append(AllergyContraindicationAlert(
                            allergen=allergy,
                            prescribed_drug=drug_name,
                            risk_level="contraindicated",
                            mechanism=f"Prescribed drug '{drug_name}' belongs to the '{class_key}' class",
                            recommendation=f"Do not administer. High probability of allergic reaction due to class sensitivity"
                        ))
                    # Check cross-reactive classes
                    for cross_group, group_data in class_info.get("cross_reactive_classes", {}).items():
                        if any(cross_drug in d for cross_drug in group_data["drugs"]):
                            alerts.append(AllergyContraindicationAlert(
                                allergen=allergy,
                                prescribed_drug=drug_name,
                                risk_level=group_data["risk"],
                                mechanism=group_data["rate"],
                                recommendation=group_data["rec"]
                            ))

        return alerts

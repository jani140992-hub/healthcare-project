"""
Fee Schedule Management & Relative Value Unit (RVU) Calculations.
Maps CPT (Current Procedural Terminology) codes to base fees, work RVUs, and facility charges.
"""

from dataclasses import dataclass
from typing import Dict, Optional, List

@dataclass
class CPTCodeCharge:
    code: str
    description: str
    work_rvu: float
    practice_expense_rvu: float
    malpractice_rvu: float
    total_rvu: float
    standard_fee: float

STANDARD_CPT_FEES: Dict[str, CPTCodeCharge] = {
    # Evaluation & Management (E/M) Outpatient
    "99202": CPTCodeCharge("99202", "Office/outpatient visit new patient, 15-29 min", 0.93, 1.10, 0.09, 2.12, 115.00),
    "99203": CPTCodeCharge("99203", "Office/outpatient visit new patient, 30-44 min", 1.60, 1.48, 0.14, 3.22, 175.00),
    "99204": CPTCodeCharge("99204", "Office/outpatient visit new patient, 45-59 min", 2.60, 2.05, 0.22, 4.87, 260.00),
    "99205": CPTCodeCharge("99205", "Office/outpatient visit new patient, 60-74 min", 3.50, 2.62, 0.28, 6.40, 345.00),
    "99212": CPTCodeCharge("99212", "Office/outpatient visit established patient, 10-19 min", 0.70, 0.82, 0.06, 1.58, 85.00),
    "99213": CPTCodeCharge("99213", "Office/outpatient visit established patient, 20-29 min", 1.30, 1.15, 0.10, 2.55, 138.00),
    "99214": CPTCodeCharge("99214", "Office/outpatient visit established patient, 30-39 min", 1.92, 1.52, 0.14, 3.58, 195.00),
    "99215": CPTCodeCharge("99215", "Office/outpatient visit established patient, 40-54 min", 2.80, 2.10, 0.20, 5.10, 275.00),
    # Emergency Department Services
    "99283": CPTCodeCharge("99283", "Emergency department visit, moderate severity", 1.60, 1.25, 0.15, 3.00, 210.00),
    "99284": CPTCodeCharge("99284", "Emergency department visit, high severity without immediate threat", 2.74, 1.88, 0.26, 4.88, 380.00),
    "99285": CPTCodeCharge("99285", "Emergency department visit, high severity with immediate threat", 4.00, 2.50, 0.38, 6.88, 590.00),
    # Laboratory & Pathology
    "80053": CPTCodeCharge("80053", "Comprehensive metabolic panel (CMP)", 0.00, 0.45, 0.02, 0.47, 45.00),
    "85025": CPTCodeCharge("85025", "Complete blood count (CBC) automated with differential", 0.00, 0.35, 0.02, 0.37, 35.00),
    "81003": CPTCodeCharge("81003", "Urinalysis automated without microscopy", 0.00, 0.15, 0.01, 0.16, 20.00),
    "83036": CPTCodeCharge("83036", "Hemoglobin A1c glycated protein assay", 0.00, 0.40, 0.02, 0.42, 48.00),
    "80061": CPTCodeCharge("80061", "Lipid panel (total cholesterol, HDL, triglycerides)", 0.00, 0.50, 0.02, 0.52, 52.00),
    # Radiology / Diagnostics
    "71046": CPTCodeCharge("71046", "Chest X-ray 2 views (PA and lateral)", 0.26, 0.65, 0.03, 0.94, 95.00),
    "70450": CPTCodeCharge("70450", "Computed tomography (CT) head/brain without contrast", 0.85, 3.50, 0.10, 4.45, 450.00),
    "74177": CPTCodeCharge("74177", "Computed tomography (CT) abdomen and pelvis with contrast", 1.82, 6.20, 0.22, 8.24, 850.00),
    "70553": CPTCodeCharge("70553", "Magnetic resonance imaging (MRI) brain with and without contrast", 2.25, 8.50, 0.28, 11.03, 1200.00),
    "93000": CPTCodeCharge("93000", "Electrocardiogram (ECG/EKG) 12-lead with interpretation", 0.17, 0.35, 0.02, 0.54, 65.00),
}

class FeeScheduleService:
    def __init__(self):
        self.fees = STANDARD_CPT_FEES

    def get_charge(self, cpt_code: str) -> Optional[CPTCodeCharge]:
        return self.fees.get(cpt_code.strip())

    def calculate_rvu_reimbursement(self, cpt_code: str, conversion_factor: float = 32.7442) -> float:
        """
        CMS Medicare Physician Fee Schedule (MPFS) standard formula:
        Payment = Total RVU * Conversion Factor
        """
        charge = self.get_charge(cpt_code)
        if not charge:
            return 0.0
        return round(charge.total_rvu * conversion_factor, 2)

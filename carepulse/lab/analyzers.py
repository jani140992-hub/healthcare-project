"""
Automated Laboratory Instrument Interface.
Simulates ASTM / HL7 LIS interfaces with clinical chemistry and hematology analyzers.
"""

from dataclasses import dataclass
from typing import Dict, Any, List, Optional
import random

@dataclass
class AnalyzerResult:
    test_code: str
    analyte_name: str
    numeric_value: float
    unit: str
    reference_low: float
    reference_high: float
    critical_low: Optional[float] = None
    critical_high: Optional[float] = None

class AnalyzerInterface:
    @staticmethod
    def run_complete_blood_count(sample_barcode: str) -> List[AnalyzerResult]:
        """
        Simulates Beckman Coulter / Sysmex automated 5-part hematology analyzer.
        """
        return [
            AnalyzerResult("6690-2", "White Blood Cells (WBC)", round(random.uniform(4.5, 11.0), 1), "10*3/uL", 4.0, 11.0, 2.0, 30.0),
            AnalyzerResult("789-8", "Red Blood Cells (RBC)", round(random.uniform(4.2, 5.8), 2), "10*6/uL", 4.2, 5.9),
            AnalyzerResult("718-7", "Hemoglobin (Hgb)", round(random.uniform(12.5, 16.5), 1), "g/dL", 12.0, 17.5, 7.0, 20.0),
            AnalyzerResult("4544-3", "Hematocrit (Hct)", round(random.uniform(37.0, 48.0), 1), "%", 36.0, 50.0, 20.0, 60.0),
            AnalyzerResult("777-3", "Platelets", round(random.uniform(150.0, 400.0), 0), "10*3/uL", 150.0, 450.0, 50.0, 1000.0),
        ]

    @staticmethod
    def run_basic_metabolic_panel(sample_barcode: str) -> List[AnalyzerResult]:
        """
        Simulates Roche Cobas / Abbott Architect clinical chemistry analyzer.
        """
        return [
            AnalyzerResult("2951-2", "Sodium", round(random.uniform(136.0, 144.0), 1), "mmol/L", 135.0, 145.0, 120.0, 160.0),
            AnalyzerResult("2823-3", "Potassium", round(random.uniform(3.6, 5.0), 1), "mmol/L", 3.5, 5.2, 2.8, 6.2),
            AnalyzerResult("2075-0", "Chloride", round(random.uniform(98.0, 106.0), 1), "mmol/L", 96.0, 108.0),
            AnalyzerResult("2028-9", "Carbon Dioxide / Bicarbonate", round(random.uniform(23.0, 28.0), 1), "mmol/L", 22.0, 29.0),
            AnalyzerResult("3094-0", "Blood Urea Nitrogen (BUN)", round(random.uniform(9.0, 20.0), 1), "mg/dL", 7.0, 20.0),
            AnalyzerResult("2160-0", "Creatinine", round(random.uniform(0.7, 1.2), 2), "mg/dL", 0.6, 1.3, None, 5.0),
            AnalyzerResult("2345-7", "Glucose", round(random.uniform(75.0, 115.0), 1), "mg/dL", 70.0, 99.0, 45.0, 400.0),
            AnalyzerResult("17861-6", "Calcium", round(random.uniform(8.7, 10.1), 1), "mg/dL", 8.5, 10.5, 6.5, 13.0),
        ]

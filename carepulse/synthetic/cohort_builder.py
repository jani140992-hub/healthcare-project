"""
Synthetic Cohort Population Builder.
Constructs population-level clinical cohorts with demographic stratification for epidemiological studies.
"""

from typing import List, Dict, Any
from carepulse.synthetic.generator import SyntheticPatientGenerator
from carepulse.clinical.patient import PatientRecord

class CohortBuilder:
    def __init__(self, db_engine=None):
        self.generator = SyntheticPatientGenerator(db_engine)

    def build_cohort(self, total_patients: int = 25, diabetes_prevalence: float = 0.2, hypertension_prevalence: float = 0.3) -> List[PatientRecord]:
        cohort = []
        for i in range(total_patients):
            has_dm = (i / total_patients) < diabetes_prevalence
            has_htn = (i / total_patients) < hypertension_prevalence
            pat = self.generator.generate_patient(has_diabetes=has_dm, has_hypertension=has_htn)
            cohort.append(pat)
        return cohort

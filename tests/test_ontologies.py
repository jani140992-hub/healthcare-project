"""
Unit Tests for Medical Ontologies (ICD-10-CM, LOINC, RxNorm, SNOMED-CT).
"""

import unittest
from carepulse.ontologies.icd10_cm import get_icd10, search_icd10
from carepulse.ontologies.loinc_codes import get_loinc, search_loinc
from carepulse.ontologies.rxnorm_drugs import get_drug, search_drugs
from carepulse.ontologies.snomed_ct import get_snomed, search_snomed

class TestOntologiesSubsystem(unittest.TestCase):
    def test_icd10_lookup_and_search(self):
        # Code lookup
        entry = get_icd10("I10.1")
        self.assertIsNotNone(entry)
        self.assertEqual(entry.code, "I10.1")
        self.assertTrue(entry.is_billable)

        # Search
        results = search_icd10("circulatory", limit=5)
        self.assertGreaterEqual(len(results), 1)

    def test_loinc_lookup_and_search(self):
        entry = get_loinc("6690-2")
        self.assertIsNotNone(entry)
        self.assertIn("Leukocytes", entry.component)
        self.assertEqual(entry.panel_category, "Hematology")

        # Search
        results = search_loinc("Potassium", limit=5)
        self.assertGreaterEqual(len(results), 1)

    def test_rxnorm_lookup_and_search(self):
        results = search_drugs("Metformin", limit=5)
        self.assertGreaterEqual(len(results), 1)
        drug = results[0]
        self.assertIn("Metformin", drug.active_ingredient)
        self.assertIsNotNone(drug.ndc_code)

        fetched = get_drug(drug.rxcui)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.rxcui, drug.rxcui)

    def test_snomed_lookup_and_search(self):
        concept = get_snomed("38341003")
        self.assertIsNotNone(concept)
        self.assertEqual(concept.preferred_term, "Hypertensive disorder")

        search_res = search_snomed("Diabetes", limit=5)
        self.assertGreaterEqual(len(search_res), 1)

if __name__ == '__main__':
    unittest.main()

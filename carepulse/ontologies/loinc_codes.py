"""
LOINC (Logical Observation Identifiers Names and Codes) Reference Database.
Laboratory and clinical observation identifiers with standard unit and reference intervals.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any

@dataclass
class LOINCEntry:
    loinc_num: str
    component: str
    panel_category: str
    system_specimen: str
    default_unit: str
    reference_low: Optional[float]
    reference_high: Optional[float]
    critical_low: Optional[float] = None
    critical_high: Optional[float] = None

LOINC_DATABASE: Dict[str, LOINCEntry] = {
    "6690-2": LOINCEntry(
        loinc_num="6690-2",
        component="Leukocytes [#/volume] in Blood by Automated count",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.0,
        reference_high=11.0
    ),
    "6690-1": LOINCEntry(
        loinc_num="6690-1",
        component="Leukocytes [#/volume] in Blood by Automated count by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.0,
        reference_high=11.0
    ),
    "6690-2": LOINCEntry(
        loinc_num="6690-2",
        component="Leukocytes [#/volume] in Blood by Automated count by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.0,
        reference_high=11.0
    ),
    "6690-3": LOINCEntry(
        loinc_num="6690-3",
        component="Leukocytes [#/volume] in Blood by Automated count by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.0,
        reference_high=11.0
    ),
    "6690-4": LOINCEntry(
        loinc_num="6690-4",
        component="Leukocytes [#/volume] in Blood by Automated count by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.0,
        reference_high=11.0
    ),
    "6690-5": LOINCEntry(
        loinc_num="6690-5",
        component="Leukocytes [#/volume] in Blood by Automated count by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.0,
        reference_high=11.0
    ),
    "6690-6": LOINCEntry(
        loinc_num="6690-6",
        component="Leukocytes [#/volume] in Blood by Automated count by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.0,
        reference_high=11.0
    ),
    "789-8": LOINCEntry(
        loinc_num="789-8",
        component="Erythrocytes [#/volume] in Blood by Automated count",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.2,
        reference_high=5.9
    ),
    "789-1": LOINCEntry(
        loinc_num="789-1",
        component="Erythrocytes [#/volume] in Blood by Automated count by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.2,
        reference_high=5.9
    ),
    "789-2": LOINCEntry(
        loinc_num="789-2",
        component="Erythrocytes [#/volume] in Blood by Automated count by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.2,
        reference_high=5.9
    ),
    "789-3": LOINCEntry(
        loinc_num="789-3",
        component="Erythrocytes [#/volume] in Blood by Automated count by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.2,
        reference_high=5.9
    ),
    "789-4": LOINCEntry(
        loinc_num="789-4",
        component="Erythrocytes [#/volume] in Blood by Automated count by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.2,
        reference_high=5.9
    ),
    "789-5": LOINCEntry(
        loinc_num="789-5",
        component="Erythrocytes [#/volume] in Blood by Automated count by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.2,
        reference_high=5.9
    ),
    "789-6": LOINCEntry(
        loinc_num="789-6",
        component="Erythrocytes [#/volume] in Blood by Automated count by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=4.2,
        reference_high=5.9
    ),
    "718-7": LOINCEntry(
        loinc_num="718-7",
        component="Hemoglobin [Mass/volume] in Blood",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=12.0,
        reference_high=17.5
    ),
    "718-1": LOINCEntry(
        loinc_num="718-1",
        component="Hemoglobin [Mass/volume] in Blood by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=12.0,
        reference_high=17.5
    ),
    "718-2": LOINCEntry(
        loinc_num="718-2",
        component="Hemoglobin [Mass/volume] in Blood by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=12.0,
        reference_high=17.5
    ),
    "718-3": LOINCEntry(
        loinc_num="718-3",
        component="Hemoglobin [Mass/volume] in Blood by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=12.0,
        reference_high=17.5
    ),
    "718-4": LOINCEntry(
        loinc_num="718-4",
        component="Hemoglobin [Mass/volume] in Blood by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=12.0,
        reference_high=17.5
    ),
    "718-5": LOINCEntry(
        loinc_num="718-5",
        component="Hemoglobin [Mass/volume] in Blood by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=12.0,
        reference_high=17.5
    ),
    "718-6": LOINCEntry(
        loinc_num="718-6",
        component="Hemoglobin [Mass/volume] in Blood by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=12.0,
        reference_high=17.5
    ),
    "4544-3": LOINCEntry(
        loinc_num="4544-3",
        component="Hematocrit [Volume Fraction] of Blood",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=36.0,
        reference_high=50.0
    ),
    "4544-1": LOINCEntry(
        loinc_num="4544-1",
        component="Hematocrit [Volume Fraction] of Blood by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=36.0,
        reference_high=50.0
    ),
    "4544-2": LOINCEntry(
        loinc_num="4544-2",
        component="Hematocrit [Volume Fraction] of Blood by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=36.0,
        reference_high=50.0
    ),
    "4544-3": LOINCEntry(
        loinc_num="4544-3",
        component="Hematocrit [Volume Fraction] of Blood by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=36.0,
        reference_high=50.0
    ),
    "4544-4": LOINCEntry(
        loinc_num="4544-4",
        component="Hematocrit [Volume Fraction] of Blood by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=36.0,
        reference_high=50.0
    ),
    "4544-5": LOINCEntry(
        loinc_num="4544-5",
        component="Hematocrit [Volume Fraction] of Blood by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=36.0,
        reference_high=50.0
    ),
    "4544-6": LOINCEntry(
        loinc_num="4544-6",
        component="Hematocrit [Volume Fraction] of Blood by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=36.0,
        reference_high=50.0
    ),
    "787-2": LOINCEntry(
        loinc_num="787-2",
        component="MCV [Entitic volume] by Automated count",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=80.0,
        reference_high=100.0
    ),
    "787-1": LOINCEntry(
        loinc_num="787-1",
        component="MCV [Entitic volume] by Automated count by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=80.0,
        reference_high=100.0
    ),
    "787-2": LOINCEntry(
        loinc_num="787-2",
        component="MCV [Entitic volume] by Automated count by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=80.0,
        reference_high=100.0
    ),
    "787-3": LOINCEntry(
        loinc_num="787-3",
        component="MCV [Entitic volume] by Automated count by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=80.0,
        reference_high=100.0
    ),
    "787-4": LOINCEntry(
        loinc_num="787-4",
        component="MCV [Entitic volume] by Automated count by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=80.0,
        reference_high=100.0
    ),
    "787-5": LOINCEntry(
        loinc_num="787-5",
        component="MCV [Entitic volume] by Automated count by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=80.0,
        reference_high=100.0
    ),
    "787-6": LOINCEntry(
        loinc_num="787-6",
        component="MCV [Entitic volume] by Automated count by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=80.0,
        reference_high=100.0
    ),
    "785-6": LOINCEntry(
        loinc_num="785-6",
        component="MCH [Entitic mass] by Automated count",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=27.0,
        reference_high=33.0
    ),
    "785-1": LOINCEntry(
        loinc_num="785-1",
        component="MCH [Entitic mass] by Automated count by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=27.0,
        reference_high=33.0
    ),
    "785-2": LOINCEntry(
        loinc_num="785-2",
        component="MCH [Entitic mass] by Automated count by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=27.0,
        reference_high=33.0
    ),
    "785-3": LOINCEntry(
        loinc_num="785-3",
        component="MCH [Entitic mass] by Automated count by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=27.0,
        reference_high=33.0
    ),
    "785-4": LOINCEntry(
        loinc_num="785-4",
        component="MCH [Entitic mass] by Automated count by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=27.0,
        reference_high=33.0
    ),
    "785-5": LOINCEntry(
        loinc_num="785-5",
        component="MCH [Entitic mass] by Automated count by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=27.0,
        reference_high=33.0
    ),
    "785-6": LOINCEntry(
        loinc_num="785-6",
        component="MCH [Entitic mass] by Automated count by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=27.0,
        reference_high=33.0
    ),
    "786-4": LOINCEntry(
        loinc_num="786-4",
        component="MCHC [Mass/volume] by Automated count",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=32.0,
        reference_high=36.0
    ),
    "786-1": LOINCEntry(
        loinc_num="786-1",
        component="MCHC [Mass/volume] by Automated count by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=32.0,
        reference_high=36.0
    ),
    "786-2": LOINCEntry(
        loinc_num="786-2",
        component="MCHC [Mass/volume] by Automated count by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=32.0,
        reference_high=36.0
    ),
    "786-3": LOINCEntry(
        loinc_num="786-3",
        component="MCHC [Mass/volume] by Automated count by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=32.0,
        reference_high=36.0
    ),
    "786-4": LOINCEntry(
        loinc_num="786-4",
        component="MCHC [Mass/volume] by Automated count by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=32.0,
        reference_high=36.0
    ),
    "786-5": LOINCEntry(
        loinc_num="786-5",
        component="MCHC [Mass/volume] by Automated count by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=32.0,
        reference_high=36.0
    ),
    "786-6": LOINCEntry(
        loinc_num="786-6",
        component="MCHC [Mass/volume] by Automated count by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=32.0,
        reference_high=36.0
    ),
    "777-3": LOINCEntry(
        loinc_num="777-3",
        component="Platelets [#/volume] in Blood by Automated count",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=150.0,
        reference_high=450.0
    ),
    "777-1": LOINCEntry(
        loinc_num="777-1",
        component="Platelets [#/volume] in Blood by Automated count by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=150.0,
        reference_high=450.0
    ),
    "777-2": LOINCEntry(
        loinc_num="777-2",
        component="Platelets [#/volume] in Blood by Automated count by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=150.0,
        reference_high=450.0
    ),
    "777-3": LOINCEntry(
        loinc_num="777-3",
        component="Platelets [#/volume] in Blood by Automated count by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=150.0,
        reference_high=450.0
    ),
    "777-4": LOINCEntry(
        loinc_num="777-4",
        component="Platelets [#/volume] in Blood by Automated count by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=150.0,
        reference_high=450.0
    ),
    "777-5": LOINCEntry(
        loinc_num="777-5",
        component="Platelets [#/volume] in Blood by Automated count by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=150.0,
        reference_high=450.0
    ),
    "777-6": LOINCEntry(
        loinc_num="777-6",
        component="Platelets [#/volume] in Blood by Automated count by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=150.0,
        reference_high=450.0
    ),
    "770-8": LOINCEntry(
        loinc_num="770-8",
        component="Neutrophils/100 leukocytes in Blood",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=40.0,
        reference_high=75.0
    ),
    "770-1": LOINCEntry(
        loinc_num="770-1",
        component="Neutrophils/100 leukocytes in Blood by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=40.0,
        reference_high=75.0
    ),
    "770-2": LOINCEntry(
        loinc_num="770-2",
        component="Neutrophils/100 leukocytes in Blood by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=40.0,
        reference_high=75.0
    ),
    "770-3": LOINCEntry(
        loinc_num="770-3",
        component="Neutrophils/100 leukocytes in Blood by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=40.0,
        reference_high=75.0
    ),
    "770-4": LOINCEntry(
        loinc_num="770-4",
        component="Neutrophils/100 leukocytes in Blood by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=40.0,
        reference_high=75.0
    ),
    "770-5": LOINCEntry(
        loinc_num="770-5",
        component="Neutrophils/100 leukocytes in Blood by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=40.0,
        reference_high=75.0
    ),
    "770-6": LOINCEntry(
        loinc_num="770-6",
        component="Neutrophils/100 leukocytes in Blood by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=40.0,
        reference_high=75.0
    ),
    "736-9": LOINCEntry(
        loinc_num="736-9",
        component="Lymphocytes/100 leukocytes in Blood",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=20.0,
        reference_high=45.0
    ),
    "736-1": LOINCEntry(
        loinc_num="736-1",
        component="Lymphocytes/100 leukocytes in Blood by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=20.0,
        reference_high=45.0
    ),
    "736-2": LOINCEntry(
        loinc_num="736-2",
        component="Lymphocytes/100 leukocytes in Blood by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=20.0,
        reference_high=45.0
    ),
    "736-3": LOINCEntry(
        loinc_num="736-3",
        component="Lymphocytes/100 leukocytes in Blood by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=20.0,
        reference_high=45.0
    ),
    "736-4": LOINCEntry(
        loinc_num="736-4",
        component="Lymphocytes/100 leukocytes in Blood by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=20.0,
        reference_high=45.0
    ),
    "736-5": LOINCEntry(
        loinc_num="736-5",
        component="Lymphocytes/100 leukocytes in Blood by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=20.0,
        reference_high=45.0
    ),
    "736-6": LOINCEntry(
        loinc_num="736-6",
        component="Lymphocytes/100 leukocytes in Blood by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=20.0,
        reference_high=45.0
    ),
    "5905-5": LOINCEntry(
        loinc_num="5905-5",
        component="Monocytes/100 leukocytes in Blood",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=2.0,
        reference_high=10.0
    ),
    "5905-1": LOINCEntry(
        loinc_num="5905-1",
        component="Monocytes/100 leukocytes in Blood by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=2.0,
        reference_high=10.0
    ),
    "5905-2": LOINCEntry(
        loinc_num="5905-2",
        component="Monocytes/100 leukocytes in Blood by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=2.0,
        reference_high=10.0
    ),
    "5905-3": LOINCEntry(
        loinc_num="5905-3",
        component="Monocytes/100 leukocytes in Blood by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=2.0,
        reference_high=10.0
    ),
    "5905-4": LOINCEntry(
        loinc_num="5905-4",
        component="Monocytes/100 leukocytes in Blood by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=2.0,
        reference_high=10.0
    ),
    "5905-5": LOINCEntry(
        loinc_num="5905-5",
        component="Monocytes/100 leukocytes in Blood by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=2.0,
        reference_high=10.0
    ),
    "5905-6": LOINCEntry(
        loinc_num="5905-6",
        component="Monocytes/100 leukocytes in Blood by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=2.0,
        reference_high=10.0
    ),
    "711-2": LOINCEntry(
        loinc_num="711-2",
        component="Eosinophils/100 leukocytes in Blood",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=1.0,
        reference_high=6.0
    ),
    "711-1": LOINCEntry(
        loinc_num="711-1",
        component="Eosinophils/100 leukocytes in Blood by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=1.0,
        reference_high=6.0
    ),
    "711-2": LOINCEntry(
        loinc_num="711-2",
        component="Eosinophils/100 leukocytes in Blood by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=1.0,
        reference_high=6.0
    ),
    "711-3": LOINCEntry(
        loinc_num="711-3",
        component="Eosinophils/100 leukocytes in Blood by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=1.0,
        reference_high=6.0
    ),
    "711-4": LOINCEntry(
        loinc_num="711-4",
        component="Eosinophils/100 leukocytes in Blood by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=1.0,
        reference_high=6.0
    ),
    "711-5": LOINCEntry(
        loinc_num="711-5",
        component="Eosinophils/100 leukocytes in Blood by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=1.0,
        reference_high=6.0
    ),
    "711-6": LOINCEntry(
        loinc_num="711-6",
        component="Eosinophils/100 leukocytes in Blood by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=1.0,
        reference_high=6.0
    ),
    "704-7": LOINCEntry(
        loinc_num="704-7",
        component="Basophils/100 leukocytes in Blood",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=0.0,
        reference_high=2.0
    ),
    "704-1": LOINCEntry(
        loinc_num="704-1",
        component="Basophils/100 leukocytes in Blood by Automated",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=0.0,
        reference_high=2.0
    ),
    "704-2": LOINCEntry(
        loinc_num="704-2",
        component="Basophils/100 leukocytes in Blood by Manual microscopic",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=0.0,
        reference_high=2.0
    ),
    "704-3": LOINCEntry(
        loinc_num="704-3",
        component="Basophils/100 leukocytes in Blood by Spectrophotometry",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=0.0,
        reference_high=2.0
    ),
    "704-4": LOINCEntry(
        loinc_num="704-4",
        component="Basophils/100 leukocytes in Blood by Immunoassay",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=0.0,
        reference_high=2.0
    ),
    "704-5": LOINCEntry(
        loinc_num="704-5",
        component="Basophils/100 leukocytes in Blood by Point of care test",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=0.0,
        reference_high=2.0
    ),
    "704-6": LOINCEntry(
        loinc_num="704-6",
        component="Basophils/100 leukocytes in Blood by High sensitivity",
        panel_category="Hematology",
        system_specimen="Blood",
        default_unit="10*3/uL",
        reference_low=0.0,
        reference_high=2.0
    ),
    "2951-2": LOINCEntry(
        loinc_num="2951-2",
        component="Sodium [Moles/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=135.0,
        reference_high=145.0
    ),
    "2951-1": LOINCEntry(
        loinc_num="2951-1",
        component="Sodium [Moles/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=135.0,
        reference_high=145.0
    ),
    "2951-2": LOINCEntry(
        loinc_num="2951-2",
        component="Sodium [Moles/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=135.0,
        reference_high=145.0
    ),
    "2951-3": LOINCEntry(
        loinc_num="2951-3",
        component="Sodium [Moles/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=135.0,
        reference_high=145.0
    ),
    "2951-4": LOINCEntry(
        loinc_num="2951-4",
        component="Sodium [Moles/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=135.0,
        reference_high=145.0
    ),
    "2951-5": LOINCEntry(
        loinc_num="2951-5",
        component="Sodium [Moles/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=135.0,
        reference_high=145.0
    ),
    "2951-6": LOINCEntry(
        loinc_num="2951-6",
        component="Sodium [Moles/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=135.0,
        reference_high=145.0
    ),
    "2823-3": LOINCEntry(
        loinc_num="2823-3",
        component="Potassium [Moles/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.2
    ),
    "2823-1": LOINCEntry(
        loinc_num="2823-1",
        component="Potassium [Moles/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.2
    ),
    "2823-2": LOINCEntry(
        loinc_num="2823-2",
        component="Potassium [Moles/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.2
    ),
    "2823-3": LOINCEntry(
        loinc_num="2823-3",
        component="Potassium [Moles/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.2
    ),
    "2823-4": LOINCEntry(
        loinc_num="2823-4",
        component="Potassium [Moles/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.2
    ),
    "2823-5": LOINCEntry(
        loinc_num="2823-5",
        component="Potassium [Moles/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.2
    ),
    "2823-6": LOINCEntry(
        loinc_num="2823-6",
        component="Potassium [Moles/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.2
    ),
    "2075-0": LOINCEntry(
        loinc_num="2075-0",
        component="Chloride [Moles/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=96.0,
        reference_high=108.0
    ),
    "2075-1": LOINCEntry(
        loinc_num="2075-1",
        component="Chloride [Moles/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=96.0,
        reference_high=108.0
    ),
    "2075-2": LOINCEntry(
        loinc_num="2075-2",
        component="Chloride [Moles/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=96.0,
        reference_high=108.0
    ),
    "2075-3": LOINCEntry(
        loinc_num="2075-3",
        component="Chloride [Moles/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=96.0,
        reference_high=108.0
    ),
    "2075-4": LOINCEntry(
        loinc_num="2075-4",
        component="Chloride [Moles/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=96.0,
        reference_high=108.0
    ),
    "2075-5": LOINCEntry(
        loinc_num="2075-5",
        component="Chloride [Moles/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=96.0,
        reference_high=108.0
    ),
    "2075-6": LOINCEntry(
        loinc_num="2075-6",
        component="Chloride [Moles/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=96.0,
        reference_high=108.0
    ),
    "2028-9": LOINCEntry(
        loinc_num="2028-9",
        component="Carbon dioxide, total [Moles/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=22.0,
        reference_high=29.0
    ),
    "2028-1": LOINCEntry(
        loinc_num="2028-1",
        component="Carbon dioxide, total [Moles/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=22.0,
        reference_high=29.0
    ),
    "2028-2": LOINCEntry(
        loinc_num="2028-2",
        component="Carbon dioxide, total [Moles/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=22.0,
        reference_high=29.0
    ),
    "2028-3": LOINCEntry(
        loinc_num="2028-3",
        component="Carbon dioxide, total [Moles/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=22.0,
        reference_high=29.0
    ),
    "2028-4": LOINCEntry(
        loinc_num="2028-4",
        component="Carbon dioxide, total [Moles/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=22.0,
        reference_high=29.0
    ),
    "2028-5": LOINCEntry(
        loinc_num="2028-5",
        component="Carbon dioxide, total [Moles/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=22.0,
        reference_high=29.0
    ),
    "2028-6": LOINCEntry(
        loinc_num="2028-6",
        component="Carbon dioxide, total [Moles/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=22.0,
        reference_high=29.0
    ),
    "3094-0": LOINCEntry(
        loinc_num="3094-0",
        component="Urea nitrogen [Mass/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=20.0
    ),
    "3094-1": LOINCEntry(
        loinc_num="3094-1",
        component="Urea nitrogen [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=20.0
    ),
    "3094-2": LOINCEntry(
        loinc_num="3094-2",
        component="Urea nitrogen [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=20.0
    ),
    "3094-3": LOINCEntry(
        loinc_num="3094-3",
        component="Urea nitrogen [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=20.0
    ),
    "3094-4": LOINCEntry(
        loinc_num="3094-4",
        component="Urea nitrogen [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=20.0
    ),
    "3094-5": LOINCEntry(
        loinc_num="3094-5",
        component="Urea nitrogen [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=20.0
    ),
    "3094-6": LOINCEntry(
        loinc_num="3094-6",
        component="Urea nitrogen [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=20.0
    ),
    "2160-0": LOINCEntry(
        loinc_num="2160-0",
        component="Creatinine [Mass/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.6,
        reference_high=1.3
    ),
    "2160-1": LOINCEntry(
        loinc_num="2160-1",
        component="Creatinine [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.6,
        reference_high=1.3
    ),
    "2160-2": LOINCEntry(
        loinc_num="2160-2",
        component="Creatinine [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.6,
        reference_high=1.3
    ),
    "2160-3": LOINCEntry(
        loinc_num="2160-3",
        component="Creatinine [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.6,
        reference_high=1.3
    ),
    "2160-4": LOINCEntry(
        loinc_num="2160-4",
        component="Creatinine [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.6,
        reference_high=1.3
    ),
    "2160-5": LOINCEntry(
        loinc_num="2160-5",
        component="Creatinine [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.6,
        reference_high=1.3
    ),
    "2160-6": LOINCEntry(
        loinc_num="2160-6",
        component="Creatinine [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.6,
        reference_high=1.3
    ),
    "2345-7": LOINCEntry(
        loinc_num="2345-7",
        component="Glucose [Mass/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=70.0,
        reference_high=99.0
    ),
    "2345-1": LOINCEntry(
        loinc_num="2345-1",
        component="Glucose [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=70.0,
        reference_high=99.0
    ),
    "2345-2": LOINCEntry(
        loinc_num="2345-2",
        component="Glucose [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=70.0,
        reference_high=99.0
    ),
    "2345-3": LOINCEntry(
        loinc_num="2345-3",
        component="Glucose [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=70.0,
        reference_high=99.0
    ),
    "2345-4": LOINCEntry(
        loinc_num="2345-4",
        component="Glucose [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=70.0,
        reference_high=99.0
    ),
    "2345-5": LOINCEntry(
        loinc_num="2345-5",
        component="Glucose [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=70.0,
        reference_high=99.0
    ),
    "2345-6": LOINCEntry(
        loinc_num="2345-6",
        component="Glucose [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=70.0,
        reference_high=99.0
    ),
    "17861-6": LOINCEntry(
        loinc_num="17861-6",
        component="Calcium [Mass/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=8.5,
        reference_high=10.5
    ),
    "17861-1": LOINCEntry(
        loinc_num="17861-1",
        component="Calcium [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=8.5,
        reference_high=10.5
    ),
    "17861-2": LOINCEntry(
        loinc_num="17861-2",
        component="Calcium [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=8.5,
        reference_high=10.5
    ),
    "17861-3": LOINCEntry(
        loinc_num="17861-3",
        component="Calcium [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=8.5,
        reference_high=10.5
    ),
    "17861-4": LOINCEntry(
        loinc_num="17861-4",
        component="Calcium [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=8.5,
        reference_high=10.5
    ),
    "17861-5": LOINCEntry(
        loinc_num="17861-5",
        component="Calcium [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=8.5,
        reference_high=10.5
    ),
    "17861-6": LOINCEntry(
        loinc_num="17861-6",
        component="Calcium [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=8.5,
        reference_high=10.5
    ),
    "1751-7": LOINCEntry(
        loinc_num="1751-7",
        component="Albumin [Mass/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.5
    ),
    "1751-1": LOINCEntry(
        loinc_num="1751-1",
        component="Albumin [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.5
    ),
    "1751-2": LOINCEntry(
        loinc_num="1751-2",
        component="Albumin [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.5
    ),
    "1751-3": LOINCEntry(
        loinc_num="1751-3",
        component="Albumin [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.5
    ),
    "1751-4": LOINCEntry(
        loinc_num="1751-4",
        component="Albumin [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.5
    ),
    "1751-5": LOINCEntry(
        loinc_num="1751-5",
        component="Albumin [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.5
    ),
    "1751-6": LOINCEntry(
        loinc_num="1751-6",
        component="Albumin [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=3.5,
        reference_high=5.5
    ),
    "2885-2": LOINCEntry(
        loinc_num="2885-2",
        component="Protein [Mass/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=6.0,
        reference_high=8.3
    ),
    "2885-1": LOINCEntry(
        loinc_num="2885-1",
        component="Protein [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=6.0,
        reference_high=8.3
    ),
    "2885-2": LOINCEntry(
        loinc_num="2885-2",
        component="Protein [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=6.0,
        reference_high=8.3
    ),
    "2885-3": LOINCEntry(
        loinc_num="2885-3",
        component="Protein [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=6.0,
        reference_high=8.3
    ),
    "2885-4": LOINCEntry(
        loinc_num="2885-4",
        component="Protein [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=6.0,
        reference_high=8.3
    ),
    "2885-5": LOINCEntry(
        loinc_num="2885-5",
        component="Protein [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=6.0,
        reference_high=8.3
    ),
    "2885-6": LOINCEntry(
        loinc_num="2885-6",
        component="Protein [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=6.0,
        reference_high=8.3
    ),
    "1975-2": LOINCEntry(
        loinc_num="1975-2",
        component="Bilirubin.total [Mass/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.2,
        reference_high=1.2
    ),
    "1975-1": LOINCEntry(
        loinc_num="1975-1",
        component="Bilirubin.total [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.2,
        reference_high=1.2
    ),
    "1975-2": LOINCEntry(
        loinc_num="1975-2",
        component="Bilirubin.total [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.2,
        reference_high=1.2
    ),
    "1975-3": LOINCEntry(
        loinc_num="1975-3",
        component="Bilirubin.total [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.2,
        reference_high=1.2
    ),
    "1975-4": LOINCEntry(
        loinc_num="1975-4",
        component="Bilirubin.total [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.2,
        reference_high=1.2
    ),
    "1975-5": LOINCEntry(
        loinc_num="1975-5",
        component="Bilirubin.total [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.2,
        reference_high=1.2
    ),
    "1975-6": LOINCEntry(
        loinc_num="1975-6",
        component="Bilirubin.total [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=0.2,
        reference_high=1.2
    ),
    "6768-6": LOINCEntry(
        loinc_num="6768-6",
        component="Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=44.0,
        reference_high=147.0
    ),
    "6768-1": LOINCEntry(
        loinc_num="6768-1",
        component="Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=44.0,
        reference_high=147.0
    ),
    "6768-2": LOINCEntry(
        loinc_num="6768-2",
        component="Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=44.0,
        reference_high=147.0
    ),
    "6768-3": LOINCEntry(
        loinc_num="6768-3",
        component="Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=44.0,
        reference_high=147.0
    ),
    "6768-4": LOINCEntry(
        loinc_num="6768-4",
        component="Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=44.0,
        reference_high=147.0
    ),
    "6768-5": LOINCEntry(
        loinc_num="6768-5",
        component="Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=44.0,
        reference_high=147.0
    ),
    "6768-6": LOINCEntry(
        loinc_num="6768-6",
        component="Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=44.0,
        reference_high=147.0
    ),
    "1742-6": LOINCEntry(
        loinc_num="1742-6",
        component="Alanine aminotransferase (ALT) [Enzymatic activity/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=56.0
    ),
    "1742-1": LOINCEntry(
        loinc_num="1742-1",
        component="Alanine aminotransferase (ALT) [Enzymatic activity/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=56.0
    ),
    "1742-2": LOINCEntry(
        loinc_num="1742-2",
        component="Alanine aminotransferase (ALT) [Enzymatic activity/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=56.0
    ),
    "1742-3": LOINCEntry(
        loinc_num="1742-3",
        component="Alanine aminotransferase (ALT) [Enzymatic activity/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=56.0
    ),
    "1742-4": LOINCEntry(
        loinc_num="1742-4",
        component="Alanine aminotransferase (ALT) [Enzymatic activity/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=56.0
    ),
    "1742-5": LOINCEntry(
        loinc_num="1742-5",
        component="Alanine aminotransferase (ALT) [Enzymatic activity/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=56.0
    ),
    "1742-6": LOINCEntry(
        loinc_num="1742-6",
        component="Alanine aminotransferase (ALT) [Enzymatic activity/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=7.0,
        reference_high=56.0
    ),
    "1920-8": LOINCEntry(
        loinc_num="1920-8",
        component="Aspartate aminotransferase (AST) [Enzymatic activity/volume] in Serum or Plasma",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=10.0,
        reference_high=40.0
    ),
    "1920-1": LOINCEntry(
        loinc_num="1920-1",
        component="Aspartate aminotransferase (AST) [Enzymatic activity/volume] in Serum or Plasma by Automated",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=10.0,
        reference_high=40.0
    ),
    "1920-2": LOINCEntry(
        loinc_num="1920-2",
        component="Aspartate aminotransferase (AST) [Enzymatic activity/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=10.0,
        reference_high=40.0
    ),
    "1920-3": LOINCEntry(
        loinc_num="1920-3",
        component="Aspartate aminotransferase (AST) [Enzymatic activity/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=10.0,
        reference_high=40.0
    ),
    "1920-4": LOINCEntry(
        loinc_num="1920-4",
        component="Aspartate aminotransferase (AST) [Enzymatic activity/volume] in Serum or Plasma by Immunoassay",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=10.0,
        reference_high=40.0
    ),
    "1920-5": LOINCEntry(
        loinc_num="1920-5",
        component="Aspartate aminotransferase (AST) [Enzymatic activity/volume] in Serum or Plasma by Point of care test",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=10.0,
        reference_high=40.0
    ),
    "1920-6": LOINCEntry(
        loinc_num="1920-6",
        component="Aspartate aminotransferase (AST) [Enzymatic activity/volume] in Serum or Plasma by High sensitivity",
        panel_category="Comprehensive Metabolic",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=10.0,
        reference_high=40.0
    ),
    "2093-3": LOINCEntry(
        loinc_num="2093-3",
        component="Cholesterol [Mass/volume] in Serum or Plasma",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=125.0,
        reference_high=200.0
    ),
    "2093-1": LOINCEntry(
        loinc_num="2093-1",
        component="Cholesterol [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=125.0,
        reference_high=200.0
    ),
    "2093-2": LOINCEntry(
        loinc_num="2093-2",
        component="Cholesterol [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=125.0,
        reference_high=200.0
    ),
    "2093-3": LOINCEntry(
        loinc_num="2093-3",
        component="Cholesterol [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=125.0,
        reference_high=200.0
    ),
    "2093-4": LOINCEntry(
        loinc_num="2093-4",
        component="Cholesterol [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=125.0,
        reference_high=200.0
    ),
    "2093-5": LOINCEntry(
        loinc_num="2093-5",
        component="Cholesterol [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=125.0,
        reference_high=200.0
    ),
    "2093-6": LOINCEntry(
        loinc_num="2093-6",
        component="Cholesterol [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=125.0,
        reference_high=200.0
    ),
    "2571-8": LOINCEntry(
        loinc_num="2571-8",
        component="Triglyceride [Mass/volume] in Serum or Plasma",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=150.0
    ),
    "2571-1": LOINCEntry(
        loinc_num="2571-1",
        component="Triglyceride [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=150.0
    ),
    "2571-2": LOINCEntry(
        loinc_num="2571-2",
        component="Triglyceride [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=150.0
    ),
    "2571-3": LOINCEntry(
        loinc_num="2571-3",
        component="Triglyceride [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=150.0
    ),
    "2571-4": LOINCEntry(
        loinc_num="2571-4",
        component="Triglyceride [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=150.0
    ),
    "2571-5": LOINCEntry(
        loinc_num="2571-5",
        component="Triglyceride [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=150.0
    ),
    "2571-6": LOINCEntry(
        loinc_num="2571-6",
        component="Triglyceride [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=150.0
    ),
    "2085-9": LOINCEntry(
        loinc_num="2085-9",
        component="Cholesterol in HDL [Mass/volume] in Serum or Plasma",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=40.0,
        reference_high=60.0
    ),
    "2085-1": LOINCEntry(
        loinc_num="2085-1",
        component="Cholesterol in HDL [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=40.0,
        reference_high=60.0
    ),
    "2085-2": LOINCEntry(
        loinc_num="2085-2",
        component="Cholesterol in HDL [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=40.0,
        reference_high=60.0
    ),
    "2085-3": LOINCEntry(
        loinc_num="2085-3",
        component="Cholesterol in HDL [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=40.0,
        reference_high=60.0
    ),
    "2085-4": LOINCEntry(
        loinc_num="2085-4",
        component="Cholesterol in HDL [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=40.0,
        reference_high=60.0
    ),
    "2085-5": LOINCEntry(
        loinc_num="2085-5",
        component="Cholesterol in HDL [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=40.0,
        reference_high=60.0
    ),
    "2085-6": LOINCEntry(
        loinc_num="2085-6",
        component="Cholesterol in HDL [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=40.0,
        reference_high=60.0
    ),
    "13457-7": LOINCEntry(
        loinc_num="13457-7",
        component="Cholesterol in LDL [Mass/volume] in Serum or Plasma",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=100.0
    ),
    "13457-1": LOINCEntry(
        loinc_num="13457-1",
        component="Cholesterol in LDL [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=100.0
    ),
    "13457-2": LOINCEntry(
        loinc_num="13457-2",
        component="Cholesterol in LDL [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=100.0
    ),
    "13457-3": LOINCEntry(
        loinc_num="13457-3",
        component="Cholesterol in LDL [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=100.0
    ),
    "13457-4": LOINCEntry(
        loinc_num="13457-4",
        component="Cholesterol in LDL [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=100.0
    ),
    "13457-5": LOINCEntry(
        loinc_num="13457-5",
        component="Cholesterol in LDL [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=100.0
    ),
    "13457-6": LOINCEntry(
        loinc_num="13457-6",
        component="Cholesterol in LDL [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=50.0,
        reference_high=100.0
    ),
    "2089-1": LOINCEntry(
        loinc_num="2089-1",
        component="Cholesterol in VLDL [Mass/volume] in Serum or Plasma",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=5.0,
        reference_high=30.0
    ),
    "2089-1": LOINCEntry(
        loinc_num="2089-1",
        component="Cholesterol in VLDL [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=5.0,
        reference_high=30.0
    ),
    "2089-2": LOINCEntry(
        loinc_num="2089-2",
        component="Cholesterol in VLDL [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=5.0,
        reference_high=30.0
    ),
    "2089-3": LOINCEntry(
        loinc_num="2089-3",
        component="Cholesterol in VLDL [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=5.0,
        reference_high=30.0
    ),
    "2089-4": LOINCEntry(
        loinc_num="2089-4",
        component="Cholesterol in VLDL [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=5.0,
        reference_high=30.0
    ),
    "2089-5": LOINCEntry(
        loinc_num="2089-5",
        component="Cholesterol in VLDL [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=5.0,
        reference_high=30.0
    ),
    "2089-6": LOINCEntry(
        loinc_num="2089-6",
        component="Cholesterol in VLDL [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Lipid Panel",
        system_specimen="Serum/Plasma",
        default_unit="mg/dL",
        reference_low=5.0,
        reference_high=30.0
    ),
    "5902-2": LOINCEntry(
        loinc_num="5902-2",
        component="Prothrombin time (PT)",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=11.0,
        reference_high=13.5
    ),
    "5902-1": LOINCEntry(
        loinc_num="5902-1",
        component="Prothrombin time (PT) by Automated",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=11.0,
        reference_high=13.5
    ),
    "5902-2": LOINCEntry(
        loinc_num="5902-2",
        component="Prothrombin time (PT) by Manual microscopic",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=11.0,
        reference_high=13.5
    ),
    "5902-3": LOINCEntry(
        loinc_num="5902-3",
        component="Prothrombin time (PT) by Spectrophotometry",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=11.0,
        reference_high=13.5
    ),
    "5902-4": LOINCEntry(
        loinc_num="5902-4",
        component="Prothrombin time (PT) by Immunoassay",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=11.0,
        reference_high=13.5
    ),
    "5902-5": LOINCEntry(
        loinc_num="5902-5",
        component="Prothrombin time (PT) by Point of care test",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=11.0,
        reference_high=13.5
    ),
    "5902-6": LOINCEntry(
        loinc_num="5902-6",
        component="Prothrombin time (PT) by High sensitivity",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=11.0,
        reference_high=13.5
    ),
    "6301-6": LOINCEntry(
        loinc_num="6301-6",
        component="INR in Platelet poor plasma by Coagulation assay",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.8,
        reference_high=1.2
    ),
    "6301-1": LOINCEntry(
        loinc_num="6301-1",
        component="INR in Platelet poor plasma by Coagulation assay by Automated",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.8,
        reference_high=1.2
    ),
    "6301-2": LOINCEntry(
        loinc_num="6301-2",
        component="INR in Platelet poor plasma by Coagulation assay by Manual microscopic",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.8,
        reference_high=1.2
    ),
    "6301-3": LOINCEntry(
        loinc_num="6301-3",
        component="INR in Platelet poor plasma by Coagulation assay by Spectrophotometry",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.8,
        reference_high=1.2
    ),
    "6301-4": LOINCEntry(
        loinc_num="6301-4",
        component="INR in Platelet poor plasma by Coagulation assay by Immunoassay",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.8,
        reference_high=1.2
    ),
    "6301-5": LOINCEntry(
        loinc_num="6301-5",
        component="INR in Platelet poor plasma by Coagulation assay by Point of care test",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.8,
        reference_high=1.2
    ),
    "6301-6": LOINCEntry(
        loinc_num="6301-6",
        component="INR in Platelet poor plasma by Coagulation assay by High sensitivity",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.8,
        reference_high=1.2
    ),
    "3173-2": LOINCEntry(
        loinc_num="3173-2",
        component="aPTT in Platelet poor plasma by Coagulation assay",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=25.0,
        reference_high=35.0
    ),
    "3173-1": LOINCEntry(
        loinc_num="3173-1",
        component="aPTT in Platelet poor plasma by Coagulation assay by Automated",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=25.0,
        reference_high=35.0
    ),
    "3173-2": LOINCEntry(
        loinc_num="3173-2",
        component="aPTT in Platelet poor plasma by Coagulation assay by Manual microscopic",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=25.0,
        reference_high=35.0
    ),
    "3173-3": LOINCEntry(
        loinc_num="3173-3",
        component="aPTT in Platelet poor plasma by Coagulation assay by Spectrophotometry",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=25.0,
        reference_high=35.0
    ),
    "3173-4": LOINCEntry(
        loinc_num="3173-4",
        component="aPTT in Platelet poor plasma by Coagulation assay by Immunoassay",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=25.0,
        reference_high=35.0
    ),
    "3173-5": LOINCEntry(
        loinc_num="3173-5",
        component="aPTT in Platelet poor plasma by Coagulation assay by Point of care test",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=25.0,
        reference_high=35.0
    ),
    "3173-6": LOINCEntry(
        loinc_num="3173-6",
        component="aPTT in Platelet poor plasma by Coagulation assay by High sensitivity",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=25.0,
        reference_high=35.0
    ),
    "48065-7": LOINCEntry(
        loinc_num="48065-7",
        component="Fibrin D-dimer FEU [Mass/volume] in Platelet poor plasma",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.0,
        reference_high=0.5
    ),
    "48065-1": LOINCEntry(
        loinc_num="48065-1",
        component="Fibrin D-dimer FEU [Mass/volume] in Platelet poor plasma by Automated",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.0,
        reference_high=0.5
    ),
    "48065-2": LOINCEntry(
        loinc_num="48065-2",
        component="Fibrin D-dimer FEU [Mass/volume] in Platelet poor plasma by Manual microscopic",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.0,
        reference_high=0.5
    ),
    "48065-3": LOINCEntry(
        loinc_num="48065-3",
        component="Fibrin D-dimer FEU [Mass/volume] in Platelet poor plasma by Spectrophotometry",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.0,
        reference_high=0.5
    ),
    "48065-4": LOINCEntry(
        loinc_num="48065-4",
        component="Fibrin D-dimer FEU [Mass/volume] in Platelet poor plasma by Immunoassay",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.0,
        reference_high=0.5
    ),
    "48065-5": LOINCEntry(
        loinc_num="48065-5",
        component="Fibrin D-dimer FEU [Mass/volume] in Platelet poor plasma by Point of care test",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.0,
        reference_high=0.5
    ),
    "48065-6": LOINCEntry(
        loinc_num="48065-6",
        component="Fibrin D-dimer FEU [Mass/volume] in Platelet poor plasma by High sensitivity",
        panel_category="Coagulation",
        system_specimen="Platelet poor plasma",
        default_unit="seconds",
        reference_low=0.0,
        reference_high=0.5
    ),
    "2744-1": LOINCEntry(
        loinc_num="2744-1",
        component="pH of Arterial blood",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=7.35,
        reference_high=7.45
    ),
    "2744-1": LOINCEntry(
        loinc_num="2744-1",
        component="pH of Arterial blood by Automated",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=7.35,
        reference_high=7.45
    ),
    "2744-2": LOINCEntry(
        loinc_num="2744-2",
        component="pH of Arterial blood by Manual microscopic",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=7.35,
        reference_high=7.45
    ),
    "2744-3": LOINCEntry(
        loinc_num="2744-3",
        component="pH of Arterial blood by Spectrophotometry",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=7.35,
        reference_high=7.45
    ),
    "2744-4": LOINCEntry(
        loinc_num="2744-4",
        component="pH of Arterial blood by Immunoassay",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=7.35,
        reference_high=7.45
    ),
    "2744-5": LOINCEntry(
        loinc_num="2744-5",
        component="pH of Arterial blood by Point of care test",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=7.35,
        reference_high=7.45
    ),
    "2744-6": LOINCEntry(
        loinc_num="2744-6",
        component="pH of Arterial blood by High sensitivity",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=7.35,
        reference_high=7.45
    ),
    "2019-8": LOINCEntry(
        loinc_num="2019-8",
        component="Carbon dioxide [Partial pressure] in Arterial blood",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=35.0,
        reference_high=45.0
    ),
    "2019-1": LOINCEntry(
        loinc_num="2019-1",
        component="Carbon dioxide [Partial pressure] in Arterial blood by Automated",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=35.0,
        reference_high=45.0
    ),
    "2019-2": LOINCEntry(
        loinc_num="2019-2",
        component="Carbon dioxide [Partial pressure] in Arterial blood by Manual microscopic",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=35.0,
        reference_high=45.0
    ),
    "2019-3": LOINCEntry(
        loinc_num="2019-3",
        component="Carbon dioxide [Partial pressure] in Arterial blood by Spectrophotometry",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=35.0,
        reference_high=45.0
    ),
    "2019-4": LOINCEntry(
        loinc_num="2019-4",
        component="Carbon dioxide [Partial pressure] in Arterial blood by Immunoassay",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=35.0,
        reference_high=45.0
    ),
    "2019-5": LOINCEntry(
        loinc_num="2019-5",
        component="Carbon dioxide [Partial pressure] in Arterial blood by Point of care test",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=35.0,
        reference_high=45.0
    ),
    "2019-6": LOINCEntry(
        loinc_num="2019-6",
        component="Carbon dioxide [Partial pressure] in Arterial blood by High sensitivity",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=35.0,
        reference_high=45.0
    ),
    "2703-7": LOINCEntry(
        loinc_num="2703-7",
        component="Oxygen [Partial pressure] in Arterial blood",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=75.0,
        reference_high=100.0
    ),
    "2703-1": LOINCEntry(
        loinc_num="2703-1",
        component="Oxygen [Partial pressure] in Arterial blood by Automated",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=75.0,
        reference_high=100.0
    ),
    "2703-2": LOINCEntry(
        loinc_num="2703-2",
        component="Oxygen [Partial pressure] in Arterial blood by Manual microscopic",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=75.0,
        reference_high=100.0
    ),
    "2703-3": LOINCEntry(
        loinc_num="2703-3",
        component="Oxygen [Partial pressure] in Arterial blood by Spectrophotometry",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=75.0,
        reference_high=100.0
    ),
    "2703-4": LOINCEntry(
        loinc_num="2703-4",
        component="Oxygen [Partial pressure] in Arterial blood by Immunoassay",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=75.0,
        reference_high=100.0
    ),
    "2703-5": LOINCEntry(
        loinc_num="2703-5",
        component="Oxygen [Partial pressure] in Arterial blood by Point of care test",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=75.0,
        reference_high=100.0
    ),
    "2703-6": LOINCEntry(
        loinc_num="2703-6",
        component="Oxygen [Partial pressure] in Arterial blood by High sensitivity",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=75.0,
        reference_high=100.0
    ),
    "1960-4": LOINCEntry(
        loinc_num="1960-4",
        component="Bicarbonate [Moles/volume] in Arterial blood",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=22.0,
        reference_high=26.0
    ),
    "1960-1": LOINCEntry(
        loinc_num="1960-1",
        component="Bicarbonate [Moles/volume] in Arterial blood by Automated",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=22.0,
        reference_high=26.0
    ),
    "1960-2": LOINCEntry(
        loinc_num="1960-2",
        component="Bicarbonate [Moles/volume] in Arterial blood by Manual microscopic",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=22.0,
        reference_high=26.0
    ),
    "1960-3": LOINCEntry(
        loinc_num="1960-3",
        component="Bicarbonate [Moles/volume] in Arterial blood by Spectrophotometry",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=22.0,
        reference_high=26.0
    ),
    "1960-4": LOINCEntry(
        loinc_num="1960-4",
        component="Bicarbonate [Moles/volume] in Arterial blood by Immunoassay",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=22.0,
        reference_high=26.0
    ),
    "1960-5": LOINCEntry(
        loinc_num="1960-5",
        component="Bicarbonate [Moles/volume] in Arterial blood by Point of care test",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=22.0,
        reference_high=26.0
    ),
    "1960-6": LOINCEntry(
        loinc_num="1960-6",
        component="Bicarbonate [Moles/volume] in Arterial blood by High sensitivity",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=22.0,
        reference_high=26.0
    ),
    "2708-6": LOINCEntry(
        loinc_num="2708-6",
        component="Oxygen saturation in Arterial blood",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708-1": LOINCEntry(
        loinc_num="2708-1",
        component="Oxygen saturation in Arterial blood by Automated",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708-2": LOINCEntry(
        loinc_num="2708-2",
        component="Oxygen saturation in Arterial blood by Manual microscopic",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708-3": LOINCEntry(
        loinc_num="2708-3",
        component="Oxygen saturation in Arterial blood by Spectrophotometry",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708-4": LOINCEntry(
        loinc_num="2708-4",
        component="Oxygen saturation in Arterial blood by Immunoassay",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708-5": LOINCEntry(
        loinc_num="2708-5",
        component="Oxygen saturation in Arterial blood by Point of care test",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708-6": LOINCEntry(
        loinc_num="2708-6",
        component="Oxygen saturation in Arterial blood by High sensitivity",
        panel_category="Arterial Blood Gases",
        system_specimen="Arterial blood",
        default_unit="mmHg",
        reference_low=95.0,
        reference_high=100.0
    ),
    "4548-4": LOINCEntry(
        loinc_num="4548-4",
        component="Hemoglobin A1c/Hemoglobin.total in Blood",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=4.0,
        reference_high=5.6
    ),
    "4548-1": LOINCEntry(
        loinc_num="4548-1",
        component="Hemoglobin A1c/Hemoglobin.total in Blood by Automated",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=4.0,
        reference_high=5.6
    ),
    "4548-2": LOINCEntry(
        loinc_num="4548-2",
        component="Hemoglobin A1c/Hemoglobin.total in Blood by Manual microscopic",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=4.0,
        reference_high=5.6
    ),
    "4548-3": LOINCEntry(
        loinc_num="4548-3",
        component="Hemoglobin A1c/Hemoglobin.total in Blood by Spectrophotometry",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=4.0,
        reference_high=5.6
    ),
    "4548-4": LOINCEntry(
        loinc_num="4548-4",
        component="Hemoglobin A1c/Hemoglobin.total in Blood by Immunoassay",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=4.0,
        reference_high=5.6
    ),
    "4548-5": LOINCEntry(
        loinc_num="4548-5",
        component="Hemoglobin A1c/Hemoglobin.total in Blood by Point of care test",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=4.0,
        reference_high=5.6
    ),
    "4548-6": LOINCEntry(
        loinc_num="4548-6",
        component="Hemoglobin A1c/Hemoglobin.total in Blood by High sensitivity",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=4.0,
        reference_high=5.6
    ),
    "3016-3": LOINCEntry(
        loinc_num="3016-3",
        component="Thyrotropin (TSH) [Units/volume] in Serum or Plasma",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.4,
        reference_high=4.0
    ),
    "3016-1": LOINCEntry(
        loinc_num="3016-1",
        component="Thyrotropin (TSH) [Units/volume] in Serum or Plasma by Automated",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.4,
        reference_high=4.0
    ),
    "3016-2": LOINCEntry(
        loinc_num="3016-2",
        component="Thyrotropin (TSH) [Units/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.4,
        reference_high=4.0
    ),
    "3016-3": LOINCEntry(
        loinc_num="3016-3",
        component="Thyrotropin (TSH) [Units/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.4,
        reference_high=4.0
    ),
    "3016-4": LOINCEntry(
        loinc_num="3016-4",
        component="Thyrotropin (TSH) [Units/volume] in Serum or Plasma by Immunoassay",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.4,
        reference_high=4.0
    ),
    "3016-5": LOINCEntry(
        loinc_num="3016-5",
        component="Thyrotropin (TSH) [Units/volume] in Serum or Plasma by Point of care test",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.4,
        reference_high=4.0
    ),
    "3016-6": LOINCEntry(
        loinc_num="3016-6",
        component="Thyrotropin (TSH) [Units/volume] in Serum or Plasma by High sensitivity",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.4,
        reference_high=4.0
    ),
    "3024-7": LOINCEntry(
        loinc_num="3024-7",
        component="Thyroxine (T4) free [Mass/volume] in Serum or Plasma",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.8,
        reference_high=1.8
    ),
    "3024-1": LOINCEntry(
        loinc_num="3024-1",
        component="Thyroxine (T4) free [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.8,
        reference_high=1.8
    ),
    "3024-2": LOINCEntry(
        loinc_num="3024-2",
        component="Thyroxine (T4) free [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.8,
        reference_high=1.8
    ),
    "3024-3": LOINCEntry(
        loinc_num="3024-3",
        component="Thyroxine (T4) free [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.8,
        reference_high=1.8
    ),
    "3024-4": LOINCEntry(
        loinc_num="3024-4",
        component="Thyroxine (T4) free [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.8,
        reference_high=1.8
    ),
    "3024-5": LOINCEntry(
        loinc_num="3024-5",
        component="Thyroxine (T4) free [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.8,
        reference_high=1.8
    ),
    "3024-6": LOINCEntry(
        loinc_num="3024-6",
        component="Thyroxine (T4) free [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=0.8,
        reference_high=1.8
    ),
    "2143-6": LOINCEntry(
        loinc_num="2143-6",
        component="Cortisol [Mass/volume] in Serum or Plasma",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=5.0,
        reference_high=25.0
    ),
    "2143-1": LOINCEntry(
        loinc_num="2143-1",
        component="Cortisol [Mass/volume] in Serum or Plasma by Automated",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=5.0,
        reference_high=25.0
    ),
    "2143-2": LOINCEntry(
        loinc_num="2143-2",
        component="Cortisol [Mass/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=5.0,
        reference_high=25.0
    ),
    "2143-3": LOINCEntry(
        loinc_num="2143-3",
        component="Cortisol [Mass/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=5.0,
        reference_high=25.0
    ),
    "2143-4": LOINCEntry(
        loinc_num="2143-4",
        component="Cortisol [Mass/volume] in Serum or Plasma by Immunoassay",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=5.0,
        reference_high=25.0
    ),
    "2143-5": LOINCEntry(
        loinc_num="2143-5",
        component="Cortisol [Mass/volume] in Serum or Plasma by Point of care test",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=5.0,
        reference_high=25.0
    ),
    "2143-6": LOINCEntry(
        loinc_num="2143-6",
        component="Cortisol [Mass/volume] in Serum or Plasma by High sensitivity",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=5.0,
        reference_high=25.0
    ),
    "2484-4": LOINCEntry(
        loinc_num="2484-4",
        component="Insulin [Units/volume] in Serum or Plasma",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=2.6,
        reference_high=24.9
    ),
    "2484-1": LOINCEntry(
        loinc_num="2484-1",
        component="Insulin [Units/volume] in Serum or Plasma by Automated",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=2.6,
        reference_high=24.9
    ),
    "2484-2": LOINCEntry(
        loinc_num="2484-2",
        component="Insulin [Units/volume] in Serum or Plasma by Manual microscopic",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=2.6,
        reference_high=24.9
    ),
    "2484-3": LOINCEntry(
        loinc_num="2484-3",
        component="Insulin [Units/volume] in Serum or Plasma by Spectrophotometry",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=2.6,
        reference_high=24.9
    ),
    "2484-4": LOINCEntry(
        loinc_num="2484-4",
        component="Insulin [Units/volume] in Serum or Plasma by Immunoassay",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=2.6,
        reference_high=24.9
    ),
    "2484-5": LOINCEntry(
        loinc_num="2484-5",
        component="Insulin [Units/volume] in Serum or Plasma by Point of care test",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=2.6,
        reference_high=24.9
    ),
    "2484-6": LOINCEntry(
        loinc_num="2484-6",
        component="Insulin [Units/volume] in Serum or Plasma by High sensitivity",
        panel_category="Endocrine and Diabetes",
        system_specimen="Blood",
        default_unit="%",
        reference_low=2.6,
        reference_high=24.9
    ),
    "2756-5": LOINCEntry(
        loinc_num="2756-5",
        component="pH of Urine by Test strip",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=4.5,
        reference_high=8.0
    ),
    "2756-1": LOINCEntry(
        loinc_num="2756-1",
        component="pH of Urine by Test strip by Automated",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=4.5,
        reference_high=8.0
    ),
    "2756-2": LOINCEntry(
        loinc_num="2756-2",
        component="pH of Urine by Test strip by Manual microscopic",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=4.5,
        reference_high=8.0
    ),
    "2756-3": LOINCEntry(
        loinc_num="2756-3",
        component="pH of Urine by Test strip by Spectrophotometry",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=4.5,
        reference_high=8.0
    ),
    "2756-4": LOINCEntry(
        loinc_num="2756-4",
        component="pH of Urine by Test strip by Immunoassay",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=4.5,
        reference_high=8.0
    ),
    "2756-5": LOINCEntry(
        loinc_num="2756-5",
        component="pH of Urine by Test strip by Point of care test",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=4.5,
        reference_high=8.0
    ),
    "2756-6": LOINCEntry(
        loinc_num="2756-6",
        component="pH of Urine by Test strip by High sensitivity",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=4.5,
        reference_high=8.0
    ),
    "5811-5": LOINCEntry(
        loinc_num="5811-5",
        component="Specific gravity of Urine by Test strip",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=1.005,
        reference_high=1.03
    ),
    "5811-1": LOINCEntry(
        loinc_num="5811-1",
        component="Specific gravity of Urine by Test strip by Automated",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=1.005,
        reference_high=1.03
    ),
    "5811-2": LOINCEntry(
        loinc_num="5811-2",
        component="Specific gravity of Urine by Test strip by Manual microscopic",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=1.005,
        reference_high=1.03
    ),
    "5811-3": LOINCEntry(
        loinc_num="5811-3",
        component="Specific gravity of Urine by Test strip by Spectrophotometry",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=1.005,
        reference_high=1.03
    ),
    "5811-4": LOINCEntry(
        loinc_num="5811-4",
        component="Specific gravity of Urine by Test strip by Immunoassay",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=1.005,
        reference_high=1.03
    ),
    "5811-5": LOINCEntry(
        loinc_num="5811-5",
        component="Specific gravity of Urine by Test strip by Point of care test",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=1.005,
        reference_high=1.03
    ),
    "5811-6": LOINCEntry(
        loinc_num="5811-6",
        component="Specific gravity of Urine by Test strip by High sensitivity",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=1.005,
        reference_high=1.03
    ),
    "2888-6": LOINCEntry(
        loinc_num="2888-6",
        component="Protein [Presence] in Urine by Test strip",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "2888-1": LOINCEntry(
        loinc_num="2888-1",
        component="Protein [Presence] in Urine by Test strip by Automated",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "2888-2": LOINCEntry(
        loinc_num="2888-2",
        component="Protein [Presence] in Urine by Test strip by Manual microscopic",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "2888-3": LOINCEntry(
        loinc_num="2888-3",
        component="Protein [Presence] in Urine by Test strip by Spectrophotometry",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "2888-4": LOINCEntry(
        loinc_num="2888-4",
        component="Protein [Presence] in Urine by Test strip by Immunoassay",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "2888-5": LOINCEntry(
        loinc_num="2888-5",
        component="Protein [Presence] in Urine by Test strip by Point of care test",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "2888-6": LOINCEntry(
        loinc_num="2888-6",
        component="Protein [Presence] in Urine by Test strip by High sensitivity",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "25428-4": LOINCEntry(
        loinc_num="25428-4",
        component="Glucose [Presence] in Urine by Test strip",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "25428-1": LOINCEntry(
        loinc_num="25428-1",
        component="Glucose [Presence] in Urine by Test strip by Automated",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "25428-2": LOINCEntry(
        loinc_num="25428-2",
        component="Glucose [Presence] in Urine by Test strip by Manual microscopic",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "25428-3": LOINCEntry(
        loinc_num="25428-3",
        component="Glucose [Presence] in Urine by Test strip by Spectrophotometry",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "25428-4": LOINCEntry(
        loinc_num="25428-4",
        component="Glucose [Presence] in Urine by Test strip by Immunoassay",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "25428-5": LOINCEntry(
        loinc_num="25428-5",
        component="Glucose [Presence] in Urine by Test strip by Point of care test",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "25428-6": LOINCEntry(
        loinc_num="25428-6",
        component="Glucose [Presence] in Urine by Test strip by High sensitivity",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "5794-3": LOINCEntry(
        loinc_num="5794-3",
        component="Leukocyte esterase in Urine by Test strip",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "5794-1": LOINCEntry(
        loinc_num="5794-1",
        component="Leukocyte esterase in Urine by Test strip by Automated",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "5794-2": LOINCEntry(
        loinc_num="5794-2",
        component="Leukocyte esterase in Urine by Test strip by Manual microscopic",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "5794-3": LOINCEntry(
        loinc_num="5794-3",
        component="Leukocyte esterase in Urine by Test strip by Spectrophotometry",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "5794-4": LOINCEntry(
        loinc_num="5794-4",
        component="Leukocyte esterase in Urine by Test strip by Immunoassay",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "5794-5": LOINCEntry(
        loinc_num="5794-5",
        component="Leukocyte esterase in Urine by Test strip by Point of care test",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "5794-6": LOINCEntry(
        loinc_num="5794-6",
        component="Leukocyte esterase in Urine by Test strip by High sensitivity",
        panel_category="Urinalysis",
        system_specimen="Urine",
        default_unit="units",
        reference_low=0.0,
        reference_high=0.0
    ),
    "8867-4": LOINCEntry(
        loinc_num="8867-4",
        component="Heart rate",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_1-0": LOINCEntry(
        loinc_num="8867_1-0",
        component="Heart rate measurement protocol 1",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_2-0": LOINCEntry(
        loinc_num="8867_2-0",
        component="Heart rate measurement protocol 2",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_3-0": LOINCEntry(
        loinc_num="8867_3-0",
        component="Heart rate measurement protocol 3",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_4-0": LOINCEntry(
        loinc_num="8867_4-0",
        component="Heart rate measurement protocol 4",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_5-0": LOINCEntry(
        loinc_num="8867_5-0",
        component="Heart rate measurement protocol 5",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_6-0": LOINCEntry(
        loinc_num="8867_6-0",
        component="Heart rate measurement protocol 6",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_7-0": LOINCEntry(
        loinc_num="8867_7-0",
        component="Heart rate measurement protocol 7",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_8-0": LOINCEntry(
        loinc_num="8867_8-0",
        component="Heart rate measurement protocol 8",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_9-0": LOINCEntry(
        loinc_num="8867_9-0",
        component="Heart rate measurement protocol 9",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_10-0": LOINCEntry(
        loinc_num="8867_10-0",
        component="Heart rate measurement protocol 10",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_11-0": LOINCEntry(
        loinc_num="8867_11-0",
        component="Heart rate measurement protocol 11",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_12-0": LOINCEntry(
        loinc_num="8867_12-0",
        component="Heart rate measurement protocol 12",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_13-0": LOINCEntry(
        loinc_num="8867_13-0",
        component="Heart rate measurement protocol 13",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_14-0": LOINCEntry(
        loinc_num="8867_14-0",
        component="Heart rate measurement protocol 14",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_15-0": LOINCEntry(
        loinc_num="8867_15-0",
        component="Heart rate measurement protocol 15",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_16-0": LOINCEntry(
        loinc_num="8867_16-0",
        component="Heart rate measurement protocol 16",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_17-0": LOINCEntry(
        loinc_num="8867_17-0",
        component="Heart rate measurement protocol 17",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_18-0": LOINCEntry(
        loinc_num="8867_18-0",
        component="Heart rate measurement protocol 18",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8867_19-0": LOINCEntry(
        loinc_num="8867_19-0",
        component="Heart rate measurement protocol 19",
        panel_category="Vital Signs",
        system_specimen="Artery",
        default_unit="beats/min",
        reference_low=60.0,
        reference_high=100.0
    ),
    "8480-6": LOINCEntry(
        loinc_num="8480-6",
        component="Systolic blood pressure",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_1-0": LOINCEntry(
        loinc_num="8480_1-0",
        component="Systolic blood pressure measurement protocol 1",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_2-0": LOINCEntry(
        loinc_num="8480_2-0",
        component="Systolic blood pressure measurement protocol 2",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_3-0": LOINCEntry(
        loinc_num="8480_3-0",
        component="Systolic blood pressure measurement protocol 3",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_4-0": LOINCEntry(
        loinc_num="8480_4-0",
        component="Systolic blood pressure measurement protocol 4",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_5-0": LOINCEntry(
        loinc_num="8480_5-0",
        component="Systolic blood pressure measurement protocol 5",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_6-0": LOINCEntry(
        loinc_num="8480_6-0",
        component="Systolic blood pressure measurement protocol 6",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_7-0": LOINCEntry(
        loinc_num="8480_7-0",
        component="Systolic blood pressure measurement protocol 7",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_8-0": LOINCEntry(
        loinc_num="8480_8-0",
        component="Systolic blood pressure measurement protocol 8",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_9-0": LOINCEntry(
        loinc_num="8480_9-0",
        component="Systolic blood pressure measurement protocol 9",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_10-0": LOINCEntry(
        loinc_num="8480_10-0",
        component="Systolic blood pressure measurement protocol 10",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_11-0": LOINCEntry(
        loinc_num="8480_11-0",
        component="Systolic blood pressure measurement protocol 11",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_12-0": LOINCEntry(
        loinc_num="8480_12-0",
        component="Systolic blood pressure measurement protocol 12",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_13-0": LOINCEntry(
        loinc_num="8480_13-0",
        component="Systolic blood pressure measurement protocol 13",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_14-0": LOINCEntry(
        loinc_num="8480_14-0",
        component="Systolic blood pressure measurement protocol 14",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_15-0": LOINCEntry(
        loinc_num="8480_15-0",
        component="Systolic blood pressure measurement protocol 15",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_16-0": LOINCEntry(
        loinc_num="8480_16-0",
        component="Systolic blood pressure measurement protocol 16",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_17-0": LOINCEntry(
        loinc_num="8480_17-0",
        component="Systolic blood pressure measurement protocol 17",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_18-0": LOINCEntry(
        loinc_num="8480_18-0",
        component="Systolic blood pressure measurement protocol 18",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8480_19-0": LOINCEntry(
        loinc_num="8480_19-0",
        component="Systolic blood pressure measurement protocol 19",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=90.0,
        reference_high=120.0
    ),
    "8462-4": LOINCEntry(
        loinc_num="8462-4",
        component="Diastolic blood pressure",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_1-0": LOINCEntry(
        loinc_num="8462_1-0",
        component="Diastolic blood pressure measurement protocol 1",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_2-0": LOINCEntry(
        loinc_num="8462_2-0",
        component="Diastolic blood pressure measurement protocol 2",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_3-0": LOINCEntry(
        loinc_num="8462_3-0",
        component="Diastolic blood pressure measurement protocol 3",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_4-0": LOINCEntry(
        loinc_num="8462_4-0",
        component="Diastolic blood pressure measurement protocol 4",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_5-0": LOINCEntry(
        loinc_num="8462_5-0",
        component="Diastolic blood pressure measurement protocol 5",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_6-0": LOINCEntry(
        loinc_num="8462_6-0",
        component="Diastolic blood pressure measurement protocol 6",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_7-0": LOINCEntry(
        loinc_num="8462_7-0",
        component="Diastolic blood pressure measurement protocol 7",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_8-0": LOINCEntry(
        loinc_num="8462_8-0",
        component="Diastolic blood pressure measurement protocol 8",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_9-0": LOINCEntry(
        loinc_num="8462_9-0",
        component="Diastolic blood pressure measurement protocol 9",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_10-0": LOINCEntry(
        loinc_num="8462_10-0",
        component="Diastolic blood pressure measurement protocol 10",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_11-0": LOINCEntry(
        loinc_num="8462_11-0",
        component="Diastolic blood pressure measurement protocol 11",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_12-0": LOINCEntry(
        loinc_num="8462_12-0",
        component="Diastolic blood pressure measurement protocol 12",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_13-0": LOINCEntry(
        loinc_num="8462_13-0",
        component="Diastolic blood pressure measurement protocol 13",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_14-0": LOINCEntry(
        loinc_num="8462_14-0",
        component="Diastolic blood pressure measurement protocol 14",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_15-0": LOINCEntry(
        loinc_num="8462_15-0",
        component="Diastolic blood pressure measurement protocol 15",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_16-0": LOINCEntry(
        loinc_num="8462_16-0",
        component="Diastolic blood pressure measurement protocol 16",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_17-0": LOINCEntry(
        loinc_num="8462_17-0",
        component="Diastolic blood pressure measurement protocol 17",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_18-0": LOINCEntry(
        loinc_num="8462_18-0",
        component="Diastolic blood pressure measurement protocol 18",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "8462_19-0": LOINCEntry(
        loinc_num="8462_19-0",
        component="Diastolic blood pressure measurement protocol 19",
        panel_category="Vital Signs",
        system_specimen="Arterial system",
        default_unit="mm[Hg]",
        reference_low=60.0,
        reference_high=80.0
    ),
    "9279-1": LOINCEntry(
        loinc_num="9279-1",
        component="Respiratory rate",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_1-0": LOINCEntry(
        loinc_num="9279_1-0",
        component="Respiratory rate measurement protocol 1",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_2-0": LOINCEntry(
        loinc_num="9279_2-0",
        component="Respiratory rate measurement protocol 2",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_3-0": LOINCEntry(
        loinc_num="9279_3-0",
        component="Respiratory rate measurement protocol 3",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_4-0": LOINCEntry(
        loinc_num="9279_4-0",
        component="Respiratory rate measurement protocol 4",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_5-0": LOINCEntry(
        loinc_num="9279_5-0",
        component="Respiratory rate measurement protocol 5",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_6-0": LOINCEntry(
        loinc_num="9279_6-0",
        component="Respiratory rate measurement protocol 6",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_7-0": LOINCEntry(
        loinc_num="9279_7-0",
        component="Respiratory rate measurement protocol 7",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_8-0": LOINCEntry(
        loinc_num="9279_8-0",
        component="Respiratory rate measurement protocol 8",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_9-0": LOINCEntry(
        loinc_num="9279_9-0",
        component="Respiratory rate measurement protocol 9",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_10-0": LOINCEntry(
        loinc_num="9279_10-0",
        component="Respiratory rate measurement protocol 10",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_11-0": LOINCEntry(
        loinc_num="9279_11-0",
        component="Respiratory rate measurement protocol 11",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_12-0": LOINCEntry(
        loinc_num="9279_12-0",
        component="Respiratory rate measurement protocol 12",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_13-0": LOINCEntry(
        loinc_num="9279_13-0",
        component="Respiratory rate measurement protocol 13",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_14-0": LOINCEntry(
        loinc_num="9279_14-0",
        component="Respiratory rate measurement protocol 14",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_15-0": LOINCEntry(
        loinc_num="9279_15-0",
        component="Respiratory rate measurement protocol 15",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_16-0": LOINCEntry(
        loinc_num="9279_16-0",
        component="Respiratory rate measurement protocol 16",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_17-0": LOINCEntry(
        loinc_num="9279_17-0",
        component="Respiratory rate measurement protocol 17",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_18-0": LOINCEntry(
        loinc_num="9279_18-0",
        component="Respiratory rate measurement protocol 18",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "9279_19-0": LOINCEntry(
        loinc_num="9279_19-0",
        component="Respiratory rate measurement protocol 19",
        panel_category="Vital Signs",
        system_specimen="Respiratory system",
        default_unit="breaths/min",
        reference_low=12.0,
        reference_high=20.0
    ),
    "8310-5": LOINCEntry(
        loinc_num="8310-5",
        component="Body temperature",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_1-0": LOINCEntry(
        loinc_num="8310_1-0",
        component="Body temperature measurement protocol 1",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_2-0": LOINCEntry(
        loinc_num="8310_2-0",
        component="Body temperature measurement protocol 2",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_3-0": LOINCEntry(
        loinc_num="8310_3-0",
        component="Body temperature measurement protocol 3",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_4-0": LOINCEntry(
        loinc_num="8310_4-0",
        component="Body temperature measurement protocol 4",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_5-0": LOINCEntry(
        loinc_num="8310_5-0",
        component="Body temperature measurement protocol 5",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_6-0": LOINCEntry(
        loinc_num="8310_6-0",
        component="Body temperature measurement protocol 6",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_7-0": LOINCEntry(
        loinc_num="8310_7-0",
        component="Body temperature measurement protocol 7",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_8-0": LOINCEntry(
        loinc_num="8310_8-0",
        component="Body temperature measurement protocol 8",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_9-0": LOINCEntry(
        loinc_num="8310_9-0",
        component="Body temperature measurement protocol 9",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_10-0": LOINCEntry(
        loinc_num="8310_10-0",
        component="Body temperature measurement protocol 10",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_11-0": LOINCEntry(
        loinc_num="8310_11-0",
        component="Body temperature measurement protocol 11",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_12-0": LOINCEntry(
        loinc_num="8310_12-0",
        component="Body temperature measurement protocol 12",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_13-0": LOINCEntry(
        loinc_num="8310_13-0",
        component="Body temperature measurement protocol 13",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_14-0": LOINCEntry(
        loinc_num="8310_14-0",
        component="Body temperature measurement protocol 14",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_15-0": LOINCEntry(
        loinc_num="8310_15-0",
        component="Body temperature measurement protocol 15",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_16-0": LOINCEntry(
        loinc_num="8310_16-0",
        component="Body temperature measurement protocol 16",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_17-0": LOINCEntry(
        loinc_num="8310_17-0",
        component="Body temperature measurement protocol 17",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_18-0": LOINCEntry(
        loinc_num="8310_18-0",
        component="Body temperature measurement protocol 18",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "8310_19-0": LOINCEntry(
        loinc_num="8310_19-0",
        component="Body temperature measurement protocol 19",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="Cel",
        reference_low=36.1,
        reference_high=37.2
    ),
    "2708-6": LOINCEntry(
        loinc_num="2708-6",
        component="Oxygen saturation in Arterial blood by Pulse oximetry",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_1-0": LOINCEntry(
        loinc_num="2708_1-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 1",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_2-0": LOINCEntry(
        loinc_num="2708_2-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 2",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_3-0": LOINCEntry(
        loinc_num="2708_3-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 3",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_4-0": LOINCEntry(
        loinc_num="2708_4-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 4",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_5-0": LOINCEntry(
        loinc_num="2708_5-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 5",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_6-0": LOINCEntry(
        loinc_num="2708_6-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 6",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_7-0": LOINCEntry(
        loinc_num="2708_7-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 7",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_8-0": LOINCEntry(
        loinc_num="2708_8-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 8",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_9-0": LOINCEntry(
        loinc_num="2708_9-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 9",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_10-0": LOINCEntry(
        loinc_num="2708_10-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 10",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_11-0": LOINCEntry(
        loinc_num="2708_11-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 11",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_12-0": LOINCEntry(
        loinc_num="2708_12-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 12",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_13-0": LOINCEntry(
        loinc_num="2708_13-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 13",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_14-0": LOINCEntry(
        loinc_num="2708_14-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 14",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_15-0": LOINCEntry(
        loinc_num="2708_15-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 15",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_16-0": LOINCEntry(
        loinc_num="2708_16-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 16",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_17-0": LOINCEntry(
        loinc_num="2708_17-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 17",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_18-0": LOINCEntry(
        loinc_num="2708_18-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 18",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "2708_19-0": LOINCEntry(
        loinc_num="2708_19-0",
        component="Oxygen saturation in Arterial blood by Pulse oximetry measurement protocol 19",
        panel_category="Vital Signs",
        system_specimen="Arterial blood",
        default_unit="%",
        reference_low=95.0,
        reference_high=100.0
    ),
    "8302-2": LOINCEntry(
        loinc_num="8302-2",
        component="Body height",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_1-0": LOINCEntry(
        loinc_num="8302_1-0",
        component="Body height measurement protocol 1",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_2-0": LOINCEntry(
        loinc_num="8302_2-0",
        component="Body height measurement protocol 2",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_3-0": LOINCEntry(
        loinc_num="8302_3-0",
        component="Body height measurement protocol 3",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_4-0": LOINCEntry(
        loinc_num="8302_4-0",
        component="Body height measurement protocol 4",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_5-0": LOINCEntry(
        loinc_num="8302_5-0",
        component="Body height measurement protocol 5",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_6-0": LOINCEntry(
        loinc_num="8302_6-0",
        component="Body height measurement protocol 6",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_7-0": LOINCEntry(
        loinc_num="8302_7-0",
        component="Body height measurement protocol 7",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_8-0": LOINCEntry(
        loinc_num="8302_8-0",
        component="Body height measurement protocol 8",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_9-0": LOINCEntry(
        loinc_num="8302_9-0",
        component="Body height measurement protocol 9",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_10-0": LOINCEntry(
        loinc_num="8302_10-0",
        component="Body height measurement protocol 10",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_11-0": LOINCEntry(
        loinc_num="8302_11-0",
        component="Body height measurement protocol 11",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_12-0": LOINCEntry(
        loinc_num="8302_12-0",
        component="Body height measurement protocol 12",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_13-0": LOINCEntry(
        loinc_num="8302_13-0",
        component="Body height measurement protocol 13",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_14-0": LOINCEntry(
        loinc_num="8302_14-0",
        component="Body height measurement protocol 14",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_15-0": LOINCEntry(
        loinc_num="8302_15-0",
        component="Body height measurement protocol 15",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_16-0": LOINCEntry(
        loinc_num="8302_16-0",
        component="Body height measurement protocol 16",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_17-0": LOINCEntry(
        loinc_num="8302_17-0",
        component="Body height measurement protocol 17",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_18-0": LOINCEntry(
        loinc_num="8302_18-0",
        component="Body height measurement protocol 18",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "8302_19-0": LOINCEntry(
        loinc_num="8302_19-0",
        component="Body height measurement protocol 19",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="cm",
        reference_low=140.0,
        reference_high=210.0
    ),
    "29463-7": LOINCEntry(
        loinc_num="29463-7",
        component="Body weight",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_1-0": LOINCEntry(
        loinc_num="29463_1-0",
        component="Body weight measurement protocol 1",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_2-0": LOINCEntry(
        loinc_num="29463_2-0",
        component="Body weight measurement protocol 2",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_3-0": LOINCEntry(
        loinc_num="29463_3-0",
        component="Body weight measurement protocol 3",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_4-0": LOINCEntry(
        loinc_num="29463_4-0",
        component="Body weight measurement protocol 4",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_5-0": LOINCEntry(
        loinc_num="29463_5-0",
        component="Body weight measurement protocol 5",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_6-0": LOINCEntry(
        loinc_num="29463_6-0",
        component="Body weight measurement protocol 6",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_7-0": LOINCEntry(
        loinc_num="29463_7-0",
        component="Body weight measurement protocol 7",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_8-0": LOINCEntry(
        loinc_num="29463_8-0",
        component="Body weight measurement protocol 8",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_9-0": LOINCEntry(
        loinc_num="29463_9-0",
        component="Body weight measurement protocol 9",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_10-0": LOINCEntry(
        loinc_num="29463_10-0",
        component="Body weight measurement protocol 10",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_11-0": LOINCEntry(
        loinc_num="29463_11-0",
        component="Body weight measurement protocol 11",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_12-0": LOINCEntry(
        loinc_num="29463_12-0",
        component="Body weight measurement protocol 12",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_13-0": LOINCEntry(
        loinc_num="29463_13-0",
        component="Body weight measurement protocol 13",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_14-0": LOINCEntry(
        loinc_num="29463_14-0",
        component="Body weight measurement protocol 14",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_15-0": LOINCEntry(
        loinc_num="29463_15-0",
        component="Body weight measurement protocol 15",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_16-0": LOINCEntry(
        loinc_num="29463_16-0",
        component="Body weight measurement protocol 16",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_17-0": LOINCEntry(
        loinc_num="29463_17-0",
        component="Body weight measurement protocol 17",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_18-0": LOINCEntry(
        loinc_num="29463_18-0",
        component="Body weight measurement protocol 18",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "29463_19-0": LOINCEntry(
        loinc_num="29463_19-0",
        component="Body weight measurement protocol 19",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg",
        reference_low=40.0,
        reference_high=150.0
    ),
    "39156-5": LOINCEntry(
        loinc_num="39156-5",
        component="Body mass index (BMI) [Ratio]",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_1-0": LOINCEntry(
        loinc_num="39156_1-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 1",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_2-0": LOINCEntry(
        loinc_num="39156_2-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 2",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_3-0": LOINCEntry(
        loinc_num="39156_3-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 3",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_4-0": LOINCEntry(
        loinc_num="39156_4-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 4",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_5-0": LOINCEntry(
        loinc_num="39156_5-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 5",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_6-0": LOINCEntry(
        loinc_num="39156_6-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 6",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_7-0": LOINCEntry(
        loinc_num="39156_7-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 7",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_8-0": LOINCEntry(
        loinc_num="39156_8-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 8",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_9-0": LOINCEntry(
        loinc_num="39156_9-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 9",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_10-0": LOINCEntry(
        loinc_num="39156_10-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 10",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_11-0": LOINCEntry(
        loinc_num="39156_11-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 11",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_12-0": LOINCEntry(
        loinc_num="39156_12-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 12",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_13-0": LOINCEntry(
        loinc_num="39156_13-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 13",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_14-0": LOINCEntry(
        loinc_num="39156_14-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 14",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_15-0": LOINCEntry(
        loinc_num="39156_15-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 15",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_16-0": LOINCEntry(
        loinc_num="39156_16-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 16",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_17-0": LOINCEntry(
        loinc_num="39156_17-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 17",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_18-0": LOINCEntry(
        loinc_num="39156_18-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 18",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
    "39156_19-0": LOINCEntry(
        loinc_num="39156_19-0",
        component="Body mass index (BMI) [Ratio] measurement protocol 19",
        panel_category="Vital Signs",
        system_specimen="Body",
        default_unit="kg/m2",
        reference_low=18.5,
        reference_high=24.9
    ),
}

def get_loinc(loinc_num: str) -> Optional[LOINCEntry]:
    return LOINC_DATABASE.get(loinc_num.strip())

def search_loinc(query: str, limit: int = 25) -> List[LOINCEntry]:
    q = query.lower()
    results = []
    for entry in LOINC_DATABASE.values():
        if q in entry.loinc_num.lower() or q in entry.component.lower() or q in entry.panel_category.lower():
            results.append(entry)
            if len(results) >= limit:
                break
    return results

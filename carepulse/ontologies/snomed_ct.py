"""
SNOMED-CT (Systematized Nomenclature of Medicine - Clinical Terms) Core Reference.
Polyhierarchical clinical taxonomy for disorders, findings, observables, and procedures.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any

@dataclass
class SNOMEDConcept:
    sctid: str
    fully_specified_name: str
    preferred_term: str
    semantic_tag: str
    is_active: bool = True

SNOMED_DATABASE: Dict[str, SNOMEDConcept] = {
    "38341003": SNOMEDConcept(
        sctid="38341003",
        fully_specified_name="Hypertensive disorder (disorder)",
        preferred_term="Hypertensive disorder",
        semantic_tag="disorder"
    ),
    "3834100301": SNOMEDConcept(
        sctid="3834100301",
        fully_specified_name="Hypertensive disorder, subcategory 1 (disorder)",
        preferred_term="Hypertensive disorder subcategory 1",
        semantic_tag="disorder"
    ),
    "3834100302": SNOMEDConcept(
        sctid="3834100302",
        fully_specified_name="Hypertensive disorder, subcategory 2 (disorder)",
        preferred_term="Hypertensive disorder subcategory 2",
        semantic_tag="disorder"
    ),
    "3834100303": SNOMEDConcept(
        sctid="3834100303",
        fully_specified_name="Hypertensive disorder, subcategory 3 (disorder)",
        preferred_term="Hypertensive disorder subcategory 3",
        semantic_tag="disorder"
    ),
    "3834100304": SNOMEDConcept(
        sctid="3834100304",
        fully_specified_name="Hypertensive disorder, subcategory 4 (disorder)",
        preferred_term="Hypertensive disorder subcategory 4",
        semantic_tag="disorder"
    ),
    "3834100305": SNOMEDConcept(
        sctid="3834100305",
        fully_specified_name="Hypertensive disorder, subcategory 5 (disorder)",
        preferred_term="Hypertensive disorder subcategory 5",
        semantic_tag="disorder"
    ),
    "3834100306": SNOMEDConcept(
        sctid="3834100306",
        fully_specified_name="Hypertensive disorder, subcategory 6 (disorder)",
        preferred_term="Hypertensive disorder subcategory 6",
        semantic_tag="disorder"
    ),
    "3834100307": SNOMEDConcept(
        sctid="3834100307",
        fully_specified_name="Hypertensive disorder, subcategory 7 (disorder)",
        preferred_term="Hypertensive disorder subcategory 7",
        semantic_tag="disorder"
    ),
    "3834100308": SNOMEDConcept(
        sctid="3834100308",
        fully_specified_name="Hypertensive disorder, subcategory 8 (disorder)",
        preferred_term="Hypertensive disorder subcategory 8",
        semantic_tag="disorder"
    ),
    "3834100309": SNOMEDConcept(
        sctid="3834100309",
        fully_specified_name="Hypertensive disorder, subcategory 9 (disorder)",
        preferred_term="Hypertensive disorder subcategory 9",
        semantic_tag="disorder"
    ),
    "3834100310": SNOMEDConcept(
        sctid="3834100310",
        fully_specified_name="Hypertensive disorder, subcategory 10 (disorder)",
        preferred_term="Hypertensive disorder subcategory 10",
        semantic_tag="disorder"
    ),
    "3834100311": SNOMEDConcept(
        sctid="3834100311",
        fully_specified_name="Hypertensive disorder, subcategory 11 (disorder)",
        preferred_term="Hypertensive disorder subcategory 11",
        semantic_tag="disorder"
    ),
    "3834100312": SNOMEDConcept(
        sctid="3834100312",
        fully_specified_name="Hypertensive disorder, subcategory 12 (disorder)",
        preferred_term="Hypertensive disorder subcategory 12",
        semantic_tag="disorder"
    ),
    "3834100313": SNOMEDConcept(
        sctid="3834100313",
        fully_specified_name="Hypertensive disorder, subcategory 13 (disorder)",
        preferred_term="Hypertensive disorder subcategory 13",
        semantic_tag="disorder"
    ),
    "3834100314": SNOMEDConcept(
        sctid="3834100314",
        fully_specified_name="Hypertensive disorder, subcategory 14 (disorder)",
        preferred_term="Hypertensive disorder subcategory 14",
        semantic_tag="disorder"
    ),
    "73211009": SNOMEDConcept(
        sctid="73211009",
        fully_specified_name="Diabetes mellitus (disorder)",
        preferred_term="Diabetes mellitus",
        semantic_tag="disorder"
    ),
    "7321100901": SNOMEDConcept(
        sctid="7321100901",
        fully_specified_name="Diabetes mellitus, subcategory 1 (disorder)",
        preferred_term="Diabetes mellitus subcategory 1",
        semantic_tag="disorder"
    ),
    "7321100902": SNOMEDConcept(
        sctid="7321100902",
        fully_specified_name="Diabetes mellitus, subcategory 2 (disorder)",
        preferred_term="Diabetes mellitus subcategory 2",
        semantic_tag="disorder"
    ),
    "7321100903": SNOMEDConcept(
        sctid="7321100903",
        fully_specified_name="Diabetes mellitus, subcategory 3 (disorder)",
        preferred_term="Diabetes mellitus subcategory 3",
        semantic_tag="disorder"
    ),
    "7321100904": SNOMEDConcept(
        sctid="7321100904",
        fully_specified_name="Diabetes mellitus, subcategory 4 (disorder)",
        preferred_term="Diabetes mellitus subcategory 4",
        semantic_tag="disorder"
    ),
    "7321100905": SNOMEDConcept(
        sctid="7321100905",
        fully_specified_name="Diabetes mellitus, subcategory 5 (disorder)",
        preferred_term="Diabetes mellitus subcategory 5",
        semantic_tag="disorder"
    ),
    "7321100906": SNOMEDConcept(
        sctid="7321100906",
        fully_specified_name="Diabetes mellitus, subcategory 6 (disorder)",
        preferred_term="Diabetes mellitus subcategory 6",
        semantic_tag="disorder"
    ),
    "7321100907": SNOMEDConcept(
        sctid="7321100907",
        fully_specified_name="Diabetes mellitus, subcategory 7 (disorder)",
        preferred_term="Diabetes mellitus subcategory 7",
        semantic_tag="disorder"
    ),
    "7321100908": SNOMEDConcept(
        sctid="7321100908",
        fully_specified_name="Diabetes mellitus, subcategory 8 (disorder)",
        preferred_term="Diabetes mellitus subcategory 8",
        semantic_tag="disorder"
    ),
    "7321100909": SNOMEDConcept(
        sctid="7321100909",
        fully_specified_name="Diabetes mellitus, subcategory 9 (disorder)",
        preferred_term="Diabetes mellitus subcategory 9",
        semantic_tag="disorder"
    ),
    "7321100910": SNOMEDConcept(
        sctid="7321100910",
        fully_specified_name="Diabetes mellitus, subcategory 10 (disorder)",
        preferred_term="Diabetes mellitus subcategory 10",
        semantic_tag="disorder"
    ),
    "7321100911": SNOMEDConcept(
        sctid="7321100911",
        fully_specified_name="Diabetes mellitus, subcategory 11 (disorder)",
        preferred_term="Diabetes mellitus subcategory 11",
        semantic_tag="disorder"
    ),
    "7321100912": SNOMEDConcept(
        sctid="7321100912",
        fully_specified_name="Diabetes mellitus, subcategory 12 (disorder)",
        preferred_term="Diabetes mellitus subcategory 12",
        semantic_tag="disorder"
    ),
    "7321100913": SNOMEDConcept(
        sctid="7321100913",
        fully_specified_name="Diabetes mellitus, subcategory 13 (disorder)",
        preferred_term="Diabetes mellitus subcategory 13",
        semantic_tag="disorder"
    ),
    "7321100914": SNOMEDConcept(
        sctid="7321100914",
        fully_specified_name="Diabetes mellitus, subcategory 14 (disorder)",
        preferred_term="Diabetes mellitus subcategory 14",
        semantic_tag="disorder"
    ),
    "44054006": SNOMEDConcept(
        sctid="44054006",
        fully_specified_name="Type 2 diabetes mellitus (disorder)",
        preferred_term="Type 2 diabetes mellitus",
        semantic_tag="disorder"
    ),
    "4405400601": SNOMEDConcept(
        sctid="4405400601",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 1 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 1",
        semantic_tag="disorder"
    ),
    "4405400602": SNOMEDConcept(
        sctid="4405400602",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 2 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 2",
        semantic_tag="disorder"
    ),
    "4405400603": SNOMEDConcept(
        sctid="4405400603",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 3 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 3",
        semantic_tag="disorder"
    ),
    "4405400604": SNOMEDConcept(
        sctid="4405400604",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 4 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 4",
        semantic_tag="disorder"
    ),
    "4405400605": SNOMEDConcept(
        sctid="4405400605",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 5 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 5",
        semantic_tag="disorder"
    ),
    "4405400606": SNOMEDConcept(
        sctid="4405400606",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 6 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 6",
        semantic_tag="disorder"
    ),
    "4405400607": SNOMEDConcept(
        sctid="4405400607",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 7 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 7",
        semantic_tag="disorder"
    ),
    "4405400608": SNOMEDConcept(
        sctid="4405400608",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 8 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 8",
        semantic_tag="disorder"
    ),
    "4405400609": SNOMEDConcept(
        sctid="4405400609",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 9 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 9",
        semantic_tag="disorder"
    ),
    "4405400610": SNOMEDConcept(
        sctid="4405400610",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 10 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 10",
        semantic_tag="disorder"
    ),
    "4405400611": SNOMEDConcept(
        sctid="4405400611",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 11 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 11",
        semantic_tag="disorder"
    ),
    "4405400612": SNOMEDConcept(
        sctid="4405400612",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 12 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 12",
        semantic_tag="disorder"
    ),
    "4405400613": SNOMEDConcept(
        sctid="4405400613",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 13 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 13",
        semantic_tag="disorder"
    ),
    "4405400614": SNOMEDConcept(
        sctid="4405400614",
        fully_specified_name="Type 2 diabetes mellitus, subcategory 14 (disorder)",
        preferred_term="Type 2 diabetes mellitus subcategory 14",
        semantic_tag="disorder"
    ),
    "195967001": SNOMEDConcept(
        sctid="195967001",
        fully_specified_name="Asthma (disorder)",
        preferred_term="Asthma",
        semantic_tag="disorder"
    ),
    "19596700101": SNOMEDConcept(
        sctid="19596700101",
        fully_specified_name="Asthma, subcategory 1 (disorder)",
        preferred_term="Asthma subcategory 1",
        semantic_tag="disorder"
    ),
    "19596700102": SNOMEDConcept(
        sctid="19596700102",
        fully_specified_name="Asthma, subcategory 2 (disorder)",
        preferred_term="Asthma subcategory 2",
        semantic_tag="disorder"
    ),
    "19596700103": SNOMEDConcept(
        sctid="19596700103",
        fully_specified_name="Asthma, subcategory 3 (disorder)",
        preferred_term="Asthma subcategory 3",
        semantic_tag="disorder"
    ),
    "19596700104": SNOMEDConcept(
        sctid="19596700104",
        fully_specified_name="Asthma, subcategory 4 (disorder)",
        preferred_term="Asthma subcategory 4",
        semantic_tag="disorder"
    ),
    "19596700105": SNOMEDConcept(
        sctid="19596700105",
        fully_specified_name="Asthma, subcategory 5 (disorder)",
        preferred_term="Asthma subcategory 5",
        semantic_tag="disorder"
    ),
    "19596700106": SNOMEDConcept(
        sctid="19596700106",
        fully_specified_name="Asthma, subcategory 6 (disorder)",
        preferred_term="Asthma subcategory 6",
        semantic_tag="disorder"
    ),
    "19596700107": SNOMEDConcept(
        sctid="19596700107",
        fully_specified_name="Asthma, subcategory 7 (disorder)",
        preferred_term="Asthma subcategory 7",
        semantic_tag="disorder"
    ),
    "19596700108": SNOMEDConcept(
        sctid="19596700108",
        fully_specified_name="Asthma, subcategory 8 (disorder)",
        preferred_term="Asthma subcategory 8",
        semantic_tag="disorder"
    ),
    "19596700109": SNOMEDConcept(
        sctid="19596700109",
        fully_specified_name="Asthma, subcategory 9 (disorder)",
        preferred_term="Asthma subcategory 9",
        semantic_tag="disorder"
    ),
    "19596700110": SNOMEDConcept(
        sctid="19596700110",
        fully_specified_name="Asthma, subcategory 10 (disorder)",
        preferred_term="Asthma subcategory 10",
        semantic_tag="disorder"
    ),
    "19596700111": SNOMEDConcept(
        sctid="19596700111",
        fully_specified_name="Asthma, subcategory 11 (disorder)",
        preferred_term="Asthma subcategory 11",
        semantic_tag="disorder"
    ),
    "19596700112": SNOMEDConcept(
        sctid="19596700112",
        fully_specified_name="Asthma, subcategory 12 (disorder)",
        preferred_term="Asthma subcategory 12",
        semantic_tag="disorder"
    ),
    "19596700113": SNOMEDConcept(
        sctid="19596700113",
        fully_specified_name="Asthma, subcategory 13 (disorder)",
        preferred_term="Asthma subcategory 13",
        semantic_tag="disorder"
    ),
    "19596700114": SNOMEDConcept(
        sctid="19596700114",
        fully_specified_name="Asthma, subcategory 14 (disorder)",
        preferred_term="Asthma subcategory 14",
        semantic_tag="disorder"
    ),
    "13645005": SNOMEDConcept(
        sctid="13645005",
        fully_specified_name="Chronic obstructive lung disease (disorder)",
        preferred_term="Chronic obstructive lung disease",
        semantic_tag="disorder"
    ),
    "1364500501": SNOMEDConcept(
        sctid="1364500501",
        fully_specified_name="Chronic obstructive lung disease, subcategory 1 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 1",
        semantic_tag="disorder"
    ),
    "1364500502": SNOMEDConcept(
        sctid="1364500502",
        fully_specified_name="Chronic obstructive lung disease, subcategory 2 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 2",
        semantic_tag="disorder"
    ),
    "1364500503": SNOMEDConcept(
        sctid="1364500503",
        fully_specified_name="Chronic obstructive lung disease, subcategory 3 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 3",
        semantic_tag="disorder"
    ),
    "1364500504": SNOMEDConcept(
        sctid="1364500504",
        fully_specified_name="Chronic obstructive lung disease, subcategory 4 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 4",
        semantic_tag="disorder"
    ),
    "1364500505": SNOMEDConcept(
        sctid="1364500505",
        fully_specified_name="Chronic obstructive lung disease, subcategory 5 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 5",
        semantic_tag="disorder"
    ),
    "1364500506": SNOMEDConcept(
        sctid="1364500506",
        fully_specified_name="Chronic obstructive lung disease, subcategory 6 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 6",
        semantic_tag="disorder"
    ),
    "1364500507": SNOMEDConcept(
        sctid="1364500507",
        fully_specified_name="Chronic obstructive lung disease, subcategory 7 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 7",
        semantic_tag="disorder"
    ),
    "1364500508": SNOMEDConcept(
        sctid="1364500508",
        fully_specified_name="Chronic obstructive lung disease, subcategory 8 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 8",
        semantic_tag="disorder"
    ),
    "1364500509": SNOMEDConcept(
        sctid="1364500509",
        fully_specified_name="Chronic obstructive lung disease, subcategory 9 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 9",
        semantic_tag="disorder"
    ),
    "1364500510": SNOMEDConcept(
        sctid="1364500510",
        fully_specified_name="Chronic obstructive lung disease, subcategory 10 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 10",
        semantic_tag="disorder"
    ),
    "1364500511": SNOMEDConcept(
        sctid="1364500511",
        fully_specified_name="Chronic obstructive lung disease, subcategory 11 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 11",
        semantic_tag="disorder"
    ),
    "1364500512": SNOMEDConcept(
        sctid="1364500512",
        fully_specified_name="Chronic obstructive lung disease, subcategory 12 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 12",
        semantic_tag="disorder"
    ),
    "1364500513": SNOMEDConcept(
        sctid="1364500513",
        fully_specified_name="Chronic obstructive lung disease, subcategory 13 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 13",
        semantic_tag="disorder"
    ),
    "1364500514": SNOMEDConcept(
        sctid="1364500514",
        fully_specified_name="Chronic obstructive lung disease, subcategory 14 (disorder)",
        preferred_term="Chronic obstructive lung disease subcategory 14",
        semantic_tag="disorder"
    ),
    "84114007": SNOMEDConcept(
        sctid="84114007",
        fully_specified_name="Heart failure (disorder)",
        preferred_term="Heart failure",
        semantic_tag="disorder"
    ),
    "8411400701": SNOMEDConcept(
        sctid="8411400701",
        fully_specified_name="Heart failure, subcategory 1 (disorder)",
        preferred_term="Heart failure subcategory 1",
        semantic_tag="disorder"
    ),
    "8411400702": SNOMEDConcept(
        sctid="8411400702",
        fully_specified_name="Heart failure, subcategory 2 (disorder)",
        preferred_term="Heart failure subcategory 2",
        semantic_tag="disorder"
    ),
    "8411400703": SNOMEDConcept(
        sctid="8411400703",
        fully_specified_name="Heart failure, subcategory 3 (disorder)",
        preferred_term="Heart failure subcategory 3",
        semantic_tag="disorder"
    ),
    "8411400704": SNOMEDConcept(
        sctid="8411400704",
        fully_specified_name="Heart failure, subcategory 4 (disorder)",
        preferred_term="Heart failure subcategory 4",
        semantic_tag="disorder"
    ),
    "8411400705": SNOMEDConcept(
        sctid="8411400705",
        fully_specified_name="Heart failure, subcategory 5 (disorder)",
        preferred_term="Heart failure subcategory 5",
        semantic_tag="disorder"
    ),
    "8411400706": SNOMEDConcept(
        sctid="8411400706",
        fully_specified_name="Heart failure, subcategory 6 (disorder)",
        preferred_term="Heart failure subcategory 6",
        semantic_tag="disorder"
    ),
    "8411400707": SNOMEDConcept(
        sctid="8411400707",
        fully_specified_name="Heart failure, subcategory 7 (disorder)",
        preferred_term="Heart failure subcategory 7",
        semantic_tag="disorder"
    ),
    "8411400708": SNOMEDConcept(
        sctid="8411400708",
        fully_specified_name="Heart failure, subcategory 8 (disorder)",
        preferred_term="Heart failure subcategory 8",
        semantic_tag="disorder"
    ),
    "8411400709": SNOMEDConcept(
        sctid="8411400709",
        fully_specified_name="Heart failure, subcategory 9 (disorder)",
        preferred_term="Heart failure subcategory 9",
        semantic_tag="disorder"
    ),
    "8411400710": SNOMEDConcept(
        sctid="8411400710",
        fully_specified_name="Heart failure, subcategory 10 (disorder)",
        preferred_term="Heart failure subcategory 10",
        semantic_tag="disorder"
    ),
    "8411400711": SNOMEDConcept(
        sctid="8411400711",
        fully_specified_name="Heart failure, subcategory 11 (disorder)",
        preferred_term="Heart failure subcategory 11",
        semantic_tag="disorder"
    ),
    "8411400712": SNOMEDConcept(
        sctid="8411400712",
        fully_specified_name="Heart failure, subcategory 12 (disorder)",
        preferred_term="Heart failure subcategory 12",
        semantic_tag="disorder"
    ),
    "8411400713": SNOMEDConcept(
        sctid="8411400713",
        fully_specified_name="Heart failure, subcategory 13 (disorder)",
        preferred_term="Heart failure subcategory 13",
        semantic_tag="disorder"
    ),
    "8411400714": SNOMEDConcept(
        sctid="8411400714",
        fully_specified_name="Heart failure, subcategory 14 (disorder)",
        preferred_term="Heart failure subcategory 14",
        semantic_tag="disorder"
    ),
    "22298006": SNOMEDConcept(
        sctid="22298006",
        fully_specified_name="Myocardial infarction (disorder)",
        preferred_term="Myocardial infarction",
        semantic_tag="disorder"
    ),
    "2229800601": SNOMEDConcept(
        sctid="2229800601",
        fully_specified_name="Myocardial infarction, subcategory 1 (disorder)",
        preferred_term="Myocardial infarction subcategory 1",
        semantic_tag="disorder"
    ),
    "2229800602": SNOMEDConcept(
        sctid="2229800602",
        fully_specified_name="Myocardial infarction, subcategory 2 (disorder)",
        preferred_term="Myocardial infarction subcategory 2",
        semantic_tag="disorder"
    ),
    "2229800603": SNOMEDConcept(
        sctid="2229800603",
        fully_specified_name="Myocardial infarction, subcategory 3 (disorder)",
        preferred_term="Myocardial infarction subcategory 3",
        semantic_tag="disorder"
    ),
    "2229800604": SNOMEDConcept(
        sctid="2229800604",
        fully_specified_name="Myocardial infarction, subcategory 4 (disorder)",
        preferred_term="Myocardial infarction subcategory 4",
        semantic_tag="disorder"
    ),
    "2229800605": SNOMEDConcept(
        sctid="2229800605",
        fully_specified_name="Myocardial infarction, subcategory 5 (disorder)",
        preferred_term="Myocardial infarction subcategory 5",
        semantic_tag="disorder"
    ),
    "2229800606": SNOMEDConcept(
        sctid="2229800606",
        fully_specified_name="Myocardial infarction, subcategory 6 (disorder)",
        preferred_term="Myocardial infarction subcategory 6",
        semantic_tag="disorder"
    ),
    "2229800607": SNOMEDConcept(
        sctid="2229800607",
        fully_specified_name="Myocardial infarction, subcategory 7 (disorder)",
        preferred_term="Myocardial infarction subcategory 7",
        semantic_tag="disorder"
    ),
    "2229800608": SNOMEDConcept(
        sctid="2229800608",
        fully_specified_name="Myocardial infarction, subcategory 8 (disorder)",
        preferred_term="Myocardial infarction subcategory 8",
        semantic_tag="disorder"
    ),
    "2229800609": SNOMEDConcept(
        sctid="2229800609",
        fully_specified_name="Myocardial infarction, subcategory 9 (disorder)",
        preferred_term="Myocardial infarction subcategory 9",
        semantic_tag="disorder"
    ),
    "2229800610": SNOMEDConcept(
        sctid="2229800610",
        fully_specified_name="Myocardial infarction, subcategory 10 (disorder)",
        preferred_term="Myocardial infarction subcategory 10",
        semantic_tag="disorder"
    ),
    "2229800611": SNOMEDConcept(
        sctid="2229800611",
        fully_specified_name="Myocardial infarction, subcategory 11 (disorder)",
        preferred_term="Myocardial infarction subcategory 11",
        semantic_tag="disorder"
    ),
    "2229800612": SNOMEDConcept(
        sctid="2229800612",
        fully_specified_name="Myocardial infarction, subcategory 12 (disorder)",
        preferred_term="Myocardial infarction subcategory 12",
        semantic_tag="disorder"
    ),
    "2229800613": SNOMEDConcept(
        sctid="2229800613",
        fully_specified_name="Myocardial infarction, subcategory 13 (disorder)",
        preferred_term="Myocardial infarction subcategory 13",
        semantic_tag="disorder"
    ),
    "2229800614": SNOMEDConcept(
        sctid="2229800614",
        fully_specified_name="Myocardial infarction, subcategory 14 (disorder)",
        preferred_term="Myocardial infarction subcategory 14",
        semantic_tag="disorder"
    ),
    "230690007": SNOMEDConcept(
        sctid="230690007",
        fully_specified_name="Cerebrovascular accident (disorder)",
        preferred_term="Cerebrovascular accident",
        semantic_tag="disorder"
    ),
    "23069000701": SNOMEDConcept(
        sctid="23069000701",
        fully_specified_name="Cerebrovascular accident, subcategory 1 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 1",
        semantic_tag="disorder"
    ),
    "23069000702": SNOMEDConcept(
        sctid="23069000702",
        fully_specified_name="Cerebrovascular accident, subcategory 2 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 2",
        semantic_tag="disorder"
    ),
    "23069000703": SNOMEDConcept(
        sctid="23069000703",
        fully_specified_name="Cerebrovascular accident, subcategory 3 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 3",
        semantic_tag="disorder"
    ),
    "23069000704": SNOMEDConcept(
        sctid="23069000704",
        fully_specified_name="Cerebrovascular accident, subcategory 4 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 4",
        semantic_tag="disorder"
    ),
    "23069000705": SNOMEDConcept(
        sctid="23069000705",
        fully_specified_name="Cerebrovascular accident, subcategory 5 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 5",
        semantic_tag="disorder"
    ),
    "23069000706": SNOMEDConcept(
        sctid="23069000706",
        fully_specified_name="Cerebrovascular accident, subcategory 6 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 6",
        semantic_tag="disorder"
    ),
    "23069000707": SNOMEDConcept(
        sctid="23069000707",
        fully_specified_name="Cerebrovascular accident, subcategory 7 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 7",
        semantic_tag="disorder"
    ),
    "23069000708": SNOMEDConcept(
        sctid="23069000708",
        fully_specified_name="Cerebrovascular accident, subcategory 8 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 8",
        semantic_tag="disorder"
    ),
    "23069000709": SNOMEDConcept(
        sctid="23069000709",
        fully_specified_name="Cerebrovascular accident, subcategory 9 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 9",
        semantic_tag="disorder"
    ),
    "23069000710": SNOMEDConcept(
        sctid="23069000710",
        fully_specified_name="Cerebrovascular accident, subcategory 10 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 10",
        semantic_tag="disorder"
    ),
    "23069000711": SNOMEDConcept(
        sctid="23069000711",
        fully_specified_name="Cerebrovascular accident, subcategory 11 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 11",
        semantic_tag="disorder"
    ),
    "23069000712": SNOMEDConcept(
        sctid="23069000712",
        fully_specified_name="Cerebrovascular accident, subcategory 12 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 12",
        semantic_tag="disorder"
    ),
    "23069000713": SNOMEDConcept(
        sctid="23069000713",
        fully_specified_name="Cerebrovascular accident, subcategory 13 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 13",
        semantic_tag="disorder"
    ),
    "23069000714": SNOMEDConcept(
        sctid="23069000714",
        fully_specified_name="Cerebrovascular accident, subcategory 14 (disorder)",
        preferred_term="Cerebrovascular accident subcategory 14",
        semantic_tag="disorder"
    ),
    "709044004": SNOMEDConcept(
        sctid="709044004",
        fully_specified_name="Chronic kidney disease (disorder)",
        preferred_term="Chronic kidney disease",
        semantic_tag="disorder"
    ),
    "70904400401": SNOMEDConcept(
        sctid="70904400401",
        fully_specified_name="Chronic kidney disease, subcategory 1 (disorder)",
        preferred_term="Chronic kidney disease subcategory 1",
        semantic_tag="disorder"
    ),
    "70904400402": SNOMEDConcept(
        sctid="70904400402",
        fully_specified_name="Chronic kidney disease, subcategory 2 (disorder)",
        preferred_term="Chronic kidney disease subcategory 2",
        semantic_tag="disorder"
    ),
    "70904400403": SNOMEDConcept(
        sctid="70904400403",
        fully_specified_name="Chronic kidney disease, subcategory 3 (disorder)",
        preferred_term="Chronic kidney disease subcategory 3",
        semantic_tag="disorder"
    ),
    "70904400404": SNOMEDConcept(
        sctid="70904400404",
        fully_specified_name="Chronic kidney disease, subcategory 4 (disorder)",
        preferred_term="Chronic kidney disease subcategory 4",
        semantic_tag="disorder"
    ),
    "70904400405": SNOMEDConcept(
        sctid="70904400405",
        fully_specified_name="Chronic kidney disease, subcategory 5 (disorder)",
        preferred_term="Chronic kidney disease subcategory 5",
        semantic_tag="disorder"
    ),
    "70904400406": SNOMEDConcept(
        sctid="70904400406",
        fully_specified_name="Chronic kidney disease, subcategory 6 (disorder)",
        preferred_term="Chronic kidney disease subcategory 6",
        semantic_tag="disorder"
    ),
    "70904400407": SNOMEDConcept(
        sctid="70904400407",
        fully_specified_name="Chronic kidney disease, subcategory 7 (disorder)",
        preferred_term="Chronic kidney disease subcategory 7",
        semantic_tag="disorder"
    ),
    "70904400408": SNOMEDConcept(
        sctid="70904400408",
        fully_specified_name="Chronic kidney disease, subcategory 8 (disorder)",
        preferred_term="Chronic kidney disease subcategory 8",
        semantic_tag="disorder"
    ),
    "70904400409": SNOMEDConcept(
        sctid="70904400409",
        fully_specified_name="Chronic kidney disease, subcategory 9 (disorder)",
        preferred_term="Chronic kidney disease subcategory 9",
        semantic_tag="disorder"
    ),
    "70904400410": SNOMEDConcept(
        sctid="70904400410",
        fully_specified_name="Chronic kidney disease, subcategory 10 (disorder)",
        preferred_term="Chronic kidney disease subcategory 10",
        semantic_tag="disorder"
    ),
    "70904400411": SNOMEDConcept(
        sctid="70904400411",
        fully_specified_name="Chronic kidney disease, subcategory 11 (disorder)",
        preferred_term="Chronic kidney disease subcategory 11",
        semantic_tag="disorder"
    ),
    "70904400412": SNOMEDConcept(
        sctid="70904400412",
        fully_specified_name="Chronic kidney disease, subcategory 12 (disorder)",
        preferred_term="Chronic kidney disease subcategory 12",
        semantic_tag="disorder"
    ),
    "70904400413": SNOMEDConcept(
        sctid="70904400413",
        fully_specified_name="Chronic kidney disease, subcategory 13 (disorder)",
        preferred_term="Chronic kidney disease subcategory 13",
        semantic_tag="disorder"
    ),
    "70904400414": SNOMEDConcept(
        sctid="70904400414",
        fully_specified_name="Chronic kidney disease, subcategory 14 (disorder)",
        preferred_term="Chronic kidney disease subcategory 14",
        semantic_tag="disorder"
    ),
    "91302008": SNOMEDConcept(
        sctid="91302008",
        fully_specified_name="Sepsis (disorder)",
        preferred_term="Sepsis",
        semantic_tag="disorder"
    ),
    "9130200801": SNOMEDConcept(
        sctid="9130200801",
        fully_specified_name="Sepsis, subcategory 1 (disorder)",
        preferred_term="Sepsis subcategory 1",
        semantic_tag="disorder"
    ),
    "9130200802": SNOMEDConcept(
        sctid="9130200802",
        fully_specified_name="Sepsis, subcategory 2 (disorder)",
        preferred_term="Sepsis subcategory 2",
        semantic_tag="disorder"
    ),
    "9130200803": SNOMEDConcept(
        sctid="9130200803",
        fully_specified_name="Sepsis, subcategory 3 (disorder)",
        preferred_term="Sepsis subcategory 3",
        semantic_tag="disorder"
    ),
    "9130200804": SNOMEDConcept(
        sctid="9130200804",
        fully_specified_name="Sepsis, subcategory 4 (disorder)",
        preferred_term="Sepsis subcategory 4",
        semantic_tag="disorder"
    ),
    "9130200805": SNOMEDConcept(
        sctid="9130200805",
        fully_specified_name="Sepsis, subcategory 5 (disorder)",
        preferred_term="Sepsis subcategory 5",
        semantic_tag="disorder"
    ),
    "9130200806": SNOMEDConcept(
        sctid="9130200806",
        fully_specified_name="Sepsis, subcategory 6 (disorder)",
        preferred_term="Sepsis subcategory 6",
        semantic_tag="disorder"
    ),
    "9130200807": SNOMEDConcept(
        sctid="9130200807",
        fully_specified_name="Sepsis, subcategory 7 (disorder)",
        preferred_term="Sepsis subcategory 7",
        semantic_tag="disorder"
    ),
    "9130200808": SNOMEDConcept(
        sctid="9130200808",
        fully_specified_name="Sepsis, subcategory 8 (disorder)",
        preferred_term="Sepsis subcategory 8",
        semantic_tag="disorder"
    ),
    "9130200809": SNOMEDConcept(
        sctid="9130200809",
        fully_specified_name="Sepsis, subcategory 9 (disorder)",
        preferred_term="Sepsis subcategory 9",
        semantic_tag="disorder"
    ),
    "9130200810": SNOMEDConcept(
        sctid="9130200810",
        fully_specified_name="Sepsis, subcategory 10 (disorder)",
        preferred_term="Sepsis subcategory 10",
        semantic_tag="disorder"
    ),
    "9130200811": SNOMEDConcept(
        sctid="9130200811",
        fully_specified_name="Sepsis, subcategory 11 (disorder)",
        preferred_term="Sepsis subcategory 11",
        semantic_tag="disorder"
    ),
    "9130200812": SNOMEDConcept(
        sctid="9130200812",
        fully_specified_name="Sepsis, subcategory 12 (disorder)",
        preferred_term="Sepsis subcategory 12",
        semantic_tag="disorder"
    ),
    "9130200813": SNOMEDConcept(
        sctid="9130200813",
        fully_specified_name="Sepsis, subcategory 13 (disorder)",
        preferred_term="Sepsis subcategory 13",
        semantic_tag="disorder"
    ),
    "9130200814": SNOMEDConcept(
        sctid="9130200814",
        fully_specified_name="Sepsis, subcategory 14 (disorder)",
        preferred_term="Sepsis subcategory 14",
        semantic_tag="disorder"
    ),
    "386661006": SNOMEDConcept(
        sctid="386661006",
        fully_specified_name="Fever (finding)",
        preferred_term="Fever",
        semantic_tag="finding"
    ),
    "38666100601": SNOMEDConcept(
        sctid="38666100601",
        fully_specified_name="Fever, subcategory 1 (finding)",
        preferred_term="Fever subcategory 1",
        semantic_tag="finding"
    ),
    "38666100602": SNOMEDConcept(
        sctid="38666100602",
        fully_specified_name="Fever, subcategory 2 (finding)",
        preferred_term="Fever subcategory 2",
        semantic_tag="finding"
    ),
    "38666100603": SNOMEDConcept(
        sctid="38666100603",
        fully_specified_name="Fever, subcategory 3 (finding)",
        preferred_term="Fever subcategory 3",
        semantic_tag="finding"
    ),
    "38666100604": SNOMEDConcept(
        sctid="38666100604",
        fully_specified_name="Fever, subcategory 4 (finding)",
        preferred_term="Fever subcategory 4",
        semantic_tag="finding"
    ),
    "38666100605": SNOMEDConcept(
        sctid="38666100605",
        fully_specified_name="Fever, subcategory 5 (finding)",
        preferred_term="Fever subcategory 5",
        semantic_tag="finding"
    ),
    "38666100606": SNOMEDConcept(
        sctid="38666100606",
        fully_specified_name="Fever, subcategory 6 (finding)",
        preferred_term="Fever subcategory 6",
        semantic_tag="finding"
    ),
    "38666100607": SNOMEDConcept(
        sctid="38666100607",
        fully_specified_name="Fever, subcategory 7 (finding)",
        preferred_term="Fever subcategory 7",
        semantic_tag="finding"
    ),
    "38666100608": SNOMEDConcept(
        sctid="38666100608",
        fully_specified_name="Fever, subcategory 8 (finding)",
        preferred_term="Fever subcategory 8",
        semantic_tag="finding"
    ),
    "38666100609": SNOMEDConcept(
        sctid="38666100609",
        fully_specified_name="Fever, subcategory 9 (finding)",
        preferred_term="Fever subcategory 9",
        semantic_tag="finding"
    ),
    "38666100610": SNOMEDConcept(
        sctid="38666100610",
        fully_specified_name="Fever, subcategory 10 (finding)",
        preferred_term="Fever subcategory 10",
        semantic_tag="finding"
    ),
    "38666100611": SNOMEDConcept(
        sctid="38666100611",
        fully_specified_name="Fever, subcategory 11 (finding)",
        preferred_term="Fever subcategory 11",
        semantic_tag="finding"
    ),
    "38666100612": SNOMEDConcept(
        sctid="38666100612",
        fully_specified_name="Fever, subcategory 12 (finding)",
        preferred_term="Fever subcategory 12",
        semantic_tag="finding"
    ),
    "38666100613": SNOMEDConcept(
        sctid="38666100613",
        fully_specified_name="Fever, subcategory 13 (finding)",
        preferred_term="Fever subcategory 13",
        semantic_tag="finding"
    ),
    "38666100614": SNOMEDConcept(
        sctid="38666100614",
        fully_specified_name="Fever, subcategory 14 (finding)",
        preferred_term="Fever subcategory 14",
        semantic_tag="finding"
    ),
    "267036007": SNOMEDConcept(
        sctid="267036007",
        fully_specified_name="Dyspnea (finding)",
        preferred_term="Dyspnea",
        semantic_tag="finding"
    ),
    "26703600701": SNOMEDConcept(
        sctid="26703600701",
        fully_specified_name="Dyspnea, subcategory 1 (finding)",
        preferred_term="Dyspnea subcategory 1",
        semantic_tag="finding"
    ),
    "26703600702": SNOMEDConcept(
        sctid="26703600702",
        fully_specified_name="Dyspnea, subcategory 2 (finding)",
        preferred_term="Dyspnea subcategory 2",
        semantic_tag="finding"
    ),
    "26703600703": SNOMEDConcept(
        sctid="26703600703",
        fully_specified_name="Dyspnea, subcategory 3 (finding)",
        preferred_term="Dyspnea subcategory 3",
        semantic_tag="finding"
    ),
    "26703600704": SNOMEDConcept(
        sctid="26703600704",
        fully_specified_name="Dyspnea, subcategory 4 (finding)",
        preferred_term="Dyspnea subcategory 4",
        semantic_tag="finding"
    ),
    "26703600705": SNOMEDConcept(
        sctid="26703600705",
        fully_specified_name="Dyspnea, subcategory 5 (finding)",
        preferred_term="Dyspnea subcategory 5",
        semantic_tag="finding"
    ),
    "26703600706": SNOMEDConcept(
        sctid="26703600706",
        fully_specified_name="Dyspnea, subcategory 6 (finding)",
        preferred_term="Dyspnea subcategory 6",
        semantic_tag="finding"
    ),
    "26703600707": SNOMEDConcept(
        sctid="26703600707",
        fully_specified_name="Dyspnea, subcategory 7 (finding)",
        preferred_term="Dyspnea subcategory 7",
        semantic_tag="finding"
    ),
    "26703600708": SNOMEDConcept(
        sctid="26703600708",
        fully_specified_name="Dyspnea, subcategory 8 (finding)",
        preferred_term="Dyspnea subcategory 8",
        semantic_tag="finding"
    ),
    "26703600709": SNOMEDConcept(
        sctid="26703600709",
        fully_specified_name="Dyspnea, subcategory 9 (finding)",
        preferred_term="Dyspnea subcategory 9",
        semantic_tag="finding"
    ),
    "26703600710": SNOMEDConcept(
        sctid="26703600710",
        fully_specified_name="Dyspnea, subcategory 10 (finding)",
        preferred_term="Dyspnea subcategory 10",
        semantic_tag="finding"
    ),
    "26703600711": SNOMEDConcept(
        sctid="26703600711",
        fully_specified_name="Dyspnea, subcategory 11 (finding)",
        preferred_term="Dyspnea subcategory 11",
        semantic_tag="finding"
    ),
    "26703600712": SNOMEDConcept(
        sctid="26703600712",
        fully_specified_name="Dyspnea, subcategory 12 (finding)",
        preferred_term="Dyspnea subcategory 12",
        semantic_tag="finding"
    ),
    "26703600713": SNOMEDConcept(
        sctid="26703600713",
        fully_specified_name="Dyspnea, subcategory 13 (finding)",
        preferred_term="Dyspnea subcategory 13",
        semantic_tag="finding"
    ),
    "26703600714": SNOMEDConcept(
        sctid="26703600714",
        fully_specified_name="Dyspnea, subcategory 14 (finding)",
        preferred_term="Dyspnea subcategory 14",
        semantic_tag="finding"
    ),
    "29857009": SNOMEDConcept(
        sctid="29857009",
        fully_specified_name="Chest pain (finding)",
        preferred_term="Chest pain",
        semantic_tag="finding"
    ),
    "2985700901": SNOMEDConcept(
        sctid="2985700901",
        fully_specified_name="Chest pain, subcategory 1 (finding)",
        preferred_term="Chest pain subcategory 1",
        semantic_tag="finding"
    ),
    "2985700902": SNOMEDConcept(
        sctid="2985700902",
        fully_specified_name="Chest pain, subcategory 2 (finding)",
        preferred_term="Chest pain subcategory 2",
        semantic_tag="finding"
    ),
    "2985700903": SNOMEDConcept(
        sctid="2985700903",
        fully_specified_name="Chest pain, subcategory 3 (finding)",
        preferred_term="Chest pain subcategory 3",
        semantic_tag="finding"
    ),
    "2985700904": SNOMEDConcept(
        sctid="2985700904",
        fully_specified_name="Chest pain, subcategory 4 (finding)",
        preferred_term="Chest pain subcategory 4",
        semantic_tag="finding"
    ),
    "2985700905": SNOMEDConcept(
        sctid="2985700905",
        fully_specified_name="Chest pain, subcategory 5 (finding)",
        preferred_term="Chest pain subcategory 5",
        semantic_tag="finding"
    ),
    "2985700906": SNOMEDConcept(
        sctid="2985700906",
        fully_specified_name="Chest pain, subcategory 6 (finding)",
        preferred_term="Chest pain subcategory 6",
        semantic_tag="finding"
    ),
    "2985700907": SNOMEDConcept(
        sctid="2985700907",
        fully_specified_name="Chest pain, subcategory 7 (finding)",
        preferred_term="Chest pain subcategory 7",
        semantic_tag="finding"
    ),
    "2985700908": SNOMEDConcept(
        sctid="2985700908",
        fully_specified_name="Chest pain, subcategory 8 (finding)",
        preferred_term="Chest pain subcategory 8",
        semantic_tag="finding"
    ),
    "2985700909": SNOMEDConcept(
        sctid="2985700909",
        fully_specified_name="Chest pain, subcategory 9 (finding)",
        preferred_term="Chest pain subcategory 9",
        semantic_tag="finding"
    ),
    "2985700910": SNOMEDConcept(
        sctid="2985700910",
        fully_specified_name="Chest pain, subcategory 10 (finding)",
        preferred_term="Chest pain subcategory 10",
        semantic_tag="finding"
    ),
    "2985700911": SNOMEDConcept(
        sctid="2985700911",
        fully_specified_name="Chest pain, subcategory 11 (finding)",
        preferred_term="Chest pain subcategory 11",
        semantic_tag="finding"
    ),
    "2985700912": SNOMEDConcept(
        sctid="2985700912",
        fully_specified_name="Chest pain, subcategory 12 (finding)",
        preferred_term="Chest pain subcategory 12",
        semantic_tag="finding"
    ),
    "2985700913": SNOMEDConcept(
        sctid="2985700913",
        fully_specified_name="Chest pain, subcategory 13 (finding)",
        preferred_term="Chest pain subcategory 13",
        semantic_tag="finding"
    ),
    "2985700914": SNOMEDConcept(
        sctid="2985700914",
        fully_specified_name="Chest pain, subcategory 14 (finding)",
        preferred_term="Chest pain subcategory 14",
        semantic_tag="finding"
    ),
    "422400008": SNOMEDConcept(
        sctid="422400008",
        fully_specified_name="Vomiting (finding)",
        preferred_term="Vomiting",
        semantic_tag="finding"
    ),
    "42240000801": SNOMEDConcept(
        sctid="42240000801",
        fully_specified_name="Vomiting, subcategory 1 (finding)",
        preferred_term="Vomiting subcategory 1",
        semantic_tag="finding"
    ),
    "42240000802": SNOMEDConcept(
        sctid="42240000802",
        fully_specified_name="Vomiting, subcategory 2 (finding)",
        preferred_term="Vomiting subcategory 2",
        semantic_tag="finding"
    ),
    "42240000803": SNOMEDConcept(
        sctid="42240000803",
        fully_specified_name="Vomiting, subcategory 3 (finding)",
        preferred_term="Vomiting subcategory 3",
        semantic_tag="finding"
    ),
    "42240000804": SNOMEDConcept(
        sctid="42240000804",
        fully_specified_name="Vomiting, subcategory 4 (finding)",
        preferred_term="Vomiting subcategory 4",
        semantic_tag="finding"
    ),
    "42240000805": SNOMEDConcept(
        sctid="42240000805",
        fully_specified_name="Vomiting, subcategory 5 (finding)",
        preferred_term="Vomiting subcategory 5",
        semantic_tag="finding"
    ),
    "42240000806": SNOMEDConcept(
        sctid="42240000806",
        fully_specified_name="Vomiting, subcategory 6 (finding)",
        preferred_term="Vomiting subcategory 6",
        semantic_tag="finding"
    ),
    "42240000807": SNOMEDConcept(
        sctid="42240000807",
        fully_specified_name="Vomiting, subcategory 7 (finding)",
        preferred_term="Vomiting subcategory 7",
        semantic_tag="finding"
    ),
    "42240000808": SNOMEDConcept(
        sctid="42240000808",
        fully_specified_name="Vomiting, subcategory 8 (finding)",
        preferred_term="Vomiting subcategory 8",
        semantic_tag="finding"
    ),
    "42240000809": SNOMEDConcept(
        sctid="42240000809",
        fully_specified_name="Vomiting, subcategory 9 (finding)",
        preferred_term="Vomiting subcategory 9",
        semantic_tag="finding"
    ),
    "42240000810": SNOMEDConcept(
        sctid="42240000810",
        fully_specified_name="Vomiting, subcategory 10 (finding)",
        preferred_term="Vomiting subcategory 10",
        semantic_tag="finding"
    ),
    "42240000811": SNOMEDConcept(
        sctid="42240000811",
        fully_specified_name="Vomiting, subcategory 11 (finding)",
        preferred_term="Vomiting subcategory 11",
        semantic_tag="finding"
    ),
    "42240000812": SNOMEDConcept(
        sctid="42240000812",
        fully_specified_name="Vomiting, subcategory 12 (finding)",
        preferred_term="Vomiting subcategory 12",
        semantic_tag="finding"
    ),
    "42240000813": SNOMEDConcept(
        sctid="42240000813",
        fully_specified_name="Vomiting, subcategory 13 (finding)",
        preferred_term="Vomiting subcategory 13",
        semantic_tag="finding"
    ),
    "42240000814": SNOMEDConcept(
        sctid="42240000814",
        fully_specified_name="Vomiting, subcategory 14 (finding)",
        preferred_term="Vomiting subcategory 14",
        semantic_tag="finding"
    ),
    "62315008": SNOMEDConcept(
        sctid="62315008",
        fully_specified_name="Diarrhea (finding)",
        preferred_term="Diarrhea",
        semantic_tag="finding"
    ),
    "6231500801": SNOMEDConcept(
        sctid="6231500801",
        fully_specified_name="Diarrhea, subcategory 1 (finding)",
        preferred_term="Diarrhea subcategory 1",
        semantic_tag="finding"
    ),
    "6231500802": SNOMEDConcept(
        sctid="6231500802",
        fully_specified_name="Diarrhea, subcategory 2 (finding)",
        preferred_term="Diarrhea subcategory 2",
        semantic_tag="finding"
    ),
    "6231500803": SNOMEDConcept(
        sctid="6231500803",
        fully_specified_name="Diarrhea, subcategory 3 (finding)",
        preferred_term="Diarrhea subcategory 3",
        semantic_tag="finding"
    ),
    "6231500804": SNOMEDConcept(
        sctid="6231500804",
        fully_specified_name="Diarrhea, subcategory 4 (finding)",
        preferred_term="Diarrhea subcategory 4",
        semantic_tag="finding"
    ),
    "6231500805": SNOMEDConcept(
        sctid="6231500805",
        fully_specified_name="Diarrhea, subcategory 5 (finding)",
        preferred_term="Diarrhea subcategory 5",
        semantic_tag="finding"
    ),
    "6231500806": SNOMEDConcept(
        sctid="6231500806",
        fully_specified_name="Diarrhea, subcategory 6 (finding)",
        preferred_term="Diarrhea subcategory 6",
        semantic_tag="finding"
    ),
    "6231500807": SNOMEDConcept(
        sctid="6231500807",
        fully_specified_name="Diarrhea, subcategory 7 (finding)",
        preferred_term="Diarrhea subcategory 7",
        semantic_tag="finding"
    ),
    "6231500808": SNOMEDConcept(
        sctid="6231500808",
        fully_specified_name="Diarrhea, subcategory 8 (finding)",
        preferred_term="Diarrhea subcategory 8",
        semantic_tag="finding"
    ),
    "6231500809": SNOMEDConcept(
        sctid="6231500809",
        fully_specified_name="Diarrhea, subcategory 9 (finding)",
        preferred_term="Diarrhea subcategory 9",
        semantic_tag="finding"
    ),
    "6231500810": SNOMEDConcept(
        sctid="6231500810",
        fully_specified_name="Diarrhea, subcategory 10 (finding)",
        preferred_term="Diarrhea subcategory 10",
        semantic_tag="finding"
    ),
    "6231500811": SNOMEDConcept(
        sctid="6231500811",
        fully_specified_name="Diarrhea, subcategory 11 (finding)",
        preferred_term="Diarrhea subcategory 11",
        semantic_tag="finding"
    ),
    "6231500812": SNOMEDConcept(
        sctid="6231500812",
        fully_specified_name="Diarrhea, subcategory 12 (finding)",
        preferred_term="Diarrhea subcategory 12",
        semantic_tag="finding"
    ),
    "6231500813": SNOMEDConcept(
        sctid="6231500813",
        fully_specified_name="Diarrhea, subcategory 13 (finding)",
        preferred_term="Diarrhea subcategory 13",
        semantic_tag="finding"
    ),
    "6231500814": SNOMEDConcept(
        sctid="6231500814",
        fully_specified_name="Diarrhea, subcategory 14 (finding)",
        preferred_term="Diarrhea subcategory 14",
        semantic_tag="finding"
    ),
    "422587007": SNOMEDConcept(
        sctid="422587007",
        fully_specified_name="Nausea (finding)",
        preferred_term="Nausea",
        semantic_tag="finding"
    ),
    "42258700701": SNOMEDConcept(
        sctid="42258700701",
        fully_specified_name="Nausea, subcategory 1 (finding)",
        preferred_term="Nausea subcategory 1",
        semantic_tag="finding"
    ),
    "42258700702": SNOMEDConcept(
        sctid="42258700702",
        fully_specified_name="Nausea, subcategory 2 (finding)",
        preferred_term="Nausea subcategory 2",
        semantic_tag="finding"
    ),
    "42258700703": SNOMEDConcept(
        sctid="42258700703",
        fully_specified_name="Nausea, subcategory 3 (finding)",
        preferred_term="Nausea subcategory 3",
        semantic_tag="finding"
    ),
    "42258700704": SNOMEDConcept(
        sctid="42258700704",
        fully_specified_name="Nausea, subcategory 4 (finding)",
        preferred_term="Nausea subcategory 4",
        semantic_tag="finding"
    ),
    "42258700705": SNOMEDConcept(
        sctid="42258700705",
        fully_specified_name="Nausea, subcategory 5 (finding)",
        preferred_term="Nausea subcategory 5",
        semantic_tag="finding"
    ),
    "42258700706": SNOMEDConcept(
        sctid="42258700706",
        fully_specified_name="Nausea, subcategory 6 (finding)",
        preferred_term="Nausea subcategory 6",
        semantic_tag="finding"
    ),
    "42258700707": SNOMEDConcept(
        sctid="42258700707",
        fully_specified_name="Nausea, subcategory 7 (finding)",
        preferred_term="Nausea subcategory 7",
        semantic_tag="finding"
    ),
    "42258700708": SNOMEDConcept(
        sctid="42258700708",
        fully_specified_name="Nausea, subcategory 8 (finding)",
        preferred_term="Nausea subcategory 8",
        semantic_tag="finding"
    ),
    "42258700709": SNOMEDConcept(
        sctid="42258700709",
        fully_specified_name="Nausea, subcategory 9 (finding)",
        preferred_term="Nausea subcategory 9",
        semantic_tag="finding"
    ),
    "42258700710": SNOMEDConcept(
        sctid="42258700710",
        fully_specified_name="Nausea, subcategory 10 (finding)",
        preferred_term="Nausea subcategory 10",
        semantic_tag="finding"
    ),
    "42258700711": SNOMEDConcept(
        sctid="42258700711",
        fully_specified_name="Nausea, subcategory 11 (finding)",
        preferred_term="Nausea subcategory 11",
        semantic_tag="finding"
    ),
    "42258700712": SNOMEDConcept(
        sctid="42258700712",
        fully_specified_name="Nausea, subcategory 12 (finding)",
        preferred_term="Nausea subcategory 12",
        semantic_tag="finding"
    ),
    "42258700713": SNOMEDConcept(
        sctid="42258700713",
        fully_specified_name="Nausea, subcategory 13 (finding)",
        preferred_term="Nausea subcategory 13",
        semantic_tag="finding"
    ),
    "42258700714": SNOMEDConcept(
        sctid="42258700714",
        fully_specified_name="Nausea, subcategory 14 (finding)",
        preferred_term="Nausea subcategory 14",
        semantic_tag="finding"
    ),
    "82272006": SNOMEDConcept(
        sctid="82272006",
        fully_specified_name="Common cold (disorder)",
        preferred_term="Common cold",
        semantic_tag="disorder"
    ),
    "8227200601": SNOMEDConcept(
        sctid="8227200601",
        fully_specified_name="Common cold, subcategory 1 (disorder)",
        preferred_term="Common cold subcategory 1",
        semantic_tag="disorder"
    ),
    "8227200602": SNOMEDConcept(
        sctid="8227200602",
        fully_specified_name="Common cold, subcategory 2 (disorder)",
        preferred_term="Common cold subcategory 2",
        semantic_tag="disorder"
    ),
    "8227200603": SNOMEDConcept(
        sctid="8227200603",
        fully_specified_name="Common cold, subcategory 3 (disorder)",
        preferred_term="Common cold subcategory 3",
        semantic_tag="disorder"
    ),
    "8227200604": SNOMEDConcept(
        sctid="8227200604",
        fully_specified_name="Common cold, subcategory 4 (disorder)",
        preferred_term="Common cold subcategory 4",
        semantic_tag="disorder"
    ),
    "8227200605": SNOMEDConcept(
        sctid="8227200605",
        fully_specified_name="Common cold, subcategory 5 (disorder)",
        preferred_term="Common cold subcategory 5",
        semantic_tag="disorder"
    ),
    "8227200606": SNOMEDConcept(
        sctid="8227200606",
        fully_specified_name="Common cold, subcategory 6 (disorder)",
        preferred_term="Common cold subcategory 6",
        semantic_tag="disorder"
    ),
    "8227200607": SNOMEDConcept(
        sctid="8227200607",
        fully_specified_name="Common cold, subcategory 7 (disorder)",
        preferred_term="Common cold subcategory 7",
        semantic_tag="disorder"
    ),
    "8227200608": SNOMEDConcept(
        sctid="8227200608",
        fully_specified_name="Common cold, subcategory 8 (disorder)",
        preferred_term="Common cold subcategory 8",
        semantic_tag="disorder"
    ),
    "8227200609": SNOMEDConcept(
        sctid="8227200609",
        fully_specified_name="Common cold, subcategory 9 (disorder)",
        preferred_term="Common cold subcategory 9",
        semantic_tag="disorder"
    ),
    "8227200610": SNOMEDConcept(
        sctid="8227200610",
        fully_specified_name="Common cold, subcategory 10 (disorder)",
        preferred_term="Common cold subcategory 10",
        semantic_tag="disorder"
    ),
    "8227200611": SNOMEDConcept(
        sctid="8227200611",
        fully_specified_name="Common cold, subcategory 11 (disorder)",
        preferred_term="Common cold subcategory 11",
        semantic_tag="disorder"
    ),
    "8227200612": SNOMEDConcept(
        sctid="8227200612",
        fully_specified_name="Common cold, subcategory 12 (disorder)",
        preferred_term="Common cold subcategory 12",
        semantic_tag="disorder"
    ),
    "8227200613": SNOMEDConcept(
        sctid="8227200613",
        fully_specified_name="Common cold, subcategory 13 (disorder)",
        preferred_term="Common cold subcategory 13",
        semantic_tag="disorder"
    ),
    "8227200614": SNOMEDConcept(
        sctid="8227200614",
        fully_specified_name="Common cold, subcategory 14 (disorder)",
        preferred_term="Common cold subcategory 14",
        semantic_tag="disorder"
    ),
    "10509002": SNOMEDConcept(
        sctid="10509002",
        fully_specified_name="Acute bronchitis (disorder)",
        preferred_term="Acute bronchitis",
        semantic_tag="disorder"
    ),
    "1050900201": SNOMEDConcept(
        sctid="1050900201",
        fully_specified_name="Acute bronchitis, subcategory 1 (disorder)",
        preferred_term="Acute bronchitis subcategory 1",
        semantic_tag="disorder"
    ),
    "1050900202": SNOMEDConcept(
        sctid="1050900202",
        fully_specified_name="Acute bronchitis, subcategory 2 (disorder)",
        preferred_term="Acute bronchitis subcategory 2",
        semantic_tag="disorder"
    ),
    "1050900203": SNOMEDConcept(
        sctid="1050900203",
        fully_specified_name="Acute bronchitis, subcategory 3 (disorder)",
        preferred_term="Acute bronchitis subcategory 3",
        semantic_tag="disorder"
    ),
    "1050900204": SNOMEDConcept(
        sctid="1050900204",
        fully_specified_name="Acute bronchitis, subcategory 4 (disorder)",
        preferred_term="Acute bronchitis subcategory 4",
        semantic_tag="disorder"
    ),
    "1050900205": SNOMEDConcept(
        sctid="1050900205",
        fully_specified_name="Acute bronchitis, subcategory 5 (disorder)",
        preferred_term="Acute bronchitis subcategory 5",
        semantic_tag="disorder"
    ),
    "1050900206": SNOMEDConcept(
        sctid="1050900206",
        fully_specified_name="Acute bronchitis, subcategory 6 (disorder)",
        preferred_term="Acute bronchitis subcategory 6",
        semantic_tag="disorder"
    ),
    "1050900207": SNOMEDConcept(
        sctid="1050900207",
        fully_specified_name="Acute bronchitis, subcategory 7 (disorder)",
        preferred_term="Acute bronchitis subcategory 7",
        semantic_tag="disorder"
    ),
    "1050900208": SNOMEDConcept(
        sctid="1050900208",
        fully_specified_name="Acute bronchitis, subcategory 8 (disorder)",
        preferred_term="Acute bronchitis subcategory 8",
        semantic_tag="disorder"
    ),
    "1050900209": SNOMEDConcept(
        sctid="1050900209",
        fully_specified_name="Acute bronchitis, subcategory 9 (disorder)",
        preferred_term="Acute bronchitis subcategory 9",
        semantic_tag="disorder"
    ),
    "1050900210": SNOMEDConcept(
        sctid="1050900210",
        fully_specified_name="Acute bronchitis, subcategory 10 (disorder)",
        preferred_term="Acute bronchitis subcategory 10",
        semantic_tag="disorder"
    ),
    "1050900211": SNOMEDConcept(
        sctid="1050900211",
        fully_specified_name="Acute bronchitis, subcategory 11 (disorder)",
        preferred_term="Acute bronchitis subcategory 11",
        semantic_tag="disorder"
    ),
    "1050900212": SNOMEDConcept(
        sctid="1050900212",
        fully_specified_name="Acute bronchitis, subcategory 12 (disorder)",
        preferred_term="Acute bronchitis subcategory 12",
        semantic_tag="disorder"
    ),
    "1050900213": SNOMEDConcept(
        sctid="1050900213",
        fully_specified_name="Acute bronchitis, subcategory 13 (disorder)",
        preferred_term="Acute bronchitis subcategory 13",
        semantic_tag="disorder"
    ),
    "1050900214": SNOMEDConcept(
        sctid="1050900214",
        fully_specified_name="Acute bronchitis, subcategory 14 (disorder)",
        preferred_term="Acute bronchitis subcategory 14",
        semantic_tag="disorder"
    ),
    "233604007": SNOMEDConcept(
        sctid="233604007",
        fully_specified_name="Pneumonia (disorder)",
        preferred_term="Pneumonia",
        semantic_tag="disorder"
    ),
    "23360400701": SNOMEDConcept(
        sctid="23360400701",
        fully_specified_name="Pneumonia, subcategory 1 (disorder)",
        preferred_term="Pneumonia subcategory 1",
        semantic_tag="disorder"
    ),
    "23360400702": SNOMEDConcept(
        sctid="23360400702",
        fully_specified_name="Pneumonia, subcategory 2 (disorder)",
        preferred_term="Pneumonia subcategory 2",
        semantic_tag="disorder"
    ),
    "23360400703": SNOMEDConcept(
        sctid="23360400703",
        fully_specified_name="Pneumonia, subcategory 3 (disorder)",
        preferred_term="Pneumonia subcategory 3",
        semantic_tag="disorder"
    ),
    "23360400704": SNOMEDConcept(
        sctid="23360400704",
        fully_specified_name="Pneumonia, subcategory 4 (disorder)",
        preferred_term="Pneumonia subcategory 4",
        semantic_tag="disorder"
    ),
    "23360400705": SNOMEDConcept(
        sctid="23360400705",
        fully_specified_name="Pneumonia, subcategory 5 (disorder)",
        preferred_term="Pneumonia subcategory 5",
        semantic_tag="disorder"
    ),
    "23360400706": SNOMEDConcept(
        sctid="23360400706",
        fully_specified_name="Pneumonia, subcategory 6 (disorder)",
        preferred_term="Pneumonia subcategory 6",
        semantic_tag="disorder"
    ),
    "23360400707": SNOMEDConcept(
        sctid="23360400707",
        fully_specified_name="Pneumonia, subcategory 7 (disorder)",
        preferred_term="Pneumonia subcategory 7",
        semantic_tag="disorder"
    ),
    "23360400708": SNOMEDConcept(
        sctid="23360400708",
        fully_specified_name="Pneumonia, subcategory 8 (disorder)",
        preferred_term="Pneumonia subcategory 8",
        semantic_tag="disorder"
    ),
    "23360400709": SNOMEDConcept(
        sctid="23360400709",
        fully_specified_name="Pneumonia, subcategory 9 (disorder)",
        preferred_term="Pneumonia subcategory 9",
        semantic_tag="disorder"
    ),
    "23360400710": SNOMEDConcept(
        sctid="23360400710",
        fully_specified_name="Pneumonia, subcategory 10 (disorder)",
        preferred_term="Pneumonia subcategory 10",
        semantic_tag="disorder"
    ),
    "23360400711": SNOMEDConcept(
        sctid="23360400711",
        fully_specified_name="Pneumonia, subcategory 11 (disorder)",
        preferred_term="Pneumonia subcategory 11",
        semantic_tag="disorder"
    ),
    "23360400712": SNOMEDConcept(
        sctid="23360400712",
        fully_specified_name="Pneumonia, subcategory 12 (disorder)",
        preferred_term="Pneumonia subcategory 12",
        semantic_tag="disorder"
    ),
    "23360400713": SNOMEDConcept(
        sctid="23360400713",
        fully_specified_name="Pneumonia, subcategory 13 (disorder)",
        preferred_term="Pneumonia subcategory 13",
        semantic_tag="disorder"
    ),
    "23360400714": SNOMEDConcept(
        sctid="23360400714",
        fully_specified_name="Pneumonia, subcategory 14 (disorder)",
        preferred_term="Pneumonia subcategory 14",
        semantic_tag="disorder"
    ),
    "80146002": SNOMEDConcept(
        sctid="80146002",
        fully_specified_name="Appendectomy (procedure)",
        preferred_term="Appendectomy",
        semantic_tag="procedure"
    ),
    "8014600201": SNOMEDConcept(
        sctid="8014600201",
        fully_specified_name="Appendectomy, subcategory 1 (procedure)",
        preferred_term="Appendectomy subcategory 1",
        semantic_tag="procedure"
    ),
    "8014600202": SNOMEDConcept(
        sctid="8014600202",
        fully_specified_name="Appendectomy, subcategory 2 (procedure)",
        preferred_term="Appendectomy subcategory 2",
        semantic_tag="procedure"
    ),
    "8014600203": SNOMEDConcept(
        sctid="8014600203",
        fully_specified_name="Appendectomy, subcategory 3 (procedure)",
        preferred_term="Appendectomy subcategory 3",
        semantic_tag="procedure"
    ),
    "8014600204": SNOMEDConcept(
        sctid="8014600204",
        fully_specified_name="Appendectomy, subcategory 4 (procedure)",
        preferred_term="Appendectomy subcategory 4",
        semantic_tag="procedure"
    ),
    "8014600205": SNOMEDConcept(
        sctid="8014600205",
        fully_specified_name="Appendectomy, subcategory 5 (procedure)",
        preferred_term="Appendectomy subcategory 5",
        semantic_tag="procedure"
    ),
    "8014600206": SNOMEDConcept(
        sctid="8014600206",
        fully_specified_name="Appendectomy, subcategory 6 (procedure)",
        preferred_term="Appendectomy subcategory 6",
        semantic_tag="procedure"
    ),
    "8014600207": SNOMEDConcept(
        sctid="8014600207",
        fully_specified_name="Appendectomy, subcategory 7 (procedure)",
        preferred_term="Appendectomy subcategory 7",
        semantic_tag="procedure"
    ),
    "8014600208": SNOMEDConcept(
        sctid="8014600208",
        fully_specified_name="Appendectomy, subcategory 8 (procedure)",
        preferred_term="Appendectomy subcategory 8",
        semantic_tag="procedure"
    ),
    "8014600209": SNOMEDConcept(
        sctid="8014600209",
        fully_specified_name="Appendectomy, subcategory 9 (procedure)",
        preferred_term="Appendectomy subcategory 9",
        semantic_tag="procedure"
    ),
    "8014600210": SNOMEDConcept(
        sctid="8014600210",
        fully_specified_name="Appendectomy, subcategory 10 (procedure)",
        preferred_term="Appendectomy subcategory 10",
        semantic_tag="procedure"
    ),
    "8014600211": SNOMEDConcept(
        sctid="8014600211",
        fully_specified_name="Appendectomy, subcategory 11 (procedure)",
        preferred_term="Appendectomy subcategory 11",
        semantic_tag="procedure"
    ),
    "8014600212": SNOMEDConcept(
        sctid="8014600212",
        fully_specified_name="Appendectomy, subcategory 12 (procedure)",
        preferred_term="Appendectomy subcategory 12",
        semantic_tag="procedure"
    ),
    "8014600213": SNOMEDConcept(
        sctid="8014600213",
        fully_specified_name="Appendectomy, subcategory 13 (procedure)",
        preferred_term="Appendectomy subcategory 13",
        semantic_tag="procedure"
    ),
    "8014600214": SNOMEDConcept(
        sctid="8014600214",
        fully_specified_name="Appendectomy, subcategory 14 (procedure)",
        preferred_term="Appendectomy subcategory 14",
        semantic_tag="procedure"
    ),
    "172043006": SNOMEDConcept(
        sctid="172043006",
        fully_specified_name="Coronary artery bypass graft (procedure)",
        preferred_term="Coronary artery bypass graft",
        semantic_tag="procedure"
    ),
    "17204300601": SNOMEDConcept(
        sctid="17204300601",
        fully_specified_name="Coronary artery bypass graft, subcategory 1 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 1",
        semantic_tag="procedure"
    ),
    "17204300602": SNOMEDConcept(
        sctid="17204300602",
        fully_specified_name="Coronary artery bypass graft, subcategory 2 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 2",
        semantic_tag="procedure"
    ),
    "17204300603": SNOMEDConcept(
        sctid="17204300603",
        fully_specified_name="Coronary artery bypass graft, subcategory 3 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 3",
        semantic_tag="procedure"
    ),
    "17204300604": SNOMEDConcept(
        sctid="17204300604",
        fully_specified_name="Coronary artery bypass graft, subcategory 4 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 4",
        semantic_tag="procedure"
    ),
    "17204300605": SNOMEDConcept(
        sctid="17204300605",
        fully_specified_name="Coronary artery bypass graft, subcategory 5 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 5",
        semantic_tag="procedure"
    ),
    "17204300606": SNOMEDConcept(
        sctid="17204300606",
        fully_specified_name="Coronary artery bypass graft, subcategory 6 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 6",
        semantic_tag="procedure"
    ),
    "17204300607": SNOMEDConcept(
        sctid="17204300607",
        fully_specified_name="Coronary artery bypass graft, subcategory 7 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 7",
        semantic_tag="procedure"
    ),
    "17204300608": SNOMEDConcept(
        sctid="17204300608",
        fully_specified_name="Coronary artery bypass graft, subcategory 8 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 8",
        semantic_tag="procedure"
    ),
    "17204300609": SNOMEDConcept(
        sctid="17204300609",
        fully_specified_name="Coronary artery bypass graft, subcategory 9 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 9",
        semantic_tag="procedure"
    ),
    "17204300610": SNOMEDConcept(
        sctid="17204300610",
        fully_specified_name="Coronary artery bypass graft, subcategory 10 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 10",
        semantic_tag="procedure"
    ),
    "17204300611": SNOMEDConcept(
        sctid="17204300611",
        fully_specified_name="Coronary artery bypass graft, subcategory 11 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 11",
        semantic_tag="procedure"
    ),
    "17204300612": SNOMEDConcept(
        sctid="17204300612",
        fully_specified_name="Coronary artery bypass graft, subcategory 12 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 12",
        semantic_tag="procedure"
    ),
    "17204300613": SNOMEDConcept(
        sctid="17204300613",
        fully_specified_name="Coronary artery bypass graft, subcategory 13 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 13",
        semantic_tag="procedure"
    ),
    "17204300614": SNOMEDConcept(
        sctid="17204300614",
        fully_specified_name="Coronary artery bypass graft, subcategory 14 (procedure)",
        preferred_term="Coronary artery bypass graft subcategory 14",
        semantic_tag="procedure"
    ),
    "232717009": SNOMEDConcept(
        sctid="232717009",
        fully_specified_name="Percutaneous coronary intervention (procedure)",
        preferred_term="Percutaneous coronary intervention",
        semantic_tag="procedure"
    ),
    "23271700901": SNOMEDConcept(
        sctid="23271700901",
        fully_specified_name="Percutaneous coronary intervention, subcategory 1 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 1",
        semantic_tag="procedure"
    ),
    "23271700902": SNOMEDConcept(
        sctid="23271700902",
        fully_specified_name="Percutaneous coronary intervention, subcategory 2 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 2",
        semantic_tag="procedure"
    ),
    "23271700903": SNOMEDConcept(
        sctid="23271700903",
        fully_specified_name="Percutaneous coronary intervention, subcategory 3 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 3",
        semantic_tag="procedure"
    ),
    "23271700904": SNOMEDConcept(
        sctid="23271700904",
        fully_specified_name="Percutaneous coronary intervention, subcategory 4 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 4",
        semantic_tag="procedure"
    ),
    "23271700905": SNOMEDConcept(
        sctid="23271700905",
        fully_specified_name="Percutaneous coronary intervention, subcategory 5 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 5",
        semantic_tag="procedure"
    ),
    "23271700906": SNOMEDConcept(
        sctid="23271700906",
        fully_specified_name="Percutaneous coronary intervention, subcategory 6 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 6",
        semantic_tag="procedure"
    ),
    "23271700907": SNOMEDConcept(
        sctid="23271700907",
        fully_specified_name="Percutaneous coronary intervention, subcategory 7 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 7",
        semantic_tag="procedure"
    ),
    "23271700908": SNOMEDConcept(
        sctid="23271700908",
        fully_specified_name="Percutaneous coronary intervention, subcategory 8 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 8",
        semantic_tag="procedure"
    ),
    "23271700909": SNOMEDConcept(
        sctid="23271700909",
        fully_specified_name="Percutaneous coronary intervention, subcategory 9 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 9",
        semantic_tag="procedure"
    ),
    "23271700910": SNOMEDConcept(
        sctid="23271700910",
        fully_specified_name="Percutaneous coronary intervention, subcategory 10 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 10",
        semantic_tag="procedure"
    ),
    "23271700911": SNOMEDConcept(
        sctid="23271700911",
        fully_specified_name="Percutaneous coronary intervention, subcategory 11 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 11",
        semantic_tag="procedure"
    ),
    "23271700912": SNOMEDConcept(
        sctid="23271700912",
        fully_specified_name="Percutaneous coronary intervention, subcategory 12 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 12",
        semantic_tag="procedure"
    ),
    "23271700913": SNOMEDConcept(
        sctid="23271700913",
        fully_specified_name="Percutaneous coronary intervention, subcategory 13 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 13",
        semantic_tag="procedure"
    ),
    "23271700914": SNOMEDConcept(
        sctid="23271700914",
        fully_specified_name="Percutaneous coronary intervention, subcategory 14 (procedure)",
        preferred_term="Percutaneous coronary intervention subcategory 14",
        semantic_tag="procedure"
    ),
    "52734007": SNOMEDConcept(
        sctid="52734007",
        fully_specified_name="Total hip replacement (procedure)",
        preferred_term="Total hip replacement",
        semantic_tag="procedure"
    ),
    "5273400701": SNOMEDConcept(
        sctid="5273400701",
        fully_specified_name="Total hip replacement, subcategory 1 (procedure)",
        preferred_term="Total hip replacement subcategory 1",
        semantic_tag="procedure"
    ),
    "5273400702": SNOMEDConcept(
        sctid="5273400702",
        fully_specified_name="Total hip replacement, subcategory 2 (procedure)",
        preferred_term="Total hip replacement subcategory 2",
        semantic_tag="procedure"
    ),
    "5273400703": SNOMEDConcept(
        sctid="5273400703",
        fully_specified_name="Total hip replacement, subcategory 3 (procedure)",
        preferred_term="Total hip replacement subcategory 3",
        semantic_tag="procedure"
    ),
    "5273400704": SNOMEDConcept(
        sctid="5273400704",
        fully_specified_name="Total hip replacement, subcategory 4 (procedure)",
        preferred_term="Total hip replacement subcategory 4",
        semantic_tag="procedure"
    ),
    "5273400705": SNOMEDConcept(
        sctid="5273400705",
        fully_specified_name="Total hip replacement, subcategory 5 (procedure)",
        preferred_term="Total hip replacement subcategory 5",
        semantic_tag="procedure"
    ),
    "5273400706": SNOMEDConcept(
        sctid="5273400706",
        fully_specified_name="Total hip replacement, subcategory 6 (procedure)",
        preferred_term="Total hip replacement subcategory 6",
        semantic_tag="procedure"
    ),
    "5273400707": SNOMEDConcept(
        sctid="5273400707",
        fully_specified_name="Total hip replacement, subcategory 7 (procedure)",
        preferred_term="Total hip replacement subcategory 7",
        semantic_tag="procedure"
    ),
    "5273400708": SNOMEDConcept(
        sctid="5273400708",
        fully_specified_name="Total hip replacement, subcategory 8 (procedure)",
        preferred_term="Total hip replacement subcategory 8",
        semantic_tag="procedure"
    ),
    "5273400709": SNOMEDConcept(
        sctid="5273400709",
        fully_specified_name="Total hip replacement, subcategory 9 (procedure)",
        preferred_term="Total hip replacement subcategory 9",
        semantic_tag="procedure"
    ),
    "5273400710": SNOMEDConcept(
        sctid="5273400710",
        fully_specified_name="Total hip replacement, subcategory 10 (procedure)",
        preferred_term="Total hip replacement subcategory 10",
        semantic_tag="procedure"
    ),
    "5273400711": SNOMEDConcept(
        sctid="5273400711",
        fully_specified_name="Total hip replacement, subcategory 11 (procedure)",
        preferred_term="Total hip replacement subcategory 11",
        semantic_tag="procedure"
    ),
    "5273400712": SNOMEDConcept(
        sctid="5273400712",
        fully_specified_name="Total hip replacement, subcategory 12 (procedure)",
        preferred_term="Total hip replacement subcategory 12",
        semantic_tag="procedure"
    ),
    "5273400713": SNOMEDConcept(
        sctid="5273400713",
        fully_specified_name="Total hip replacement, subcategory 13 (procedure)",
        preferred_term="Total hip replacement subcategory 13",
        semantic_tag="procedure"
    ),
    "5273400714": SNOMEDConcept(
        sctid="5273400714",
        fully_specified_name="Total hip replacement, subcategory 14 (procedure)",
        preferred_term="Total hip replacement subcategory 14",
        semantic_tag="procedure"
    ),
    "392021009": SNOMEDConcept(
        sctid="392021009",
        fully_specified_name="Lumbar puncture (procedure)",
        preferred_term="Lumbar puncture",
        semantic_tag="procedure"
    ),
    "39202100901": SNOMEDConcept(
        sctid="39202100901",
        fully_specified_name="Lumbar puncture, subcategory 1 (procedure)",
        preferred_term="Lumbar puncture subcategory 1",
        semantic_tag="procedure"
    ),
    "39202100902": SNOMEDConcept(
        sctid="39202100902",
        fully_specified_name="Lumbar puncture, subcategory 2 (procedure)",
        preferred_term="Lumbar puncture subcategory 2",
        semantic_tag="procedure"
    ),
    "39202100903": SNOMEDConcept(
        sctid="39202100903",
        fully_specified_name="Lumbar puncture, subcategory 3 (procedure)",
        preferred_term="Lumbar puncture subcategory 3",
        semantic_tag="procedure"
    ),
    "39202100904": SNOMEDConcept(
        sctid="39202100904",
        fully_specified_name="Lumbar puncture, subcategory 4 (procedure)",
        preferred_term="Lumbar puncture subcategory 4",
        semantic_tag="procedure"
    ),
    "39202100905": SNOMEDConcept(
        sctid="39202100905",
        fully_specified_name="Lumbar puncture, subcategory 5 (procedure)",
        preferred_term="Lumbar puncture subcategory 5",
        semantic_tag="procedure"
    ),
    "39202100906": SNOMEDConcept(
        sctid="39202100906",
        fully_specified_name="Lumbar puncture, subcategory 6 (procedure)",
        preferred_term="Lumbar puncture subcategory 6",
        semantic_tag="procedure"
    ),
    "39202100907": SNOMEDConcept(
        sctid="39202100907",
        fully_specified_name="Lumbar puncture, subcategory 7 (procedure)",
        preferred_term="Lumbar puncture subcategory 7",
        semantic_tag="procedure"
    ),
    "39202100908": SNOMEDConcept(
        sctid="39202100908",
        fully_specified_name="Lumbar puncture, subcategory 8 (procedure)",
        preferred_term="Lumbar puncture subcategory 8",
        semantic_tag="procedure"
    ),
    "39202100909": SNOMEDConcept(
        sctid="39202100909",
        fully_specified_name="Lumbar puncture, subcategory 9 (procedure)",
        preferred_term="Lumbar puncture subcategory 9",
        semantic_tag="procedure"
    ),
    "39202100910": SNOMEDConcept(
        sctid="39202100910",
        fully_specified_name="Lumbar puncture, subcategory 10 (procedure)",
        preferred_term="Lumbar puncture subcategory 10",
        semantic_tag="procedure"
    ),
    "39202100911": SNOMEDConcept(
        sctid="39202100911",
        fully_specified_name="Lumbar puncture, subcategory 11 (procedure)",
        preferred_term="Lumbar puncture subcategory 11",
        semantic_tag="procedure"
    ),
    "39202100912": SNOMEDConcept(
        sctid="39202100912",
        fully_specified_name="Lumbar puncture, subcategory 12 (procedure)",
        preferred_term="Lumbar puncture subcategory 12",
        semantic_tag="procedure"
    ),
    "39202100913": SNOMEDConcept(
        sctid="39202100913",
        fully_specified_name="Lumbar puncture, subcategory 13 (procedure)",
        preferred_term="Lumbar puncture subcategory 13",
        semantic_tag="procedure"
    ),
    "39202100914": SNOMEDConcept(
        sctid="39202100914",
        fully_specified_name="Lumbar puncture, subcategory 14 (procedure)",
        preferred_term="Lumbar puncture subcategory 14",
        semantic_tag="procedure"
    ),
    "116152004": SNOMEDConcept(
        sctid="116152004",
        fully_specified_name="Insertion of intravenous catheter (procedure)",
        preferred_term="Insertion of intravenous catheter",
        semantic_tag="procedure"
    ),
    "11615200401": SNOMEDConcept(
        sctid="11615200401",
        fully_specified_name="Insertion of intravenous catheter, subcategory 1 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 1",
        semantic_tag="procedure"
    ),
    "11615200402": SNOMEDConcept(
        sctid="11615200402",
        fully_specified_name="Insertion of intravenous catheter, subcategory 2 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 2",
        semantic_tag="procedure"
    ),
    "11615200403": SNOMEDConcept(
        sctid="11615200403",
        fully_specified_name="Insertion of intravenous catheter, subcategory 3 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 3",
        semantic_tag="procedure"
    ),
    "11615200404": SNOMEDConcept(
        sctid="11615200404",
        fully_specified_name="Insertion of intravenous catheter, subcategory 4 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 4",
        semantic_tag="procedure"
    ),
    "11615200405": SNOMEDConcept(
        sctid="11615200405",
        fully_specified_name="Insertion of intravenous catheter, subcategory 5 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 5",
        semantic_tag="procedure"
    ),
    "11615200406": SNOMEDConcept(
        sctid="11615200406",
        fully_specified_name="Insertion of intravenous catheter, subcategory 6 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 6",
        semantic_tag="procedure"
    ),
    "11615200407": SNOMEDConcept(
        sctid="11615200407",
        fully_specified_name="Insertion of intravenous catheter, subcategory 7 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 7",
        semantic_tag="procedure"
    ),
    "11615200408": SNOMEDConcept(
        sctid="11615200408",
        fully_specified_name="Insertion of intravenous catheter, subcategory 8 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 8",
        semantic_tag="procedure"
    ),
    "11615200409": SNOMEDConcept(
        sctid="11615200409",
        fully_specified_name="Insertion of intravenous catheter, subcategory 9 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 9",
        semantic_tag="procedure"
    ),
    "11615200410": SNOMEDConcept(
        sctid="11615200410",
        fully_specified_name="Insertion of intravenous catheter, subcategory 10 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 10",
        semantic_tag="procedure"
    ),
    "11615200411": SNOMEDConcept(
        sctid="11615200411",
        fully_specified_name="Insertion of intravenous catheter, subcategory 11 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 11",
        semantic_tag="procedure"
    ),
    "11615200412": SNOMEDConcept(
        sctid="11615200412",
        fully_specified_name="Insertion of intravenous catheter, subcategory 12 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 12",
        semantic_tag="procedure"
    ),
    "11615200413": SNOMEDConcept(
        sctid="11615200413",
        fully_specified_name="Insertion of intravenous catheter, subcategory 13 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 13",
        semantic_tag="procedure"
    ),
    "11615200414": SNOMEDConcept(
        sctid="11615200414",
        fully_specified_name="Insertion of intravenous catheter, subcategory 14 (procedure)",
        preferred_term="Insertion of intravenous catheter subcategory 14",
        semantic_tag="procedure"
    ),
    "225116006": SNOMEDConcept(
        sctid="225116006",
        fully_specified_name="Chest radiography (procedure)",
        preferred_term="Chest radiography",
        semantic_tag="procedure"
    ),
    "22511600601": SNOMEDConcept(
        sctid="22511600601",
        fully_specified_name="Chest radiography, subcategory 1 (procedure)",
        preferred_term="Chest radiography subcategory 1",
        semantic_tag="procedure"
    ),
    "22511600602": SNOMEDConcept(
        sctid="22511600602",
        fully_specified_name="Chest radiography, subcategory 2 (procedure)",
        preferred_term="Chest radiography subcategory 2",
        semantic_tag="procedure"
    ),
    "22511600603": SNOMEDConcept(
        sctid="22511600603",
        fully_specified_name="Chest radiography, subcategory 3 (procedure)",
        preferred_term="Chest radiography subcategory 3",
        semantic_tag="procedure"
    ),
    "22511600604": SNOMEDConcept(
        sctid="22511600604",
        fully_specified_name="Chest radiography, subcategory 4 (procedure)",
        preferred_term="Chest radiography subcategory 4",
        semantic_tag="procedure"
    ),
    "22511600605": SNOMEDConcept(
        sctid="22511600605",
        fully_specified_name="Chest radiography, subcategory 5 (procedure)",
        preferred_term="Chest radiography subcategory 5",
        semantic_tag="procedure"
    ),
    "22511600606": SNOMEDConcept(
        sctid="22511600606",
        fully_specified_name="Chest radiography, subcategory 6 (procedure)",
        preferred_term="Chest radiography subcategory 6",
        semantic_tag="procedure"
    ),
    "22511600607": SNOMEDConcept(
        sctid="22511600607",
        fully_specified_name="Chest radiography, subcategory 7 (procedure)",
        preferred_term="Chest radiography subcategory 7",
        semantic_tag="procedure"
    ),
    "22511600608": SNOMEDConcept(
        sctid="22511600608",
        fully_specified_name="Chest radiography, subcategory 8 (procedure)",
        preferred_term="Chest radiography subcategory 8",
        semantic_tag="procedure"
    ),
    "22511600609": SNOMEDConcept(
        sctid="22511600609",
        fully_specified_name="Chest radiography, subcategory 9 (procedure)",
        preferred_term="Chest radiography subcategory 9",
        semantic_tag="procedure"
    ),
    "22511600610": SNOMEDConcept(
        sctid="22511600610",
        fully_specified_name="Chest radiography, subcategory 10 (procedure)",
        preferred_term="Chest radiography subcategory 10",
        semantic_tag="procedure"
    ),
    "22511600611": SNOMEDConcept(
        sctid="22511600611",
        fully_specified_name="Chest radiography, subcategory 11 (procedure)",
        preferred_term="Chest radiography subcategory 11",
        semantic_tag="procedure"
    ),
    "22511600612": SNOMEDConcept(
        sctid="22511600612",
        fully_specified_name="Chest radiography, subcategory 12 (procedure)",
        preferred_term="Chest radiography subcategory 12",
        semantic_tag="procedure"
    ),
    "22511600613": SNOMEDConcept(
        sctid="22511600613",
        fully_specified_name="Chest radiography, subcategory 13 (procedure)",
        preferred_term="Chest radiography subcategory 13",
        semantic_tag="procedure"
    ),
    "22511600614": SNOMEDConcept(
        sctid="22511600614",
        fully_specified_name="Chest radiography, subcategory 14 (procedure)",
        preferred_term="Chest radiography subcategory 14",
        semantic_tag="procedure"
    ),
    "241615005": SNOMEDConcept(
        sctid="241615005",
        fully_specified_name="Computed tomography of head (procedure)",
        preferred_term="Computed tomography of head",
        semantic_tag="procedure"
    ),
    "24161500501": SNOMEDConcept(
        sctid="24161500501",
        fully_specified_name="Computed tomography of head, subcategory 1 (procedure)",
        preferred_term="Computed tomography of head subcategory 1",
        semantic_tag="procedure"
    ),
    "24161500502": SNOMEDConcept(
        sctid="24161500502",
        fully_specified_name="Computed tomography of head, subcategory 2 (procedure)",
        preferred_term="Computed tomography of head subcategory 2",
        semantic_tag="procedure"
    ),
    "24161500503": SNOMEDConcept(
        sctid="24161500503",
        fully_specified_name="Computed tomography of head, subcategory 3 (procedure)",
        preferred_term="Computed tomography of head subcategory 3",
        semantic_tag="procedure"
    ),
    "24161500504": SNOMEDConcept(
        sctid="24161500504",
        fully_specified_name="Computed tomography of head, subcategory 4 (procedure)",
        preferred_term="Computed tomography of head subcategory 4",
        semantic_tag="procedure"
    ),
    "24161500505": SNOMEDConcept(
        sctid="24161500505",
        fully_specified_name="Computed tomography of head, subcategory 5 (procedure)",
        preferred_term="Computed tomography of head subcategory 5",
        semantic_tag="procedure"
    ),
    "24161500506": SNOMEDConcept(
        sctid="24161500506",
        fully_specified_name="Computed tomography of head, subcategory 6 (procedure)",
        preferred_term="Computed tomography of head subcategory 6",
        semantic_tag="procedure"
    ),
    "24161500507": SNOMEDConcept(
        sctid="24161500507",
        fully_specified_name="Computed tomography of head, subcategory 7 (procedure)",
        preferred_term="Computed tomography of head subcategory 7",
        semantic_tag="procedure"
    ),
    "24161500508": SNOMEDConcept(
        sctid="24161500508",
        fully_specified_name="Computed tomography of head, subcategory 8 (procedure)",
        preferred_term="Computed tomography of head subcategory 8",
        semantic_tag="procedure"
    ),
    "24161500509": SNOMEDConcept(
        sctid="24161500509",
        fully_specified_name="Computed tomography of head, subcategory 9 (procedure)",
        preferred_term="Computed tomography of head subcategory 9",
        semantic_tag="procedure"
    ),
    "24161500510": SNOMEDConcept(
        sctid="24161500510",
        fully_specified_name="Computed tomography of head, subcategory 10 (procedure)",
        preferred_term="Computed tomography of head subcategory 10",
        semantic_tag="procedure"
    ),
    "24161500511": SNOMEDConcept(
        sctid="24161500511",
        fully_specified_name="Computed tomography of head, subcategory 11 (procedure)",
        preferred_term="Computed tomography of head subcategory 11",
        semantic_tag="procedure"
    ),
    "24161500512": SNOMEDConcept(
        sctid="24161500512",
        fully_specified_name="Computed tomography of head, subcategory 12 (procedure)",
        preferred_term="Computed tomography of head subcategory 12",
        semantic_tag="procedure"
    ),
    "24161500513": SNOMEDConcept(
        sctid="24161500513",
        fully_specified_name="Computed tomography of head, subcategory 13 (procedure)",
        preferred_term="Computed tomography of head subcategory 13",
        semantic_tag="procedure"
    ),
    "24161500514": SNOMEDConcept(
        sctid="24161500514",
        fully_specified_name="Computed tomography of head, subcategory 14 (procedure)",
        preferred_term="Computed tomography of head subcategory 14",
        semantic_tag="procedure"
    ),
    "271649006": SNOMEDConcept(
        sctid="271649006",
        fully_specified_name="Systolic blood pressure (observable entity)",
        preferred_term="Systolic blood pressure",
        semantic_tag="observable entity"
    ),
    "27164900601": SNOMEDConcept(
        sctid="27164900601",
        fully_specified_name="Systolic blood pressure, subcategory 1 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 1",
        semantic_tag="observable entity"
    ),
    "27164900602": SNOMEDConcept(
        sctid="27164900602",
        fully_specified_name="Systolic blood pressure, subcategory 2 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 2",
        semantic_tag="observable entity"
    ),
    "27164900603": SNOMEDConcept(
        sctid="27164900603",
        fully_specified_name="Systolic blood pressure, subcategory 3 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 3",
        semantic_tag="observable entity"
    ),
    "27164900604": SNOMEDConcept(
        sctid="27164900604",
        fully_specified_name="Systolic blood pressure, subcategory 4 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 4",
        semantic_tag="observable entity"
    ),
    "27164900605": SNOMEDConcept(
        sctid="27164900605",
        fully_specified_name="Systolic blood pressure, subcategory 5 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 5",
        semantic_tag="observable entity"
    ),
    "27164900606": SNOMEDConcept(
        sctid="27164900606",
        fully_specified_name="Systolic blood pressure, subcategory 6 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 6",
        semantic_tag="observable entity"
    ),
    "27164900607": SNOMEDConcept(
        sctid="27164900607",
        fully_specified_name="Systolic blood pressure, subcategory 7 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 7",
        semantic_tag="observable entity"
    ),
    "27164900608": SNOMEDConcept(
        sctid="27164900608",
        fully_specified_name="Systolic blood pressure, subcategory 8 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 8",
        semantic_tag="observable entity"
    ),
    "27164900609": SNOMEDConcept(
        sctid="27164900609",
        fully_specified_name="Systolic blood pressure, subcategory 9 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 9",
        semantic_tag="observable entity"
    ),
    "27164900610": SNOMEDConcept(
        sctid="27164900610",
        fully_specified_name="Systolic blood pressure, subcategory 10 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 10",
        semantic_tag="observable entity"
    ),
    "27164900611": SNOMEDConcept(
        sctid="27164900611",
        fully_specified_name="Systolic blood pressure, subcategory 11 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 11",
        semantic_tag="observable entity"
    ),
    "27164900612": SNOMEDConcept(
        sctid="27164900612",
        fully_specified_name="Systolic blood pressure, subcategory 12 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 12",
        semantic_tag="observable entity"
    ),
    "27164900613": SNOMEDConcept(
        sctid="27164900613",
        fully_specified_name="Systolic blood pressure, subcategory 13 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 13",
        semantic_tag="observable entity"
    ),
    "27164900614": SNOMEDConcept(
        sctid="27164900614",
        fully_specified_name="Systolic blood pressure, subcategory 14 (observable entity)",
        preferred_term="Systolic blood pressure subcategory 14",
        semantic_tag="observable entity"
    ),
    "271650006": SNOMEDConcept(
        sctid="271650006",
        fully_specified_name="Diastolic blood pressure (observable entity)",
        preferred_term="Diastolic blood pressure",
        semantic_tag="observable entity"
    ),
    "27165000601": SNOMEDConcept(
        sctid="27165000601",
        fully_specified_name="Diastolic blood pressure, subcategory 1 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 1",
        semantic_tag="observable entity"
    ),
    "27165000602": SNOMEDConcept(
        sctid="27165000602",
        fully_specified_name="Diastolic blood pressure, subcategory 2 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 2",
        semantic_tag="observable entity"
    ),
    "27165000603": SNOMEDConcept(
        sctid="27165000603",
        fully_specified_name="Diastolic blood pressure, subcategory 3 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 3",
        semantic_tag="observable entity"
    ),
    "27165000604": SNOMEDConcept(
        sctid="27165000604",
        fully_specified_name="Diastolic blood pressure, subcategory 4 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 4",
        semantic_tag="observable entity"
    ),
    "27165000605": SNOMEDConcept(
        sctid="27165000605",
        fully_specified_name="Diastolic blood pressure, subcategory 5 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 5",
        semantic_tag="observable entity"
    ),
    "27165000606": SNOMEDConcept(
        sctid="27165000606",
        fully_specified_name="Diastolic blood pressure, subcategory 6 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 6",
        semantic_tag="observable entity"
    ),
    "27165000607": SNOMEDConcept(
        sctid="27165000607",
        fully_specified_name="Diastolic blood pressure, subcategory 7 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 7",
        semantic_tag="observable entity"
    ),
    "27165000608": SNOMEDConcept(
        sctid="27165000608",
        fully_specified_name="Diastolic blood pressure, subcategory 8 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 8",
        semantic_tag="observable entity"
    ),
    "27165000609": SNOMEDConcept(
        sctid="27165000609",
        fully_specified_name="Diastolic blood pressure, subcategory 9 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 9",
        semantic_tag="observable entity"
    ),
    "27165000610": SNOMEDConcept(
        sctid="27165000610",
        fully_specified_name="Diastolic blood pressure, subcategory 10 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 10",
        semantic_tag="observable entity"
    ),
    "27165000611": SNOMEDConcept(
        sctid="27165000611",
        fully_specified_name="Diastolic blood pressure, subcategory 11 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 11",
        semantic_tag="observable entity"
    ),
    "27165000612": SNOMEDConcept(
        sctid="27165000612",
        fully_specified_name="Diastolic blood pressure, subcategory 12 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 12",
        semantic_tag="observable entity"
    ),
    "27165000613": SNOMEDConcept(
        sctid="27165000613",
        fully_specified_name="Diastolic blood pressure, subcategory 13 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 13",
        semantic_tag="observable entity"
    ),
    "27165000614": SNOMEDConcept(
        sctid="27165000614",
        fully_specified_name="Diastolic blood pressure, subcategory 14 (observable entity)",
        preferred_term="Diastolic blood pressure subcategory 14",
        semantic_tag="observable entity"
    ),
    "364075005": SNOMEDConcept(
        sctid="364075005",
        fully_specified_name="Heart rate (observable entity)",
        preferred_term="Heart rate",
        semantic_tag="observable entity"
    ),
    "36407500501": SNOMEDConcept(
        sctid="36407500501",
        fully_specified_name="Heart rate, subcategory 1 (observable entity)",
        preferred_term="Heart rate subcategory 1",
        semantic_tag="observable entity"
    ),
    "36407500502": SNOMEDConcept(
        sctid="36407500502",
        fully_specified_name="Heart rate, subcategory 2 (observable entity)",
        preferred_term="Heart rate subcategory 2",
        semantic_tag="observable entity"
    ),
    "36407500503": SNOMEDConcept(
        sctid="36407500503",
        fully_specified_name="Heart rate, subcategory 3 (observable entity)",
        preferred_term="Heart rate subcategory 3",
        semantic_tag="observable entity"
    ),
    "36407500504": SNOMEDConcept(
        sctid="36407500504",
        fully_specified_name="Heart rate, subcategory 4 (observable entity)",
        preferred_term="Heart rate subcategory 4",
        semantic_tag="observable entity"
    ),
    "36407500505": SNOMEDConcept(
        sctid="36407500505",
        fully_specified_name="Heart rate, subcategory 5 (observable entity)",
        preferred_term="Heart rate subcategory 5",
        semantic_tag="observable entity"
    ),
    "36407500506": SNOMEDConcept(
        sctid="36407500506",
        fully_specified_name="Heart rate, subcategory 6 (observable entity)",
        preferred_term="Heart rate subcategory 6",
        semantic_tag="observable entity"
    ),
    "36407500507": SNOMEDConcept(
        sctid="36407500507",
        fully_specified_name="Heart rate, subcategory 7 (observable entity)",
        preferred_term="Heart rate subcategory 7",
        semantic_tag="observable entity"
    ),
    "36407500508": SNOMEDConcept(
        sctid="36407500508",
        fully_specified_name="Heart rate, subcategory 8 (observable entity)",
        preferred_term="Heart rate subcategory 8",
        semantic_tag="observable entity"
    ),
    "36407500509": SNOMEDConcept(
        sctid="36407500509",
        fully_specified_name="Heart rate, subcategory 9 (observable entity)",
        preferred_term="Heart rate subcategory 9",
        semantic_tag="observable entity"
    ),
    "36407500510": SNOMEDConcept(
        sctid="36407500510",
        fully_specified_name="Heart rate, subcategory 10 (observable entity)",
        preferred_term="Heart rate subcategory 10",
        semantic_tag="observable entity"
    ),
    "36407500511": SNOMEDConcept(
        sctid="36407500511",
        fully_specified_name="Heart rate, subcategory 11 (observable entity)",
        preferred_term="Heart rate subcategory 11",
        semantic_tag="observable entity"
    ),
    "36407500512": SNOMEDConcept(
        sctid="36407500512",
        fully_specified_name="Heart rate, subcategory 12 (observable entity)",
        preferred_term="Heart rate subcategory 12",
        semantic_tag="observable entity"
    ),
    "36407500513": SNOMEDConcept(
        sctid="36407500513",
        fully_specified_name="Heart rate, subcategory 13 (observable entity)",
        preferred_term="Heart rate subcategory 13",
        semantic_tag="observable entity"
    ),
    "36407500514": SNOMEDConcept(
        sctid="36407500514",
        fully_specified_name="Heart rate, subcategory 14 (observable entity)",
        preferred_term="Heart rate subcategory 14",
        semantic_tag="observable entity"
    ),
    "86290005": SNOMEDConcept(
        sctid="86290005",
        fully_specified_name="Respiratory rate (observable entity)",
        preferred_term="Respiratory rate",
        semantic_tag="observable entity"
    ),
    "8629000501": SNOMEDConcept(
        sctid="8629000501",
        fully_specified_name="Respiratory rate, subcategory 1 (observable entity)",
        preferred_term="Respiratory rate subcategory 1",
        semantic_tag="observable entity"
    ),
    "8629000502": SNOMEDConcept(
        sctid="8629000502",
        fully_specified_name="Respiratory rate, subcategory 2 (observable entity)",
        preferred_term="Respiratory rate subcategory 2",
        semantic_tag="observable entity"
    ),
    "8629000503": SNOMEDConcept(
        sctid="8629000503",
        fully_specified_name="Respiratory rate, subcategory 3 (observable entity)",
        preferred_term="Respiratory rate subcategory 3",
        semantic_tag="observable entity"
    ),
    "8629000504": SNOMEDConcept(
        sctid="8629000504",
        fully_specified_name="Respiratory rate, subcategory 4 (observable entity)",
        preferred_term="Respiratory rate subcategory 4",
        semantic_tag="observable entity"
    ),
    "8629000505": SNOMEDConcept(
        sctid="8629000505",
        fully_specified_name="Respiratory rate, subcategory 5 (observable entity)",
        preferred_term="Respiratory rate subcategory 5",
        semantic_tag="observable entity"
    ),
    "8629000506": SNOMEDConcept(
        sctid="8629000506",
        fully_specified_name="Respiratory rate, subcategory 6 (observable entity)",
        preferred_term="Respiratory rate subcategory 6",
        semantic_tag="observable entity"
    ),
    "8629000507": SNOMEDConcept(
        sctid="8629000507",
        fully_specified_name="Respiratory rate, subcategory 7 (observable entity)",
        preferred_term="Respiratory rate subcategory 7",
        semantic_tag="observable entity"
    ),
    "8629000508": SNOMEDConcept(
        sctid="8629000508",
        fully_specified_name="Respiratory rate, subcategory 8 (observable entity)",
        preferred_term="Respiratory rate subcategory 8",
        semantic_tag="observable entity"
    ),
    "8629000509": SNOMEDConcept(
        sctid="8629000509",
        fully_specified_name="Respiratory rate, subcategory 9 (observable entity)",
        preferred_term="Respiratory rate subcategory 9",
        semantic_tag="observable entity"
    ),
    "8629000510": SNOMEDConcept(
        sctid="8629000510",
        fully_specified_name="Respiratory rate, subcategory 10 (observable entity)",
        preferred_term="Respiratory rate subcategory 10",
        semantic_tag="observable entity"
    ),
    "8629000511": SNOMEDConcept(
        sctid="8629000511",
        fully_specified_name="Respiratory rate, subcategory 11 (observable entity)",
        preferred_term="Respiratory rate subcategory 11",
        semantic_tag="observable entity"
    ),
    "8629000512": SNOMEDConcept(
        sctid="8629000512",
        fully_specified_name="Respiratory rate, subcategory 12 (observable entity)",
        preferred_term="Respiratory rate subcategory 12",
        semantic_tag="observable entity"
    ),
    "8629000513": SNOMEDConcept(
        sctid="8629000513",
        fully_specified_name="Respiratory rate, subcategory 13 (observable entity)",
        preferred_term="Respiratory rate subcategory 13",
        semantic_tag="observable entity"
    ),
    "8629000514": SNOMEDConcept(
        sctid="8629000514",
        fully_specified_name="Respiratory rate, subcategory 14 (observable entity)",
        preferred_term="Respiratory rate subcategory 14",
        semantic_tag="observable entity"
    ),
    "386725007": SNOMEDConcept(
        sctid="386725007",
        fully_specified_name="Body temperature (observable entity)",
        preferred_term="Body temperature",
        semantic_tag="observable entity"
    ),
    "38672500701": SNOMEDConcept(
        sctid="38672500701",
        fully_specified_name="Body temperature, subcategory 1 (observable entity)",
        preferred_term="Body temperature subcategory 1",
        semantic_tag="observable entity"
    ),
    "38672500702": SNOMEDConcept(
        sctid="38672500702",
        fully_specified_name="Body temperature, subcategory 2 (observable entity)",
        preferred_term="Body temperature subcategory 2",
        semantic_tag="observable entity"
    ),
    "38672500703": SNOMEDConcept(
        sctid="38672500703",
        fully_specified_name="Body temperature, subcategory 3 (observable entity)",
        preferred_term="Body temperature subcategory 3",
        semantic_tag="observable entity"
    ),
    "38672500704": SNOMEDConcept(
        sctid="38672500704",
        fully_specified_name="Body temperature, subcategory 4 (observable entity)",
        preferred_term="Body temperature subcategory 4",
        semantic_tag="observable entity"
    ),
    "38672500705": SNOMEDConcept(
        sctid="38672500705",
        fully_specified_name="Body temperature, subcategory 5 (observable entity)",
        preferred_term="Body temperature subcategory 5",
        semantic_tag="observable entity"
    ),
    "38672500706": SNOMEDConcept(
        sctid="38672500706",
        fully_specified_name="Body temperature, subcategory 6 (observable entity)",
        preferred_term="Body temperature subcategory 6",
        semantic_tag="observable entity"
    ),
    "38672500707": SNOMEDConcept(
        sctid="38672500707",
        fully_specified_name="Body temperature, subcategory 7 (observable entity)",
        preferred_term="Body temperature subcategory 7",
        semantic_tag="observable entity"
    ),
    "38672500708": SNOMEDConcept(
        sctid="38672500708",
        fully_specified_name="Body temperature, subcategory 8 (observable entity)",
        preferred_term="Body temperature subcategory 8",
        semantic_tag="observable entity"
    ),
    "38672500709": SNOMEDConcept(
        sctid="38672500709",
        fully_specified_name="Body temperature, subcategory 9 (observable entity)",
        preferred_term="Body temperature subcategory 9",
        semantic_tag="observable entity"
    ),
    "38672500710": SNOMEDConcept(
        sctid="38672500710",
        fully_specified_name="Body temperature, subcategory 10 (observable entity)",
        preferred_term="Body temperature subcategory 10",
        semantic_tag="observable entity"
    ),
    "38672500711": SNOMEDConcept(
        sctid="38672500711",
        fully_specified_name="Body temperature, subcategory 11 (observable entity)",
        preferred_term="Body temperature subcategory 11",
        semantic_tag="observable entity"
    ),
    "38672500712": SNOMEDConcept(
        sctid="38672500712",
        fully_specified_name="Body temperature, subcategory 12 (observable entity)",
        preferred_term="Body temperature subcategory 12",
        semantic_tag="observable entity"
    ),
    "38672500713": SNOMEDConcept(
        sctid="38672500713",
        fully_specified_name="Body temperature, subcategory 13 (observable entity)",
        preferred_term="Body temperature subcategory 13",
        semantic_tag="observable entity"
    ),
    "38672500714": SNOMEDConcept(
        sctid="38672500714",
        fully_specified_name="Body temperature, subcategory 14 (observable entity)",
        preferred_term="Body temperature subcategory 14",
        semantic_tag="observable entity"
    ),
    "431314004": SNOMEDConcept(
        sctid="431314004",
        fully_specified_name="Peripheral oxygen saturation (observable entity)",
        preferred_term="Peripheral oxygen saturation",
        semantic_tag="observable entity"
    ),
    "43131400401": SNOMEDConcept(
        sctid="43131400401",
        fully_specified_name="Peripheral oxygen saturation, subcategory 1 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 1",
        semantic_tag="observable entity"
    ),
    "43131400402": SNOMEDConcept(
        sctid="43131400402",
        fully_specified_name="Peripheral oxygen saturation, subcategory 2 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 2",
        semantic_tag="observable entity"
    ),
    "43131400403": SNOMEDConcept(
        sctid="43131400403",
        fully_specified_name="Peripheral oxygen saturation, subcategory 3 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 3",
        semantic_tag="observable entity"
    ),
    "43131400404": SNOMEDConcept(
        sctid="43131400404",
        fully_specified_name="Peripheral oxygen saturation, subcategory 4 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 4",
        semantic_tag="observable entity"
    ),
    "43131400405": SNOMEDConcept(
        sctid="43131400405",
        fully_specified_name="Peripheral oxygen saturation, subcategory 5 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 5",
        semantic_tag="observable entity"
    ),
    "43131400406": SNOMEDConcept(
        sctid="43131400406",
        fully_specified_name="Peripheral oxygen saturation, subcategory 6 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 6",
        semantic_tag="observable entity"
    ),
    "43131400407": SNOMEDConcept(
        sctid="43131400407",
        fully_specified_name="Peripheral oxygen saturation, subcategory 7 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 7",
        semantic_tag="observable entity"
    ),
    "43131400408": SNOMEDConcept(
        sctid="43131400408",
        fully_specified_name="Peripheral oxygen saturation, subcategory 8 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 8",
        semantic_tag="observable entity"
    ),
    "43131400409": SNOMEDConcept(
        sctid="43131400409",
        fully_specified_name="Peripheral oxygen saturation, subcategory 9 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 9",
        semantic_tag="observable entity"
    ),
    "43131400410": SNOMEDConcept(
        sctid="43131400410",
        fully_specified_name="Peripheral oxygen saturation, subcategory 10 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 10",
        semantic_tag="observable entity"
    ),
    "43131400411": SNOMEDConcept(
        sctid="43131400411",
        fully_specified_name="Peripheral oxygen saturation, subcategory 11 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 11",
        semantic_tag="observable entity"
    ),
    "43131400412": SNOMEDConcept(
        sctid="43131400412",
        fully_specified_name="Peripheral oxygen saturation, subcategory 12 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 12",
        semantic_tag="observable entity"
    ),
    "43131400413": SNOMEDConcept(
        sctid="43131400413",
        fully_specified_name="Peripheral oxygen saturation, subcategory 13 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 13",
        semantic_tag="observable entity"
    ),
    "43131400414": SNOMEDConcept(
        sctid="43131400414",
        fully_specified_name="Peripheral oxygen saturation, subcategory 14 (observable entity)",
        preferred_term="Peripheral oxygen saturation subcategory 14",
        semantic_tag="observable entity"
    ),
}

def get_snomed(sctid: str) -> Optional[SNOMEDConcept]:
    return SNOMED_DATABASE.get(str(sctid).strip())

def search_snomed(query: str, limit: int = 25) -> List[SNOMEDConcept]:
    q = query.lower()
    results = []
    for entry in SNOMED_DATABASE.values():
        if q in entry.sctid or q in entry.fully_specified_name.lower():
            results.append(entry)
            if len(results) >= limit:
                break
    return results

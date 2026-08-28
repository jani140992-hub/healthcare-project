"""
RxNorm Clinical Drug Database & National Drug Directory.
Normalized pharmaceutical substances, brand mappings, strengths, and DEA schedules.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any

@dataclass
class RxNormEntry:
    rxcui: str
    brand_name: str
    active_ingredient: str
    strength: str
    dosage_form: str
    drug_class: str
    dea_schedule: Optional[str] = None
    ndc_code: Optional[str] = None

RXNORM_DATABASE: Dict[str, RxNormEntry] = {
    "100001": RxNormEntry(
        rxcui="100001",
        brand_name="Lisinopril 2.5 mg",
        active_ingredient="Lisinopril",
        strength="2.5 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100001-0100-01"
    ),
    "100002": RxNormEntry(
        rxcui="100002",
        brand_name="Lisinopril 2.5 mg [30 count bottle]",
        active_ingredient="Lisinopril",
        strength="2.5 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100002-0101-02"
    ),
    "100003": RxNormEntry(
        rxcui="100003",
        brand_name="Lisinopril 2.5 mg [90 count bottle]",
        active_ingredient="Lisinopril",
        strength="2.5 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100003-0102-02"
    ),
    "100004": RxNormEntry(
        rxcui="100004",
        brand_name="Lisinopril 2.5 mg [100 unit dose blister]",
        active_ingredient="Lisinopril",
        strength="2.5 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100004-0103-02"
    ),
    "100005": RxNormEntry(
        rxcui="100005",
        brand_name="Lisinopril 5 mg",
        active_ingredient="Lisinopril",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100005-0104-01"
    ),
    "100006": RxNormEntry(
        rxcui="100006",
        brand_name="Lisinopril 5 mg [30 count bottle]",
        active_ingredient="Lisinopril",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100006-0105-02"
    ),
    "100007": RxNormEntry(
        rxcui="100007",
        brand_name="Lisinopril 5 mg [90 count bottle]",
        active_ingredient="Lisinopril",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100007-0106-02"
    ),
    "100008": RxNormEntry(
        rxcui="100008",
        brand_name="Lisinopril 5 mg [100 unit dose blister]",
        active_ingredient="Lisinopril",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100008-0107-02"
    ),
    "100009": RxNormEntry(
        rxcui="100009",
        brand_name="Lisinopril 10 mg",
        active_ingredient="Lisinopril",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100009-0108-01"
    ),
    "100010": RxNormEntry(
        rxcui="100010",
        brand_name="Lisinopril 10 mg [30 count bottle]",
        active_ingredient="Lisinopril",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100010-0109-02"
    ),
    "100011": RxNormEntry(
        rxcui="100011",
        brand_name="Lisinopril 10 mg [90 count bottle]",
        active_ingredient="Lisinopril",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100011-0110-02"
    ),
    "100012": RxNormEntry(
        rxcui="100012",
        brand_name="Lisinopril 10 mg [100 unit dose blister]",
        active_ingredient="Lisinopril",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100012-0111-02"
    ),
    "100013": RxNormEntry(
        rxcui="100013",
        brand_name="Lisinopril 20 mg",
        active_ingredient="Lisinopril",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100013-0112-01"
    ),
    "100014": RxNormEntry(
        rxcui="100014",
        brand_name="Lisinopril 20 mg [30 count bottle]",
        active_ingredient="Lisinopril",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100014-0113-02"
    ),
    "100015": RxNormEntry(
        rxcui="100015",
        brand_name="Lisinopril 20 mg [90 count bottle]",
        active_ingredient="Lisinopril",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100015-0114-02"
    ),
    "100016": RxNormEntry(
        rxcui="100016",
        brand_name="Lisinopril 20 mg [100 unit dose blister]",
        active_ingredient="Lisinopril",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100016-0115-02"
    ),
    "100017": RxNormEntry(
        rxcui="100017",
        brand_name="Lisinopril 40 mg",
        active_ingredient="Lisinopril",
        strength="40 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100017-0116-01"
    ),
    "100018": RxNormEntry(
        rxcui="100018",
        brand_name="Lisinopril 40 mg [30 count bottle]",
        active_ingredient="Lisinopril",
        strength="40 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100018-0117-02"
    ),
    "100019": RxNormEntry(
        rxcui="100019",
        brand_name="Lisinopril 40 mg [90 count bottle]",
        active_ingredient="Lisinopril",
        strength="40 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100019-0118-02"
    ),
    "100020": RxNormEntry(
        rxcui="100020",
        brand_name="Lisinopril 40 mg [100 unit dose blister]",
        active_ingredient="Lisinopril",
        strength="40 mg",
        dosage_form="Oral Tablet",
        drug_class="ACE Inhibitor",
        dea_schedule=None,
        ndc_code="100020-0119-02"
    ),
    "100021": RxNormEntry(
        rxcui="100021",
        brand_name="Losartan Potassium 25 mg",
        active_ingredient="Losartan Potassium",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="ARB",
        dea_schedule=None,
        ndc_code="100021-0120-01"
    ),
    "100022": RxNormEntry(
        rxcui="100022",
        brand_name="Losartan Potassium 25 mg [30 count bottle]",
        active_ingredient="Losartan Potassium",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="ARB",
        dea_schedule=None,
        ndc_code="100022-0121-02"
    ),
    "100023": RxNormEntry(
        rxcui="100023",
        brand_name="Losartan Potassium 25 mg [90 count bottle]",
        active_ingredient="Losartan Potassium",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="ARB",
        dea_schedule=None,
        ndc_code="100023-0122-02"
    ),
    "100024": RxNormEntry(
        rxcui="100024",
        brand_name="Losartan Potassium 25 mg [100 unit dose blister]",
        active_ingredient="Losartan Potassium",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="ARB",
        dea_schedule=None,
        ndc_code="100024-0123-02"
    ),
    "100025": RxNormEntry(
        rxcui="100025",
        brand_name="Losartan Potassium 50 mg",
        active_ingredient="Losartan Potassium",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="ARB",
        dea_schedule=None,
        ndc_code="100025-0124-01"
    ),
    "100026": RxNormEntry(
        rxcui="100026",
        brand_name="Losartan Potassium 50 mg [30 count bottle]",
        active_ingredient="Losartan Potassium",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="ARB",
        dea_schedule=None,
        ndc_code="100026-0125-02"
    ),
    "100027": RxNormEntry(
        rxcui="100027",
        brand_name="Losartan Potassium 50 mg [90 count bottle]",
        active_ingredient="Losartan Potassium",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="ARB",
        dea_schedule=None,
        ndc_code="100027-0126-02"
    ),
    "100028": RxNormEntry(
        rxcui="100028",
        brand_name="Losartan Potassium 50 mg [100 unit dose blister]",
        active_ingredient="Losartan Potassium",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="ARB",
        dea_schedule=None,
        ndc_code="100028-0127-02"
    ),
    "100029": RxNormEntry(
        rxcui="100029",
        brand_name="Losartan Potassium 100 mg",
        active_ingredient="Losartan Potassium",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="ARB",
        dea_schedule=None,
        ndc_code="100029-0128-01"
    ),
    "100030": RxNormEntry(
        rxcui="100030",
        brand_name="Losartan Potassium 100 mg [30 count bottle]",
        active_ingredient="Losartan Potassium",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="ARB",
        dea_schedule=None,
        ndc_code="100030-0129-02"
    ),
    "100031": RxNormEntry(
        rxcui="100031",
        brand_name="Losartan Potassium 100 mg [90 count bottle]",
        active_ingredient="Losartan Potassium",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="ARB",
        dea_schedule=None,
        ndc_code="100031-0130-02"
    ),
    "100032": RxNormEntry(
        rxcui="100032",
        brand_name="Losartan Potassium 100 mg [100 unit dose blister]",
        active_ingredient="Losartan Potassium",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="ARB",
        dea_schedule=None,
        ndc_code="100032-0131-02"
    ),
    "100033": RxNormEntry(
        rxcui="100033",
        brand_name="Amlodipine Besylate 2.5 mg",
        active_ingredient="Amlodipine Besylate",
        strength="2.5 mg",
        dosage_form="Oral Tablet",
        drug_class="CCB",
        dea_schedule=None,
        ndc_code="100033-0132-01"
    ),
    "100034": RxNormEntry(
        rxcui="100034",
        brand_name="Amlodipine Besylate 2.5 mg [30 count bottle]",
        active_ingredient="Amlodipine Besylate",
        strength="2.5 mg",
        dosage_form="Oral Tablet",
        drug_class="CCB",
        dea_schedule=None,
        ndc_code="100034-0133-02"
    ),
    "100035": RxNormEntry(
        rxcui="100035",
        brand_name="Amlodipine Besylate 2.5 mg [90 count bottle]",
        active_ingredient="Amlodipine Besylate",
        strength="2.5 mg",
        dosage_form="Oral Tablet",
        drug_class="CCB",
        dea_schedule=None,
        ndc_code="100035-0134-02"
    ),
    "100036": RxNormEntry(
        rxcui="100036",
        brand_name="Amlodipine Besylate 2.5 mg [100 unit dose blister]",
        active_ingredient="Amlodipine Besylate",
        strength="2.5 mg",
        dosage_form="Oral Tablet",
        drug_class="CCB",
        dea_schedule=None,
        ndc_code="100036-0135-02"
    ),
    "100037": RxNormEntry(
        rxcui="100037",
        brand_name="Amlodipine Besylate 5 mg",
        active_ingredient="Amlodipine Besylate",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="CCB",
        dea_schedule=None,
        ndc_code="100037-0136-01"
    ),
    "100038": RxNormEntry(
        rxcui="100038",
        brand_name="Amlodipine Besylate 5 mg [30 count bottle]",
        active_ingredient="Amlodipine Besylate",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="CCB",
        dea_schedule=None,
        ndc_code="100038-0137-02"
    ),
    "100039": RxNormEntry(
        rxcui="100039",
        brand_name="Amlodipine Besylate 5 mg [90 count bottle]",
        active_ingredient="Amlodipine Besylate",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="CCB",
        dea_schedule=None,
        ndc_code="100039-0138-02"
    ),
    "100040": RxNormEntry(
        rxcui="100040",
        brand_name="Amlodipine Besylate 5 mg [100 unit dose blister]",
        active_ingredient="Amlodipine Besylate",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="CCB",
        dea_schedule=None,
        ndc_code="100040-0139-02"
    ),
    "100041": RxNormEntry(
        rxcui="100041",
        brand_name="Amlodipine Besylate 10 mg",
        active_ingredient="Amlodipine Besylate",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="CCB",
        dea_schedule=None,
        ndc_code="100041-0140-01"
    ),
    "100042": RxNormEntry(
        rxcui="100042",
        brand_name="Amlodipine Besylate 10 mg [30 count bottle]",
        active_ingredient="Amlodipine Besylate",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="CCB",
        dea_schedule=None,
        ndc_code="100042-0141-02"
    ),
    "100043": RxNormEntry(
        rxcui="100043",
        brand_name="Amlodipine Besylate 10 mg [90 count bottle]",
        active_ingredient="Amlodipine Besylate",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="CCB",
        dea_schedule=None,
        ndc_code="100043-0142-02"
    ),
    "100044": RxNormEntry(
        rxcui="100044",
        brand_name="Amlodipine Besylate 10 mg [100 unit dose blister]",
        active_ingredient="Amlodipine Besylate",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="CCB",
        dea_schedule=None,
        ndc_code="100044-0143-02"
    ),
    "100045": RxNormEntry(
        rxcui="100045",
        brand_name="Hydrochlorothiazide 12.5 mg",
        active_ingredient="Hydrochlorothiazide",
        strength="12.5 mg",
        dosage_form="Oral Tablet",
        drug_class="Thiazide Diuretic",
        dea_schedule=None,
        ndc_code="100045-0144-01"
    ),
    "100046": RxNormEntry(
        rxcui="100046",
        brand_name="Hydrochlorothiazide 12.5 mg [30 count bottle]",
        active_ingredient="Hydrochlorothiazide",
        strength="12.5 mg",
        dosage_form="Oral Tablet",
        drug_class="Thiazide Diuretic",
        dea_schedule=None,
        ndc_code="100046-0145-02"
    ),
    "100047": RxNormEntry(
        rxcui="100047",
        brand_name="Hydrochlorothiazide 12.5 mg [90 count bottle]",
        active_ingredient="Hydrochlorothiazide",
        strength="12.5 mg",
        dosage_form="Oral Tablet",
        drug_class="Thiazide Diuretic",
        dea_schedule=None,
        ndc_code="100047-0146-02"
    ),
    "100048": RxNormEntry(
        rxcui="100048",
        brand_name="Hydrochlorothiazide 12.5 mg [100 unit dose blister]",
        active_ingredient="Hydrochlorothiazide",
        strength="12.5 mg",
        dosage_form="Oral Tablet",
        drug_class="Thiazide Diuretic",
        dea_schedule=None,
        ndc_code="100048-0147-02"
    ),
    "100049": RxNormEntry(
        rxcui="100049",
        brand_name="Hydrochlorothiazide 25 mg",
        active_ingredient="Hydrochlorothiazide",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Thiazide Diuretic",
        dea_schedule=None,
        ndc_code="100049-0148-01"
    ),
    "100050": RxNormEntry(
        rxcui="100050",
        brand_name="Hydrochlorothiazide 25 mg [30 count bottle]",
        active_ingredient="Hydrochlorothiazide",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Thiazide Diuretic",
        dea_schedule=None,
        ndc_code="100050-0149-02"
    ),
    "100051": RxNormEntry(
        rxcui="100051",
        brand_name="Hydrochlorothiazide 25 mg [90 count bottle]",
        active_ingredient="Hydrochlorothiazide",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Thiazide Diuretic",
        dea_schedule=None,
        ndc_code="100051-0150-02"
    ),
    "100052": RxNormEntry(
        rxcui="100052",
        brand_name="Hydrochlorothiazide 25 mg [100 unit dose blister]",
        active_ingredient="Hydrochlorothiazide",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Thiazide Diuretic",
        dea_schedule=None,
        ndc_code="100052-0151-02"
    ),
    "100053": RxNormEntry(
        rxcui="100053",
        brand_name="Hydrochlorothiazide 50 mg",
        active_ingredient="Hydrochlorothiazide",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Thiazide Diuretic",
        dea_schedule=None,
        ndc_code="100053-0152-01"
    ),
    "100054": RxNormEntry(
        rxcui="100054",
        brand_name="Hydrochlorothiazide 50 mg [30 count bottle]",
        active_ingredient="Hydrochlorothiazide",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Thiazide Diuretic",
        dea_schedule=None,
        ndc_code="100054-0153-02"
    ),
    "100055": RxNormEntry(
        rxcui="100055",
        brand_name="Hydrochlorothiazide 50 mg [90 count bottle]",
        active_ingredient="Hydrochlorothiazide",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Thiazide Diuretic",
        dea_schedule=None,
        ndc_code="100055-0154-02"
    ),
    "100056": RxNormEntry(
        rxcui="100056",
        brand_name="Hydrochlorothiazide 50 mg [100 unit dose blister]",
        active_ingredient="Hydrochlorothiazide",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Thiazide Diuretic",
        dea_schedule=None,
        ndc_code="100056-0155-02"
    ),
    "100057": RxNormEntry(
        rxcui="100057",
        brand_name="Metoprolol Tartrate 25 mg",
        active_ingredient="Metoprolol Tartrate",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100057-0156-01"
    ),
    "100058": RxNormEntry(
        rxcui="100058",
        brand_name="Metoprolol Tartrate 25 mg [30 count bottle]",
        active_ingredient="Metoprolol Tartrate",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100058-0157-02"
    ),
    "100059": RxNormEntry(
        rxcui="100059",
        brand_name="Metoprolol Tartrate 25 mg [90 count bottle]",
        active_ingredient="Metoprolol Tartrate",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100059-0158-02"
    ),
    "100060": RxNormEntry(
        rxcui="100060",
        brand_name="Metoprolol Tartrate 25 mg [100 unit dose blister]",
        active_ingredient="Metoprolol Tartrate",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100060-0159-02"
    ),
    "100061": RxNormEntry(
        rxcui="100061",
        brand_name="Metoprolol Tartrate 50 mg",
        active_ingredient="Metoprolol Tartrate",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100061-0160-01"
    ),
    "100062": RxNormEntry(
        rxcui="100062",
        brand_name="Metoprolol Tartrate 50 mg [30 count bottle]",
        active_ingredient="Metoprolol Tartrate",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100062-0161-02"
    ),
    "100063": RxNormEntry(
        rxcui="100063",
        brand_name="Metoprolol Tartrate 50 mg [90 count bottle]",
        active_ingredient="Metoprolol Tartrate",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100063-0162-02"
    ),
    "100064": RxNormEntry(
        rxcui="100064",
        brand_name="Metoprolol Tartrate 50 mg [100 unit dose blister]",
        active_ingredient="Metoprolol Tartrate",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100064-0163-02"
    ),
    "100065": RxNormEntry(
        rxcui="100065",
        brand_name="Metoprolol Tartrate 100 mg",
        active_ingredient="Metoprolol Tartrate",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100065-0164-01"
    ),
    "100066": RxNormEntry(
        rxcui="100066",
        brand_name="Metoprolol Tartrate 100 mg [30 count bottle]",
        active_ingredient="Metoprolol Tartrate",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100066-0165-02"
    ),
    "100067": RxNormEntry(
        rxcui="100067",
        brand_name="Metoprolol Tartrate 100 mg [90 count bottle]",
        active_ingredient="Metoprolol Tartrate",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100067-0166-02"
    ),
    "100068": RxNormEntry(
        rxcui="100068",
        brand_name="Metoprolol Tartrate 100 mg [100 unit dose blister]",
        active_ingredient="Metoprolol Tartrate",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100068-0167-02"
    ),
    "100069": RxNormEntry(
        rxcui="100069",
        brand_name="Metoprolol Succinate 25 mg",
        active_ingredient="Metoprolol Succinate",
        strength="25 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100069-0168-01"
    ),
    "100070": RxNormEntry(
        rxcui="100070",
        brand_name="Metoprolol Succinate 25 mg [30 count bottle]",
        active_ingredient="Metoprolol Succinate",
        strength="25 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100070-0169-02"
    ),
    "100071": RxNormEntry(
        rxcui="100071",
        brand_name="Metoprolol Succinate 25 mg [90 count bottle]",
        active_ingredient="Metoprolol Succinate",
        strength="25 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100071-0170-02"
    ),
    "100072": RxNormEntry(
        rxcui="100072",
        brand_name="Metoprolol Succinate 25 mg [100 unit dose blister]",
        active_ingredient="Metoprolol Succinate",
        strength="25 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100072-0171-02"
    ),
    "100073": RxNormEntry(
        rxcui="100073",
        brand_name="Metoprolol Succinate 50 mg",
        active_ingredient="Metoprolol Succinate",
        strength="50 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100073-0172-01"
    ),
    "100074": RxNormEntry(
        rxcui="100074",
        brand_name="Metoprolol Succinate 50 mg [30 count bottle]",
        active_ingredient="Metoprolol Succinate",
        strength="50 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100074-0173-02"
    ),
    "100075": RxNormEntry(
        rxcui="100075",
        brand_name="Metoprolol Succinate 50 mg [90 count bottle]",
        active_ingredient="Metoprolol Succinate",
        strength="50 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100075-0174-02"
    ),
    "100076": RxNormEntry(
        rxcui="100076",
        brand_name="Metoprolol Succinate 50 mg [100 unit dose blister]",
        active_ingredient="Metoprolol Succinate",
        strength="50 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100076-0175-02"
    ),
    "100077": RxNormEntry(
        rxcui="100077",
        brand_name="Metoprolol Succinate 100 mg",
        active_ingredient="Metoprolol Succinate",
        strength="100 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100077-0176-01"
    ),
    "100078": RxNormEntry(
        rxcui="100078",
        brand_name="Metoprolol Succinate 100 mg [30 count bottle]",
        active_ingredient="Metoprolol Succinate",
        strength="100 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100078-0177-02"
    ),
    "100079": RxNormEntry(
        rxcui="100079",
        brand_name="Metoprolol Succinate 100 mg [90 count bottle]",
        active_ingredient="Metoprolol Succinate",
        strength="100 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100079-0178-02"
    ),
    "100080": RxNormEntry(
        rxcui="100080",
        brand_name="Metoprolol Succinate 100 mg [100 unit dose blister]",
        active_ingredient="Metoprolol Succinate",
        strength="100 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100080-0179-02"
    ),
    "100081": RxNormEntry(
        rxcui="100081",
        brand_name="Metoprolol Succinate 200 mg",
        active_ingredient="Metoprolol Succinate",
        strength="200 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100081-0180-01"
    ),
    "100082": RxNormEntry(
        rxcui="100082",
        brand_name="Metoprolol Succinate 200 mg [30 count bottle]",
        active_ingredient="Metoprolol Succinate",
        strength="200 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100082-0181-02"
    ),
    "100083": RxNormEntry(
        rxcui="100083",
        brand_name="Metoprolol Succinate 200 mg [90 count bottle]",
        active_ingredient="Metoprolol Succinate",
        strength="200 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100083-0182-02"
    ),
    "100084": RxNormEntry(
        rxcui="100084",
        brand_name="Metoprolol Succinate 200 mg [100 unit dose blister]",
        active_ingredient="Metoprolol Succinate",
        strength="200 mg",
        dosage_form="Extended Release Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100084-0183-02"
    ),
    "100085": RxNormEntry(
        rxcui="100085",
        brand_name="Carvedilol 3.125 mg",
        active_ingredient="Carvedilol",
        strength="3.125 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100085-0184-01"
    ),
    "100086": RxNormEntry(
        rxcui="100086",
        brand_name="Carvedilol 3.125 mg [30 count bottle]",
        active_ingredient="Carvedilol",
        strength="3.125 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100086-0185-02"
    ),
    "100087": RxNormEntry(
        rxcui="100087",
        brand_name="Carvedilol 3.125 mg [90 count bottle]",
        active_ingredient="Carvedilol",
        strength="3.125 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100087-0186-02"
    ),
    "100088": RxNormEntry(
        rxcui="100088",
        brand_name="Carvedilol 3.125 mg [100 unit dose blister]",
        active_ingredient="Carvedilol",
        strength="3.125 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100088-0187-02"
    ),
    "100089": RxNormEntry(
        rxcui="100089",
        brand_name="Carvedilol 6.25 mg",
        active_ingredient="Carvedilol",
        strength="6.25 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100089-0188-01"
    ),
    "100090": RxNormEntry(
        rxcui="100090",
        brand_name="Carvedilol 6.25 mg [30 count bottle]",
        active_ingredient="Carvedilol",
        strength="6.25 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100090-0189-02"
    ),
    "100091": RxNormEntry(
        rxcui="100091",
        brand_name="Carvedilol 6.25 mg [90 count bottle]",
        active_ingredient="Carvedilol",
        strength="6.25 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100091-0190-02"
    ),
    "100092": RxNormEntry(
        rxcui="100092",
        brand_name="Carvedilol 6.25 mg [100 unit dose blister]",
        active_ingredient="Carvedilol",
        strength="6.25 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100092-0191-02"
    ),
    "100093": RxNormEntry(
        rxcui="100093",
        brand_name="Carvedilol 12.5 mg",
        active_ingredient="Carvedilol",
        strength="12.5 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100093-0192-01"
    ),
    "100094": RxNormEntry(
        rxcui="100094",
        brand_name="Carvedilol 12.5 mg [30 count bottle]",
        active_ingredient="Carvedilol",
        strength="12.5 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100094-0193-02"
    ),
    "100095": RxNormEntry(
        rxcui="100095",
        brand_name="Carvedilol 12.5 mg [90 count bottle]",
        active_ingredient="Carvedilol",
        strength="12.5 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100095-0194-02"
    ),
    "100096": RxNormEntry(
        rxcui="100096",
        brand_name="Carvedilol 12.5 mg [100 unit dose blister]",
        active_ingredient="Carvedilol",
        strength="12.5 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100096-0195-02"
    ),
    "100097": RxNormEntry(
        rxcui="100097",
        brand_name="Carvedilol 25 mg",
        active_ingredient="Carvedilol",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100097-0196-01"
    ),
    "100098": RxNormEntry(
        rxcui="100098",
        brand_name="Carvedilol 25 mg [30 count bottle]",
        active_ingredient="Carvedilol",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100098-0197-02"
    ),
    "100099": RxNormEntry(
        rxcui="100099",
        brand_name="Carvedilol 25 mg [90 count bottle]",
        active_ingredient="Carvedilol",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100099-0198-02"
    ),
    "100100": RxNormEntry(
        rxcui="100100",
        brand_name="Carvedilol 25 mg [100 unit dose blister]",
        active_ingredient="Carvedilol",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Beta Blocker",
        dea_schedule=None,
        ndc_code="100100-0199-02"
    ),
    "100101": RxNormEntry(
        rxcui="100101",
        brand_name="Spironolactone 25 mg",
        active_ingredient="Spironolactone",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Aldosterone Antagonist",
        dea_schedule=None,
        ndc_code="100101-0200-01"
    ),
    "100102": RxNormEntry(
        rxcui="100102",
        brand_name="Spironolactone 25 mg [30 count bottle]",
        active_ingredient="Spironolactone",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Aldosterone Antagonist",
        dea_schedule=None,
        ndc_code="100102-0201-02"
    ),
    "100103": RxNormEntry(
        rxcui="100103",
        brand_name="Spironolactone 25 mg [90 count bottle]",
        active_ingredient="Spironolactone",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Aldosterone Antagonist",
        dea_schedule=None,
        ndc_code="100103-0202-02"
    ),
    "100104": RxNormEntry(
        rxcui="100104",
        brand_name="Spironolactone 25 mg [100 unit dose blister]",
        active_ingredient="Spironolactone",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="Aldosterone Antagonist",
        dea_schedule=None,
        ndc_code="100104-0203-02"
    ),
    "100105": RxNormEntry(
        rxcui="100105",
        brand_name="Spironolactone 50 mg",
        active_ingredient="Spironolactone",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Aldosterone Antagonist",
        dea_schedule=None,
        ndc_code="100105-0204-01"
    ),
    "100106": RxNormEntry(
        rxcui="100106",
        brand_name="Spironolactone 50 mg [30 count bottle]",
        active_ingredient="Spironolactone",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Aldosterone Antagonist",
        dea_schedule=None,
        ndc_code="100106-0205-02"
    ),
    "100107": RxNormEntry(
        rxcui="100107",
        brand_name="Spironolactone 50 mg [90 count bottle]",
        active_ingredient="Spironolactone",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Aldosterone Antagonist",
        dea_schedule=None,
        ndc_code="100107-0206-02"
    ),
    "100108": RxNormEntry(
        rxcui="100108",
        brand_name="Spironolactone 50 mg [100 unit dose blister]",
        active_ingredient="Spironolactone",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Aldosterone Antagonist",
        dea_schedule=None,
        ndc_code="100108-0207-02"
    ),
    "100109": RxNormEntry(
        rxcui="100109",
        brand_name="Spironolactone 100 mg",
        active_ingredient="Spironolactone",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="Aldosterone Antagonist",
        dea_schedule=None,
        ndc_code="100109-0208-01"
    ),
    "100110": RxNormEntry(
        rxcui="100110",
        brand_name="Spironolactone 100 mg [30 count bottle]",
        active_ingredient="Spironolactone",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="Aldosterone Antagonist",
        dea_schedule=None,
        ndc_code="100110-0209-02"
    ),
    "100111": RxNormEntry(
        rxcui="100111",
        brand_name="Spironolactone 100 mg [90 count bottle]",
        active_ingredient="Spironolactone",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="Aldosterone Antagonist",
        dea_schedule=None,
        ndc_code="100111-0210-02"
    ),
    "100112": RxNormEntry(
        rxcui="100112",
        brand_name="Spironolactone 100 mg [100 unit dose blister]",
        active_ingredient="Spironolactone",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="Aldosterone Antagonist",
        dea_schedule=None,
        ndc_code="100112-0211-02"
    ),
    "100113": RxNormEntry(
        rxcui="100113",
        brand_name="Metformin Hydrochloride 500 mg",
        active_ingredient="Metformin Hydrochloride",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Biguanide",
        dea_schedule=None,
        ndc_code="100113-0212-01"
    ),
    "100114": RxNormEntry(
        rxcui="100114",
        brand_name="Metformin Hydrochloride 500 mg [30 count bottle]",
        active_ingredient="Metformin Hydrochloride",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Biguanide",
        dea_schedule=None,
        ndc_code="100114-0213-02"
    ),
    "100115": RxNormEntry(
        rxcui="100115",
        brand_name="Metformin Hydrochloride 500 mg [90 count bottle]",
        active_ingredient="Metformin Hydrochloride",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Biguanide",
        dea_schedule=None,
        ndc_code="100115-0214-02"
    ),
    "100116": RxNormEntry(
        rxcui="100116",
        brand_name="Metformin Hydrochloride 500 mg [100 unit dose blister]",
        active_ingredient="Metformin Hydrochloride",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Biguanide",
        dea_schedule=None,
        ndc_code="100116-0215-02"
    ),
    "100117": RxNormEntry(
        rxcui="100117",
        brand_name="Metformin Hydrochloride 850 mg",
        active_ingredient="Metformin Hydrochloride",
        strength="850 mg",
        dosage_form="Oral Tablet",
        drug_class="Biguanide",
        dea_schedule=None,
        ndc_code="100117-0216-01"
    ),
    "100118": RxNormEntry(
        rxcui="100118",
        brand_name="Metformin Hydrochloride 850 mg [30 count bottle]",
        active_ingredient="Metformin Hydrochloride",
        strength="850 mg",
        dosage_form="Oral Tablet",
        drug_class="Biguanide",
        dea_schedule=None,
        ndc_code="100118-0217-02"
    ),
    "100119": RxNormEntry(
        rxcui="100119",
        brand_name="Metformin Hydrochloride 850 mg [90 count bottle]",
        active_ingredient="Metformin Hydrochloride",
        strength="850 mg",
        dosage_form="Oral Tablet",
        drug_class="Biguanide",
        dea_schedule=None,
        ndc_code="100119-0218-02"
    ),
    "100120": RxNormEntry(
        rxcui="100120",
        brand_name="Metformin Hydrochloride 850 mg [100 unit dose blister]",
        active_ingredient="Metformin Hydrochloride",
        strength="850 mg",
        dosage_form="Oral Tablet",
        drug_class="Biguanide",
        dea_schedule=None,
        ndc_code="100120-0219-02"
    ),
    "100121": RxNormEntry(
        rxcui="100121",
        brand_name="Metformin Hydrochloride 1000 mg",
        active_ingredient="Metformin Hydrochloride",
        strength="1000 mg",
        dosage_form="Oral Tablet",
        drug_class="Biguanide",
        dea_schedule=None,
        ndc_code="100121-0220-01"
    ),
    "100122": RxNormEntry(
        rxcui="100122",
        brand_name="Metformin Hydrochloride 1000 mg [30 count bottle]",
        active_ingredient="Metformin Hydrochloride",
        strength="1000 mg",
        dosage_form="Oral Tablet",
        drug_class="Biguanide",
        dea_schedule=None,
        ndc_code="100122-0221-02"
    ),
    "100123": RxNormEntry(
        rxcui="100123",
        brand_name="Metformin Hydrochloride 1000 mg [90 count bottle]",
        active_ingredient="Metformin Hydrochloride",
        strength="1000 mg",
        dosage_form="Oral Tablet",
        drug_class="Biguanide",
        dea_schedule=None,
        ndc_code="100123-0222-02"
    ),
    "100124": RxNormEntry(
        rxcui="100124",
        brand_name="Metformin Hydrochloride 1000 mg [100 unit dose blister]",
        active_ingredient="Metformin Hydrochloride",
        strength="1000 mg",
        dosage_form="Oral Tablet",
        drug_class="Biguanide",
        dea_schedule=None,
        ndc_code="100124-0223-02"
    ),
    "100125": RxNormEntry(
        rxcui="100125",
        brand_name="Glipizide 5 mg",
        active_ingredient="Glipizide",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="Sulfonylurea",
        dea_schedule=None,
        ndc_code="100125-0224-01"
    ),
    "100126": RxNormEntry(
        rxcui="100126",
        brand_name="Glipizide 5 mg [30 count bottle]",
        active_ingredient="Glipizide",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="Sulfonylurea",
        dea_schedule=None,
        ndc_code="100126-0225-02"
    ),
    "100127": RxNormEntry(
        rxcui="100127",
        brand_name="Glipizide 5 mg [90 count bottle]",
        active_ingredient="Glipizide",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="Sulfonylurea",
        dea_schedule=None,
        ndc_code="100127-0226-02"
    ),
    "100128": RxNormEntry(
        rxcui="100128",
        brand_name="Glipizide 5 mg [100 unit dose blister]",
        active_ingredient="Glipizide",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="Sulfonylurea",
        dea_schedule=None,
        ndc_code="100128-0227-02"
    ),
    "100129": RxNormEntry(
        rxcui="100129",
        brand_name="Glipizide 10 mg",
        active_ingredient="Glipizide",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="Sulfonylurea",
        dea_schedule=None,
        ndc_code="100129-0228-01"
    ),
    "100130": RxNormEntry(
        rxcui="100130",
        brand_name="Glipizide 10 mg [30 count bottle]",
        active_ingredient="Glipizide",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="Sulfonylurea",
        dea_schedule=None,
        ndc_code="100130-0229-02"
    ),
    "100131": RxNormEntry(
        rxcui="100131",
        brand_name="Glipizide 10 mg [90 count bottle]",
        active_ingredient="Glipizide",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="Sulfonylurea",
        dea_schedule=None,
        ndc_code="100131-0230-02"
    ),
    "100132": RxNormEntry(
        rxcui="100132",
        brand_name="Glipizide 10 mg [100 unit dose blister]",
        active_ingredient="Glipizide",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="Sulfonylurea",
        dea_schedule=None,
        ndc_code="100132-0231-02"
    ),
    "100133": RxNormEntry(
        rxcui="100133",
        brand_name="Empagliflozin 10 mg",
        active_ingredient="Empagliflozin",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100133-0232-01"
    ),
    "100134": RxNormEntry(
        rxcui="100134",
        brand_name="Empagliflozin 10 mg [30 count bottle]",
        active_ingredient="Empagliflozin",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100134-0233-02"
    ),
    "100135": RxNormEntry(
        rxcui="100135",
        brand_name="Empagliflozin 10 mg [90 count bottle]",
        active_ingredient="Empagliflozin",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100135-0234-02"
    ),
    "100136": RxNormEntry(
        rxcui="100136",
        brand_name="Empagliflozin 10 mg [100 unit dose blister]",
        active_ingredient="Empagliflozin",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100136-0235-02"
    ),
    "100137": RxNormEntry(
        rxcui="100137",
        brand_name="Empagliflozin 25 mg",
        active_ingredient="Empagliflozin",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100137-0236-01"
    ),
    "100138": RxNormEntry(
        rxcui="100138",
        brand_name="Empagliflozin 25 mg [30 count bottle]",
        active_ingredient="Empagliflozin",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100138-0237-02"
    ),
    "100139": RxNormEntry(
        rxcui="100139",
        brand_name="Empagliflozin 25 mg [90 count bottle]",
        active_ingredient="Empagliflozin",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100139-0238-02"
    ),
    "100140": RxNormEntry(
        rxcui="100140",
        brand_name="Empagliflozin 25 mg [100 unit dose blister]",
        active_ingredient="Empagliflozin",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100140-0239-02"
    ),
    "100141": RxNormEntry(
        rxcui="100141",
        brand_name="Dapagliflozin 5 mg",
        active_ingredient="Dapagliflozin",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100141-0240-01"
    ),
    "100142": RxNormEntry(
        rxcui="100142",
        brand_name="Dapagliflozin 5 mg [30 count bottle]",
        active_ingredient="Dapagliflozin",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100142-0241-02"
    ),
    "100143": RxNormEntry(
        rxcui="100143",
        brand_name="Dapagliflozin 5 mg [90 count bottle]",
        active_ingredient="Dapagliflozin",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100143-0242-02"
    ),
    "100144": RxNormEntry(
        rxcui="100144",
        brand_name="Dapagliflozin 5 mg [100 unit dose blister]",
        active_ingredient="Dapagliflozin",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100144-0243-02"
    ),
    "100145": RxNormEntry(
        rxcui="100145",
        brand_name="Dapagliflozin 10 mg",
        active_ingredient="Dapagliflozin",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100145-0244-01"
    ),
    "100146": RxNormEntry(
        rxcui="100146",
        brand_name="Dapagliflozin 10 mg [30 count bottle]",
        active_ingredient="Dapagliflozin",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100146-0245-02"
    ),
    "100147": RxNormEntry(
        rxcui="100147",
        brand_name="Dapagliflozin 10 mg [90 count bottle]",
        active_ingredient="Dapagliflozin",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100147-0246-02"
    ),
    "100148": RxNormEntry(
        rxcui="100148",
        brand_name="Dapagliflozin 10 mg [100 unit dose blister]",
        active_ingredient="Dapagliflozin",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="SGLT2 Inhibitor",
        dea_schedule=None,
        ndc_code="100148-0247-02"
    ),
    "100149": RxNormEntry(
        rxcui="100149",
        brand_name="Semaglutide 0.25 mg/0.5mL",
        active_ingredient="Semaglutide",
        strength="0.25 mg/0.5mL",
        dosage_form="Subcutaneous Solution Pen",
        drug_class="GLP-1 RA",
        dea_schedule=None,
        ndc_code="100149-0248-01"
    ),
    "100150": RxNormEntry(
        rxcui="100150",
        brand_name="Semaglutide 0.25 mg/0.5mL [30 count bottle]",
        active_ingredient="Semaglutide",
        strength="0.25 mg/0.5mL",
        dosage_form="Subcutaneous Solution Pen",
        drug_class="GLP-1 RA",
        dea_schedule=None,
        ndc_code="100150-0249-02"
    ),
    "100151": RxNormEntry(
        rxcui="100151",
        brand_name="Semaglutide 0.25 mg/0.5mL [90 count bottle]",
        active_ingredient="Semaglutide",
        strength="0.25 mg/0.5mL",
        dosage_form="Subcutaneous Solution Pen",
        drug_class="GLP-1 RA",
        dea_schedule=None,
        ndc_code="100151-0250-02"
    ),
    "100152": RxNormEntry(
        rxcui="100152",
        brand_name="Semaglutide 0.25 mg/0.5mL [100 unit dose blister]",
        active_ingredient="Semaglutide",
        strength="0.25 mg/0.5mL",
        dosage_form="Subcutaneous Solution Pen",
        drug_class="GLP-1 RA",
        dea_schedule=None,
        ndc_code="100152-0251-02"
    ),
    "100153": RxNormEntry(
        rxcui="100153",
        brand_name="Semaglutide 0.5 mg/0.5mL",
        active_ingredient="Semaglutide",
        strength="0.5 mg/0.5mL",
        dosage_form="Subcutaneous Solution Pen",
        drug_class="GLP-1 RA",
        dea_schedule=None,
        ndc_code="100153-0252-01"
    ),
    "100154": RxNormEntry(
        rxcui="100154",
        brand_name="Semaglutide 0.5 mg/0.5mL [30 count bottle]",
        active_ingredient="Semaglutide",
        strength="0.5 mg/0.5mL",
        dosage_form="Subcutaneous Solution Pen",
        drug_class="GLP-1 RA",
        dea_schedule=None,
        ndc_code="100154-0253-02"
    ),
    "100155": RxNormEntry(
        rxcui="100155",
        brand_name="Semaglutide 0.5 mg/0.5mL [90 count bottle]",
        active_ingredient="Semaglutide",
        strength="0.5 mg/0.5mL",
        dosage_form="Subcutaneous Solution Pen",
        drug_class="GLP-1 RA",
        dea_schedule=None,
        ndc_code="100155-0254-02"
    ),
    "100156": RxNormEntry(
        rxcui="100156",
        brand_name="Semaglutide 0.5 mg/0.5mL [100 unit dose blister]",
        active_ingredient="Semaglutide",
        strength="0.5 mg/0.5mL",
        dosage_form="Subcutaneous Solution Pen",
        drug_class="GLP-1 RA",
        dea_schedule=None,
        ndc_code="100156-0255-02"
    ),
    "100157": RxNormEntry(
        rxcui="100157",
        brand_name="Semaglutide 1 mg/0.5mL",
        active_ingredient="Semaglutide",
        strength="1 mg/0.5mL",
        dosage_form="Subcutaneous Solution Pen",
        drug_class="GLP-1 RA",
        dea_schedule=None,
        ndc_code="100157-0256-01"
    ),
    "100158": RxNormEntry(
        rxcui="100158",
        brand_name="Semaglutide 1 mg/0.5mL [30 count bottle]",
        active_ingredient="Semaglutide",
        strength="1 mg/0.5mL",
        dosage_form="Subcutaneous Solution Pen",
        drug_class="GLP-1 RA",
        dea_schedule=None,
        ndc_code="100158-0257-02"
    ),
    "100159": RxNormEntry(
        rxcui="100159",
        brand_name="Semaglutide 1 mg/0.5mL [90 count bottle]",
        active_ingredient="Semaglutide",
        strength="1 mg/0.5mL",
        dosage_form="Subcutaneous Solution Pen",
        drug_class="GLP-1 RA",
        dea_schedule=None,
        ndc_code="100159-0258-02"
    ),
    "100160": RxNormEntry(
        rxcui="100160",
        brand_name="Semaglutide 1 mg/0.5mL [100 unit dose blister]",
        active_ingredient="Semaglutide",
        strength="1 mg/0.5mL",
        dosage_form="Subcutaneous Solution Pen",
        drug_class="GLP-1 RA",
        dea_schedule=None,
        ndc_code="100160-0259-02"
    ),
    "100161": RxNormEntry(
        rxcui="100161",
        brand_name="Insulin Glargine 100 units/mL",
        active_ingredient="Insulin Glargine",
        strength="100 units/mL",
        dosage_form="Subcutaneous Solution",
        drug_class="Long-acting Insulin",
        dea_schedule=None,
        ndc_code="100161-0260-01"
    ),
    "100162": RxNormEntry(
        rxcui="100162",
        brand_name="Insulin Glargine 100 units/mL [30 count bottle]",
        active_ingredient="Insulin Glargine",
        strength="100 units/mL",
        dosage_form="Subcutaneous Solution",
        drug_class="Long-acting Insulin",
        dea_schedule=None,
        ndc_code="100162-0261-02"
    ),
    "100163": RxNormEntry(
        rxcui="100163",
        brand_name="Insulin Glargine 100 units/mL [90 count bottle]",
        active_ingredient="Insulin Glargine",
        strength="100 units/mL",
        dosage_form="Subcutaneous Solution",
        drug_class="Long-acting Insulin",
        dea_schedule=None,
        ndc_code="100163-0262-02"
    ),
    "100164": RxNormEntry(
        rxcui="100164",
        brand_name="Insulin Glargine 100 units/mL [100 unit dose blister]",
        active_ingredient="Insulin Glargine",
        strength="100 units/mL",
        dosage_form="Subcutaneous Solution",
        drug_class="Long-acting Insulin",
        dea_schedule=None,
        ndc_code="100164-0263-02"
    ),
    "100165": RxNormEntry(
        rxcui="100165",
        brand_name="Insulin Lispro 100 units/mL",
        active_ingredient="Insulin Lispro",
        strength="100 units/mL",
        dosage_form="Subcutaneous Solution",
        drug_class="Rapid-acting Insulin",
        dea_schedule=None,
        ndc_code="100165-0264-01"
    ),
    "100166": RxNormEntry(
        rxcui="100166",
        brand_name="Insulin Lispro 100 units/mL [30 count bottle]",
        active_ingredient="Insulin Lispro",
        strength="100 units/mL",
        dosage_form="Subcutaneous Solution",
        drug_class="Rapid-acting Insulin",
        dea_schedule=None,
        ndc_code="100166-0265-02"
    ),
    "100167": RxNormEntry(
        rxcui="100167",
        brand_name="Insulin Lispro 100 units/mL [90 count bottle]",
        active_ingredient="Insulin Lispro",
        strength="100 units/mL",
        dosage_form="Subcutaneous Solution",
        drug_class="Rapid-acting Insulin",
        dea_schedule=None,
        ndc_code="100167-0266-02"
    ),
    "100168": RxNormEntry(
        rxcui="100168",
        brand_name="Insulin Lispro 100 units/mL [100 unit dose blister]",
        active_ingredient="Insulin Lispro",
        strength="100 units/mL",
        dosage_form="Subcutaneous Solution",
        drug_class="Rapid-acting Insulin",
        dea_schedule=None,
        ndc_code="100168-0267-02"
    ),
    "100169": RxNormEntry(
        rxcui="100169",
        brand_name="Amoxicillin 250 mg",
        active_ingredient="Amoxicillin",
        strength="250 mg",
        dosage_form="Oral Capsule",
        drug_class="Penicillin",
        dea_schedule=None,
        ndc_code="100169-0268-01"
    ),
    "100170": RxNormEntry(
        rxcui="100170",
        brand_name="Amoxicillin 250 mg [30 count bottle]",
        active_ingredient="Amoxicillin",
        strength="250 mg",
        dosage_form="Oral Capsule",
        drug_class="Penicillin",
        dea_schedule=None,
        ndc_code="100170-0269-02"
    ),
    "100171": RxNormEntry(
        rxcui="100171",
        brand_name="Amoxicillin 250 mg [90 count bottle]",
        active_ingredient="Amoxicillin",
        strength="250 mg",
        dosage_form="Oral Capsule",
        drug_class="Penicillin",
        dea_schedule=None,
        ndc_code="100171-0270-02"
    ),
    "100172": RxNormEntry(
        rxcui="100172",
        brand_name="Amoxicillin 250 mg [100 unit dose blister]",
        active_ingredient="Amoxicillin",
        strength="250 mg",
        dosage_form="Oral Capsule",
        drug_class="Penicillin",
        dea_schedule=None,
        ndc_code="100172-0271-02"
    ),
    "100173": RxNormEntry(
        rxcui="100173",
        brand_name="Amoxicillin 500 mg",
        active_ingredient="Amoxicillin",
        strength="500 mg",
        dosage_form="Oral Capsule",
        drug_class="Penicillin",
        dea_schedule=None,
        ndc_code="100173-0272-01"
    ),
    "100174": RxNormEntry(
        rxcui="100174",
        brand_name="Amoxicillin 500 mg [30 count bottle]",
        active_ingredient="Amoxicillin",
        strength="500 mg",
        dosage_form="Oral Capsule",
        drug_class="Penicillin",
        dea_schedule=None,
        ndc_code="100174-0273-02"
    ),
    "100175": RxNormEntry(
        rxcui="100175",
        brand_name="Amoxicillin 500 mg [90 count bottle]",
        active_ingredient="Amoxicillin",
        strength="500 mg",
        dosage_form="Oral Capsule",
        drug_class="Penicillin",
        dea_schedule=None,
        ndc_code="100175-0274-02"
    ),
    "100176": RxNormEntry(
        rxcui="100176",
        brand_name="Amoxicillin 500 mg [100 unit dose blister]",
        active_ingredient="Amoxicillin",
        strength="500 mg",
        dosage_form="Oral Capsule",
        drug_class="Penicillin",
        dea_schedule=None,
        ndc_code="100176-0275-02"
    ),
    "100177": RxNormEntry(
        rxcui="100177",
        brand_name="Amoxicillin 875 mg",
        active_ingredient="Amoxicillin",
        strength="875 mg",
        dosage_form="Oral Capsule",
        drug_class="Penicillin",
        dea_schedule=None,
        ndc_code="100177-0276-01"
    ),
    "100178": RxNormEntry(
        rxcui="100178",
        brand_name="Amoxicillin 875 mg [30 count bottle]",
        active_ingredient="Amoxicillin",
        strength="875 mg",
        dosage_form="Oral Capsule",
        drug_class="Penicillin",
        dea_schedule=None,
        ndc_code="100178-0277-02"
    ),
    "100179": RxNormEntry(
        rxcui="100179",
        brand_name="Amoxicillin 875 mg [90 count bottle]",
        active_ingredient="Amoxicillin",
        strength="875 mg",
        dosage_form="Oral Capsule",
        drug_class="Penicillin",
        dea_schedule=None,
        ndc_code="100179-0278-02"
    ),
    "100180": RxNormEntry(
        rxcui="100180",
        brand_name="Amoxicillin 875 mg [100 unit dose blister]",
        active_ingredient="Amoxicillin",
        strength="875 mg",
        dosage_form="Oral Capsule",
        drug_class="Penicillin",
        dea_schedule=None,
        ndc_code="100180-0279-02"
    ),
    "100181": RxNormEntry(
        rxcui="100181",
        brand_name="Amoxicillin / Clavulanate 500/125 mg",
        active_ingredient="Amoxicillin / Clavulanate",
        strength="500/125 mg",
        dosage_form="Oral Tablet",
        drug_class="Penicillin Combination",
        dea_schedule=None,
        ndc_code="100181-0280-01"
    ),
    "100182": RxNormEntry(
        rxcui="100182",
        brand_name="Amoxicillin / Clavulanate 500/125 mg [30 count bottle]",
        active_ingredient="Amoxicillin / Clavulanate",
        strength="500/125 mg",
        dosage_form="Oral Tablet",
        drug_class="Penicillin Combination",
        dea_schedule=None,
        ndc_code="100182-0281-02"
    ),
    "100183": RxNormEntry(
        rxcui="100183",
        brand_name="Amoxicillin / Clavulanate 500/125 mg [90 count bottle]",
        active_ingredient="Amoxicillin / Clavulanate",
        strength="500/125 mg",
        dosage_form="Oral Tablet",
        drug_class="Penicillin Combination",
        dea_schedule=None,
        ndc_code="100183-0282-02"
    ),
    "100184": RxNormEntry(
        rxcui="100184",
        brand_name="Amoxicillin / Clavulanate 500/125 mg [100 unit dose blister]",
        active_ingredient="Amoxicillin / Clavulanate",
        strength="500/125 mg",
        dosage_form="Oral Tablet",
        drug_class="Penicillin Combination",
        dea_schedule=None,
        ndc_code="100184-0283-02"
    ),
    "100185": RxNormEntry(
        rxcui="100185",
        brand_name="Amoxicillin / Clavulanate 875/125 mg",
        active_ingredient="Amoxicillin / Clavulanate",
        strength="875/125 mg",
        dosage_form="Oral Tablet",
        drug_class="Penicillin Combination",
        dea_schedule=None,
        ndc_code="100185-0284-01"
    ),
    "100186": RxNormEntry(
        rxcui="100186",
        brand_name="Amoxicillin / Clavulanate 875/125 mg [30 count bottle]",
        active_ingredient="Amoxicillin / Clavulanate",
        strength="875/125 mg",
        dosage_form="Oral Tablet",
        drug_class="Penicillin Combination",
        dea_schedule=None,
        ndc_code="100186-0285-02"
    ),
    "100187": RxNormEntry(
        rxcui="100187",
        brand_name="Amoxicillin / Clavulanate 875/125 mg [90 count bottle]",
        active_ingredient="Amoxicillin / Clavulanate",
        strength="875/125 mg",
        dosage_form="Oral Tablet",
        drug_class="Penicillin Combination",
        dea_schedule=None,
        ndc_code="100187-0286-02"
    ),
    "100188": RxNormEntry(
        rxcui="100188",
        brand_name="Amoxicillin / Clavulanate 875/125 mg [100 unit dose blister]",
        active_ingredient="Amoxicillin / Clavulanate",
        strength="875/125 mg",
        dosage_form="Oral Tablet",
        drug_class="Penicillin Combination",
        dea_schedule=None,
        ndc_code="100188-0287-02"
    ),
    "100189": RxNormEntry(
        rxcui="100189",
        brand_name="Cephalexin 250 mg",
        active_ingredient="Cephalexin",
        strength="250 mg",
        dosage_form="Oral Capsule",
        drug_class="First Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100189-0288-01"
    ),
    "100190": RxNormEntry(
        rxcui="100190",
        brand_name="Cephalexin 250 mg [30 count bottle]",
        active_ingredient="Cephalexin",
        strength="250 mg",
        dosage_form="Oral Capsule",
        drug_class="First Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100190-0289-02"
    ),
    "100191": RxNormEntry(
        rxcui="100191",
        brand_name="Cephalexin 250 mg [90 count bottle]",
        active_ingredient="Cephalexin",
        strength="250 mg",
        dosage_form="Oral Capsule",
        drug_class="First Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100191-0290-02"
    ),
    "100192": RxNormEntry(
        rxcui="100192",
        brand_name="Cephalexin 250 mg [100 unit dose blister]",
        active_ingredient="Cephalexin",
        strength="250 mg",
        dosage_form="Oral Capsule",
        drug_class="First Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100192-0291-02"
    ),
    "100193": RxNormEntry(
        rxcui="100193",
        brand_name="Cephalexin 500 mg",
        active_ingredient="Cephalexin",
        strength="500 mg",
        dosage_form="Oral Capsule",
        drug_class="First Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100193-0292-01"
    ),
    "100194": RxNormEntry(
        rxcui="100194",
        brand_name="Cephalexin 500 mg [30 count bottle]",
        active_ingredient="Cephalexin",
        strength="500 mg",
        dosage_form="Oral Capsule",
        drug_class="First Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100194-0293-02"
    ),
    "100195": RxNormEntry(
        rxcui="100195",
        brand_name="Cephalexin 500 mg [90 count bottle]",
        active_ingredient="Cephalexin",
        strength="500 mg",
        dosage_form="Oral Capsule",
        drug_class="First Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100195-0294-02"
    ),
    "100196": RxNormEntry(
        rxcui="100196",
        brand_name="Cephalexin 500 mg [100 unit dose blister]",
        active_ingredient="Cephalexin",
        strength="500 mg",
        dosage_form="Oral Capsule",
        drug_class="First Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100196-0295-02"
    ),
    "100197": RxNormEntry(
        rxcui="100197",
        brand_name="Ceftriaxone 250 mg",
        active_ingredient="Ceftriaxone",
        strength="250 mg",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100197-0296-01"
    ),
    "100198": RxNormEntry(
        rxcui="100198",
        brand_name="Ceftriaxone 250 mg [30 count bottle]",
        active_ingredient="Ceftriaxone",
        strength="250 mg",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100198-0297-02"
    ),
    "100199": RxNormEntry(
        rxcui="100199",
        brand_name="Ceftriaxone 250 mg [90 count bottle]",
        active_ingredient="Ceftriaxone",
        strength="250 mg",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100199-0298-02"
    ),
    "100200": RxNormEntry(
        rxcui="100200",
        brand_name="Ceftriaxone 250 mg [100 unit dose blister]",
        active_ingredient="Ceftriaxone",
        strength="250 mg",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100200-0299-02"
    ),
    "100201": RxNormEntry(
        rxcui="100201",
        brand_name="Ceftriaxone 500 mg",
        active_ingredient="Ceftriaxone",
        strength="500 mg",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100201-0300-01"
    ),
    "100202": RxNormEntry(
        rxcui="100202",
        brand_name="Ceftriaxone 500 mg [30 count bottle]",
        active_ingredient="Ceftriaxone",
        strength="500 mg",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100202-0301-02"
    ),
    "100203": RxNormEntry(
        rxcui="100203",
        brand_name="Ceftriaxone 500 mg [90 count bottle]",
        active_ingredient="Ceftriaxone",
        strength="500 mg",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100203-0302-02"
    ),
    "100204": RxNormEntry(
        rxcui="100204",
        brand_name="Ceftriaxone 500 mg [100 unit dose blister]",
        active_ingredient="Ceftriaxone",
        strength="500 mg",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100204-0303-02"
    ),
    "100205": RxNormEntry(
        rxcui="100205",
        brand_name="Ceftriaxone 1 g",
        active_ingredient="Ceftriaxone",
        strength="1 g",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100205-0304-01"
    ),
    "100206": RxNormEntry(
        rxcui="100206",
        brand_name="Ceftriaxone 1 g [30 count bottle]",
        active_ingredient="Ceftriaxone",
        strength="1 g",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100206-0305-02"
    ),
    "100207": RxNormEntry(
        rxcui="100207",
        brand_name="Ceftriaxone 1 g [90 count bottle]",
        active_ingredient="Ceftriaxone",
        strength="1 g",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100207-0306-02"
    ),
    "100208": RxNormEntry(
        rxcui="100208",
        brand_name="Ceftriaxone 1 g [100 unit dose blister]",
        active_ingredient="Ceftriaxone",
        strength="1 g",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100208-0307-02"
    ),
    "100209": RxNormEntry(
        rxcui="100209",
        brand_name="Ceftriaxone 2 g",
        active_ingredient="Ceftriaxone",
        strength="2 g",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100209-0308-01"
    ),
    "100210": RxNormEntry(
        rxcui="100210",
        brand_name="Ceftriaxone 2 g [30 count bottle]",
        active_ingredient="Ceftriaxone",
        strength="2 g",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100210-0309-02"
    ),
    "100211": RxNormEntry(
        rxcui="100211",
        brand_name="Ceftriaxone 2 g [90 count bottle]",
        active_ingredient="Ceftriaxone",
        strength="2 g",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100211-0310-02"
    ),
    "100212": RxNormEntry(
        rxcui="100212",
        brand_name="Ceftriaxone 2 g [100 unit dose blister]",
        active_ingredient="Ceftriaxone",
        strength="2 g",
        dosage_form="Injectable Solution",
        drug_class="Third Gen Cephalosporin",
        dea_schedule=None,
        ndc_code="100212-0311-02"
    ),
    "100213": RxNormEntry(
        rxcui="100213",
        brand_name="Azithromycin 250 mg",
        active_ingredient="Azithromycin",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Macrolide",
        dea_schedule=None,
        ndc_code="100213-0312-01"
    ),
    "100214": RxNormEntry(
        rxcui="100214",
        brand_name="Azithromycin 250 mg [30 count bottle]",
        active_ingredient="Azithromycin",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Macrolide",
        dea_schedule=None,
        ndc_code="100214-0313-02"
    ),
    "100215": RxNormEntry(
        rxcui="100215",
        brand_name="Azithromycin 250 mg [90 count bottle]",
        active_ingredient="Azithromycin",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Macrolide",
        dea_schedule=None,
        ndc_code="100215-0314-02"
    ),
    "100216": RxNormEntry(
        rxcui="100216",
        brand_name="Azithromycin 250 mg [100 unit dose blister]",
        active_ingredient="Azithromycin",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Macrolide",
        dea_schedule=None,
        ndc_code="100216-0315-02"
    ),
    "100217": RxNormEntry(
        rxcui="100217",
        brand_name="Azithromycin 500 mg",
        active_ingredient="Azithromycin",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Macrolide",
        dea_schedule=None,
        ndc_code="100217-0316-01"
    ),
    "100218": RxNormEntry(
        rxcui="100218",
        brand_name="Azithromycin 500 mg [30 count bottle]",
        active_ingredient="Azithromycin",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Macrolide",
        dea_schedule=None,
        ndc_code="100218-0317-02"
    ),
    "100219": RxNormEntry(
        rxcui="100219",
        brand_name="Azithromycin 500 mg [90 count bottle]",
        active_ingredient="Azithromycin",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Macrolide",
        dea_schedule=None,
        ndc_code="100219-0318-02"
    ),
    "100220": RxNormEntry(
        rxcui="100220",
        brand_name="Azithromycin 500 mg [100 unit dose blister]",
        active_ingredient="Azithromycin",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Macrolide",
        dea_schedule=None,
        ndc_code="100220-0319-02"
    ),
    "100221": RxNormEntry(
        rxcui="100221",
        brand_name="Ciprofloxacin 250 mg",
        active_ingredient="Ciprofloxacin",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100221-0320-01"
    ),
    "100222": RxNormEntry(
        rxcui="100222",
        brand_name="Ciprofloxacin 250 mg [30 count bottle]",
        active_ingredient="Ciprofloxacin",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100222-0321-02"
    ),
    "100223": RxNormEntry(
        rxcui="100223",
        brand_name="Ciprofloxacin 250 mg [90 count bottle]",
        active_ingredient="Ciprofloxacin",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100223-0322-02"
    ),
    "100224": RxNormEntry(
        rxcui="100224",
        brand_name="Ciprofloxacin 250 mg [100 unit dose blister]",
        active_ingredient="Ciprofloxacin",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100224-0323-02"
    ),
    "100225": RxNormEntry(
        rxcui="100225",
        brand_name="Ciprofloxacin 500 mg",
        active_ingredient="Ciprofloxacin",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100225-0324-01"
    ),
    "100226": RxNormEntry(
        rxcui="100226",
        brand_name="Ciprofloxacin 500 mg [30 count bottle]",
        active_ingredient="Ciprofloxacin",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100226-0325-02"
    ),
    "100227": RxNormEntry(
        rxcui="100227",
        brand_name="Ciprofloxacin 500 mg [90 count bottle]",
        active_ingredient="Ciprofloxacin",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100227-0326-02"
    ),
    "100228": RxNormEntry(
        rxcui="100228",
        brand_name="Ciprofloxacin 500 mg [100 unit dose blister]",
        active_ingredient="Ciprofloxacin",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100228-0327-02"
    ),
    "100229": RxNormEntry(
        rxcui="100229",
        brand_name="Ciprofloxacin 750 mg",
        active_ingredient="Ciprofloxacin",
        strength="750 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100229-0328-01"
    ),
    "100230": RxNormEntry(
        rxcui="100230",
        brand_name="Ciprofloxacin 750 mg [30 count bottle]",
        active_ingredient="Ciprofloxacin",
        strength="750 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100230-0329-02"
    ),
    "100231": RxNormEntry(
        rxcui="100231",
        brand_name="Ciprofloxacin 750 mg [90 count bottle]",
        active_ingredient="Ciprofloxacin",
        strength="750 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100231-0330-02"
    ),
    "100232": RxNormEntry(
        rxcui="100232",
        brand_name="Ciprofloxacin 750 mg [100 unit dose blister]",
        active_ingredient="Ciprofloxacin",
        strength="750 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100232-0331-02"
    ),
    "100233": RxNormEntry(
        rxcui="100233",
        brand_name="Levofloxacin 250 mg",
        active_ingredient="Levofloxacin",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100233-0332-01"
    ),
    "100234": RxNormEntry(
        rxcui="100234",
        brand_name="Levofloxacin 250 mg [30 count bottle]",
        active_ingredient="Levofloxacin",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100234-0333-02"
    ),
    "100235": RxNormEntry(
        rxcui="100235",
        brand_name="Levofloxacin 250 mg [90 count bottle]",
        active_ingredient="Levofloxacin",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100235-0334-02"
    ),
    "100236": RxNormEntry(
        rxcui="100236",
        brand_name="Levofloxacin 250 mg [100 unit dose blister]",
        active_ingredient="Levofloxacin",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100236-0335-02"
    ),
    "100237": RxNormEntry(
        rxcui="100237",
        brand_name="Levofloxacin 500 mg",
        active_ingredient="Levofloxacin",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100237-0336-01"
    ),
    "100238": RxNormEntry(
        rxcui="100238",
        brand_name="Levofloxacin 500 mg [30 count bottle]",
        active_ingredient="Levofloxacin",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100238-0337-02"
    ),
    "100239": RxNormEntry(
        rxcui="100239",
        brand_name="Levofloxacin 500 mg [90 count bottle]",
        active_ingredient="Levofloxacin",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100239-0338-02"
    ),
    "100240": RxNormEntry(
        rxcui="100240",
        brand_name="Levofloxacin 500 mg [100 unit dose blister]",
        active_ingredient="Levofloxacin",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100240-0339-02"
    ),
    "100241": RxNormEntry(
        rxcui="100241",
        brand_name="Levofloxacin 750 mg",
        active_ingredient="Levofloxacin",
        strength="750 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100241-0340-01"
    ),
    "100242": RxNormEntry(
        rxcui="100242",
        brand_name="Levofloxacin 750 mg [30 count bottle]",
        active_ingredient="Levofloxacin",
        strength="750 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100242-0341-02"
    ),
    "100243": RxNormEntry(
        rxcui="100243",
        brand_name="Levofloxacin 750 mg [90 count bottle]",
        active_ingredient="Levofloxacin",
        strength="750 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100243-0342-02"
    ),
    "100244": RxNormEntry(
        rxcui="100244",
        brand_name="Levofloxacin 750 mg [100 unit dose blister]",
        active_ingredient="Levofloxacin",
        strength="750 mg",
        dosage_form="Oral Tablet",
        drug_class="Fluoroquinolone",
        dea_schedule=None,
        ndc_code="100244-0343-02"
    ),
    "100245": RxNormEntry(
        rxcui="100245",
        brand_name="Doxycycline Hyclate 50 mg",
        active_ingredient="Doxycycline Hyclate",
        strength="50 mg",
        dosage_form="Oral Capsule",
        drug_class="Tetracycline",
        dea_schedule=None,
        ndc_code="100245-0344-01"
    ),
    "100246": RxNormEntry(
        rxcui="100246",
        brand_name="Doxycycline Hyclate 50 mg [30 count bottle]",
        active_ingredient="Doxycycline Hyclate",
        strength="50 mg",
        dosage_form="Oral Capsule",
        drug_class="Tetracycline",
        dea_schedule=None,
        ndc_code="100246-0345-02"
    ),
    "100247": RxNormEntry(
        rxcui="100247",
        brand_name="Doxycycline Hyclate 50 mg [90 count bottle]",
        active_ingredient="Doxycycline Hyclate",
        strength="50 mg",
        dosage_form="Oral Capsule",
        drug_class="Tetracycline",
        dea_schedule=None,
        ndc_code="100247-0346-02"
    ),
    "100248": RxNormEntry(
        rxcui="100248",
        brand_name="Doxycycline Hyclate 50 mg [100 unit dose blister]",
        active_ingredient="Doxycycline Hyclate",
        strength="50 mg",
        dosage_form="Oral Capsule",
        drug_class="Tetracycline",
        dea_schedule=None,
        ndc_code="100248-0347-02"
    ),
    "100249": RxNormEntry(
        rxcui="100249",
        brand_name="Doxycycline Hyclate 100 mg",
        active_ingredient="Doxycycline Hyclate",
        strength="100 mg",
        dosage_form="Oral Capsule",
        drug_class="Tetracycline",
        dea_schedule=None,
        ndc_code="100249-0348-01"
    ),
    "100250": RxNormEntry(
        rxcui="100250",
        brand_name="Doxycycline Hyclate 100 mg [30 count bottle]",
        active_ingredient="Doxycycline Hyclate",
        strength="100 mg",
        dosage_form="Oral Capsule",
        drug_class="Tetracycline",
        dea_schedule=None,
        ndc_code="100250-0349-02"
    ),
    "100251": RxNormEntry(
        rxcui="100251",
        brand_name="Doxycycline Hyclate 100 mg [90 count bottle]",
        active_ingredient="Doxycycline Hyclate",
        strength="100 mg",
        dosage_form="Oral Capsule",
        drug_class="Tetracycline",
        dea_schedule=None,
        ndc_code="100251-0350-02"
    ),
    "100252": RxNormEntry(
        rxcui="100252",
        brand_name="Doxycycline Hyclate 100 mg [100 unit dose blister]",
        active_ingredient="Doxycycline Hyclate",
        strength="100 mg",
        dosage_form="Oral Capsule",
        drug_class="Tetracycline",
        dea_schedule=None,
        ndc_code="100252-0351-02"
    ),
    "100253": RxNormEntry(
        rxcui="100253",
        brand_name="Vancomycin Hydrochloride 500 mg",
        active_ingredient="Vancomycin Hydrochloride",
        strength="500 mg",
        dosage_form="Intravenous Solution",
        drug_class="Glycopeptide",
        dea_schedule=None,
        ndc_code="100253-0352-01"
    ),
    "100254": RxNormEntry(
        rxcui="100254",
        brand_name="Vancomycin Hydrochloride 500 mg [30 count bottle]",
        active_ingredient="Vancomycin Hydrochloride",
        strength="500 mg",
        dosage_form="Intravenous Solution",
        drug_class="Glycopeptide",
        dea_schedule=None,
        ndc_code="100254-0353-02"
    ),
    "100255": RxNormEntry(
        rxcui="100255",
        brand_name="Vancomycin Hydrochloride 500 mg [90 count bottle]",
        active_ingredient="Vancomycin Hydrochloride",
        strength="500 mg",
        dosage_form="Intravenous Solution",
        drug_class="Glycopeptide",
        dea_schedule=None,
        ndc_code="100255-0354-02"
    ),
    "100256": RxNormEntry(
        rxcui="100256",
        brand_name="Vancomycin Hydrochloride 500 mg [100 unit dose blister]",
        active_ingredient="Vancomycin Hydrochloride",
        strength="500 mg",
        dosage_form="Intravenous Solution",
        drug_class="Glycopeptide",
        dea_schedule=None,
        ndc_code="100256-0355-02"
    ),
    "100257": RxNormEntry(
        rxcui="100257",
        brand_name="Vancomycin Hydrochloride 1 g",
        active_ingredient="Vancomycin Hydrochloride",
        strength="1 g",
        dosage_form="Intravenous Solution",
        drug_class="Glycopeptide",
        dea_schedule=None,
        ndc_code="100257-0356-01"
    ),
    "100258": RxNormEntry(
        rxcui="100258",
        brand_name="Vancomycin Hydrochloride 1 g [30 count bottle]",
        active_ingredient="Vancomycin Hydrochloride",
        strength="1 g",
        dosage_form="Intravenous Solution",
        drug_class="Glycopeptide",
        dea_schedule=None,
        ndc_code="100258-0357-02"
    ),
    "100259": RxNormEntry(
        rxcui="100259",
        brand_name="Vancomycin Hydrochloride 1 g [90 count bottle]",
        active_ingredient="Vancomycin Hydrochloride",
        strength="1 g",
        dosage_form="Intravenous Solution",
        drug_class="Glycopeptide",
        dea_schedule=None,
        ndc_code="100259-0358-02"
    ),
    "100260": RxNormEntry(
        rxcui="100260",
        brand_name="Vancomycin Hydrochloride 1 g [100 unit dose blister]",
        active_ingredient="Vancomycin Hydrochloride",
        strength="1 g",
        dosage_form="Intravenous Solution",
        drug_class="Glycopeptide",
        dea_schedule=None,
        ndc_code="100260-0359-02"
    ),
    "100261": RxNormEntry(
        rxcui="100261",
        brand_name="Vancomycin Hydrochloride 1.5 g",
        active_ingredient="Vancomycin Hydrochloride",
        strength="1.5 g",
        dosage_form="Intravenous Solution",
        drug_class="Glycopeptide",
        dea_schedule=None,
        ndc_code="100261-0360-01"
    ),
    "100262": RxNormEntry(
        rxcui="100262",
        brand_name="Vancomycin Hydrochloride 1.5 g [30 count bottle]",
        active_ingredient="Vancomycin Hydrochloride",
        strength="1.5 g",
        dosage_form="Intravenous Solution",
        drug_class="Glycopeptide",
        dea_schedule=None,
        ndc_code="100262-0361-02"
    ),
    "100263": RxNormEntry(
        rxcui="100263",
        brand_name="Vancomycin Hydrochloride 1.5 g [90 count bottle]",
        active_ingredient="Vancomycin Hydrochloride",
        strength="1.5 g",
        dosage_form="Intravenous Solution",
        drug_class="Glycopeptide",
        dea_schedule=None,
        ndc_code="100263-0362-02"
    ),
    "100264": RxNormEntry(
        rxcui="100264",
        brand_name="Vancomycin Hydrochloride 1.5 g [100 unit dose blister]",
        active_ingredient="Vancomycin Hydrochloride",
        strength="1.5 g",
        dosage_form="Intravenous Solution",
        drug_class="Glycopeptide",
        dea_schedule=None,
        ndc_code="100264-0363-02"
    ),
    "100265": RxNormEntry(
        rxcui="100265",
        brand_name="Acetaminophen 325 mg",
        active_ingredient="Acetaminophen",
        strength="325 mg",
        dosage_form="Oral Tablet",
        drug_class="Non-opioid Analgesic",
        dea_schedule=None,
        ndc_code="100265-0364-01"
    ),
    "100266": RxNormEntry(
        rxcui="100266",
        brand_name="Acetaminophen 325 mg [30 count bottle]",
        active_ingredient="Acetaminophen",
        strength="325 mg",
        dosage_form="Oral Tablet",
        drug_class="Non-opioid Analgesic",
        dea_schedule=None,
        ndc_code="100266-0365-02"
    ),
    "100267": RxNormEntry(
        rxcui="100267",
        brand_name="Acetaminophen 325 mg [90 count bottle]",
        active_ingredient="Acetaminophen",
        strength="325 mg",
        dosage_form="Oral Tablet",
        drug_class="Non-opioid Analgesic",
        dea_schedule=None,
        ndc_code="100267-0366-02"
    ),
    "100268": RxNormEntry(
        rxcui="100268",
        brand_name="Acetaminophen 325 mg [100 unit dose blister]",
        active_ingredient="Acetaminophen",
        strength="325 mg",
        dosage_form="Oral Tablet",
        drug_class="Non-opioid Analgesic",
        dea_schedule=None,
        ndc_code="100268-0367-02"
    ),
    "100269": RxNormEntry(
        rxcui="100269",
        brand_name="Acetaminophen 500 mg",
        active_ingredient="Acetaminophen",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Non-opioid Analgesic",
        dea_schedule=None,
        ndc_code="100269-0368-01"
    ),
    "100270": RxNormEntry(
        rxcui="100270",
        brand_name="Acetaminophen 500 mg [30 count bottle]",
        active_ingredient="Acetaminophen",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Non-opioid Analgesic",
        dea_schedule=None,
        ndc_code="100270-0369-02"
    ),
    "100271": RxNormEntry(
        rxcui="100271",
        brand_name="Acetaminophen 500 mg [90 count bottle]",
        active_ingredient="Acetaminophen",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Non-opioid Analgesic",
        dea_schedule=None,
        ndc_code="100271-0370-02"
    ),
    "100272": RxNormEntry(
        rxcui="100272",
        brand_name="Acetaminophen 500 mg [100 unit dose blister]",
        active_ingredient="Acetaminophen",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Non-opioid Analgesic",
        dea_schedule=None,
        ndc_code="100272-0371-02"
    ),
    "100273": RxNormEntry(
        rxcui="100273",
        brand_name="Acetaminophen 650 mg",
        active_ingredient="Acetaminophen",
        strength="650 mg",
        dosage_form="Oral Tablet",
        drug_class="Non-opioid Analgesic",
        dea_schedule=None,
        ndc_code="100273-0372-01"
    ),
    "100274": RxNormEntry(
        rxcui="100274",
        brand_name="Acetaminophen 650 mg [30 count bottle]",
        active_ingredient="Acetaminophen",
        strength="650 mg",
        dosage_form="Oral Tablet",
        drug_class="Non-opioid Analgesic",
        dea_schedule=None,
        ndc_code="100274-0373-02"
    ),
    "100275": RxNormEntry(
        rxcui="100275",
        brand_name="Acetaminophen 650 mg [90 count bottle]",
        active_ingredient="Acetaminophen",
        strength="650 mg",
        dosage_form="Oral Tablet",
        drug_class="Non-opioid Analgesic",
        dea_schedule=None,
        ndc_code="100275-0374-02"
    ),
    "100276": RxNormEntry(
        rxcui="100276",
        brand_name="Acetaminophen 650 mg [100 unit dose blister]",
        active_ingredient="Acetaminophen",
        strength="650 mg",
        dosage_form="Oral Tablet",
        drug_class="Non-opioid Analgesic",
        dea_schedule=None,
        ndc_code="100276-0375-02"
    ),
    "100277": RxNormEntry(
        rxcui="100277",
        brand_name="Ibuprofen 200 mg",
        active_ingredient="Ibuprofen",
        strength="200 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100277-0376-01"
    ),
    "100278": RxNormEntry(
        rxcui="100278",
        brand_name="Ibuprofen 200 mg [30 count bottle]",
        active_ingredient="Ibuprofen",
        strength="200 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100278-0377-02"
    ),
    "100279": RxNormEntry(
        rxcui="100279",
        brand_name="Ibuprofen 200 mg [90 count bottle]",
        active_ingredient="Ibuprofen",
        strength="200 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100279-0378-02"
    ),
    "100280": RxNormEntry(
        rxcui="100280",
        brand_name="Ibuprofen 200 mg [100 unit dose blister]",
        active_ingredient="Ibuprofen",
        strength="200 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100280-0379-02"
    ),
    "100281": RxNormEntry(
        rxcui="100281",
        brand_name="Ibuprofen 400 mg",
        active_ingredient="Ibuprofen",
        strength="400 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100281-0380-01"
    ),
    "100282": RxNormEntry(
        rxcui="100282",
        brand_name="Ibuprofen 400 mg [30 count bottle]",
        active_ingredient="Ibuprofen",
        strength="400 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100282-0381-02"
    ),
    "100283": RxNormEntry(
        rxcui="100283",
        brand_name="Ibuprofen 400 mg [90 count bottle]",
        active_ingredient="Ibuprofen",
        strength="400 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100283-0382-02"
    ),
    "100284": RxNormEntry(
        rxcui="100284",
        brand_name="Ibuprofen 400 mg [100 unit dose blister]",
        active_ingredient="Ibuprofen",
        strength="400 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100284-0383-02"
    ),
    "100285": RxNormEntry(
        rxcui="100285",
        brand_name="Ibuprofen 600 mg",
        active_ingredient="Ibuprofen",
        strength="600 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100285-0384-01"
    ),
    "100286": RxNormEntry(
        rxcui="100286",
        brand_name="Ibuprofen 600 mg [30 count bottle]",
        active_ingredient="Ibuprofen",
        strength="600 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100286-0385-02"
    ),
    "100287": RxNormEntry(
        rxcui="100287",
        brand_name="Ibuprofen 600 mg [90 count bottle]",
        active_ingredient="Ibuprofen",
        strength="600 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100287-0386-02"
    ),
    "100288": RxNormEntry(
        rxcui="100288",
        brand_name="Ibuprofen 600 mg [100 unit dose blister]",
        active_ingredient="Ibuprofen",
        strength="600 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100288-0387-02"
    ),
    "100289": RxNormEntry(
        rxcui="100289",
        brand_name="Ibuprofen 800 mg",
        active_ingredient="Ibuprofen",
        strength="800 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100289-0388-01"
    ),
    "100290": RxNormEntry(
        rxcui="100290",
        brand_name="Ibuprofen 800 mg [30 count bottle]",
        active_ingredient="Ibuprofen",
        strength="800 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100290-0389-02"
    ),
    "100291": RxNormEntry(
        rxcui="100291",
        brand_name="Ibuprofen 800 mg [90 count bottle]",
        active_ingredient="Ibuprofen",
        strength="800 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100291-0390-02"
    ),
    "100292": RxNormEntry(
        rxcui="100292",
        brand_name="Ibuprofen 800 mg [100 unit dose blister]",
        active_ingredient="Ibuprofen",
        strength="800 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100292-0391-02"
    ),
    "100293": RxNormEntry(
        rxcui="100293",
        brand_name="Naproxen 250 mg",
        active_ingredient="Naproxen",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100293-0392-01"
    ),
    "100294": RxNormEntry(
        rxcui="100294",
        brand_name="Naproxen 250 mg [30 count bottle]",
        active_ingredient="Naproxen",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100294-0393-02"
    ),
    "100295": RxNormEntry(
        rxcui="100295",
        brand_name="Naproxen 250 mg [90 count bottle]",
        active_ingredient="Naproxen",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100295-0394-02"
    ),
    "100296": RxNormEntry(
        rxcui="100296",
        brand_name="Naproxen 250 mg [100 unit dose blister]",
        active_ingredient="Naproxen",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100296-0395-02"
    ),
    "100297": RxNormEntry(
        rxcui="100297",
        brand_name="Naproxen 375 mg",
        active_ingredient="Naproxen",
        strength="375 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100297-0396-01"
    ),
    "100298": RxNormEntry(
        rxcui="100298",
        brand_name="Naproxen 375 mg [30 count bottle]",
        active_ingredient="Naproxen",
        strength="375 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100298-0397-02"
    ),
    "100299": RxNormEntry(
        rxcui="100299",
        brand_name="Naproxen 375 mg [90 count bottle]",
        active_ingredient="Naproxen",
        strength="375 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100299-0398-02"
    ),
    "100300": RxNormEntry(
        rxcui="100300",
        brand_name="Naproxen 375 mg [100 unit dose blister]",
        active_ingredient="Naproxen",
        strength="375 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100300-0399-02"
    ),
    "100301": RxNormEntry(
        rxcui="100301",
        brand_name="Naproxen 500 mg",
        active_ingredient="Naproxen",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100301-0400-01"
    ),
    "100302": RxNormEntry(
        rxcui="100302",
        brand_name="Naproxen 500 mg [30 count bottle]",
        active_ingredient="Naproxen",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100302-0401-02"
    ),
    "100303": RxNormEntry(
        rxcui="100303",
        brand_name="Naproxen 500 mg [90 count bottle]",
        active_ingredient="Naproxen",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100303-0402-02"
    ),
    "100304": RxNormEntry(
        rxcui="100304",
        brand_name="Naproxen 500 mg [100 unit dose blister]",
        active_ingredient="Naproxen",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100304-0403-02"
    ),
    "100305": RxNormEntry(
        rxcui="100305",
        brand_name="Meloxicam 7.5 mg",
        active_ingredient="Meloxicam",
        strength="7.5 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100305-0404-01"
    ),
    "100306": RxNormEntry(
        rxcui="100306",
        brand_name="Meloxicam 7.5 mg [30 count bottle]",
        active_ingredient="Meloxicam",
        strength="7.5 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100306-0405-02"
    ),
    "100307": RxNormEntry(
        rxcui="100307",
        brand_name="Meloxicam 7.5 mg [90 count bottle]",
        active_ingredient="Meloxicam",
        strength="7.5 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100307-0406-02"
    ),
    "100308": RxNormEntry(
        rxcui="100308",
        brand_name="Meloxicam 7.5 mg [100 unit dose blister]",
        active_ingredient="Meloxicam",
        strength="7.5 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100308-0407-02"
    ),
    "100309": RxNormEntry(
        rxcui="100309",
        brand_name="Meloxicam 15 mg",
        active_ingredient="Meloxicam",
        strength="15 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100309-0408-01"
    ),
    "100310": RxNormEntry(
        rxcui="100310",
        brand_name="Meloxicam 15 mg [30 count bottle]",
        active_ingredient="Meloxicam",
        strength="15 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100310-0409-02"
    ),
    "100311": RxNormEntry(
        rxcui="100311",
        brand_name="Meloxicam 15 mg [90 count bottle]",
        active_ingredient="Meloxicam",
        strength="15 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100311-0410-02"
    ),
    "100312": RxNormEntry(
        rxcui="100312",
        brand_name="Meloxicam 15 mg [100 unit dose blister]",
        active_ingredient="Meloxicam",
        strength="15 mg",
        dosage_form="Oral Tablet",
        drug_class="NSAID",
        dea_schedule=None,
        ndc_code="100312-0411-02"
    ),
    "100313": RxNormEntry(
        rxcui="100313",
        brand_name="Tramadol Hydrochloride 50 mg",
        active_ingredient="Tramadol Hydrochloride",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule IV",
        ndc_code="100313-0412-01"
    ),
    "100314": RxNormEntry(
        rxcui="100314",
        brand_name="Tramadol Hydrochloride 50 mg [30 count bottle]",
        active_ingredient="Tramadol Hydrochloride",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule IV",
        ndc_code="100314-0413-02"
    ),
    "100315": RxNormEntry(
        rxcui="100315",
        brand_name="Tramadol Hydrochloride 50 mg [90 count bottle]",
        active_ingredient="Tramadol Hydrochloride",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule IV",
        ndc_code="100315-0414-02"
    ),
    "100316": RxNormEntry(
        rxcui="100316",
        brand_name="Tramadol Hydrochloride 50 mg [100 unit dose blister]",
        active_ingredient="Tramadol Hydrochloride",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule IV",
        ndc_code="100316-0415-02"
    ),
    "100317": RxNormEntry(
        rxcui="100317",
        brand_name="Oxycodone Hydrochloride 5 mg",
        active_ingredient="Oxycodone Hydrochloride",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100317-0416-01"
    ),
    "100318": RxNormEntry(
        rxcui="100318",
        brand_name="Oxycodone Hydrochloride 5 mg [30 count bottle]",
        active_ingredient="Oxycodone Hydrochloride",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100318-0417-02"
    ),
    "100319": RxNormEntry(
        rxcui="100319",
        brand_name="Oxycodone Hydrochloride 5 mg [90 count bottle]",
        active_ingredient="Oxycodone Hydrochloride",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100319-0418-02"
    ),
    "100320": RxNormEntry(
        rxcui="100320",
        brand_name="Oxycodone Hydrochloride 5 mg [100 unit dose blister]",
        active_ingredient="Oxycodone Hydrochloride",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100320-0419-02"
    ),
    "100321": RxNormEntry(
        rxcui="100321",
        brand_name="Oxycodone Hydrochloride 10 mg",
        active_ingredient="Oxycodone Hydrochloride",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100321-0420-01"
    ),
    "100322": RxNormEntry(
        rxcui="100322",
        brand_name="Oxycodone Hydrochloride 10 mg [30 count bottle]",
        active_ingredient="Oxycodone Hydrochloride",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100322-0421-02"
    ),
    "100323": RxNormEntry(
        rxcui="100323",
        brand_name="Oxycodone Hydrochloride 10 mg [90 count bottle]",
        active_ingredient="Oxycodone Hydrochloride",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100323-0422-02"
    ),
    "100324": RxNormEntry(
        rxcui="100324",
        brand_name="Oxycodone Hydrochloride 10 mg [100 unit dose blister]",
        active_ingredient="Oxycodone Hydrochloride",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100324-0423-02"
    ),
    "100325": RxNormEntry(
        rxcui="100325",
        brand_name="Oxycodone Hydrochloride 15 mg",
        active_ingredient="Oxycodone Hydrochloride",
        strength="15 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100325-0424-01"
    ),
    "100326": RxNormEntry(
        rxcui="100326",
        brand_name="Oxycodone Hydrochloride 15 mg [30 count bottle]",
        active_ingredient="Oxycodone Hydrochloride",
        strength="15 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100326-0425-02"
    ),
    "100327": RxNormEntry(
        rxcui="100327",
        brand_name="Oxycodone Hydrochloride 15 mg [90 count bottle]",
        active_ingredient="Oxycodone Hydrochloride",
        strength="15 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100327-0426-02"
    ),
    "100328": RxNormEntry(
        rxcui="100328",
        brand_name="Oxycodone Hydrochloride 15 mg [100 unit dose blister]",
        active_ingredient="Oxycodone Hydrochloride",
        strength="15 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100328-0427-02"
    ),
    "100329": RxNormEntry(
        rxcui="100329",
        brand_name="Oxycodone Hydrochloride 20 mg",
        active_ingredient="Oxycodone Hydrochloride",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100329-0428-01"
    ),
    "100330": RxNormEntry(
        rxcui="100330",
        brand_name="Oxycodone Hydrochloride 20 mg [30 count bottle]",
        active_ingredient="Oxycodone Hydrochloride",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100330-0429-02"
    ),
    "100331": RxNormEntry(
        rxcui="100331",
        brand_name="Oxycodone Hydrochloride 20 mg [90 count bottle]",
        active_ingredient="Oxycodone Hydrochloride",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100331-0430-02"
    ),
    "100332": RxNormEntry(
        rxcui="100332",
        brand_name="Oxycodone Hydrochloride 20 mg [100 unit dose blister]",
        active_ingredient="Oxycodone Hydrochloride",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100332-0431-02"
    ),
    "100333": RxNormEntry(
        rxcui="100333",
        brand_name="Morphine Sulfate 15 mg",
        active_ingredient="Morphine Sulfate",
        strength="15 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100333-0432-01"
    ),
    "100334": RxNormEntry(
        rxcui="100334",
        brand_name="Morphine Sulfate 15 mg [30 count bottle]",
        active_ingredient="Morphine Sulfate",
        strength="15 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100334-0433-02"
    ),
    "100335": RxNormEntry(
        rxcui="100335",
        brand_name="Morphine Sulfate 15 mg [90 count bottle]",
        active_ingredient="Morphine Sulfate",
        strength="15 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100335-0434-02"
    ),
    "100336": RxNormEntry(
        rxcui="100336",
        brand_name="Morphine Sulfate 15 mg [100 unit dose blister]",
        active_ingredient="Morphine Sulfate",
        strength="15 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100336-0435-02"
    ),
    "100337": RxNormEntry(
        rxcui="100337",
        brand_name="Morphine Sulfate 30 mg",
        active_ingredient="Morphine Sulfate",
        strength="30 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100337-0436-01"
    ),
    "100338": RxNormEntry(
        rxcui="100338",
        brand_name="Morphine Sulfate 30 mg [30 count bottle]",
        active_ingredient="Morphine Sulfate",
        strength="30 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100338-0437-02"
    ),
    "100339": RxNormEntry(
        rxcui="100339",
        brand_name="Morphine Sulfate 30 mg [90 count bottle]",
        active_ingredient="Morphine Sulfate",
        strength="30 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100339-0438-02"
    ),
    "100340": RxNormEntry(
        rxcui="100340",
        brand_name="Morphine Sulfate 30 mg [100 unit dose blister]",
        active_ingredient="Morphine Sulfate",
        strength="30 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100340-0439-02"
    ),
    "100341": RxNormEntry(
        rxcui="100341",
        brand_name="Morphine Sulfate 60 mg",
        active_ingredient="Morphine Sulfate",
        strength="60 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100341-0440-01"
    ),
    "100342": RxNormEntry(
        rxcui="100342",
        brand_name="Morphine Sulfate 60 mg [30 count bottle]",
        active_ingredient="Morphine Sulfate",
        strength="60 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100342-0441-02"
    ),
    "100343": RxNormEntry(
        rxcui="100343",
        brand_name="Morphine Sulfate 60 mg [90 count bottle]",
        active_ingredient="Morphine Sulfate",
        strength="60 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100343-0442-02"
    ),
    "100344": RxNormEntry(
        rxcui="100344",
        brand_name="Morphine Sulfate 60 mg [100 unit dose blister]",
        active_ingredient="Morphine Sulfate",
        strength="60 mg",
        dosage_form="Oral Tablet",
        drug_class="Opioid Analgesic",
        dea_schedule="Schedule II",
        ndc_code="100344-0443-02"
    ),
    "100345": RxNormEntry(
        rxcui="100345",
        brand_name="Sertraline Hydrochloride 25 mg",
        active_ingredient="Sertraline Hydrochloride",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100345-0444-01"
    ),
    "100346": RxNormEntry(
        rxcui="100346",
        brand_name="Sertraline Hydrochloride 25 mg [30 count bottle]",
        active_ingredient="Sertraline Hydrochloride",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100346-0445-02"
    ),
    "100347": RxNormEntry(
        rxcui="100347",
        brand_name="Sertraline Hydrochloride 25 mg [90 count bottle]",
        active_ingredient="Sertraline Hydrochloride",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100347-0446-02"
    ),
    "100348": RxNormEntry(
        rxcui="100348",
        brand_name="Sertraline Hydrochloride 25 mg [100 unit dose blister]",
        active_ingredient="Sertraline Hydrochloride",
        strength="25 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100348-0447-02"
    ),
    "100349": RxNormEntry(
        rxcui="100349",
        brand_name="Sertraline Hydrochloride 50 mg",
        active_ingredient="Sertraline Hydrochloride",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100349-0448-01"
    ),
    "100350": RxNormEntry(
        rxcui="100350",
        brand_name="Sertraline Hydrochloride 50 mg [30 count bottle]",
        active_ingredient="Sertraline Hydrochloride",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100350-0449-02"
    ),
    "100351": RxNormEntry(
        rxcui="100351",
        brand_name="Sertraline Hydrochloride 50 mg [90 count bottle]",
        active_ingredient="Sertraline Hydrochloride",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100351-0450-02"
    ),
    "100352": RxNormEntry(
        rxcui="100352",
        brand_name="Sertraline Hydrochloride 50 mg [100 unit dose blister]",
        active_ingredient="Sertraline Hydrochloride",
        strength="50 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100352-0451-02"
    ),
    "100353": RxNormEntry(
        rxcui="100353",
        brand_name="Sertraline Hydrochloride 100 mg",
        active_ingredient="Sertraline Hydrochloride",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100353-0452-01"
    ),
    "100354": RxNormEntry(
        rxcui="100354",
        brand_name="Sertraline Hydrochloride 100 mg [30 count bottle]",
        active_ingredient="Sertraline Hydrochloride",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100354-0453-02"
    ),
    "100355": RxNormEntry(
        rxcui="100355",
        brand_name="Sertraline Hydrochloride 100 mg [90 count bottle]",
        active_ingredient="Sertraline Hydrochloride",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100355-0454-02"
    ),
    "100356": RxNormEntry(
        rxcui="100356",
        brand_name="Sertraline Hydrochloride 100 mg [100 unit dose blister]",
        active_ingredient="Sertraline Hydrochloride",
        strength="100 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100356-0455-02"
    ),
    "100357": RxNormEntry(
        rxcui="100357",
        brand_name="Fluoxetine Hydrochloride 10 mg",
        active_ingredient="Fluoxetine Hydrochloride",
        strength="10 mg",
        dosage_form="Oral Capsule",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100357-0456-01"
    ),
    "100358": RxNormEntry(
        rxcui="100358",
        brand_name="Fluoxetine Hydrochloride 10 mg [30 count bottle]",
        active_ingredient="Fluoxetine Hydrochloride",
        strength="10 mg",
        dosage_form="Oral Capsule",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100358-0457-02"
    ),
    "100359": RxNormEntry(
        rxcui="100359",
        brand_name="Fluoxetine Hydrochloride 10 mg [90 count bottle]",
        active_ingredient="Fluoxetine Hydrochloride",
        strength="10 mg",
        dosage_form="Oral Capsule",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100359-0458-02"
    ),
    "100360": RxNormEntry(
        rxcui="100360",
        brand_name="Fluoxetine Hydrochloride 10 mg [100 unit dose blister]",
        active_ingredient="Fluoxetine Hydrochloride",
        strength="10 mg",
        dosage_form="Oral Capsule",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100360-0459-02"
    ),
    "100361": RxNormEntry(
        rxcui="100361",
        brand_name="Fluoxetine Hydrochloride 20 mg",
        active_ingredient="Fluoxetine Hydrochloride",
        strength="20 mg",
        dosage_form="Oral Capsule",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100361-0460-01"
    ),
    "100362": RxNormEntry(
        rxcui="100362",
        brand_name="Fluoxetine Hydrochloride 20 mg [30 count bottle]",
        active_ingredient="Fluoxetine Hydrochloride",
        strength="20 mg",
        dosage_form="Oral Capsule",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100362-0461-02"
    ),
    "100363": RxNormEntry(
        rxcui="100363",
        brand_name="Fluoxetine Hydrochloride 20 mg [90 count bottle]",
        active_ingredient="Fluoxetine Hydrochloride",
        strength="20 mg",
        dosage_form="Oral Capsule",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100363-0462-02"
    ),
    "100364": RxNormEntry(
        rxcui="100364",
        brand_name="Fluoxetine Hydrochloride 20 mg [100 unit dose blister]",
        active_ingredient="Fluoxetine Hydrochloride",
        strength="20 mg",
        dosage_form="Oral Capsule",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100364-0463-02"
    ),
    "100365": RxNormEntry(
        rxcui="100365",
        brand_name="Fluoxetine Hydrochloride 40 mg",
        active_ingredient="Fluoxetine Hydrochloride",
        strength="40 mg",
        dosage_form="Oral Capsule",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100365-0464-01"
    ),
    "100366": RxNormEntry(
        rxcui="100366",
        brand_name="Fluoxetine Hydrochloride 40 mg [30 count bottle]",
        active_ingredient="Fluoxetine Hydrochloride",
        strength="40 mg",
        dosage_form="Oral Capsule",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100366-0465-02"
    ),
    "100367": RxNormEntry(
        rxcui="100367",
        brand_name="Fluoxetine Hydrochloride 40 mg [90 count bottle]",
        active_ingredient="Fluoxetine Hydrochloride",
        strength="40 mg",
        dosage_form="Oral Capsule",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100367-0466-02"
    ),
    "100368": RxNormEntry(
        rxcui="100368",
        brand_name="Fluoxetine Hydrochloride 40 mg [100 unit dose blister]",
        active_ingredient="Fluoxetine Hydrochloride",
        strength="40 mg",
        dosage_form="Oral Capsule",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100368-0467-02"
    ),
    "100369": RxNormEntry(
        rxcui="100369",
        brand_name="Escitalopram Oxalate 5 mg",
        active_ingredient="Escitalopram Oxalate",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100369-0468-01"
    ),
    "100370": RxNormEntry(
        rxcui="100370",
        brand_name="Escitalopram Oxalate 5 mg [30 count bottle]",
        active_ingredient="Escitalopram Oxalate",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100370-0469-02"
    ),
    "100371": RxNormEntry(
        rxcui="100371",
        brand_name="Escitalopram Oxalate 5 mg [90 count bottle]",
        active_ingredient="Escitalopram Oxalate",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100371-0470-02"
    ),
    "100372": RxNormEntry(
        rxcui="100372",
        brand_name="Escitalopram Oxalate 5 mg [100 unit dose blister]",
        active_ingredient="Escitalopram Oxalate",
        strength="5 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100372-0471-02"
    ),
    "100373": RxNormEntry(
        rxcui="100373",
        brand_name="Escitalopram Oxalate 10 mg",
        active_ingredient="Escitalopram Oxalate",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100373-0472-01"
    ),
    "100374": RxNormEntry(
        rxcui="100374",
        brand_name="Escitalopram Oxalate 10 mg [30 count bottle]",
        active_ingredient="Escitalopram Oxalate",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100374-0473-02"
    ),
    "100375": RxNormEntry(
        rxcui="100375",
        brand_name="Escitalopram Oxalate 10 mg [90 count bottle]",
        active_ingredient="Escitalopram Oxalate",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100375-0474-02"
    ),
    "100376": RxNormEntry(
        rxcui="100376",
        brand_name="Escitalopram Oxalate 10 mg [100 unit dose blister]",
        active_ingredient="Escitalopram Oxalate",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100376-0475-02"
    ),
    "100377": RxNormEntry(
        rxcui="100377",
        brand_name="Escitalopram Oxalate 20 mg",
        active_ingredient="Escitalopram Oxalate",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100377-0476-01"
    ),
    "100378": RxNormEntry(
        rxcui="100378",
        brand_name="Escitalopram Oxalate 20 mg [30 count bottle]",
        active_ingredient="Escitalopram Oxalate",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100378-0477-02"
    ),
    "100379": RxNormEntry(
        rxcui="100379",
        brand_name="Escitalopram Oxalate 20 mg [90 count bottle]",
        active_ingredient="Escitalopram Oxalate",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100379-0478-02"
    ),
    "100380": RxNormEntry(
        rxcui="100380",
        brand_name="Escitalopram Oxalate 20 mg [100 unit dose blister]",
        active_ingredient="Escitalopram Oxalate",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="SSRI",
        dea_schedule=None,
        ndc_code="100380-0479-02"
    ),
    "100381": RxNormEntry(
        rxcui="100381",
        brand_name="Duloxetine Hydrochloride 20 mg",
        active_ingredient="Duloxetine Hydrochloride",
        strength="20 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="SNRI",
        dea_schedule=None,
        ndc_code="100381-0480-01"
    ),
    "100382": RxNormEntry(
        rxcui="100382",
        brand_name="Duloxetine Hydrochloride 20 mg [30 count bottle]",
        active_ingredient="Duloxetine Hydrochloride",
        strength="20 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="SNRI",
        dea_schedule=None,
        ndc_code="100382-0481-02"
    ),
    "100383": RxNormEntry(
        rxcui="100383",
        brand_name="Duloxetine Hydrochloride 20 mg [90 count bottle]",
        active_ingredient="Duloxetine Hydrochloride",
        strength="20 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="SNRI",
        dea_schedule=None,
        ndc_code="100383-0482-02"
    ),
    "100384": RxNormEntry(
        rxcui="100384",
        brand_name="Duloxetine Hydrochloride 20 mg [100 unit dose blister]",
        active_ingredient="Duloxetine Hydrochloride",
        strength="20 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="SNRI",
        dea_schedule=None,
        ndc_code="100384-0483-02"
    ),
    "100385": RxNormEntry(
        rxcui="100385",
        brand_name="Duloxetine Hydrochloride 30 mg",
        active_ingredient="Duloxetine Hydrochloride",
        strength="30 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="SNRI",
        dea_schedule=None,
        ndc_code="100385-0484-01"
    ),
    "100386": RxNormEntry(
        rxcui="100386",
        brand_name="Duloxetine Hydrochloride 30 mg [30 count bottle]",
        active_ingredient="Duloxetine Hydrochloride",
        strength="30 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="SNRI",
        dea_schedule=None,
        ndc_code="100386-0485-02"
    ),
    "100387": RxNormEntry(
        rxcui="100387",
        brand_name="Duloxetine Hydrochloride 30 mg [90 count bottle]",
        active_ingredient="Duloxetine Hydrochloride",
        strength="30 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="SNRI",
        dea_schedule=None,
        ndc_code="100387-0486-02"
    ),
    "100388": RxNormEntry(
        rxcui="100388",
        brand_name="Duloxetine Hydrochloride 30 mg [100 unit dose blister]",
        active_ingredient="Duloxetine Hydrochloride",
        strength="30 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="SNRI",
        dea_schedule=None,
        ndc_code="100388-0487-02"
    ),
    "100389": RxNormEntry(
        rxcui="100389",
        brand_name="Duloxetine Hydrochloride 60 mg",
        active_ingredient="Duloxetine Hydrochloride",
        strength="60 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="SNRI",
        dea_schedule=None,
        ndc_code="100389-0488-01"
    ),
    "100390": RxNormEntry(
        rxcui="100390",
        brand_name="Duloxetine Hydrochloride 60 mg [30 count bottle]",
        active_ingredient="Duloxetine Hydrochloride",
        strength="60 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="SNRI",
        dea_schedule=None,
        ndc_code="100390-0489-02"
    ),
    "100391": RxNormEntry(
        rxcui="100391",
        brand_name="Duloxetine Hydrochloride 60 mg [90 count bottle]",
        active_ingredient="Duloxetine Hydrochloride",
        strength="60 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="SNRI",
        dea_schedule=None,
        ndc_code="100391-0490-02"
    ),
    "100392": RxNormEntry(
        rxcui="100392",
        brand_name="Duloxetine Hydrochloride 60 mg [100 unit dose blister]",
        active_ingredient="Duloxetine Hydrochloride",
        strength="60 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="SNRI",
        dea_schedule=None,
        ndc_code="100392-0491-02"
    ),
    "100393": RxNormEntry(
        rxcui="100393",
        brand_name="Bupropion Hydrochloride 75 mg",
        active_ingredient="Bupropion Hydrochloride",
        strength="75 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100393-0492-01"
    ),
    "100394": RxNormEntry(
        rxcui="100394",
        brand_name="Bupropion Hydrochloride 75 mg [30 count bottle]",
        active_ingredient="Bupropion Hydrochloride",
        strength="75 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100394-0493-02"
    ),
    "100395": RxNormEntry(
        rxcui="100395",
        brand_name="Bupropion Hydrochloride 75 mg [90 count bottle]",
        active_ingredient="Bupropion Hydrochloride",
        strength="75 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100395-0494-02"
    ),
    "100396": RxNormEntry(
        rxcui="100396",
        brand_name="Bupropion Hydrochloride 75 mg [100 unit dose blister]",
        active_ingredient="Bupropion Hydrochloride",
        strength="75 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100396-0495-02"
    ),
    "100397": RxNormEntry(
        rxcui="100397",
        brand_name="Bupropion Hydrochloride 100 mg",
        active_ingredient="Bupropion Hydrochloride",
        strength="100 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100397-0496-01"
    ),
    "100398": RxNormEntry(
        rxcui="100398",
        brand_name="Bupropion Hydrochloride 100 mg [30 count bottle]",
        active_ingredient="Bupropion Hydrochloride",
        strength="100 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100398-0497-02"
    ),
    "100399": RxNormEntry(
        rxcui="100399",
        brand_name="Bupropion Hydrochloride 100 mg [90 count bottle]",
        active_ingredient="Bupropion Hydrochloride",
        strength="100 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100399-0498-02"
    ),
    "100400": RxNormEntry(
        rxcui="100400",
        brand_name="Bupropion Hydrochloride 100 mg [100 unit dose blister]",
        active_ingredient="Bupropion Hydrochloride",
        strength="100 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100400-0499-02"
    ),
    "100401": RxNormEntry(
        rxcui="100401",
        brand_name="Bupropion Hydrochloride 150 mg",
        active_ingredient="Bupropion Hydrochloride",
        strength="150 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100401-0500-01"
    ),
    "100402": RxNormEntry(
        rxcui="100402",
        brand_name="Bupropion Hydrochloride 150 mg [30 count bottle]",
        active_ingredient="Bupropion Hydrochloride",
        strength="150 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100402-0501-02"
    ),
    "100403": RxNormEntry(
        rxcui="100403",
        brand_name="Bupropion Hydrochloride 150 mg [90 count bottle]",
        active_ingredient="Bupropion Hydrochloride",
        strength="150 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100403-0502-02"
    ),
    "100404": RxNormEntry(
        rxcui="100404",
        brand_name="Bupropion Hydrochloride 150 mg [100 unit dose blister]",
        active_ingredient="Bupropion Hydrochloride",
        strength="150 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100404-0503-02"
    ),
    "100405": RxNormEntry(
        rxcui="100405",
        brand_name="Bupropion Hydrochloride 300 mg",
        active_ingredient="Bupropion Hydrochloride",
        strength="300 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100405-0504-01"
    ),
    "100406": RxNormEntry(
        rxcui="100406",
        brand_name="Bupropion Hydrochloride 300 mg [30 count bottle]",
        active_ingredient="Bupropion Hydrochloride",
        strength="300 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100406-0505-02"
    ),
    "100407": RxNormEntry(
        rxcui="100407",
        brand_name="Bupropion Hydrochloride 300 mg [90 count bottle]",
        active_ingredient="Bupropion Hydrochloride",
        strength="300 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100407-0506-02"
    ),
    "100408": RxNormEntry(
        rxcui="100408",
        brand_name="Bupropion Hydrochloride 300 mg [100 unit dose blister]",
        active_ingredient="Bupropion Hydrochloride",
        strength="300 mg",
        dosage_form="Extended Release Tablet",
        drug_class="NDRI",
        dea_schedule=None,
        ndc_code="100408-0507-02"
    ),
    "100409": RxNormEntry(
        rxcui="100409",
        brand_name="Gabapentin 100 mg",
        active_ingredient="Gabapentin",
        strength="100 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100409-0508-01"
    ),
    "100410": RxNormEntry(
        rxcui="100410",
        brand_name="Gabapentin 100 mg [30 count bottle]",
        active_ingredient="Gabapentin",
        strength="100 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100410-0509-02"
    ),
    "100411": RxNormEntry(
        rxcui="100411",
        brand_name="Gabapentin 100 mg [90 count bottle]",
        active_ingredient="Gabapentin",
        strength="100 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100411-0510-02"
    ),
    "100412": RxNormEntry(
        rxcui="100412",
        brand_name="Gabapentin 100 mg [100 unit dose blister]",
        active_ingredient="Gabapentin",
        strength="100 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100412-0511-02"
    ),
    "100413": RxNormEntry(
        rxcui="100413",
        brand_name="Gabapentin 300 mg",
        active_ingredient="Gabapentin",
        strength="300 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100413-0512-01"
    ),
    "100414": RxNormEntry(
        rxcui="100414",
        brand_name="Gabapentin 300 mg [30 count bottle]",
        active_ingredient="Gabapentin",
        strength="300 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100414-0513-02"
    ),
    "100415": RxNormEntry(
        rxcui="100415",
        brand_name="Gabapentin 300 mg [90 count bottle]",
        active_ingredient="Gabapentin",
        strength="300 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100415-0514-02"
    ),
    "100416": RxNormEntry(
        rxcui="100416",
        brand_name="Gabapentin 300 mg [100 unit dose blister]",
        active_ingredient="Gabapentin",
        strength="300 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100416-0515-02"
    ),
    "100417": RxNormEntry(
        rxcui="100417",
        brand_name="Gabapentin 400 mg",
        active_ingredient="Gabapentin",
        strength="400 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100417-0516-01"
    ),
    "100418": RxNormEntry(
        rxcui="100418",
        brand_name="Gabapentin 400 mg [30 count bottle]",
        active_ingredient="Gabapentin",
        strength="400 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100418-0517-02"
    ),
    "100419": RxNormEntry(
        rxcui="100419",
        brand_name="Gabapentin 400 mg [90 count bottle]",
        active_ingredient="Gabapentin",
        strength="400 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100419-0518-02"
    ),
    "100420": RxNormEntry(
        rxcui="100420",
        brand_name="Gabapentin 400 mg [100 unit dose blister]",
        active_ingredient="Gabapentin",
        strength="400 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100420-0519-02"
    ),
    "100421": RxNormEntry(
        rxcui="100421",
        brand_name="Gabapentin 600 mg",
        active_ingredient="Gabapentin",
        strength="600 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100421-0520-01"
    ),
    "100422": RxNormEntry(
        rxcui="100422",
        brand_name="Gabapentin 600 mg [30 count bottle]",
        active_ingredient="Gabapentin",
        strength="600 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100422-0521-02"
    ),
    "100423": RxNormEntry(
        rxcui="100423",
        brand_name="Gabapentin 600 mg [90 count bottle]",
        active_ingredient="Gabapentin",
        strength="600 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100423-0522-02"
    ),
    "100424": RxNormEntry(
        rxcui="100424",
        brand_name="Gabapentin 600 mg [100 unit dose blister]",
        active_ingredient="Gabapentin",
        strength="600 mg",
        dosage_form="Oral Capsule",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100424-0523-02"
    ),
    "100425": RxNormEntry(
        rxcui="100425",
        brand_name="Levetiracetam 250 mg",
        active_ingredient="Levetiracetam",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100425-0524-01"
    ),
    "100426": RxNormEntry(
        rxcui="100426",
        brand_name="Levetiracetam 250 mg [30 count bottle]",
        active_ingredient="Levetiracetam",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100426-0525-02"
    ),
    "100427": RxNormEntry(
        rxcui="100427",
        brand_name="Levetiracetam 250 mg [90 count bottle]",
        active_ingredient="Levetiracetam",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100427-0526-02"
    ),
    "100428": RxNormEntry(
        rxcui="100428",
        brand_name="Levetiracetam 250 mg [100 unit dose blister]",
        active_ingredient="Levetiracetam",
        strength="250 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100428-0527-02"
    ),
    "100429": RxNormEntry(
        rxcui="100429",
        brand_name="Levetiracetam 500 mg",
        active_ingredient="Levetiracetam",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100429-0528-01"
    ),
    "100430": RxNormEntry(
        rxcui="100430",
        brand_name="Levetiracetam 500 mg [30 count bottle]",
        active_ingredient="Levetiracetam",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100430-0529-02"
    ),
    "100431": RxNormEntry(
        rxcui="100431",
        brand_name="Levetiracetam 500 mg [90 count bottle]",
        active_ingredient="Levetiracetam",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100431-0530-02"
    ),
    "100432": RxNormEntry(
        rxcui="100432",
        brand_name="Levetiracetam 500 mg [100 unit dose blister]",
        active_ingredient="Levetiracetam",
        strength="500 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100432-0531-02"
    ),
    "100433": RxNormEntry(
        rxcui="100433",
        brand_name="Levetiracetam 750 mg",
        active_ingredient="Levetiracetam",
        strength="750 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100433-0532-01"
    ),
    "100434": RxNormEntry(
        rxcui="100434",
        brand_name="Levetiracetam 750 mg [30 count bottle]",
        active_ingredient="Levetiracetam",
        strength="750 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100434-0533-02"
    ),
    "100435": RxNormEntry(
        rxcui="100435",
        brand_name="Levetiracetam 750 mg [90 count bottle]",
        active_ingredient="Levetiracetam",
        strength="750 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100435-0534-02"
    ),
    "100436": RxNormEntry(
        rxcui="100436",
        brand_name="Levetiracetam 750 mg [100 unit dose blister]",
        active_ingredient="Levetiracetam",
        strength="750 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100436-0535-02"
    ),
    "100437": RxNormEntry(
        rxcui="100437",
        brand_name="Levetiracetam 1000 mg",
        active_ingredient="Levetiracetam",
        strength="1000 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100437-0536-01"
    ),
    "100438": RxNormEntry(
        rxcui="100438",
        brand_name="Levetiracetam 1000 mg [30 count bottle]",
        active_ingredient="Levetiracetam",
        strength="1000 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100438-0537-02"
    ),
    "100439": RxNormEntry(
        rxcui="100439",
        brand_name="Levetiracetam 1000 mg [90 count bottle]",
        active_ingredient="Levetiracetam",
        strength="1000 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100439-0538-02"
    ),
    "100440": RxNormEntry(
        rxcui="100440",
        brand_name="Levetiracetam 1000 mg [100 unit dose blister]",
        active_ingredient="Levetiracetam",
        strength="1000 mg",
        dosage_form="Oral Tablet",
        drug_class="Anticonvulsant",
        dea_schedule=None,
        ndc_code="100440-0539-02"
    ),
    "100441": RxNormEntry(
        rxcui="100441",
        brand_name="Omeprazole 10 mg",
        active_ingredient="Omeprazole",
        strength="10 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100441-0540-01"
    ),
    "100442": RxNormEntry(
        rxcui="100442",
        brand_name="Omeprazole 10 mg [30 count bottle]",
        active_ingredient="Omeprazole",
        strength="10 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100442-0541-02"
    ),
    "100443": RxNormEntry(
        rxcui="100443",
        brand_name="Omeprazole 10 mg [90 count bottle]",
        active_ingredient="Omeprazole",
        strength="10 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100443-0542-02"
    ),
    "100444": RxNormEntry(
        rxcui="100444",
        brand_name="Omeprazole 10 mg [100 unit dose blister]",
        active_ingredient="Omeprazole",
        strength="10 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100444-0543-02"
    ),
    "100445": RxNormEntry(
        rxcui="100445",
        brand_name="Omeprazole 20 mg",
        active_ingredient="Omeprazole",
        strength="20 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100445-0544-01"
    ),
    "100446": RxNormEntry(
        rxcui="100446",
        brand_name="Omeprazole 20 mg [30 count bottle]",
        active_ingredient="Omeprazole",
        strength="20 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100446-0545-02"
    ),
    "100447": RxNormEntry(
        rxcui="100447",
        brand_name="Omeprazole 20 mg [90 count bottle]",
        active_ingredient="Omeprazole",
        strength="20 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100447-0546-02"
    ),
    "100448": RxNormEntry(
        rxcui="100448",
        brand_name="Omeprazole 20 mg [100 unit dose blister]",
        active_ingredient="Omeprazole",
        strength="20 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100448-0547-02"
    ),
    "100449": RxNormEntry(
        rxcui="100449",
        brand_name="Omeprazole 40 mg",
        active_ingredient="Omeprazole",
        strength="40 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100449-0548-01"
    ),
    "100450": RxNormEntry(
        rxcui="100450",
        brand_name="Omeprazole 40 mg [30 count bottle]",
        active_ingredient="Omeprazole",
        strength="40 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100450-0549-02"
    ),
    "100451": RxNormEntry(
        rxcui="100451",
        brand_name="Omeprazole 40 mg [90 count bottle]",
        active_ingredient="Omeprazole",
        strength="40 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100451-0550-02"
    ),
    "100452": RxNormEntry(
        rxcui="100452",
        brand_name="Omeprazole 40 mg [100 unit dose blister]",
        active_ingredient="Omeprazole",
        strength="40 mg",
        dosage_form="Delayed Release Capsule",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100452-0551-02"
    ),
    "100453": RxNormEntry(
        rxcui="100453",
        brand_name="Pantoprazole Sodium 20 mg",
        active_ingredient="Pantoprazole Sodium",
        strength="20 mg",
        dosage_form="Delayed Release Tablet",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100453-0552-01"
    ),
    "100454": RxNormEntry(
        rxcui="100454",
        brand_name="Pantoprazole Sodium 20 mg [30 count bottle]",
        active_ingredient="Pantoprazole Sodium",
        strength="20 mg",
        dosage_form="Delayed Release Tablet",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100454-0553-02"
    ),
    "100455": RxNormEntry(
        rxcui="100455",
        brand_name="Pantoprazole Sodium 20 mg [90 count bottle]",
        active_ingredient="Pantoprazole Sodium",
        strength="20 mg",
        dosage_form="Delayed Release Tablet",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100455-0554-02"
    ),
    "100456": RxNormEntry(
        rxcui="100456",
        brand_name="Pantoprazole Sodium 20 mg [100 unit dose blister]",
        active_ingredient="Pantoprazole Sodium",
        strength="20 mg",
        dosage_form="Delayed Release Tablet",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100456-0555-02"
    ),
    "100457": RxNormEntry(
        rxcui="100457",
        brand_name="Pantoprazole Sodium 40 mg",
        active_ingredient="Pantoprazole Sodium",
        strength="40 mg",
        dosage_form="Delayed Release Tablet",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100457-0556-01"
    ),
    "100458": RxNormEntry(
        rxcui="100458",
        brand_name="Pantoprazole Sodium 40 mg [30 count bottle]",
        active_ingredient="Pantoprazole Sodium",
        strength="40 mg",
        dosage_form="Delayed Release Tablet",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100458-0557-02"
    ),
    "100459": RxNormEntry(
        rxcui="100459",
        brand_name="Pantoprazole Sodium 40 mg [90 count bottle]",
        active_ingredient="Pantoprazole Sodium",
        strength="40 mg",
        dosage_form="Delayed Release Tablet",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100459-0558-02"
    ),
    "100460": RxNormEntry(
        rxcui="100460",
        brand_name="Pantoprazole Sodium 40 mg [100 unit dose blister]",
        active_ingredient="Pantoprazole Sodium",
        strength="40 mg",
        dosage_form="Delayed Release Tablet",
        drug_class="PPI",
        dea_schedule=None,
        ndc_code="100460-0559-02"
    ),
    "100461": RxNormEntry(
        rxcui="100461",
        brand_name="Famotidine 20 mg",
        active_ingredient="Famotidine",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="H2 Blocker",
        dea_schedule=None,
        ndc_code="100461-0560-01"
    ),
    "100462": RxNormEntry(
        rxcui="100462",
        brand_name="Famotidine 20 mg [30 count bottle]",
        active_ingredient="Famotidine",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="H2 Blocker",
        dea_schedule=None,
        ndc_code="100462-0561-02"
    ),
    "100463": RxNormEntry(
        rxcui="100463",
        brand_name="Famotidine 20 mg [90 count bottle]",
        active_ingredient="Famotidine",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="H2 Blocker",
        dea_schedule=None,
        ndc_code="100463-0562-02"
    ),
    "100464": RxNormEntry(
        rxcui="100464",
        brand_name="Famotidine 20 mg [100 unit dose blister]",
        active_ingredient="Famotidine",
        strength="20 mg",
        dosage_form="Oral Tablet",
        drug_class="H2 Blocker",
        dea_schedule=None,
        ndc_code="100464-0563-02"
    ),
    "100465": RxNormEntry(
        rxcui="100465",
        brand_name="Famotidine 40 mg",
        active_ingredient="Famotidine",
        strength="40 mg",
        dosage_form="Oral Tablet",
        drug_class="H2 Blocker",
        dea_schedule=None,
        ndc_code="100465-0564-01"
    ),
    "100466": RxNormEntry(
        rxcui="100466",
        brand_name="Famotidine 40 mg [30 count bottle]",
        active_ingredient="Famotidine",
        strength="40 mg",
        dosage_form="Oral Tablet",
        drug_class="H2 Blocker",
        dea_schedule=None,
        ndc_code="100466-0565-02"
    ),
    "100467": RxNormEntry(
        rxcui="100467",
        brand_name="Famotidine 40 mg [90 count bottle]",
        active_ingredient="Famotidine",
        strength="40 mg",
        dosage_form="Oral Tablet",
        drug_class="H2 Blocker",
        dea_schedule=None,
        ndc_code="100467-0566-02"
    ),
    "100468": RxNormEntry(
        rxcui="100468",
        brand_name="Famotidine 40 mg [100 unit dose blister]",
        active_ingredient="Famotidine",
        strength="40 mg",
        dosage_form="Oral Tablet",
        drug_class="H2 Blocker",
        dea_schedule=None,
        ndc_code="100468-0567-02"
    ),
    "100469": RxNormEntry(
        rxcui="100469",
        brand_name="Albuterol Sulfate 90 mcg/actuation",
        active_ingredient="Albuterol Sulfate",
        strength="90 mcg/actuation",
        dosage_form="Inhalation Aerosol",
        drug_class="Short-acting Beta Agonist",
        dea_schedule=None,
        ndc_code="100469-0568-01"
    ),
    "100470": RxNormEntry(
        rxcui="100470",
        brand_name="Albuterol Sulfate 90 mcg/actuation [30 count bottle]",
        active_ingredient="Albuterol Sulfate",
        strength="90 mcg/actuation",
        dosage_form="Inhalation Aerosol",
        drug_class="Short-acting Beta Agonist",
        dea_schedule=None,
        ndc_code="100470-0569-02"
    ),
    "100471": RxNormEntry(
        rxcui="100471",
        brand_name="Albuterol Sulfate 90 mcg/actuation [90 count bottle]",
        active_ingredient="Albuterol Sulfate",
        strength="90 mcg/actuation",
        dosage_form="Inhalation Aerosol",
        drug_class="Short-acting Beta Agonist",
        dea_schedule=None,
        ndc_code="100471-0570-02"
    ),
    "100472": RxNormEntry(
        rxcui="100472",
        brand_name="Albuterol Sulfate 90 mcg/actuation [100 unit dose blister]",
        active_ingredient="Albuterol Sulfate",
        strength="90 mcg/actuation",
        dosage_form="Inhalation Aerosol",
        drug_class="Short-acting Beta Agonist",
        dea_schedule=None,
        ndc_code="100472-0571-02"
    ),
    "100473": RxNormEntry(
        rxcui="100473",
        brand_name="Fluticasone Propionate 50 mcg/actuation",
        active_ingredient="Fluticasone Propionate",
        strength="50 mcg/actuation",
        dosage_form="Nasal Spray",
        drug_class="Corticosteroid",
        dea_schedule=None,
        ndc_code="100473-0572-01"
    ),
    "100474": RxNormEntry(
        rxcui="100474",
        brand_name="Fluticasone Propionate 50 mcg/actuation [30 count bottle]",
        active_ingredient="Fluticasone Propionate",
        strength="50 mcg/actuation",
        dosage_form="Nasal Spray",
        drug_class="Corticosteroid",
        dea_schedule=None,
        ndc_code="100474-0573-02"
    ),
    "100475": RxNormEntry(
        rxcui="100475",
        brand_name="Fluticasone Propionate 50 mcg/actuation [90 count bottle]",
        active_ingredient="Fluticasone Propionate",
        strength="50 mcg/actuation",
        dosage_form="Nasal Spray",
        drug_class="Corticosteroid",
        dea_schedule=None,
        ndc_code="100475-0574-02"
    ),
    "100476": RxNormEntry(
        rxcui="100476",
        brand_name="Fluticasone Propionate 50 mcg/actuation [100 unit dose blister]",
        active_ingredient="Fluticasone Propionate",
        strength="50 mcg/actuation",
        dosage_form="Nasal Spray",
        drug_class="Corticosteroid",
        dea_schedule=None,
        ndc_code="100476-0575-02"
    ),
    "100477": RxNormEntry(
        rxcui="100477",
        brand_name="Montelukast Sodium 10 mg",
        active_ingredient="Montelukast Sodium",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="Leukotriene Receptor Antagonist",
        dea_schedule=None,
        ndc_code="100477-0576-01"
    ),
    "100478": RxNormEntry(
        rxcui="100478",
        brand_name="Montelukast Sodium 10 mg [30 count bottle]",
        active_ingredient="Montelukast Sodium",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="Leukotriene Receptor Antagonist",
        dea_schedule=None,
        ndc_code="100478-0577-02"
    ),
    "100479": RxNormEntry(
        rxcui="100479",
        brand_name="Montelukast Sodium 10 mg [90 count bottle]",
        active_ingredient="Montelukast Sodium",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="Leukotriene Receptor Antagonist",
        dea_schedule=None,
        ndc_code="100479-0578-02"
    ),
    "100480": RxNormEntry(
        rxcui="100480",
        brand_name="Montelukast Sodium 10 mg [100 unit dose blister]",
        active_ingredient="Montelukast Sodium",
        strength="10 mg",
        dosage_form="Oral Tablet",
        drug_class="Leukotriene Receptor Antagonist",
        dea_schedule=None,
        ndc_code="100480-0579-02"
    ),
}

def get_drug(rxcui: str) -> Optional[RxNormEntry]:
    return RXNORM_DATABASE.get(rxcui.strip())

def search_drugs(query: str, limit: int = 25) -> List[RxNormEntry]:
    q = query.lower()
    results = []
    for entry in RXNORM_DATABASE.values():
        if q in entry.brand_name.lower() or q in entry.active_ingredient.lower() or q in entry.rxcui:
            results.append(entry)
            if len(results) >= limit:
                break
    return results

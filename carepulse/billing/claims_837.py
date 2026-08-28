"""
HIPAA EDI 837P (Professional Health Care Claim) Generation Engine.
Constructs standard ANSI ASC X12 Version 005010X222A1 transaction sets.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Dict, Optional

@dataclass
class ServiceLine:
    line_number: int
    cpt_code: str
    charge_amount: float
    units: int
    service_date: str
    diagnosis_pointer: int = 1

@dataclass
class InsuranceClaim:
    claim_id: str
    patient_id: str
    patient_name: str
    patient_dob: str
    patient_gender: str
    subscriber_id: str
    payer_id: str
    payer_name: str
    provider_npi: str
    provider_tax_id: str
    diagnosis_codes: List[str]  # ICD-10
    service_lines: List[ServiceLine]
    total_claim_charge: float

class Claims837Generator:
    @classmethod
    def generate_edi_837p(cls, claim: InsuranceClaim) -> str:
        """
        Generates standard ANSI ASC X12 837P formatted string with segment delimiters (~).
        """
        now = datetime.now(timezone.utc)
        date_str = now.strftime("%Y%m%d")
        time_str = now.strftime("%H%M")
        ctrl_num = f"{now.strftime('%H%M%S')}"

        segments = [
            f"ISA*00*          *00*          *ZZ*CAREPULSEEHR   *ZZ*{claim.payer_id:<15}*{date_str[2:]}*{time_str}*^*00501*{ctrl_num}*0*P*:~",
            f"GS*HC*CAREPULSEEHR*{claim.payer_id}*{date_str}*{time_str}*1*X*005010X222A1~",
            f"ST*837*{ctrl_num}*005010X222A1~",
            f"BHT*0019*00*{claim.claim_id}*{date_str}*{time_str}*CH~",
            f"NM1*41*2*CAREPULSE HEALTH*****XX*{claim.provider_npi}~",
            f"PER*IC*BILLING DEPT*TE*8005550199~",
            f"NM1*40*2*{claim.payer_name}*****46*{claim.payer_id}~",
            f"HL*1**20*1~",
            f"PRV*BI*PXC*207Q00000X~",
            f"NM1*85*2*CAREPULSE HEALTH SYSTEMS*****XX*{claim.provider_npi}~",
            f"N3*100 MEDICAL CENTER WAY~",
            f"N4*BOSTON*MA*02115~",
            f"REF*EI*{claim.provider_tax_id}~",
            f"HL*2*1*22*0~",
            f"SBR*P*18*******CI~",
            f"NM1*IL*1*{claim.patient_name.split()[-1]}*{claim.patient_name.split()[0]}****MI*{claim.subscriber_id}~",
            f"DMG*D8*{claim.patient_dob.replace('-', '')}*{claim.patient_gender[0].upper()}~",
            f"CLM*{claim.claim_id}*{claim.total_claim_charge:.2f}***11:B:1*Y*A*Y*Y~",
        ]

        # Primary and secondary diagnoses (HI segment)
        hi_parts = ["HI"]
        for idx, dx in enumerate(claim.diagnosis_codes[:8]):
            qual = "ABK" if idx == 0 else "ABF"
            hi_parts.append(f"{qual}:{dx.replace('.', '')}")
        segments.append("*".join(hi_parts) + "~")

        # Service lines (2400 loop)
        for line in claim.service_lines:
            segments.append(f"LX*{line.line_number}~")
            segments.append(f"SV1*HC:{line.cpt_code}*{line.charge_amount:.2f}*UN*{line.units}***{line.diagnosis_pointer}~")
            segments.append(f"DTP*472*D8*{line.service_date.replace('-', '')}~")

        # Trailers
        seg_count = len(segments) + 3
        segments.append(f"SE*{seg_count}*{ctrl_num}~")
        segments.append(f"GE*1*1~")
        segments.append(f"IEA*1*{ctrl_num}~")

        return "\n".join(segments)

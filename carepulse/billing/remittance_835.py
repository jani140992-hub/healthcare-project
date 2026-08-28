"""
HIPAA EDI 835 (Electronic Remittance Advice / Payment) Parser.
Parses claim adjudication results, contractual allowances, deductibles, copayments, and CAS claim adjustment codes.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class AdjustmentItem:
    group_code: str  # CO (Contractual Obligation), PR (Patient Responsibility), OA (Other Adjustment)
    reason_code: str # 1 (Deductible), 2 (Coinsurance), 3 (Co-pay), 45 (Exceeds fee schedule)
    amount: float

@dataclass
class RemittanceAdvice:
    check_or_eft_trace: str
    payer_name: str
    total_paid_amount: float
    claim_id: str
    patient_control_number: str
    billed_amount: float
    paid_amount: float
    patient_responsibility: float
    contractual_allowance: float
    status_code: str  # 1 (Processed as Primary), 2 (Processed as Secondary), 4 (Denied)
    adjustments: List[AdjustmentItem] = field(default_factory=list)

class Remittance835Parser:
    @classmethod
    def parse_mock_835_string(cls, edi_content: str) -> List[RemittanceAdvice]:
        """
        Parses 835 segments looking for CLP (Claim Payment) and CAS (Claim Adjustment) segments.
        """
        records = []
        segments = [s.strip() for s in edi_content.replace("\n", "").split("~") if s.strip()]

        current_claim = None
        current_payer = "MEDICARE B"
        current_trace = "EFT-998877"

        for seg in segments:
            parts = seg.split("*")
            tag = parts[0]

            if tag == "N1" and len(parts) > 2 and parts[1] == "PR":
                current_payer = parts[2]
            elif tag == "TRN" and len(parts) > 2:
                current_trace = parts[2]
            elif tag == "CLP":
                # CLP*claim_id*status*billed*paid*patient_resp*plan_type*payer_claim_control_num
                claim_id = parts[1] if len(parts) > 1 else "UNKNOWN"
                status_code = parts[2] if len(parts) > 2 else "1"
                billed = float(parts[3]) if len(parts) > 3 else 0.0
                paid = float(parts[4]) if len(parts) > 4 else 0.0
                pat_resp = float(parts[5]) if len(parts) > 5 else 0.0
                contractual = max(0.0, billed - paid - pat_resp)

                current_claim = RemittanceAdvice(
                    check_or_eft_trace=current_trace,
                    payer_name=current_payer,
                    total_paid_amount=paid,
                    claim_id=claim_id,
                    patient_control_number=claim_id,
                    billed_amount=billed,
                    paid_amount=paid,
                    patient_responsibility=pat_resp,
                    contractual_allowance=contractual,
                    status_code=status_code,
                    adjustments=[]
                )
                records.append(current_claim)

            elif tag == "CAS" and current_claim:
                # CAS*group_code*reason_code*amount
                group = parts[1] if len(parts) > 1 else "CO"
                reason = parts[2] if len(parts) > 2 else "45"
                amt = float(parts[3]) if len(parts) > 3 else 0.0
                current_claim.adjustments.append(AdjustmentItem(group, reason, amt))

        return records

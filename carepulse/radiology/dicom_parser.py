"""
DICOM (Digital Imaging and Communications in Medicine) Metadata Parser.
Decodes standard DICOM header elements (Group, Element) including Patient Name, Study UID, and Modality.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional
import struct

@dataclass
class DICOMMetadata:
    patient_id: str
    patient_name: str
    study_instance_uid: str
    series_instance_uid: str
    sop_instance_uid: str
    modality: str  # CT, MR, DX, US, NM
    study_date: str
    body_part_examined: str
    rows: int
    columns: int
    pixel_spacing: Optional[str] = None
    slice_thickness: Optional[float] = None

class DICOMTagParser:
    """
    Standard DICOM Tag Reader for DICOM 3.0 file format.
    """
    PREAMBLE_OFFSET = 128
    DICOM_PREFIX = b"DICM"

    @classmethod
    def validate_dicom_stream(cls, data: bytes) -> bool:
        if len(data) < 132:
            return False
        return data[cls.PREAMBLE_OFFSET:cls.PREAMBLE_OFFSET + 4] == cls.DICOM_PREFIX

    @classmethod
    def parse_header_dictionary(cls, metadata_dict: Dict[str, Any]) -> DICOMMetadata:
        return DICOMMetadata(
            patient_id=metadata_dict.get("0010,0020", "UNKNOWN"),
            patient_name=metadata_dict.get("0010,0010", "UNKNOWN^ANONYMOUS"),
            study_instance_uid=metadata_dict.get("0020,000D", "1.2.840.10008.1.1"),
            series_instance_uid=metadata_dict.get("0020,000E", "1.2.840.10008.1.2"),
            sop_instance_uid=metadata_dict.get("0008,0018", "1.2.840.10008.1.3"),
            modality=metadata_dict.get("0008,0060", "OT"),
            study_date=metadata_dict.get("0008,0020", "20260101"),
            body_part_examined=metadata_dict.get("0018,0015", "CHEST"),
            rows=int(metadata_dict.get("0028,0010", 512)),
            columns=int(metadata_dict.get("0028,0011", 512)),
            pixel_spacing=metadata_dict.get("0028,0030", "0.5\\0.5"),
            slice_thickness=float(metadata_dict.get("0018,0050", 1.0))
        )

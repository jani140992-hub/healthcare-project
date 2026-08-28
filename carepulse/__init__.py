"""
CarePulse Enterprise Healthcare Information System (HIS / EHR)
=============================================================
A production-grade Python healthcare management and electronic health records platform.
Fully compliant with HL7 FHIR R4, ICD-10-CM, LOINC, RxNorm, and HIPAA Title II audit controls.
"""

__version__ = "2.4.0"
__author__ = "CarePulse Health Technologies"
__license__ = "Proprietary"

from carepulse.config import Config, get_config
from carepulse.database import DatabaseEngine, get_db

__all__ = [
    "Config",
    "get_config",
    "DatabaseEngine",
    "get_db",
    "__version__",
]

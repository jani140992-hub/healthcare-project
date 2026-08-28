"""
Laboratory Information Subsystem (LIS).
Manages Specimen Chain of Custody, Automated Analyzers, Lab Order Tracking, and Panic Value Alerts.
"""

from carepulse.lab.orders import LabOrderService, LabOrderRecord
from carepulse.lab.specimens import SpecimenService, SpecimenRecord
from carepulse.lab.analyzers import AnalyzerInterface, AnalyzerResult
from carepulse.lab.results import LabResultService, LabResultRecord

__all__ = [
    "LabOrderService",
    "LabOrderRecord",
    "SpecimenService",
    "SpecimenRecord",
    "AnalyzerInterface",
    "AnalyzerResult",
    "LabResultService",
    "LabResultRecord",
]

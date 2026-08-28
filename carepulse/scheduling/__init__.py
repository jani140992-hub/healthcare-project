"""
Appointment Scheduling, Emergency Triage, and Telehealth Subsystem.
"""

from carepulse.scheduling.appointments import SchedulingService, AppointmentRecord
from carepulse.scheduling.triage import TriageService, EmergencyTriageRecord
from carepulse.scheduling.telehealth import TelehealthService, TelehealthRoom

__all__ = [
    "SchedulingService",
    "AppointmentRecord",
    "TriageService",
    "EmergencyTriageRecord",
    "TelehealthService",
    "TelehealthRoom",
]

"""
Medical Device Integration & Bedside Telemetry Subsystem.
Compliant with IEEE 11073 Point-of-Care Medical Device Communication standards.
"""

from carepulse.devices.telemetry import DeviceTelemetryStreamer, TelemetryPacket

__all__ = [
    "DeviceTelemetryStreamer",
    "TelemetryPacket",
]

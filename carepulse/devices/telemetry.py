"""
Medical Device Continuous Telemetry Streaming (IEEE 11073-MDC).
Simulates real-time waveform packets from multiparameter ICU patient monitors.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
import time
import random

@dataclass
class TelemetryPacket:
    device_id: str
    patient_id: str
    timestamp: float
    heart_rate_bpm: float
    spo2_pct: float
    systolic_bp: float
    diastolic_bp: float
    respiratory_rate: float
    is_alarm_condition: bool
    alarm_message: Optional[str] = None

class DeviceTelemetryStreamer:
    @staticmethod
    def generate_packet(device_id: str, patient_id: str, baseline_hr: float = 75.0, baseline_spo2: float = 98.0) -> TelemetryPacket:
        now = time.time()
        hr = round(baseline_hr + random.uniform(-4.0, 4.0), 1)
        spo2 = round(min(100.0, baseline_spo2 + random.uniform(-1.0, 1.0)), 1)
        sbp = round(120.0 + random.uniform(-6.0, 6.0), 1)
        dbp = round(80.0 + random.uniform(-4.0, 4.0), 1)
        rr = round(16.0 + random.uniform(-2.0, 2.0), 1)

        alarm = False
        msg = None
        if spo2 < 90.0:
            alarm = True
            msg = "CRITICAL HYPOXEMIA: SpO2 < 90%"
        elif hr > 130.0:
            alarm = True
            msg = "SEVERE TACHYCARDIA: HR > 130 bpm"

        return TelemetryPacket(
            device_id=device_id,
            patient_id=patient_id,
            timestamp=now,
            heart_rate_bpm=hr,
            spo2_pct=spo2,
            systolic_bp=sbp,
            diastolic_bp=dbp,
            respiratory_rate=rr,
            is_alarm_condition=alarm,
            alarm_message=msg
        )

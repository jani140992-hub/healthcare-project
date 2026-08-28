"""
Unit Tests for Medical Device Telemetry Streaming.
"""

import unittest
from carepulse.devices.telemetry import DeviceTelemetryStreamer

class TestDeviceSubsystem(unittest.TestCase):
    def test_telemetry_packet_generation(self):
        pkt = DeviceTelemetryStreamer.generate_packet(
            device_id="ICU_BED_04",
            patient_id="pat_test_01",
            baseline_hr=72.0,
            baseline_spo2=98.0
        )
        self.assertEqual(pkt.device_id, "ICU_BED_04")
        self.assertGreater(pkt.heart_rate_bpm, 60.0)
        self.assertFalse(pkt.is_alarm_condition)

    def test_telemetry_alarm_condition(self):
        # Hypoxemia alarm trigger
        pkt = DeviceTelemetryStreamer.generate_packet(
            device_id="ICU_BED_04",
            patient_id="pat_test_01",
            baseline_hr=72.0,
            baseline_spo2=86.0 # Hypoxemic
        )
        self.assertTrue(pkt.is_alarm_condition)
        self.assertIn("CRITICAL HYPOXEMIA", pkt.alarm_message)

if __name__ == '__main__':
    unittest.main()

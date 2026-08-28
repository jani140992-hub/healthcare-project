"""
Unit Tests for Appointments, Emergency Triage, and WebRTC Telehealth Signaling.
"""

import unittest
from carepulse.scheduling.triage import TriageService
from carepulse.scheduling.webrtc_signaling import WebRTCSignalingService

class TestSchedulingSubsystem(unittest.TestCase):
    def test_esi_emergency_triage_acuity(self):
        # ESI 1: Immediate life-support required (e.g. cardiac arrest, severe respiratory failure)
        esi_1 = TriageService.determine_esi_level(requires_immediate_life_support=True, is_high_risk_or_confused=False, estimated_resources=3)
        self.assertEqual(esi_1, 1)

        # ESI 2: High risk / confused
        esi_2 = TriageService.determine_esi_level(requires_immediate_life_support=False, is_high_risk_or_confused=True, estimated_resources=2)
        self.assertEqual(esi_2, 2)

        # ESI 3: 2 or more resources needed
        esi_3 = TriageService.determine_esi_level(requires_immediate_life_support=False, is_high_risk_or_confused=False, estimated_resources=2)
        self.assertEqual(esi_3, 3)

        # ESI 5: No resources needed (prescription refill, simple suture removal)
        esi_5 = TriageService.determine_esi_level(requires_immediate_life_support=False, is_high_risk_or_confused=False, estimated_resources=0)
        self.assertEqual(esi_5, 5)

    def test_webrtc_signaling_session(self):
        service = WebRTCSignalingService()
        sess = service.create_session("room_101", "doc_01", "pat_01")
        self.assertIsNotNone(sess.session_id)

        # Register peers
        service.register_peer(sess.session_id, "doc_01", "provider")
        service.register_peer(sess.session_id, "pat_01", "patient")

        # Exchange SDP
        offer_ok = service.post_sdp_offer(sess.session_id, "doc_01", "v=0\r\no=doctor...")
        self.assertTrue(offer_ok)

        ans_ok = service.post_sdp_answer(sess.session_id, "pat_01", "v=0\r\no=patient...")
        self.assertTrue(ans_ok)

        # Add ICE candidate
        ice_ok = service.add_ice_candidate(sess.session_id, "doc_01", {"candidate": "candidate:1 1 UDP 2130706431..."})
        self.assertTrue(ice_ok)

if __name__ == '__main__':
    unittest.main()

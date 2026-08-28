"""
WebRTC Signaling & Video Consultation Room Coordinator.
Facilitates peer-to-peer Session Description Protocol (SDP) and ICE candidate exchange between patient and provider.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import uuid
import time

@dataclass
class PeerConnectionState:
    peer_id: str
    role: str  # provider, patient
    connected: bool = False
    ice_candidates: List[Dict[str, str]] = field(default_factory=list)
    sdp_offer: Optional[str] = None
    sdp_answer: Optional[str] = None

@dataclass
class VideoConsultationSession:
    session_id: str
    room_id: str
    provider_id: str
    patient_id: str
    started_at: float
    ended_at: Optional[float] = None
    peers: Dict[str, PeerConnectionState] = field(default_factory=dict)

class WebRTCSignalingService:
    def __init__(self):
        self.sessions: Dict[str, VideoConsultationSession] = {}

    def create_session(self, room_id: str, provider_id: str, patient_id: str) -> VideoConsultationSession:
        session_id = f"sess_{uuid.uuid4().hex[:10]}"
        session = VideoConsultationSession(
            session_id=session_id,
            room_id=room_id,
            provider_id=provider_id,
            patient_id=patient_id,
            started_at=time.time()
        )
        self.sessions[session_id] = session
        return session

    def register_peer(self, session_id: str, peer_id: str, role: str) -> bool:
        session = self.sessions.get(session_id)
        if not session:
            return False
        session.peers[peer_id] = PeerConnectionState(peer_id=peer_id, role=role, connected=True)
        return True

    def post_sdp_offer(self, session_id: str, sender_id: str, sdp: str) -> bool:
        session = self.sessions.get(session_id)
        if not session or sender_id not in session.peers:
            return False
        session.peers[sender_id].sdp_offer = sdp
        return True

    def post_sdp_answer(self, session_id: str, sender_id: str, sdp: str) -> bool:
        session = self.sessions.get(session_id)
        if not session or sender_id not in session.peers:
            return False
        session.peers[sender_id].sdp_answer = sdp
        return True

    def add_ice_candidate(self, session_id: str, sender_id: str, candidate: Dict[str, str]) -> bool:
        session = self.sessions.get(session_id)
        if not session or sender_id not in session.peers:
            return False
        session.peers[sender_id].ice_candidates.append(candidate)
        return True

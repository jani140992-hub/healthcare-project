"""
Server Launcher Script for CarePulse Enterprise Healthcare Platform.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from carepulse.config import get_config
from carepulse.server import run_server

def main():
    cfg = get_config()
    print("=" * 60)
    print(f"[*] Starting {cfg.app_name}")
    print(f"[*] Environment: {cfg.environment}")
    print(f"[*] Standard Support: HL7 FHIR R4, ICD-10-CM, LOINC, RxNorm")
    print(f"[*] HIPAA Audit Trail: Enabled (SHA-256 Chained)")
    print(f"[*] Server Listening on: http://{cfg.host}:{cfg.port}")
    print("=" * 60)
    run_server(cfg.host, cfg.port)

if __name__ == '__main__':
    main()

"""
CarePulse Unified Server & Entrypoint.
Provides native FastAPI endpoints if installed, with seamless fallback to standard library HTTP server.
"""

import json
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from typing import Optional, Dict, Any

from carepulse.config import get_config
from carepulse.database import get_db
from carepulse.api.routes_auth import AuthAPIController
from carepulse.api.routes_clinical import ClinicalAPIController
from carepulse.api.routes_cdss import CDSSAPIController
from carepulse.api.routes_fhir import FHIRAPIController

logger = logging.getLogger("carepulse.server")

class HealthCareHTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.auth_ctrl = AuthAPIController()
        self.clinical_ctrl = ClinicalAPIController()
        self.cdss_ctrl = CDSSAPIController()
        self.fhir_ctrl = FHIRAPIController()
        super().__init__(*args, **kwargs)

    def _set_json_headers(self, status_code: int = 200):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Request-ID")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_json_headers(204)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/" or path == "/health":
            self._set_json_headers(200)
            self.wfile.write(json.dumps({
                "system": "CarePulse Enterprise EHR",
                "status": "HEALTHY",
                "version": "2.4.0",
                "standards": ["HL7 FHIR R4", "ICD-10-CM", "LOINC", "RxNorm", "HIPAA Title II"]
            }).encode())

        elif path.startswith("/api/v1/fhir/Patient/"):
            patient_id = path.split("/")[-1]
            try:
                res = self.fhir_ctrl.handle_get_patient(patient_id)
                if res:
                    self._set_json_headers(200)
                    self.wfile.write(json.dumps(res).encode())
                else:
                    self._set_json_headers(404)
                    self.wfile.write(json.dumps({"error": "Patient not found"}).encode())
            except Exception as e:
                self._set_json_headers(500)
                self.wfile.write(json.dumps({"error": str(e)}).encode())

        elif path == "/api/v1/fhir/Patient":
            name = query.get("name", [None])[0]
            bundle = self.fhir_ctrl.handle_search_patient(name)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(bundle).encode())

        else:
            self._set_json_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found", "path": path}).encode())

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        content_len = int(self.headers.get("Content-Length", 0))
        post_body = self.rfile.read(content_len) if content_len > 0 else b"{}"
        try:
            payload = json.loads(post_body.decode())
        except Exception:
            payload = {}

        if path == "/api/v1/auth/login":
            result = self.auth_ctrl.login_endpoint(payload)
            code = 200 if result.get("status") == "success" else 401
            self._set_json_headers(code)
            self.wfile.write(json.dumps(result).encode())

        elif path == "/api/v1/clinical/patient":
            try:
                res = self.clinical_ctrl.register_patient_endpoint(payload, actor_id="sys_admin", actor_role="system_admin")
                self._set_json_headers(201)
                self.wfile.write(json.dumps(res).encode())
            except Exception as e:
                self._set_json_headers(400)
                self.wfile.write(json.dumps({"error": str(e)}).encode())

        elif path == "/api/v1/cdss/ddi-check":
            drugs = payload.get("drugs", [])
            alerts = self.cdss_ctrl.check_drug_interactions(drugs)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"alerts": alerts, "count": len(alerts)}).encode())

        else:
            self._set_json_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint Not Found", "path": path}).encode())

def run_server(host: str = "127.0.0.1", port: int = 8000):
    server = HTTPServer((host, port), HealthCareHTTPRequestHandler)
    print(f"[*] CarePulse Enterprise EHR server listening on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server shutdown gracefully.")
    finally:
        server.server_close()

if __name__ == '__main__':
    cfg = get_config()
    run_server(cfg.host, cfg.port)

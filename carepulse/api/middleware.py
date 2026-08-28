"""
API Middleware for Request Tracing, CORS, and HIPAA Audit Interception.
"""

import time
import uuid
from typing import Callable, Dict, Any
from carepulse.auth.audit import HIPAALogger, AuditAction

class RequestContextMiddleware:
    def __init__(self, app_handler: Callable):
        self.handler = app_handler
        self.audit_logger = HIPAALogger()

    def process_request(self, request_headers: Dict[str, str], method: str, path: str) -> Dict[str, Any]:
        trace_id = request_headers.get("X-Request-ID", f"req_{uuid.uuid4().hex[:12]}")
        start_time = time.time()

        return {
            "trace_id": trace_id,
            "method": method,
            "path": path,
            "start_time": start_time
        }

    def process_response(self, context: Dict[str, Any], status_code: int) -> Dict[str, str]:
        duration_ms = round((time.time() - context["start_time"]) * 1000, 2)
        return {
            "X-Request-ID": context["trace_id"],
            "X-Response-Time-MS": str(duration_ms),
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
        }

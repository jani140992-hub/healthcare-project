"""
Authentication & Authorization API Route Controllers.
"""

from typing import Dict, Any, Optional
from carepulse.auth.service import AuthService
from carepulse.auth.models import Role

class AuthAPIController:
    def __init__(self, db_engine=None):
        self.auth_service = AuthService(db_engine)

    def login_endpoint(self, payload: Dict[str, Any], ip_address: str = "127.0.0.1") -> Dict[str, Any]:
        username = payload.get("username", "")
        password = payload.get("password", "")
        res = self.auth_service.authenticate(username, password, ip_address=ip_address)
        if not res:
            return {"status": "error", "message": "Invalid username or password", "code": 401}
        user, token = res
        return {
            "status": "success",
            "token": token,
            "user": {
                "id": user.id,
                "username": user.username,
                "role": user.role.value,
                "full_name": user.full_name
            }
        }

    def register_user_endpoint(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        role_str = payload.get("role", "registered_nurse")
        user = self.auth_service.register_user(
            username=payload["username"],
            email=payload["email"],
            password=payload["password"],
            first_name=payload["first_name"],
            last_name=payload["last_name"],
            role=Role(role_str),
            department=payload.get("department")
        )
        return {
            "status": "success",
            "user_id": user.id,
            "username": user.username
        }

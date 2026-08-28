"""
Security Decorators & Permission Enforcement Engine.
Enforces HIPAA Title II Access Control (45 CFR § 164.312(a)(1)).
"""

import functools
from typing import Callable, Any
from carepulse.auth.models import User, Permission

class PermissionDeniedError(Exception):
    def __init__(self, message: str = "Access Denied: Insufficient HIPAA Permissions"):
        super().__init__(message)
        self.message = message

def require_permission(permission: Permission):
    """
    Decorator to assert that the calling user context possesses the necessary permission.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            user = kwargs.get("current_user")
            if not user:
                for arg in args:
                    if isinstance(arg, User):
                        user = arg
                        break
            if not user:
                raise PermissionDeniedError("Authentication context missing: No current user provided")
            if not user.has_permission(permission):
                raise PermissionDeniedError(
                    f"User '{user.username}' with role '{user.role.value}' lacks required permission: '{permission.value}'"
                )
            return func(*args, **kwargs)
        return wrapper
    return decorator

def check_patient_context_access(user: User, patient_id: str) -> bool:
    """
    Ensures Patients can only access their own records, while Clinical Staff can access within scope.
    """
    if user.role.value == "patient":
        return user.id == patient_id
    return user.has_permission(Permission.PATIENT_READ)

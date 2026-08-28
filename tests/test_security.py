"""
Unit Tests for HIPAA Security, Authentication, RBAC, and Cryptographic Audit Chain.
"""

import unittest
import os
import tempfile
from carepulse.database import DatabaseEngine
from carepulse.auth.models import Role, Permission, User
from carepulse.auth.service import AuthService
from carepulse.auth.audit import HIPAALogger, AuditAction

class TestSecuritySubsystem(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.temp_db.close()
        self.db = DatabaseEngine(db_path=self.temp_db.name)
        self.auth_svc = AuthService(self.db)
        self.audit_logger = HIPAALogger(self.db)

    def tearDown(self):
        try:
            os.unlink(self.temp_db.name)
        except Exception:
            pass

    def test_user_registration_and_authentication(self):
        user = self.auth_svc.register_user(
            username="dr_watson",
            email="watson@bakerstreet.org",
            password="SecurePassword2026!",
            first_name="John",
            last_name="Watson",
            role=Role.ATTENDING_PHYSICIAN
        )
        self.assertEqual(user.username, "dr_watson")
        self.assertEqual(user.role, Role.ATTENDING_PHYSICIAN)

        # Successful auth
        res = self.auth_svc.authenticate("dr_watson", "SecurePassword2026!")
        self.assertIsNotNone(res)
        auth_user, token = res
        self.assertEqual(auth_user.id, user.id)
        self.assertTrue(len(token) > 20)

        # Decode JWT
        decoded = self.auth_svc.decode_jwt(token)
        self.assertIsNotNone(decoded)
        self.assertEqual(decoded["sub"], user.id)
        self.assertEqual(decoded["role"], "attending_physician")

        # Wrong password
        wrong = self.auth_svc.authenticate("dr_watson", "WrongPassword!")
        self.assertIsNone(wrong)

    def test_rbac_permissions_enforcement(self):
        doctor = User(id="u1", username="doc", email="doc@med.org", first_name="Dr", last_name="Who", role=Role.ATTENDING_PHYSICIAN)
        nurse = User(id="u2", username="nurse", email="nurse@med.org", first_name="Florence", last_name="N", role=Role.REGISTERED_NURSE)
        pharmacist = User(id="u3", username="pharm", email="pharm@med.org", first_name="Carl", last_name="P", role=Role.CLINICAL_PHARMACIST)

        # Doctor can prescribe
        self.assertTrue(doctor.has_permission(Permission.PRESCRIPTION_WRITE))
        self.assertTrue(doctor.has_permission(Permission.CLINICAL_NOTE_SIGN))

        # Nurse cannot prescribe, but can read/write patient data
        self.assertFalse(nurse.has_permission(Permission.PRESCRIPTION_WRITE))
        self.assertTrue(nurse.has_permission(Permission.PATIENT_WRITE))

        # Pharmacist can dispense
        self.assertTrue(pharmacist.has_permission(Permission.PRESCRIPTION_DISPENSE))
        self.assertFalse(pharmacist.has_permission(Permission.PRESCRIPTION_WRITE))

    def test_tamper_evident_hipaa_audit_chain(self):
        # Generate 5 chained audit events
        for i in range(5):
            self.audit_logger.log_event(
                actor_id="user_test",
                actor_role="attending_physician",
                action=AuditAction.PHI_READ,
                resource_type="Patient",
                resource_id=f"pat_{i}",
                patient_id=f"pat_{i}",
                details={"action_index": i}
            )

        # Verify integrity
        is_valid, err = self.audit_logger.verify_integrity()
        self.assertTrue(is_valid, f"Chain integrity failed: {err}")

        # Tamper with an audit entry directly in SQLite
        tamper_sql = "UPDATE hipaa_audit_log SET details = '{\"tampered\": true}' WHERE id = 3"
        self.db.execute_insert(tamper_sql)

        # Re-verify -> Must detect tampering!
        tampered_valid, tamper_err = self.audit_logger.verify_integrity()
        self.assertFalse(tampered_valid)
        self.assertIn("Tampered entry detected", tamper_err)

if __name__ == '__main__':
    unittest.main()

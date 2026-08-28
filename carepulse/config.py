"""
Enterprise Configuration Management for CarePulse.
Supports environment-based configuration, HIPAA compliance switches, and encryption settings.
"""

import os
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class DatabaseConfig:
    db_type: str = "sqlite"
    sqlite_path: str = "carepulse.db"
    host: Optional[str] = None
    port: Optional[int] = 5432
    username: Optional[str] = None
    password: Optional[str] = None
    database_name: str = "carepulse_ehr"
    connection_timeout: int = 30
    pool_size: int = 20
    max_overflow: int = 10

@dataclass
class SecurityConfig:
    secret_key: str = "carepulse-enterprise-insecure-dev-key-change-in-prod-2026"
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 60
    mfa_required: bool = True
    session_timeout_minutes: int = 15
    password_min_length: int = 12
    password_require_special: bool = True
    password_require_numbers: bool = True
    password_require_uppercase: bool = True
    max_login_attempts: int = 5
    lockout_duration_minutes: int = 30
    hipaa_audit_trail_enabled: bool = True
    phi_encryption_at_rest: bool = True

@dataclass
class FHIRConfig:
    enabled: bool = True
    version: str = "R4"
    base_url: str = "/api/v1/fhir"
    default_page_size: int = 50
    max_page_size: int = 500
    strict_validation: bool = True

@dataclass
class CDSSConfig:
    enable_ddi_alerts: bool = True
    enable_allergy_contraindications: bool = True
    enable_early_warning_scores: bool = True
    enable_pediatric_weight_checks: bool = True
    early_warning_system: str = "NEWS2"  # NEWS2, qSOFA, MEWS

@dataclass
class Config:
    environment: str = "development"  # development, staging, production
    app_name: str = "CarePulse Enterprise EHR"
    api_prefix: str = "/api/v1"
    host: str = "127.0.0.1"
    port: int = 8000
    debug: bool = True
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    security: SecurityConfig = field(default_factory=SecurityConfig)
    fhir: FHIRConfig = field(default_factory=FHIRConfig)
    cdss: CDSSConfig = field(default_factory=CDSSConfig)
    allowed_origins: List[str] = field(default_factory=lambda: ["http://localhost:3000", "http://127.0.0.1:8000"])

_config_instance: Optional[Config] = None

def get_config() -> Config:
    global _config_instance
    if _config_instance is None:
        env = os.getenv("CAREPULSE_ENV", "development")
        sqlite_file = os.getenv("CAREPULSE_DB_FILE", "carepulse.db")
        secret = os.getenv("CAREPULSE_SECRET_KEY", "carepulse-enterprise-insecure-dev-key-change-in-prod-2026")
        
        db_cfg = DatabaseConfig(sqlite_path=sqlite_file)
        sec_cfg = SecurityConfig(secret_key=secret)
        _config_instance = Config(
            environment=env,
            debug=(env == "development"),
            database=db_cfg,
            security=sec_cfg
        )
    return _config_instance

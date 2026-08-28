"""
OpenAPI 3.0.3 Specification Definition for CarePulse Healthcare API.
"""

from typing import Dict, Any

OPENAPI_SPECIFICATION: Dict[str, Any] = {
    "openapi": "3.0.3",
    "info": {
        "title": "CarePulse Enterprise EHR & FHIR R4 API",
        "description": "Comprehensive RESTful Healthcare API providing electronic health record management, clinical decision support, and HL7 FHIR R4 interoperability.",
        "version": "2.4.0",
        "contact": {
            "name": "CarePulse Engineering",
            "email": "api@carepulse.health"
        },
        "license": {
            "name": "Apache 2.0",
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
        }
    },
    "servers": [
        {"url": "http://127.0.0.1:8000", "description": "Local Development Server"}
    ],
    "paths": {
        "/health": {
            "get": {
                "summary": "Health Check & Capabilities",
                "responses": {
                    "200": {
                        "description": "System status and supported standards."
                    }
                }
            }
        },
        "/api/v1/auth/login": {
            "post": {
                "summary": "Staff Login & JWT Generation",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "username": {"type": "string"},
                                    "password": {"type": "string"}
                                },
                                "required": ["username", "password"]
                            }
                        }
                    }
                },
                "responses": {
                    "200": {"description": "JWT authentication token."},
                    "401": {"description": "Invalid credentials or account locked."}
                }
            }
        },
        "/api/v1/clinical/patient": {
            "post": {
                "summary": "Register New Patient (MPI)",
                "security": [{"BearerAuth": []}],
                "responses": {
                    "201": {"description": "Patient successfully registered."}
                }
            }
        },
        "/api/v1/cdss/ddi-check": {
            "post": {
                "summary": "Drug-Drug Interaction Screening",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "drugs": {"type": "array", "items": {"type": "string"}}
                                },
                                "required": ["drugs"]
                            }
                        }
                    }
                },
                "responses": {
                    "200": {"description": "List of interaction alerts and severity."}
                }
            }
        },
        "/api/v1/fhir/Patient/{id}": {
            "get": {
                "summary": "Retrieve FHIR R4 Patient Resource",
                "parameters": [
                    {"name": "id", "in": "path", "required": True, "schema": {"type": "string"}}
                ],
                "responses": {
                    "200": {"description": "Standard FHIR Patient JSON document."}
                }
            }
        }
    },
    "components": {
        "securitySchemes": {
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT"
            }
        }
    }
}

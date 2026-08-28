"""
CLI utility to export OpenAPI 3.0.3 specification to JSON.
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from carepulse.api.openapi_spec import OPENAPI_SPECIFICATION

def main():
    target = os.path.join(BASE_DIR, "openapi.json")
    with open(target, "w", encoding="utf-8") as f:
        json.dump(OPENAPI_SPECIFICATION, f, indent=2)
    print(f"[OK] Exported OpenAPI specification to {target}")

if __name__ == '__main__':
    main()

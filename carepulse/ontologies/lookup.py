"""
Clinical Ontology Fast Lookup & Fuzzy Matching Engine.
Provides prefix indexing, tokenized search, and category filtering across clinical taxonomies.
"""

from typing import Dict, List, Any, Optional

class OntologyLookupEngine:
    def __init__(self, items: Optional[List[Dict[str, Any]]] = None, code_key: str = "code", name_key: str = "description"):
        self.code_key = code_key
        self.name_key = name_key
        self.by_code: Dict[str, Dict[str, Any]] = {}
        self.index: List[Dict[str, Any]] = []

        if items:
            for it in items:
                self.add_item(it)

    def add_item(self, item: Dict[str, Any]):
        c = str(item.get(self.code_key, "")).upper().strip()
        self.by_code[c] = item
        self.index.append(item)

    def lookup_by_code(self, code: str) -> Optional[Dict[str, Any]]:
        return self.by_code.get(code.upper().strip())

    def search_by_text(self, query: str, limit: int = 20) -> List[Dict[str, Any]]:
        tokens = query.lower().split()
        results = []
        for item in self.index:
            desc = str(item.get(self.name_key, "")).lower()
            code = str(item.get(self.code_key, "")).lower()
            if all(tok in desc or tok in code for tok in tokens):
                results.append(item)
                if len(results) >= limit:
                    break
        return results

"""
Pharmacy Inventory & Stock Management.
Tracks lot numbers, serial barcodes, expiration dates, refrigeration controls, and DEA schedules.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Optional

@dataclass
class MedicationInventoryItem:
    item_id: str
    ndc: str
    drug_name: str
    strength: str
    dosage_form: str
    lot_number: str
    expiration_date: str  # YYYY-MM-DD
    quantity_on_hand: int
    reorder_threshold: int = 100
    dea_schedule: Optional[str] = None  # Schedule II, III, IV, V, or Non-controlled
    requires_refrigeration: bool = False
    storage_bin: Optional[str] = None

class PharmacyInventoryService:
    def __init__(self):
        self._inventory: Dict[str, MedicationInventoryItem] = {}

    def add_or_update_stock(self, item: MedicationInventoryItem):
        self._inventory[item.item_id] = item

    def check_stock_availability(self, ndc: str, required_quantity: int) -> bool:
        total = sum(i.quantity_on_hand for i in self._inventory.values() if i.ndc == ndc and not self._is_expired(i.expiration_date))
        return total >= required_quantity

    def deduct_stock(self, item_id: str, quantity: int) -> bool:
        item = self._inventory.get(item_id)
        if not item or item.quantity_on_hand < quantity:
            return False
        item.quantity_on_hand -= quantity
        return True

    def get_expiring_soon(self, days: int = 30) -> List[MedicationInventoryItem]:
        now_dt = datetime.now(timezone.utc)
        expiring = []
        for item in self._inventory.values():
            try:
                exp_dt = datetime.strptime(item.expiration_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
                diff = (exp_dt - now_dt).days
                if 0 <= diff <= days:
                    expiring.append(item)
            except Exception:
                pass
        return expiring

    def get_low_stock_items(self) -> List[MedicationInventoryItem]:
        return [item for item in self._inventory.values() if item.quantity_on_hand <= item.reorder_threshold]

    @staticmethod
    def _is_expired(exp_date_str: str) -> bool:
        try:
            exp_dt = datetime.strptime(exp_date_str, "%Y-%m-%d").date()
            return exp_dt < datetime.now(timezone.utc).date()
        except Exception:
            return True

"""Inventory storage management."""

import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "inventory.json"


def load_inventory():
    """Load inventory data from the JSON file."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_inventory(inventory):
    """Save inventory data to the JSON file."""
    DATA_DIR.mkdir(exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(inventory, f, indent=4)

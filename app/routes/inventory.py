"""Routes for the Coffee Tracker API."""

from fastapi import APIRouter, FastAPI, HTTPException

from app.schemas import (
    Inventory,
    InventoryAddSupply,
    InventoryCreate,
    InventoryRemove,
)
from app.storage import load_inventory, save_inventory

router = APIRouter(prefix="/api/v1", tags=["Inventory"])


# Get the current inventory of the coffee shop
@router.get("")
def get_inventory():
    """Get the current inventory of coffee."""
    return load_inventory()


# Get inventory item by ID
@router.get("/{item_id}")
def get_inventory_item(item_id: int):
    """Get an inventory item by its ID."""
    inventory = load_inventory()
    for item in inventory:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@router.post("/create")
def create_inventory_item(item: InventoryCreate):
    """Create a new inventory item."""
    inventory = load_inventory()
    for inv_item in inventory:
        if inv_item["id"] == item.id:
            raise HTTPException(
                status_code=400, detail="Item with this ID already exists"
            )
    new_item = {
        "id": item.id,
        "name": item.name,
        "quantity": item.quantity,
        "description": item.description or "",
    }
    inventory.append(new_item)
    save_inventory(inventory)
    return new_item


# Add a new item to the inventory
@router.post("/add")
def add_inventory_item(item: InventoryAddSupply):
    """Add a new item to the inventory."""
    inventory = load_inventory()
    for inv_item in inventory:
        if inv_item["id"] == item.item_id:
            inv_item["quantity"] += item.quantity
            save_inventory(inventory)
            return inv_item
    new_item = {
        "id": item.item_id,
        "name": f"Item {item.item_id}",
        "quantity": item.quantity,
        "description": "",
    }
    inventory.append(new_item)
    save_inventory(inventory)
    return new_item


# Remove an item from the inventory
@router.post("/remove")
def remove_inventory_item(item: InventoryRemove):
    """Remove an item from the inventory."""
    inventory = load_inventory()
    for i, inv_item in enumerate(inventory):
        if inv_item["id"] == item.item_id:
            if inv_item["quantity"] < item.quantity:
                raise HTTPException(
                    status_code=400, detail="Not enough quantity to remove"
                )
            inv_item["quantity"] -= item.quantity
            if inv_item["quantity"] == 0:
                inventory.pop(i)
            save_inventory(inventory)
            return {"message": "Item removed successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

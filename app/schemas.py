from typing import Optional

from pydantic import BaseModel, Field


class Inventory(BaseModel):
    id: int
    name: str
    quantity: float
    unit: str
    description: Optional[str] = None


class InventoryStatus(BaseModel):
    total_items: int = Field(..., description="Total number of items in inventory")
    total_quantity: float = Field(
        ..., description="Total quantity of all items in inventory"
    )


class InventoryAddSupply(BaseModel):
    item_id: int = Field(..., description="ID of the item to add supply to")
    quantity: float = Field(..., description="Quantity to add to inventory")


class InventoryRemove(BaseModel):
    item_id: int = Field(..., description="ID of the item to remove")
    quantity: float = Field(..., description="Quantity to remove from inventory")


class InventoryUpdate(BaseModel):
    item_id: int = Field(..., description="ID of the item to update")
    name: Optional[str] = Field(None, description="New name for the item")
    quantity: Optional[float] = Field(None, description="New quantity for the item")
    description: Optional[str] = Field(None, description="New description for the item")


class InventoryCreate(BaseModel):
    id: int = Field(..., description="ID for the new inventory item")
    name: str = Field(..., description="Name of the new inventory item")
    quantity: float = Field(..., description="Initial quantity for the new item")
    unit: str = Field(..., description="Unit of measurement for the new item")
    description: Optional[str] = Field(None, description="Description for the new item")

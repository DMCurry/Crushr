from pydantic import BaseModel
from typing import List
from utilities import ItemType


class RemoveItemSchema(BaseModel):
    plan_id: int
    item_id: int
    item_type: ItemType


class AddItemsInputSchema(BaseModel):
    plan_id: int
    item_ids: List[int]


class CreatePlanInputSchema(BaseModel):
    plan_name: str
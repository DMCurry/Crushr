from pydantic import BaseModel
from typing import List

class AddItemsInputSchema(BaseModel):
    plan_id: int
    item_ids: List[int]


class CreatePlanInputSchema(BaseModel):
    plan_name: str
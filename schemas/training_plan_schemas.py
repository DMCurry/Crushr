from pydantic import BaseModel
from typing import List
from utilities import ItemType
from schemas.exercise_schemas import ExerciseSchema
from schemas.performance_test_schemas import PerformanceTestSchema


class RemoveItemSchema(BaseModel):
    plan_id: int
    item_id: int
    item_type: ItemType


class AddItemsInputSchema(BaseModel):
    plan_id: int
    item_ids: List[int]


class CreatePlanInputSchema(BaseModel):
    plan_name: str


class UpdatePlanInputSchema(CreatePlanInputSchema):
    plan_id: int


class TrainingPlanOutputSchema(BaseModel):
    plan_name: str
    id: int
    exercises: List[ExerciseSchema]
    performance_tests: List[PerformanceTestSchema]

    class Config:
        from_attributes = True


from pydantic import BaseModel
from typing import List
from utilities import ItemType
from schemas.exercise_schemas import ExerciseSchemaWithID
from schemas.performance_test_schemas import PerformanceTestSchemaWithID


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
    exercises: List[ExerciseSchemaWithID]
    performance_tests: List[PerformanceTestSchemaWithID]

    class Config:
        from_attributes = True


class TrainingPlansOutputSchema(BaseModel):
    plans: List[TrainingPlanOutputSchema]
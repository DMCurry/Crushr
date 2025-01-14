from pydantic import BaseModel
from typing import List

class AddExercisesInputSchema(BaseModel):
    plan_id: int
    exercise_ids: List[int]
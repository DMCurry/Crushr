from pydantic import BaseModel
from typing import List, Optional

class ScheduleExerciseSchema(BaseModel):
    exercise_id: int
    exercise_name: str
    exercise_reps: int
    exercise_description: str

class ScheduleSchema(BaseModel):
    Monday: Optional[List[ScheduleExerciseSchema]] = None
    Tuesday: Optional[List[ScheduleExerciseSchema]] = None
    Wednesday: Optional[List[ScheduleExerciseSchema]] = None
    Thursday: Optional[List[ScheduleExerciseSchema]] = None
    Friday: Optional[List[ScheduleExerciseSchema]] = None

class WeeklyScheduleSchema(BaseModel):
    data: Optional[ScheduleSchema] = None


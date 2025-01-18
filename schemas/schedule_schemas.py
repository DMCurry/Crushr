from pydantic import BaseModel
from typing import List, Optional

class ScheduleExerciseOutputSchema(BaseModel):
    exercise_id: int
    exercise_name: str
    exercise_reps: int
    exercise_description: str

class ScheduleOutputSchema(BaseModel):
    Monday: Optional[List[ScheduleExerciseOutputSchema]] = None
    Tuesday: Optional[List[ScheduleExerciseOutputSchema]] = None
    Wednesday: Optional[List[ScheduleExerciseOutputSchema]] = None
    Thursday: Optional[List[ScheduleExerciseOutputSchema]] = None
    Friday: Optional[List[ScheduleExerciseOutputSchema]] = None

class WeeklyScheduleOutputSchema(BaseModel):
    data: Optional[ScheduleOutputSchema] = None
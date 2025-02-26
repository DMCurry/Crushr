from pydantic import BaseModel
from typing import List, Optional

class ScheduleExerciseSchema(BaseModel):
    exercise_id: int
    exercise_name: str
    exercise_reps: int
    exercise_description: str

class SchedulePerformanceTestSchema(BaseModel):
    performance_test_id: int
    performance_test_name: str
    performance_test_value: float
    performance_test_description: str

class ScheduleItems(BaseModel):
    exercises: Optional[List[ScheduleExerciseSchema]] = None
    performance_tests: Optional[List[SchedulePerformanceTestSchema]] = None

class ScheduleSchema(BaseModel):
    Monday: Optional[ScheduleItems] = None
    Tuesday: Optional[ScheduleItems] = None
    Wednesday: Optional[ScheduleItems] = None
    Thursday: Optional[ScheduleItems] = None
    Friday: Optional[ScheduleItems] = None
    Saturday: Optional[ScheduleItems] = None
    Sunday: Optional[ScheduleItems] = None

class WeeklyScheduleSchema(BaseModel):
    data: Optional[ScheduleSchema] = None

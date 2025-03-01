from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

from .exercise import Exercise
from .performance_test import PerformanceTest
from .analytics import Analytics
from .training_plan import TrainingPlan
from .training_exercise import training_exercise
from .weekly_schedule import WeeklySchedule
from .user import User
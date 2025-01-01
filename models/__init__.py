from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

from .exercise import Exercise
from .performance_test import PerformanceTest
from .schedule import Schedule
from .schedule_exercise import schedule_exercise
from .training_plan import TrainingPlan
from .user import User
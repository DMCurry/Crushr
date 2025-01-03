from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

from .exercise import Exercise
from .performance_test import PerformanceTest
from .training_plan import TrainingPlan
from .training_exercise import training_exercise
from .user import User
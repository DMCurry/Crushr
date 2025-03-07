from typing import List, Literal
import enum
from sqlalchemy import String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.training_exercise import training_exercise
from models.training_performance_test import training_performance_test
# from models.exercise import Exercise
# from models.training_plan import TrainingPlan
# from models.performance_test import PerformanceTest
from . import Base


class TrainingPlan(Base):
    __tablename__ = "training_plan"

    id: Mapped[int] = mapped_column(primary_key=True)
    plan_name: Mapped[str] = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="training_plans")
    performance_tests: Mapped[List["PerformanceTest"]] = relationship(
        secondary=training_performance_test,
        back_populates="training_plans"
    )
    exercises: Mapped[List["Exercise"]] = relationship(
        secondary=training_exercise,
        back_populates="training_plans"
    )
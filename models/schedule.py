from __future__ import annotations

from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.schedule_exercise import schedule_exercise
# from models.exercise import Exercise
# from models.training_plan import TrainingPlan
# from models.performance_test import PerformanceTest
from . import Base


class Schedule(Base):
    __tablename__ = "schedule"

    id: Mapped[int] = mapped_column(primary_key=True)
    plan_name: Mapped[str] = mapped_column(String(30))
    plan_id: Mapped[int] = mapped_column(ForeignKey("training_plan.id"))
    plan: Mapped["TrainingPlan"] = relationship(back_populates="schedule")
    performance_tests: Mapped[List["PerformanceTest"]] = relationship()
    exercises: Mapped[List["Exercise"]] = relationship(
        secondary=schedule_exercise,
        back_populates="schedules"
    )
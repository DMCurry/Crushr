from __future__ import annotations

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from models.weekly_schedule import WeeklySchedule
from . import Base
from models.training_exercise import training_exercise
#from models.training_plan import TrainingPlan


class Exercise(Base):
    __tablename__ = "exercise"

    id: Mapped[int] = mapped_column(primary_key=True)
    exercise_name: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    reps: Mapped[int] = mapped_column(Integer, nullable=False)
    training_plan_id: Mapped[Optional[int]] = mapped_column(ForeignKey("training_plan.id"), nullable=True)
    weekly_schedule: Mapped["WeeklySchedule"] = relationship(back_populates="exercise")
    training_plan: Mapped[List["TrainingPlan"]] = relationship(
        secondary=training_exercise,
        back_populates="exercises"
    )
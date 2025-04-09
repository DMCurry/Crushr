from __future__ import annotations

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from . import Base
from models.training_exercise import training_exercise
from models.weekly_schedule_exercise import weekly_schedule_exercise
#from models.training_plan import TrainingPlan


class Exercise(Base):
    __tablename__ = "exercise"

    id: Mapped[int] = mapped_column(primary_key=True)
    exercise_name: Mapped[str] = mapped_column(String(60), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    reps: Mapped[int] = mapped_column(Integer, nullable=False)
    sets: Mapped[int] = mapped_column(Integer, nullable=False)
    link: Mapped[str] = mapped_column(String(200), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    weekly_schedule_days: Mapped[List["WeeklySchedule"]] = relationship(
        secondary=weekly_schedule_exercise,
        back_populates="exercises"
    )
    training_plans: Mapped[List["TrainingPlan"]] = relationship(
        secondary=training_exercise,
        back_populates="exercises"
    )
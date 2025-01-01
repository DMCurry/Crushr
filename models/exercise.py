from __future__ import annotations

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from . import Base
from models.schedule_exercise import schedule_exercise
from models.schedule import Schedule


class Exercise(Base):
    __tablename__ = "exercise"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    reps: Mapped[int] = mapped_column(Integer, nullable=False)
    schedule_id: Mapped[Optional[int]] = mapped_column(ForeignKey("schedule.id"), nullable=True)
    schedules: Mapped[List[Schedule]] = relationship(
        secondary=schedule_exercise,
        back_populates="exercises"
    )
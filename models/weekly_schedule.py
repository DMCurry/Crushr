from typing import List, Literal
from sqlalchemy import String, Enum, ForeignKey
from utilities import Weekday
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.weekly_schedule_exercise import weekly_schedule_exercise
from . import Base



class WeeklySchedule(Base):
    __tablename__ = "weekly_schedule"

    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[Weekday] = mapped_column(Enum(Weekday))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    exercises: Mapped[List["Exercise"]] = relationship(
        secondary=weekly_schedule_exercise,
        back_populates="weekly_schedule_days"
    )
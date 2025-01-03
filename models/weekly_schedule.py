from typing import List, Literal
import enum
from sqlalchemy import String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base

class Weekday(enum.Enum):
    MON = "Monday"
    TUE = "Tuesday"
    WED = "Wednesday"
    THU = "Thursday"
    FRI = "Friday"


class WeeklySchedule(Base):
    __tablename__ = "weekly_schedule"

    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[Weekday] = mapped_column(Enum(Weekday))
    exercise_id: Mapped[int] = mapped_column(ForeignKey("exercise.id"))
    exercise: Mapped["Exercise"] = relationship(back_populates="weekly_schedule")
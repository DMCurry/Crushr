from typing import List, Literal
import enum
from sqlalchemy import String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.weekly_schedule_exercise import weekly_schedule_exercise
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
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    exercises: Mapped[List["Exercise"]] = relationship(secondary=weekly_schedule_exercise)

from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from . import Base


weekly_schedule_exercise = Table(
    "weekly_schedule_exercise",
    Base.metadata,
    Column("weekly_schedule_id", ForeignKey("weekly_schedule.id")),
    Column("exercise_id", ForeignKey("exercise.id"))
)
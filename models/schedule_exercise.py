from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from . import Base


schedule_exercise = Table(
    "schedule_exercise",
    Base.metadata,
    Column("schedule_id", ForeignKey("schedule.id"), primary_key=True),
    Column("exercise_id", ForeignKey("exercise.id"), primary_key=True)
)
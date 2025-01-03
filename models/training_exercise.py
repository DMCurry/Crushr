from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from . import Base


training_exercise = Table(
    "training_exercise",
    Base.metadata,
    Column("training_plan_id", ForeignKey("training_plan.id"), primary_key=True),
    Column("exercise_id", ForeignKey("exercise.id"), primary_key=True)
)
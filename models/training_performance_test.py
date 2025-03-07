from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from . import Base


training_performance_test = Table(
    "training_performance_test",
    Base.metadata,
    Column("training_plan_id", ForeignKey("training_plan.id"), primary_key=True),
    Column("performance_test_id", ForeignKey("performance_test.id"), primary_key=True)
)

from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from . import Base


weekly_schedule_performance_test = Table(
    "weekly_schedule_performance_test",
    Base.metadata,
    Column("weekly_schedule_id", ForeignKey("weekly_schedule.id")),
    Column("performance_test_id", ForeignKey("performance_test.id"))
)
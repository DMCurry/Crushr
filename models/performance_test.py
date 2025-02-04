from __future__ import annotations

from typing import Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy import String, Float, Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from . import Base
from models.weekly_schedule_performance_test import weekly_schedule_performance_test


#from models.training_plan import TrainingPlan


class PerformanceTest(Base):
    __tablename__ = "performance_test"

    id: Mapped[int] = mapped_column(primary_key=True)
    test_name: Mapped[str] = mapped_column(String(30))
    performance_value: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    training_plan_id: Mapped[Optional[int]] = mapped_column(ForeignKey("training_plan.id"), nullable=True)
    training_plan: Mapped["TrainingPlan"] = relationship(back_populates="performance_tests")
    weekly_schedule_days_performance: Mapped[List["WeeklySchedule"]] = relationship(
        secondary=weekly_schedule_performance_test,
        back_populates="performance_tests"
    )
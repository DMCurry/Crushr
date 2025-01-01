from __future__ import annotations

from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Float, Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from . import Base
from models.schedule import Schedule


class PerformanceTest(Base):
    __tablename__ = "performance_test"

    id: Mapped[int] = mapped_column(primary_key=True)
    test_name: Mapped[str] = mapped_column(String(30))
    performance_value: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    schedule_id: Mapped[Optional[int]] = mapped_column(ForeignKey("schedule.id"), nullable=True)
    schedule: Mapped["Schedule"] = relationship(back_populates="schedule")
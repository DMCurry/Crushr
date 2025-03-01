from sqlalchemy import ForeignKey, Float, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from typing import List
from . import Base


class Analytics(Base):
    __tablename__ = "analytics"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    performance_test_id: Mapped[int] = mapped_column(ForeignKey("performance_test.id"), nullable=False)
    performance_test_result: Mapped[float] = mapped_column(Float(2))
    test_date: Mapped[date] = mapped_column(Date())
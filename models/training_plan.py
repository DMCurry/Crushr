from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from . import Base
from models.schedule import Schedule


class TrainingPlan(Base):
    __tablename__ = "training_plan"

    id: Mapped[int] = mapped_column(primary_key=True)
    plan_name: Mapped[str] = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["Schedule"] = relationship(back_populates="training_plan")
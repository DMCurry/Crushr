from typing import List, Sequence
from sqlalchemy import select, ScalarResult
from sqlalchemy.orm import Mapped, joinedload

from models import TrainingPlan
from models.training_plan import TrainingPlan
from app.services.base import BaseService
from models.user import User


class TrainingPlanService(BaseService):

    def get_plan(self, plan_id) -> Mapped[TrainingPlan]:
        pass

    def get_plans(self, user_id) -> Sequence[TrainingPlan]:
        query = select(TrainingPlan).options(joinedload(TrainingPlan.exercises)).where(TrainingPlan.user_id == user_id)
        plans = self.db.execute(query).unique().scalars().all()
        return plans

    def create_plan(self, plan_input) -> Mapped[TrainingPlan]:
        pass
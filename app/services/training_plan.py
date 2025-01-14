from typing import List, Sequence
from sqlalchemy import select, ScalarResult
from sqlalchemy.orm import Mapped, joinedload

from models import TrainingPlan
from models import Exercise
from models.training_plan import TrainingPlan
from app.services.base import BaseService
from models.user import User


class TrainingPlanService(BaseService):

    def get_plan(self, plan_id: int) -> Mapped[TrainingPlan]:
        pass

    def get_plans(self, user_id) -> Sequence[TrainingPlan]:
        query = select(TrainingPlan).options(joinedload(TrainingPlan.exercises)).where(TrainingPlan.user_id == user_id)
        plans = self.db.execute(query).unique().scalars().all()
        return plans

    def create_plan(self, plan_input) -> Mapped[TrainingPlan]:
        pass

    def add_exercises_to_plan(self, user_id: int, plan_id: int, exercise_ids: List[int]):
        plan_query = select(TrainingPlan).where(TrainingPlan.user_id == user_id).where(TrainingPlan.id == plan_id)
        plan = self.db.execute(plan_query).scalar_one_or_none()
        exercise_query = select(Exercise).where(Exercise.id.in_(exercise_ids))
        exercises = self.db.execute(exercise_query).scalars()

        plan.exercises = list(exercises)
        self.db.commit()
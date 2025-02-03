from typing import List, Sequence
from sqlalchemy import select, ScalarResult
from sqlalchemy.orm import Mapped, joinedload

from models import Exercise, PerformanceTest
from models.training_plan import TrainingPlan
from app.services.base import BaseService
from models.user import User


class TrainingPlanService(BaseService):

    def get_plan(self, plan_id: int) -> Mapped[TrainingPlan]:
        pass

    def get_plans(self, user_id) -> Sequence[TrainingPlan]:
        query = select(TrainingPlan).options(joinedload(TrainingPlan.exercises), joinedload(TrainingPlan.performance_tests)).where(TrainingPlan.user_id == user_id)
        plans = self.db.execute(query).unique().scalars().all()
        return plans

    def create_plan(self, user_id: int, plan_name: str) -> TrainingPlan:
        training_plan = TrainingPlan(
            plan_name = plan_name,
            user_id = user_id
        )
        self.db.add(training_plan)
        self.db.commit()
        return training_plan

    def add_exercises_to_plan(self, user_id: int, plan_id: int, exercise_ids: List[int]):
        plan_query = select(TrainingPlan).where(TrainingPlan.user_id == user_id).where(TrainingPlan.id == plan_id)
        plan = self.db.execute(plan_query).scalar_one_or_none()
        exercise_query = select(Exercise).where(Exercise.id.in_(exercise_ids))
        exercises = self.db.execute(exercise_query).scalars()

        plan.exercises = list(exercises)
        self.db.commit()

    def add_performance_tests_to_plan(self, user_id: int, plan_id: int, performance_test_ids: List[int]):
        plan_query = select(TrainingPlan).where(TrainingPlan.user_id == user_id).where(TrainingPlan.id == plan_id)
        plan = self.db.execute(plan_query).scalar_one_or_none()
        performance_test_query = select(PerformanceTest).where(PerformanceTest.id.in_(performance_test_ids))
        performance_tests = self.db.execute(performance_test_query).scalars()

        plan.performance_tests = list(performance_tests)
        self.db.commit()

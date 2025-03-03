from typing import List, Sequence
from sqlalchemy import select, ScalarResult
from sqlalchemy.orm import Mapped, joinedload
from fastapi import status, HTTPException
from models import Exercise, PerformanceTest
from models.training_plan import TrainingPlan
from app.services.base import BaseService
from models.user import User
from utilities import ItemType


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

    def update_plan(self, user_id: int, plan_id: int, new_plan_name: str) -> TrainingPlan:
        plan_query = select(TrainingPlan).where(TrainingPlan.user_id == user_id).where(TrainingPlan.id == plan_id)
        plan = self.db.execute(plan_query).scalar_one_or_none()
        if plan is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="training plan not found"
            )
        plan.plan_name = new_plan_name
        self.db.commit()
        return plan

    def add_exercises_to_plan(self, user_id: int, plan_id: int, exercise_ids: List[int]) -> TrainingPlan:
        plan_query = select(TrainingPlan).where(TrainingPlan.user_id == user_id).where(TrainingPlan.id == plan_id)
        plan = self.db.execute(plan_query).scalar_one_or_none()
        exercise_query = select(Exercise).where(Exercise.id.in_(exercise_ids))
        exercises = self.db.execute(exercise_query).scalars()

        plan.exercises = list(exercises)
        self.db.commit()
        return plan

    def add_performance_tests_to_plan(self, user_id: int, plan_id: int, performance_test_ids: List[int]) -> TrainingPlan:
        plan_query = select(TrainingPlan).where(TrainingPlan.user_id == user_id).where(TrainingPlan.id == plan_id)
        plan = self.db.execute(plan_query).scalar_one_or_none()
        performance_test_query = select(PerformanceTest).where(PerformanceTest.id.in_(performance_test_ids))
        performance_tests = self.db.execute(performance_test_query).scalars()

        plan.performance_tests = list(performance_tests)
        self.db.commit()
        return plan

    def remove_item(self, user_id, item) -> TrainingPlan:
        plan_query = select(TrainingPlan).where(TrainingPlan.user_id == user_id).where(TrainingPlan.id == item.plan_id)
        plan = self.db.execute(plan_query).scalar_one_or_none()
        if plan is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="plan not found"
            )
        if item.item_type == ItemType.TEST:
            remove_item = next((test for test in plan.performance_tests if test.id == item.item_id), None)
            if remove_item is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="performance test not found"
                )
            plan.performance_tests.remove(remove_item)
        else:
            remove_item = next((exercise for exercise in plan.exercises if exercise.id == item.item_id), None)
            if remove_item is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="exercise not found"
                )
            plan.exercises.remove(remove_item)
        self.db.commit()
        return plan

    def delete_plan(self, user_id, plan_id) -> None:
        query = (select(TrainingPlan)
                 .where(TrainingPlan.user_id == user_id)
                 .where(TrainingPlan.id == plan_id)
                 )
        plan = self.db.execute(query).scalar_one_or_none()
        if not plan:
            raise status.HTTP_404_NOT_FOUND
        self.db.delete(plan)
        self.db.commit()

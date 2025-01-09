from typing import List
from sqlalchemy import select

from models import TrainingPlan
from models.user import User
from models.exercise import Exercise
from app.services.base import BaseService

class ExerciseService(BaseService):

    def get_exercise(self, name: str) -> Exercise:
        query = select(Exercise).where(Exercise.exercise_name == name)
        exercise = self.db.execute(query).scalar_one_or_none()
        return exercise

    def get_exercises(self, plan_id: int) -> List[Exercise]:
        query = select(TrainingPlan).where(TrainingPlan.id == plan_id)
        plan = self.db.execute(query).scalar_one_or_none()
        return plan.exercises

    def create_exercise(self):
        pass

    def update_exercise(self) -> Exercise:
        pass

    def delete_exercise(self):
        pass
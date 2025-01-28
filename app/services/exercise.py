from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Mapped
from models.user import User
from models.exercise import Exercise
from app.services.base import BaseService
from schemas.exercise_schemas import ExerciseSchema


class ExerciseService(BaseService):

    def get_exercise(self, name: str) -> Exercise:
        query = select(Exercise).where(Exercise.exercise_name == name)
        exercise = self.db.execute(query).scalar_one_or_none()
        return exercise

    def get_exercises(self, user_id: int) -> Mapped[List[Exercise]]:
        query = select(User).where(User.id == user_id)
        user = self.db.execute(query).scalar_one_or_none()
        return user.exercises

    def create_exercise(self, user_id: int, exercise_info: ExerciseSchema) -> Exercise:
        exercise = Exercise(
            exercise_name = exercise_info.exercise_name,
            description = exercise_info.description,
            reps = exercise_info.reps,
            user_id = user_id
        )
        self.db.add(exercise)
        self.db.commit()
        return exercise

    def update_exercise(self) -> Exercise:
        pass

    def delete_exercise(self):
        pass
from typing import List, Sequence
from sqlalchemy import select, ScalarResult, Row
from sqlalchemy.orm import Mapped, joinedload

from models import WeeklySchedule
from models import Exercise
from models.training_plan import TrainingPlan
from app.services.base import BaseService
from models.weekly_schedule_exercise import weekly_schedule_exercise


class ScheduleService(BaseService):

    def get_schedule(self, user_id: int) -> dict:
        query = (select(WeeklySchedule.day, Exercise.id, Exercise.exercise_name, Exercise.reps, Exercise.description)
                .join(weekly_schedule_exercise, WeeklySchedule.id == weekly_schedule_exercise.c.weekly_schedule_id)
                .join(Exercise, weekly_schedule_exercise.c.exercise_id == Exercise.id)
                .where(WeeklySchedule.user_id == user_id)
                .order_by(WeeklySchedule.day))
        schedule = self.db.execute(query).all()

        schedule_map = {}
        for day, exercise_id, exercise_name, exercise_reps, exercise_desc in schedule:
            if schedule_map.get(day) is None:
                schedule_map[day.value] = []
            schedule_map[day.value].append(
                {
                    "exercise_id": exercise_id,
                    "exercise_name": exercise_name,
                    "exercise_reps": exercise_reps,
                    "exercise_description": exercise_desc
                }
            )
        return schedule_map

    def get_scheduled_exercises(self, user_id: int) -> Mapped[list]:
        query = select(WeeklySchedule).where(WeeklySchedule.user_id == user_id)
        schedule = self.db.execute(query).scalar_one_or_none()
        return schedule.exercises

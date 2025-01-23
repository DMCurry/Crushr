from typing import List, Sequence
from sqlalchemy import select, ScalarResult, Row
from sqlalchemy.orm import Mapped, joinedload
from utilities import Weekday

from models import WeeklySchedule
from models import Exercise
from models.training_plan import TrainingPlan
from app.services.base import BaseService
from models.weekly_schedule_exercise import weekly_schedule_exercise
from schemas.schedule_schemas import WeeklyScheduleSchema


class ScheduleService(BaseService):

    def get_schedule(self, user_id: int) -> dict:
        query = select(WeeklySchedule).where(WeeklySchedule.user_id == user_id)
        schedule = self.db.execute(query).scalars().all()
        schedule_map = {}
        for row in schedule:
            day = row.day
            if schedule_map.get(day) is None:
                schedule_map[day.value] = []
            for exercise in row.exercises:
                schedule_map[day.value].append(
                    {
                        "exercise_id": exercise.id,
                        "exercise_name": exercise.exercise_name,
                        "exercise_reps": exercise.reps,
                        "exercise_description": exercise.description
                    }
                )
        return schedule_map

    def get_scheduled_exercises(self, user_id: int) -> Mapped[list]:
        query = select(WeeklySchedule).where(WeeklySchedule.user_id == user_id)
        schedule = self.db.execute(query).scalar_one_or_none()
        return schedule.exercises

    def update_schedule(self, user_id: int, schedule_data: WeeklyScheduleSchema) -> dict:
        for day, exercises in schedule_data.model_dump().items():
            query = (select(WeeklySchedule)
                     .where(WeeklySchedule.user_id == user_id)
                     .where(WeeklySchedule.day == Weekday(day)))
            day_schedule_row = self.db.execute(query).scalar_one_or_none()
            has_day_schedule = day_schedule_row is not None

            #  If there are no exercises for the day in request but there is a row in DB then remove row
            if (has_day_schedule and exercises is None) or (has_day_schedule and len(exercises) == 0):
                self.db.delete(day_schedule_row)
            elif exercises is not None:
                #  Update exercises for current day
                exercise_ids = [exercise.get("exercise_id") for exercise in exercises]
                exercises_query = select(Exercise).where(Exercise.id.in_(exercise_ids))
                exercise_objects = self.db.execute(exercises_query).scalars().all()
                if not has_day_schedule:
                    new_weekly_schedule_row = WeeklySchedule(
                        day = Weekday(day),
                        user_id = user_id,
                        exercises = exercise_objects
                    )
                    self.db.add(new_weekly_schedule_row)
                else:
                    day_schedule_row.exercises = exercise_objects
            self.db.commit()
        return self.get_schedule(user_id)
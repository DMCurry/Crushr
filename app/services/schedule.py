from typing import List, Sequence
from sqlalchemy import select, ScalarResult, Row
from sqlalchemy.orm import Mapped, joinedload
from utilities import Weekday

from models import WeeklySchedule, PerformanceTest, Exercise
from models.training_plan import TrainingPlan
from app.services.base import BaseService
from models.weekly_schedule_exercise import weekly_schedule_exercise
from schemas.schedule_schemas import WeeklyScheduleSchema


class ScheduleService(BaseService):

    def get_schedule(self, user_id: int) -> dict:
        schedule = self.get_current_schedule(user_id)
        schedule_map = {}
        for row in schedule:
            day = row.day
            if schedule_map.get(day) is None:
                schedule_map[day.value] = {"exercises": [], "performance_tests": []}
            for exercise in row.exercises:
                schedule_map[day.value]["exercises"].append(
                    {
                        "exercise_id": exercise.id,
                        "exercise_name": exercise.exercise_name,
                        "exercise_reps": exercise.reps,
                        "exercise_sets": exercise.sets,
                        "exercise_description": exercise.description
                    }
                )
            for performance_test in row.performance_tests:
                schedule_map[day.value]["performance_tests"].append(
                    {
                        "performance_test_id": performance_test.id,
                        "performance_test_name": performance_test.test_name,
                        "performance_test_value": performance_test.performance_value,
                        "performance_test_description": performance_test.description
                    }
                )
        return schedule_map

    def get_current_schedule(self, user_id: int):
        query = select(WeeklySchedule).where(WeeklySchedule.user_id == user_id)
        schedule = self.db.execute(query).scalars().all()
        return schedule

    def get_scheduled_exercises(self, user_id: int) -> Mapped[list]:
        query = select(WeeklySchedule).where(WeeklySchedule.user_id == user_id)
        schedule = self.db.execute(query).scalar_one_or_none()
        return schedule.exercises

    def update_schedule(self, user_id: int, schedule_data: WeeklyScheduleSchema) -> dict:
        for day, item_lists in schedule_data.model_dump().items():
            query = (select(WeeklySchedule)
                     .where(WeeklySchedule.user_id == user_id)
                     .where(WeeklySchedule.day == Weekday(day)))
            day_schedule_row = self.db.execute(query).scalar_one_or_none()
            has_day_schedule = day_schedule_row is not None
            exercises = [] if item_lists is None else [] if item_lists.get("exercises") is None else item_lists.get("exercises", [])
            performance_tests = [] if item_lists is None else [] if item_lists.get("performance_tests") is None else item_lists.get("performance_tests", [])
            no_items = len(exercises) == 0 and len(performance_tests) == 0

            #  If there are no exercises for the day in request but there is a row in DB then remove row
            if has_day_schedule and no_items:
                self.db.delete(day_schedule_row)
            else:
                #  Get exercises objects
                exercise_ids = [exercise.get("exercise_id") for exercise in exercises]
                exercises_query = select(Exercise).where(Exercise.id.in_(exercise_ids))
                exercise_objects = self.db.execute(exercises_query).scalars().all()

                # Get performance_test objects
                performance_test_ids = [performance_test.get("performance_test_id") for performance_test in performance_tests]
                performance_test_query = select(PerformanceTest).where(PerformanceTest.id.in_(performance_test_ids))
                performance_test_objects = self.db.execute(performance_test_query).scalars().all()

                if not has_day_schedule:
                    new_weekly_schedule_row = WeeklySchedule(
                        day = Weekday(day),
                        user_id = int(user_id),
                        exercises = exercise_objects,
                        performance_tests = performance_test_objects
                    )
                    self.db.add(new_weekly_schedule_row)
                else:
                    day_schedule_row.exercises = exercise_objects
                    day_schedule_row.performance_tests = performance_test_objects
            self.db.commit()
        return self.get_schedule(user_id)

    def remove_non_training_plan_exercises(self, user_id: int):
        schedule = self.get_current_schedule(user_id)
        for row in schedule:
            for exercise in list(row.exercises):
                if len(exercise.training_plans) == 0:
                    row.exercises.remove(exercise)
            for performance_test in list(row.performance_tests):
                if len(performance_test.training_plans) == 0:
                    row.performance_tests.remove(performance_test)
        self.db.commit()
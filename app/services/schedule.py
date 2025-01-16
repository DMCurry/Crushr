from typing import List, Sequence
from sqlalchemy import select, ScalarResult
from sqlalchemy.orm import Mapped, joinedload

from models import WeeklySchedule
from models import Exercise
from models.training_plan import TrainingPlan
from app.services.base import BaseService


class ScheduleService(BaseService):

    def get_schedule(self):
        pass
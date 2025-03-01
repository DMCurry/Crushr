from typing import List
from fastapi import status
from sqlalchemy import select, Sequence
from sqlalchemy.orm import Mapped
from models.performance_test import PerformanceTest
from models.user import User
from models.analytics import Analytics
from app.services.base import BaseService


class AnalyticsService(BaseService):

    def get_user_performance_tests_with_analytics(self, user_id: int) -> Sequence[PerformanceTest]:
        query = select(PerformanceTest).where(PerformanceTest.user_id == user_id)
        performance_tests = self.db.execute(query).scalars().all()
        return performance_tests

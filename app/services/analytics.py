from typing import List
from fastapi import status
from sqlalchemy import select, Sequence
from sqlalchemy.orm import Mapped
from models.performance_test import PerformanceTest
from models.user import User
from models.analytics import Analytics
from app.services.base import BaseService
from schemas.analytics_schemas import AnalyticsEntrySchema


class AnalyticsService(BaseService):

    def get_user_performance_tests_with_analytics(self, user_id: int) -> Sequence[PerformanceTest]:
        query = select(PerformanceTest).where(PerformanceTest.user_id == user_id)
        performance_tests = self.db.execute(query).scalars().all()
        return performance_tests

    def record_analytics_event(self, user_id: int, analytics_input: AnalyticsEntrySchema) -> Analytics:
        query = (select(Analytics).where(Analytics.user_id == user_id)
                 .where(Analytics.performance_test_id == analytics_input.test_id)
                 .where(Analytics.test_date == analytics_input.date))
        analytics = self.db.execute(query).scalars().one_or_none()
        if analytics is not None:
            analytics.performance_test_result = analytics_input.test_value
        else:
            analytics = Analytics(
                performance_test_id = analytics_input.test_id,
                performance_test_result = analytics_input.test_value,
                user_id = user_id,
                test_date = analytics_input.date
            )
            self.db.add(analytics)
        self.db.commit()
        return analytics
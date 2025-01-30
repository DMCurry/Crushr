from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Mapped
from models.user import User
from models.performance_test import PerformanceTest
from app.services.base import BaseService
from schemas.performance_test_schemas import PerformanceTestSchema


class PerformanceTestService(BaseService):

    def get_performance_tests(self, user_id: int) -> Mapped[List[PerformanceTest]]:
        query = select(User).where(User.id == user_id)
        user = self.db.execute(query).scalar_one_or_none()
        return user.performance_tests

    def create_performance_test(self, user_id: int, performance_test_info: PerformanceTestSchema):
        performance_test = PerformanceTest(
            test_name = performance_test_info.test_name,
            description = performance_test_info.description,
            performance_value = performance_test_info.performance_value,
            user_id = user_id
        )
        self.db.add(performance_test)
        self.db.commit()
        return performance_test

    def update_performance_test(self, user_id, performance_test_id,  performance_test_info):
        pass
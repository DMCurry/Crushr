from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Mapped
from models.user import User
from models.performance_test import PerformanceTest
from app.services.base import BaseService


class PerformanceTestService(BaseService):

    def get_performance_tests(self, user_id: int):
        pass

    def create_performance_test(self, user_id, performance_test_info):
        pass

    def update_performance_test(self, user_id, performance_test_id,  performance_test_info):
        pass
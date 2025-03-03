from typing import Optional, List, Any
from datetime import date
from pydantic import BaseModel, Field, model_validator
from schemas.performance_test_schemas import PerformanceTestSchema


class TestResultSchema(BaseModel):
    performance_test_result: float
    test_date: date

    class Config:
        from_attributes = True


class GraphSchema(PerformanceTestSchema):
    analytics: List[TestResultSchema]

    class Config:
        from_attributes = True


class UserAnalyticsSchema(BaseModel):
    data: List[GraphSchema]

    class Config:
        from_attributes = True


class AnalyticsEntrySchema(BaseModel):
    test_id: int
    test_value: float
    date: date
from pydantic import BaseModel, Field

class PerformanceTestSchema(BaseModel):
    test_name: str
    performance_value: float = Field()
    description: str = Field()

    class Config:
        from_attributes = True

class PerformanceTestUpdateSchema(PerformanceTestSchema):
    id: int
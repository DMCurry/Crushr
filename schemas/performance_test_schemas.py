from pydantic import BaseModel, Field

class PerformanceTestSchema(BaseModel):
    test_name: str
    description: str = Field()

    class Config:
        from_attributes = True

class PerformanceTestSchemaWithID(PerformanceTestSchema):
    id: int

    class Config:
        from_attributes = True
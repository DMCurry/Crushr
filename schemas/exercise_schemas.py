from typing import Optional

from pydantic import BaseModel, Field

class ExerciseSchema(BaseModel):
    exercise_name: str
    reps: int = Field(serialization_alias="exercise_reps")
    sets: int = Field(serialization_alias="exercise_sets")
    link: Optional[str] = Field(serialization_alias="exercise_link")
    description: str = Field(serialization_alias="exercise_description")

    class Config:
        from_attributes = True

class ExerciseSchemaWithID(ExerciseSchema):
    id: int

    class Config:
        from_attributes = True

from pydantic import BaseModel, EmailStr, Field


class UserCreateSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, pattern="^[a-zA-Z0-9_]+$", description="Username must be 3-50 characters and contain only alphanumeric characters and underscores.")
    email: EmailStr = Field(..., description="A valid email address.")
    password: str = Field(..., min_length=8, max_length=128, description="Password must be at least 8 characters long.")

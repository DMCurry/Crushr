from sqlalchemy import select
from models.user import User
from pydantic import EmailStr
from app.services.base import BaseService
from schemas.user_schemas import UserCreateSchema
from utilities import hash_password
from fastapi import HTTPException, status


class UserService(BaseService):

    def get_user(self, username: str) -> User:
        query = select(User).where(User.username == username)
        return self.db.execute(query).scalar_one_or_none()

    def create_user(self, user_info: UserCreateSchema) -> User:
        existing_user = self.get_user(user_info.username)
        existing_email = self.get_user_by_email(user_info.email)
        if existing_user is not None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Username already exists"
            )
        if existing_email is not None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User with email already exists"
            )
        user = User(
            username=user_info.username,
            email=user_info.email,
            hashed_password=hash_password(user_info.password)
        )
        self.db.add(user)
        self.db.commit()
        return user

    def get_user_by_email(self, email: EmailStr) -> User:
        query = select(User).where(User.email == email)
        return self.db.execute(query).scalar_one_or_none()

    def update_user(self) -> User:
        pass

    def delete_user(self):
        pass

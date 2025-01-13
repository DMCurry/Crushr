from sqlalchemy import select
from models.user import User
from app.services.base import BaseService
from schemas.user_schemas import UserCreateSchema
from utilities import hash_password


class UserService(BaseService):

    def get_user(self, username: str) -> User:
        query = select(User).where(User.username == username)
        return self.db.execute(query).scalar_one_or_none()

    def create_user(self, user_info: UserCreateSchema) -> User:
        user = User(
            username=user_info.username,
            email=user_info.email,
            hashed_password=hash_password(user_info.password)
        )
        self.db.add(user)
        self.db.commit()
        return user

    def update_user(self) -> User:
        pass

    def delete_user(self):
        pass

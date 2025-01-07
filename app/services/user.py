from sqlalchemy import select
from models.user import User
from app.services.base import BaseService

class UserService(BaseService):

    def get_user(self, username: str) -> User:
        query = select(User).where(User.username == username)
        return self.db.execute(query).scalar_one_or_none()

    def create_user(self):
        pass

    def update_user(self) -> User:
        pass

    def delete_user(self):
        pass

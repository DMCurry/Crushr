import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import select
from models.user import User
from app.services.base import BaseService


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

class LoginService(BaseService):

    def create_access_token(self, data: dict):
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    def hash_password(self, password: str) -> str:
        return PWD_CONTEXT.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return PWD_CONTEXT.verify(plain_password, hashed_password)

    def authenticate_user(self, username: str, password: str):
        stmt = select(User).where(User.username == username)
        user = self.db.execute(stmt).scalar_one_or_none()
        if user and self.verify_password(password, user.hashed_password):
            return user
        return None
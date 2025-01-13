import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from sqlalchemy import select
from models.user import User
from app.services.base import BaseService
from utilities import verify_password


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class LoginService(BaseService):

    def create_access_token(self, data: dict):
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    def authenticate_user(self, username: str, password: str):
        stmt = select(User).where(User.username == username)
        user = self.db.execute(stmt).scalar_one_or_none()
        if user and verify_password(password, user.hashed_password):
            return user
        return None
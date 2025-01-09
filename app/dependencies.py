import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.core.db import SessionLocal
from typing import Generator

# Secret and algorithm for decoding the token
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

# Define OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def decode_and_verify_token(token: str):
    """
    Decodes and verifies the JWT token.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        raise ValueError(f"Invalid token: {str(e)}")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Dependency to retrieve the current user based on the JWT.
    """
    try:
        payload = decode_and_verify_token(token)
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: user ID missing",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return {"id": user_id}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_db() -> Generator[Session, None, None]:
    """
    Provides a SQLAlchemy session.
    Ensures db is closed after use.
    """
    db = SessionLocal()
    try:
        yield db # Provide the session to the request
    finally:
        db.close() # Close the session after the request
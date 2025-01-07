from sqlalchemy.orm import Session
from app.core.db import SessionLocal
from typing import Generator


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
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.services.login import LoginService
from app.dependencies import get_db

router = APIRouter(prefix="/login", tags=["login"])


def get_login_service(db: Session = Depends(get_db)):
    return LoginService(db=db)


@router.post("")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), login_service: LoginService = Depends(get_login_service)
):
    """
    Logs a user in by validating their username and password.
    Sets JWT token in cookies on successful login.
    """
    user = login_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Generate a JWT access token
    access_token = login_service.create_access_token(
        data={"sub": str(user.id)}
    )
    response = JSONResponse(content={"message": "Login successful"})
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite='Lax',
        secure=False,  # Set to True in production for HTTPS
        max_age=3600,  # Token expiration in seconds
    )
    return response

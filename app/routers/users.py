from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.user import UserService
from app.dependencies import get_db
from schemas.user_schemas import UserCreateSchema


router = APIRouter(prefix="/users", tags=["users"])

def get_user_service(db: Session = Depends(get_db)):
    return UserService(db=db)

# IF USING THIS MAKE SURE TO ADD A DEPENDENCY INJECTION TO VALIDATE USER AUTH
# @router.get("")
# async def get_user(username: str,  user_service: UserService = Depends(get_user_service)):
#     user = user_service.get_user(username)
#     return user


@router.post("")
async def create_user(user_info: UserCreateSchema, user_service: UserService = Depends(get_user_service)):
    new_user = user_service.create_user(user_info)
    return new_user
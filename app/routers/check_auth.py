from fastapi import APIRouter, Depends
from app.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("")
async def auth(
        current_user: dict = Depends(get_current_user)):
    user_id = current_user.get("id")
    return {}
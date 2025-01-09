from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from app.services.exercise import ExerciseService
from app.dependencies import get_current_user


router = APIRouter(prefix="/exercises", tags=["exercises"])

mock_exercises_db = {
    "usr12345": [
        {"name": "no hangs", "description": "hang without full bodyweight", "reps": 3, "duration": "20s"},
        {"name": "lock off campus", "description": "lock off campus rungs jugs", "reps": 2, "duration": None}
    ]
}

@router.get("")
async def get_exercises(current_user: dict = Depends(get_current_user)):
    user_id = current_user.get("id")
    # TODO: Need to connect exercises to User model so list of exercises can be standalone to user
    return {}

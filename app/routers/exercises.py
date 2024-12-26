from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query

router = APIRouter(prefix="/exercises", tags=["exercises"])

mock_exercises_db = {
    "usr12345": [
        {"name": "no hangs", "description": "hang without full bodyweight", "reps": 3, "duration": "20s"},
        {"name": "lock off campus", "description": "lock off campus rungs jugs", "reps": 2, "duration": None}
    ]
}

@router.get("")
async def get_exercises(user_id = Query(None)):
    exercises = mock_exercises_db.get(user_id, {})
    return exercises
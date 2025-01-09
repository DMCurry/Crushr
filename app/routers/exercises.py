from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from app.services.exercise import ExerciseService
from app.dependencies import get_current_user
from app.dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/exercises", tags=["exercises"])


def get_exercise_service(db: Session = Depends(get_db)):
    return ExerciseService(db=db)


@router.get("")
async def get_exercises(
        current_user: dict = Depends(get_current_user),
        exercise_service: ExerciseService = Depends(get_exercise_service)):
    user_id = current_user.get("id")
    exercises = exercise_service.get_exercises(user_id)
    return exercises

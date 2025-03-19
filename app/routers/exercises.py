from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from app.services.exercise import ExerciseService
from app.dependencies import get_current_user
from app.dependencies import get_db
from sqlalchemy.orm import Session
from schemas.exercise_schemas import ExerciseSchema, ExerciseSchemaWithID


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


@router.get("/training-plans")
async def get_exercise_training_plans(
        exercise_id: int,
        current_user: dict = Depends(get_current_user),
        exercise_service: ExerciseService = Depends(get_exercise_service)):
    user_id = current_user.get("id")
    training_plans = exercise_service.get_exercise_training_plans(user_id, exercise_id)
    return training_plans


@router.post("")
async def create_exercise(
        exercise_input: ExerciseSchema,
        current_user: dict = Depends(get_current_user),
        exercise_service: ExerciseService = Depends(get_exercise_service)) -> ExerciseSchema:
    user_id = current_user.get("id")
    exercise = exercise_service.create_exercise(user_id, exercise_input)
    return ExerciseSchema.model_validate(exercise)


@router.put("")
async def update_exercise(
        exercise_input: ExerciseSchemaWithID,
        current_user: dict = Depends(get_current_user),
        exercise_service: ExerciseService = Depends(get_exercise_service)) -> ExerciseSchema:
    user_id = current_user.get("id")
    exercise = exercise_service.update_exercise(user_id, exercise_input.id, exercise_input)
    return ExerciseSchema.model_validate(exercise)


@router.delete("")
async def delete_exercise(
        exercise_id: int,
        current_user: dict = Depends(get_current_user),
        exercise_service: ExerciseService = Depends(get_exercise_service)):
    user_id = current_user.get("id")
    exercise_service.delete_exercise(user_id, exercise_id)
    return

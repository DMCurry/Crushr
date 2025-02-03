from fastapi import APIRouter, Depends
from app.services.training_plan import TrainingPlanService
from app.dependencies import get_current_user
from app.dependencies import get_db
from sqlalchemy.orm import Session
from schemas.training_plan_schemas import AddItemsInputSchema, CreatePlanInputSchema

router = APIRouter(prefix="/training-plan", tags=["training_plan"])


def get_training_plan_service(db: Session = Depends(get_db)):
    return TrainingPlanService(db=db)


@router.get("")
async def get_training_plans(
        current_user: dict = Depends(get_current_user),
        training_plan_service: TrainingPlanService = Depends(get_training_plan_service)):
    user_id = current_user.get("id")
    training_plans = training_plan_service.get_plans(user_id)
    return training_plans


@router.post("")
async def create_training_plan(
        new_plan_input: CreatePlanInputSchema,
        current_user: dict = Depends(get_current_user),
        training_plan_service: TrainingPlanService = Depends(get_training_plan_service)):
    user_id = current_user.get("id")
    training_plan = training_plan_service.create_plan(user_id, new_plan_input.plan_name)
    return training_plan


@router.post("/add-exercises")
async def add_exercises(
        add_exercises_input: AddItemsInputSchema,
        current_user: dict = Depends(get_current_user),
        training_plan_service: TrainingPlanService = Depends(get_training_plan_service)):
    user_id = current_user.get("id")
    training_plan_service.add_exercises_to_plan(user_id, add_exercises_input.plan_id, add_exercises_input.item_ids)
    return {}


@router.post("/add-performance-tests")
async def add_performance_tests(
        add_performance_test_input: AddItemsInputSchema,
        current_user: dict = Depends(get_current_user),
        training_plan_service: TrainingPlanService = Depends(get_training_plan_service)):
    user_id = current_user.get("id")
    training_plan_service.add_performance_tests_to_plan(
        user_id, add_performance_test_input.plan_id, add_performance_test_input.item_ids
    )
    return {}
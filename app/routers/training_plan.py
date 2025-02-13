from fastapi import APIRouter, Depends
from app.services.training_plan import TrainingPlanService
from app.dependencies import get_current_user
from app.dependencies import get_db
from sqlalchemy.orm import Session
from schemas.training_plan_schemas import (
    AddItemsInputSchema, CreatePlanInputSchema, UpdatePlanInputSchema, RemoveItemSchema, TrainingPlanOutputSchema
)

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
    return TrainingPlanOutputSchema.model_validate(training_plan)


@router.put("")
async def update_training_plan(
        plan_update_input: UpdatePlanInputSchema,
        current_user: dict = Depends(get_current_user),
        training_plan_service: TrainingPlanService = Depends(get_training_plan_service)):
    user_id = current_user.get("id")
    training_plan = training_plan_service.update_plan(user_id, plan_update_input.plan_id, plan_update_input.plan_name)
    return TrainingPlanOutputSchema.model_validate(training_plan)


@router.post("/add-exercises")
async def add_exercises(
        add_exercises_input: AddItemsInputSchema,
        current_user: dict = Depends(get_current_user),
        training_plan_service: TrainingPlanService = Depends(get_training_plan_service)):
    user_id = current_user.get("id")
    plan = training_plan_service.add_exercises_to_plan(user_id, add_exercises_input.plan_id, add_exercises_input.item_ids)
    return TrainingPlanOutputSchema.model_validate(plan)


@router.post("/add-performance-tests")
async def add_performance_tests(
        add_performance_test_input: AddItemsInputSchema,
        current_user: dict = Depends(get_current_user),
        training_plan_service: TrainingPlanService = Depends(get_training_plan_service)):
    user_id = current_user.get("id")
    plan = training_plan_service.add_performance_tests_to_plan(
        user_id, add_performance_test_input.plan_id, add_performance_test_input.item_ids
    )
    return TrainingPlanOutputSchema.model_validate(plan)


@router.put("/remove-item")
async def remove_item(
        item: RemoveItemSchema,
        current_user: dict = Depends(get_current_user),
        training_plan_service: TrainingPlanService = Depends(get_training_plan_service)):
    user_id = current_user.get("id")
    plan = training_plan_service.remove_item(user_id, item)
    return TrainingPlanOutputSchema.model_validate(plan)
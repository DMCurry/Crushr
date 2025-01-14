from fastapi import APIRouter, Depends
from app.services.training_plan import TrainingPlanService
from app.dependencies import get_current_user
from app.dependencies import get_db
from sqlalchemy.orm import Session


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
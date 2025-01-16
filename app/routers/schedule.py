from fastapi import APIRouter, Depends
from app.services.schedule import ScheduleService
from app.dependencies import get_current_user
from app.dependencies import get_db
from sqlalchemy.orm import Session
from schemas.training_plan_schemas import AddExercisesInputSchema


router = APIRouter(prefix="/schedule", tags=["schedule"])


def get_schedule_service(db: Session = Depends(get_db)):
    return ScheduleService(db=db)


@router.get("")
async def get_training_plans(
        current_user: dict = Depends(get_current_user),
        schedule_service: ScheduleService = Depends(get_schedule_service())):
    user_id = current_user.get("id")
    schedule = schedule_service.get_schedule(user_id)
    return schedule
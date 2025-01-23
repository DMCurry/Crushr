from fastapi import APIRouter, Depends
from app.services.schedule import ScheduleService
from app.dependencies import get_current_user
from app.dependencies import get_db
from sqlalchemy.orm import Session
from schemas.schedule_schemas import WeeklyScheduleSchema


router = APIRouter(prefix="/schedule", tags=["schedule"])


def get_schedule_service(db: Session = Depends(get_db)):
    return ScheduleService(db=db)


@router.get("")
async def get_schedule(
        current_user: dict = Depends(get_current_user),
        schedule_service: ScheduleService = Depends(get_schedule_service)) -> WeeklyScheduleSchema:
    user_id = current_user.get("id")
    schedule = schedule_service.get_schedule(user_id)
    return WeeklyScheduleSchema(data=schedule)


@router.put("")
async def update_schedule(
        schedule_data: WeeklyScheduleSchema,
        current_user: dict = Depends(get_current_user),
        schedule_service: ScheduleService = Depends(get_schedule_service)) -> WeeklyScheduleSchema:
    user_id = current_user.get("id")
    schedule = schedule_service.update_schedule(user_id, schedule_data.data)
    return WeeklyScheduleSchema(data=schedule)
from fastapi import APIRouter, Depends
from app.services.schedule import ScheduleService
from app.dependencies import get_current_user
from app.dependencies import get_db
from sqlalchemy.orm import Session
from schemas.schedule_schemas import WeeklyScheduleOutputSchema


router = APIRouter(prefix="/schedule", tags=["schedule"])


def get_schedule_service(db: Session = Depends(get_db)):
    return ScheduleService(db=db)


@router.get("")
async def get_schedule(
        current_user: dict = Depends(get_current_user),
        schedule_service: ScheduleService = Depends(get_schedule_service)) -> WeeklyScheduleOutputSchema:
    user_id = current_user.get("id")
    schedule = schedule_service.get_schedule(user_id)
    return WeeklyScheduleOutputSchema(data=schedule)

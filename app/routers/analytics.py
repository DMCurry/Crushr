from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app.services.analytics import AnalyticsService
from schemas.analytics_schemas import UserAnalyticsSchema


router = APIRouter(prefix="/analytics", tags=["analytics"])

def get_analytics_service(db: Session = Depends(get_db)):
    return AnalyticsService(db=db)


@router.get("")
async def get_schedule(
        current_user: dict = Depends(get_current_user),
        analytics_service: AnalyticsService = Depends(get_analytics_service)) -> UserAnalyticsSchema:
    user_id = current_user.get("id")
    user_analytics = analytics_service.get_user_performance_tests_with_analytics(user_id)
    return UserAnalyticsSchema(data=user_analytics)

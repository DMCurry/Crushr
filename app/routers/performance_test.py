from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from app.services.performance_test import PerformanceTestService
from app.dependencies import get_current_user
from app.dependencies import get_db
from sqlalchemy.orm import Session
from schemas.performance_test_schemas import PerformanceTestSchema, PerformanceTestUpdateSchema


router = APIRouter(prefix="/performance-tests", tags=["performance_tests"])


def get_performance_test_service(db: Session = Depends(get_db)):
    return PerformanceTestService(db=db)


@router.get("")
async def get_performance_tests(
        current_user: dict = Depends(get_current_user),
        performance_test_service: PerformanceTestService = Depends(get_performance_test_service)):
    user_id = current_user.get("id")
    performance_tests = performance_test_service.get_performance_tests(user_id)
    return performance_tests

@router.post("")
async def create_performance_test(
        performance_test_input: PerformanceTestSchema,
        current_user: dict = Depends(get_current_user),
        performance_test_service: PerformanceTestService = Depends(get_performance_test_service)) -> PerformanceTestSchema:
    user_id = current_user.get("id")
    performance_test = performance_test_service.create_performance_test(user_id, performance_test_input)
    return PerformanceTestSchema.model_validate(performance_test)


@router.put("")
async def update_performance_test(
        performance_test_input: PerformanceTestUpdateSchema,
        current_user: dict = Depends(get_current_user),
        performance_test_service: PerformanceTestService = Depends(get_performance_test_service)) -> PerformanceTestSchema:
    user_id = current_user.get("id")
    performance_test = performance_test_service.update_performance_test(user_id, performance_test_input.id, performance_test_input)
    return PerformanceTestSchema.model_validate(performance_test)


@router.delete("")
async def delete_performance_test(
        test_id: int,
        current_user: dict = Depends(get_current_user),
        performance_test_service: PerformanceTestService = Depends(get_performance_test_service)):
    user_id = current_user.get("id")
    performance_test_service.delete_performance_test(user_id, test_id)
    return
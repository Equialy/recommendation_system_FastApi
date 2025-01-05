from fastapi import APIRouter, Depends
from typing import Annotated

from src.api.dependencies import   recommendations_service
from src.services.recommendations import RecommendationsService
router = APIRouter(
    prefix="/recommendations",
    tags=["Рекомендации"],
    responses={404: {"description": "Not found"}},
)


@router.post("/generate_recommendations", summary="Генерация рекомендаций")
async def generate_recommendations(user_id: int,  get_generate_recommendations_service: Annotated[RecommendationsService, Depends(recommendations_service)] ):
    result = await get_generate_recommendations_service.generate_recommendations(user_id)
    return {"result": result}

@router.get("", summary="Просмотреть рекомендацию")
async def get_recommendations(user_id: int, get_recommendations_service: Annotated[RecommendationsService, Depends(recommendations_service)]):
    result = await get_recommendations_service.recommendations_repo.get_recommendations(user_id)
    return {"result": result}
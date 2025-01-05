from fastapi import APIRouter, Depends
from typing import Annotated

from src.api.dependencies import purchases_service
from src.schemas.users_purchases import UsersPurchasesSchemaAdd, UsersPurchasesSchema
from src.services.purchases import PurchasesService


router = APIRouter(
    prefix="/purchases",
    tags=["Покупки"],
    responses={404: {"description": "Not found"}},
)

@router.get("", summary="Просмотр покупок пользователя")
async def get_purchases(user_id: int, get_purchase_service: Annotated[PurchasesService, Depends(purchases_service)]) -> list[UsersPurchasesSchema]:
    purchses_item = await get_purchase_service.get_user_purchase(user_id)
    return purchses_item


@router.post("", summary="Добавление покупки")
async def add_purchases(purchases_data: UsersPurchasesSchemaAdd , get_purchase_service: Annotated[PurchasesService, Depends(purchases_service)]) :
    result = await get_purchase_service.add_purchases(purchases_data)
    return {"status": "purchases added"}





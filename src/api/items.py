from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import items_service
from src.schemas.items import ItemsSchemaAdd, ItemsSchema
from src.services.items import ItemsService

router = APIRouter(
    tags=["Товары"],
    prefix="/items"
)


@router.post("", summary="Добавление товара")
async def create_item(item_data: ItemsSchemaAdd, get_service_item: Annotated[ItemsService, Depends(items_service)]):
    item_add = await get_service_item.add_items(item_data)
    return {"add_item": item_add}


@router.get("", summary="Просмотр всех товаров")
async def get_items_all(get_service_item: Annotated[ItemsService, Depends(items_service)]) -> list[ItemsSchema]:
    items_get = await get_service_item.get_all_items()
    return items_get

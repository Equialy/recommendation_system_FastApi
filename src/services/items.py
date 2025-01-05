from fastapi import HTTPException

from src.models import Items
from src.repositories.items import ItemsRepositories
from src.schemas.items import ItemsSchemaAdd


class ItemsService:

    def __init__(self, items_repo: ItemsRepositories):
        self.items_repo: ItemsRepositories = items_repo


    async def add_items(self, items_data: ItemsSchemaAdd) -> Items:
        items_dict = items_data.model_dump()
        try:
            result = await self.items_repo.add_one(items_dict)
        except:
            raise HTTPException(status_code=400, detail="Ошибка запроса")
        return result

    async def get_all_items(self) :
        return await self.items_repo.find_all()

from unicodedata import category

from src.repositories.purchases import PurchasesRepository
from src.schemas.users_purchases import UsersPurchasesSchemaAdd, UsersPurchasesSchema


class PurchasesService:

    def __init__(self, purchases_repo: PurchasesRepository):
        self.purchases_repo: PurchasesRepository = purchases_repo

    async def add_purchases(self, purchases_data: UsersPurchasesSchemaAdd):
        result = {}
        for item in purchases_data.cart:
            purchases_dict = item.model_dump()
            print(purchases_dict)
            result = await self.purchases_repo.add_one(user_id=purchases_data.user_id, item_id=item.item_id, category=item.category)
        return result

    async def get_user_purchase(self, user_id: int):
        result = await self.purchases_repo.get_one_by_user_id(user_id)
        return result
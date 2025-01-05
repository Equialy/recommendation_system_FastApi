from sqlalchemy import select

from src.models.users_purchases import UserPurchases
from src.utils.repository import SQLAlchemyRepository


class PurchasesRepository(SQLAlchemyRepository):

    model = UserPurchases

    async def add_one(self, **kwargs):
        purchase = self.model(**kwargs)
        self.session.add(purchase)
        await self.session.flush()
        print(f"Возврат {purchase}")
        return purchase.to_read_model()

    async def get_all_purchases(self) :
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        returning = [row[0].to_read_model() for row in result.all()]
        print(returning)
        return returning

    async def get_one_by_user_id(self, user_id) :
        stmt = select(self.model).where(self.model.user_id == user_id)
        result =  await self.session.execute(stmt)
        return result.scalars().all()



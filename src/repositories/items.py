from sqlalchemy import select

from src.models.Items import Items
from src.utils.repository import SQLAlchemyRepository


class ItemsRepositories(SQLAlchemyRepository):
    model = Items

    async def add_one(self, data):
        item_model = self.model(**data)
        self.session.add(item_model)
        await self.session.flush()
        return item_model

    async def find_all(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return [row[0].to_read_model() for row in result.all()]
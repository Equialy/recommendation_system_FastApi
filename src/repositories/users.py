from sqlalchemy import select

from src.models.users import Users
from src.utils.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):

    model = Users

    async def add_one(self, data):
        user = self.model(**data)
        self.session.add(user)
        await self.session.flush()

        return user

    async def find_all(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return [row[0].to_read_model() for row in result.all()]


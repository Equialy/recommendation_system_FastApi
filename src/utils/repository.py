from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    def __init__(self, session):
        raise NotImplementedError

    @abstractmethod
    async def add_one(self, data: dict):
        return NotImplementedError

    @abstractmethod
    async def get_one_by_id(self, id):
        return NotImplementedError

    @abstractmethod
    async def find_all(self):
        return NotImplementedError

    @abstractmethod
    async def delete_one(self, data):
        return NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, **kwargs):
        pass

    async def get_one_by_id(self, id):
        pass

    async def find_all(self):
        pass

    async def delete_one(self, data):
        pass
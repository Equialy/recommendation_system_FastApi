from src.models.users import Users
from src.repositories.users import UsersRepository
from src.schemas.users import UsersSchemaAdd


class UsersService:

    def __init__(self, users_repo: UsersRepository):
        self.users_repo: UsersRepository = users_repo

    async def create_user(self, user_data: UsersSchemaAdd) -> Users:
        user_dict = user_data.model_dump()
        result = await self.users_repo.add_one(user_dict)
        return result

    async def get_all_users(self) -> Users:
        result = await self.users_repo.find_all()
        return result
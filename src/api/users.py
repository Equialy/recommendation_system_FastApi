from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import users_service
from src.schemas.users import UsersSchemaAdd
from src.services.users import UsersService

router = APIRouter(
    tags=["Пользователи"],
    prefix="/users"
)

@router.post("", summary="Добавление пользователя")
async def create_users(username: UsersSchemaAdd, get_users_service: Annotated[UsersService, Depends(users_service)]):
    user_add = await get_users_service.create_user(user_data=username)
    return {"user": user_add}

@router.get("", summary="Просмотр всех пользователей")
async def get_users(get_users_service: Annotated[UsersService, Depends(users_service)]):
    users_get = await get_users_service.get_all_users()
    return {"all_users": users_get}
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_async_session
from src.repositories.items import ItemsRepositories
from src.repositories.purchases import PurchasesRepository
from src.repositories.recommendations import RecommendationsRepository
from src.repositories.users import UsersRepository
from src.services.items import ItemsService
from src.services.purchases import PurchasesService
from src.services.recommendations import RecommendationsService
from src.services.users import UsersService




def users_service(session: AsyncSession = Depends(get_async_session)):
    return UsersService(UsersRepository(session))

def items_service(session: AsyncSession = Depends(get_async_session)):
    return ItemsService(ItemsRepositories(session))

def recommendations_repository(session: AsyncSession = Depends(get_async_session)):
    return RecommendationsRepository(session)

def purchases_repository(session: AsyncSession = Depends(get_async_session)):
    return PurchasesRepository(session)
# Фабрики для сервисов

def purchases_service(purchases_repo: PurchasesRepository = Depends(purchases_repository)):
    return PurchasesService(purchases_repo)

def recommendations_service(
    recommendations_repo: RecommendationsRepository = Depends(recommendations_repository),
    purchases_repo: PurchasesRepository = Depends(purchases_repository),
):
    return RecommendationsService(recommendations_repo, purchases_repo)


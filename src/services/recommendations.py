from src.models.users_purchases import UserPurchases
from src.repositories.purchases import PurchasesRepository
from src.repositories.recommendations import RecommendationsRepository
import pandas as pd
import numpy as np

class RecommendationsService:

    def __init__(self, recommendations_repo: RecommendationsRepository, purchases_repo: PurchasesRepository):
        self.recommendations_repo: RecommendationsRepository = recommendations_repo
        self.purchases_repo: PurchasesRepository = purchases_repo


    async def build_cooccurrence_matrix(self, purchases: list[UserPurchases]) -> pd.DataFrame:
        items = {}
        for purchase in purchases:
            if purchase.item_id not in items:
                items[purchase.item_id] = len(items)
        print(f"Словарь items {items}")
        matrix = np.zeros((len(items), len(items)))
        print(f"Матрица {matrix}")

        # Группируем покупки по пользователям
        user_purchases = {}
        for purchase in purchases:
            if purchase.user_id not in user_purchases:
                user_purchases[purchase.user_id] = []
            user_purchases[purchase.user_id].append(purchase.item_id)
        print(f"Группируем покупки по пользователям {user_purchases}")

        # Заполняем матрицу
        for user_items in user_purchases.values():
            for i in range(len(user_items)):
                for j in range(i + 1, len(user_items)):
                    idx1, idx2 = items[user_items[i]], items[user_items[j]]
                    matrix[idx1][idx2] += 1
                    matrix[idx2][idx1] += 1
        print(f"Заполняем матрицу {matrix}")
        print(f"""Дата фрейм 
{pd.DataFrame(matrix, index=list(items.keys()), columns=list(items.keys()))}""")

        return pd.DataFrame(matrix, index=list(items.keys()), columns=list(items.keys()))

    async def _get_most_popular_items(self,user_items: set[int], all_purchases: list[UserPurchases]) -> int | None:
        """
            Выбирает самый популярный товар из тех, которые пользователь еще не покупал.

            :param user_items: Товары, которые уже куплены пользователем.
            :param all_purchases: Все покупки всех пользователей.
            :return: ID самого популярного товара или None, если рекомендации отсутствуют.
            """
        # Словарь для подсчета количества покупок каждого товара
        item_popularity = {}

        for purchase in all_purchases:
            if purchase.item_id not in user_items:  # Только товары, которые пользователь еще не покупал
                item_popularity[purchase.item_id] = item_popularity.get(purchase.item_id, 0) + 1

        # Если нет подходящих товаров, возвращаем None
        if not item_popularity:
            return None

        # Найти самый популярный товар
        most_popular_item = max(item_popularity, key=item_popularity.get)
        return most_popular_item

    async def generate_recommendations(self, user_id: int) -> None:
            # Получаем историю покупок пользователя
            user_purchases_all = await self.purchases_repo.get_all_purchases()

            user_purchases = await self.purchases_repo.get_one_by_user_id(user_id)
            user_items = {purchase.item_id for purchase in user_purchases}
            print(f"Покупки пользователя {user_items}")

            # Построение матрицы
            cooccurrence_matrix = await self.build_cooccurrence_matrix(user_purchases_all)
            print(f"Индексы матрицы {cooccurrence_matrix.index}")

            recommendations = set()

            for item_id in user_items:
                if item_id in cooccurrence_matrix.index:
                    similar_items = cooccurrence_matrix[item_id].sort_values(ascending=False)
                    for similar_item_id in similar_items.index:
                        if similar_item_id not in user_items:
                            recommendations.add(similar_item_id)
            print(f"Рекомендации {recommendations}")

            if not recommendations:
                recommended_item_id = await self._get_most_popular_items(user_items, user_purchases_all)
            else:
                # Выбираем самый популярный товар из рекомендаций
                recommended_item_id = await self._get_most_popular_items(recommendations, user_purchases_all)

            if recommended_item_id:
                await self.recommendations_repo.save_recommendations(
                    user_id=user_id,
                    item_id=recommended_item_id
                )
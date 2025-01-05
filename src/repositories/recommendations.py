from sqlalchemy import select

from src.models.Items import Items
from src.models.recommendations import Recommendations
from src.models.users_purchases import UserPurchases
from src.utils.repository import SQLAlchemyRepository


class RecommendationsRepository(SQLAlchemyRepository):

    model = Recommendations

    async def get_user_purchses(self, user_id: int) -> list[UserPurchases]:
        stmt = select(UserPurchases).where(UserPurchases.user_id == user_id)
        result = await self.session.execute(stmt)
        return [row[0].to_read_model() for row in result.all()]

    async def get_all_purchases(self) -> list[UserPurchases]:
        stmt = select(UserPurchases)
        result = await self.session.execute(stmt)
        return [row[0].to_read_model() for row in result.all()]


    async def save_recommendations(self, user_id, item_id):
        recommendations = self.model(user_id=user_id, item_id=item_id)
        self.session.add(recommendations)
        await self.session.flush()
        print(f"Сохранение рекомендации {recommendations}")
        return recommendations

    async def get_recommendations(self, user_id: int) -> list[dict]:
        query = select(self.model, Items).join(Items).where(
            self.model.user_id == user_id
        )
        result = await self.session.execute(query)
        recommendations = []
        for rec, item in result:
            recommendations.append({
                "item_id": item.id,
                "category": item.category
            })
        return recommendations


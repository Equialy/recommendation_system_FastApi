from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.database import Base
from src.schemas.recommendations import RecommendationsSchema


class Recommendations(Base):
    __tablename__ = 'recommendations'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    item_id: Mapped[int] = mapped_column(ForeignKey('items.id'))



    def to_read_model(self) -> RecommendationsSchema:
        return RecommendationsSchema(
            id=self.id,
            user_id=self.user_id,
            item_id=self.item_id

        )

from datetime import date, datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.db.database import Base
from src.schemas.users_purchases import UsersPurchasesSchema


class UserPurchases(Base):
    __tablename__ = 'user_purchases'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    item_id: Mapped[int] = mapped_column(ForeignKey('items.id'))
    category: Mapped[str] = mapped_column(nullable=False)
    purchase_date: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)


    def to_read_model(self) -> UsersPurchasesSchema:
        return UsersPurchasesSchema(
            id=self.id,
            user_id=self.user_id,
            item_id=self.item_id,
            category=self.category,
            purchase_date=self.purchase_date
        )



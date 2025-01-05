from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.db.database import Base
from src.schemas.items import ItemsSchema


class Items(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(nullable=False)

    def to_read_model(self) -> ItemsSchema:
        return ItemsSchema(
            id=self.id,
            name=self.name,
            category=self.category,

        )
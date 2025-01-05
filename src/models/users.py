from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.database import Base
from src.schemas.users import UsersSchema


class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)



    def to_read_model(self) -> UsersSchema:
        return UsersSchema(
            id=self.id,
            username=self.username,

        )
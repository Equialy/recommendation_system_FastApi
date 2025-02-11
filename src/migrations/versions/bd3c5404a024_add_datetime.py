"""add datetime

Revision ID: bd3c5404a024
Revises: 50bc7d8f937a
Create Date: 2024-12-22 20:13:24.460552

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd3c5404a024'
down_revision: Union[str, None] = '50bc7d8f937a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_users_recommendations', 'users', type_='foreignkey')
    op.drop_constraint('fk_users_purchases', 'users', type_='foreignkey')
    op.drop_column('users', 'purchases')
    op.drop_column('users', 'recommendations')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('recommendations', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('purchases', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('fk_users_purchases', 'users', 'user_purchases', ['purchases'], ['id'])
    op.create_foreign_key('fk_users_recommendations', 'users', 'recommendations', ['recommendations'], ['id'])
    # ### end Alembic commands ###

"""Init

Revision ID: db7285025046
Revises: 
Create Date: 2024-12-22 19:49:20.470687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db7285025046'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Создание таблиц без внешних ключей
    op.create_table(
        'items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('category', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'user_purchases',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('item_id', sa.Integer(), nullable=False),
        sa.Column('category', sa.String(), nullable=False),
        sa.Column('purchase_date', sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'recommendations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('item_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('purchases', sa.Integer(), nullable=True),  # Временно nullable
        sa.Column('recommendations', sa.Integer(), nullable=True),  # Временно nullable
        sa.PrimaryKeyConstraint('id')
    )

    # Добавление внешних ключей после создания всех таблиц
    op.create_foreign_key(
        'fk_user_purchases_user_id', 'user_purchases', 'users',
        ['user_id'], ['id']
    )
    op.create_foreign_key(
        'fk_user_purchases_item_id', 'user_purchases', 'items',
        ['item_id'], ['id']
    )
    op.create_foreign_key(
        'fk_recommendations_user_id', 'recommendations', 'users',
        ['user_id'], ['id']
    )
    op.create_foreign_key(
        'fk_recommendations_item_id', 'recommendations', 'items',
        ['item_id'], ['id']
    )
    op.create_foreign_key(
        'fk_users_purchases', 'users', 'user_purchases',
        ['purchases'], ['id']
    )
    op.create_foreign_key(
        'fk_users_recommendations', 'users', 'recommendations',
        ['recommendations'], ['id']
    )


def downgrade() -> None:
    # Удаление внешних ключей перед удалением таблиц
    op.drop_constraint('fk_users_recommendations', 'users', type_='foreignkey')
    op.drop_constraint('fk_users_purchases', 'users', type_='foreignkey')
    op.drop_constraint('fk_recommendations_item_id', 'recommendations', type_='foreignkey')
    op.drop_constraint('fk_recommendations_user_id', 'recommendations', type_='foreignkey')
    op.drop_constraint('fk_user_purchases_item_id', 'user_purchases', type_='foreignkey')
    op.drop_constraint('fk_user_purchases_user_id', 'user_purchases', type_='foreignkey')
    op.drop_table('users')
    op.drop_table('recommendations')
    op.drop_table('user_purchases')
    op.drop_table('items')
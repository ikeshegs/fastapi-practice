"""add content column to posts table

Revision ID: 014a96fb1f16
Revises: 1da16ceff934
Create Date: 2024-09-30 18:47:01.017038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '014a96fb1f16'
down_revision: Union[str, None] = '1da16ceff934'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

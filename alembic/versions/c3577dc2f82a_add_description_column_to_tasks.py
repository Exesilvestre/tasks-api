"""Add description column to tasks

Revision ID: c3577dc2f82a
Revises: 2afa3542136b
Create Date: 2025-06-22 13:01:56.990688

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3577dc2f82a'
down_revision: Union[str, Sequence[str], None] = '2afa3542136b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('tasks', sa.Column('description', sa.String(length=255), nullable=True))


def downgrade():
    op.drop_column('tasks', 'description')

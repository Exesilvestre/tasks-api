"""Create taskpriority enum type

Revision ID: dd0b5552d55d
Revises: 2658014b4781
Create Date: 2025-06-22 12:58:40.892715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd0b5552d55d'
down_revision: Union[str, Sequence[str], None] = '2658014b4781'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


taskpriority = sa.Enum('low', 'medium', 'high', name='taskpriority')


def upgrade():

    op.alter_column('tasks', 'priority',
        existing_type=sa.Enum('low', 'medium', 'high', name='priority'),
        type_=sa.Enum('low', 'medium', 'high', name='taskpriority'),
        existing_nullable=False
    )

def downgrade():
    op.alter_column('tasks', 'priority',
        existing_type=sa.Enum('low', 'medium', 'high', name='taskpriority'),
        type_=sa.Enum('low', 'medium', 'high', name='priority'),
        existing_nullable=False
    )

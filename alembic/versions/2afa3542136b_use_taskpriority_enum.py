""" use taskpriority enum

Revision ID: 2afa3542136b
Revises: dd0b5552d55d
Create Date: 2025-06-22 13:01:03.510203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2afa3542136b'
down_revision: Union[str, Sequence[str], None] = 'dd0b5552d55d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

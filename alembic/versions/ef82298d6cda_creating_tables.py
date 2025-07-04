"""creating tables

Revision ID: ef82298d6cda
Revises:
Create Date: 2025-06-22 16:22:46.921389

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ef82298d6cda"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "task_lists",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=80), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_task_lists_id"), "task_lists", ["id"], unique=False)
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=80), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column(
            "status",
            sa.Enum("pending", "in_progress", "done", name="taskstatus"),
            nullable=False,
        ),
        sa.Column(
            "priority",
            sa.Enum("low", "medium", "high", name="taskpriority"),
            nullable=False,
        ),
        sa.Column("percentage_finalized", sa.Float(), nullable=False),
        sa.Column("task_list_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["task_list_id"],
            ["task_lists.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_tasks_id"), "tasks", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_tasks_id"), table_name="tasks")
    op.drop_table("tasks")
    op.drop_index(op.f("ix_task_lists_id"), table_name="task_lists")
    op.drop_table("task_lists")
    # ### end Alembic commands ###

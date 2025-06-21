import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Float, ForeignKey, Integer, String, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.status import TaskStatus
from app.core.priority import TaskPriority
from app.infrastructure.db.base import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=80), nullable=False)
    status: Mapped[TaskStatus] = mapped_column(SQLEnum(TaskStatus), default=TaskStatus.pending, nullable=False)
    priority: Mapped[TaskPriority] = mapped_column(SQLEnum(TaskPriority), default=TaskPriority.medium, nullable=False)
    percentage_finalized: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    task_list_id: Mapped[int] = mapped_column(ForeignKey("task_lists.id"), nullable=False)
    task_list: Mapped["TaskListModel"] = relationship("TaskListModel", back_populates="tasks")  # type: ignore

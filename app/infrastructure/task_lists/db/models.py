import enum
from typing import Optional, TYPE_CHECKING
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.infrastructure.db.base import Base
from app.infrastructure.tasks.db.models import TaskModel


class TaskListModel(Base):
    __tablename__ = "task_lists"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=80), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(
        String(length=255), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    tasks: Mapped[list["TaskModel"]] = relationship(
        "TaskModel",
        back_populates="task_list",
        cascade="all, delete-orphan",
        lazy="select",
    )

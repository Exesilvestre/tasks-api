from typing import Optional
from pydantic import BaseModel
from app.domain.core.priority import TaskPriority
from app.infrastructure.tasks.db.models import TaskStatus


class TaskEntity(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending
    priority: TaskPriority = TaskPriority.medium
    percentage_finalized: float = 0.0
    task_list_id: int

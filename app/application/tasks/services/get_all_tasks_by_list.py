from typing import Optional
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException
from app.application.tasks.utils import validate_priority, validate_status
from app.application.tasks.exceptions.excepcions import (
    InvalidPriorityException,
    InvalidStatusException,
)
from app.domain.task_lists.interface import TaskListInterface
from app.domain.tasks.entities import TaskEntity
from app.domain.tasks.interface import TaskInterface
from app.domain.core.priority import TaskPriority
from app.infrastructure.tasks.db.models import TaskStatus


class GetAllTasksByListService:
    def __init__(self, repository: TaskInterface, list_repository: TaskListInterface):
        self.repository = repository
        self.list_repository = list_repository

    def execute(
        self,
        list_id: int,
        status: Optional[str] = None,
        priority: Optional[str] = None,
    ) -> tuple[list[TaskEntity], float]:
        task_list = self.list_repository.get_by_id(list_id)
        if not task_list:
            raise TaskListNotFoundException(list_id)

        tasks = self.repository.get_all_by_list(list_id)

        # Validate and apply filters
        if status:
            try:
                valid_status = validate_status(status, TaskStatus)
            except Exception:
                raise InvalidStatusException(status)
            tasks = [t for t in tasks if t.status == valid_status]

        if priority:
            try:
                valid_priority = validate_priority(priority, TaskPriority)
            except Exception:
                raise InvalidPriorityException(priority)
            tasks = [t for t in tasks if t.priority == valid_priority]

        # completion average
        total = len(tasks)
        avg_completion = (
            round(sum(t.percentage_finalized for t in tasks) / total, 2)
            if total > 0
            else 0.0
        )

        return tasks, avg_completion

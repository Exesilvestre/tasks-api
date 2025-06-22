from app.application.tasks.utils import validate_priority, validate_status
from app.domain.tasks.interface import TaskInterface
from app.domain.task_lists.interface import TaskListInterface
from app.domain.tasks.entities import TaskEntity
from app.application.tasks.dtos.task_dto import TaskUpdateDTO, TaskResponseDTO
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException
from app.application.tasks.exceptions.excepcions import (
    TaskNotFoundException,
    TaskAlreadyExistsException,
    InvalidPercentageException,
)
from app.domain.core.priority import TaskPriority
from app.infrastructure.tasks.db.models import TaskStatus


class UpdateTaskService:
    def __init__(self, task_repo: TaskInterface, list_repo: TaskListInterface):
        self.task_repo = task_repo
        self.list_repo = list_repo

    def execute(
        self, task_list_id: int, task_id: int, dto: TaskUpdateDTO
    ) -> TaskResponseDTO:
        task_list = self.list_repo.get_by_id(task_list_id)
        if not task_list:
            raise TaskListNotFoundException(task_list_id)

        task = self.task_repo.get_by_id(task_list_id, task_id)
        if not task or task.task_list_id != task_list_id:
            raise TaskNotFoundException(task_id)

        if dto.name and dto.name != task.name:
            tasks = self.task_repo.get_all_by_list(task_list_id)
            if any(t.name.lower() == dto.name.lower() for t in tasks):
                raise TaskAlreadyExistsException(dto.name)

        status = validate_status(dto.status, TaskStatus) if dto.status else task.status
        priority = (
            validate_priority(dto.priority, TaskPriority)
            if dto.priority
            else task.priority
        )

        percentage = (
            dto.percentage_finalized
            if dto.percentage_finalized is not None
            else task.percentage_finalized
        )
        if not isinstance(percentage, float) or not (0.0 <= percentage <= 1.0):
            raise InvalidPercentageException(percentage)

        updated_entity = TaskEntity(
            id=task.id,
            name=dto.name or task.name,
            description=dto.description or task.description,
            status=status,
            priority=priority,
            percentage_finalized=percentage,
            task_list_id=task_list_id,
        )

        updated = self.task_repo.update(task_id, updated_entity)
        return TaskResponseDTO.from_entity(updated)

from app.domain.tasks.interface import TaskInterface
from app.domain.task_lists.interface import TaskListInterface
from app.application.tasks.dtos.task_dto import TaskStatusUpdateDTO, TaskResponseDTO
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException
from app.application.tasks.exceptions.excepcions import (
    TaskNotFoundException,
    InvalidStatusException,
)
from app.application.tasks.utils import validate_status
from app.domain.core.status import TaskStatus


class UpdateTaskStatusService:
    def __init__(self, task_repo: TaskInterface, list_repo: TaskListInterface):
        self.task_repo = task_repo
        self.list_repo = list_repo

    def execute(
        self, list_id: int, task_id: int, dto: TaskStatusUpdateDTO
    ) -> TaskResponseDTO:
        task_list = self.list_repo.get_by_id(list_id)
        if not task_list:
            raise TaskListNotFoundException(list_id)

        task = self.task_repo.get_by_id(list_id, task_id)
        if not task:
            raise TaskNotFoundException(task_id)

        try:
            status = validate_status(dto.status, TaskStatus)
        except Exception:
            raise InvalidStatusException(dto.status)

        task.status = status
        updated = self.task_repo.update(task_id, task)

        return TaskResponseDTO.from_entity(updated)

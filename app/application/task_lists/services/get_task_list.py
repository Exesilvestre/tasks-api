from app.domain.task_lists.interface import TaskListInterface
from app.application.task_lists.dtos.create_task_list_dto import (
    CreateTaskListResponseDTO,
)
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException


class GetTaskListService:
    def __init__(self, repository: TaskListInterface):
        self.repository = repository

    def execute(self, list_id: int) -> CreateTaskListResponseDTO:
        entity = self.repository.get_by_id(list_id)
        if not entity:
            raise TaskListNotFoundException(list_id)
        return CreateTaskListResponseDTO.from_entity(entity)

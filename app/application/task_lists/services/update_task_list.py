from typing import Optional
from app.domain.task_lists.interface import TaskListInterface
from app.domain.task_lists.entities import TaskListEntity
from app.application.task_lists.dtos.create_task_list_dto import CreateTaskListDTO, CreateTaskListResponseDTO


class UpdateTaskListService:
    def __init__(self, repository: TaskListInterface):
        self.repository = repository

    def execute(self, list_id: int, dto: CreateTaskListDTO) -> Optional[CreateTaskListResponseDTO]:
        entity = TaskListEntity(
            name=dto.name,
            description=dto.description
        )
        updated_entity = self.repository.update(list_id, entity)
        if not updated_entity:
            return None
        return CreateTaskListResponseDTO.from_entity(updated_entity)
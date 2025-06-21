from app.domain.task_lists.interface import TaskListInterface
from app.domain.task_lists.entities import TaskListEntity
from app.application.task_lists.dtos.create_task_list_dto import CreateTaskListDTO, CreateTaskListResponseDTO
from app.application.task_lists.exceptions.exceptions import (
    TaskListAlreadyExistsException,
    TaskListNameEmptyException,
)


class CreateTaskListService:
    def __init__(self, repository: TaskListInterface):
        self.repository = repository

    def execute(self, dto: CreateTaskListDTO) -> CreateTaskListResponseDTO:
        if not dto.name.strip():
            raise TaskListNameEmptyException()

        # validate that the name is unique
        existing_lists = self.repository.list_all()
        if any(list.name == dto.name for list in existing_lists):
            raise TaskListAlreadyExistsException(dto.name)

        task_list_entity = TaskListEntity(
            name=dto.name,
            description=dto.description
        )
        created_entity = self.repository.create(task_list_entity)
        return CreateTaskListResponseDTO.from_entity(created_entity)
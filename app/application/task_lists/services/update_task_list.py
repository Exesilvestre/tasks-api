from app.domain.task_lists.interface import TaskListInterface
from app.domain.task_lists.entities import TaskListEntity
from app.application.task_lists.dtos.update_task_list_dto import UpdateTaskListDTO, UpdateTaskListResponseDTO
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException, TaskListAlreadyExistsException


class UpdateTaskListService:
    def __init__(self, repository: TaskListInterface):
        self.repository = repository

    def execute(self, list_id: int, dto: UpdateTaskListDTO) -> UpdateTaskListResponseDTO:
        # Verificar si existe el ID
        db_list = self.repository.get_by_id(list_id)
        if not db_list:
            raise TaskListNotFoundException(list_id)

        # Verify if the new name already exists in another list
        if dto.name:
            all_lists = self.repository.get_all()
            if any(list.name == dto.name and list.id != list_id for list in all_lists):
                raise TaskListAlreadyExistsException(dto.name)

        entity = TaskListEntity(
            name=dto.name,
            description=dto.description if dto.description else db_list.description
        )

        updated_entity = self.repository.update(list_id, entity)
        return UpdateTaskListResponseDTO.from_entity(updated_entity)

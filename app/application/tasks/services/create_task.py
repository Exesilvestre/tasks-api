from app.application.tasks.dtos.task_dto import TaskCreateDTO, TaskResponseDTO
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException
from app.application.tasks.exceptions.excepcions import InvalidPercentageException, TaskAlreadyExistsException
from app.application.tasks.utils import validate_priority, validate_status
from app.domain.core.priority import TaskPriority
from app.domain.core.status import TaskStatus
from app.domain.task_lists.interface import TaskListInterface
from app.domain.tasks.entities import TaskEntity
from app.domain.tasks.interface import TaskInterface


class CreateTaskService:
    def __init__(self, task_repo: TaskInterface, list_repo: TaskListInterface):
        self.task_repo = task_repo
        self.list_repo = list_repo

    def execute(self, list_id: int, dto: TaskCreateDTO) -> TaskResponseDTO:
        task_list = self.list_repo.get_by_id(list_id)
        if not task_list:
            raise TaskListNotFoundException(list_id)

        priority = validate_priority(dto.priority, TaskPriority) if dto.priority else TaskPriority.medium
        status = validate_status(dto.status, TaskStatus) if dto.status else TaskStatus.pending

        if not isinstance(dto.percentage_finalized, float) or not (0.0 <= dto.percentage_finalized <= 1.0):
            raise InvalidPercentageException(dto.percentage_finalized)

        existing_tasks = self.task_repo.get_all_by_list(list_id)
        for task in existing_tasks:
            if task.name.lower() == dto.name.lower():
                raise TaskAlreadyExistsException(dto.name)

        task_entity = TaskEntity(
            name=dto.name,
            description=dto.description,
            status=status,
            priority=priority,
            percentage_finalized=dto.percentage_finalized,
            task_list_id=list_id
        )

        created = self.task_repo.create(task_entity)
        return TaskResponseDTO.from_entity(created)
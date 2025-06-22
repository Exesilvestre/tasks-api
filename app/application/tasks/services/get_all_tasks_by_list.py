from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException
from app.domain.task_lists.interface import TaskListInterface
from app.domain.tasks.entities import TaskEntity
from app.domain.tasks.interface import TaskInterface


class GetAllTasksByListService:
    def __init__(self, repository: TaskInterface, list_repository: TaskListInterface):
        self.repository = repository
        self.list_repository = list_repository

    def execute(self, list_id: int) -> list[TaskEntity]:
        task_list = self.list_repository.get_by_id(list_id)
        if not task_list:
            raise TaskListNotFoundException(list_id)
        tasks = self.repository.get_all_by_list(list_id)
        return tasks

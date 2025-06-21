from app.domain.task_lists.interface import TaskListInterface
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException


class DeleteTaskListService:
    def __init__(self, repository: TaskListInterface):
        self.repository = repository

    def execute(self, list_id: int) -> None:
        deleted = self.repository.delete(list_id)
        if not deleted:
            raise TaskListNotFoundException(list_id)

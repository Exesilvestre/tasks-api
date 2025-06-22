from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException
from app.domain.task_lists.interface import TaskListInterface
from app.domain.tasks.interface import TaskInterface
from app.application.tasks.exceptions.excepcions import TaskNotFoundException


class DeleteTaskService:
    def __init__(self, task_repo: TaskInterface, list_repo: TaskListInterface):
        self.task_repo = task_repo
        self.list_repo = list_repo

    def execute(self, list_id: int, task_id: int) -> None:
        task_list = self.list_repo.get_by_id(list_id)
        if not task_list:
            raise TaskListNotFoundException(list_id)

        deleted = self.task_repo.delete(list_id, task_id)
        if not deleted:
            raise TaskNotFoundException(task_id)

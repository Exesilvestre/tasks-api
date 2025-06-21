from app.domain.task_lists.interface import TaskListInterface


class DeleteTaskListService:
    def __init__(self, repository: TaskListInterface):
        self.repository = repository

    def execute(self, list_id: int) -> bool:
        return self.repository.delete(list_id)

from typing import List
from app.domain.task_lists.entities import TaskListEntity
from app.domain.task_lists.interface import TaskListInterface


class ListTaskListsService:
    def __init__(self, repository: TaskListInterface):
        self.repository = repository

    def execute(self) -> List[TaskListEntity]:
        return self.repository.get_all()

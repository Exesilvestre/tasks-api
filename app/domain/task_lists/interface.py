from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.task_lists.entities import TaskListEntity


class TaskListInterface(ABC):

    @abstractmethod
    def get_by_id(self, list_id: int) -> Optional[TaskListEntity]:
        pass

    @abstractmethod
    def get_all(self) -> List[TaskListEntity]:
        pass

    @abstractmethod
    def create(self, task_list: TaskListEntity) -> TaskListEntity:
        pass

    @abstractmethod
    def update(self, list_id: int, task_list: TaskListEntity) -> TaskListEntity:
        pass

    @abstractmethod
    def delete(self, list_id: int) -> None:
        pass
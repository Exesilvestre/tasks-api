from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.tasks.entities import TaskEntity


class TaskInterface(ABC):

    @abstractmethod
    def get_all_by_list(self, list_id: int) -> List[TaskEntity]:
        pass

    @abstractmethod
    def create(self, list_id: int, task: TaskEntity) -> TaskEntity:
        pass

    @abstractmethod
    def update(self, task_id: int, task: TaskEntity) -> Optional[TaskEntity]:
        pass

    @abstractmethod
    def delete(self, task_id: int) -> bool:
        pass

    @abstractmethod
    def get_by_id(self, list_id: int, task_id: int) -> Optional[TaskEntity]:
        pass

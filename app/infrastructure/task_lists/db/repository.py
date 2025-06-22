from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.task_lists.interface import TaskListInterface
from app.domain.task_lists.entities import TaskListEntity
from app.infrastructure.task_lists.db.models import TaskListModel


class TaskListRepository(TaskListInterface):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, list_id: int) -> Optional[TaskListEntity]:
        task_list = self.session.query(TaskListModel).filter_by(id=list_id).first()
        return (
            TaskListEntity.model_validate(task_list, from_attributes=True)
            if task_list
            else None
        )

    def get_all(self) -> List[TaskListEntity]:
        task_lists = self.session.query(TaskListModel).all()
        return [
            TaskListEntity.model_validate(list, from_attributes=True)
            for list in task_lists
        ]

    def create(self, task_list: TaskListEntity) -> TaskListEntity:
        db_task_list = TaskListModel(
            name=task_list.name, description=task_list.description
        )
        self.session.add(db_task_list)
        self.session.commit()
        self.session.refresh(db_task_list)
        return TaskListEntity.model_validate(db_task_list, from_attributes=True)

    def update(
        self, list_id: int, task_list: TaskListEntity
    ) -> Optional[TaskListEntity]:
        db_task_list = self.session.query(TaskListModel).filter_by(id=list_id).first()
        if not db_task_list:
            return None

        if task_list.name:
            db_task_list.name = task_list.name
        if task_list.description is not None:
            db_task_list.description = task_list.description

        self.session.commit()
        self.session.refresh(db_task_list)
        return TaskListEntity.model_validate(db_task_list, from_attributes=True)

    def delete(self, list_id: int) -> bool:
        db_task_list = self.session.query(TaskListModel).filter_by(id=list_id).first()
        if db_task_list:
            self.session.delete(db_task_list)
            self.session.commit()
            return True
        return False

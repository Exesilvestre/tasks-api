from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.tasks.entities import TaskEntity
from app.domain.tasks.interface import TaskInterface
from app.infrastructure.tasks.db.models import TaskModel


class TaskRepository(TaskInterface):
    def __init__(self, session: Session):
        self.session = session

    def get_all_by_list(self, list_id: int) -> List[TaskEntity]:
        tasks = (
            self.session
            .query(TaskModel)
            .filter_by(task_list_id=list_id)
            .all()
        )
        return [TaskEntity.model_validate(task, from_attributes=True) for task in tasks]

    def create(self, task: TaskEntity) -> TaskEntity:
        db_task = TaskModel(
            name=task.name,
            description=task.description,
            priority=task.priority,
            status=task.status,
            percentage_finalized=task.percentage_finalized,
            task_list_id=task.task_list_id
        )
        self.session.add(db_task)
        self.session.commit()
        self.session.refresh(db_task)
        return TaskEntity.model_validate(db_task, from_attributes=True)

    def update(self, task_id: int, task_data: TaskEntity) -> Optional[TaskEntity]:
        task = self.session.query(TaskModel).filter_by(id=task_id).first()
        if not task:
            return None

        if task_data.name is not None:
            task.name = task_data.name
        if task_data.description is not None:
            task.description = task_data.description
        if task_data.priority is not None:
            task.priority = task_data.priority
        if task_data.status is not None:
            task.status = task_data.status
        if task_data.percentage_finalized is not None:
            task.percentage_finalized = task_data.percentage_finalized

        self.session.commit()
        self.session.refresh(task)
        return TaskEntity.model_validate(task, from_attributes=True)

    def delete(self, list_id: int, task_id: int) -> bool:
        task = (
            self.session.query(TaskModel)
            .filter_by(id=task_id, task_list_id=list_id)
            .first()
        )
        if not task:
            return False
        self.session.delete(task)
        self.session.commit()
        return True

    def get_by_id(self, list_id: int, task_id: int) -> Optional[TaskEntity]:
        task = (
            self.session.query(TaskModel)
            .filter_by(id=task_id, task_list_id=list_id)
            .first()
        )
        if not task:
            return None
        return TaskEntity.model_validate(task, from_attributes=True)

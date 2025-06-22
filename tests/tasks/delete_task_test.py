import pytest
from app.application.tasks.services.delete_task import DeleteTaskService
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException
from app.application.tasks.exceptions.excepcions import TaskNotFoundException
from app.infrastructure.tasks.db.repository import TaskRepository
from app.infrastructure.task_lists.db.repository import TaskListRepository
from app.domain.task_lists.entities import TaskListEntity
from app.domain.tasks.entities import TaskEntity
from app.domain.core.priority import TaskPriority
from app.domain.core.status import TaskStatus


def test_delete_task_success(db_session):
    list_repo = TaskListRepository(db_session)
    task_repo = TaskRepository(db_session)
    service = DeleteTaskService(task_repo, list_repo)

    # Create list and task
    list_entity = TaskListEntity(name="Work", description="Work tasks")
    created_list = list_repo.create(list_entity)

    task_entity = TaskEntity(
        name="Task to delete",
        description="Description",
        priority=TaskPriority.medium,
        status=TaskStatus.pending,
        percentage_finalized=0.0,
        task_list_id=created_list.id,
    )
    created_task = task_repo.create(task_entity)

    service.execute(created_list.id, created_task.id)

    assert task_repo.get_by_id(created_list.id, created_task.id) is None


def test_delete_task_list_not_found_raises(db_session):
    list_repo = TaskListRepository(db_session)
    task_repo = TaskRepository(db_session)
    service = DeleteTaskService(task_repo, list_repo)

    with pytest.raises(TaskListNotFoundException):
        service.execute(50, 1)


def test_delete_task_not_found_raises(db_session):
    list_repo = TaskListRepository(db_session)
    task_repo = TaskRepository(db_session)
    service = DeleteTaskService(task_repo, list_repo)

    list_entity = TaskListEntity(name="Work", description="Work tasks")
    created_list = list_repo.create(list_entity)

    with pytest.raises(TaskNotFoundException):
        service.execute(created_list.id, 0)

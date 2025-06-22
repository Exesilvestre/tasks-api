import pytest
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException
from app.application.tasks.services.get_all_tasks_by_list import GetAllTasksByListService
from app.infrastructure.tasks.db.repository import TaskRepository
from app.infrastructure.task_lists.db.repository import TaskListRepository
from app.domain.task_lists.entities import TaskListEntity
from app.domain.tasks.entities import TaskEntity
from app.domain.core.priority import TaskPriority
from app.domain.core.status import TaskStatus


def test_get_all_tasks_by_list_success(db_session):
    list_repo = TaskListRepository(db_session)
    task_repo = TaskRepository(db_session)
    service = GetAllTasksByListService(task_repo, list_repo)

    # Crear lista
    created_list = list_repo.create(TaskListEntity(name="Work", description="Work tasks"))

    # Crear tareas
    task1 = TaskEntity(
        name="Task 1",
        description="desc 1",
        priority=TaskPriority.high,
        status=TaskStatus.pending,
        percentage_finalized=0.0,
        task_list_id=created_list.id
    )
    task2 = TaskEntity(
        name="Task 2",
        description="desc 2",
        priority=TaskPriority.low,
        status=TaskStatus.done,
        percentage_finalized=1.0,
        task_list_id=created_list.id
    )
    task_repo.create(task1)
    task_repo.create(task2)

    tasks = service.execute(created_list.id)

    assert len(tasks) == 2
    assert all(task.task_list_id == created_list.id for task in tasks)


def test_get_all_tasks_by_list_not_found_raises(db_session):
    list_repo = TaskListRepository(db_session)
    task_repo = TaskRepository(db_session)
    service = GetAllTasksByListService(task_repo, list_repo)

    with pytest.raises(TaskListNotFoundException):
        service.execute(50)

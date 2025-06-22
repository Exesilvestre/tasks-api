import pytest
from app.application.tasks.services.update_task import UpdateTaskService
from app.application.tasks.dtos.task_dto import TaskUpdateDTO
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException
from app.application.tasks.exceptions.excepcions import (
    TaskNotFoundException,
    TaskAlreadyExistsException,
    InvalidPercentageException,
)
from app.infrastructure.tasks.db.repository import TaskRepository
from app.infrastructure.task_lists.db.repository import TaskListRepository
from app.domain.core.priority import TaskPriority
from app.domain.core.status import TaskStatus
from app.domain.task_lists.entities import TaskListEntity
from app.domain.tasks.entities import TaskEntity


@pytest.fixture
def list_and_tasks(db_session):
    list_repo = TaskListRepository(db_session)
    task_repo = TaskRepository(db_session)

    created_list = list_repo.create(
        TaskListEntity(name="Work", description="Work tasks")
    )

    task1 = task_repo.create(
        TaskEntity(
            name="Task 1",
            description="desc 1",
            status=TaskStatus.pending,
            priority=TaskPriority.medium,
            percentage_finalized=0.0,
            task_list_id=created_list.id,
        )
    )
    task2 = task_repo.create(
        TaskEntity(
            name="Task 2",
            description="desc 2",
            status=TaskStatus.pending,
            priority=TaskPriority.medium,
            percentage_finalized=0.0,
            task_list_id=created_list.id,
        )
    )
    return list_repo, task_repo, created_list, task1, task2


def test_update_task_success(list_and_tasks):
    list_repo, task_repo, created_list, task1, _ = list_and_tasks
    service = UpdateTaskService(task_repo, list_repo)

    dto = TaskUpdateDTO(
        name="New Task",
        description="New description",
        status=TaskStatus.done.value,
        priority=TaskPriority.high.value,
        percentage_finalized=0.75,
    )

    response = service.execute(created_list.id, task1.id, dto)

    assert response.id == task1.id
    assert response.name == dto.name
    assert response.description == dto.description
    assert response.status == dto.status
    assert response.priority == dto.priority
    assert response.percentage_finalized == dto.percentage_finalized


def test_update_task_list_not_found(list_and_tasks):
    list_repo, task_repo, _, _, _ = list_and_tasks
    service = UpdateTaskService(task_repo, list_repo)

    dto = TaskUpdateDTO(name="Name")

    with pytest.raises(TaskListNotFoundException):
        service.execute(9999, 1, dto)


def test_update_task_not_found(list_and_tasks):
    list_repo, task_repo, created_list, _, _ = list_and_tasks
    service = UpdateTaskService(task_repo, list_repo)

    dto = TaskUpdateDTO(name="Name")

    with pytest.raises(TaskNotFoundException):
        service.execute(created_list.id, 9999, dto)


def test_update_task_duplicate_name_raises(list_and_tasks):
    list_repo, task_repo, created_list, task1, task2 = list_and_tasks
    service = UpdateTaskService(task_repo, list_repo)

    dto = TaskUpdateDTO(name="Task 1")

    with pytest.raises(TaskAlreadyExistsException):
        service.execute(created_list.id, task2.id, dto)


def test_update_task_invalid_percentage_raises(list_and_tasks):
    list_repo, task_repo, created_list, task1, _ = list_and_tasks
    service = UpdateTaskService(task_repo, list_repo)

    dto = TaskUpdateDTO(percentage_finalized=2.0)

    with pytest.raises(InvalidPercentageException):
        service.execute(created_list.id, task1.id, dto)

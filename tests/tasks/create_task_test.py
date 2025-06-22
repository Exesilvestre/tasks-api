import pytest
from app.application.tasks.services.create_task import CreateTaskService
from app.application.tasks.dtos.task_dto import TaskCreateDTO
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException
from app.application.tasks.exceptions.excepcions import (
    InvalidPercentageException,
    TaskAlreadyExistsException,
)
from app.infrastructure.tasks.db.repository import TaskRepository
from app.infrastructure.task_lists.db.repository import TaskListRepository
from app.domain.core.priority import TaskPriority
from app.domain.core.status import TaskStatus
from app.domain.task_lists.entities import TaskListEntity


@pytest.fixture
def created_task_list(db_session):
    list_repo = TaskListRepository(db_session)
    list_entity = TaskListEntity(name="work", description="work tasks")
    return list_repo.create(list_entity)


def test_create_task_success(db_session, created_task_list):
    task_repo = TaskRepository(db_session)
    service = CreateTaskService(task_repo, TaskListRepository(db_session))

    dto = TaskCreateDTO(
        name="My Task",
        description="Task description",
        priority=TaskPriority.high.value,
        status=TaskStatus.pending.value,
        percentage_finalized=0.5,
    )

    response = service.execute(created_task_list.id, dto)

    assert response.id is not None
    assert response.name == dto.name
    assert response.percentage_finalized == dto.percentage_finalized


def test_create_task_list_not_found_raises(db_session):
    task_repo = TaskRepository(db_session)
    service = CreateTaskService(task_repo, TaskListRepository(db_session))

    dto = TaskCreateDTO(
        name="My Task",
        description="Task description",
        percentage_finalized=0.5,
    )

    with pytest.raises(TaskListNotFoundException):
        service.execute(9999, dto)


def test_create_task_invalid_percentage_raises(db_session, created_task_list):
    task_repo = TaskRepository(db_session)
    service = CreateTaskService(task_repo, TaskListRepository(db_session))

    dto = TaskCreateDTO(
        name="My Task",
        description="Task description",
        percentage_finalized=2.0,  # Inválido
    )

    with pytest.raises(InvalidPercentageException):
        service.execute(created_task_list.id, dto)


def test_create_task_duplicate_name_raises(db_session, created_task_list):
    task_repo = TaskRepository(db_session)
    service = CreateTaskService(task_repo, TaskListRepository(db_session))

    existing_task_dto = TaskCreateDTO(
        name="Task 1",
        description="desc",
        percentage_finalized=0.0,
    )
    service.execute(created_task_list.id, existing_task_dto)

    duplicate_task_dto = TaskCreateDTO(
        name="task 1",  # mismo nombre, diferente case
        description="desc",
        percentage_finalized=0.5,
    )

    with pytest.raises(TaskAlreadyExistsException):
        service.execute(created_task_list.id, duplicate_task_dto)

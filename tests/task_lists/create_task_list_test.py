import pytest
from app.application.task_lists.services.create_task_list import CreateTaskListService
from app.application.task_lists.dtos.create_task_list_dto import CreateTaskListDTO
from app.application.task_lists.exceptions.exceptions import (
    TaskListNameEmptyException,
    TaskListAlreadyExistsException,
)
from app.domain.task_lists.entities import TaskListEntity
from app.infrastructure.task_lists.db.repository import TaskListRepository


def test_create_task_list_success(db_session):
    repo = TaskListRepository(db_session)
    service = CreateTaskListService(repo)

    dto = CreateTaskListDTO(name="Work", description="Work-related tasks")
    response = service.execute(dto)

    assert response.id is not None
    assert response.name == "Work"
    assert response.description == "Work-related tasks"


def test_create_task_list_with_empty_name_raises_exception(db_session):
    repo = TaskListRepository(db_session)
    service = CreateTaskListService(repo)

    dto = CreateTaskListDTO(name="   ", description="Blank name")

    with pytest.raises(TaskListNameEmptyException):
        service.execute(dto)


def test_create_task_list_with_duplicate_name_raises_exception(db_session):
    repo = TaskListRepository(db_session)
    service = CreateTaskListService(repo)
    fisrt_list_dto = CreateTaskListDTO(name="Home", description="Work-related tasks")
    service.execute(fisrt_list_dto)

    second_list_dto = CreateTaskListDTO(name="Home", description="Duplicate name")

    with pytest.raises(TaskListAlreadyExistsException):
        service.execute(second_list_dto)

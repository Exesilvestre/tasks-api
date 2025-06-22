import pytest
from app.application.task_lists.services.update_task_list import UpdateTaskListService
from app.infrastructure.task_lists.db.repository import TaskListRepository
from app.application.task_lists.dtos.create_task_list_dto import CreateTaskListDTO
from app.application.task_lists.dtos.update_task_list_dto import UpdateTaskListDTO
from app.application.task_lists.exceptions.exceptions import (
    TaskListNotFoundException,
    TaskListAlreadyExistsException,
)
from app.application.task_lists.services.create_task_list import CreateTaskListService


def test_update_task_list_success(db_session):
    repo = TaskListRepository(db_session)
    create_service = CreateTaskListService(repo)
    update_service = UpdateTaskListService(repo)

    create_dto = CreateTaskListDTO(name="Original", description="original")
    created = create_service.execute(create_dto)

    update_dto = UpdateTaskListDTO(name="Updated", description="Updated")
    response = update_service.execute(created.id, update_dto)

    assert response.name == "Updated"
    assert response.description == "Updated"


def test_update_task_list_not_found_raises_exception(db_session):
    repo = TaskListRepository(db_session)
    update_service = UpdateTaskListService(repo)

    update_dto = UpdateTaskListDTO(name="No existe", description="No existe")
    with pytest.raises(TaskListNotFoundException):
        update_service.execute(999999, update_dto)


def test_update_task_list_duplicate_name_raises_exception(db_session):
    repo = TaskListRepository(db_session)
    create_service = CreateTaskListService(repo)
    update_service = UpdateTaskListService(repo)

    create_service.execute(CreateTaskListDTO(name="home", description="home tasks"))
    second = create_service.execute(CreateTaskListDTO(name="work", description="work tasks"))

    update_dto = UpdateTaskListDTO(name="home", description="Desc duplicada")
    with pytest.raises(TaskListAlreadyExistsException):
        update_service.execute(second.id, update_dto)

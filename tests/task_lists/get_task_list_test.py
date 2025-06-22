import pytest
from app.application.task_lists.services.get_task_list import GetTaskListService
from app.infrastructure.task_lists.db.repository import TaskListRepository
from app.application.task_lists.dtos.create_task_list_dto import CreateTaskListDTO
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException
from app.application.task_lists.services.create_task_list import CreateTaskListService


def test_get_task_list_success(db_session):
    repo = TaskListRepository(db_session)
    create_service = CreateTaskListService(repo)
    get_service = GetTaskListService(repo)

    list_dto = CreateTaskListDTO(name="lista 1", description="cosas de la casa")
    created = create_service.execute(list_dto)

    response = get_service.execute(created.id)

    assert response.id == created.id
    assert response.name == created.name
    assert response.description == created.description


def test_get_task_list_not_found_raises_exception(db_session):
    repo = TaskListRepository(db_session)
    get_service = GetTaskListService(repo)

    with pytest.raises(TaskListNotFoundException):
        get_service.execute(50)

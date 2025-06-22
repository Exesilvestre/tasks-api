import pytest
from app.application.task_lists.services.create_task_list import CreateTaskListService
from app.application.task_lists.services.delete_task_list import DeleteTaskListService
from app.application.task_lists.exceptions.exceptions import TaskListNotFoundException
from app.application.task_lists.dtos.create_task_list_dto import CreateTaskListDTO
from app.infrastructure.task_lists.db.repository import TaskListRepository


def test_delete_task_list_success(db_session):
    repo = TaskListRepository(db_session)
    create_service = CreateTaskListService(repo)
    delete_service = DeleteTaskListService(repo)

    list_dto = CreateTaskListDTO(name="lista 1 ", description="lista a borrar")
    created = create_service.execute(list_dto)

    delete_service.execute(created.id)

    all_lists = repo.get_all()
    assert all(created.id != lst.id for lst in all_lists)


def test_delete_task_list_not_found_raises_exception(db_session):
    repo = TaskListRepository(db_session)
    delete_service = DeleteTaskListService(repo)

    with pytest.raises(TaskListNotFoundException):
        delete_service.execute(999999)
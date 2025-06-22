import pytest
from app.application.task_lists.services.get_all_lists import ListTaskListsService
from app.infrastructure.task_lists.db.repository import TaskListRepository
from app.application.task_lists.dtos.create_task_list_dto import CreateTaskListDTO
from app.application.task_lists.services.create_task_list import CreateTaskListService


def test_list_task_lists_returns_all(db_session):
    repo = TaskListRepository(db_session)
    create_service = CreateTaskListService(repo)
    list_service = ListTaskListsService(repo)

    lists_dtos = [
        CreateTaskListDTO(name="List 1", description="Desc 1"),
        CreateTaskListDTO(name="List 2", description="Desc 2"),
    ]

    for lista in lists_dtos:
        create_service.execute(lista)

    result = list_service.execute()

    assert len(result) >= 2
    names = [task_list.name for task_list in result]
    assert "List 1" in names
    assert "List 2" in names

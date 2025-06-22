from fastapi import APIRouter, Path, Depends, Query, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from app.application.shared.helper import map_exception_to_http
from app.application.tasks.services.create_task import CreateTaskService
from app.application.tasks.services.delete_task import DeleteTaskService
from app.application.tasks.services.get_all_tasks_by_list import (
    GetAllTasksByListService,
)
from app.application.tasks.dtos.task_dto import (
    TaskCreateDTO,
    TaskListWithCompletionDTO,
    TaskResponseDTO,
    TaskStatusUpdateDTO,
    TaskUpdateDTO,
)
from app.application.tasks.services.update_task import UpdateTaskService
from app.application.tasks.services.update_task_status import UpdateTaskStatusService
from app.infrastructure.db.session import get_session
from app.infrastructure.task_lists.db.repository import TaskListRepository
from app.infrastructure.tasks.db.repository import TaskRepository

router = APIRouter(prefix="/tasklists/{task_list_id}/tasks", tags=["tasks"])


@router.get("/", response_model=TaskListWithCompletionDTO)
def get_all_tasks(
    task_list_id: int,
    status: str = Query(default=None),
    priority: str = Query(default=None),
    session: Session = Depends(get_session),
):
    task_repo = TaskRepository(session)
    list_repo = TaskListRepository(session)
    service = GetAllTasksByListService(task_repo, list_repo)
    try:
        tasks, completion = service.execute(task_list_id, status, priority)
        return TaskListWithCompletionDTO(
            tasks=[TaskResponseDTO.from_entity(task) for task in tasks],
            completion=completion,
        )
    except Exception as e:
        raise map_exception_to_http(e)


@router.post("/", response_model=TaskResponseDTO)
def create_task(
    task_list_id: int = Path(...),
    dto: TaskCreateDTO = ...,
    session: Session = Depends(get_session),
):
    task_repo = TaskRepository(session)
    list_repo = TaskListRepository(session)
    service = CreateTaskService(task_repo, list_repo)
    try:
        return service.execute(task_list_id, dto)
    except Exception as e:
        raise map_exception_to_http(e)


@router.put("/{task_id}", response_model=TaskResponseDTO)
def update_task(
    task_list_id: int,
    task_id: int,
    dto: TaskUpdateDTO,
    session: Session = Depends(get_session),
):
    task_repo = TaskRepository(session)
    list_repo = TaskListRepository(session)
    service = UpdateTaskService(task_repo, list_repo)
    try:
        return service.execute(task_list_id, task_id, dto)
    except Exception as e:
        raise map_exception_to_http(e)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(list_id: int, task_id: int, session: Session = Depends(get_session)):
    task_repo = TaskRepository(session)
    list_repo = TaskListRepository(session)
    service = DeleteTaskService(task_repo, list_repo)
    try:
        service.execute(list_id, task_id)
    except Exception as e:
        raise map_exception_to_http(e)


@router.patch("/{task_id}/status", response_model=TaskResponseDTO)
def update_task_status(
    task_list_id: int,
    task_id: int,
    dto: TaskStatusUpdateDTO,
    session: Session = Depends(get_session),
):
    task_repo = TaskRepository(session)
    list_repo = TaskListRepository(session)
    service = UpdateTaskStatusService(task_repo, list_repo)
    try:
        return service.execute(task_list_id, task_id, dto)
    except Exception as e:
        raise map_exception_to_http(e)

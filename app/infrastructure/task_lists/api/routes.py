from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.application.shared.helper import map_exception_to_http
from app.application.task_lists.exceptions.exceptions import (
    TaskListAlreadyExistsException,
    TaskListNameEmptyException,
    TaskListNotFoundException,
)
from app.application.task_lists.services.create_task_list import CreateTaskListService
from app.application.task_lists.services.get_all_lists import ListTaskListsService
from app.application.task_lists.services.get_task_list import GetTaskListService
from app.application.task_lists.services.update_task_list import UpdateTaskListService
from app.application.task_lists.services.delete_task_list import DeleteTaskListService

from app.application.task_lists.dtos.create_task_list_dto import (
    CreateTaskListDTO,
    CreateTaskListResponseDTO,
)
from app.application.task_lists.dtos.update_task_list_dto import (
    UpdateTaskListDTO,
    UpdateTaskListResponseDTO,
)

from app.infrastructure.db.session import get_session
from app.infrastructure.task_lists.db.repository import TaskListRepository

router = APIRouter(prefix="/tasklists", tags=["tasklists"])


@router.post("/", response_model=CreateTaskListResponseDTO)
def create_task_list(dto: CreateTaskListDTO, session: Session = Depends(get_session)):
    repo = TaskListRepository(session)
    service = CreateTaskListService(repo)
    try:
        return service.execute(dto)
    except Exception as e:
        raise map_exception_to_http(e)


@router.get("/{list_id}", response_model=CreateTaskListResponseDTO)
def get_task_list(list_id: int, session: Session = Depends(get_session)):
    repo = TaskListRepository(session)
    service = GetTaskListService(repo)
    try:
        return service.execute(list_id)
    except Exception as e:
        raise map_exception_to_http(e)


@router.put("/{list_id}", response_model=UpdateTaskListResponseDTO)
def update_task_list(
    list_id: int, dto: UpdateTaskListDTO, session: Session = Depends(get_session)
):
    repo = TaskListRepository(session)
    service = UpdateTaskListService(repo)
    try:
        return service.execute(list_id, dto)
    except Exception as e:
        raise map_exception_to_http(e)


@router.delete("/{list_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_list(list_id: int, session: Session = Depends(get_session)):
    repo = TaskListRepository(session)
    service = DeleteTaskListService(repo)
    try:
        service.execute(list_id)
    except Exception as e:
        raise map_exception_to_http(e)


@router.get("/", response_model=List[CreateTaskListResponseDTO])
def list_all_task_lists(session: Session = Depends(get_session)):
    repo = TaskListRepository(session)
    service = ListTaskListsService(repo)
    try:
        entities = service.execute()
        return [CreateTaskListResponseDTO.from_entity(e) for e in entities]
    except Exception as e:
        raise map_exception_to_http(e)

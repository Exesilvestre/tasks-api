from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.application.task_lists.dtos.update_task_list_dto import UpdateTaskListDTO, UpdateTaskListResponseDTO
from app.application.task_lists.exceptions.exceptions import TaskListAlreadyExistsException, TaskListNameEmptyException, TaskListNotFoundException
from app.application.task_lists.services.create_task_list import CreateTaskListService
from app.application.task_lists.services.get_all_lists import ListTaskListsService
from app.application.task_lists.services.get_task_list import GetTaskListService
from app.application.task_lists.services.update_task_list import UpdateTaskListService
from app.application.task_lists.services.delete_task_list import DeleteTaskListService

from app.application.task_lists.dtos.create_task_list_dto import (
    CreateTaskListDTO, CreateTaskListResponseDTO
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
    except TaskListAlreadyExistsException as e:
        raise HTTPException(status_code=400, detail=e.message)
    except TaskListNameEmptyException as e:
        raise HTTPException(status_code=422, detail=e.message)


@router.get("/{list_id}", response_model=CreateTaskListResponseDTO)
def get_task_list(list_id: int, session: Session = Depends(get_session)):
    repo = TaskListRepository(session)
    service = GetTaskListService(repo)
    try:
        return service.execute(list_id)
    except TaskListNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.get("/", response_model=List[CreateTaskListResponseDTO])
def list_all_task_lists(session: Session = Depends(get_session)):
    repo = TaskListRepository(session)
    service = ListTaskListsService(repo)
    entities = service.execute()
    return [CreateTaskListResponseDTO.from_entity(e) for e in entities]


@router.put("/{list_id}", response_model=UpdateTaskListResponseDTO)
def update_task_list(list_id: int, dto: UpdateTaskListDTO, session: Session = Depends(get_session)):
    repo = TaskListRepository(session)
    service = UpdateTaskListService(repo)
    updated = service.execute(list_id, dto)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task list not found")
    return updated


@router.delete("/{list_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_list(list_id: int, session: Session = Depends(get_session)):
    repo = TaskListRepository(session)
    service = DeleteTaskListService(repo)
    success = service.execute(list_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task list not found")
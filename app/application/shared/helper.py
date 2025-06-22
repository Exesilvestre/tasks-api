from fastapi import HTTPException

# Excepciones tasklists
from app.application.task_lists.exceptions.exceptions import (
    TaskListNotFoundException,
    TaskListAlreadyExistsException,
    TaskListNameEmptyException,
)

# Excepciones tasks
from app.application.tasks.exceptions.excepcions import (
    TaskAlreadyExistsException,
    TaskNotFoundException,
    InvalidPriorityException,
    InvalidStatusException,
    InvalidPercentageException
)


def map_exception_to_http(e: Exception) -> HTTPException:
    # TaskLists
    if isinstance(e, TaskListNotFoundException):
        return HTTPException(status_code=404, detail=str(e))
    if isinstance(e, (TaskListAlreadyExistsException, TaskAlreadyExistsException)):
        return HTTPException(status_code=409, detail=str(e))
    if isinstance(e, TaskListNameEmptyException):
        return HTTPException(status_code=400, detail=str(e))

    # Tasks
    if isinstance(e, TaskNotFoundException):
        return HTTPException(status_code=404, detail=str(e))
    if isinstance(e, (InvalidPriorityException, InvalidStatusException, InvalidPercentageException)):
        return HTTPException(status_code=400, detail=str(e))

    # unhandled error
    return HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

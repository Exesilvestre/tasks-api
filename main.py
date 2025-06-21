from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.application.task_lists.exceptions.exceptions import TaskListAlreadyExistsException, TaskListNameEmptyException, TaskListNotFoundException
from app.infrastructure.tasks.api.routes import router as tasks_router
from app.infrastructure.task_lists.api.routes import router as lists_router 


app = FastAPI()


@app.exception_handler(TaskListAlreadyExistsException)
async def task_list_already_exists_handler(request: Request, exc: TaskListAlreadyExistsException):
    return JSONResponse(status_code=400, content={"detail": exc.message})


@app.exception_handler(TaskListNameEmptyException)
async def task_list_name_empty_handler(request: Request, exc: TaskListNameEmptyException):
    return JSONResponse(status_code=400, content={"detail": exc.message})


@app.exception_handler(TaskListNotFoundException)
async def task_list_not_found_handler(request: Request, exc: TaskListNotFoundException):
    return JSONResponse(status_code=404, content={"detail": exc.message})


app.include_router(lists_router)
app.include_router(tasks_router)

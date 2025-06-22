from fastapi import FastAPI
from app.infrastructure.tasks.api.routes import router as tasks_router
from app.infrastructure.task_lists.api.routes import router as lists_router


app = FastAPI()


app.include_router(lists_router)
app.include_router(tasks_router)

from fastapi import FastAPI

from app.infrastructure.tasks.api.routes import router


app = FastAPI()

app.include_router(router)

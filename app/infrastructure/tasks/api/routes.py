from fastapi import APIRouter


router = APIRouter(prefix="/tasks")


@router.get("/{task_id}")
def get_task(task_id: str):
    return "hello task 1"


@router.put("/task_id")
def update_task(task_id: str):
    return "updating task"


@router.post("/")
def create_task():
    return "creating task"


@router.delete("/task_id")
def remove_task(task_id: str):
    return "deleting task"

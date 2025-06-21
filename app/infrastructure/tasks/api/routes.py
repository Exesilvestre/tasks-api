from fastapi import APIRouter, Path

router = APIRouter(prefix="/tasklists/{task_list_id}/tasks", tags=["tasks"])


@router.get("/{task_id}")
def get_task(task_list_id: int = Path(...), task_id: int = Path(...)):
    return {"task_list_id": task_list_id, "task_id": task_id, "msg": "Get task"}


@router.put("/{task_id}")
def update_task(task_list_id: int = Path(...), task_id: int = Path(...)):
    return {"task_list_id": task_list_id, "task_id": task_id, "msg": "Update task"}


@router.post("/")
def create_task(task_list_id: int = Path(...)):
    return {"task_list_id": task_list_id, "msg": "Create task"}


@router.delete("/{task_id}")
def remove_task(task_list_id: int = Path(...), task_id: int = Path(...)):
    return {"task_list_id": task_list_id, "task_id": task_id, "msg": "Delete task"}
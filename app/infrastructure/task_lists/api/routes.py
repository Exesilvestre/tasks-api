from fastapi import APIRouter, Path

router = APIRouter(prefix="/tasklists", tags=["tasklists"])


@router.get("/{list_id}")
def get_task(list_id: int = Path(...)):
    return {"list_id": list_id, "msg": "Get list"}


@router.put("/{list_id}")
def update_task(list_id: int = Path(...)):
    return {"list_id": list_id, "msg": "Update list"}


@router.post("/")
def create_task():
    return {"msg": "Create list"}


@router.delete("/{list_id}")
def remove_task(list_id: int = Path(...)):
    return {"list_id": list_id, "msg": "Delete list"}
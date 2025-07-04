from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TaskListEntity(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

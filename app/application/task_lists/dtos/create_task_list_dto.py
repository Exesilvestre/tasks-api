from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from app.domain.task_lists.entities import TaskListEntity


class CreateTaskListDTO(BaseModel):
    name: str
    description: Optional[str] = None


class CreateTaskListResponseDTO(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    @classmethod
    def from_entity(cls, entity: TaskListEntity) -> "CreateTaskListResponseDTO":
        return cls(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )

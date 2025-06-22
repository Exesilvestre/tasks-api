from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

from app.domain.task_lists.entities import TaskListEntity


class CreateTaskListDTO(BaseModel):
    name: str = Field(..., example="Work Tasks")
    description: Optional[str] = Field(None, example="Tasks related to work projects")


class CreateTaskListResponseDTO(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Work Tasks")
    description: Optional[str] = Field(None, example="Tasks related to work projects")
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    @classmethod
    def from_entity(cls, entity: TaskListEntity) -> "CreateTaskListResponseDTO":
        return cls(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
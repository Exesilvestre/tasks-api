from typing import List, Optional
from pydantic import BaseModel, Field


class TaskCreateDTO(BaseModel):
    name: str
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    percentage_finalized: Optional[float] = 0.0


class TaskResponseDTO(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    percentage_finalized: Optional[float] = 0.0

    @classmethod
    def from_entity(cls, entity):
        return cls(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            priority=entity.priority,
            status=entity.status,
            percentage_finalized=entity.percentage_finalized,
        )


class TaskUpdateDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    percentage_finalized: Optional[float] = None


class TaskStatusUpdateDTO(BaseModel):
    status: str = Field(..., example="done")


class TaskListWithCompletionDTO(BaseModel):
    tasks: List[TaskResponseDTO]
    completion: float

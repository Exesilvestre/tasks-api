from typing import List, Optional
from pydantic import BaseModel, Field


class TaskCreateDTO(BaseModel):
    name: str = Field(..., example="example: laundry")
    description: Optional[str] = Field(None, example="example: midnight laundry")
    priority: Optional[str] = Field(
        None,
        example="medium",
        description="Task priority. Valid values: low, medium, high"
    )
    status: Optional[str] = Field(
        None,
        example="in_progress",
        description="Task status. Valid values: pending, in_progress, done"
    )
    percentage_finalized: Optional[float] = Field(
        0.0,
        example=0.5,
        description="Completion percentage (0.0 to 1.0)"
    )


class TaskResponseDTO(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    priority: Optional[str] = Field(
        None,
        example="medium",
        description="Task priority. Valid values: low, medium, high"
    )
    status: Optional[str] = Field(
        None,
        example="pending",
        description="Task status. Valid values: pending, in_progress, done"
    )
    percentage_finalized: Optional[float] = Field(
        0.0,
        example=0.75,
        description="Completion percentage (0.0 to 1.0)"
    )

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
    name: Optional[str] = Field(None, example="Updated task title")
    description: Optional[str] = Field(None, example="Updated task description")
    status: Optional[str] = Field(
        None,
        example="done",
        description="Task status. Valid values: pending, in_progress, done"
    )
    priority: Optional[str] = Field(
        None,
        example="high",
        description="Task priority. Valid values: low, medium, high"
    )
    percentage_finalized: Optional[float] = Field(
        None,
        example=1.0,
        description="Completion percentage (0.0 to 1.0)"
    )


class TaskStatusUpdateDTO(BaseModel):
    status: str = Field(
        ...,
        example="done",
        description="Task status. Valid values: pending, in_progress, done"
    )


class TaskListWithCompletionDTO(BaseModel):
    tasks: List[TaskResponseDTO]
    completion: float = Field(..., example=0.64)

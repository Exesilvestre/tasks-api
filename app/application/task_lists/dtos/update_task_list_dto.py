from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UpdateTaskListDTO(BaseModel):
    name: str
    description: Optional[str] = None


class UpdateTaskListResponseDTO(BaseModel):
    name: str
    description: Optional[str]
    updated_at: datetime

    @classmethod
    def from_entity(cls, entity):
        return cls(
            name=entity.name,
            description=entity.description,
            updated_at=entity.updated_at,
        )
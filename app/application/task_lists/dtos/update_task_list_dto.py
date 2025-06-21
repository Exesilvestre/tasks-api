from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UpdateTaskListDTO(BaseModel):
    name: Optional[str]
    description: Optional[str]


class UpdateTaskListResponseDTO(BaseModel):
    name: Optional[str]
    description: Optional[str]
    updated_at: Optional[datetime]

    @classmethod
    def from_entity(cls, entity):
        return cls(
            name=entity.name,
            description=entity.description,
            updated_at=entity.updated_at,
        )
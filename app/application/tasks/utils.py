from typing import Type
from enum import Enum
from app.application.tasks.exceptions.excepcions import (
    InvalidStatusException,
    InvalidPriorityException,
)


def validate_status(value: str, enum_type: Type[Enum]) -> Enum:
    if not isinstance(value, str):
        raise InvalidStatusException(value)
    value_lower = value.lower()
    if value_lower not in enum_type._value2member_map_:
        raise InvalidStatusException(value)
    return enum_type(value_lower)


def validate_priority(value: str, enum_type: Type[Enum]) -> Enum:
    if not isinstance(value, str):
        raise InvalidPriorityException(value)
    value_lower = value.lower()
    if value_lower not in enum_type._value2member_map_:
        raise InvalidPriorityException(value)
    return enum_type(value_lower)

from typing import Any, Type
from enum import Enum
from tortoise.exceptions import ValidationError


class EnumValidator:
    def __init__(self, enum: Type[Enum]):
        self._enum = list(enum)

    def __call__(self, value: Any):
        if value not in self._enum:
            raise ValidationError("Invalid Type")

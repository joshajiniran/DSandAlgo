from enum import Enum
from uuid import uuid4

from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class UserRole(str, Enum):
    CONSUMER = "consumer"
    ADMIN = "admin"


class User(BaseModel):
    id: uuid4
    role: UserRole

    @property
    def is_admin(self) -> bool:
        return self.role == UserRole.ADMIN


casual_user = User(uuid4(), "admin")
print(casual_user.is_admin)

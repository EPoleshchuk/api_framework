from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import Field, ConfigDict, BaseModel


class UserResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID
    email: str
    full_name: str = Field(alias="fullName")
    roles: List[str]
    verified: bool
    created_at: datetime = Field(alias="createdAt")
    banned: bool

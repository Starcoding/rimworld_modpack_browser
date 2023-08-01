from uuid import UUID
from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    uuid: UUID | None
    nickname: str

    class Config:
        from_attributes = True


class UserSchemaAdd(BaseModel):
    nickname: str
    uuid: UUID | None

from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.core.users.application.schemas.name_info_schema import NameInfoSchema


class UserUpdateSchema(BaseModel):
    uuid: UUID
    login: str
    password: str
    email: EmailStr
    name: NameInfoSchema

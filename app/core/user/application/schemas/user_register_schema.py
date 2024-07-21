from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.core.user.application.schemas.name_info_schema import NameInfoSchema


class UserRegisterSchema(BaseModel):
    login: str
    password: str
    email: EmailStr
    name: NameInfoSchema

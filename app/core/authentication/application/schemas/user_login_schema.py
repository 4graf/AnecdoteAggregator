from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.core.user.application.schemas.name_info_schema import NameInfoSchema


class UserLoginSchema(BaseModel):
    login: str
    password: str

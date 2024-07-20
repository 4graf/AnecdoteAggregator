from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.core.users.application.schemas.name_info_schema import NameInfoSchema
from app.core.users.domain.user_entity import User


class UserReadSchema(BaseModel):
    uuid: UUID
    login: str
    email: EmailStr
    name: NameInfoSchema

    @classmethod
    def from_entity(cls, user: User) -> "UserReadSchema":
        return cls(
            uuid=user.uuid.uuid,
            login=user.login.login,
            email=user.email.email,
            name=NameInfoSchema.from_entity(user.name)
        )

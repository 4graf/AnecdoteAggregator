from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.shared_kernel.db.dao import BaseDao
from app.core.shared_kernel.domain.value_objects import UserUUID
from app.core.users.domain.user_entity import User
from app.core.users.domain.value_object.email import Email
from app.core.users.domain.value_object.login import Login
from app.core.users.domain.value_object.password_hash import PasswordHash
from app.core.users.domain.value_object.user_name import UserName


class UserDao(BaseDao):
    __tablename__ = 'user'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String, unique=True)
    password_hash: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    first_name: Mapped[str] = mapped_column(String)
    second_name: Mapped[str] = mapped_column(String)

    def to_entity(self) -> User:
        return User(
            uuid=UserUUID(self.id),
            login=Login(self.login),
            password_hash=PasswordHash(self.password_hash),
            email=Email(self.email),
            name=UserName(first_name=self.first_name,
                          second_name=self.second_name),
        )

    @classmethod
    def from_entity(cls, user: User) -> "UserDao":
        return cls(
            id=user.uuid.uuid,
            login=user.login.login,
            password_hash=user.password_hash.password_hash,
            email=user.email.email,
            first_name=user.name.first_name,
            second_name=user.name.second_name
        )

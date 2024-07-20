from dataclasses import dataclass

from app.core.shared_kernel.domain.entity import BaseEntity
from app.core.shared_kernel.domain.value_objects import UserUUID
from app.core.user.domain.value_object.email import Email
from app.core.user.domain.value_object.login import Login
from app.core.user.domain.value_object.password_hash import PasswordHash
from app.core.user.domain.value_object.user_name import UserName


@dataclass
class User(BaseEntity):
    uuid: UserUUID
    login: Login
    password_hash: PasswordHash
    email: Email
    name: UserName

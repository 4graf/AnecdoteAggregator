from dataclasses import dataclass

from app.core.shared_kernel.domain.value_objects import UserUUID
from app.core.users.domain.value_object.email import Email
from app.core.users.domain.value_object.user_name import UserName


@dataclass
class User:
    uuid: UserUUID
    email: Email
    name: UserName

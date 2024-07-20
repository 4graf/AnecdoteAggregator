from uuid import uuid4, UUID

from app.core.shared_kernel.domain.value_objects import UserUUID
from app.core.users.application.schemas.user_read_schema import UserReadSchema
from app.core.users.application.schemas.user_register_schema import UserRegisterSchema
from app.core.users.application.schemas.user_update_schema import UserUpdateSchema
from app.core.users.domain.exceptions import UserNotFoundError
from app.core.users.domain.user_entity import User
from app.core.users.domain.user_repository import UserRepository
from app.core.users.domain.value_object.email import Email
from app.core.users.domain.value_object.login import Login
from app.core.users.domain.value_object.password_hash import PasswordHash
from app.core.users.domain.value_object.user_name import UserName


class UserService:
    """

    """

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def register_user(self, data: UserRegisterSchema) -> UserReadSchema:
        if data.name:
            user_name = UserName(first_name=data.name.first_name,
                                 second_name=data.name.second_name)
        else:
            user_name = None

        user = User(
            uuid=UserUUID(uuid4()),
            login=Login(data.login),
            password_hash=PasswordHash(data.password),  # ToDo: добавить хеширование
            email=Email(data.email),
            name=user_name
        )
        await self.user_repository.add(user)

        return UserReadSchema.from_entity(user)

    async def get_user_by_id(self, id_: UUID) -> UserReadSchema:
        user = await self.user_repository.get(id_)
        if not user:
            raise UserNotFoundError

        return UserReadSchema.from_entity(user)

    async def get_all_user(self) -> list[UserReadSchema]:
        users = await self.user_repository.get_all()

        return [UserReadSchema.from_entity(user) for user in users]

    async def update_user(self, data: UserUpdateSchema) -> UserReadSchema:
        if data.name:
            user_name = UserName(first_name=data.name.first_name,
                                 second_name=data.name.second_name)
        else:
            user_name = None

        user = User(
            uuid=UserUUID(data.uuid),
            login=Login(data.login),
            password_hash=PasswordHash(data.password),  # ToDo: добавить хеширование
            email=Email(data.email),
            name=user_name
        )
        await self.user_repository.update(user)

        return UserReadSchema.from_entity(user)

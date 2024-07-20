from app.core.shared_kernel.db.repository import BaseDBRepository
from app.core.users.domain.user_entity import User
from app.core.users.domain.user_repository import UserRepository
from app.core.users.infrastructure.models.user_dao import UserDao


class UserDBRepository(UserRepository, BaseDBRepository[User, UserDao]):
    ...

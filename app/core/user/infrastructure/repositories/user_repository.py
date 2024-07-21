from app.core.shared_kernel.db.dao import BaseDao
from app.core.shared_kernel.db.repository import BaseDBRepository
from app.core.user.domain.user_entity import User
from app.core.user.domain.user_repository import UserRepository
from app.core.user.infrastructure.models.user_dao import UserDao


class UserDBRepository(UserRepository, BaseDBRepository[User]):

    @property
    def dao(self) -> type[BaseDao]:
        return UserDao

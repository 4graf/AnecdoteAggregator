from abc import ABC
from typing import Sequence

from app.core.shared_kernel.domain.repository import BaseRepository
from app.core.user.domain.user_entity import User


class UserRepository(BaseRepository[User], ABC):
    """
    Объявляет интерфейс репозитория для сущности User
    """

    async def get_by_login(self, login: str) -> Sequence[User]:
        filter_map = {"login": login}
        return await self.get_by_filter(filter_map)

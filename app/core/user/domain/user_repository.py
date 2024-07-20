from abc import ABC
from typing import Protocol

from app.core.shared_kernel.domain.repository import BaseRepository
from app.core.user.domain.user_entity import User


class UserRepository(BaseRepository[User], ABC):
    """
    Объявляет интерфейс репозитория для сущности User
    """

    ...

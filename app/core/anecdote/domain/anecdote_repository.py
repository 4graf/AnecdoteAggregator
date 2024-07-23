from abc import ABC, abstractmethod
from typing import Sequence
from uuid import UUID

from app.core.anecdote.domain.anecdote_entity import Anecdote
from app.core.shared_kernel.domain.repository import BaseRepository


class AnecdoteRepository(BaseRepository[Anecdote], ABC):
    """
        Объявляет интерфейс репозитория для сущности Anecdote
    """

    @abstractmethod
    async def get_user_anecdotes(self, user_id: UUID) -> Sequence[Anecdote]:
        ...

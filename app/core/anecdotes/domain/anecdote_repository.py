from abc import ABC

from app.core.anecdotes.domain.anecdote_entity import Anecdote
from app.core.shared_kernel.domain.repository import BaseRepository


class AnecdoteRepository(BaseRepository[Anecdote], ABC):
    """
        Объявляет интерфейс репозитория для сущности Anecdote
    """

    ...

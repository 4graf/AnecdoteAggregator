from abc import ABC

from core.anecdotes.domain.anecdote_entity import Anecdote
from core.shared_kernel.domain.repository import BaseRepository


class AnecdoteRepository(BaseRepository[Anecdote], ABC):
    """
        Объявляет интерфейс репозитория для сущности Anecdote
    """

    ...

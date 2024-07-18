from typing import Protocol


class AnecdoteRepository(DefaultRepository, Protocol):
    """
    Объявляет интерфейс репозитория для сущности Anecdote
    """

    ...

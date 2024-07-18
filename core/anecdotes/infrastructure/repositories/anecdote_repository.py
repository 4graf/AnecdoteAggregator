from core.anecdotes.domain.anecdote_entity import Anecdote
from core.anecdotes.domain.anecdote_repository import AnecdoteRepository
from core.anecdotes.infrastructure.models.anecdote_dao import AnecdoteDao
from core.shared_kernel.db.repository import BaseDBRepository


class AnecdoteDBRepository(AnecdoteRepository, BaseDBRepository[Anecdote, AnecdoteDao]):
    ...

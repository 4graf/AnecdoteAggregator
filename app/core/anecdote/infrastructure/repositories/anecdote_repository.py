from app.core.anecdote.domain.anecdote_entity import Anecdote
from app.core.anecdote.domain.anecdote_repository import AnecdoteRepository
from app.core.anecdote.infrastructure.models.anecdote_dao import AnecdoteDao
from app.core.shared_kernel.db.dao import BaseDao
from app.core.shared_kernel.db.repository import BaseDBRepository


class AnecdoteDBRepository(AnecdoteRepository, BaseDBRepository[Anecdote]):

    @property
    def dao(self) -> type[BaseDao]:
        return AnecdoteDao

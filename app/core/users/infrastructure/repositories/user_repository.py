from app.core.anecdotes.domain.anecdote_entity import Anecdote
from app.core.anecdotes.domain.anecdote_repository import AnecdoteRepository
from app.core.anecdotes.infrastructure.models.anecdote_dao import AnecdoteDao
from app.core.shared_kernel.db.repository import BaseDBRepository


class UserDBRepository(UserRepository, BaseDBRepository[User, UserDao]):
    ...

from core.anecdotes.application.schemas.AnecdoteAddSchema import AnecdoteAddSchema
from core.anecdotes.domain.anecdote_repository import AnecdoteRepository


class AnecdoteService(...):
    """

    """

    # Or __init__ ?
    anecdote_repository: AnecdoteRepository

    def add_anecdote(self, anecdote_add: AnecdoteAddSchema):
        self.anecdote_repository.add(anecdote_add)

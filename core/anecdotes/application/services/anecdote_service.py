from uuid import uuid4, UUID

from core.anecdotes.application.schemas.anecdote_add_schema import AnecdoteAddSchema
from core.anecdotes.application.schemas.anecdote_read_schema import AnecdoteReadSchema
from core.anecdotes.domain.anecdote_entity import Anecdote
from core.anecdotes.domain.anecdote_repository import AnecdoteRepository
from core.anecdotes.domain.value_objects.anecdote_author import AnecdoteAuthor
from core.anecdotes.domain.value_objects.anecdote_text import AnecdoteText
from core.anecdotes.domain.value_objects.likes_count import LikesCount
from core.shared_kernel.domain.value_objects import AnecdoteUUID, UserUUID


class AnecdoteService(...):
    """

    """

    # Or __init__ ?
    anecdote_repository: AnecdoteRepository

    async def add_anecdote(self, data: AnecdoteAddSchema) -> AnecdoteReadSchema:
        anecdote = Anecdote(
            uuid=AnecdoteUUID(uuid4()),
            text=AnecdoteText(data.text),
            author=AnecdoteAuthor(first_name=data.author.first_name,
                                  second_name=data.author.second_name),
            user_id=UserUUID(data.user_id),
            likes_count=LikesCount(0)
        )
        await self.anecdote_repository.add(anecdote)
        return AnecdoteReadSchema.from_entity(anecdote)

    async def get_anecdote_by_id(self, id_: UUID) -> AnecdoteReadSchema:
        anecdote = await self.anecdote_repository.get(id_)
        if not anecdote:
            raise AnecdoteNotFoundError
        return AnecdoteReadSchema.from_entity(anecdote)

    async def get_all_anecdotes(self) -> list[AnecdoteReadSchema]:
        all_anecdotes = await self.anecdote_repository.get_all()
        return [AnecdoteReadSchema.from_entity(anecdote) for anecdote in all_anecdotes]

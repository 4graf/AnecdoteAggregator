from uuid import uuid4, UUID

from app.core.anecdote.application.schemas.anecdote_add_schema import AnecdoteAddSchema
from app.core.anecdote.application.schemas.anecdote_read_schema import AnecdoteReadSchema
from app.core.anecdote.application.schemas.anecdote_update_schema import AnecdoteUpdateSchema
from app.core.anecdote.domain.anecdote_entity import Anecdote
from app.core.anecdote.domain.anecdote_repository import AnecdoteRepository
from app.core.anecdote.domain.exceptions import AnecdoteNotFoundError
from app.core.anecdote.domain.value_objects.anecdote_author import AnecdoteAuthor
from app.core.anecdote.domain.value_objects.anecdote_text import AnecdoteText
from app.core.anecdote.domain.value_objects.likes_count import LikesCount
from app.core.shared_kernel.db.exceptions import EntityExistError
from app.core.shared_kernel.domain.value_objects import AnecdoteUUID, UserUUID


class AnecdoteService:
    """

    """

    def __init__(self, anecdote_repository: AnecdoteRepository):
        self.anecdote_repository = anecdote_repository

    async def add_anecdote(self, data: AnecdoteAddSchema, user_id: UUID) -> AnecdoteReadSchema:
        if data.author:
            anecdote_author = AnecdoteAuthor(first_name=data.author.first_name,
                                             second_name=data.author.second_name)
        else:
            anecdote_author = None

        anecdote = Anecdote(
            uuid=AnecdoteUUID(uuid4()),
            text=AnecdoteText(data.text),
            author=anecdote_author,
            user_id=UserUUID(user_id),
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

    async def get_user_anecdotes(self, user_id: UUID) -> list[AnecdoteReadSchema]:
        anecdotes = await self.anecdote_repository.get_user_anecdotes(user_id)
        return [AnecdoteReadSchema.from_entity(anecdote) for anecdote in anecdotes]

    async def update_anecdote(self, data: AnecdoteUpdateSchema) -> AnecdoteReadSchema:
        if data.author:
            anecdote_author = AnecdoteAuthor(first_name=data.author.first_name,
                                             second_name=data.author.second_name)
        else:
            anecdote_author = None

        anecdote = Anecdote(
            uuid=AnecdoteUUID(data.uuid),
            text=AnecdoteText(data.text),
            author=anecdote_author,
            user_id=UserUUID(data.user_id),
            likes_count=LikesCount(data.likes_count)
        )
        await self.anecdote_repository.update(anecdote)
        return AnecdoteReadSchema.from_entity(anecdote)

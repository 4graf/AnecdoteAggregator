from uuid import UUID

from pydantic import BaseModel

from core.anecdotes.application.schemas.author_info_schema import AuthorInfoSchema
from core.anecdotes.domain.anecdote_entity import Anecdote


class AnecdoteReadSchema(BaseModel):
    uuid: UUID
    text: str
    user_id: UUID
    author: AuthorInfoSchema | None
    likes_count: int

    @classmethod
    def from_entity(cls, entity: Anecdote) -> "AnecdoteReadSchema":
        return cls(
            uuid=entity.uuid.uuid,
            text=entity.text.text,
            user_id=entity.user_id.uuid,
            author=AuthorInfoSchema.from_entity(entity.author),
            likes_count=entity.likes_count.count
        )

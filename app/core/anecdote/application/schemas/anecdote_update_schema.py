from uuid import UUID

from pydantic import BaseModel

from app.core.anecdote.application.schemas.author_info_schema import AuthorInfoSchema


class AnecdoteUpdateSchema(BaseModel):
    uuid: UUID
    user_id: UUID
    text: str
    author: AuthorInfoSchema | None
    likes_count: int

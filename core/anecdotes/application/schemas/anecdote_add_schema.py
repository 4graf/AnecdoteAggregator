from uuid import UUID

from pydantic import BaseModel

from core.anecdotes.application.schemas.author_info_schema import AuthorInfoSchema


class AnecdoteAddSchema(BaseModel):
    text: str
    user_id: UUID
    author: AuthorInfoSchema | None

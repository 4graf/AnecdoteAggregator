from pydantic import BaseModel

from app.core.anecdote.application.schemas.author_info_schema import AuthorInfoSchema


class AnecdoteAddSchema(BaseModel):
    text: str
    author: AuthorInfoSchema | None

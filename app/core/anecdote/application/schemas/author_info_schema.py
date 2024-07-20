from pydantic import BaseModel

from app.core.anecdote.domain.value_objects.anecdote_author import AnecdoteAuthor


class AuthorInfoSchema(BaseModel):
    first_name: str
    second_name: str

    @classmethod
    def from_entity(cls, author: AnecdoteAuthor) -> "AuthorInfoSchema":
        return cls(
            first_name=author.first_name,
            second_name=author.second_name
        )

from dataclasses import dataclass

from app.core.anecdotes.domain.value_objects.anecdote_author import AnecdoteAuthor
from app.core.anecdotes.domain.value_objects.anecdote_text import AnecdoteText
from app.core.anecdotes.domain.value_objects.likes_count import LikesCount
from app.core.shared_kernel.domain.value_objects import AnecdoteUUID, UserUUID


@dataclass
class Anecdote:
    uuid: AnecdoteUUID
    text: AnecdoteText
    author: AnecdoteAuthor | None
    user_id: UserUUID
    likes_count: LikesCount

    def like(self) -> "Anecdote":
        likes_count = LikesCount(self.likes_count.count + 1)
        return self

    def cancel_like(self) -> "Anecdote":
        likes_count = LikesCount(self.likes_count.count - 1)
        return self

from dataclasses import dataclass

from app.core.anecdote.domain.value_objects.anecdote_author import AnecdoteAuthor
from app.core.anecdote.domain.value_objects.anecdote_text import AnecdoteText
from app.core.anecdote.domain.value_objects.likes_count import LikesCount
from app.core.shared_kernel.domain.entity import BaseEntity
from app.core.shared_kernel.domain.value_objects import AnecdoteUUID, UserUUID


@dataclass
class Anecdote(BaseEntity):
    uuid: AnecdoteUUID
    text: AnecdoteText
    author: AnecdoteAuthor | None
    user_id: UserUUID
    likes_count: LikesCount

    def like(self) -> "Anecdote":
        self.likes_count = LikesCount(self.likes_count.count + 1)
        return self

    def cancel_like(self) -> "Anecdote":
        self.likes_count = LikesCount(self.likes_count.count - 1)
        return self

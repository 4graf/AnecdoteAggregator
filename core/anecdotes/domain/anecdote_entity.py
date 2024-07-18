from dataclasses import dataclass

from core.anecdotes.domain.value_objects.anecdote_author import AnecdoteAuthor
from core.anecdotes.domain.value_objects.anecdote_text import AnecdoteText
from core.anecdotes.domain.value_objects.likes_count import LikesCount
from core.shared_kernel.value_objects import AnecdoteUUID, UserUUID


@dataclass
class Anecdote:
    uuid: AnecdoteUUID
    text: AnecdoteText
    author: AnecdoteAuthor
    user_id: UserUUID
    likes_count: LikesCount

    def like(self) -> "Anecdote":
        likes_count = LikesCount(self.likes_count.count + 1)
        return self

    def cancel_like(self) -> "Anecdote":
        likes_count = LikesCount(self.likes_count.count - 1)
        return self

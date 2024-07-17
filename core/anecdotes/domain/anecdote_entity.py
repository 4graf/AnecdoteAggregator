from dataclasses import dataclass
from uuid import UUID


# Перенести в отдельный модуль?
class AnecdoteText:
    ...


class AnecdoteAuthor:
    ...


class LikesCount:
    ...


@dataclass
class Anecdote:
    uuid: UUID
    text: AnecdoteText
    author: AnecdoteAuthor
    likes_count: LikesCount
    # like_status: LikeStatus

    # up like, down like?
    def like(self) -> "Anecdote":
        # if like_status != LikeStatus.not_liked
        likes_count = LikesCount(self.likes_count.count + 1)
        return self

    def cancel_like(self) -> "Anecdote":
        # if like_status != LikeStatus.liked
        likes_count = LikesCount(self.likes_count.count - 1)
        return self

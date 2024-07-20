from uuid import UUID

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.core.anecdotes.domain.anecdote_entity import Anecdote
from app.core.anecdotes.domain.value_objects.anecdote_author import AnecdoteAuthor
from app.core.anecdotes.domain.value_objects.anecdote_text import AnecdoteText
from app.core.anecdotes.domain.value_objects.likes_count import LikesCount
from app.core.shared_kernel.db.dao import BaseDao
from app.core.shared_kernel.domain.value_objects import UserUUID, AnecdoteUUID


class AnecdoteDao(BaseDao):
    __tablename__ = 'anecdote'

    id: Mapped[UUID] = mapped_column(primary_key=True)  # server_default=text('gen_random_uuid()') ?
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    text: Mapped[str] = mapped_column(String)
    author_first_name: Mapped[str] = mapped_column(String, nullable=True)
    author_second_name: Mapped[str] = mapped_column(String, nullable=True)
    likes_count: Mapped[int] = mapped_column(Integer)

    # user: Mapped["UserDao"] = relationship(back_populates="anecdotes")

    def to_entity(self) -> Anecdote:
        return Anecdote(
            uuid=AnecdoteUUID(self.id),
            user_id=UserUUID(self.user_id),
            text=AnecdoteText(self.text),
            author=AnecdoteAuthor(first_name=self.author_first_name,
                                  second_name=self.author_second_name),
            likes_count=LikesCount(self.likes_count)
        )

    @classmethod
    def from_entity(cls, anecdote: Anecdote) -> "AnecdoteDao":
        return cls(
            id=anecdote.uuid.uuid,
            user_id=anecdote.user_id.uuid,
            text=anecdote.text.text,
            author_first_name=anecdote.author.first_name,
            author_second_name=anecdote.author.second_name,
            likes_count=anecdote.likes_count
        )

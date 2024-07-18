from uuid import UUID

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from core.anecdotes.domain.anecdote_entity import Anecdote
from core.shared_kernel.db.dao import BaseDao


class AnecdoteDao(BaseDao):
    __tablename__ = 'anecdote'

    id: Mapped[UUID] = mapped_column(primary_key=True)  # server_default=text('gen_random_uuid()') ?
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    text: Mapped[str] = mapped_column(String)
    author: Mapped[str] = mapped_column(String, nullable=True)
    likes_count: Mapped[int] = mapped_column(Integer)

    # user: Mapped["UserDao"] = relationship(back_populates="anecdotes")

    def to_entity(self) -> Anecdote:
        return Anecdote(
            uuid=self.id,
            user_id=self.user_id,
            text=self.text,
            author=self.author,
            likes_count=self.likes_count
        )

    @staticmethod
    def from_entity(anecdote: Anecdote) -> "AnecdoteDao":
        return AnecdoteDao(
            id=anecdote.uuid,
            user_id=anecdote.user_id,
            text=anecdote.text,
            author=anecdote.author,
            likes_count=anecdote.likes_count
        )

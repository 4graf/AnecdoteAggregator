from dataclasses import dataclass

from core.anecdotes.domain.value_objects.anecdote_text import AnecdoteText
from core.shared_kernel.value_objects import UserUUID


@dataclass
class AnecdoteAddSchema:
    text: AnecdoteText
    user_uuid: UserUUID

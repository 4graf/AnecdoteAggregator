from dataclasses import dataclass

from core.shared_kernel.value_objects import AnecdoteUUID, UserUUID


@dataclass
class User:
    uuid: UserUUID

    liked_anecdote_ids: list[AnecdoteUUID]


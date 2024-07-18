from dataclasses import dataclass
from uuid import UUID


@dataclass
class UserUUID:
    uuid: UUID


@dataclass
class AnecdoteUUID:
    uuid: UUID


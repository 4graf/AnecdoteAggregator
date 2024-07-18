from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Sequence
from uuid import UUID

Entity = TypeVar('Entity')


class BaseRepository(ABC, Generic[Entity]):
    """
        Абстрактный репозиторий с generic сущности
    """

    @abstractmethod
    async def add(self, entity: Entity | list[Entity]) -> Entity | Sequence[Entity]:
        ...

    @abstractmethod
    async def update(self, entity: Entity) -> Entity:
        ...

    @abstractmethod
    async def get(self, id_: UUID) -> Entity | None:
        ...

    @abstractmethod
    async def get_all(self) -> Sequence[Entity]:
        ...

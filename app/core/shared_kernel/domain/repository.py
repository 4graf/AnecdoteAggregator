from abc import ABC, abstractmethod
from typing import Sequence, Generic, TypeVar
from uuid import UUID

from app.core.shared_kernel.domain.entity import BaseEntity

Entity = TypeVar("Entity", bound=BaseEntity)


class BaseRepository(ABC, Generic[Entity]):
    """
        Абстрактный репозиторий
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
    async def get_by_filter(self, filter_map: dict) -> Sequence[Entity]:
        ...

    @abstractmethod
    async def get_all(self) -> Sequence[Entity]:
        ...

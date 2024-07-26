from abc import ABC, abstractmethod
from typing import Sequence, TypeVar
from uuid import UUID

from sqlalchemy import insert, update, select
from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.shared_kernel.db.dao import BaseDao
from app.core.shared_kernel.db.exceptions import EntityExistError
from app.core.shared_kernel.domain.entity import BaseEntity
from app.core.shared_kernel.domain.repository import BaseRepository

Entity = TypeVar("Entity", bound=BaseEntity)


class BaseDBRepository(BaseRepository[Entity], ABC):

    @property
    @abstractmethod
    def dao(self) -> type[BaseDao]:
        ...
    
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, entity: Entity | list[Entity]) -> Entity | Sequence[Entity]:
        add_dao = self.dao.from_entity(entity)
        stmt = (
            insert(self.dao)
            .values(add_dao.to_dict())
            .returning(self.dao)
        )
        try:
            result = await self.session.execute(stmt)
            result = result.scalars().all()
            await self.session.commit()
        except IntegrityError as e:
            raise EntityExistError from e
        return result[0].to_entity() if len(result) == 1 else [dao.to_entity() for dao in result]

    async def update(self, entity: Entity) -> Entity:
        update_dao = self.dao.from_entity(entity)
        stmt = (
            update(self.dao)
            .values(update_dao.to_dict())
            .filter_by(id=update_dao.id)
            .returning(self.dao)
        )

        result = await self.session.execute(stmt)
        result = result.scalar_one()
        await self.session.commit()
        return result.to_entity()

    async def get(self, id_: UUID) -> Entity | None:
        stmt = (
            select(self.dao)
            .filter_by(id=id_)
        )

        result = await self.session.execute(stmt)
        result = result.scalar_one_or_none()
        return result.to_entity() if result else None

    async def get_by_filter(self, filter_map: dict) -> Sequence[Entity]:
        stmt = (
            select(self.dao)
            .filter_by(**filter_map)
        )

        try:
            result = await self.session.execute(stmt)
            result = result.scalars().all()
        except NoResultFound:
            return []

        return [dao.to_entity() for dao in result]

    async def get_all(self) -> Sequence[Entity]:
        stmt = (
            select(self.dao)
        )

        try:
            result = await self.session.execute(stmt)
            result = result.scalars().all()
        except NoResultFound:
            return []

        return [dao.to_entity() for dao in result]

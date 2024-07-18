from abc import ABC
from typing import TypeVar, Generic, Sequence, Any
from uuid import UUID

from sqlalchemy import insert, update, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from core.shared_kernel.domain.repository import BaseRepository

Entity = TypeVar('Entity')
Dao = TypeVar('Dao')


class BaseDBRepository(BaseRepository[Entity], Generic[Entity, Dao]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, entity: Entity | list[Entity]) -> Entity | Sequence[Entity]:
        stmt = (
            insert(Dao)
            .values(entity)
            .returning(Dao)
        )

        result = await self.session.execute(stmt)
        result = result.scalars().all()
        await self.session.commit()
        return result[0].to_entity() if len(result) == 1 else [dao.to_entity() for dao in result]

    async def update(self, entity: Entity) -> Entity:
        update_data = Dao.from_entity(entity)
        stmt = (
            update(Dao)
            .values(update_data)
            # .filter(Dao.id == id_)
            .filter_by(id=update_data.id)
            .returning(Dao)
        )

        result = await self.session.execute(stmt)
        result = result.scalar_one()
        await self.session.commit()
        return result.to_entity()

    async def get(self, id_: UUID) -> Entity | None:
        stmt = (
            select(Dao)
            .filter_by(id=id_)
        )

        result = await self.session.execute(stmt)
        result = result.scalar_one_or_none()
        return result.to_entity() if result else None

    async def get_all(self) -> Sequence[Entity]:
        stmt = (
            select(Dao)
        )

        try:
            result = await self.session.execute(stmt)
            result = result.scalars().all()
        except NoResultFound:
            return []

        return [dao.to_entity() for dao in result]

from abc import abstractmethod

from sqlalchemy.orm import DeclarativeBase

from app.core.shared_kernel.domain.entity import BaseEntity


class BaseDao(DeclarativeBase):
    """
    Базовая модель для SQLAlchemy моделей.
    """

    __abstract__ = True

    @abstractmethod
    def to_entity(self) -> BaseEntity:
        ...

    @staticmethod
    @abstractmethod
    def from_entity(entity: BaseEntity) -> "BaseDao":
        ...

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

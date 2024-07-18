from abc import abstractmethod, ABC

from sqlalchemy.orm import DeclarativeBase

from app.core.shared_kernel.domain.entity import BaseEntity


class BaseDao(ABC, DeclarativeBase):
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
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from app.settings import DatabaseSettings

settings = DatabaseSettings()
engine = create_async_engine(settings.postgres_url.unicode_string(), echo=False)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_db_session() -> AsyncSession:
    """
    Получает асинхронную сессию для взаимодействия с базой данных.

        :return: Асинхронная сессия SQLAlchemy.
    """

    async with async_session_maker() as session:
        try:
            yield session
        except Exception:
            ...
            await session.rollback()
            raise
        finally:
            await session.close()

"""
API-маршрут для проверки работоспособности приложения.
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.core.shared_kernel.db.dependencies import get_async_db_session

healthcheck_router = APIRouter()


@healthcheck_router.get("/healthcheck", status_code=status.HTTP_200_OK)
async def do_healthcheck(session: Annotated[AsyncSession, Depends(get_async_db_session)]) \
        -> int:
    """
    Проводит проверку работоспособности приложения.

        :param session: Сессия базы данных.
        :return: Статус код ответа.
    """
    await session.execute(select())
    return status.HTTP_200_OK

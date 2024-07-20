from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.anecdote.application.services.anecdote_service import AnecdoteService
from app.core.anecdote.infrastructure.repositories.anecdote_repository import AnecdoteDBRepository
from app.core.shared_kernel.db.dependencies import get_async_db_session


async def get_anecdote_service(session: AsyncSession = Depends(get_async_db_session)) -> AnecdoteService:
    anecdote_repository = AnecdoteDBRepository(session)
    return AnecdoteService(anecdote_repository)

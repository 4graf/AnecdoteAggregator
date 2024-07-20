from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.shared_kernel.db.dependencies import get_async_db_session
from app.core.user.application.services.user_service import UserService
from app.core.user.infrastructure.repositories.user_repository import UserDBRepository


async def get_user_service(session: AsyncSession = Depends(get_async_db_session)) -> UserService:
    user_repository = UserDBRepository(session)
    return UserService(user_repository)

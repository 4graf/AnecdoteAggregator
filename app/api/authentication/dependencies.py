from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.shared_kernel.db.dependencies import get_async_db_session
from app.core.user.application.authentication.services.authentication_service import AuthenticationService
from app.core.user.infrastructure.repositories.user_repository import UserDBRepository


async def get_authentication_service(session: AsyncSession = Depends(get_async_db_session)) -> AuthenticationService:
    user_repository = UserDBRepository(session)
    return AuthenticationService(user_repository)

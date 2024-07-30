from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.shared_kernel.db.dependencies import get_async_db_session
from app.core.user.application.authentication.schemas.user_from_token_schema import UserFromTokenSchema
from app.core.user.application.authentication.services.token_service import TokenService
from app.core.user.application.schemas.user_read_schema import UserReadSchema
from app.core.user.application.services.user_service import UserService
from app.core.user.infrastructure.repositories.user_repository import UserDBRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")  # ToDo: исправить хардкод пути эндпоинта


async def get_current_user(access_token: Annotated[str, Depends(oauth2_scheme)]) -> UserFromTokenSchema:
    return TokenService.decode_access_token(access_token)


async def get_current_user_info(access_token: Annotated[str, Depends(oauth2_scheme)],
                                session: AsyncSession = Depends(get_async_db_session)) -> UserReadSchema:
    user_repository = UserDBRepository(session)
    user_service = UserService(user_repository)

    token_data = TokenService.decode_access_token(access_token)

    user = await user_service.get_user_by_id(token_data.uuid)
    return user

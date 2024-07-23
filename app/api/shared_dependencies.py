from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.user.application.authentication.schemas.user_from_token_schema import UserFromTokenSchema
from app.core.user.application.authentication.services.token_service import TokenService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")  # ToDo: исправить хардкод пути эндпоинта


async def get_current_user(access_token: Annotated[str, Depends(oauth2_scheme)]) -> UserFromTokenSchema:
    return TokenService.decode_access_token(access_token)

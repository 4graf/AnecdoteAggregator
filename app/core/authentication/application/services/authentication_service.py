from datetime import datetime, timedelta
from uuid import uuid4

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

from app.core.authentication.application.schemas.access_token_schema import AccessTokenSchema
from app.core.authentication.application.schemas.authentication_tokens_schema import AuthenticationTokensSchema
from app.core.authentication.application.schemas.token_payload_schema import TokenPayloadSchema
from app.core.authentication.application.schemas.user_login_schema import UserLoginSchema
from app.core.authentication.application.services.token_service import TokenService
from app.settings import JWTSettings

settings = JWTSettings()


class AuthenticationService:
    """

    """

    async def login(self, user_login: UserLoginSchema) -> AuthenticationTokensSchema:
        user = await user_service.get_user_by_login(user_login.login)
        access_token = TokenService.create_access_token({"user_id": user.uuid})
        return AuthenticationTokensSchema(access_token=access_token)



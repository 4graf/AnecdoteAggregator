from datetime import datetime, timedelta
from uuid import uuid4, UUID

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

from app.core.user.application.authentication.exceptions import TokenExpiredException, TokenCorruptedException
from app.core.user.application.authentication.schemas.access_token_schema import AccessTokenSchema
from app.core.user.application.authentication.schemas.user_from_token_schema import UserFromTokenSchema
from app.core.user.application.authentication.schemas.user_to_token_schema import UserToTokenSchema
from app.settings import AuthenticationSettings

settings = AuthenticationSettings()


class TokenService:
    """

    """

    @classmethod
    def create_access_token(cls, data: UserToTokenSchema) -> AccessTokenSchema:
        to_encode = data.model_dump().copy()
        expire = datetime.now() + timedelta(minutes=settings.access_expiration)
        to_encode['exp'] = expire
        token_id = str(uuid4())
        to_encode['token_id'] = token_id
        encoded_jwt = jwt.encode(to_encode, settings.access_secret_key, settings.jwt_algorithm)

        return AccessTokenSchema(access_token=encoded_jwt,
                                 token_type="Bearer")

    @classmethod
    def decode_access_token(cls, access_token: str) -> UserFromTokenSchema:
        try:
            data = jwt.decode(access_token, settings.access_secret_key, [settings.jwt_algorithm])
        except ExpiredSignatureError as e:
            raise TokenExpiredException from e
        except InvalidTokenError as e:
            raise TokenCorruptedException from e

        user = UserFromTokenSchema(uuid=UUID(data['uuid']),
                                   token_id=data['token_id'])
        return user

    @classmethod
    def refresh_access_token(cls, ):
        ...

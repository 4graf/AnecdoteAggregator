from datetime import datetime, timedelta
from uuid import uuid4

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

from app.core.authentication.application.schemas.access_token_schema import AccessTokenSchema
from app.core.authentication.application.schemas.token_payload_schema import TokenPayloadSchema
from app.settings import JWTSettings

settings = JWTSettings()


class TokenService:
    """

    """

    @classmethod
    def create_access_token(cls, data: dict) -> AccessTokenSchema:
        to_encode = data.copy()
        expire = datetime.now() + timedelta(minutes=settings.access_expiration)
        to_encode['exp'] = expire
        token_id = str(uuid4())
        to_encode['token_id'] = token_id
        encoded_jwt = jwt.encode(to_encode, settings.access_secret_key, settings.algorithm)

        return AccessTokenSchema(token=TokenPayloadSchema(sub=encoded_jwt,
                                                          exp=expire,
                                                          token_id=token_id),
                                 token_type="Bearer")

    @classmethod
    def decode_access_token(cls, access_token: AccessTokenSchema) -> dict:
        try:
            data = jwt.decode(access_token.token.sub, settings.access_secret_key, [settings.algorithm])
        except ExpiredSignatureError as exc:
            raise TokenExpiredException from exc
        except InvalidTokenError as exc:
            raise TokenCorruptedException from exc

        return data

    @classmethod
    def refresh_access_token(cls, ):
        ...

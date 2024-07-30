from pydantic import BaseModel

from app.core.user.application.authentication.schemas.access_token_schema import AccessTokenSchema
from app.core.user.application.authentication.schemas.refresh_token_schema import RefreshTokenSchema


class AuthenticationTokensSchema(BaseModel):
    access_token: AccessTokenSchema
    refresh_token: RefreshTokenSchema

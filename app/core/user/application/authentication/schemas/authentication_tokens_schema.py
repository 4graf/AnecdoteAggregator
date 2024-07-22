from dataclasses import dataclass

from app.core.user.application.authentication.schemas.access_token_schema import AccessTokenSchema
from app.core.shared_kernel.domain.entity import BaseEntity


@dataclass
class AuthenticationTokensSchema(BaseEntity):
    access_token: AccessTokenSchema
    # refresh_token: RefreshTokenSchema

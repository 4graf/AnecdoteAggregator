from dataclasses import dataclass

from pydantic import BaseModel

from app.core.user.application.authentication.schemas.token_payload_schema import TokenPayloadSchema


@dataclass
class RefreshTokenSchema(BaseModel):
    token: TokenPayloadSchema
    token_type: str
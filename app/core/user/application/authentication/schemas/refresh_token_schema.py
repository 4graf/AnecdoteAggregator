from pydantic import BaseModel


class RefreshTokenSchema(BaseModel):
    refresh_token: str
    token_type: str

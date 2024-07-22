from datetime import datetime

from pydantic import BaseModel


class TokenPayloadSchema(BaseModel):
    sub: str
    exp: datetime
    token_id: str


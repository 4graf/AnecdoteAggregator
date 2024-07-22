from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel


@dataclass
class TokenPayloadSchema(BaseModel):
    sub: str
    exp: datetime
    token_id: str

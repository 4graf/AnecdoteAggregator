from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    login: str
    password: str

from pydantic import BaseModel


class UserToTokenSchema(BaseModel):
    uuid: str
    # role: UserRole
from uuid import UUID

from pydantic import BaseModel


class UserFromTokenSchema(BaseModel):
    uuid: UUID
    token_id: str
    # role: UserRole  # ToDo: Добавить роли пользователей

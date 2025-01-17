from uuid import uuid4

from app.core.shared_kernel.db.exceptions import EntityExistsError
from app.core.shared_kernel.domain.value_objects import UserUUID
from app.core.user.application.authentication.exceptions import WrongPasswordError
from app.core.user.application.authentication.schemas.authentication_tokens_schema import AuthenticationTokensSchema
from app.core.user.application.authentication.schemas.user_login_schema import UserLoginSchema
from app.core.user.application.authentication.schemas.user_to_token_schema import UserToTokenSchema
from app.core.user.application.authentication.services.password_service import PasswordService
from app.core.user.application.authentication.services.token_service import TokenService
from app.core.user.application.schemas.user_create_schema import UserCreateSchema
from app.core.user.domain.exceptions import UserNotFoundError, UserExistsError
from app.core.user.domain.user_entity import User
from app.core.user.domain.user_repository import UserRepository
from app.core.user.domain.value_object.email import Email
from app.core.user.domain.value_object.login import Login
from app.core.user.domain.value_object.password_hash import PasswordHash
from app.core.user.domain.value_object.user_name import UserName
from app.settings import AuthenticationSettings

settings = AuthenticationSettings()


class AuthenticationService:
    """

    """
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def register_user(self, data: UserCreateSchema) -> AuthenticationTokensSchema:
        if data.name:
            user_name = UserName(first_name=data.name.first_name,
                                 second_name=data.name.second_name)
        else:
            user_name = None

        try:
            user = User(
                uuid=UserUUID(uuid4()),
                login=Login(data.login),
                password_hash=PasswordHash(PasswordService.hash_password(data.password)),
                email=Email(data.email),
                name=user_name
            )
            await self.user_repository.add(user)
        except EntityExistsError as e:
            raise UserExistsError from e

        user_to_token = UserToTokenSchema(uuid=str(user.uuid.uuid))
        access_token = TokenService.create_access_token(user_to_token)
        refresh_token = TokenService.create_refresh_token(user_to_token)
        return AuthenticationTokensSchema(access_token=access_token,
                                          refresh_token=refresh_token)

    async def login(self, user_login: UserLoginSchema) -> AuthenticationTokensSchema:
        users = await self.user_repository.get_by_login(user_login.login)
        if not users:
            raise UserNotFoundError
        user = users[0]
        if not PasswordService.validate_password(user_login.password, user.password_hash.password_hash):
            raise WrongPasswordError

        user_to_token = UserToTokenSchema(uuid=str(user.uuid.uuid))
        access_token = TokenService.create_access_token(user_to_token)
        refresh_token = TokenService.create_refresh_token(user_to_token)
        return AuthenticationTokensSchema(access_token=access_token,
                                          refresh_token=refresh_token)

    async def logout(self):
        #  ToDo: Добавить Redis и вести учёт деактивированных токенов
        ...

    async def refresh(self, refresh_token: str) -> AuthenticationTokensSchema:
        user_data = TokenService.decode_refresh_token(refresh_token)

        #  ToDo: удаление всего семейства старых токенов

        if not await self.user_repository.get(user_data.uuid):
            raise UserNotFoundError

        user_to_token = UserToTokenSchema(uuid=str(user_data.uuid))
        new_access_token = TokenService.create_access_token(user_to_token)
        new_refresh_token = TokenService.create_refresh_token(user_to_token)

        return AuthenticationTokensSchema(access_token=new_access_token,
                                          refresh_token=new_refresh_token)

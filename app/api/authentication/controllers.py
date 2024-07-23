"""
API-маршруты для управления пользователями.
"""
from typing import Annotated

from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from app.api.authentication.dependencies import get_authentication_service
from app.core.user.application.authentication.schemas.access_token_schema import AccessTokenSchema
from app.core.user.application.authentication.schemas.user_login_schema import UserLoginSchema
from app.core.user.application.authentication.services.authentication_service import AuthenticationService
from app.core.user.application.schemas.user_create_schema import UserCreateSchema

authentication_router = APIRouter()


@authentication_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreateSchema,
                        authentication_service: Annotated[AuthenticationService, Depends(get_authentication_service)],
                        response: Response) \
        -> AccessTokenSchema:
    """
    Регистрирует нового пользователя

        :param user: Данные нового пользователя.
        :param authentication_service: Сервис для работы с аутентификацией.
        :param response: Объект ответа для установления cookies.
        :return: Данные пользователя.
    """
    tokens = await authentication_service.register_user(data=user)
    # response.set_cookie(key='refresh_token',
    #                     value=tokens.refresh_token,
    #                     httponly=True,
    #                     samesite='lax')
    access_token = tokens.access_token
    return access_token


@authentication_router.post("/login", status_code=status.HTTP_200_OK)
async def login(authentication_service: Annotated[AuthenticationService, Depends(get_authentication_service)],
                form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                response: Response) \
        -> AccessTokenSchema:
    """
    Аутентифицирует пользователя

        :param authentication_service: Сервис для работы с аутентификацией.
        :param form_data: Данные для аутентификации пользователя.
        :param response: Объект ответа для установления cookies.
        :return: Данные пользователя.
    """
    user_login = UserLoginSchema(login=form_data.username,
                                 password=form_data.password)
    tokens = await authentication_service.login(user_login=user_login)
    # response.set_cookie(key='refresh_token',
    #                     value=tokens.refresh_token,
    #                     httponly=True,
    #                     samesite='lax')
    access_token = tokens.access_token
    return access_token


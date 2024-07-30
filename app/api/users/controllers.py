"""
API-маршруты для управления пользователями.
"""
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status
from starlette.exceptions import HTTPException

from app.api.http_errors import ResourceNotFoundByIDError
from app.api.shared_dependencies import get_current_user
from app.api.users.dependencies import get_user_service
from app.core.user.application.authentication.schemas.user_from_token_schema import UserFromTokenSchema
from app.core.user.application.schemas.user_read_schema import UserReadSchema
from app.core.user.application.services.user_service import UserService
from app.core.user.domain.exceptions import UserNotFoundError

user_router = APIRouter()


@user_router.get("/all", status_code=status.HTTP_200_OK)
async def get_users(current_user: Annotated[UserFromTokenSchema, Depends(get_current_user)],
                    user_service: Annotated[UserService, Depends(get_user_service)]) \
        -> list[UserReadSchema]:
    """
    Получает всех пользователей

        :param current_user: Данные текущего пользователя.
        :param user_service: Сервис для работы с пользователями.
        :return: Данные пользователя.
    """
    ...  # ToDo: добавить проверку на администратора

    return await user_service.get_all_user()


@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: UUID,
                   current_user: Annotated[UserFromTokenSchema, Depends(get_current_user)],
                   user_service: Annotated[UserService, Depends(get_user_service)]) \
        -> UserReadSchema:
    """
    Получает пользователя по его идентификатору

        :param user_id: Идентификатор пользователя.
        :param current_user: Данные текущего пользователя.
        :param user_service: Сервис для работы с пользователями.
        :return: Данные пользователя.
    """
    try:
        user = await user_service.get_user_by_id(user_id)
    except UserNotFoundError as e:
        raise ResourceNotFoundByIDError(exception_msg=str(e)) from e

    return user

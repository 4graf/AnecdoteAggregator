"""
API-маршруты для управления пользователями.
"""
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status
from starlette.exceptions import HTTPException

from app.api.users.dependencies import get_user_service
from app.core.user.application.schemas.user_read_schema import UserReadSchema
from app.core.user.application.services.user_service import UserService
from app.core.user.domain.exceptions import UserNotFoundError

user_router = APIRouter()


@user_router.get("/all", status_code=status.HTTP_200_OK)
async def get_users(user_service: Annotated[UserService, Depends(get_user_service)]) \
        -> list[UserReadSchema]:
    """
    Получает всех пользователей

        :param user_service: Сервис для работы с пользователями.
        :return: Данные пользователя.
    """
    return await user_service.get_all_user()


@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: UUID,
                   user_service: Annotated[UserService, Depends(get_user_service)]) \
        -> UserReadSchema:
    """
    Получает пользователя по его идентификатору

        :param user_id: Идентификатор пользователя.
        :param user_service: Сервис для работы с пользователями.
        :return: Данные пользователя.
    """
    try:
        user = await user_service.get_user_by_id(user_id)
    except UserNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=str(exc)) from exc

    return user

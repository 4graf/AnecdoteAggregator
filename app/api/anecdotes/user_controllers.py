"""
API-маршруты для управления пользователя своими анекдотами.
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from app.api.anecdotes.dependencies import get_anecdote_service
from app.api.shared_dependencies import get_current_user
from app.core.anecdote.application.schemas.anecdote_read_schema import AnecdoteReadSchema
from app.core.anecdote.application.services.anecdote_service import AnecdoteService
from app.core.user.application.authentication.schemas.user_from_token_schema import UserFromTokenSchema

anecdote_user_router = APIRouter()


@anecdote_user_router.get("/all", status_code=status.HTTP_200_OK)
async def get_user_anecdotes(anecdote_service: Annotated[AnecdoteService, Depends(get_anecdote_service)],
                             current_user: Annotated[UserFromTokenSchema, Depends(get_current_user)]) \
        -> list[AnecdoteReadSchema]:
    """
    Получает все анекдоты пользователя

        :param anecdote_service: Сервис для работы с анекдотами.
        :param current_user: Данные текущего пользователя.
        :return: Данные анекдотов.
    """
    return await anecdote_service.get_user_anecdotes(current_user.uuid)

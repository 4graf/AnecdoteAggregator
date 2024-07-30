"""
API-маршруты для управления анекдотами.
"""
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status
from starlette.exceptions import HTTPException

from app.api.anecdotes.dependencies import get_anecdote_service
from app.api.http_errors import RequestParamValidationError
from app.api.shared_dependencies import get_current_user
from app.core.anecdote.application.schemas.anecdote_add_schema import AnecdoteAddSchema
from app.core.anecdote.application.schemas.anecdote_read_schema import AnecdoteReadSchema
from app.core.anecdote.application.services.anecdote_service import AnecdoteService
from app.core.anecdote.domain.exceptions import AnecdoteNotFoundError, AnecdoteError
from app.core.user.application.authentication.schemas.user_from_token_schema import UserFromTokenSchema

anecdote_router = APIRouter()


@anecdote_router.post("/add", status_code=status.HTTP_201_CREATED)
async def add_anecdote(anecdote: AnecdoteAddSchema,
                       current_user: Annotated[UserFromTokenSchema, Depends(get_current_user)],
                       anecdote_service: Annotated[AnecdoteService, Depends(get_anecdote_service)]) \
        -> AnecdoteReadSchema:
    """
    Создаёт новый анекдот

        :param anecdote: Данные нового анекдота.
        :param current_user: Данные текущего пользователя.
        :param anecdote_service: Сервис для работы с анекдотами.
        :return: Данные анекдота.
    """
    try:
        return await anecdote_service.add_anecdote(data=anecdote, user_id=current_user.uuid)
    except AnecdoteError as e:
        raise RequestParamValidationError(exception_msg=str(e)) from e


@anecdote_router.get("/all", status_code=status.HTTP_200_OK)
async def get_anecdotes(anecdote_service: Annotated[AnecdoteService, Depends(get_anecdote_service)]) \
        -> list[AnecdoteReadSchema]:
    """
    Получает все анекдоты

        :param anecdote_service: Сервис для работы с анекдотами.
        :return: Данные анекдотов.
    """
    return await anecdote_service.get_all_anecdotes()


@anecdote_router.get("/{anecdote_id}", status_code=status.HTTP_200_OK)
async def get_anecdote(anecdote_id: UUID,
                       anecdote_service: Annotated[AnecdoteService, Depends(get_anecdote_service)]) \
        -> AnecdoteReadSchema:
    """
    Получает анекдот по его идентификатору

        :param anecdote_id: Идентификатор анекдота.
        :param anecdote_service: Сервис для работы с анекдотами.
        :return: Данные анекдота.
    """
    try:
        anecdote = await anecdote_service.get_anecdote_by_id(anecdote_id)
    except AnecdoteNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=str(exc)) from exc

    return anecdote

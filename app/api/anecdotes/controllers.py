"""
API-маршруты для управления пользователями.
"""
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status

from app.api.anecdotes.dependencies import get_anecdote_service
from app.core.anecdotes.application.schemas.anecdote_add_schema import AnecdoteAddSchema
from app.core.anecdotes.application.schemas.anecdote_read_schema import AnecdoteReadSchema
from app.core.anecdotes.application.services.anecdote_service import AnecdoteService

anecdote_router = APIRouter()


@anecdote_router.post("/add", status_code=status.HTTP_200_OK)
async def add_anecdote(anecdote: AnecdoteAddSchema,
                       # user: ...,
                       anecdote_service: Annotated[AnecdoteService, Depends(get_anecdote_service)]) \
        -> AnecdoteReadSchema:
    """
    Создаёт новый анекдот

        :param anecdote: Данные нового анекдота.
        :param anecdote_service: Сервис для работы с анекдотами.
        :return: Данные анекдота.
    """
    user_id = ...
    return await anecdote_service.add_anecdote(data=anecdote, user_id=user_id)


@anecdote_router.get("/all", status_code=status.HTTP_200_OK)
async def get_anecdotes(anecdote_service: Annotated[AnecdoteService, Depends(get_anecdote_service)]) \
        -> list[AnecdoteReadSchema]:
    """
    Получает все анекдоты

        :param anecdote_service: Сервис для работы с анекдотами.
        :return: Данные анекдотов.
    """
    return await anecdote_service.get_all_anecdotes()


@anecdote_router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_anecdote(anecdote_id: UUID,
                       anecdote_service: Annotated[AnecdoteService, Depends(get_anecdote_service)]) \
        -> AnecdoteReadSchema:
    """
    Получает анекдот по его идентификатору

        :param anecdote_id: Идентификатор анекдота.
        :param anecdote_service: Сервис для работы с анекдотами.
        :return: Данные анекдота.
    """
    # try:
    return await anecdote_service.get_anecdote_by_id(anecdote_id)
    # except UserNotFoundException as exc:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=str(exc)) from exc

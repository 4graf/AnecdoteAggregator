from fastapi import APIRouter

from app.api.anecdotes.controllers import anecdote_router
from app.api.authentication.controllers import authentication_router
from app.api.users.controllers import user_router

api_v1_router = APIRouter(prefix="/v1")

api_v1_router.include_router(anecdote_router, prefix="/anecdote", tags=["Anecdote"])
api_v1_router.include_router(user_router, prefix="/user", tags=["User"])
api_v1_router.include_router(authentication_router, prefix="/auth", tags=["Authentication"])

api_routers = [api_v1_router]

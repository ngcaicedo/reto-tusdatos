from fastapi import APIRouter
from .endpoints import auth, user

api_router = APIRouter()
api_router.include_router(auth.auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(user.user_router, prefix="/users", tags=["users"])

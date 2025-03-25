from fastapi import APIRouter
from .endpoints import auth, user, event, assistant

api_router = APIRouter()
api_router.include_router(auth.auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(user.user_router, prefix="/users", tags=["users"])
api_router.include_router(event.event_router, prefix="/events", tags=["users"])
api_router.include_router(assistant.assistant_router, prefix="/assistants", tags=["users"])

from fastapi import APIRouter

from ._events import router as events_router
from ._html import router as html_router


api_router = APIRouter(prefix="/api/v1")

api_router.include_router(events_router)


__all__ = ["api_router", "html_router"]

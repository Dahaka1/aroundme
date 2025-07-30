from fastapi import APIRouter

from ._events import router as events_router


router = APIRouter(prefix="/api/v1")

router.include_router(events_router)


__all__ = ["router"]

from fastapi import APIRouter

from services import EventsService


router = APIRouter(prefix="/events")

service = EventsService()


@router.get("")
async def get_events(lat: float, lon: float):
    return await service.get_events(lat, lon)

import random

from pydantic import BaseModel

from uuid import UUID, uuid4
from enum import StrEnum

from utils.rand import generate_sentence, generate_name


class _EventGroupEnum(StrEnum):
    sport = "sport"
    party = "party"
    master_class = "master_class"


class _Event(BaseModel):
    id: UUID
    name: str
    group: _EventGroupEnum
    lat: float
    lon: float
    description: str


class EventsResponse(BaseModel):
    events: list[_Event]


class EventsService:
    _EVENTS_RANDOM_AMOUNT = 35

    async def get_events(self, lat: float, lon: float) -> EventsResponse:
        return EventsResponse(events=[
            _Event(
                id=uuid4(),
                name=generate_name(),
                group=random.choice(list(_EventGroupEnum)),
                lat=lat + random.uniform(-0.003, 0.003),
                lon=lon + random.uniform(-0.003, 0.003),
                description=generate_sentence()
            )

            for _ in range(self._EVENTS_RANDOM_AMOUNT)
        ])

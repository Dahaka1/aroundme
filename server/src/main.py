from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.http import http_router

from contextlib import asynccontextmanager

from utils.logging import get_logger

logger = get_logger()

app = FastAPI()
app.include_router(http_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"]
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

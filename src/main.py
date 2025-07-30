from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.http import api_router, html_router

from contextlib import asynccontextmanager

from utils.logging import get_logger

from dotenv import load_dotenv

logger = get_logger()

load_dotenv()


app = FastAPI()
app.include_router(api_router)
app.include_router(html_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"]
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def get_index_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.jinja2",
        context={
            "yandex_api_key": os.getenv("YANDEX_API_KEY", ""),
            "server_host": os.getenv("SERVER_HOST") or "https://" + os.getenv("RAILWAY_PUBLIC_DOMAIN", "")
        }
    )

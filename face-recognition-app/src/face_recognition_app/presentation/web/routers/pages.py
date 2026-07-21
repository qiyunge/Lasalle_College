from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


WEB_DIRECTORY = Path(__file__).resolve().parents[1]
TEMPLATE_DIRECTORY = WEB_DIRECTORY / "templates"
STATIC_DIRECTORY = WEB_DIRECTORY / "static"

templates = Jinja2Templates(directory=TEMPLATE_DIRECTORY)
router = APIRouter(include_in_schema=False)


def _context(active_page: str) -> dict[str, str]:
    return {"active_page": active_page, "api_base_url": ""}


@router.get("/")
def camera_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="camera.html",
        context=_context("camera"),
    )


@router.get("/model")
def model_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="model.html",
        context=_context("model"),
    )


@router.get("/about")
def about_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context=_context("about"),
    )

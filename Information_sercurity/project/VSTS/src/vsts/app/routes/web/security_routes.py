from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse

from vsts.app import templates

router = APIRouter()

@router.get("/crypto", response_class=HTMLResponse ,name="crypto")
async def crypto_page(request: Request) -> HTMLResponse:
    """
    Placeholder page for crypto module.
    """
    return templates.TemplateResponse(
        request,
        "crypto.html",
        {
            "project_name": "Security Demo Platform",

        }
    )

@router.get("/signature", response_class=HTMLResponse, name="signature")
async def signature_page(request: Request) -> HTMLResponse:
    """
    Placeholder page for signature module.
    """
    return templates.TemplateResponse(
        request,
        "signature.html",
        {
             "project_name": "Security Demo Platform",


        }
    )


@router.get("/keys", response_class=HTMLResponse, name="keys")
async def keys_page(request: Request) -> HTMLResponse:
    """
    Placeholder page for key management module.
    """
    return templates.TemplateResponse(
        request,
        "keys.html",
        {
             "project_name": "Security Demo Platform",


        }
    )

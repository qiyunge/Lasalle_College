from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from vsts.app.web_config import templates

router = APIRouter()

features = [
     {
        "title": "Key Generation",
        "description": "Generate RSA public/private key pairs.",
        "endpoint": "keys",
        "icon": "🔑",
    },
    {
        "title": "Encryption / Decryption",
        "description": "Encrypt and decrypt messages securely.",
        "endpoint": "crypto",
        "icon": "🔐",
    },
    {
        "title": "Digital Signature",
        "description": "Sign messages and verify authenticity.",
        "endpoint": "signature",
        "icon": "✍️",
    },
   
    {
        "title": "API Docs",
        "description": "Test backend APIs with Swagger UI.",
        "endpoint": "swagger_ui_html",
        "icon": "📄",
    },
]

@router.get("/", response_class=HTMLResponse, name="home")
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "project_name": "Security Demo Platform",
            "project_subtitle": (
                "A FastAPI-based web application for encryption, "
                "digital signature, and key management demonstrations."
            ),
            "features": features,
        },
    )
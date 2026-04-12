from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()

@router.get("/health", name = "api_health_check")
async def health_check() -> JSONResponse:
    """
    API endpoint for health check.
    """
    return JSONResponse(content={"status": "ok",
                                 "services": "security-demo-platform",
                                 "version": "0.1.0",})
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


# --- Web Configuration ---
from vsts.app import STATIC_DIR
from vsts.app.routes import page_web_router
from vsts.app.routes import security_web_router 
# --- API Routes ---
from vsts.app.routes import system_api_router
from vsts.app.routes import crypto_api_router
from vsts.app.routes import signature_api_router
from vsts.app.routes import keys_gen_api_router


app = FastAPI(
    title="Security Demo Platform",
    description="A FastAPI-based web application for encryption, signature, and key management demonstrations.",
    version="0.1.0",
)


# Mount static files if the folder exists
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


app.include_router(
    router=page_web_router) 
app.include_router(
    router=security_web_router)
app.include_router(
    router=system_api_router, prefix="/api", tags=["System"])   
app.include_router(
    router=crypto_api_router, prefix="/api", tags=["Crypto"])
app.include_router(
    router=signature_api_router, prefix="/api", tags=["Signature"])
app.include_router(
    router=keys_gen_api_router, prefix="/api", tags=["Key Generation"]) 
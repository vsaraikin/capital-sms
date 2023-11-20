import colorama
import logging
from fastapi import FastAPI

from app.configs import settings
from app.routers import sms_handler
from app.logger import load_logger

colorama.init()

load_logger("logging.yaml")

logger = logging.getLogger(__name__)

app = FastAPI(debug=True)

app.include_router(sms_handler.router, prefix="/api", tags=["2FA Verification"])


@app.get("/")
async def root():
    return {"message": "2FA Verification Service is up and running!"}


@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }

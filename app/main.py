from fastapi import FastAPI
from routers import verification
import logging
from fastapi.logger import logger as fastapi_logger

from logging.config import dictConfig
from utils.logger import log_config

# Logging
dictConfig(log_config)
gunicorn_error_logger = logging.getLogger("gunicorn.error")
gunicorn_logger = logging.getLogger("gunicorn")
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers = gunicorn_error_logger.handlers

fastapi_logger.handlers = gunicorn_error_logger.handlers

if __name__ != "__main__":
    fastapi_logger.setLevel(gunicorn_logger.level)
else:
    fastapi_logger.setLevel(logging.DEBUG)

app = FastAPI(debug=True)

app.include_router(verification.router, prefix="/api", tags=["2FA Verification"])


@app.get("/")
async def root():
    return {"message": "2FA Verification Service is up and running!"}

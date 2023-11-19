import colorama
import logging
from fastapi import FastAPI
from routers import verification
from utils.logger import load_logger

colorama.init()

load_logger("logging.yaml")

logger = logging.getLogger(__name__)


app = FastAPI(debug=True)

app.include_router(verification.router, prefix="/api", tags=["2FA Verification"])


@app.get("/")
async def root():
    return {"message": "2FA Verification Service is up and running!"}

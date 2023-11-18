from fastapi import FastAPI
from app.routers import verification

app = FastAPI()

app.include_router(verification.router, prefix="/api", tags=["2FA Verification"])


@app.get("/")
async def root():
    return {"message": "2FA Verification Service is up and running!"}

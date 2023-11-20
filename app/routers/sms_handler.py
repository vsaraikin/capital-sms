import logging
from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse
import httpx

from models.checker import CheckCodeRequest
from models.verification import VerificationRequest
from vonage_custom.client import ClientV2

router = APIRouter()
vonage = ClientV2()

users_calls = {}  # TODO: some better user identification may be placed (e.g. DB)


logger = logging.getLogger(__name__)


@router.post("/verify")
async def request_verification(verification: VerificationRequest):
    """Send to client code for verification"""
    try:
        response = await vonage.send_message(
            {
                "locale": "es-es",  # optional TODO: some client preferences func may be placed (from DB)
                "channel_timeout": 300,  # optional
                "client_ref": "my-ref",  # optional
                "brand": "Capital.com",  # required
                "workflow": [{"channel": "sms", "to": verification.phone}],  # required
            }
        )
        if response.status_code == 202:  # vonage success
            logger.info(" /verify")
            request_id = response.json()["request_id"]
            users_calls[verification.phone] = request_id
            return JSONResponse(status_code=200, content=None)
        else:
            logger.error(f"Error /verify {response.status_code}")
            return JSONResponse(
                status_code=response.status_code, content={"message": response.json()}
            )
    except httpx.HTTPError as e:
        logger.error(f"/verify {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@router.post("/check")
async def check_code(data: CheckCodeRequest):
    """Check the code for its state"""
    try:
        response = await vonage.verify_message(users_calls[data.to], data.code)

        if response.status_code == 200:
            logger.info("/check")

            users_calls.pop(data.to)  # request completed => remove it
            return JSONResponse(status_code=200, content=None)
        else:
            logger.error(f"Error /check {response.status_code}")

            return JSONResponse(
                status_code=response.status_code,
                content={"Error from Vonage": response.json()},
            )

    except httpx.HTTPError as e:
        logger.error(f"/check {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

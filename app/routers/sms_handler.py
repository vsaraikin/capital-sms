import logging
from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse

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
        # TODO: additional phone verification, custom error for that
        response = await vonage.send_message(verification.phone)

        if response.status_code == 202:  # vonage success
            logger.info("/verify")

            # Add user's `request_id` to our storage
            request_id = response.json()["request_id"]
            users_calls[verification.phone] = request_id

            return JSONResponse(status_code=200, content=None)
        else:
            logger.error(f"/verify {response.json()}")

            # TODO: left `content` as not empty for debugging, should have unique pydantic model from vonage api
            return JSONResponse(
                status_code=response.status_code, content={"message": response.json()}
            )
    # TODO: add custom errors handlers
    except Exception as e:
        logger.error(f"/verify {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/check")
async def check_code(data: CheckCodeRequest):
    """Check the code for its state"""
    try:
        # TODO: validate user's request_id, add custom error for undefined request_id
        response = await vonage.verify_message(users_calls[data.to], data.code)

        if response.status_code == 200:
            logger.info("/check")

            users_calls.pop(data.to)  # request completed => remove it
            return JSONResponse(status_code=200, content=None)
        else:
            logger.error(f"/check {response.json()}")

            # TODO: left `content` as not empty for debugging, should have unique pydantic model from vonage api
            return JSONResponse(
                status_code=response.status_code,
                content={"Error from Vonage": response.json()},
            )

    # TODO: add custom errors handlers
    except Exception as e:
        logger.error(f"/check {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse
import httpx

from models.check_code import CheckCodeRequest
from models.verify import VerificationRequest
from vonage_custom.client import ClientV2

router = APIRouter()
vonage = ClientV2()


users_calls = {}


@router.post("/verify")
async def request_verification(verification: VerificationRequest):
    try:
        response = vonage.send_message(
            {
                "locale": "es-es",  # optional TODO: some client country func may be placed
                "channel_timeout": 300,  # optional
                "client_ref": "my-ref",  # optional
                "brand": "Capital.com",  # required
                "workflow": [
                    {"channel": "sms", "to": verification.to}  # required  # required
                ],
            }
        )
        if response.status_code == 202:  # vonage success
            request_id = response.json()["request_id"]
            users_calls[verification.to] = request_id
            return JSONResponse(status_code=200, content=None)
        else:
            return JSONResponse(
                status_code=404, content={"Error from Vonage": response.json()}
            )
    except httpx.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@router.post("/check/{request_id}")
async def check_code(data: CheckCodeRequest):
    # TODO: Identify user in other way
    try:
        response = vonage.verify_message(users_calls["48600756692"], data.code)

        if response.status_code == 200:
            del response["request_id"]  # remove request id
            return JSONResponse(status_code=200, content=response)
        else:
            del response["instance"]  # remove request id
            return JSONResponse(
                status_code=400, content={"Error from Vonage": response.json()}
            )

    except httpx.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

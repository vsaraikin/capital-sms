from pydantic import BaseModel, Field


class CheckCodeRequest(BaseModel):
    to: str  # phone number
    code: str = Field(..., min_length=4, max_length=10)


class CheckCodeResponse(BaseModel):
    request_id: str
    status: str

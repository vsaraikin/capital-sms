from pydantic import BaseModel
from typing import List


class VerificationResponse202(BaseModel):
    request_id: str
    check_url: str


class VerificationResponse409(BaseModel):
    title: str
    type: str
    detail: str
    instance: str
    request_id: str


class InvalidParameter(BaseModel):
    name: str
    reason: str


class VerificationResponse422(BaseModel):
    title: str
    type: str
    detail: str
    instance: str
    invalid_parameters: List[InvalidParameter]


class VerificationResponse429(BaseModel):
    title: str
    type: str
    detail: str
    instance: str


class CheckCodeResponse(BaseModel):
    request_id: str
    status: str

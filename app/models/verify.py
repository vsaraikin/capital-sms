from pydantic import BaseModel
from typing import List, Optional


class VerificationWorkflow(BaseModel):
    channel: str
    to: str


class VerificationRequestVonage(BaseModel):
    locale: Optional[str] = None
    channel_timeout: Optional[int] = None
    client_ref: Optional[str] = None
    code_length: Optional[int] = None
    code: Optional[str] = None
    brand: str
    workflow: List[VerificationWorkflow]


class VerificationRequest(BaseModel):
    to: str  # phone number


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

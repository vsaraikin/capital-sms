from pydantic import BaseModel


class VerificationRequest(BaseModel):
    to: str  # phone number

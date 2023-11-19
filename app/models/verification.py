from pydantic import BaseModel


class VerificationRequest(BaseModel):
    phone: str  # phone number

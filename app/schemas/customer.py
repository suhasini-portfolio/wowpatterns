"""
Customer Schemas
"""

from pydantic import BaseModel, EmailStr, Field

class CustomerRegisterRequest(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6)
    mobile_country_id: int
    mobile_country_code: int
    mobile: str = Field(..., min_length=10, max_length=15)

class CustomerResponse(BaseModel):
    customer_id: int
    customer_code: str
    full_name: str
    email: EmailStr

    model_config = {
        "from_attributes": True
    }

class CustomerLoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class CustomerProfileResponse(BaseModel):
    customer_id: int
    customer_code: str
    full_name: str
    email: EmailStr
    mobile_country_id: int | None = None
    mobile_country_code: int | None = None
    mobile: str | None = None
    is_active: bool

    class Config:
        from_attributes = True

class CustomerProfileUpdateRequest(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    mobile_country_id: int | None = None
    mobile_country_code: str | None = None
    mobile: str | None = Field(default=None, min_length=10, max_length=15)

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CustomerAddressCreate(BaseModel):
    customer_id: int
    full_name: str = Field(..., max_length=100)
    mobile_country_id: int
    mobile_country_code: int
    mobile: str = Field(..., max_length=15)
    email: str = Field(..., max_length=50)
    country_id: int
    state_id: int
    city_id: int
    zip_code: str = Field(..., max_length=20)
    landmark: str | None = Field(default=None, max_length=500)
    address: str
    is_default: bool = False
    is_active: bool = True


class CustomerAddressUpdate(BaseModel):
    full_name: str | None = Field(default=None, max_length=100)
    mobile_country_id: int | None = None
    mobile_country_code: int | None = None
    mobile: str | None = Field(default=None, max_length=15)
    email: str | None = Field(default=None, max_length=50)
    country_id: int | None = None
    state_id: int | None = None
    city_id: int | None = None
    zip_code: str | None = Field(default=None, max_length=20)
    landmark: str | None = Field(default=None, max_length=500)
    address: str | None = None
    is_default: bool | None = None
    is_active: bool | None = None


class CustomerAddressResponse(BaseModel):
    customer_address_id: int
    customer_id: int
    full_name: str
    mobile_country_id: int
    mobile_country_code: int
    mobile: str
    email: str
    country_id: int
    state_id: int
    city_id: int
    zip_code: str
    landmark: str | None
    address: str
    is_default: bool
    is_active: bool
    created_date: datetime
    updated_date: datetime | None

    model_config = ConfigDict(from_attributes=True)
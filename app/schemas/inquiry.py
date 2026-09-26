from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class InquiryCreate(BaseModel):
    name: str | None = Field(default=None, max_length=100)
    company: str | None = Field(default=None, max_length=100)
    country: str | None = Field(default=None, max_length=100)
    email: str | None = Field(default=None, max_length=100)
    mobile: str | None = Field(default=None, max_length=15)
    mobile_country_id: int | None = 0
    mobile_country_code: int | None = None

    product_id: int = 0
    inquiry_type: str = Field(default="G", max_length=5)
    message: str | None = None
    order_id: int = 0
    design: str | None = Field(default=None, max_length=250)
    note: str | None = None


class InquiryUpdate(BaseModel):
    name: str | None = Field(default=None, max_length=100)
    company: str | None = Field(default=None, max_length=100)
    country: str | None = Field(default=None, max_length=100)
    email: str | None = Field(default=None, max_length=100)
    mobile: str | None = Field(default=None, max_length=15)
    mobile_country_id: int | None = None
    mobile_country_code: int | None = None

    product_id: int | None = None
    inquiry_type: str | None = Field(default=None, max_length=5)
    message: str | None = None
    order_id: int | None = None
    design: str | None = Field(default=None, max_length=250)
    note: str | None = None


class InquiryResponse(BaseModel):
    inquiry_id: int
    name: str | None
    company: str | None
    country: str | None
    email: str | None
    mobile: str | None
    mobile_country_id: int | None
    mobile_country_code: int | None
    product_id: int
    inquiry_type: str
    message: str | None
    order_id: int
    design: str | None
    note: str | None
    created_by: int
    created_date: datetime

    model_config = ConfigDict(from_attributes=True)
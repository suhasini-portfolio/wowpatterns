from pydantic import BaseModel, ConfigDict, Field


class ShippingStatusCreate(BaseModel):
    shipping_status: str = Field(..., max_length=255)
    priority: int
    status: int = 1
    email_subject: str = Field(..., max_length=255)


class ShippingStatusUpdate(BaseModel):
    shipping_status: str | None = Field(default=None, max_length=255)
    priority: int | None = None
    status: int | None = None
    email_subject: str | None = Field(default=None, max_length=255)


class ShippingStatusResponse(BaseModel):
    shipping_status_id: int
    shipping_status: str
    priority: int
    status: int
    email_subject: str

    model_config = ConfigDict(from_attributes=True)
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class OrderShippingStatusCreate(BaseModel):
    order_id: int
    order_item_id: int
    shipping_status_id: int = 1
    messages: str | None = None


class OrderShippingStatusUpdate(BaseModel):
    shipping_status_id: int | None = None
    messages: str | None = None


class OrderShippingStatusResponse(BaseModel):
    order_shipping_status_id: int
    order_id: int
    order_item_id: int
    shipping_status_id: int
    messages: str | None
    updated_by: int
    created_by: int
    created_date: datetime
    updated_date: datetime | None

    model_config = ConfigDict(from_attributes=True)
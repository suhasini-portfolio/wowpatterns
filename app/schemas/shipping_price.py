from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ShippingPriceCreate(BaseModel):
    shipping_type: str | None = Field(default=None, max_length=20)
    country_id: int = 0
    shipping_amount: Decimal = Field(
        default=Decimal("0.00"),
        max_digits=10,
        decimal_places=2,
    )
    shipping_price: Decimal | None = Field(
        default=Decimal("0.00"),
        max_digits=10,
        decimal_places=2,
    )
    delivery_period: str | None = Field(default="", max_length=255)
    extra_item_price: Decimal | None = Field(
        default=Decimal("0.00"),
        max_digits=10,
        decimal_places=2,
    )


class ShippingPriceUpdate(BaseModel):
    shipping_type: str | None = Field(default=None, max_length=20)
    country_id: int | None = None
    shipping_amount: Decimal | None = Field(
        default=None,
        max_digits=10,
        decimal_places=2,
    )
    shipping_price: Decimal | None = Field(
        default=None,
        max_digits=10,
        decimal_places=2,
    )
    is_active: bool | None = None
    delivery_period: str | None = Field(default=None, max_length=255)
    extra_item_price: Decimal | None = Field(
        default=None,
        max_digits=10,
        decimal_places=2,
    )


class ShippingPriceResponse(BaseModel):
    shipping_price_id: int
    shipping_type: str | None
    country_id: int
    shipping_amount: Decimal
    shipping_price: Decimal | None
    is_active: bool | None
    delivery_period: str | None
    extra_item_price: Decimal | None
    created_by: int
    created_date: datetime | None
    updated_by: int
    updated_date: datetime | None

    model_config = ConfigDict(from_attributes=True)
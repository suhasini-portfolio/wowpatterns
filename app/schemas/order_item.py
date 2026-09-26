from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class OrderItemCreate(BaseModel):
    order_id: int
    product_id: int
    product_type: str = Field(..., max_length=5)
    fabric_product_id: int | None = 0
    quantity: int = Field(..., gt=0)
    price: float
    print_quality: str | None = Field(default=None, max_length=5)
    artist_commission_percentage: Decimal | None = Field(
        default=0,
        max_digits=8,
        decimal_places=0
    )
    artist_commission: Decimal | None = Field(
        default=0,
        max_digits=8,
        decimal_places=0
    )
    shipping_status_id: int = 1


class OrderItemUpdate(BaseModel):
    product_id: int | None = None
    product_type: str | None = Field(default=None, max_length=5)
    fabric_product_id: int | None = None
    quantity: int | None = Field(default=None, gt=0)
    price: float | None = None
    print_quality: str | None = Field(default=None, max_length=5)
    artist_commission_percentage: Decimal | None = Field(
        default=None,
        max_digits=8,
        decimal_places=0
    )
    artist_commission: Decimal | None = Field(
        default=None,
        max_digits=8,
        decimal_places=0
    )
    shipping_status_id: int | None = None


class OrderItemResponse(BaseModel):
    order_item_id: int
    order_id: int
    product_id: int
    product_type: str
    fabric_product_id: int | None
    quantity: int
    price: float
    print_quality: str | None
    artist_commission_percentage: Decimal | None
    artist_commission: Decimal | None
    shipping_status_id: int
    is_active: bool
    created_date: datetime
    updated_date: datetime | None

    model_config = ConfigDict(from_attributes=True)
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class OrderCreate(BaseModel):
    order_status: str = Field(..., max_length=50)

    total_price: float
    discount: float = 0.00
    gst_price: Decimal | None = Field(
        default=0.00,
        max_digits=8,
        decimal_places=2,
    )
    grand_total: float | None = 0.00

    shipping_full_name: str | None = Field(
        default=None,
        max_length=55,
    )
    shipping_mobile_country_id: int | None = None
    shipping_mobile_country_code: int | None = None
    shipping_mobile: str | None = Field(
        default=None,
        max_length=16,
    )

    shipping_country_id: int | None = 0
    shipping_state_id: int | None = 0
    shipping_city_id: int | None = 0

    shipping_zip_code: str | None = Field(
        default=None,
        max_length=20,
    )
    shipping_email: str | None = Field(
        default=None,
        max_length=50,
    )
    shipping_landmark: str | None = Field(
        default=None,
        max_length=500,
    )
    shipping_address: str | None = None

    order_type: str | None = Field(
        default="O",
        max_length=5,
    )


class OrderUpdate(BaseModel):
    order_status: str | None = Field(
        default=None,
        max_length=50,
    )

    discount: float | None = None
    gst_price: Decimal | None = Field(
        default=None,
        max_digits=8,
        decimal_places=2,
    )
    grand_total: float | None = None

    shipping_full_name: str | None = Field(
        default=None,
        max_length=55,
    )
    shipping_mobile_country_id: int | None = None
    shipping_mobile_country_code: int | None = None
    shipping_mobile: str | None = Field(
        default=None,
        max_length=16,
    )
    shipping_country_id: int | None = None
    shipping_state_id: int | None = None
    shipping_city_id: int | None = None
    shipping_zip_code: str | None = Field(
        default=None,
        max_length=20,
    )
    shipping_email: str | None = Field(
        default=None,
        max_length=50,
    )
    shipping_landmark: str | None = Field(
        default=None,
        max_length=500,
    )
    shipping_address: str | None = None

    is_cancelled: bool | None = None
    cancelled_reason: str | None = None

    order_type: str | None = Field(
        default=None,
        max_length=5,
    )


class OrderResponse(BaseModel):
    order_id: int
    customer_id: int
    order_status: str
    total_price: float
    discount: float
    gst_price: Decimal | None
    grand_total: float | None

    shipping_full_name: str | None
    shipping_mobile_country_id: int | None
    shipping_mobile_country_code: int | None
    shipping_mobile: str | None
    shipping_country_id: int | None
    shipping_state_id: int | None
    shipping_city_id: int | None
    shipping_zip_code: str | None
    shipping_email: str | None
    shipping_landmark: str | None
    shipping_address: str | None

    order_number: str | None
    token: str | None
    razorpay_payment_id: str | None

    is_cancelled: bool
    cancelled_by: str | None
    cancelled_by_user_id: int | None
    cancelled_date: datetime | None
    cancelled_reason: str | None

    is_cancelled_archive: bool
    is_cancellation_approved: bool
    cancellation_approved_by_user_id: int | None
    cancellation_approved_date: datetime | None

    is_refund_initiated: bool
    refund_initiated_by_user_id: int | None
    refund_amount: Decimal | None
    refund_initiated_date: datetime | None

    is_amount_refunded: bool
    refunded_date: datetime | None

    is_cancellation_rejected: bool
    cancellation_rejected_by_user_id: int | None
    cancellation_rejected_date: datetime | None

    shipping_price_id: int | None
    shipping_price: Decimal | None

    order_type: str | None
    invoice_number: str | None
    razor_status: str | None
    razor_updated_date: datetime | None

    created_date: datetime
    is_active: bool
    updated_date: datetime | None

    model_config = ConfigDict(from_attributes=True)
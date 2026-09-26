from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class RazorpayWebhookCreate(BaseModel):
    created_date: datetime | None = None
    status: bool | None = True
    webhook_signature: str | None = Field(default=None, max_length=2000)
    webhook_event: str | None = Field(default=None, max_length=50)
    razorpay_payment_id: str | None = Field(default=None, max_length=255)

    amount: Decimal = Field(
        default=Decimal("0.00"),
        max_digits=16,
        decimal_places=2
    )

    currency: str = Field(..., max_length=10)

    base_amount: Decimal | None = Field(
        default=Decimal("0.00"),
        max_digits=16,
        decimal_places=2
    )

    event_status: str | None = Field(default="", max_length=20)
    order_id: str | None = Field(default=None, max_length=100)
    ck_order_id: str | None = Field(default=None, max_length=50)

    is_captured: bool = False

    description: str | None = Field(default=None, max_length=255)

    event_created_at: datetime | None = None

    amount_refunded: Decimal | None = Field(
        default=Decimal("0.00"),
        max_digits=16,
        decimal_places=2
    )

    refund_status: str | None = Field(default=None, max_length=50)


class RazorpayWebhookUpdate(BaseModel):
    status: bool | None = None
    webhook_signature: str | None = Field(default=None, max_length=2000)
    webhook_event: str | None = Field(default=None, max_length=50)
    razorpay_payment_id: str | None = Field(default=None, max_length=255)

    amount: Decimal | None = Field(
        default=None,
        max_digits=16,
        decimal_places=2
    )

    currency: str | None = Field(default=None, max_length=10)

    base_amount: Decimal | None = Field(
        default=None,
        max_digits=16,
        decimal_places=2
    )

    event_status: str | None = Field(default=None, max_length=20)
    order_id: str | None = Field(default=None, max_length=100)
    ck_order_id: str | None = Field(default=None, max_length=50)

    is_captured: bool | None = None

    description: str | None = Field(default=None, max_length=255)

    event_created_at: datetime | None = None

    amount_refunded: Decimal | None = Field(
        default=None,
        max_digits=16,
        decimal_places=2
    )

    refund_status: str | None = Field(default=None, max_length=50)


class RazorpayWebhookResponse(BaseModel):
    razorpay_webhook_id: int
    created_date: datetime | None
    status: bool | None
    webhook_signature: str | None
    webhook_event: str | None
    razorpay_payment_id: str | None
    amount: Decimal
    currency: str
    base_amount: Decimal | None
    event_status: str | None
    order_id: str | None
    ck_order_id: str | None
    is_captured: bool
    description: str | None
    event_created_at: datetime | None
    amount_refunded: Decimal | None
    refund_status: str | None

    model_config = ConfigDict(from_attributes=True)
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Boolean, DateTime, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class RazorpayWebhook(Base):
    __tablename__ = "razorwebhooks"

    razorpay_webhook_id: Mapped[int] = mapped_column(
        "RazorpayWebhookID",
        Integer,
        primary_key=True,
        autoincrement=True
    )

    created_date: Mapped[datetime | None] = mapped_column(
        "CreatedDate",
        DateTime,
        nullable=True
    )

    status: Mapped[bool | None] = mapped_column(
        "Status",
        Boolean,
        nullable=True,
        default=True
    )

    webhook_signature: Mapped[str | None] = mapped_column(
        "WebhookSignature",
        String(2000),
        nullable=True
    )

    webhook_event: Mapped[str | None] = mapped_column(
        "WebhookEvent",
        String(50),
        nullable=True
    )

    razorpay_payment_id: Mapped[str | None] = mapped_column(
        "RazorpayPaymentID",
        String(255),
        nullable=True
    )

    amount: Mapped[Decimal] = mapped_column(
        "Amount",
        Numeric(16, 2),
        nullable=False,
        default=Decimal("0.00")
    )

    currency: Mapped[str] = mapped_column(
        "Currency",
        String(10),
        nullable=False
    )

    base_amount: Mapped[Decimal | None] = mapped_column(
        "BaseAmount",
        Numeric(16, 2),
        nullable=True,
        default=Decimal("0.00")
    )

    event_status: Mapped[str | None] = mapped_column(
        "EventStatus",
        String(20),
        nullable=True,
        default=""
    )

    order_id: Mapped[str | None] = mapped_column(
        "OrderID",
        String(100),
        nullable=True
    )

    ck_order_id: Mapped[str | None] = mapped_column(
        "CK_OrderID",
        String(50),
        nullable=True
    )

    is_captured: Mapped[bool] = mapped_column(
        "IsCaptured",
        Boolean,
        nullable=False,
        default=False
    )

    description: Mapped[str | None] = mapped_column(
        "Description",
        String(255),
        nullable=True
    )

    event_created_at: Mapped[datetime | None] = mapped_column(
        "EventCreatedAt",
        DateTime,
        nullable=True
    )

    amount_refunded: Mapped[Decimal | None] = mapped_column(
        "AmountRefunded",
        Numeric(16, 2),
        nullable=True,
        default=Decimal("0.00")
    )

    refund_status: Mapped[str | None] = mapped_column(
        "RefundStatus",
        String(50),
        nullable=True
    )
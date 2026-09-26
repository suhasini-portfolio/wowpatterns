from datetime import datetime
from decimal import Decimal

from sqlalchemy import Boolean, DateTime, Float, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(
        "OrderID", Integer, primary_key=True, autoincrement=True
    )

    customer_id: Mapped[int] = mapped_column(
        "CustomerID", Integer, nullable=False
    )

    order_status: Mapped[str] = mapped_column(
        "OrderStatus", String(50), nullable=False
    )

    total_price: Mapped[float] = mapped_column(
        "TotalPrice", Float, nullable=False
    )

    discount: Mapped[float] = mapped_column(
        "Discount", Float, nullable=False, default=0.00
    )

    gst_price: Mapped[Decimal | None] = mapped_column(
        "GSTPrice", Numeric(8, 2), nullable=True, default=0.00
    )

    grand_total: Mapped[float | None] = mapped_column(
        "GrandTotal", Float, nullable=True, default=0.00
    )

    shipping_full_name: Mapped[str | None] = mapped_column(
        "ShippingFullName", String(55), nullable=True
    )

    shipping_mobile_country_id: Mapped[int | None] = mapped_column(
        "ShippingMobileCountryID", Integer, nullable=True
    )

    shipping_mobile_country_code: Mapped[int | None] = mapped_column(
        "ShippingMobileCountryCode", Integer, nullable=True
    )

    shipping_mobile: Mapped[str | None] = mapped_column(
        "ShippingMobile", String(16), nullable=True
    )

    shipping_country_id: Mapped[int | None] = mapped_column(
        "ShippingCountryID", Integer, nullable=True, default=0
    )

    shipping_state_id: Mapped[int | None] = mapped_column(
        "ShippingStateID", Integer, nullable=True, default=0
    )

    shipping_city_id: Mapped[int | None] = mapped_column(
        "ShippingCityID", Integer, nullable=True, default=0
    )

    shipping_zip_code: Mapped[str | None] = mapped_column(
        "ShippingZipCode", String(20), nullable=True
    )

    shipping_email: Mapped[str | None] = mapped_column(
        "ShippingEmail", String(50), nullable=True
    )

    shipping_landmark: Mapped[str | None] = mapped_column(
        "ShippingLandmark", String(500), nullable=True
    )

    shipping_address: Mapped[str | None] = mapped_column(
        "ShippingAddress", Text, nullable=True
    )

    order_number: Mapped[str | None] = mapped_column(
        "OrderNumber", String(20), nullable=True, default=""
    )

    token: Mapped[str | None] = mapped_column(
        "Token", String(20), nullable=True, default=""
    )

    razorpay_payment_id: Mapped[str | None] = mapped_column(
        "RazorpayPaymentID", String(100), nullable=True, default=""
    )

    is_cancelled: Mapped[bool] = mapped_column(
        "IsCancelled", Boolean, nullable=False, default=False
    )

    cancelled_by: Mapped[str | None] = mapped_column(
        "CancelledBy", String(10), nullable=True, default=""
    )

    cancelled_by_user_id: Mapped[int | None] = mapped_column(
        "CancelledByUserID", Integer, nullable=True, default=0
    )

    cancelled_date: Mapped[datetime | None] = mapped_column(
        "CancelledDate", DateTime, nullable=True
    )

    cancelled_reason: Mapped[str | None] = mapped_column(
        "CancelledReason", Text, nullable=True
    )

    is_cancelled_archive: Mapped[bool] = mapped_column(
        "IsCancelledArchive", Boolean, nullable=False, default=False
    )

    is_cancellation_approved: Mapped[bool] = mapped_column(
        "IsCancellationApproved", Boolean, nullable=False, default=False
    )

    cancellation_approved_by_user_id: Mapped[int | None] = mapped_column(
        "CancellationApprovedByUserID", Integer, nullable=True, default=0
    )

    cancellation_approved_date: Mapped[datetime | None] = mapped_column(
        "CancellationApprovedDate", DateTime, nullable=True
    )

    is_refund_initiated: Mapped[bool] = mapped_column(
        "IsRefundInitiated", Boolean, nullable=False, default=False
    )

    refund_initiated_by_user_id: Mapped[int | None] = mapped_column(
        "RefundInitiatedByUserID", Integer, nullable=True, default=0
    )

    refund_amount: Mapped[Decimal | None] = mapped_column(
        "RefundAmount", Numeric(10, 2), nullable=True, default=0.00
    )

    refund_initiated_date: Mapped[datetime | None] = mapped_column(
        "RefundInitiatedDate", DateTime, nullable=True
    )

    is_amount_refunded: Mapped[bool] = mapped_column(
        "IsAmountRefunded", Boolean, nullable=False, default=False
    )

    refunded_date: Mapped[datetime | None] = mapped_column(
        "RefundedDate", DateTime, nullable=True
    )

    is_cancellation_rejected: Mapped[bool] = mapped_column(
        "IsCancellationRejected", Boolean, nullable=False, default=False
    )

    cancellation_rejected_by_user_id: Mapped[int | None] = mapped_column(
        "CancellationRejectedByUserID", Integer, nullable=True, default=0
    )

    cancellation_rejected_date: Mapped[datetime | None] = mapped_column(
        "CancellationRejectedDate", DateTime, nullable=True
    )

    shipping_price_id: Mapped[int | None] = mapped_column(
        "ShippingPriceID", Integer, nullable=True
    )

    shipping_price: Mapped[Decimal | None] = mapped_column(
        "ShippingPrice", Numeric(10, 2), nullable=True, default=0.00
    )

    order_type: Mapped[str | None] = mapped_column(
        "OrderType", String(5), nullable=True, default="O"
    )

    invoice_number: Mapped[str | None] = mapped_column(
        "InvoiceNumber", String(20), nullable=True
    )

    razor_status: Mapped[str | None] = mapped_column(
        "RazorStatus", String(100), nullable=True, default=""
    )

    razor_updated_date: Mapped[datetime | None] = mapped_column(
        "RazorUpdatedDate", DateTime, nullable=True
    )

    created_date: Mapped[datetime] = mapped_column(
        "CreatedDate", DateTime, nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        "IsActive", Boolean, nullable=False, default=True
    )

    updated_date: Mapped[datetime | None] = mapped_column(
        "UpdatedDate", DateTime, nullable=True
    )